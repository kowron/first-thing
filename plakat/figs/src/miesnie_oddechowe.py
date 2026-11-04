# MIĘŚNIE ODDECHOWE (Bochenek, t. I, s. 693, 696–697; streszczenie s. 701) – schemat kierunku działania.
# Klatka piersiowa od przodu (prawa strona ciała po lewej stronie rysunku):
#   lewa połowa rysunku (prawa strona ciała) – mięśnie wdechowe: główne – przepona i mm. międzyżebrowe zewnętrzne;
#     pomocnicze – mm. pochyłe, m. mostkowo-obojczykowo-sutkowy, m. podobojczykowy, m. piersiowy mniejszy i większy,
#     m. zębaty przedni (strzałki niebieskie – kierunek pociągania żeber / mostka);
#   prawa połowa rysunku (lewa strona ciała) – mięśnie wydechowe: mm. międzyżebrowe wewnętrzne, m. poprzeczny klatki
#     piersiowej (za mostkiem), pomocnicze – mięśnie brzucha, m. najszerszy grzbietu („mięsień kaszlu”) (strzałki czerwone).
# Wstawka: m. zębaty tylny górny – od tyłu (pomocniczy wdechowy).
# Przebieg włókien mm. międzyżebrowych wg s. 685–686: zewnętrzne – ku dołowi i do mostka, wewnętrzne – ku dołowi
# i w stronę kręgosłupa. M. poprzeczny klatki piersiowej wg s. 688. M. najszerszy grzbietu – s. 654–655.
# Schemat własny; mięśnie uproszczone (pasma pokazujące kierunek działania), m. piersiowy większy – tylko część dolna.
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 150, 110
f = Fig('miesnie_oddechowe', W, H,
        caption='mięśnie oddechowe · klatka piersiowa od przodu (prawa strona ciała po lewej) · schemat kierunku działania')
S = 1.25                     # mm na cm
CX, Y0 = 75.0, 27.0          # oś pośrodkowa; górny brzeg trzonu Th1
YTOPC, YBOTC = -11.0, 33.0   # linie cięcia (cm)


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
    rng = range(1, m + 1) if closed else range(1, m)
    for i in rng:
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


def poly(pts):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + ' Z'


def line(pts):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts)


def band(pts, w0, w1=None, n=10, cap0=False, cap1=False):
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
        a1 = math.atan2(q[1] - center[1], q[0] - center[0])
        da = a1 - a0
        while da > 0: da -= 2 * math.pi
        if abs(da) < math.pi * 0.9: da += 2 * math.pi
        da = -math.pi if da < 0 else math.pi
        return [(center[0] + w * math.cos(a0 + da * j / k), center[1] + w * math.sin(a0 + da * j / k)) for j in range(1, k)]
    out = list(left)
    if cap1:
        out += capf(left[-1], right[-1], c[-1], w1 / 2)
    out += right[::-1]
    if cap0:
        out += capf(right[0], left[0], c[0], w0 / 2)
    return out


def add(cls, d):
    f.add(f'<path class="{cls}" d="{d}"/>')


def P(u, y, side):
    """punkt rysunku: u – odległość od płaszczyzny pośrodkowej (cm), side=-1 prawa strona ciała (lewa rysunku)"""
    return (CX + side * S * u, Y0 + S * y)


def PS(pts, side):
    return [P(u, y, side) for u, y in pts]


def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


# ---------------------------------------------------------------- klatka od przodu (dane jak w oddychanie_wymiary.py)
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
STERN_HALF = [(0, 4.5), (1.3, 4.1), (2.5, 3.8), (2.75, 4.9), (2.35, 6.2), (1.65, 8.2), (1.55, 8.9), (1.65, 9.3),
              (1.85, 11.6), (1.95, 14.0), (2.05, 16.4), (1.95, 18.5), (1.5, 19.7), (1.0, 20.1), (0.95, 21.9), (0.45, 23.1)]
DIA_E = [(14.3, 28.4), (13.6, 24.5), (11.6, 19.8), (8.6, 17.2), (5.6, 16.7), (2.6, 17.6), (0.0, 18.2),
         (-2.6, 18.0), (-5.8, 17.6), (-8.8, 18.3), (-11.7, 20.9), (-13.6, 25.2), (-14.3, 28.6)]


def rib_mid(a, j):
    return (a[0] - (a[0] - j[0]) * 0.30, a[1] + (j[1] - a[1]) * 0.60)


RIBC = [cr([RA[k], rib_mid(RA[k], RJ[k]), RJ[k]], n=20) for k in range(12)]     # osie żeber (od boku do chrząstki)


def rib_y(k, u):
    """y osi żebra k dla danego u (część kostna, od A do J)"""
    c = RIBC[k]
    for (u0, y0), (u1, y1) in zip(c, c[1:]):
        if (u0 - u) * (u1 - u) <= 0 and u0 != u1:
            return y0 + (y1 - y0) * (u - u0) / (u1 - u0)
    return None


def rib_pt(k, u):
    return (u, rib_y(k, u))


def rib_y2(k, u):
    """jak rib_y, ale poza zakresem osi – y skrajnego punktu"""
    y = rib_y(k, u)
    if y is None:
        y = RA[k][1] if u >= RA[k][0] else RJ[k][1]
    return y


# ================================================================ 1. łopatka (za klatką), m. poprzeczny klatki piersiowej
SCAP = [(8.2, -0.6), (10.4, 0.0), (12.4, 0.7), (14.6, 0.6), (16.4, 0.0), (18.6, -0.1), (19.1, 0.8), (17.0, 1.6),
        (16.3, 2.6), (16.0, 4.5), (16.1, 6.4), (14.6, 9.2), (12.8, 13.5), (11.4, 17.4), (10.6, 17.3), (8.9, 11.5),
        (7.8, 5.0)]
for sd in (-1, 1):
    add('bone', smooth(PS(SCAP, sd), closed=True, t=0.35))
    add('facet', smooth(PS([(16.3, 2.7), (16.75, 3.4), (16.85, 4.6), (16.6, 6.0), (16.1, 6.2), (16.05, 4.4), (16.15, 3.0)], sd),
                        closed=True, t=0.4))
# m. poprzeczny klatki piersiowej (lewa strona ciała – prawa rysunku): od tylnej powierzchni dolnej części mostka
# i wyrostka mieczykowatego do granicy chrzęstno-kostnej żeber II–VI; włókna dolne poprzeczne, górne skośnie ku górze
TT_BASE = [15.4, 16.8, 18.2, 19.6, 21.2]
TT = []
for i, k in enumerate(range(1, 6)):
    j = RJ[k]
    b = (0.5, TT_BASE[i])
    mid = lerp(b, j, 0.5)
    pts = PS([b, mid, (j[0] - 0.2, j[1] + 0.1)], 1)
    TT.append(pts)
    add('muscle', poly(band(pts, 1.5 * S, 0.8 * S, cap1=True)))
    add('musclel', line(pts))

# ================================================================ 2. mm. międzyżebrowe (pod żebrami)


def space_poly(k, u0, u1, n=8):
    us = [u0 + (u1 - u0) * i / n for i in range(n + 1)]
    top = [rib_pt(k, u) for u in us]
    bot = [rib_pt(k + 1, u) for u in us[::-1]]
    return top + bot


def space_fibers(k, u0, u1, du, n=6):
    """włókna od żebra k do żebra k+1 przesunięte o du (cm) w osi u"""
    out = []
    for i in range(n + 1):
        ua = u0 + (u1 - u0) * i / n
        ub = ua + du
        if not (min(u0, u1) - 0.01 <= ub <= max(u0, u1) + 0.01):
            continue
        ya, yb = rib_y(k, ua), rib_y(k + 1, ub)
        if ya is None or yb is None:
            continue
        out.append(((ua, ya), (ub, yb)))
    return out


# zewnętrzne (prawa strona ciała): włókna ku dołowi i do mostka (przyśrodkowo)
EXT = []
for k in range(3, 8):
    u0 = max(RJ[k][0], RJ[k + 1][0]) + 0.2
    u1 = RA[k][0] - 0.9
    pts = space_poly(k, u0, u1)
    add('muscle', poly(PS(pts, -1)))
    for a, b in space_fibers(k, u0, u1, -0.9, n=7):
        add('musclel', line(PS([a, b], -1)))
    EXT.append((k, u0, u1))
# wewnętrzne (lewa strona ciała): włókna ku dołowi i w stronę kręgosłupa (bocznie)
INT = []
for k in range(2, 7):
    u0 = max(RJ[k][0], RJ[k + 1][0]) + 0.2
    u1 = RA[k][0] - 0.9
    pts = space_poly(k, u0, u1)
    add('muscle', poly(PS(pts, 1)))
    for a, b in space_fibers(k, u0, u1, 0.9, n=7):
        add('musclel', line(PS([a, b], 1)))
    INT.append((k, u0, u1))

# ================================================================ 3. kręgosłup szyjny, żebra, mostek
# trzony C3–Th2 (od przodu) z wyrostkami poprzecznymi
VERT = []
y = -0.5
for name, h, hw in (('C7', 1.5, 1.25), ('C6', 1.4, 1.2), ('C5', 1.4, 1.15), ('C4', 1.4, 1.1), ('C3', 1.4, 1.1), ('C2', 1.6, 1.1)):
    VERT.append((y - h, y, hw, 2.75 if name != 'C7' else 3.2))
    y -= h + 0.45
for yt, yb, hw, tp in VERT + [(0.0, 2.0, 1.45, 3.4), (2.5, 4.6, 1.55, 3.6)]:
    ym = (yt + yb) / 2
    for sd in (-1, 1):
        add('bone', smooth(PS([(hw - 0.3, ym - 0.35), (tp - 0.2, ym - 0.45), (tp, ym), (tp - 0.2, ym + 0.45), (hw - 0.3, ym + 0.35)], sd),
                           closed=True, t=0.3))
    add('bone', smooth([P(hw, yt + 0.2, -1), P(hw - 0.25, yt, -1), P(hw - 0.25, yt, 1), P(hw, yt + 0.2, 1),
                        P(hw + 0.05, yb - 0.2, 1), P(hw - 0.2, yb, 1), P(hw - 0.2, yb, -1), P(hw + 0.05, yb - 0.2, -1)],
                       closed=True, t=0.25))
for (yt, yb, hw, tp), (yt2, yb2, hw2, tp2) in zip(VERT[::-1][1:] + [(0.0, 2.0, 1.45, 3.4)], VERT[::-1][:1] + VERT[::-1][2:]):
    pass
# krążki między trzonami
seq = sorted(VERT + [(0.0, 2.0, 1.45, 3.4), (2.5, 4.6, 1.55, 3.6)])
for (yt, yb, hw, tp), (yt2, yb2, hw2, tp2) in zip(seq, seq[1:]):
    w = min(hw, hw2) - 0.15
    add('annulus', poly([P(w, yb, -1), P(w, yb, 1), P(w, yt2, 1), P(w, yt2, -1)]))
# tylne części żeber I–II (od głowy do najbardziej bocznego punktu)
for k, head in ((0, (1.5, 0.9)), (1, (1.6, 3.4))):
    for sd in (-1, 1):
        pts = PS([head, ((head[0] + RA[k][0]) / 2, (head[1] + RA[k][1]) / 2 - 0.25), RA[k]], sd)
        add('bone', poly(band(pts, RW[k][0] * S * 0.95, RW[k][0] * S, cap0=True)))
# żebra (część przednia) i chrząstki
for sd in (-1, 1):
    for k in range(12):
        a, j = RA[k], RJ[k]
        add('bone', poly(band(PS([a, rib_mid(a, j), j], sd), RW[k][0] * S, RW[k][1] * S, cap0=True, cap1=(k >= 10))))
    for k in range(12):
        w = (0.95 if k < 10 else 0.6) * S
        add('cart', poly(band(PS(CART[k], sd), w, w * (0.95 if k < 7 else 0.8), cap1=(k >= 7))))
outline = PS(STERN_HALF, -1) + [P(0, 23.5, -1)] + PS(list(reversed(STERN_HALF[1:])), 1)
add('bone', smooth(outline, closed=True, t=0.35))
for yy in (8.95, 19.75):
    hw = 1.55 if yy < 10 else 1.45
    add('bonel', line([P(hw, yy, -1), P(hw, yy, 1)]))

# ================================================================ 4. mięśnie wdechowe pomocnicze (prawa strona ciała)
L = -1
# mm. pochyłe: od wyrostków poprzecznych C3–C7 do I i II żebra (przyczepy żebrowe za obojczykiem)
SCAL = [([(2.7, -10.6), (3.7, -4.5), (5.4, 1.6)], 1.0, 1.25),     # środkowy
        ([(3.0, -4.6), (4.9, -0.8), (7.3, 3.4)], 0.8, 1.0),       # tylny
        ([(2.4, -8.8), (3.0, -3.5), (4.3, 2.6)], 0.95, 1.1)]      # przedni
for pts, w0, w1 in SCAL:
    pp = PS(pts, L)
    add('muscle', poly(band(pp, w0 * S, w1 * S)))
    add('musclel', line(pp))
# m. podobojczykowy: I żebro (granica kostno-chrzęstna) → dolna powierzchnia obojczyka
SUBCL = PS([(3.9, 4.95), (7.0, 4.35), (10.4, 3.45)], L)
add('muscle', poly(band(SUBCL, 1.0 * S, 0.65 * S, cap0=True, cap1=True)))
# m. piersiowy mniejszy: żebra III–V → wyrostek kruczy
PMIN = [(7.4, 11.4), (8.0, 12.7), (8.7, 14.2), (9.4, 15.6), (10.0, 16.9), (11.0, 16.4), (11.9, 15.6),
        (13.3, 10.6), (14.4, 5.5), (14.0, 4.9), (13.3, 5.0), (10.5, 8.2)]
add('muscle', smooth(PS(PMIN, L), closed=True, t=0.25))
for o in ((7.9, 12.2), (8.9, 14.5), (9.8, 16.3), (11.2, 16.0)):
    add('musclel', line(PS([o, (13.95, 5.3)], L)))
# wyrostek kruczy (nad m. piersiowym mniejszym)
for sd in (-1, 1):
    add('bone', poly(band(PS([(12.5, 1.4), (13.4, 2.8), (14.2, 4.6)], sd), 1.0 * S, 0.8 * S, cap1=True)))
# m. zębaty przedni: zęby na żebrach IV–IX (boczna ściana klatki), dalej ku tyłowi do łopatki
SA_K = range(3, 9)
sa = [(RA[2][0] + 0.2, RA[2][1] + 1.6)]
for k in SA_K:
    sa.append((RA[k][0] + 0.45, RA[k][1] + 0.3))
sa.append((RA[8][0] + 0.2, RA[8][1] + 1.3))
teeth = []
for k in list(SA_K)[::-1]:
    ut = RA[k][0] - 2.4
    teeth.append(rib_pt(k, ut))
    teeth.append((RA[k][0] - 0.7, (rib_y2(k, RA[k][0] - 0.7) + rib_y2(k - 1, RA[k][0] - 0.7)) / 2))
SA = sa + teeth
add('muscle', poly(PS(SA, L)))
for k in SA_K:
    a = rib_pt(k, RA[k][0] - 2.0)
    add('musclel', line(PS([a, (RA[k][0] + 0.3, RA[k][1] - 1.4)], L)))
# m. piersiowy większy (część dolna): mostek / chrząstki V–VI → grzebień guzka większego kości ramiennej
PMAJ = [(2.1, 15.2), (5.0, 14.2), (9.0, 12.4), (13.0, 10.3), (16.6, 8.1), (18.7, 7.1), (19.2, 9.6), (16.8, 11.2),
        (13.4, 14.4), (9.6, 17.4), (6.0, 19.6), (3.4, 20.5), (2.0, 19.0)]

# ================================================================ 5. kości obręczy i ramienia
CLAV = [(2.7, 4.1), (5.0, 3.45), (8.0, 2.9), (11.0, 2.3), (14.0, 1.55), (16.7, 0.75)]
HUM_SHAFT = [(18.6, 6.0), (19.0, 14.0), (19.4, 24.0), (19.7, 36.0)]
for sd in (-1, 1):
    add('bone', poly(band(PS(HUM_SHAFT, sd), 2.5 * S, 2.0 * S)))
    add('bone', smooth(PS([(16.0, 4.3), (16.4, 2.4), (17.8, 1.6), (19.8, 2.0), (20.9, 3.4), (20.6, 5.4), (19.6, 6.8),
                           (17.6, 7.0), (16.4, 5.9)], sd), closed=True, t=0.4))
    add('bonel', line(PS([(19.9, 2.2), (19.4, 3.4), (19.6, 5.2), (19.9, 6.4)], sd)))
    add('bone', poly(band(PS(CLAV, sd), 1.75 * S, 1.2 * S, cap0=True, cap1=True)))
# m. piersiowy większy – na wierzchu (pokrywa dolną część m. piersiowego mniejszego)
add('muscle', smooth(PS(PMAJ, L), closed=True, t=0.25))
for o, e in (((2.4, 16.2), (18.7, 7.8)), ((2.6, 18.2), (18.8, 8.6)), ((4.5, 19.8), (19.0, 9.3)), ((7.5, 17.9), (18.9, 8.9))):
    add('musclel', line(PS([o, e], L)))

# m. mostkowo-obojczykowo-sutkowy: głowa boczna (obojczyk) i przyśrodkowa (rękojeść mostka) → wyrostek sutkowaty
add('muscle', poly(band(PS([(4.1, 3.4), (4.7, -0.5), (5.2, -4.5), (5.6, -9.0)], L), 1.7 * S, 1.2 * S, cap0=True)))
SCM = PS([(0.9, 5.2), (2.4, 0.4), (4.1, -4.6), (5.4, -9.0), (6.0, -12.5)], L)
add('muscle', poly(band(SCM, 1.25 * S, 1.9 * S, cap0=True)))
add('musclel', line(SCM))

# ================================================================ 6. mięśnie wydechowe pomocnicze (lewa strona ciała)
R = 1
# mięśnie brzucha: m. prosty brzucha (z smugami ścięgnistymi) i m. skośny zewnętrzny brzucha
RECT = [(0.6, 22.0), (1.6, 19.6), (3.4, 18.3), (5.6, 17.6), (7.5, 18.0), (7.7, 21.0), (7.5, 26.0), (7.3, 34.5), (0.6, 34.5)]
add('muscle', poly(PS(cr(RECT[:6], n=4) + RECT[6:], R)))
for yy in (24.3, 29.6):
    add('tendon', poly(PS([(0.6, yy - 0.35), (7.6, yy - 0.6), (7.55, yy + 0.25), (0.6, yy + 0.45)], R)))
for u in (2.2, 3.9, 5.6):
    add('musclel', line(PS([(u, 19.2 if u < 4 else 18.4), (u, 34.5)], R)))
EO = [(7.6, 25.2), (9.4, 24.6)]
for k in range(7, 12):
    EO.append(rib_pt(k, RA[k][0] - 1.6) if k < 10 else (RA[k][0] - 0.5, RA[k][1] + 0.4))
EO += [(14.2, 30.0), (14.6, 34.5), (7.5, 34.5), (7.6, 30.0)]
add('muscle', poly(PS(EO, R)))
for a, b in (((10.5, 25.4), (8.0, 29.0)), ((12.0, 26.7), (8.6, 32.0)), ((13.3, 28.0), (9.6, 34.5)), ((14.1, 31.0), (12.0, 34.5))):
    add('musclel', line(PS([a, b], R)))
# m. najszerszy grzbietu – część boczna (brzeg boczny), dochodzi do kości ramiennej
LD = PS([(15.6, 36.0), (16.1, 28.0), (16.5, 21.0), (17.0, 14.5), (17.8, 9.6)], R)
add('muscle', poly(band(LD, 2.6 * S, 1.1 * S)))
add('musclel', line(LD))

# ================================================================ 7. przepona
dA = [P(-u, y, -1) for u, y in DIA_E]          # u ze znakiem: + prawa strona ciała → lewa rysunku
add('muscle', poly(band(dA, 1.1 * S, n=12)))
add('tendon', poly(band(dA[4:9], 1.1 * S, n=12)))

# ================================================================ 8. strzałki kierunku działania
# wdech (niebieskie): przepona w dół; żebra ku górze
xd = P(5.6, 0, L)[0]
f.arrow(f'M{xd:.2f},{P(0, 17.6, L)[1]:.2f} L{xd:.2f},{P(0, 22.4, L)[1]:.2f}')
f.arrow(line([P(10.4, 22.4, L), P(10.4, 19.0, L)]))                          # mm. międzyżebrowe zewn. – żebro w górę
f.arrow(line([P(6.6, 2.4, L), P(5.6, -1.6, L)]))                             # mm. pochyłe – I żebro w górę
f.arrow(line([P(1.0, 7.4, L), P(1.9, 3.2, L)]))                              # m. mostkowo-obojczykowo-sutkowy – mostek w górę
f.arrow(line([P(10.6, 13.0, L), P(12.7, 9.2, L)]))                           # m. piersiowy mniejszy
f.arrow(line([P(16.0, 21.0, L), P(17.4, 17.0, L)]))                          # m. zębaty przedni
# wydech (czerwone): żebra ku dołowi
f.arrow(line([P(11.2, 9.6, R), P(11.2, 13.4, R)]), red=True)                 # mm. międzyżebrowe wewn.
f.arrow(line([P(4.4, 26.5, R), P(4.4, 31.0, R)]), red=True)                  # mięśnie brzucha
f.arrow(line([P(19.2, 24.0, R), P(16.2, 24.0, R)]), red=True)                # m. najszerszy grzbietu – nacisk na żebra
f.arrow(line([P(7.2, 13.6, R), P(5.0, 15.6, R)]), red=True)                  # m. poprzeczny klatki piersiowej

# przycięcie u góry i u dołu
body = ''.join(f.body)
f.body = [f'<defs><clipPath id="cp_mo"><rect x="0" y="{Y0 + S * YTOPC:.2f}" width="{W}" height="{S * (YBOTC - YTOPC):.2f}"/>'
          f'</clipPath></defs><g clip-path="url(#cp_mo)">{body}</g>']

# ================================================================ nagłówki
f.text(26.0, 6.0, 'mięśnie wdechowe', cls='big', anchor='middle')
f.text(124.0, 6.0, 'mięśnie wydechowe', cls='big', anchor='middle')

# ================================================================ podpisy – wdechowe (lewa kolumna)
XL = 47.0
f.label(P(5.0, -6.5, L), 'm. mostkowo-obojczykowo-sutkowy', 'm. sternocleidomastoideus', (XL, 13.0), side='L')
f.label(P(5.9, 0.6, L), 'mm. pochyłe', 'mm. scaleni', (XL, 23.0), side='L')
f.label(P(8.4, 4.0, L), 'm. podobojczykowy', 'm. subclavius', (XL, 32.0), side='L')
f.label(P(12.6, 8.4, L), 'm. piersiowy mniejszy', 'm. pectoralis minor', (XL, 41.0), side='L')
f.label(P(12.0, 12.6, L), 'm. piersiowy większy', 'm. pectoralis major', (XL, 50.0), side='L')
f.label(P(14.3, 19.6, L), 'm. zębaty przedni', 'm. serratus anterior', (XL, 59.0), side='L')
f.label(P(11.6, 22.6, L), 'mm. międzyżebrowe zewnętrzne', 'mm. intercostales externi', (XL, 68.0), side='L')
f.label(P(8.0, 18.0, L), 'przepona', 'diaphragma', (XL, 77.0), side='L')
# wydechowe (prawa kolumna)
XR = 103.0
f.label(P(10.4, 11.4, R), 'mm. międzyżebrowe wewnętrzne', 'mm. intercostales interni', (XR, 30.0), side='R')
f.label(P(4.6, 12.6, R), 'm. poprzeczny klatki piersiowej', 'm. transversus thoracis', (XR, 39.0), side='R')
f.label(P(16.6, 19.0, R), 'm. najszerszy grzbietu', 'm. latissimus dorsi', (XR, 50.0), side='R')
f.label(P(10.0, 30.0, R), 'mięśnie brzucha', None, (XR, 62.0), side='R')

f.save()
print('ok')
