# -*- coding: utf-8 -*-
"""Pomocnicze funkcje do stron „Kościec” i „Połączenia i mechanika” (ten sam styl co plakat mięśni)."""
import re, os, json, html

FIGDIR = '/home/user/first-thing/plakat/figs/out'


def mk(t):
    if t is None:
        return ''
    t = html.escape(t, quote=False) if '<' not in t else t
    t = t.replace('°', '<span class="deg">°</span>')
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'\{\{(.+?)\}\}', r'<span class="lti">\1</span>', t)
    t = re.sub(r'\[\[(.+?)\]\]', r'<span class="ls">(\1)</span>', t)
    return t


def lat(t, cls='lt'):
    return f'<span class="{cls}">{mk(t)}</span>' if t else ''


# ---------------------------------------------------------------- poziom 3
def _rows(items):
    rows = []
    for it in items:
        if rows and rows[-1][0] == it['k']:
            rows[-1][1].append(it)
        else:
            rows.append((it['k'], [it]))
    return rows


def l3rows(items):
    h = []
    for k, its in _rows(items):
        warn = (k.strip() == '!')
        lab = '<span class="wi">!</span> NIEZGODNOŚĆ W BOCHENKU' if warn else k
        if len(its) == 1 and not warn:
            x = its[0]
            pg = f' <span class="l3pg">s.&nbsp;{x["pg"]}</span>' if x.get('pg') else ''
            h.append(f'<div class="l3r one"><span class="l3k">{lab}</span> {mk(x["t"])}{pg}</div>')
            continue
        body = ''.join(f'<li>{mk(x["t"])}' + (f' <span class="l3pg">s.&nbsp;{x["pg"]}</span>' if x.get('pg') else '') + '</li>' for x in its)
        h.append(f'<div class="l3r{" l3w" if warn else ""}"><div class="l3k">{lab}</div><ul>{body}</ul></div>')
    return ''.join(h)


def l3block(items, cls='', title='SZCZEGÓŁY Z BOCHENKA'):
    if not items:
        return ''
    # „!” zawsze na końcu
    items = [i for i in items if i['k'].strip() != '!'] + [i for i in items if i['k'].strip() == '!']
    return f'<div class="l3 {cls}"><div class="l3h"><span class="l3n">3</span>{title}</div>{l3rows(items)}</div>'


# ---------------------------------------------------------------- drzewo
def q(sym, txt, pg=''):
    p = f'<span class="qpg">s. {pg}</span>' if pg else ''
    return f'<div class="q"><span class="qn">{sym}</span><span class="qt">{mk(txt)}</span>{p}</div>'


def gnode(title, la='', kind='grp', col='', why='', pg='', l3=None):
    h = [f'<div class="node g {kind} {col}">']
    p = f'<span class="pg">s. {pg}</span>' if pg else ''
    h.append(f'<div class="hd"><span class="pl">{mk(title)}</span>{p}</div>')
    if la:
        h.append(f'<div class="gla">{mk(la)}</div>')
    if why:
        h.append(f'<div class="why">{mk(why)}</div>')
    if l3:
        h.append(l3block(l3, 'ing'))
    h.append('</div>')
    return ''.join(h)


def sub(nodehtml, kids='', mode='list', qhtml='', width='', col='', extra='', id='', pre=''):
    st = f'width:{width}mm;' if width else ''
    k = f'<div class="kids {mode}">{kids}</div>' if kids else ''
    cls = 'sub rowsub' if (mode == 'row' and kids) else ('sub g2sub' if mode == 'grid2' else ('sub hasq' if qhtml else 'sub'))
    ida = f' id="{id}"' if id else ''
    pre = f'<div class="intro">{pre}</div>' if pre else ''
    return f'<div class="{cls}"{ida} data-c="{col}" style="{st}">{nodehtml}{pre}{qhtml}{k}{extra}</div>'


def dock(under, html_, gap=6):
    return f'<div class="dock" data-under="{under}" data-gap="{gap}">{html_}</div>' if html_ else ''


# ---------------------------------------------------------------- rysunki
def fig_svg(name):
    p = os.path.join(FIGDIR, name + '.svg')
    if not os.path.exists(p):
        return None, 0, 0
    s = open(p, encoding='utf-8').read()
    m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', s)
    w, h = (float(m.group(1)), float(m.group(2))) if m else (0, 0)
    # style rysunków są wspólne i dodawane raz do strony (z przedrostkiem .figsvg) – tu usuwamy lokalne <style>
    s = re.sub(r'<style>.*?</style>', '', s, flags=re.S)
    s = s.replace('<svg ', '<svg class="figsvg" ', 1)
    # markery strzałek (#ah, #ah2) są identyczne we wszystkich rysunkach – powtórzone id nie przeszkadzają
    return s, w, h


FIGSCALE = 1.0      # globalna skala rysunków (ustawiana przez build_os.py)
FIGSCALE_FOR = {}   # skala dla pojedynczych rysunków (nazwa → skala), np. większe rysunki przepony


def figs_html(names, missing, maxw=None):
    """Zwraca (html, szer_kolumny, wys_łączna, układ) – rysunki przeskalowane do maxw (mm)."""
    items = []
    for n in names:
        s, w, h = fig_svg(n)
        if s is None:
            missing.append(n)
            pw = min(150 * FIGSCALE, maxw or 1e9)
            ph = 78 * FIGSCALE * pw / (150 * FIGSCALE)
            items.append((f'<div class="figmiss" style="width:{pw:.1f}mm;height:{ph:.1f}mm">[rysunek: {n}]</div>', pw, ph))
            continue
        sc = FIGSCALE_FOR.get(n, FIGSCALE)
        if maxw and w * sc > maxw:
            sc = maxw / w
        W, H = w * sc, h * sc
        s = re.sub(r'width="[\d.]+mm" height="[\d.]+mm"', f'width="{W:.2f}mm" height="{H:.2f}mm"', s, count=1)
        items.append((f'<div class="fig">{s}</div>', W, H))
    if not items:
        return '', 0, 0, 'col'
    tot_w = sum(i[1] for i in items) + 2 * (len(items) - 1)
    if maxw and len(items) > 1 and tot_w <= maxw:
        return ''.join(i[0] for i in items), tot_w, max(i[2] for i in items), 'row'
    return ''.join(i[0] for i in items), max(i[1] for i in items), sum(i[2] for i in items) + 1.5 * (len(items) - 1), 'col'


# ---------------------------------------------------------------- karta z JSON
def card_html(c, col, width, figs=(), missing=None, layout='auto', extra_html='', K=1.0):
    """c – węzeł 'card' z JSON; width – szerokość karty w mm (już po skali K)."""
    missing = missing if missing is not None else []
    tag = f'<span class="tag">{mk(c["tag"])}</span>' if c.get('tag') else ''
    cpg = f'<span class="cpg">s.&nbsp;{c["pg"]}</span>' if c.get('pg') else ''
    h = [f'<div class="node card osc {col}" style="width:{width:.2f}mm">',
         f'<div class="ch">{cpg}<span class="nm">{mk(c["title"])}</span> {lat(c.get("lat"))}{tag}</div><div class="bd">']
    secs = ''.join(f'<div class="xrow"><div class="k">{mk(s["k"])}</div><ul>' + ''.join(f'<li>{mk(i)}</li>' for i in s.get('items', [])) + '</ul></div>'
                   for s in c.get('sections', []))
    if c.get('timeline'):
        secs += '<div class="xrow tl"><div class="k">OŚ CZASU</div><ol class="tline">' + ''.join(
            f'<li><b>{mk(t["age"])}</b> – {mk(t["t"])}' + (f' <span class="l3pg">s.&nbsp;{t["pg"]}</span>' if t.get('pg') else '') + '</li>'
            for t in c['timeline']) + '</ol></div>'
    secs += extra_html
    inner_w = width - 6.5 * K
    nchar = sum(len(i) for s in c.get('sections', []) for i in s.get('items', [])) + len(re.sub(r'<[^>]+>', '', extra_html))
    # układ: rysunek z lewej (gdy obok zmieści się kolumna tekstu ≥ 70 mm), inaczej rysunki u góry
    fh, fw, fhh, farr = figs_html(list(figs), missing, inner_w)
    if fh and layout == 'auto':
        layout = 'left' if (inner_w - fw >= 72 * K and nchar > 250) else 'top'
    if fh and layout == 'left':
        fh, fw, fhh, farr = figs_html(list(figs), missing, inner_w - 72 * K)
        tw = inner_w - fw
        cols = ' secs3' if tw >= 330 * K else (' secs2' if tw >= 160 * K and nchar > 500 else '')
        h.append(f'<div class="figleft" style="grid-template-columns:{fw:.2f}mm 1fr"><div class="figs {farr}">{fh}</div><div class="secs{cols}">{secs}</div></div>')
    elif fh:
        cols = ' secs2' if inner_w >= 150 * K and nchar > 500 else ''
        h.append(f'<div class="figs top {farr}">{fh}</div><div class="secs{cols}">{secs}</div>')
    else:
        cols = ' secs2' if inner_w >= 150 * K and nchar > 400 else ''
        h.append(f'<div class="secs{cols}">{secs}</div>')
    h.append(l3block(c.get('l3', [])))
    h.append('</div></div>')
    return ''.join(h)


def est_height(c, width, figs, K=1.0):
    """Zgrubna wysokość karty (mm) – do równoważenia kolumn."""
    fhh = 0
    for n in figs:
        s, w, hh = fig_svg(n)
        if s:
            sc = min(FIGSCALE_FOR.get(n, FIGSCALE), (width - 6) / w) if w else 1
            fhh += hh * sc
    nchar = sum(len(i) for s in c.get('sections', []) for i in s.get('items', [])) + 60 * len(c.get('sections', []))
    l3c = sum(len(x['t']) for x in c.get('l3', []))
    cpl = (width - 8) / (1.32 * K)
    return 14 * K + fhh + nchar / cpl * 3.3 * K + l3c / (cpl * 2.1) * 1.6 * K


def find(tree, title):
    """Szuka węzła (grupy lub karty) po tytule (dokładnie albo początek)."""
    for n in tree:
        if n.get('title') == title or n.get('title', '').startswith(title):
            return n
        r = find(n.get('children', []), title)
        if r:
            return r
    return None


def walk(tree):
    for n in tree:
        yield n
        yield from walk(n.get('children', []))


def fig_css():
    """Style figlib z przedrostkiem .figsvg (żeby nie kolidowały z klasami plakatu)."""
    import sys
    sys.path.insert(0, '/home/user/first-thing/plakat/figs')
    from figlib import STYLE
    out = []
    for rule in STYLE.strip().split('}'):
        if '{' not in rule:
            continue
        sel, body = rule.split('{', 1)
        sels = ','.join('.figsvg ' + x.strip() for x in sel.split(','))
        out.append(f'{sels}{{{body}}}')
    # markery strzałek mają osobne id dla każdego rysunku – reguła marker-end musi wskazać właściwy (patrz fig_svg)
    return '\n'.join(out)
