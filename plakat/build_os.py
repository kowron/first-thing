# -*- coding: utf-8 -*-
# Strony „Kościec osiowy” (PAGE=kosciec) i „Połączenia i mechanika” (PAGE=mech) – plakat A0, styl jak plakat mięśni.
import os, re, json, sys
import html as html_mod
sys.path.insert(0, '/home/user/first-thing/plakat')
import oslib
from oslib import mk, lat, l3block, q, gnode, sub, dock, card_html, fig_css, find, walk, est_height

PAGE = os.environ.get('PAGE', 'mech')
K = float(os.environ.get('K', 1.0))
L3S = float(os.environ.get('L3S', 0.9))
PAGE_W, PAGE_H = float(os.environ.get('PW', 1189)), float(os.environ.get('PH', 841))
LAYOUT = os.environ.get('LAYOUT', PAGE)       # plik układu layout_<LAYOUT>.py (domyślnie jak PAGE)
DATA = os.environ.get('DATA', 'mech' if PAGE == 'mech' else 'kosciec')
oslib.FIGSCALE = float(os.environ.get('FIGSCALE', 1.0))
INNER_W = PAGE_W - 28
J = lambda n: json.load(open(f'/home/user/first-thing/plakat/{n}.json', encoding='utf-8')) if os.path.exists(f'/home/user/first-thing/plakat/{n}.json') else {'tree': []}
MISSING, USED = [], set()
PALETTE = ['purple', 'teal', 'coral', 'blue', 'pink', 'red', 'green', 'amber']

# ---------------------------------------------------------------- konfiguracja układu (uzupełniana po obejrzeniu treści)
# FIG: tytuł karty (lub jego początek) → lista rysunków;  WIDTH: tytuł grupy/karty → szerokość w mm;  MODE: tytuł grupy → 'row'/'list'
FIG = {}
GFIG = {}
WIDTH = {}
MODE = {}
COLOR = {}
SKIP = set()
MERGE = set()
GRID2 = {}      # tytuł grupy → tytuły dzieci w lewej kolumnie (wymuszony podział grid2)
ROWSPEC = {}    # tytuł grupy → [(szerokość, [tytuły dzieci w tej kolumnie]), ...]
FIGSCALE_FOR = oslib.FIGSCALE_FOR
exec(open(f'/home/user/first-thing/plakat/layout_{LAYOUT}.py', encoding='utf-8').read()) if os.path.exists(f'/home/user/first-thing/plakat/layout_{LAYOUT}.py') else None


MEAS_PATH = f"/home/user/first-thing/plakat/measure_{PAGE}_{K:g}_{oslib.FIGSCALE:g}.json"
MEAS = {}
if os.path.exists(MEAS_PATH) and not os.environ.get('MEASURE'):
    MEAS = {t: {int(w): h for w, h in v.items()} for t, v in json.load(open(MEAS_PATH, encoding='utf-8')).items()}


def h_card(c, w):
    v = MEAS.get(c['title'])
    if v:
        ws = sorted(v)
        if w <= ws[0]:
            return v[ws[0]] * (1 + (ws[0] - w) / ws[0] * 0.6)
        if w >= ws[-1]:
            return v[ws[-1]]
        for a, b in zip(ws, ws[1:]):
            if a <= w <= b:
                return v[a] + (v[b] - v[a]) * (w - a) / (b - a)
    return est_height(c, w, c.get('figs') or figs_for(c['title']), K)


def h_node(n, w):
    """Szacowana wysokość węzła (mm) przy szerokości w."""
    if n.get('title') in SKIP:
        return 0
    if n['type'] == 'card':
        return h_card(n, w)
    kids = [c for c in n.get('children', []) if c.get('title') not in SKIP]
    head = 20 * K + (8 * K if n.get('q') else 0)
    if n['title'] in MERGE:
        return head + sum(h_card(c, w) - 8 * K for c in kids)
    mode = lookup(MODE, n['title'], 'list')
    if mode == 'grid2':
        cw = (w - 7 * K) / 2
        hs = [h_node(c, cw) + 3 * K for c in kids]
        return head + 6 * K + _best_split(hs)[0]
    if mode in ('row', 'intro-row'):
        return head + 10 * K + max([h_node(c, w / max(1, len(kids))) for c in kids] or [0])
    return head + sum(h_node(c, w - 5 * K) + 3 * K for c in kids)


def _best_split(hs):
    """Podział listy wysokości na 2 kolumny: (maks. wysokość, [indeksy kol. 0], [indeksy kol. 1]).
    Najpierw próbuje podziału ciągłego (lewa kolumna = początek listy) – czyta się naturalnie."""
    best = None
    for i in range(1, len(hs)):
        m = max(sum(hs[:i]), sum(hs[i:]))
        if best is None or m < best[0]:
            best = (m, list(range(i)), list(range(i, len(hs))))
    if best is None:
        return (sum(hs), list(range(len(hs))), [])
    # zachłanny (przeplatany) – tylko jeśli wyraźnie lepszy
    a, b, sa, sb = [], [], 0.0, 0.0
    for i, h in enumerate(hs):
        if sa <= sb:
            a.append(i); sa += h
        else:
            b.append(i); sb += h
    if max(sa, sb) < best[0] * 0.93:
        return (max(sa, sb), a, b)
    return best


def figs_for(title):
    v = lookup(FIG, title)
    return v or []


def lookup(d, title, default=None):
    if title in d:
        return d[title]
    best = None
    for k in d:
        if title.startswith(k) and (best is None or len(k) > len(best)):
            best = k
    return d[best] if best is not None else default


def _cards_flat(node):
    for c in node.get('children', []):
        if c['type'] == 'card':
            yield c
        else:
            yield from _cards_flat(c)


def merged_card(node, col, width):
    """Grupa jako jedna karta: rysunki dzieci u góry, każda karta-dziecko jako pod-blok z tytułem."""
    kids = list(_cards_flat(node))
    figs = []
    for c in kids:
        figs += c.get('figs') or figs_for(c['title'])
    secs = []
    for c in kids:
        x = {'k': c['title'].upper(), 'items': []}
        body = ''.join(f'<div class="xrow"><div class="k">{mk(sc["k"])}</div><ul>' + ''.join(f'<li>{mk(i)}</li>' for i in sc.get('items', [])) + '</ul></div>'
                       for sc in c.get('sections', []))
        tag = f'<span class="tag">{mk(c["tag"])}</span>' if c.get('tag') else ''
        secs.append(f'<div class="sm mrg"><div class="sh"><span class="snm">{mk(c["title"])}</span> {lat(c.get("lat"), "slt")}{tag}'
                    + (f' <span class="l3pg">s.&nbsp;{c["pg"]}</span>' if c.get('pg') else '') + f'</div>{body}{l3block(c.get("l3", []))}</div>')
    pseudo = {'title': node['title'], 'lat': node.get('lat', ''), 'pg': node.get('pg', ''), 'sections': [], 'l3': node.get('l3', [])}
    return card_html(pseudo, col, width, figs, MISSING, K=K, extra_html=''.join(secs))


def render(node, width, col, depth, qc=None):
    """Zwraca HTML węzła (grupa → sub z dziećmi; karta → karta). qc – licznik pytań w rozdziale."""
    if node.get('title') in SKIP:
        return ''
    if node['type'] == 'card':
        figs = node.get('figs') or figs_for(node['title'])
        w = lookup(WIDTH, node['title'], width)
        return card_html(node, col, min(w, width), figs, MISSING, K=K)
    if qc is None:
        qc = [0]
    if node['title'] in MERGE:
        return merged_card(node, col, width)
    kids = [c for c in node.get('children', []) if c.get('title') not in SKIP]
    gf = lookup(GFIG, node['title'])          # rysunek zbiorczy dla grupy → karta-rysunek na początku
    if gf and not any(k.get('_gfig') for k in kids):
        cap, names = gf
        kids = [{'type': 'card', 'title': cap, 'sections': [], 'figs': names, '_gfig': True}] + kids
    mode = lookup(MODE, node['title'], 'list')
    kind = {0: 'chap', 1: 'world', 2: 'grp'}.get(depth, 'sg')
    gcol = lookup(COLOR, node['title'], 'c1') if kind == 'chap' else col
    head = gnode(node['title'], node.get('lat', ''), kind, gcol, node.get('why', ''), node.get('pg', ''), node.get('l3'))
    qh = ''
    if node.get('q') and kids:
        qc[0] += 1
        qh = q(str(qc[0]), node['q'], node.get('pg', '').split('–')[0].split(',')[0])
    if not kids:
        return sub(head, '', 'list', width=width, col=gcol)
    def kcol(i, c):
        if c.get('title') in COLOR:
            return COLOR[c['title']]
        return PALETTE[(i + 1) % len(PALETTE)] if depth == 0 else gcol
    sid = re.sub(r'\W+', '_', node['title'])[:30]
    if mode == 'grid2':
        gap = 7 * K
        cw = (width - gap) / 2
        forced = lookup(GRID2, node['title'])
        if forced:
            idx0 = [i for i, c in enumerate(kids) if c['title'] in forced]
            idx1 = [i for i in range(len(kids)) if i not in idx0]
        else:
            _, idx0, idx1 = _best_split([h_node(c, cw) + 3 * K for c in kids])
        cols = [[(i, kids[i]) for i in idx0], [(i, kids[i]) for i in idx1]]
        inner = ''.join(f'<div class="gcol" style="width:{cw:.2f}mm">' + ''.join(render(c, cw, kcol(i, c), depth + 1, qc) for i, c in col) + '</div>'
                        for col in cols)
        return sub(head, inner, 'grid2', qh, width=width, col=gcol, id=sid)
    pre = ''
    if mode == 'intro-row':
        pre = render(kids[0], width, kcol(0, kids[0]), depth + 1, qc)
        kids = kids[1:]
        mode = 'row'
    if mode == 'row' and node['title'] in ROWSPEC:
        parts = []
        byt = {c['title']: (i, c) for i, c in enumerate(kids)}
        for w, titles in ROWSPEC[node['title']]:
            grp = [byt[t] for t in titles if t in byt]
            if len(grp) == 1:
                i, c = grp[0]
                parts.append(render(c, w, kcol(i, c), depth + 1, qc))
            else:
                parts.append(f'<div class="kstack" style="width:{w}mm">' + ''.join(render(c, w, kcol(i, c), depth + 1, qc) for i, c in grp) + '</div>')
        return sub(head, ''.join(parts), 'row', qh, width=width, col=gcol, id=sid, pre=pre)
    if mode == 'row':
        ws = lookup(WIDTH, node['title'] + ' /kids')
        if not ws:
            gap = 7
            each = (width - gap * (len(kids) - 1)) / len(kids)
            ws = [each] * len(kids)
        parts, i = [], 0
        for w in ws:
            if isinstance(w, (list, tuple)):          # ('stack', szerokość, ile) – kilka grup jedna pod drugą w jednej kolumnie
                _, sw, n = w
                grp = kids[i:i + n]
                parts.append(f'<div class="kstack" style="width:{sw}mm">' + ''.join(render(c, sw, kcol(i + j, c), depth + 1, qc) for j, c in enumerate(grp)) + '</div>')
                i += n
            else:
                if i < len(kids):
                    parts.append(render(kids[i], w, kcol(i, kids[i]), depth + 1, qc))
                i += 1
        return sub(head, ''.join(parts), 'row', qh, width=width, col=gcol, id=sid, pre=pre)
    indent = 8.5 * K if qh else 5 * K
    inner = ''.join(render(c, width - indent, kcol(i, c), depth + 1, qc) for i, c in enumerate(kids))
    return sub(head, inner, 'list', qh, width=width, col=gcol, id=sid)


# ---------------------------------------------------------------- strony
def G(title, children, **kw):
    d = {'type': 'group', 'title': title, 'children': children}
    d.update(kw)
    return d

if DATA == 'mech':
    TITLE = globals().get('PAGE_TITLE') or 'Połączenia i mechanika szkieletu osiowego'
    SUBT = globals().get('PAGE_SUB') or 'połączenia kręgosłupa i klatki piersiowej · krzywizny · mechanika klatki · przepona i oddychanie'
    PJ, MJ, OJ = J('k_polaczenia')['tree'], J('k_mech')['tree'], J('k_oddychanie')['tree']
    pick = lambda tree, t: [n for n in tree if n['title'].startswith(t)]
    mech_nodes = MJ[0]['children'] if (len(MJ) == 1 and MJ[0]['type'] == 'group' and len(MJ[0].get('children', [])) >= 2 and not MJ[0]['title'].startswith('Krzywizny')) else MJ
    CHAPTERS = globals().get('CHAPTERS_DEF') or [
        (G('Kręgosłup', pick(PJ, 'Połączenia kręgów') + pick(PJ, 'Połączenia kości krzyżowej') + pick(mech_nodes, 'Krzywizny'),
           q='połączenia czy krzywizny?'), 'c1'),
        (G('Klatka piersiowa', pick(PJ, 'Połączenia żeber') + pick(mech_nodes, 'Mechanika klatki'), q='połączenia czy mechanika?'), 'c2'),
        (G('Oddychanie', OJ, q='przepona czy mechanika?'), 'c4'),
    ]
else:
    TITLE = globals().get('PAGE_TITLE') or 'Kościec osiowy'
    SUBT = globals().get('PAGE_SUB') or 'kręgosłup · żebra · mostek · klatka piersiowa'
    KJ, TJ = J('k_kregoslup')['tree'], J('k_klatka')['tree']
    CHAPTERS = globals().get('CHAPTERS_DEF') or [
        (KJ[0] if KJ else G('Kręgosłup', []), 'c1'),
        (TJ[0] if TJ else G('Klatka piersiowa', []), 'c2'),
    ]
if globals().get('CHAPTERS_FN'):
    CHAPTERS = CHAPTERS_FN({k: globals().get(k) for k in ('KJ', 'TJ', 'PJ', 'MJ', 'OJ', 'G', 'pick', 'mech_nodes', 'CHAPTERS')})
for hook in globals().get('PREPARE', []):
    hook(CHAPTERS)

if os.environ.get('MEASURE'):
    # tryb pomiaru: każda karta w kilku szerokościach → measure_<PAGE>.html (mierzy scripts/measure.py)
    WS = [int(x) for x in os.environ.get('MEASURE_WS', '110,130,150,170,190,220,250,280,320,380').split(',')]
    def all_cards(n, out):
        if n['type'] == 'card':
            out.append(n)
            return
        if n['title'] in MERGE:
            out.append(('MERGE', n))
            return
        gf = lookup(GFIG, n['title'])
        if gf:
            out.append({'type': 'card', 'title': gf[0], 'sections': [], 'figs': gf[1], '_gfig': True})
        for c in n.get('children', []):
            all_cards(c, out)
    cards = []
    for node, ccol in CHAPTERS:
        all_cards(node, cards)
    blocks = []
    for c in cards:
        for w in WS:
            if isinstance(c, tuple):
                h_ = merged_card(c[1], 'c1', w)
                t = c[1]['title']
            else:
                h_ = card_html(c, 'c1', w, c.get('figs') or figs_for(c['title']), MISSING, K=K)
                t = c['title']
            blocks.append(f'<div class="mbox" data-t="{html_mod.escape(t)}" data-w="{w}" style="display:inline-block;vertical-align:top;margin:2mm">{h_}</div>')
    CSS0 = open('/home/user/first-thing/plakat/style.css', encoding='utf-8').read()
    fr0, tr0 = CSS0.split('/*TREE*/')
    tr0 = re.sub(r'(?<![\w.#-])(\d*\.?\d+)(pt|mm|px)\b', lambda m: f"{float(m.group(1)) * K:.3f}".rstrip('0').rstrip('.') + m.group(2), tr0)
    open(f'/home/user/first-thing/plakat/measure_{PAGE}.html', 'w', encoding='utf-8').write(
        f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>:root {{ --l3s: {L3S}; }}\n{fr0}{tr0}\n{fig_css()}\n.poster{{width:auto;height:auto}}</style></head>'
        f'<body><div class="poster"><div class="treebox" style="position:relative">{"".join(blocks)}</div></div></body></html>')
    print('measure page', len(blocks))
    sys.exit(0)

CH_W = globals().get('CH_WIDTHS') or [INNER_W / len(CHAPTERS) - 12] * len(CHAPTERS)
chap_html = []
for (node, ccol), w in zip(CHAPTERS, CH_W):
    MODE.setdefault(node['title'], 'row' if len(node.get('children', [])) > 1 else 'list')
    COLOR.setdefault(node['title'], ccol)
    chap_html.append(render(node, w, ccol, 0))

ROOT = sub(gnode(TITLE, '', 'root', '', SUBT, ''), ''.join(chap_html), 'row', width=INNER_W, col='root')
INFO = f'''<div class="info"><div class="i1">PLAKAT DO NAUKI · ANATOMIA · SZKIELET OSIOWY</div>
<div class="i2">Wszystko wg: A. Bochenek, M. Reicher, <i>Anatomia człowieka</i>, t. I{globals().get('PAGES_NOTE', '')}</div>
<div class="i3">Poziom 1 – podział, poziom 2 – karty z rysunkami, poziom 3 – szczegóły małym drukiem.</div></div>'''
LEGEND = '''<div class="legend"><div class="lt1">JAK CZYTAĆ</div><div class="lgrid">
<div class="lrow"><span><span class="lpill">POZIOM 1</span></span><span><b>Z daleka:</b> sam podział – grupy i nazwy.</span></div>
<div class="lrow"><span><span class="lpill">POZIOM 2</span></span><span><b>Po przybliżeniu:</b> karty z rysunkami – cechy, budowa, opis.</span></div>
<div class="lrow"><span><span class="lpill">POZIOM 3</span></span><span><b>Duże przybliżenie:</b> małym drukiem w ramkach <span class="lz3">3</span> – szczegóły z Bochenka.</span></div>
<div class="lrow"><span><span class="lz">1</span></span><span>Pytanie przy rozgałęzieniu: według czego dzielimy.</span></div>
<div class="lrow"><span><span class="lsw">grupa</span></span><span>Przerywana ramka = grupa; pełna ramka = karta.</span></div>
<div class="lrow"><span class="lsm">nomen latinum</span><span>Łacina pogrubionych nazw – tak samo ważna jak polska.</span></div>
<div class="lrow"><span><span class="lw">!</span></span><span>Bochenek w różnych miejscach podaje coś innego.</span></div>
<div class="lrow"><span><span class="star">★</span></span><span>Temat wskazany jako ważny na zaliczeniu.</span></div>
<div class="lrow"><span class="lsm2">C · Th · L · S</span><span>Kręgi szyjne · piersiowe · lędźwiowe · krzyżowe.</span></div>
<div class="lrow"><span class="lsm2">I–XII</span><span>Numery żeber.</span></div>
</div></div>'''

CSS = open('/home/user/first-thing/plakat/style.css', encoding='utf-8').read()
CSS = CSS.replace('size: 1189mm 841mm', f'size: {PAGE_W:g}mm {PAGE_H:g}mm').replace(
    '.poster { width: 1189mm; height: 841mm;', f'.poster {{ width: {PAGE_W:g}mm; height: {PAGE_H:g}mm;')
frame, tree = CSS.split('/*TREE*/')
def scale(m):
    v = float(m.group(1)) * K
    return f'{v:.3f}'.rstrip('0').rstrip('.') + m.group(2)
tree = re.sub(r'(?<![\w.#-])(\d*\.?\d+)(pt|mm|px)\b', scale, tree)
CSS = frame + tree + '\n' + fig_css()
JS = open('/home/user/first-thing/plakat/wires.js', encoding='utf-8').read()
DOCKS = globals().get('DOCKS_HTML', '') or ''
html = f'''<!DOCTYPE html><html lang="pl"><head><meta charset="utf-8"><title>{TITLE} – plakat</title>
<style>:root {{ --l3s: {L3S}; }}\n{CSS}</style></head><body><div class="poster">{INFO}{LEGEND}<div class="treebox"><svg class="wires"></svg>{ROOT}{DOCKS}</div></div>
<script>window.POSTER_K = {K};</script><script>{JS}</script></body></html>'''
out = f'/home/user/first-thing/plakat/page_{PAGE}.html'
open(out, 'w', encoding='utf-8').write(html)
print('ok', out, len(html), '| brak rysunków:', len(MISSING), sorted(set(MISSING))[:40])
