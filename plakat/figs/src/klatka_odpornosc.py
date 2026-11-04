# ODPORNOŚĆ KLATKI PIERSIOWEJ (Bochenek, t. I, s. 293). Schemat własny.
# Panel górny: pierścień żebrowy (para żeber V + mostek + kręg piersiowy) w widoku od góry (przód ku górze) – „napięta
#   sprężyna”; linia przerywana – pierścień ugięty sprężyście pod naciskiem na mostek (ruch powiększony). Ściany: przednia
#   (mostek – złamania niesłychanie rzadkie), boczne (złamania częstsze), tylna (mocniejsza niż boczne, mniej sprężysta).
# Panel dolny: klatka od przodu (prawa strona ciała po lewej) – nacisk na mostek rozkłada się na szereg obustronnych
#   pierścieni żebrowych (strzałki niebieskie); uderzenie z boku trafia tylko na jedno żebro lub kilka żeber.
# Kształt klatki od przodu – ta sama geometria co figs/src/oddychanie_wymiary.py (skopiowana); kręg – jak wzor_th_gora.py.
import sys, math, os
sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth, mirror

W, H = 146, 116
f = Fig('klatka_odpornosc', W, H,
        caption='pierścień żebrowy od góry (przód ku górze) · klatka piersiowa od przodu (prawa strona ciała po lewej)')


# ---------------------------------------------------------------- pomocnicze
def cr(pts, closed=False, n=12, t=0.5):
    m = len(pts)
    if m < 3:
        out = []
        for i in range(m - 1):
            for k in range(n):
                u = k / n
                out.append((pts[i][0] + (pts[i + 1][0] - pts[i][0]) * u, pts[i][1] + (pts[i + 1][1] - pts[i][1]) * u))
        return out + [pts[-1]]
    PP = (pts[-1:] + pts + pts[:2]) if closed else ([pts[0]] + pts + [pts[-1]])
    out = []
    for i in (range(1, m + 1) if closed else range(1, m)):
        p0, p1, p2, p3 = PP[i - 1], PP[i], PP[i + 1], PP[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) * t / 3, p1[1] + (p2[1] - p0[1]) * t / 3)
        c2 = (p2[0] - (p3[0] - p1[0]) * t / 3, p2[1] - (p3[1] - p1[1]) * t / 3)
        for k in range(n):
            u = k / n
            a = (1 - u) ** 3; b = 3 * u * (1 - u) ** 2; c = 3 * u * u * (1 - u); d = u ** 3
            out.append((a * p1[0] + b * c1[0] + c * c2[0] + d * p2[0], a * p1[1] + b * c1[1] + c * c2[1] + d * p2[1]))
    if not closed:
        out.append(pts[-1])
    return out


def poly(pts, close=True):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + (' Z' if close else '')


def band(pts, w0, w1=None, n=10, cap0=False, cap1=False):
    """pasmo o szerokości w0→w1 wzdłuż krzywej przez pts (zamknięty wielokąt)"""
    w1 = w0 if w1 is None else w1
    c = cr(pts, n=n)
    L = [0.0]
    for i in range(1, len(c)):
        L.append(L[-1] + math.dist(c[i - 1], c[i]))
    tot = L[-1] or 1
    left, right = [], []
    for i, p in enumerate(c):
        a = c[max(i - 1, 0)]; b = c[min(i + 1, len(c) - 1)]
        tx, ty = b[0] - a[0], b[1] - a[1]
        ln = math.hypot(tx, ty) or 1
        nx, ny = -ty / ln, tx / ln
        w = (w0 + (w1 - w0) * L[i] / tot) / 2
        left.append((p[0] + nx * w, p[1] + ny * w))
        right.append((p[0] - nx * w, p[1] - ny * w))

    def capf(p, q, center, w, k=7):
        a0 = math.atan2(p[1] - center[1], p[0] - center[0])
        return [(center[0] + w * math.cos(a0 + math.pi * j / k), center[1] + w * math.sin(a0 + math.pi * j / k)) for j in range(1, k)]
    out = list(left)
    if cap1:
        out += capf(left[-1], right[-1], c[-1], w1 / 2)
    out += right[::-1]
    if cap0:
        out += capf(right[0], left[0], c[0], w0 / 2)
    return out


# ================================================================ PANEL A – pierścień żebrowy od góry
KA = 2.15                    # mm rysunku / cm
CXA, YA = 73.0, 12.6         # oś pośrodkowa; poziom przedniej powierzchni mostka (y = 0 cm)


def PA(x, y):
    return (CXA + x * KA, YA + y * KA)


# linia środkowa prawej kości żebrowej (cm; x – w prawo, y – ku tyłowi): głowa → guzek → kąt → bok → koniec przedni
RIB = [(1.45, 14.0), (2.75, 15.05), (4.6, 15.95), (6.9, 16.1), (9.3, 15.1), (11.2, 12.9), (12.15, 10.0), (12.15, 6.9),
       (11.2, 4.2), (9.4, 2.25), (7.3, 1.2)]
CARTL = [(7.55, 1.3), (5.0, 0.62), (2.2, 0.5)]
ST_HW, ST_Y0, ST_Y1 = 2.05, -0.3, 1.05          # mostek (przekrój trzonu): połowa szerokości, przód, tył


def ring_shapes(tf, cut=None):
    """zwraca wielokąty (klasa, punkty) pierścienia żebrowego po przekształceniu tf: (x, y) cm → (x, y) cm;
    cut – rysuj kość żebrową tylko od miejsca, gdzie y < cut (część tylna bez zmian – pominięta)"""
    out = []
    for s in (-1, 1):
        R = RIB if cut is None else [p for p in RIB if p[1] < cut]
        rib = [tf((s * x, y)) for x, y in R]
        car = [tf((s * x, y)) for x, y in CARTL]
        out.append(('cart', band([PA(*p) for p in car], 0.78 * KA, 0.72 * KA)))
        out.append(('bone', band([PA(*p) for p in rib], 1.0 * KA, 0.92 * KA, cap0=(cut is None))))
    st = [(-ST_HW + 0.35, ST_Y0), (ST_HW - 0.35, ST_Y0), (ST_HW, ST_Y0 + 0.35), (ST_HW, ST_Y1 - 0.3), (ST_HW - 0.35, ST_Y1),
          (-ST_HW + 0.35, ST_Y1), (-ST_HW, ST_Y1 - 0.3), (-ST_HW, ST_Y0 + 0.35)]
    out.append(('bone2', [PA(*tf(p)) for p in st]))
    return out


# kręg piersiowy od góry (kształt jak we wzorze wzor_th_gora: jednostki ≈ mm kości; przód ku górze)
def VW(x, y):
    return PA((x - 70) / 10.0, 12.75 + (y - 15.2) / 10.0)


C = 70
LW = [(60.5, 33), (56.8, 38.2), (50, 41.5), (45, 43.3), (42.6, 44.3), (41.2, 46.6), (42.2, 49.1), (44.8, 50),
      (49.2, 49.2), (54, 48.8), (58, 49.8), (63, 52.4), (67.2, 55), (68.3, 61), (69.1, 68), (69.6, 73.3)]
arch = LW + [(C, 74.4)] + mirror(LW, C)
f.add(f'<path class="bone" d="{smooth([VW(*p) for p in arch])}"/>')
hx, hy = VW(C, 42.2)
f.add(f'<ellipse class="hole" cx="{hx:.2f}" cy="{hy:.2f}" rx="{7.1 * KA / 10:.2f}" ry="{6.7 * KA / 10:.2f}"/>')
body = [(59.2, 35.2), (55.6, 30.2), (55.8, 23), (61, 17.2), (C, 15.2), (79, 17.2), (84.2, 23), (84.4, 30.2), (80.8, 35.2), (C, 33.6)]
f.add(f'<path class="bone" d="{smooth([VW(*p) for p in body])}"/>')
inner = [(60.6, 33.4), (57.8, 29.6), (58.1, 23.6), (62.4, 18.9), (C, 17.3), (77.6, 18.9), (81.9, 23.6), (82.2, 29.6), (79.4, 33.4), (C, 32)]
f.add(f'<path class="bonel" d="{smooth([VW(*p) for p in inner])}"/>')
a_, b_ = VW(C, 54), VW(C, 71.5)
f.add(f'<path class="bonel" d="M{a_[0]:.2f},{a_[1]:.2f} L{b_[0]:.2f},{b_[1]:.2f}"/>')

# pierścień – położenie spoczynkowe
for cls, pts in ring_shapes(lambda p: p):
    f.add(f'<path class="{cls}" d="{poly(pts)}"/>')


# pierścień pod naciskiem na mostek (linia przerywana): przód cofa się, boki nieco się rozchylają, tył bez zmian
def press(p):
    x, y = p
    u = max(0.0, 1.0 - y / 15.8)
    return (x * (1.0 + 0.05 * math.sin(math.pi * min(y, 15.8) / 15.8)), y + 2.3 * u ** 1.6)


for cls, pts in ring_shapes(press, cut=13.5):
    f.add(f'<path class="capsule" d="{poly(pts)}"/>')

# nacisk na mostek (z przodu)
s_top = PA(0, ST_Y0)
f.arrow(f'M{CXA:.2f},{s_top[1] - 9.5:.2f} L{CXA:.2f},{s_top[1] - 1.2:.2f}', red=True)


# ================================================================ PANEL B – klatka od przodu
SB = 1.5                     # mm na cm
CXB, YB = 73.0, 60.5         # oś pośrodkowa, poziom górnego brzegu Th1


def FB(u, y, side=-1):
    """u – odległość od płaszczyzny pośrodkowej (cm), side=-1 prawa strona ciała (lewa strona rysunku)"""
    return (CXB + side * SB * u, YB + SB * y)


RA = [(5.8, 2.0), (9.0, 4.9), (11.3, 7.6), (12.9, 10.2), (14.0, 12.8), (14.7, 15.4), (15.1, 18.0), (15.2, 20.5),
      (15.0, 22.9), (14.6, 25.1), (14.0, 27.0), (12.9, 28.6)]
RJ = [(3.8, 4.6), (5.8, 8.3), (7.2, 11.4), (8.3, 14.2), (9.2, 17.0), (9.9, 19.8), (10.6, 22.6), (11.3, 25.0),
      (12.1, 27.2), (12.9, 29.2), (13.3, 30.0), (12.0, 31.0)]
RW = [(1.5, 1.6), (1.1, 1.3), (0.9, 1.2), (0.9, 1.2), (0.9, 1.15), (0.9, 1.15), (0.9, 1.1), (0.85, 1.05),
      (0.85, 1.0), (0.8, 0.95), (0.75, 0.7), (0.7, 0.65)]
CART = [[(3.8, 4.6), (2.3, 5.3)],
        [(5.8, 8.3), (4.0, 8.8), (2.2, 9.0)],
        [(7.2, 11.4), (4.7, 11.7), (2.3, 11.8)],
        [(8.3, 14.2), (5.3, 14.4), (2.3, 14.3)],
        [(9.2, 17.0), (5.8, 17.0), (2.2, 16.6)],
        [(9.9, 19.8), (6.2, 19.6), (2.0, 18.6)],
        [(10.6, 22.6), (6.7, 22.1), (3.4, 20.8), (1.7, 19.8)],
        [(11.3, 25.0), (8.5, 24.4), (6.3, 22.6)],
        [(12.1, 27.2), (10.0, 26.6), (8.3, 25.0)],
        [(12.9, 29.2), (11.6, 28.8), (10.1, 27.3)],
        [(13.3, 30.0), (13.2, 30.9)],
        [(12.0, 31.0), (11.8, 31.7)]]


def rib_mid(a, j):
    return (a[0] - (a[0] - j[0]) * 0.30, a[1] + (j[1] - a[1]) * 0.60)


for side in (-1, 1):
    T = lambda p: FB(p[0], p[1], side)
    for k in range(12):
        a, j = RA[k], RJ[k]
        pts = [T(a), T(rib_mid(a, j)), T(j)]
        f.add(f'<path class="bone" d="{poly(band(pts, RW[k][0] * SB, RW[k][1] * SB, cap0=True, cap1=(k >= 10)))}"/>')
    for k in range(12):
        w = (0.95 if k < 10 else 0.6) * SB
        f.add(f'<path class="cart" d="{poly(band([T(p) for p in CART[k]], w, w * (0.95 if k < 7 else 0.8), cap1=(k >= 7)))}"/>')
half = [(0, 4.5), (1.3, 4.1), (2.5, 3.8), (2.75, 4.9), (2.35, 6.2), (1.65, 8.2), (1.55, 8.9), (1.65, 9.3),
        (1.85, 11.6), (1.95, 14.0), (2.05, 16.4), (1.95, 18.5), (1.5, 19.7), (1.0, 20.1), (0.95, 21.9), (0.45, 23.1)]
outline = [FB(u, y, -1) for u, y in half] + [FB(0, 23.5, -1)] + [FB(u, y, 1) for u, y in reversed(half[1:])]
f.add(f'<path class="bone" d="{smooth(outline, closed=True, t=0.35)}"/>')
for y in (8.95, 19.75):
    hw = 1.55 if y < 10 else 1.45
    p, q = FB(hw, y, -1), FB(hw, y, 1)
    f.add(f'<path class="bonel" d="M{p[0]:.2f},{p[1]:.2f} L{q[0]:.2f},{q[1]:.2f}"/>')

# nacisk na mostek rozkłada się na szereg obustronnych pierścieni żebrowych (II–VII) – strzałki wzdłuż chrząstek
SC = FB(0, 13.2)
for k in range(1, 7):
    pts = CART[k]
    for side in (-1, 1):
        cc = cr([FB(p[0], p[1], side) for p in pts[::-1]], n=16)       # od mostka ku kości żebrowej
        L = [0.0]
        for i in range(1, len(cc)):
            L.append(L[-1] + math.dist(cc[i - 1], cc[i]))
        sel = [p for p, l in zip(cc, L) if l >= 0.9]
        e = cc[-1]; d_ = (cc[-1][0] - cc[-4][0], cc[-1][1] - cc[-4][1]); dl = math.hypot(*d_)
        sel.append((e[0] + d_[0] / dl * 1.4, e[1] + d_[1] / dl * 1.4))
        f.arrow(poly(sel, close=False))

# uderzenie z boku (lewa strona ciała – prawa strona rysunku) na jedno żebro (VII)
L7 = FB(RA[6][0] + 0.6, RA[6][1], 1)
f.arrow(f'M{L7[0] + 9.0:.2f},{L7[1]:.2f} L{L7[0] + 1.0:.2f},{L7[1]:.2f}', red=True)

# ---------------------------------------------------------------- podpisy
TL, TR = 41.0, 105.0


def notes(x, y, lines, side):
    for k, t in enumerate(lines):
        f.text(x + (0.7 if side == 'R' else -0.7), y + 6.6 + 2.6 * k, t, cls='note', anchor='start' if side == 'R' else 'end')


# panel A
f.label((CXA, s_top[1] - 6.0), 'nacisk na mostek', None, (TL, 4.5), side='L')
notes(TL, 4.5 - 3.0, ['pierścień ugina się sprężyście', '(linia przerywana; ruch powiększony)'], 'L')
f.label(PA(-4.9, 0.6), 'ściana przednia', None, (TL, 17.0), side='L')
notes(TL, 17.0 - 3.0, ['zbudowana szczególnie korzystnie –', 'złamania niesłychanie rzadkie'], 'L')
f.label(PA(-12.15, 9.0), 'pierścień żebrowy', None, (TL, 30.5), side='L')
notes(TL, 30.5 - 3.0, ['para żeber poprzecznie złączonych', 'mostkiem – napięta sprężyna;', 'napięcie wzmagają mm. wdechowe'], 'L')
f.label(PA(-6.9, 16.1), 'ściana tylna', None, (TL, 47.0), side='L')
notes(TL, 47.0 - 3.0, ['mocniejsza niż boczne, ale mniej', 'sprężysta i mniej giętka'], 'L')

f.label(PA(1.1, 0.35), 'mostek', 'sternum', (TR, 8.0), side='R')
f.label(PA(12.15, 7.5), 'ściana boczna', None, (TR, 20.5), side='R')
notes(TR, 20.5 - 3.0, ['złamania częstsze'], 'R')
f.label(VW(77.0, 22.0), 'trzon kręgu', 'corpus vertebrae', (TR, 44.0), side='R')

# panel B
f.label(FB(*rib_mid(RA[1], RJ[1]), -1), 'kość żebrowa', 'os costale', (TL, 64.0), side='L')
f.label(SC, 'ciężar lub uderzenie na mostek', None, (TL, 76.0), side='L')
notes(TL, 76.0 - 3.0, ['rozkłada się (strzałki) na szereg', 'obustronnych pierścieni żebrowych'], 'L')
f.label(FB(8.5, 24.4, -1), 'chrząstka żebrowa', 'cartilago costalis', (TL, 93.0), side='L')
f.label((L7[0] + 6.0, L7[1]), 'uderzenie z boku', None, (TR, 77.5), side='R')
notes(TR, 77.5 - 3.0, ['trafia tylko na jedno żebro', 'lub kilka żeber'], 'R')


if os.environ.get('PTS'):
    print('sternum A', PA(0, 0), 'rib R lat', PA(12.15, 8.5), 'SC', SC, 'L7', L7)
f.save()
