# -*- coding: utf-8 -*-
# PLAKAT A0 (poziomo): Mięśnie szkieletu osiowego – podział + przyczepy (poziomy 1–2)
# Dane przyczepów: notatka „Mięśnie szkieletu osiowego wg Bochenka” (data.py, z Bochenka t. I)
import re, sys, copy
sys.path.insert(0, '/home/user/first-thing/plakat')
from data import GRZBIET, KLATKA, BRZUCH, SZYJA

def mk(t):
    t = t.replace('°', '<span class="deg">°</span>')
    t = re.sub(r'\[\[(.+?)\]\]', r'<span class="ls">(\1)</span>', t)
    return t

SHY = {'sternocleidomastoideus': 'sterno\u00adcleido\u00admastoideus'}
def lat(t, cls='lt'):
    if not t:
        return ''
    for a, b in SHY.items():
        t = t.replace(a, b)
    return f'<span class="{cls}">{mk(t)}</span>'

# ---------------------------------------------------------------- wyszukiwanie w danych
def walk(g):
    for it in g['items']:
        yield it
        if it['kind'] == 'g':
            yield from walk(it)

ALL = [GRZBIET, KLATKA, BRZUCH, SZYJA]
def M(pl):
    for ch in ALL:
        for it in walk(ch):
            if it['kind'] in ('m', 'ref') and it['pl'] == pl:
                return it
    raise KeyError(pl)

def G(title):
    for ch in ALL:
        for it in walk(ch):
            if it['kind'] == 'g' and it['title'] == title:
                return it
    raise KeyError(title)

# ---------------------------------------------------------------- elementy drzewa
def q(sym, txt, pg=''):
    p = f'<span class="qpg">s. {pg}</span>' if pg else ''
    return f'<div class="q"><span class="qn">{sym}</span><span class="qt">{txt}</span>{p}</div>'

def gnode(title, la='', kind='grp', col='', why='', pg=''):
    h = [f'<div class="node g {kind} {col}">']
    p = f'<span class="pg">s. {pg}</span>' if pg else ''
    h.append(f'<div class="hd"><span class="pl">{title}</span>{p}</div>')
    if la:
        h.append(f'<div class="gla">{mk(la)}</div>')
    if why:
        h.append(f'<div class="why">{mk(why)}</div>')
    h.append('</div>')
    return ''.join(h)

def sub(nodehtml, kids='', mode='list', qhtml='', width='', col='', extra=''):
    st = f'width:{width}mm;' if width else ''
    k = f'<div class="kids {mode}">{kids}</div>' if kids else ''
    cls = 'sub rowsub' if (mode == 'row' and kids) else ('sub hasq' if qhtml else 'sub')
    return f'<div class="{cls}" data-c="{col}" style="{st}">{nodehtml}{qhtml}{k}{extra}</div>'

def ol(items):
    if not items:
        return ''
    if len(items) == 1:
        return f'<div class="one">{mk(items[0])}</div>'
    return '<ol>' + ''.join(f'<li>{mk(x)}</li>' for x in items) + '</ol>'

def att(d, wide):
    o, i, a = d.get('o'), d.get('i'), d.get('att')
    if a:
        return f'<div class="att single"><div class="col"><div class="k">PRZYCZEPY</div>{ol(a)}</div></div>'
    if not (o or i):
        return ''
    om = f'<div class="omax">{d["omax"]}</div>' if d.get('omax') else ''
    arr = '<div class="arr">→</div>' if wide else ''
    return (f'<div class="att {"two" if wide else "stack"}">'
            f'<div class="col"><div class="k">PRZYCZEP POCZĄTKOWY</div>{ol(o)}{om}</div>{arr}'
            f'<div class="col"><div class="k">PRZYCZEP KOŃCOWY</div>{ol(i)}</div></div>')

def tags(d):
    t = ''
    if d.get('layer'):
        t += f'<span class="tag">{d["layer"]}</span>'
    if d.get('tag'):
        t += f'<span class="tag warm">{d["tag"]}</span>'
    return t

def card(m, col, wide=False, extra_rows=None, extra_warn=None, kids_html=''):
    if m['kind'] == 'ref':
        return (f'<div class="node card ref {col}"><div class="ch"><span class="nm">{m["pl"]}</span> {lat(m["lat"])}</div>'
                f'<div class="bd"><div class="note">{mk(m["txt"])} · <b>→ s. {m["pg"]}</b></div></div></div>')
    cls = f'node card {col}' + (' wide' if wide else '')
    h = [f'<div class="{cls}">']
    h.append(f'<div class="ch"><span class="nm">{m["pl"]}</span> {lat(m["lat"])}{tags(m)}</div>')
    h.append('<div class="bd">')
    h.append(f'<div class="pgl">Bochenek s. {m["pg"]}</div>')
    if m.get('note'):
        h.append(f'<div class="note">{mk(m["note"])}</div>')
    if m.get('parts'):
        h.append('<div class="parts"><span class="k">CZĘŚCI</span><ul>' + ''.join(f'<li>{mk(p)}</li>' for p in m['parts']) + '</ul></div>')
    h.append(att(m, wide))
    for s in m.get('sub', []):
        h.append(f'<div class="sm"><div class="sh"><span class="snm">{s["pl"]}</span> {lat(s["lat"], "slt")}{tags(s)}</div>{att(s, wide)}</div>')
    for (lab, items) in (extra_rows or []):
        h.append(f'<div class="xrow"><div class="k">{lab}</div><ul>' + ''.join(f'<li>{mk(x)}</li>' for x in items) + '</ul></div>')
    if m.get('f'):
        h.append('<div class="fn"><div class="k">CZYNNOŚĆ</div><ul>' + ''.join(f'<li>{mk(x)}</li>' for x in m['f']) + '</ul></div>')
    for (pl, la, txt) in m.get('extra', []):
        h.append(f'<div class="extra"><b>{pl}</b> {lat(la, "slt")} – {mk(txt)}</div>')
    for w in m.get('warn', []) + (extra_warn or []):
        h.append(f'<div class="warn"><span class="wi">!</span><span>{mk(w)}</span></div>')
    h.append('</div></div>')
    c = ''.join(h)
    if kids_html:
        return sub(c, kids_html, 'list', col=col)
    return c

def gfcard(g, col):
    return (f'<div class="node card gf {col}"><div class="ch"><span class="nm">{g["title"]} – czynność wspólna</span></div>'
            f'<div class="bd"><div class="pgl">Bochenek s. {g["groupf_pg"]}</div><div class="fn"><ul>' +
            ''.join(f'<li>{mk(x)}</li>' for x in g['groupf']) + '</ul></div></div></div>')

def cards(names, col, wide=False):
    return ''.join(card(M(n), col, wide) for n in names)

