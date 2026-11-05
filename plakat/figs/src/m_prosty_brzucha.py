# M. PROSTY BRZUCHA – widok od przodu (prawa strona ciała po lewej stronie rysunku). Schemat własny wg Bochenka t. I:
#  - przyczepy: pow. przednia chrząstek żebrowych V–VII, wyrostek mieczykowaty (i więzadła żebrowo-mieczykowe) →
#    górna gałąź kości łonowej i pow. przednia spojenia łonowego (s. 710); szerszy i cieńszy u góry (s. 710);
#  - smugi ścięgniste ok. 1 cm szerokości, rzadko ściśle poprzeczne, przeważnie nieco skośne lub łukowate (s. 710);
#    położenie (s. 711): górna – często niekompletna, łukowata – na wys. końca VIII żebra chrzęstnego, druga – na poziomie
#    pierwszego żebra wolnego, trzecia – pępka, czwarta (jeśli jest) – linii łukowatej;
#  - smugi ściśle zrośnięte z blaszką przednią pochewki (s. 710) – dlatego widoczne także po stronie z pochewką;
#  - budowa metameryczna: 6–9 miotomów, na co wskazuje unerwienie (nn. międzyżebrowe VI–XII, s. 710–711);
#  - kresa biała: od wyrostka mieczykowatego do spojenia łonowego, przy pępku ok. 2× szersza niż u góry, poniżej
#    pępka znów się zwęża (s. 719); m. piramidowy – trójkąt, podstawa na kości łonowej i spojeniu, do przodu od przyczepu
#    m. prostego, wierzchołek w kresie białej; dobrze rozwinięty ok. 7–8 cm (s. 712).
# Po prawej stronie ciała (lewa strona rysunku) – mięsień w pochewce; po lewej – po zdjęciu blaszki przedniej.
# Ukryte zarysy (wyrostek mieczykowaty, chrząstki pod mięśniem) – linią przerywaną.
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig

W, H = 160, 122
CX = 80.0
YCLIP0, YCLIP1 = 2.0, 115.0
f = Fig('m_prosty_brzucha', W, H,
        caption='m. prosty brzucha · widok od przodu; po prawej stronie ciała w pochewce, po lewej – po zdjęciu blaszki przedniej')


# ---------------------------------------------------------------- pomocnicze
def cr(pts, n=10, t=0.5):
    m = len(pts)
    if m < 3:
        out = []
        for i in range(m - 1):
            for k in range(n):
                u = k / n
                out.append((pts[i][0] + (pts[i + 1][0] - pts[i][0]) * u, pts[i][1] + (pts[i + 1][1] - pts[i][1]) * u))
        return out + [pts[-1]]
    PP = [pts[0]] + pts + [pts[-1]]
    out = []
    for i in range(1, m):
        p0, p1, p2, p3 = PP[i - 1], PP[i], PP[i + 1], PP[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) * t / 3, p1[1] + (p2[1] - p0[1]) * t / 3)
        c2 = (p2[0] - (p3[0] - p1[0]) * t / 3, p2[1] - (p3[1] - p1[1]) * t / 3)
        for k in range(n):
            u = k / n
            a = (1 - u) ** 3; b = 3 * u * (1 - u) ** 2; c = 3 * u * u * (1 - u); d = u ** 3
            out.append((a * p1[0] + b * c1[0] + c * c2[0] + d * p2[0], a * p1[1] + b * c1[1] + c * c2[1] + d * p2[1]))
    out.append(pts[-1])
    return out


def offset(pl, d):
    out = []
    for i, p in enumerate(pl):
        a = pl[max(i - 1, 0)]; b = pl[min(i + 1, len(pl) - 1)]
        tx, ty = b[0] - a[0], b[1] - a[1]
        L = math.hypot(tx, ty) or 1
        dd = d(i / (len(pl) - 1)) if callable(d) else d
        out.append((p[0] + ty / L * dd, p[1] - tx / L * dd))
    return out


def poly(pts, close=True):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + (' Z' if close else '')


def ribbon(center, w):
    """pasmo o szerokości w (stałej lub funkcji parametru 0..1) wzdłuż linii środkowej"""
    c = cr(center, n=10)
    a = offset(c, (lambda s: w(s) / 2) if callable(w) else w / 2)
    b = offset(c, (lambda s: -w(s) / 2) if callable(w) else -w / 2)
    return a + b[::-1]


def interp(prof, y):
    if y <= prof[0][0]:
        return prof[0][1]
    for (y0, v0), (y1, v1) in zip(prof, prof[1:]):
        if y <= y1:
            t = (y - y0) / (y1 - y0)
            t = t * t * (3 - 2 * t)
            return v0 + (v1 - v0) * t
    return prof[-1][1]


def P(u, y, s):
    """u – odległość od linii pośrodkowej, s=+1 lewa strona ciała (prawa rysunku), s=-1 prawa strona ciała"""
    return (CX + s * u, y)


def Ps(pts, s):
    return [P(u, y, s) for u, y in pts]


# ---------------------------------------------------------------- wymiary (mm rysunku ≈ 1 : 4)
Y_XI_TIP = 46.4          # koniec żebra XI (pierwsze wolne)
Y_UMB = 68.6             # pępek
Y_ARC = 78.0             # poziom kresy łukowatej (nieco poniżej pępka)
Y_PUB = 103.8            # górny brzeg spojenia łonowego

LA = [(16.0, 1.15), (30, 1.45), (50, 1.95), (62, 2.55), (Y_UMB, 2.85), (74, 2.2), (82, 1.2), (92, 0.8), (106, 0.75)]   # pół-szerokość kresy białej


def la(y):
    return interp(LA, y)


LAT = [(6.4, 18.3), (12, 18.6), (22, 18.4), (34, 17.9), (50, 17.0), (Y_UMB, 15.4), (78, 13.6), (88, 11.0), (96, 8.4), (101, 7.2), (Y_PUB, 6.9)]


def lat(y):
    return interp(LAT, y)


TOP = [(1.15, 17.2), (4.4, 15.1), (7.6, 11.7), (11.4, 8.3), (15.0, 6.6), (18.3, 6.4)]   # górny brzeg (przyczepy początkowe)

# chrząstki i żebra (linie środkowe; strona +)
CART = {
    'V': [(4.6, 4.6), (10, 5.9), (16, 6.4), (21, 5.6)],
    'VI': [(4.4, 10.2), (10, 12.2), (16, 13.4), (22, 13.0), (25, 11.8)],
    'VII': [(4.0, 15.2), (8, 18.4), (13, 21.4), (19, 22.8), (24, 22.0), (28, 19.8)],
    'VIII': [(12.4, 21.6), (15.5, 26.0), (20, 28.4), (25, 28.4), (29.5, 26.6)],
    'IX': [(17.4, 26.8), (20.5, 32.6), (24, 35.4), (28.5, 35.2), (31.5, 33.0)],
    'X': [(21.4, 33.6), (23.8, 40.5), (26.5, 45.0), (30, 45.4), (32.6, 43.2)],
}
BONE = {
    'V': [(21, 5.6), (28, 3.6), (37.5, 1.0)],
    'VI': [(25, 11.8), (31, 9.6), (37.5, 7.8)],
    'VII': [(28, 19.8), (32.5, 17.2), (37.5, 15.2)],
    'VIII': [(29.5, 26.6), (33.5, 24.2), (37.5, 22.5)],
    'IX': [(31.5, 33.0), (34.5, 30.8), (37.5, 29.4)],
    'X': [(32.6, 43.2), (35, 40.5), (37.5, 38.8)],
    'XI': [(37.5, 43.2), (35, 45.2), (32.4, Y_XI_TIP)],
}
WC, WB = 2.5, 2.8

# smugi ścięgniste: (u, y) linii środkowej od kresy białej do brzegu bocznego; szerokość ok. 1 cm ≈ 2.5 mm
INTER = [
    ('I', [(0, 27.6), (6, 26.2), (11, 26.0), (13.6, 26.6)], 13.6),     # łukowata, niekompletna
    ('II', [(0, 44.6), (8, 45.4), (17.2, 46.6)], None),
    ('III', [(0, Y_UMB - 0.4), (8, Y_UMB), (15.6, Y_UMB + 1.4)], None),
    ('IV', [(0, Y_ARC - 0.6), (7, Y_ARC), (13.6, Y_ARC + 0.8)], None),   # nie zawsze
]
WI = 2.5

# ---------------------------------------------------------------- kości: miednica
PELV = [(38.6, 69.4), (36.6, 72.4), (34.6, 76.8), (33.3, 81.0), (32.4, 84.6), (32.6, 86.3), (31.5, 87.5), (31.7, 89.6),
        (30.4, 92.2), (28.0, 95.2), (24.0, 97.7), (19.0, 99.6), (14.0, 100.9), (12.3, 101.5), (10.8, 100.9), (9.4, 101.8),
        (5.5, 102.9), (0.9, Y_PUB - 0.4), (0.9, 117), (6.2, 117), (6.8, 111.0), (8.6, 107.2), (12.5, 105.4), (18.5, 104.7),
        (24.0, 105.0), (27.6, 106.4), (30.6, 109.6), (33.2, 113.6), (35.2, 117), (38.6, 117)]
ASIS = (32.4, 84.6)
TUB = (10.8, 101.0)

for s in (-1, 1):
    f.add(f'<path class="bone" d="{poly(Ps(PELV, s))}"/>')
    # dół biodrowy (powierzchnia wewnętrzna talerza) i brzeg panewki – linie szczegółu
    f.add(f'<path class="bonel" d="{poly(Ps(cr([(13.0, 101.6), (19, 100.6), (24.5, 98.8), (29.4, 95.4), (33.6, 90.6), (36.4, 85.0), (38.6, 82.4)], n=6), s), close=False)}"/>')
    f.add(f'<path class="bonel" d="{poly(Ps(cr([(38.6, 98.6), (35.4, 99.4), (33.0, 102.6), (33.2, 107.4), (35.6, 111.0), (38.6, 112.0)], n=6), s), close=False)}"/>')
# spojenie łonowe (krążek międzyłonowy)
f.add(f'<path class="cart" d="{poly([(CX - 0.95, Y_PUB - 0.1), (CX + 0.95, Y_PUB - 0.1), (CX + 0.95, 120), (CX - 0.95, 120)])}"/>')

# więzadło pachwinowe (kontekst)
for s in (-1, 1):
    f.add(f'<path class="lig" d="{poly(Ps(ribbon([ASIS, (25, 92.0), (17, 97.8), TUB], 1.05), s))}"/>')

# nerwy (pod chrząstkami żebrowymi – rysowane przed nimi)
# nn. międzyżebrowe VI–XII – wchodzą do mięśnia od strony bocznej (metameria)
NERVES = [((25.0, 16.7), 19.6), ((27.4, 24.4), 25.8), ((28.8, 31.2), 33.6), ((30.0, 39.8), 42.0),
          ((28.6, 51.0), 53.4), ((27.2, 60.2), 62.4), ((25.6, 71.6), 73.6)]
for (u0, y0), y1 in NERVES:
    u1 = lat(y1) - 1.2
    um = (u0 + u1) / 2
    f.add(f'<path class="nerve" d="{poly(Ps(ribbon([(u0, y0), (um, (y0 + y1) / 2 + 0.25), (u1, y1)], 0.75), 1))}"/>')


# ---------------------------------------------------------------- kości: żebra i chrząstki
for s in (-1, 1):
    for k in ['V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI']:
        f.add(f'<path class="bone" d="{poly(Ps(ribbon(BONE[k], WB), s))}"/>')
    # koniec wolny żebra XI – zaokrąglony
    tip = BONE['XI'][-1]
    f.add(f'<circle class="bone" cx="{CX + s * tip[0]:.2f}" cy="{tip[1]:.2f}" r="1.25"/>')
    f.add(f'<path class="bone" style="stroke:none" d="{poly(Ps(ribbon(BONE["XI"][1:], WB - 0.5), s))}"/>')
    for k in ['X', 'IX', 'VIII', 'VII', 'VI', 'V']:
        f.add(f'<path class="cart" d="{poly(Ps(ribbon(CART[k], WC), s))}"/>')
    # scalenie łuku żebrowego (wnętrza bez obrysów na stykach)
    for k in ['X', 'IX', 'VIII', 'VII']:
        f.add(f'<path class="cart" style="stroke:none" d="{poly(Ps(ribbon(CART[k], WC - 0.42), s))}"/>')

# mostek (dolna część trzonu) i wyrostek mieczykowaty
ST = [(5.6, -3), (5.35, 15.0), (3.5, 16.3)]
f.add(f'<path class="bone" d="{poly(Ps(ST, 1) + Ps(ST[::-1], -1))}"/>')
XI_ = [(3.0, 16.5), (2.7, 19.8), (1.8, 23.4), (0.0, 25.6)]
xiph = cr(XI_, n=6)
xiph_pts = Ps(xiph, 1) + Ps(xiph[::-1], -1)[1:]
f.add(f'<path class="bone" d="{poly(xiph_pts)}"/>')

# ---------------------------------------------------------------- m. prosty brzucha – kontur
YS = [16.0 + 0.5 * k for k in range(int((Y_PUB - 16.0) / 0.5) + 1)]


def rectus_outline(s, y_bot=95.0):
    """mięsień (część mięsista) – od górnego brzegu do początku ścięgna końcowego"""
    top = cr(TOP, n=8)
    lat_side = [(lat(y), y) for y in [6.4 + 0.5 * k for k in range(int((y_bot - 6.4) / 0.5) + 1)]]
    med_side = [(la(y) + 0.05, y) for y in [y_bot - 0.5 * k for k in range(int((y_bot - 17.2) / 0.5) + 1)]]
    bottom = [(lat(y_bot) - (lat(y_bot) - la(y_bot)) * k / 8, y_bot + 0.8 * math.sin(math.pi * k / 8)) for k in range(9)]
    return Ps(top + lat_side[1:] + bottom[1:] + med_side[1:], s)


def tendon_outline(s, y0=94.2):
    ys = [y0 + 0.4 * k for k in range(int((Y_PUB + 0.3 - y0) / 0.4) + 1)]
    right = [(lat(y), y) for y in ys]
    left = [(la(y) + 0.05, y) for y in ys[::-1]]
    return Ps(right + left, s)


# pochewka (strona prawa ciała = lewa rysunku): mięsień + blaszka przednia
SHEATH_EXT = 1.3


def sheath_outline(s):
    top = [(u, y - 0.9) for u, y in cr(TOP, n=8)]
    top[-1] = (top[-1][0] + SHEATH_EXT, top[-1][1])
    lat_side = [(lat(y) + SHEATH_EXT, y) for y in [6.4 + 0.5 * k for k in range(int((Y_PUB - 6.4) / 0.5) + 1)]]
    med_side = [(0.0, Y_PUB), (0.0, 16.4)]
    return Ps(top + lat_side[1:] + med_side, s)


# --- strona lewa ciała (prawa rysunku): mięsień odsłonięty
s = 1
# brzeg rozciętej blaszki przedniej pochewki (wąski pasek bocznie od mięśnia)
cut = [(lat(y) + 1.4, y) for y in [7.2 + 0.5 * k for k in range(int((Y_PUB - 7.2) / 0.5) + 1)]]
inner = [(lat(y) - 0.3, y) for y in [Y_PUB - 0.5 * k for k in range(int((Y_PUB - 7.2) / 0.5) + 1)]]
f.add(f'<path class="tendon" d="{poly(Ps(cut + inner, s))}"/>')

# ścięgno końcowe i mięsień
f.add(f'<path class="tendon" d="{poly(tendon_outline(s))}"/>')
f.add(f'<path class="muscle" d="{poly(rectus_outline(s))}"/>')
# ukryte zarysy pod górnym odcinkiem mięśnia: chrząstki VI i VII (przyczepy na ich powierzchni przedniej)
TOPU = [(0.0, 17.6)] + TOP          # górny brzeg jako funkcja u


def top_y(u):
    return interp(TOPU, u)


for k in ('VI', 'VII'):
    c = cr(CART[k], n=12)
    for d in (WC / 2, -WC / 2):
        edge = [p for p in offset(c, d) if p[0] <= lat(p[1]) - 0.4 and p[1] > top_y(p[0]) + 0.4]
        if len(edge) > 1:
            f.add(f'<path class="capsule" d="{poly(Ps(edge, s), close=False)}"/>')
# włókna podłużne (biegną równolegle ku dołowi)
for k in range(1, 10):
    fr = k / 10
    pts = [(la(y) + (lat(y) - la(y)) * fr, y) for y in [7.0 + 0.5 * j for j in range(int((94.0 - 7.0) / 0.5) + 1)]]
    pts = [p for p in pts if top_y(p[0]) + 1.2 <= p[1] <= 93.0]
    f.add(f'<path class="musclel" d="{poly(Ps(pts, s), close=False)}"/>')

# smugi ścięgniste (odsłonięte)
for name, cl, uend in INTER:
    c = [(u if u > 0 else la(y) - 0.2, y) for u, y in cl]
    c[-1] = (lat(c[-1][1]) + 0.15 if uend is None else uend, c[-1][1])
    band = ribbon(c, (lambda t: WI * (1 - 0.75 * max(0.0, (t - 0.7) / 0.3) ** 1.5)) if name == 'I' else WI)
    if name == 'IV':
        f.add(f'<path class="capsule" d="{poly(Ps(band, s))}"/>')
    else:
        f.add(f'<path class="tendon" d="{poly(Ps(band, s))}"/>')
# numery smug
NUMPOS = {'I': (7.6, 27.15), 'II': (7.6, 46.25), 'III': (7.6, Y_UMB + 1.15), 'IV': (6.8, Y_ARC + 1.05)}
for name, (u, y) in NUMPOS.items():
    f.text(CX + u, y, name, cls='big', anchor='middle')

# m. piramidowy (przed m. prostym)
PYR = [(0.95, 84.4), (3.2, 88.6), (6.6, 94.6), (9.4, 99.6), (10.2, Y_PUB - 1.3), (1.0, Y_PUB - 0.3)]
f.add(f'<path class="muscle" d="{poly(Ps(cr(PYR[:5], n=6) + PYR[5:], s))}"/>')
f.add(f'<path class="shade" d="{poly(Ps(cr(PYR[:5], n=6) + PYR[5:], s))}"/>')
for k in range(1, 5):
    b = (1.0 + (9.0 - 1.0) * k / 5, Y_PUB - 0.6)
    a = (1.15, 85.6 + 1.6 * k)
    f.add(f'<path class="musclel" d="{poly(Ps([b, a], s), close=False)}"/>')

# --- strona prawa ciała (lewa rysunku): mięsień w pochewce
s = -1
f.add(f'<path class="muscle" d="{poly(rectus_outline(s))}"/>')
f.add(f'<path class="tendon" d="{poly(sheath_outline(s))}"/>')
# zarys brzegu bocznego mięśnia widoczny przez blaszkę
f.add(f'<path class="musclel" d="{poly(Ps([(lat(y), y) for y in [7.0 + 0.5 * k for k in range(int((Y_PUB - 7.0) / 0.5) + 1)]], s), close=False)}"/>')
# smugi zrośnięte z blaszką przednią – widoczne jako pasma
for name, cl, uend in INTER:
    c = [(u if u > 0 else la(y) - 0.2, y) for u, y in cl]
    c[-1] = (lat(c[-1][1]) - 0.2 if uend is None else uend, c[-1][1])
    line = cr(c, n=10)
    cls = 'capsule' if name == 'IV' else 'ligl'
    f.add(f'<path class="{cls}" d="{poly(Ps(line, s), close=False)}"/>')

# kresa biała (całość) i pępek
lw = [(la(y), y) for y in YS] + [(la(Y_PUB), Y_PUB + 0.4)]
f.add(f'<path class="tendon" d="{poly(Ps(lw, 1) + Ps(lw[::-1], -1))}"/>')
f.add(f'<circle class="cavity" cx="{CX:.2f}" cy="{Y_UMB:.2f}" r="1.75"/>')
f.add(f'<circle class="tendon" cx="{CX:.2f}" cy="{Y_UMB + 0.15:.2f}" r="0.85"/>')
# skrzyżowanie włókien ścięgien końcowych przed spojeniem
for s in (-1, 1):
    f.add(f'<path class="tendon" d="M{CX + s * 3.6:.2f},{Y_PUB - 1.4:.2f} L{CX - s * 1.2:.2f},{Y_PUB + 2.6:.2f}"/>')

# ukryty zarys wyrostka mieczykowatego (pod mięśniami i kresą białą)
f.add(f'<path class="capsule" d="{poly(xiph_pts)}"/>')

# ---------------------------------------------------------------- przycięcie u góry i u dołu
body = ''.join(f.body)
f.body = [f'<defs><clipPath id="cp_mpb"><rect x="0" y="{YCLIP0}" width="{W}" height="{YCLIP1 - YCLIP0}"/></clipPath></defs>'
          f'<g clip-path="url(#cp_mpb)">{body}</g>']

# ---------------------------------------------------------------- oznaczenia nerwów VI i XII
f.text(CX + 25.6, 15.4, 'VI', cls='note', anchor='middle')
f.text(CX + 26.2, 70.6, 'XII', cls='note', anchor='middle')

# ---------------------------------------------------------------- podpisy – lewa kolumna
TL = 41.0
f.label(P(22.0, 13.1, -1), 'chrząstki żebrowe V–VII', 'cartilagines costales', (TL, 9.0), side='L')
f.label(P(1.4, 21.2, -1), 'wyrostek mieczykowaty', 'processus xiphoideus', (TL, 19.0), side='L')
f.label(P(24.6, 40.6, -1), 'łuk żebrowy', 'arcus costalis', (TL, 33.0), side='L')
f.label(P(0.0, 52.0, -1), 'kresa biała', 'linea alba', (TL, 44.0), side='L')
f.label(P(9.0, 57.5, -1), 'blaszka przednia pochewki', 'lamina anterior', (TL, 55.0), side='L')
f.label(P(1.75, Y_UMB, -1), 'pępek', 'umbilicus', (TL, 66.0), side='L')
f.label(P(ASIS[0], ASIS[1], -1), 'kolec biodrowy przedni górny', 'spina iliaca anterior superior', (TL, 82.0), side='L')
f.label(P(0.3, 109.0, -1), 'spojenie łonowe', 'symphysis pubica', (TL, 104.0), side='L')

# ---------------------------------------------------------------- podpisy – prawa kolumna
TR = 119.0
f.label(P(10.0, 19.0, 1), 'm. prosty brzucha', 'm. rectus abdominis', (TR, 8.0), side='R')
f.label(P(22.4, 41.0, 1), 'nn. międzyżebrowe VI–XII', None, (TR, 20.0), side='R')
f.text(TR + 0.7, 23.6, '6–9 miotomów buduje mięsień –')
f.text(TR + 0.7, 26.2, 'wskazuje na to unerwienie;')
f.text(TR + 0.7, 28.8, 'smugi = zachowane granice')
f.text(TR + 0.7, 31.4, 'miotomów (nie wszystkie)')
f.label(P(13.0, 46.4, 1), 'smugi ścięgniste', 'intersectiones tendineae', (TR, 40.0), side='R')
f.text(TR + 0.7, 46.4, 'najczęściej 3–4; położenie:')
f.text(TR + 0.7, 49.0, 'I – koniec VIII żebra chrzęstnego')
f.text(TR + 0.7, 51.6, 'II – żebro XI (pierwsze wolne)')
f.text(TR + 0.7, 54.2, 'III – pępek')
f.text(TR + 0.7, 56.8, 'IV – kresa łukowata (jeśli jest)')
f.label(P(4.6, 95.0, 1), 'm. piramidowy', 'm. pyramidalis', (TR, 73.0), side='R')
f.label(P(22.0, Y_PUB - 3.6, 1), 'gałąź górna kości łonowej', 'ramus superior ossis pubis', (TR, 95.0), side='R')
f.label(P(22.0, 94.8, 1), 'więzadło pachwinowe', 'ligamentum inguinale', (TR, 84.0), side='R')

f.save()
print('ok')
