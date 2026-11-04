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
# Schemat własny; mięśnie uproszczone (pasma pokazujące kierunek działania), m. piersiowy większy – tylko część
# mostkowo-żebrowa (pasmo nad m. piersiowym mniejszym). Klatka – dane jak w oddychanie_wymiary.py.
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 150, 110
f = Fig('miesnie_oddechowe', W, H,
        caption='mięśnie oddechowe · klatka piersiowa od przodu (prawa strona ciała po lewej) · schemat kierunku działania')
S = 1.35                     # mm na cm
CX, Y0 = 75.0, 30.0          # oś pośrodkowa; górny brzeg trzonu Th1
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


def rib_hw(k, u):
    """połowa szerokości żebra k w miejscu u (cm)"""
    a, j = RA[k][0], RJ[k][0]
    t = min(max((a - u) / (a - j), 0.0), 1.0)
    return (RW[k][0] + (RW[k][1] - RW[k][0]) * t) / 2


def gap_poly(k, u0, u1, n=10):
    """przestrzeń międzyżebrowa między żebrem k i k+1 (dokładnie między brzegami żeber), u0 < u1"""
    us = [u0 + (u1 - u0) * i / n for i in range(n + 1)]
    top = [(u, rib_y(k, u) + 1.08 * rib_hw(k, u)) for u in us]
    bot = [(u, rib_y(k + 1, u) - 1.08 * rib_hw(k + 1, u)) for u in us[::-1]]
    return top + bot


def gap_fibers(k, u0, u1, du, n=7):
    out = []
    for i in range(n + 1):
        ua = u0 + (u1 - u0) * (i + 0.5) / (n + 1)
        ub = ua + du
        if not (u0 <= ub <= u1):
            continue
        out.append(((ua, rib_y(k, ua) + 1.08 * rib_hw(k, ua)), (ub, rib_y(k + 1, ub) - 1.08 * rib_hw(k + 1, ub))))
    return out


L, R = -1, 1

# ================================================================ 1. warstwa najgłębsza: łopatki, m. poprzeczny klatki piersiowej
SCAP = [(8.2, -0.6), (10.4, 0.0), (12.4, 0.7), (14.6, 0.6), (16.4, 0.0), (18.6, -0.1), (19.1, 0.8), (17.0, 1.6),
        (16.3, 2.6), (16.0, 4.5), (16.1, 6.4), (14.6, 9.2), (12.8, 13.5), (11.4, 17.4), (10.6, 17.3), (8.9, 11.5),
        (7.8, 5.0)]
for sd in (L, R):
    add('bone', smooth(PS(SCAP, sd), closed=True, t=0.35))
# m. poprzeczny klatki piersiowej (lewa strona ciała): tylna powierzchnia dolnej części trzonu mostka i wyrostka
# mieczykowatego → granica chrzęstno-kostna żeber II–VI; włókna dolne poprzeczne, górne skośnie ku górze i bocznie
TT_BASE = [15.6, 17.0, 18.4, 19.8, 21.4]
for i, k in enumerate(range(1, 6)):
    j = RJ[k]
    b = (0.4, TT_BASE[i])
    pts = PS([b, lerp(b, j, 0.5), (j[0] - 0.15, j[1] + 0.05)], R)
    add('muscle', poly(band(pts, 1.5 * S, 0.75 * S, cap1=True)))
    add('musclel', line(pts))

# ================================================================ 2. kręgosłup szyjny (C2–C7) i Th1–Th2, żebra, mostek
VERT = []
yy = -0.5
for name, h, hw in (('C7', 1.5, 1.25), ('C6', 1.4, 1.2), ('C5', 1.4, 1.15), ('C4', 1.4, 1.1), ('C3', 1.4, 1.1), ('C2', 1.7, 1.1)):
    VERT.append((yy - h, yy, hw, 3.2 if name == 'C7' else 2.75))
    yy -= h + 0.45
VERT += [(0.0, 2.0, 1.45, 3.4), (2.5, 4.6, 1.55, 3.6)]
VERT.sort()
for (yt, yb, hw, tp), (yt2, yb2, hw2, tp2) in zip(VERT, VERT[1:]):
    w = min(hw, hw2) - 0.15
    add('annulus', poly([P(w, yb, L), P(w, yb, R), P(w, yt2, R), P(w, yt2, L)]))
for yt, yb, hw, tp in VERT:
    ym = (yt + yb) / 2
    for sd in (L, R):
        add('bone', smooth(PS([(hw - 0.3, ym - 0.35), (tp - 0.2, ym - 0.45), (tp, ym), (tp - 0.2, ym + 0.45),
                               (hw - 0.3, ym + 0.35)], sd), closed=True, t=0.3))
    add('bone', smooth([P(hw, yt + 0.2, L), P(hw - 0.25, yt, L), P(hw - 0.25, yt, R), P(hw, yt + 0.2, R),
                        P(hw + 0.05, yb - 0.2, R), P(hw - 0.2, yb, R), P(hw - 0.2, yb, L), P(hw + 0.05, yb - 0.2, L)],
                       closed=True, t=0.25))
# tylne części żeber I–II (od głowy do punktu najbardziej bocznego)
for k, head in ((0, (1.5, 0.9)), (1, (1.6, 3.4))):
    for sd in (L, R):
        pts = PS([head, ((head[0] + RA[k][0]) / 2, (head[1] + RA[k][1]) / 2 - 0.25), RA[k]], sd)
        add('bone', poly(band(pts, RW[k][0] * S * 0.95, RW[k][0] * S, cap0=True)))
for sd in (L, R):
    for k in range(12):
        a, j = RA[k], RJ[k]
        add('bone', poly(band(PS([a, rib_mid(a, j), j], sd), RW[k][0] * S, RW[k][1] * S, cap0=True, cap1=(k >= 10))))
    for k in range(12):
        w = (0.95 if k < 10 else 0.6) * S
        add('cart', poly(band(PS(CART[k], sd), w, w * (0.95 if k < 7 else 0.8), cap1=(k >= 7))))
outline = PS(STERN_HALF, L) + [P(0, 23.5, L)] + PS(list(reversed(STERN_HALF[1:])), R)
add('bone', smooth(outline, closed=True, t=0.35))
for y in (8.95, 19.75):
    hw = 1.55 if y < 10 else 1.45
    add('bonel', line([P(hw, y, L), P(hw, y, R)]))

# ================================================================ 3. przepona (głębiej niż mięśnie ściany klatki)
dA = [P(-u, y, L) for u, y in DIA_E]
add('muscle', poly(band(dA, 1.1 * S, n=12)))
add('tendon', poly(band(dA[4:9], 1.1 * S, n=12)))

# ================================================================ 4. mm. międzyżebrowe (w przestrzeniach między żebrami)
# zewnętrzne (prawa strona ciała – wdech): włókna ku dołowi i do mostka (przyśrodkowo)
for k in range(3, 8):
    u0 = max(RJ[k][0], RJ[k + 1][0]) + 0.15
    u1 = RA[k][0] - 0.7
    add('muscle', poly(PS(gap_poly(k, u0, u1), L)))
    for a, b in gap_fibers(k, u0, u1, -0.9):
        add('musclel', line(PS([a, b], L)))
# wewnętrzne (lewa strona ciała – wydech): włókna ku dołowi i w stronę kręgosłupa (bocznie)
for k in range(2, 7):
    u0 = max(RJ[k][0], RJ[k + 1][0]) + 0.15
    u1 = RA[k][0] - 0.7
    add('muscle', poly(PS(gap_poly(k, u0, u1), R)))
    for a, b in gap_fibers(k, u0, u1, 0.9):
        add('musclel', line(PS([a, b], R)))

# ================================================================ 5. mięśnie wdechowe pomocnicze (prawa strona ciała)
# mm. pochyłe: wyrostki poprzeczne C3–C7 → I żebro (przedni, środkowy), II żebro (tylny); przyczepy za obojczykiem
SCAL = [([(2.7, -10.6), (3.7, -4.5), (5.4, 1.6)], 1.0, 1.25),     # środkowy
        ([(3.0, -4.6), (4.9, -0.8), (7.3, 3.4)], 0.8, 1.0),       # tylny
        ([(2.4, -8.8), (3.0, -3.5), (4.3, 2.6)], 0.95, 1.1)]      # przedni
for pts, w0, w1 in SCAL:
    pp = PS(pts, L)
    add('muscle', poly(band(pp, w0 * S, w1 * S)))
    add('musclel', line(pp))
# m. podobojczykowy: I żebro (granica kostno-chrzęstna) → dolna powierzchnia obojczyka
add('muscle', poly(band(PS([(3.9, 5.0), (7.0, 4.4), (10.4, 3.5)], L), 1.05 * S, 0.7 * S, cap0=True, cap1=True)))
# m. zębaty przedni: zęby (języczki) na bocznych odcinkach żeber IV–IX; mięsień biegnie dalej ku tyłowi do łopatki
SA_K = list(range(3, 9))
SA_TIP = []
for k in SA_K:
    ut = RA[k][0] - (2.0 if k < 5 else 2.5)
    pts = [(RA[k][0] + 0.55, RA[k][1] - 0.9), (RA[k][0] - 0.3, rib_y2(k, RA[k][0] - 0.3) - 0.1),
           (ut, rib_y(k, ut) + 0.1)]
    pp = PS(pts, L)
    add('muscle', poly(band(pp, 1.75 * S, 0.7 * S, cap1=True)))
    add('musclel', line(pp))
    SA_TIP.append(pts)
# m. piersiowy mniejszy: przednie końce żeber III–V → wyrostek kruczy
o = [(RJ[k][0] + 0.15, rib_y(k, RJ[k][0] + 0.15)) for k in (2, 3, 4)]
o5b = (RJ[4][0] + 1.7, rib_y(4, RJ[4][0] + 1.7))
COR = (14.1, 4.9)
PMIN = [o[0], o[1], o[2], o5b, (12.6, 11.0), (14.55, 5.3), (14.2, 4.6), (13.6, 4.75), (10.6, 7.6)]
add('muscle', smooth(PS(PMIN, L), closed=True, t=0.15))
for q in (o[0], lerp(o[0], o[1], 0.5), o[1], lerp(o[1], o[2], 0.5), o[2], lerp(o[2], o5b, 0.6)):
    add('musclel', line(PS([(q[0] + 0.2, q[1] - 0.2), (COR[0] + 0.1, COR[1] + 0.5)], L)))

# ================================================================ 6. mięśnie wydechowe pomocnicze (lewa strona ciała)
# mięśnie brzucha: m. prosty brzucha (ze smugami ścięgnistymi) i m. skośny zewnętrzny brzucha
RECT = [(0.6, 22.2), (1.7, 19.6), (3.6, 18.2), (5.8, 17.6), (7.6, 18.2), (7.8, 21.0), (7.6, 26.0), (7.4, 36.0), (0.6, 36.0)]
add('muscle', poly(PS(cr(RECT[:6], n=4) + RECT[6:], R)))
for y in (24.4, 29.8):
    add('tendon', poly(PS([(0.6, y - 0.35), (7.65, y - 0.6), (7.6, y + 0.25), (0.6, y + 0.45)], R)))
for u in (2.3, 4.0, 5.8):
    add('musclel', line(PS([(u, 19.0 if u < 4 else 18.2), (u, 36.0)], R)))
EO = [(7.7, 24.4), (9.8, 24.0), (11.8, 23.4), (13.5, 22.6), (14.8, 22.4), (15.1, 25.0), (14.8, 28.5), (14.5, 32.0),
      (14.4, 36.0), (7.6, 36.0), (7.75, 30.0)]
add('muscle', smooth(PS(EO, R), closed=True, t=0.2))
for a, b in (((10.4, 24.4), (8.0, 27.6)), ((12.4, 24.0), (8.3, 30.6)), ((14.1, 23.6), (8.8, 33.8)), ((14.4, 27.2), (10.6, 35.8)),
             ((14.4, 31.0), (12.8, 35.8))):
    add('musclel', line(PS([a, b], R)))

# ================================================================ 7. kości obręczy i ramienia
CLAV = [(2.7, 4.1), (5.0, 3.45), (8.0, 2.9), (11.0, 2.3), (14.0, 1.55), (16.7, 0.75)]
HUM = [(18.6, 6.0), (19.0, 14.0), (19.4, 24.0), (19.7, 36.0)]
for sd in (L, R):
    add('bone', poly(band(PS(HUM, sd), 2.5 * S, 2.0 * S)))
    add('bone', smooth(PS([(16.0, 4.3), (16.4, 2.4), (17.8, 1.6), (19.8, 2.0), (20.9, 3.4), (20.6, 5.4), (19.6, 6.8),
                           (17.6, 7.0), (16.4, 5.9)], sd), closed=True, t=0.4))
    add('bonel', line(PS([(19.9, 2.2), (19.4, 3.4), (19.6, 5.2), (19.9, 6.4)], sd)))
    add('bone', poly(band(PS([(12.4, 1.5), (13.3, 2.9), (14.2, 4.7)], sd), 1.0 * S, 0.8 * S, cap1=True)))   # wyrostek kruczy
    add('bone', poly(band(PS(CLAV, sd), 1.75 * S, 1.2 * S, cap0=True, cap1=True)))

# m. najszerszy grzbietu – brzeg boczny (lewa strona ciała), do kości ramiennej
LD = PS([(15.7, 36.0), (16.2, 28.0), (16.6, 21.0), (17.0, 14.5), (17.7, 9.4)], R)
add('muscle', poly(band(LD, 2.6 * S, 1.1 * S)))
add('musclel', line(LD))

# m. piersiowy większy (prawa strona ciała) – część mostkowo-żebrowa jako pasmo (warstwa powierzchowna,
# przykrywa m. piersiowy mniejszy): mostek i chrząstki żeber → grzebień guzka większego kości ramiennej
PMAJ = [(1.9, 13.4), (6.0, 13.0), (10.5, 11.3), (14.8, 8.8), (18.2, 6.6), (19.0, 6.9), (19.1, 9.3), (18.4, 9.8),
        (14.8, 12.6), (10.4, 16.0), (6.0, 18.4), (2.1, 19.2)]
add('muscle', smooth(PS(PMAJ, L), closed=True, t=0.25))
for q, e in (((2.1, 14.6), (18.6, 7.3)), ((2.1, 16.2), (18.7, 7.9)), ((2.1, 17.8), (18.8, 8.5)), ((4.6, 18.6), (18.8, 9.1))):
    add('musclel', line(PS([q, e], L)))

# m. mostkowo-obojczykowo-sutkowy: głowa boczna (obojczyk) i przyśrodkowa (rękojeść mostka) → wyrostek sutkowaty
add('muscle', poly(band(PS([(4.1, 3.4), (4.7, -0.5), (5.2, -4.5), (5.6, -9.0)], L), 1.7 * S, 1.2 * S, cap0=True)))
SCM = PS([(0.9, 5.2), (2.4, 0.4), (4.1, -4.6), (5.4, -9.0), (6.0, -12.5)], L)
add('muscle', poly(band(SCM, 1.25 * S, 1.9 * S, cap0=True)))
add('musclel', line(SCM))

# ================================================================ 8. strzałki kierunku działania
# wdech (niebieskie)
xd = P(5.4, 0, L)[0]
f.arrow(f'M{xd:.2f},{P(0, 17.8, L)[1]:.2f} L{xd:.2f},{P(0, 22.2, L)[1]:.2f}')        # przepona – w dół
f.arrow(line([P(11.0, 24.6, L), P(11.0, 21.0, L)]))                                     # mm. międzyżebrowe zewn.
f.arrow(line([P(6.2, 1.4, L), P(5.2, -2.6, L)]))                                        # mm. pochyłe
f.arrow(line([P(0.9, 7.6, L), P(1.6, 4.0, L)]))                                         # m. mostkowo-obojczykowo-sutkowy
f.arrow(line([P(11.4, 10.6, L), P(13.0, 7.2, L)]))                                      # m. piersiowy mniejszy
f.arrow(line([P(16.4, 20.6, L), P(17.4, 16.8, L)]))                                     # m. zębaty przedni
f.arrow(line([P(7.0, 16.6, L), P(11.4, 13.9, L)]))                                      # m. piersiowy większy
# wydech (czerwone)
f.arrow(line([P(11.3, 9.4, R), P(11.3, 13.0, R)]), red=True)                            # mm. międzyżebrowe wewn.
f.arrow(line([P(7.0, 12.9, R), P(4.8, 15.0, R)]), red=True)                             # m. poprzeczny kl. piersiowej
f.arrow(line([P(4.0, 26.6, R), P(4.0, 31.2, R)]), red=True)                             # mięśnie brzucha
f.arrow(line([P(20.0, 23.0, R), P(16.9, 23.0, R)]), red=True)                           # m. najszerszy grzbietu

# przycięcie u góry i u dołu
body = ''.join(f.body)
f.body = [f'<defs><clipPath id="cp_mo"><rect x="0" y="{Y0 + S * YTOPC:.2f}" width="{W}" height="{S * (YBOTC - YTOPC):.2f}"/>'
          f'</clipPath></defs><g clip-path="url(#cp_mo)">{body}</g>']

# ================================================================ 9. wstawka: m. zębaty tylny górny – od tyłu
S2 = 1.15
CX2, Y02 = 75.0, 85.6                   # oś; górny brzeg trzonu Th1 (wstawka)
U2, YT2, YB2 = 9.0, -5.2, 13.8          # zakres przycięcia (cm)
inset = []


def Q(u, y, side):
    """widok od tyłu: prawa strona ciała po prawej stronie rysunku"""
    return (CX2 + side * S2 * u, Y02 + S2 * y)


def QS(pts, side):
    return [Q(u, y, side) for u, y in pts]


def iadd(cls, d):
    inset.append(f'<path class="{cls}" d="{d}"/>')


YH2 = [0.9] + [(k - 1) * 2.45 + 0.4 for k in range(2, 8)]
for k in range(7):
    y0 = YH2[k]
    pts = [(2.6, y0), (4.6 + 0.25 * k, y0 + 0.35), (6.8 + 0.45 * k, y0 + 1.2 + 0.1 * k), (9.0 + 0.7 * k, y0 + 2.9 + 0.25 * k),
           (11.0 + 0.8 * k, y0 + 5.2 + 0.3 * k)]
    if k == 0:
        pts = [(2.6, y0), (4.4, y0 + 0.4), (5.9, y0 + 1.6), (6.4, y0 + 3.4)]
    for sd in (-1, 1):
        iadd('bone', poly(band(QS(pts, sd), 1.15 * S2, 1.15 * S2, cap0=True, cap1=(k == 0))))
# łuki kręgów, wyrostki poprzeczne i kolczyste C6–Th7
levels = [(-4.3, 'C6'), (-2.35, 'C7')] + [((k - 1) * 2.45 + 0.4 if k > 1 else 0.9, f'Th{k}') for k in range(1, 8)]
for y0, nm in levels:
    tp = 3.0 if nm.startswith('Th') else 2.4
    for sd in (-1, 1):
        iadd('bone', smooth(QS([(0.6, y0 - 0.55), (tp, y0 - 0.35), (tp + 0.3, y0 + 0.1), (tp, y0 + 0.55), (0.6, y0 + 0.75)], sd),
                            closed=True, t=0.3))
for y0, nm in levels:
    iadd('bone', smooth([Q(0.0, y0 - 0.6, 1), Q(0.45, y0 - 0.3, 1), Q(0.4, y0 + 1.4, 1), Q(0.0, y0 + 1.75, 1),
                         Q(0.4, y0 + 1.4, -1), Q(0.45, y0 - 0.3, -1)], closed=True, t=0.3))
# m. zębaty tylny górny (prawa strona ciała – prawa strona rysunku): wyrostki kolczyste C6–Th2 → żebra II–V
SPS_T = []                                   # zęby na żebrach II–V (tuż bocznie od kątów żeber)
for k in (1, 2, 3, 4):
    y0 = YH2[k]
    SPS_T.append((7.0 + 0.3 * k, y0 + 1.25 + 0.1 * k))
SPS = [(0.55, -4.4)]
for i, (ut, yt) in enumerate(SPS_T):
    SPS += [(ut - 0.9, yt - 0.9), (ut + 0.25, yt - 0.25), (ut + 0.1, yt + 0.55)]
SPS += [(SPS_T[-1][0] - 1.6, SPS_T[-1][1] + 0.3), (0.55, 3.0)]
iadd('muscle', poly(QS(SPS, 1)))
for i, (ut, yt) in enumerate(SPS_T):
    iadd('musclel', line(QS([(0.6, -3.6 + i * 2.0), (ut - 0.3, yt - 0.2)], 1)))
inset_arrow = line([Q(8.9, 10.6, 1), Q(6.4, 6.8, 1)])
f.add(f'<defs><clipPath id="cp_mo2"><rect x="{CX2 - S2 * U2:.2f}" y="{Y02 + S2 * YT2:.2f}" width="{2 * S2 * U2:.2f}" '
      f'height="{S2 * (YB2 - YT2):.2f}" rx="1.2"/></clipPath></defs><g clip-path="url(#cp_mo2)">{"".join(inset)}</g>')
f.arrow(inset_arrow)
f.add(f'<rect class="dim" x="{CX2 - S2 * U2:.2f}" y="{Y02 + S2 * YT2:.2f}" width="{2 * S2 * U2:.2f}" '
      f'height="{S2 * (YB2 - YT2):.2f}" rx="1.2"/>')
f.text(CX2, Y02 + S2 * YB2 + 2.8, 'od tyłu', cls='notec')

# ================================================================ nagłówki
f.text(24.0, 5.6, 'mięśnie wdechowe', cls='big', anchor='middle')
f.text(24.0, 9.2, 'prawa strona ciała · strzałki niebieskie', cls='notec')
f.text(126.0, 5.6, 'mięśnie wydechowe', cls='big', anchor='middle')
f.text(126.0, 9.2, 'lewa strona ciała · strzałki czerwone', cls='notec')

# ================================================================ podpisy – wdechowe (lewa kolumna)
XL = 45.5


def note(x, y, t, anchor):
    f.text(x, y, t, cls='note', anchor=anchor)


def lab(at, pl, la, to, side, nt=None):
    f.label(at, pl, la, to, side=side)
    if nt:
        x = to[0] + (0.7 if side == 'R' else -0.7)
        note(x, to[1] + (6.3 if la else 3.6), nt, 'start' if side == 'R' else 'end')


lab(P(5.0, -7.0, L), 'm. mostkowo-obojczykowo-sutkowy', 'm. sternocleidomastoideus', (63.0, 14.5), 'L',
    'głowa i kręgosłup ustalone')
lab(P(6.6, -0.9, L), 'mm. pochyłe', 'mm. scaleni', (XL, 25.5), 'L', 'przedłużenie mm. międzyżebrowych')
note(XL - 0.7, 34.5, 'zewnętrznych', 'end')
lab(P(9.0, 4.1, L), 'm. podobojczykowy', 'm. subclavius', (XL, 39.0), 'L')
lab(P(10.4, 9.2, L), 'm. piersiowy mniejszy', 'm. pectoralis minor', (XL, 46.0), 'L')
lab(P(13.6, 11.2, L), 'm. piersiowy większy', 'm. pectoralis major', (XL, 53.0), 'L')
lab(P(14.6, 17.2, L), 'm. zębaty przedni', 'm. serratus anterior', (XL, 60.0), 'L')
lab(P(12.0, 23.1, L), 'mm. międzyżebrowe zewnętrzne', 'mm. intercostales externi', (XL, 77.0), 'L', 'podnoszą żebra (spokojne oddychanie żebrowe)')
lab(P(9.6, 18.1, L), 'przepona', 'diaphragma', (XL, 68.0), 'L', 'ważny mięsień wdechowy')
# wydechowe (prawa kolumna)
XR = 104.5
lab(P(11.0, 11.6, R), 'mm. międzyżebrowe wewnętrzne', 'mm. intercostales interni', (XR, 31.0), 'R', 'spokojny wydech')
lab(P(3.6, 16.2, R), 'm. poprzeczny klatki piersiowej', 'm. transversus thoracis', (XR, 40.5), 'R',
    'spokojny wydech · za mostkiem')
lab(P(16.7, 17.0, R), 'm. najszerszy grzbietu', 'm. latissimus dorsi', (XR, 50.0), 'R', '„mięsień kaszlu” – części boczne')
note(XR + 0.7, 59.0, '(wiązki żebrowe – pomocnicze wdechowe)', 'start')
lab(P(11.0, 31.0, R), 'mięśnie brzucha', None, (XR, 64.0), 'R', 'najsilniej opuszczają żebra')
lab(Q(4.6, 3.6, 1), 'm. zębaty tylny górny', 'm. serratus posterior superior', (XR, 87.0), 'R', 'pomocniczy wdechowy')

# ================================================================ uwagi (warunki działania mięśni pomocniczych)
for i, t in enumerate(['mięśnie od obręczy kończyny górnej', 'i ramienia działają wdechowo, gdy ramię',
                       'jest ustalone (np. chwyt brzegu stołu)']):
    note(XL - 0.7, 92.0 + i * 2.7, t, 'end')
for i, t in enumerate(['pomocnicze wydechowe – gdy wydech', 'idzie przeciw oporowi lub szybko', '(kaszel, kichanie, śmiech)']):
    note(XR + 0.7, 71.0 + i * 2.7, t, 'start')

f.save()
print('ok')
