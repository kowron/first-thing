# -*- coding: utf-8 -*-
# PLAKAT A0 (poziomo): Mięśnie szkieletu osiowego – podział + przyczepy (poziomy 1–2)
# Dane przyczepów: notatka „Mięśnie szkieletu osiowego wg Bochenka” (data.py, z Bochenka t. I)
import re, sys, copy
sys.path.insert(0, '/home/user/first-thing/plakat')
from data import GRZBIET, KLATKA, BRZUCH, SZYJA

def mk(t):
    t = t.replace('°', '<span class="deg">°</span>')
    t = re.sub(r'\[\[(.+?)\]\]', r'<span class="ls">(\1)</span>', t)
    t = re.sub(r'\{\{(.+?)\}\}', r'<span class="lti">\1</span>', t)
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

# ---------------------------------------------------------------- poziom ③ (szczegóły z Bochenka, pliki l3_*.json)
import json, os
sys.path.insert(0, '/home/user/first-thing/plakat')
from oslib import EXPL, expl_html            # wyjaśnienia „★ W SKRÓCIE” (explain_*.json)
L3M, L3G, L3P = {}, {}, {}
for _ch in ('grzbiet', 'klatka', 'brzuch'):
    _f = os.path.join(os.environ.get('L3DIR', '/home/user/first-thing/plakat'), f'l3_{_ch}.json')
    if os.path.exists(_f):
        _d = json.load(open(_f, encoding='utf-8'))
        L3M.update(_d.get('muscles', {}))
        L3G.update(_d.get('groups', {}))
        for _p in _d.get('panels', []):
            L3P[_p['id']] = _p
# --- mięśnie głębokie grzbietu: na zaliczeniu wystarczy je WYMIENIĆ (bez przyczepów, czynności i przebiegu); pełne opisy zostają
#     przy prostowniku grzbietu (m. krzyżowo-grzbietowy), mm. dźwigaczach żeber (oddychanie) i wszystkich mięśniach powierzchownych
STAR_M = {'mm. międzyżebrowe zewnętrzne', 'mm. międzyżebrowe wewnętrzne', 'mm. podżebrowe', 'm. poprzeczny klatki piersiowej',
          'm. piersiowy większy', 'm. piersiowy mniejszy', 'm. podobojczykowy', 'm. zębaty przedni', 'm. najszerszy grzbietu',
          'm. zębaty tylny górny', 'm. zębaty tylny dolny', 'mm. dźwigacze żeber', 'm. skośny zewnętrzny brzucha',
          'm. skośny wewnętrzny brzucha', 'm. poprzeczny brzucha', 'm. prosty brzucha'}     # ★ tematy wskazane jako ważne na zaliczeniu
STAR_P = {'tlocznia', 'pochewka', 'powiez_poprzeczna', 'kanal'}
NAMES_ONLY = ['m. płatowaty głowy', 'm. płatowaty szyi', 'm. kolcowy', 'm. półkolcowy klatki piersiowej i szyi', 'm. półkolcowy głowy',
              'm. wielodzielny', 'mm. skręcające', 'mm. międzykolcowe', 'mm. międzypoprzeczne', 'm. skośny górny głowy',
              'm. prosty tylny mniejszy głowy', 'm. prosty tylny większy głowy', 'm. skośny dolny głowy', 'm. prosty boczny głowy']
for _m in NAMES_ONLY:
    L3M.pop(_m, None)
for _g in ('Mięśnie kolcowo-poprzeczne', 'Mięśnie poprzeczno-kolcowe', 'Krótkie mięśnie grzbietu', 'Mięśnie podpotyliczne'):
    L3G.pop(_g, None)
USED_M, USED_G, USED_P = set(), set(), set()

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
            h.append(f'<div class="l3r one"><span class="l3k">{lab}</span> {mk(x["t"])} <span class="l3pg">s.&nbsp;{x["pg"]}</span></div>')
            continue
        body = ''.join(f'<li>{mk(x["t"])} <span class="l3pg">s.&nbsp;{x["pg"]}</span></li>' for x in its)
        h.append(f'<div class="l3r{" l3w" if warn else ""}"><div class="l3k">{lab}</div><ul>{body}</ul></div>')
    return ''.join(h)

L3ORDER = ['BUDOWA', 'POŁOŻENIE', 'PRZYCZEPY – UZUPEŁNIENIE', 'CZYNNOŚĆ – SZCZEGÓŁY', 'UNERWIENIE', 'ODMIANY', 'UWAGI']
def l3sorted(items):
    def key(it):
        k = it['k'].strip()
        if k == '!':
            return len(L3ORDER) + 1
        return L3ORDER.index(k) if k in L3ORDER else len(L3ORDER)
    return sorted(items, key=key)        # sortowanie stabilne – kolejność w obrębie kategorii zostaje

def l3block(items, cls=''):
    if not items:
        return ''
    return f'<div class="l3 {cls}"><div class="l3h"><span class="l3n">3</span>SZCZEGÓŁY Z BOCHENKA</div>{l3rows(l3sorted(items))}</div>'

def l3panel(pid, col):
    p = L3P.get(pid)
    if not p:
        return ''
    USED_P.add(pid)
    la = f' {lat(p["lat"])}' if p.get('lat') else ''
    return (f'<div class="panel l3panel {"starp " if pid in STAR_P else ""}{col}"><div class="ph"><span class="l3n big">3</span><span class="pt">{"<span class=star>★</span> " if pid in STAR_P else ""}{p["title"]}</span>{la}'
            f'<span class="pg">Bochenek s. {p["pg"]}</span></div>{expl_html(pid, 400) if pid in EXPL else ""}<div class="l3 inpanel">{l3rows(p["items"])}</div></div>')

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
    if title in L3G:
        USED_G.add(title)
        h.append(l3block(L3G[title], 'ing'))
    h.append('</div>')
    return ''.join(h)

def sub(nodehtml, kids='', mode='list', qhtml='', width='', col='', extra='', id=''):
    st = f'width:{width}mm;' if width else ''
    k = f'<div class="kids {mode}">{kids}</div>' if kids else ''
    cls = 'sub rowsub' if (mode == 'row' and kids) else ('sub hasq' if qhtml else 'sub')
    ida = f' id="{id}"' if id else ''
    return f'<div class="{cls}"{ida} data-c="{col}" style="{st}">{nodehtml}{qhtml}{k}{extra}</div>'

def dock(under, html, gap=6, cols=1):
    c = f' cols{cols}' if cols > 1 else ''
    return f'<div class="dock{c}" data-under="{under}" data-gap="{gap}">{html}</div>' if html else ''

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
    m = trim(m)
    cls = f'node card {col}' + (' wide' if wide else '')
    h = [f'<div class="{cls}">']
    h.append(f'<div class="ch"><span class="nm">{"<span class=star>★</span> " if m["pl"] in STAR_M else ""}{m["pl"]}</span> {lat(m["lat"])}{tags(m)}</div>')
    h.append('<div class="bd">')
    h.append(f'<div class="pgl">Bochenek s. {m["pg"]}</div>')
    if m['pl'] in EXPL:
        h.append(expl_html(m['pl'], 300))
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
    if m['pl'] in L3M:
        USED_M.add(m['pl'])
        h.append(l3block(L3M[m['pl']], 'big' if m['pl'] in STAR_M else ''))
    h.append('</div></div>')
    c = ''.join(h)
    if kids_html:
        return sub(c, kids_html, 'list', col=col)
    return c

def gfcard(g, col):
    return (f'<div class="node card gf {col}"><div class="ch"><span class="nm">{g["title"]} – czynność wspólna</span></div>'
            f'<div class="bd"><div class="pgl">Bochenek s. {g["groupf_pg"]}</div><div class="fn"><ul>' +
            ''.join(f'<li>{mk(x)}</li>' for x in g['groupf']) + '</ul></div></div></div>')

# wiersze kart, które po wstawieniu rozbudowanej sekcji ★ (explain_*.json) są zbędne (indeksy w listach; ujemne = od końca)
TRIM = {
    'mm. międzyżebrowe zewnętrzne': {'note': True, 'f': [0, 1]},
    'mm. międzyżebrowe wewnętrzne': {'note': True, 'parts': [0, 1], 'f': [0]},
    'mm. podżebrowe': {'f': [0]},
    'm. poprzeczny klatki piersiowej': {'f': [0, 1]},
    'mm. dźwigacze żeber': {'note': True, 'parts': [0, 1], 'f': [0, 1]},
    'm. zębaty tylny górny': {'f': [0], 'warn': [0]},
    'm. zębaty tylny dolny': {'f': [0], 'warn': [0]},
    'm. piersiowy większy': {'f': [2, 3]},
    'm. najszerszy grzbietu': {'f': [2, 3]},
    'm. piersiowy mniejszy': {'f': [-1], 'warn': [0]},
    'm. zębaty przedni': {'f': [-1], 'note': True},
}
def trim(m):
    spec = TRIM.get(m['pl'])
    if not spec or m['pl'] not in EXPL:
        return m
    m = copy.deepcopy(m)
    for k, v in spec.items():
        if v is True:
            m.pop(k, None)
        elif m.get(k):
            n = len(m[k]); drop = {i % n for i in v if -n <= i < n}
            m[k] = [x for j, x in enumerate(m[k]) if j not in drop]
    return m

def bare(n):
    """Mięsień z pełnym PODZIAŁEM (części, warstwa), ale bez cech: przyczepów, czynności, przebiegu i uwag."""
    m = copy.deepcopy(M(n))
    for k in ('o', 'i', 'att', 'omax', 'f', 'note', 'extra', 'warn'):
        m.pop(k, None)
    for sm in m.get('sub', []):
        for k in ('o', 'i', 'att', 'omax', 'f', 'note', 'extra', 'warn'):
            sm.pop(k, None)
    return m

def barecards(names, col):
    return ''.join(card(bare(n), col, True) for n in names)

def namecard(names, col, wide=True):
    """Karta z samymi nazwami mięśni (PL + łacina) – dla mięśni, które trzeba tylko umieć wymienić."""
    ms = [M(n) for n in names]
    pgs = sorted({m['pg'] for m in ms}, key=lambda x: int(re.match(r'\d+', x).group()))
    rows = ''.join(f'<li><b>{m["pl"]}</b> {lat(m["lat"])}</li>' for m in ms)
    return (f'<div class="node card {col} namecard"><div class="bd"><div class="pgl">Bochenek s. {", ".join(pgs)}</div>'
            f'<div class="nlk">TYLKO WYMIENIĆ</div><ul class="nlist">{rows}</ul></div></div>')

def cards(names, col, wide=False):
    return ''.join(card(M(n), col, wide) for n in names)

# ======================================================================
# SKALA I SZEROKOŚCI (do strojenia: zmienne środowiskowe K=..., W_<klucz>=..., PAGE=szer x wys w mm)
# ======================================================================
K = float(os.environ.get('K', 1.0))
W = dict(pow=146, band=132, krot=74, podp=74, kpow=72, kgleb=72, kprz=98, bbocz=92, bprzed=89, btyl=89)
L3S = float(os.environ.get('L3S', 0.9))
for _k in W:
    if os.environ.get('W_' + _k):
        W[_k] = float(os.environ['W_' + _k])
GAP = float(os.environ.get('GAP', 7))
PAGE_W, PAGE_H = [float(x) for x in os.environ.get('PAGE', '1189x841').split('x')]
INNER_W = PAGE_W - 28
LEGEND_AT = os.environ.get('LEGEND', 'top')      # top | grzbiet | klatka | brzuch

W['dlugie'] = 2 * W['band'] + GAP
W['gleb'] = W['dlugie'] + W['krot'] + W['podp'] + 2 * GAP
W['grz'] = W['pow'] + W['gleb'] + GAP + 3
W['kwrap'] = W['kgleb'] + W['kprz'] + GAP
W['kl'] = W['kpow'] + W['kwrap'] + GAP + 1
W['bbp'] = W['bbocz'] + W['bprzed'] + GAP
W['brz'] = W['bbp'] + W['btyl'] + GAP + 1
REGIONS = [x for x in os.environ.get('REGIONS', 'grzbiet,klatka,brzuch').split(',') if x]
_wsum = sum(W[{'grzbiet': 'grz', 'klatka': 'kl', 'brzuch': 'brz'}[r]] for r in REGIONS)
REST = INNER_W - _wsum - 7 * (len(REGIONS) - 1)
print('szerokości: grzbiet %.0f, klatka %.0f, brzuch %.0f | wybrane %s: zapas %.0f mm' % (W['grz'], W['kl'], W['brz'], ','.join(REGIONS), REST))
assert REST >= 0, 'za szeroko'

# ======================================================================
# I. GRZBIET
# ======================================================================
PU, TE, CO, BL, PK, RE, GN, AM = 'purple', 'teal', 'coral', 'blue', 'pink', 'red', 'green', 'amber'

g_ram = sub(gnode('Mięśnie kolcowo-ramienne', 'mm. spinohumerales', 'grp', PU, 'do łopatki i k. ramiennej', '650'),
            cards(['m. czworoboczny', 'm. najszerszy grzbietu', 'm. równoległoboczny', 'dźwigacz łopatki'], PU, True),
            'list', col=PU)
g_zeb = sub(gnode('Mięśnie kolcowo-żebrowe', 'mm. spinocostales', 'grp', PU, 'do żeber', '658'),
            cards(['m. zębaty tylny górny', 'm. zębaty tylny dolny'], PU, True),
            'list', col=PU)
POW_G = sub(gnode('Powierzchowne mięśnie grzbietu', '', 'world', PU,
                  'głównie mm. kończyny górnej, które przewędrowały na grzbiet · gałęzie przednie nn. rdzeniowych', '649–650'),
            g_ram + g_zeb, 'list', q('2', 'do czego dochodzą?', '650'), width=W['pow'], col=PU, id='pow')

kp = sub(gnode('Mięśnie kolcowo-poprzeczne', 'm. spinotransversalis', 'sg', TE, 'od wyr. kolczystych do poprzecznych', '659'),
         barecards(['m. płatowaty głowy', 'm. płatowaty szyi'], TE), 'list', col=TE)
kg_card = card(M('m. krzyżowo-grzbietowy – wspólny początek'), TE, True,
               kids_html=card(M('m. biodrowo-żebrowy'), TE, True) + card(M('m. najdłuższy'), TE, True))
kg = sub(gnode('Mięsień krzyżowo-grzbietowy', 'm. sacrospinalis', 'sg', TE, 'wspólny pień – wyżej dwa mięśnie; razem prostownik grzbietu', '660–665'),
         kg_card, 'list', col=TE)
p_boczne = sub(gnode('pasmo boczne', '', 'band', TE, 'włókna do wyr. poprzecznych i żeber', '659'),
               kp + kg, 'list', width=W['band'], col=TE, id='pbocz')

pk = sub(gnode('Mięśnie poprzeczno-kolcowe', 'mm. transversospinales', 'sg', CO, '3 warstwy – coraz krótsze w głąb', '667'),
         barecards(['m. półkolcowy klatki piersiowej i szyi', 'm. półkolcowy głowy', 'm. wielodzielny', 'mm. skręcające'], CO),
         'list', col=CO)
kol = sub(gnode('Mięsień kolcowy', 'm. spinalis', 'sg', CO, 'po wyrostkach kolczystych', '667'),
          barecards(['m. kolcowy'], CO), 'list', col=CO)
p_przysr = sub(gnode('pasmo przyśrodkowe', '', 'band', CO, 'włókna do wyr. kolczystych', '659'),
               kol + pk, 'list', width=W['band'], col=CO, id='pprzy')

DLUGIE = sub(gnode('Długie mięśnie grzbietu', '', 'grp', TE, 'włókna biegną przez wiele kręgów', '659'),
             p_boczne + p_przysr, 'row', q('4', 'do których wyrostków biegną włókna?', '659'), width=W['dlugie'], col=TE, id='dlugie')
KROTKIE = sub(gnode('Krótkie mięśnie grzbietu', '', 'grp', BL, 'między dwoma sąsiednimi kręgami', '669'),
              barecards(['mm. międzykolcowe', 'mm. międzypoprzeczne'], BL) + cards(['mm. dźwigacze żeber'], BL), 'list', width=W['krot'], col=BL, id='krot')
PODPOT = sub(gnode('Mięśnie podpotyliczne', 'mm. suboccipitales', 'grp', PK, 'potylica ↔ dwa górne kręgi · 5 mięśni', '671'),
             barecards(['m. skośny górny głowy', 'm. prosty tylny mniejszy głowy', 'm. prosty tylny większy głowy',
                        'm. skośny dolny głowy', 'm. prosty boczny głowy'], PK), 'list', width=W['podp'], col=PK, id='podp')
GLEB_G = sub(gnode('Głębokie mięśnie grzbietu', 'erector spinae', 'world', TE,
                   'właściwe mięśnie grzbietu · gałęzie tylne nn. rdzeniowych', '650, 659'),
             DLUGIE + KROTKIE + PODPOT, 'row', q('3', 'jak długie są włókna?', '659'), width=W['gleb'], col=TE, id='gleb')

CH_GRZBIET = sub(gnode('Mięśnie grzbietu', 'musculi dorsi°', 'chap', 'c1', '', '649–677'),
                 POW_G + GLEB_G, 'row', q('1', 'skąd pochodzą – jaki mają nerw?', '649–650'), width=W['grz'], col='c1', id='grz')

# ======================================================================
# II. KLATKA PIERSIOWA
# ======================================================================
PRZ = copy.deepcopy(M('przepona'))
PRZ_ROWS = [
    ('ŚRODEK ŚCIĘGNISTY', ['kształt trójpłatowego liścia koniczyny – na płatku przednim leży serce z osierdziem, na bocznych podstawy płuc [[centrum tendineum]] (s. 692)']),
    ('OTWORY', [
        'rozwór aortowy – na wysokości Th12, między odnogami a kręgosłupem: aorta i przewód piersiowy [[hiatus aorticus]] (s. 691–692)',
        'rozwór przełykowy – wyżej i nieco na lewo od aortowego, w części lędźwiowej: przełyk oraz pnie błędne przedni i tylny [[hiatus esophageus]] (s. 691, 693)',
        'otwór żyły głównej – w środku ścięgnistym, na granicy płatka prawego i przedniego: żyła główna dolna i gałązki n. przeponowego prawego [[foramen venae cavae]] (s. 692–693)',
        'szczeliny w odnogach: n. trzewny większy (często też mniejszy), żyła nieparzysta (odnoga prawa) i nieparzysta krótka (odnoga lewa); bardziej bocznie pień współczulny (s. 691, 693)',
    ]),
    ('TRÓJKĄTY', [
        'trójkąt lędźwiowo-żebrowy – między częścią lędźwiową a żebrową, nad XII żebrem [[trigonum lumbocostale]] (s. 692)',
        'trójkąt mostkowo-żebrowy – między częścią mostkową a żebrową; przechodzą nim naczynia nabrzuszne górne [[trigonum sternocostale]] (s. 692)',
        'oba trójkąty i rozwór przełykowy to miejsca zmniejszonego oporu – tędy mogą powstawać przepukliny przeponowe (s. 695)',
    ]),
]
PRZ_WARN = ['Na s. 693 Bochenek pisze, że w odnodze prawej biegnie ż. nieparzysta krótka; na s. 691 – prawa: ż. nieparzysta, lewa: ż. nieparzysta krótka.']

k_pow = sub(gnode('Powierzchowne mięśnie klatki piersiowej', '', 'grp', PU, 'przyczepiają się do kośćca barku i ramienia', '677–684'),
            cards(['m. piersiowy większy', 'm. piersiowy mniejszy', 'm. podobojczykowy', 'm. zębaty przedni'], PU),
            'list', width=W['kpow'], col=PU, id='kpow')
k_gleb = sub(gnode('Głębokie albo właściwe mięśnie klatki piersiowej', '', 'grp', RE, 'właściwe mięśnie ściany klatki – ruchy oddechowe', '684–689'),
             cards(['mm. międzyżebrowe zewnętrzne', 'mm. międzyżebrowe wewnętrzne', 'mm. podżebrowe', 'm. poprzeczny klatki piersiowej'], RE),
             'list', width=W['kgleb'], col=RE, id='kgleb')
PRZ_POINTER = os.environ.get('PRZ_POINTER', 'budowa, kopuły, trójkąty, unerwienie i mechanika oddychania – na plakacie „Połączenia i mechanika”')
def przepona_short(col):
    rows = [
        ('CZĘŚCI', [
            'część lędźwiowa [[pars lumbalis]] – odnoga prawa i lewa [[crus dextrum, crus sinistrum]] od trzonów L1–L3 (prawa) i L1–L2 (lewa) oraz więzadła łukowate',
            'część żebrowa [[pars costalis]] – od wewnętrznej powierzchni chrząstek żeber VII–XII',
            'część mostkowa [[pars sternalis]] – od wewnętrznej powierzchni wyrostka mieczykowatego',
            'wszystkie trzy części kończą się na środku ścięgnistym [[centrum tendineum]]']),
        ('OTWORY', [
            'rozwór aortowy [[hiatus aorticus]] – Th12; aorta i przewód piersiowy',
            'rozwór przełykowy [[hiatus esophageus]] – przełyk i pnie błędne',
            'otwór żyły głównej [[foramen venae cavae]] – w środku ścięgnistym; żyła główna dolna']),
    ]
    h = [f'<div class="node card {col}"><div class="ch"><span class="nm">przepona</span> {lat("diaphragma")}</div><div class="bd">',
         '<div class="pgl">Bochenek s. 689–695</div>']
    for lab, items in rows:
        h.append(f'<div class="xrow"><div class="k">{lab}</div><ul>' + ''.join(f'<li>{mk(x)}</li>' for x in items) + '</ul></div>')
    h.append(f'<div class="note">→ {PRZ_POINTER}</div></div></div>')
    return ''.join(h)

L3M.pop('przepona', None); L3G.pop('Przepona', None); L3P.pop('oddychanie_l3', None)
k_prz = sub(gnode('Przepona', 'diaphragma', 'grp', GN, 'przegroda między jamą klatki piersiowej a jamą brzuszną', '689–696'),
            przepona_short(GN), 'list', width=W['kprz'], col=GN, id='kprz')

def li(x):
    if isinstance(x, tuple):
        head, subs = x
        return f'<li>{mk(head)}<ul>' + ''.join(f'<li>{mk(y)}</li>' for y in subs) + '</ul></li>'
    return f'<li>{mk(x)}</li>'

def mrow(lab, items):
    return f'<div class="xrow"><div class="k">{lab}</div><ul>' + ''.join(li(x) for x in items) + '</ul></div>'

MECH_L3 = ''
if 'oddychanie_l3' in L3P:
    USED_P.add('oddychanie_l3')
    _p = L3P['oddychanie_l3']
    MECH_L3 = (f'<div class="l3 inmech"><div class="l3h"><span class="l3n">3</span>{_p["title"].upper()} · BOCHENEK S. {_p["pg"]}</div>'
               f'<div class="l3cols">{l3rows(_p["items"])}</div></div>')

MECH = f'''<div class="panel green">
<div class="ph"><span class="pt">Mechanika oddychania</span><span class="pg">Bochenek s. 696–698</span></div>
<div class="bd two">
<div>
{mrow('WDECH', ['klatka piersiowa powiększa się we wszystkich trzech kierunkach: przepona napina się i obniża, powłoki brzucha się rozluźniają, żebra się unoszą, kręgosłup się prostuje (s. 696)'])}
{mrow('WYDECH', [
    'mięśnie brzucha się napinają, przepona się rozluźnia, żebra czynnie się opuszczają, kręgosłup się zgina (s. 696)',
    'siła sprężysta klatki piersiowej działa tylko do położenia równowagi – dalej żebra opuszczają mięśnie wydechowe (s. 697)'])}
{mrow('TYPY ODDECHOWE', [
    ('<b>żebrowy (piersiowy)</b> – poruszają się żebra (s. 696)', [
        'dolny – mechanizm żebrowo-przeponowy: dolne żebra i przepona to jeden układ (s. 697)',
        'górny – mechanizm żebrowo-mostkowy: górne żebra i mostek (s. 697)']),
    '<b>brzuszny (przeponowy)</b> – bez bezpośredniego udziału żeber; ruch przepony widać na przedniej ścianie brzucha (s. 697)',
    'przepona i mięśnie brzucha działają antagonistycznie (s. 697)',
    'spokojne oddychanie: zwykle czysty typ brzuszny; wzmożone: typ mieszany, żebrowo-przeponowy (s. 697)'])}
</div>
<div>
{mrow('MIĘŚNIE WDECHOWE', [
    '<b>główne:</b> przepona (s. 693) i mm. międzyżebrowe zewnętrzne – podnoszą żebra przy spokojnym oddychaniu żebrowym (s. 697)',
    ('<b>pomocnicze</b> (s. 697):', [
        'mm. pochyłe – przedłużenie mm. międzyżebrowych zewnętrznych',
        'm. mostkowo-obojczykowo-sutkowy – gdy głowa i kręgosłup są ustalone',
        'm. zębaty przedni, mm. piersiowe większy i mniejszy, m. najszerszy grzbietu (wiązki żebrowe), m. podobojczykowy – gdy ramię jest ustalone, np. chwyt brzegu stołu',
        'm. zębaty tylny górny'])])}
{mrow('MIĘŚNIE WYDECHOWE', [
    '<b>w spokojnym oddychaniu:</b> mm. międzyżebrowe wewnętrzne i m. poprzeczny klatki piersiowej (s. 697)',
    ('<b>pomocnicze</b> (s. 697):', [
        'mięśnie brzucha – najsilniejsze; czynne przy kaszlu i śpiewie',
        'm. najszerszy grzbietu – „mięsień kaszlu”: jego części boczne kurczą się przy utrudnionym wydechu, gdy ramiona są ustalone'])])}
</div>
</div>{MECH_L3}</div>'''

KWRAP = f'<div class="kwrap" id="kwrap" style="width:{W["kwrap"]}mm"><div class="krow">{k_gleb}{k_prz}</div></div>'
CH_KLATKA = sub(gnode('Mięśnie klatki piersiowej', 'musculi thoracis°', 'chap', 'c2', '', '677–702'),
                k_pow + KWRAP, 'row', q('1', 'z czym się łączą?', '677'), width=W['kl'], col='c2', id='kl')

# ======================================================================
# III. BRZUCH
# ======================================================================
b_bocz = sub(gnode('boczne', '', 'sg', AM, '3 warstwy: skośny zewn., skośny wewn., poprzeczny', '702, 704'),
             cards(['m. skośny zewnętrzny brzucha', 'm. skośny wewnętrzny brzucha', 'm. poprzeczny brzucha', 'dźwigacz jądra'], AM),
             'list', width=W['bbocz'], col=AM, id='bbocz')
b_przed = sub(gnode('przednie', '', 'sg', AM, 'układ mięśni prostych', '704'),
              cards(['m. prosty brzucha', 'm. piramidowy'], AM), 'list', width=W['bprzed'], col=AM, id='bprzed')
b_bp = sub(gnode('Boczne i przednie mięśnie brzucha', '', 'grp', AM, 'z boku 3 warstwy, z przodu pas mięśni prostych', '702–712'),
           b_bocz + b_przed, 'row', q('2', 'z boku czy z przodu?', '702'), width=W['bbp'], col=AM, id='bbp')
b_tyl = sub(gnode('Tylne mięśnie brzucha', '', 'grp', AM, 'po bokach kręgosłupa lędźwiowego', '712–715'),
            card(M('mm. międzypoprzeczne boczne lędźwi'), AM) + card(M('m. czworoboczny lędźwi'), AM),
            'list', width=W['btyl'], col=AM, id='btyl')
CH_BRZUCH = sub(gnode('Mięśnie brzucha', 'musculi abdominis°', 'chap', 'c3', '', '702–733'),
                b_bp + b_tyl, 'row', q('1', 'gdzie leżą?', '702'), width=W['brz'], col='c3', id='brz')

# ======================================================================
_CH = {'grzbiet': CH_GRZBIET, 'klatka': CH_KLATKA, 'brzuch': CH_BRZUCH}
_RT = os.environ.get('ROOT_TITLE', 'Mięśnie szkieletu osiowego')
_RS = os.environ.get('ROOT_SUB', 'grzbiet · klatka piersiowa · brzuch')
ROOT = sub(gnode(_RT, '', 'root', '', _RS, ''),
           ''.join(_CH[r] for r in REGIONS), 'row', width=INNER_W, col='root')

INFO = '''<div class="info">
<div class="i1">PLAKAT DO NAUKI · ANATOMIA · MIĘŚNIE</div>
<div class="i2">Wszystko wg: A. Bochenek, M. Reicher, <i>Anatomia człowieka</i>, t. I, s. 649–733</div>
<div class="i3">Poziom 1 – podział, poziom 2 – karty mięśni, poziom 3 – szczegóły z Bochenka małym drukiem.<br>Mięśnie szyi pominięte – nie ma ich na zaliczeniu. Mięśnie głębokie grzbietu – na zaliczeniu wystarczy je wymienić. Przepona szczegółowo i mechanika oddychania – na stronie „Klatka i oddychanie”.</div>
</div>'''

LEGEND_ROWS = '''<div class="lt1">JAK CZYTAĆ</div>
<div class="lrow"><span><span class="lpill">POZIOM 1</span></span><span><b>Z daleka:</b> sam podział – rozdziały, grupy, nazwy mięśni.</span></div>
<div class="lrow"><span><span class="lpill">POZIOM 2</span></span><span><b>Po przybliżeniu:</b> karty mięśni – przyczepy, czynność, części.</span></div>
<div class="lrow"><span><span class="lpill">POZIOM 3</span></span><span><b>Duże przybliżenie:</b> małym drukiem w ramkach <span class="lz3">3</span> – unerwienie, odmiany, położenie, szczegóły; panele tematyczne.</span></div>
<div class="lrow"><span><span class="lz">1</span></span><span>Pytanie przy rozgałęzieniu: według czego Bochenek dzieli grupę. Cyfra = kolejny podział w rozdziale.</span></div>
<div class="lrow"><span><span class="lsw">grupa</span></span><span>Przerywana ramka = grupa mięśni.</span></div>
<div class="lrow"><span><span class="lcard">mięsień</span></span><span>Pełna ramka = karta jednego mięśnia.</span></div>
<div class="lrow"><span class="lsm">(linea nuchae)</span><span>Łacińska nazwa miejsca przyczepu. ° = łaciny brak w t. I Bochenka.</span></div>
<div class="lrow"><span><span class="lw">!</span></span><span>Bochenek w różnych miejscach podaje coś innego.</span></div>
<div class="lrow"><span><span class="star">★</span></span><span>Temat wskazany jako ważny na zaliczeniu.</span></div>
<div class="lrow"><span class="lsm2">C · Th · L</span><span>Kręgi szyjne · piersiowe · lędźwiowe. Najwyżej 4 przyczepy na stronę.</span></div>'''

_rows_only = LEGEND_ROWS.split('</div>', 1)[1]
LEGEND_TOP = '<div class="lt1">JAK CZYTAĆ</div><div class="lgrid">' + _rows_only + '</div>'

# ---------------------------------------------------------------- panele poziomu ③ w „dokach” pod kolumnami
def chapter_panels(ch, order, skip=()):
    f = os.path.join(os.environ.get('L3DIR', '/home/user/first-thing/plakat'), f'l3_{ch}.json')
    ids = []
    if os.path.exists(f):
        ids = [p['id'] for p in json.load(open(f, encoding='utf-8')).get('panels', [])]
    ids = [i for i in order if i in ids] + [i for i in ids if i not in order]
    return [i for i in ids if i not in skip]

COLS = {'grzbiet': TE, 'klatka': GN, 'brzuch': AM}
DOCK_UNDER = {'grzbiet': os.environ.get('D_grzbiet', 'krot,podp'),
              'klatka': os.environ.get('D_klatka', 'kwrap'),
              'brzuch': os.environ.get('D_brzuch', 'bprzed,btyl')}
ORDER = {'grzbiet': ['powiezi_grzbietu'],
         'klatka': ['powiezi_klatki', 'dol_pachowy'],
         'brzuch': ['trojkat_ledzwiowy', 'tlocznia', 'pochewka', 'kresa_pepek', 'powiezie', 'powiez_poprzeczna', 'kanal', 'sciana_przepukliny', 'zstepowanie']}
DOCKS = ''
for ch in ('grzbiet', 'klatka', 'brzuch'):
    if ch not in REGIONS:
        continue
    html = ''.join(l3panel(i, COLS[ch]) for i in chapter_panels(ch, ORDER[ch], skip=('oddychanie_l3',)))
    if LEGEND_AT == ch:
        html += f'<div class="legend inflow">{LEGEND_ROWS}</div>'
    DOCKS += dock(DOCK_UNDER[ch], html, cols=int(os.environ.get('DOCKCOLS_' + ch, 1)))
LEGEND =f'<div class="legend">{LEGEND_TOP}</div>' if LEGEND_AT == 'top' else ''

# ---------------------------------------------------------------- panel z rysunkiem (własny rysunek SVG z figs/out) w osobnym doku
FIGDIR = '/home/user/first-thing/plakat/figs/out'
def fig_inline(name):
    p = os.path.join(FIGDIR, name + '.svg')
    if not os.path.exists(p):
        print('BRAK RYSUNKU', name)
        return ''
    s = open(p, encoding='utf-8').read()
    s = re.sub(r'<style>.*?</style>', '', s, flags=re.S)         # style rysunków dodajemy raz, z przedrostkiem .figsvg
    return s.replace('<svg ', '<svg class="figsvg" ', 1)

def fig_css():
    sys.path.insert(0, '/home/user/first-thing/plakat/figs')
    from figlib import STYLE
    out = []
    for rule in STYLE.strip().split('}'):
        if '{' not in rule:
            continue
        sel, body = rule.split('{', 1)
        out.append(','.join('.figsvg ' + x.strip() for x in sel.split(',')) + '{' + body + '}')
    return '\n'.join(out)

def fig_panel(figname, title, la='', pg='', col=''):
    svg = fig_inline(figname)
    if not svg:
        return ''
    la = f' {lat(la)}' if la else ''
    return (f'<div class="panel l3panel figpanel {col}"><div class="ph"><span class="pt">{title}</span>{la}'
            f'<span class="pg">Bochenek s. {pg}</span></div><div class="l3fig">{svg}</div></div>')

# pochewka m. prostego brzucha – przekroje poprzeczne (ryc. 465/466 u Bochenka; rysunek własny) – w wolnym miejscu pod kolumną mięśni bocznych
FIGDOCK = '' if 'brzuch' not in REGIONS else dock(os.environ.get('D_pochewka_fig', 'bbocz'),
               fig_panel('pochewka_przekroje', '<span class=star>★</span> Pochewka m. prostego brzucha – przekroje', 'vagina m. recti abdominis', '718', AM))
DOCKS += FIGDOCK

# ---------------------------------------------------------------- kontrola: czy wszystkie dane ③ trafiły na plakat
for name, allk, used in (('mięśnie', L3M, USED_M), ('grupy', L3G, USED_G), ('panele', L3P, USED_P)):
    miss = [k for k in allk if k not in used]
    if miss:
        print('NIEUŻYTE', name, miss)

# ---------------------------------------------------------------- CSS ze skalą K dla drzewa
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
html = f'''<!DOCTYPE html><html lang="pl"><head><meta charset="utf-8"><title>Mięśnie szkieletu osiowego – plakat</title>
<style>:root {{ --l3s: {L3S}; }}\n{CSS}</style></head><body><div class="poster">{INFO}{LEGEND}<div class="treebox"><svg class="wires"></svg>{ROOT}{DOCKS}</div></div>
<script>window.POSTER_K = {K};</script><script>{JS}</script></body></html>'''
open(os.path.join('/home/user/first-thing/plakat', os.environ.get('OUT', 'index.html')), 'w', encoding='utf-8').write(html)
print('ok', len(html), 'K', K, 'strona', PAGE_W, PAGE_H)
