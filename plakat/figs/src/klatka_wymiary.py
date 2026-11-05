# KLATKA PIERSIOWA – WYMIARY (Bochenek t. I, s. 293; wymiary przeciętne podane przez Bochenka wg Rauber-Kopscha).
# Panel A – od przodu (prawa strona ciała po lewej): wymiar poprzeczny otworu górnego (9–11 cm), na wysokości nasady
#           wyrostka mieczykowatego (20–23 cm) i na wysokości XII żebra (18–20 cm).
# Panel B – z boku (od strony lewej, przód w lewo): wymiar przednio-tylny otworu górnego (5–6 cm) i długość klatki:
#           z przodu 16–19 cm, z boku 32 cm, z tyłu 27–30 cm.
# Panel C – przekrój poprzeczny na wysokości nasady wyrostka mieczykowatego (kształt nerkowaty, s. 290): wymiar poprzeczny
#           20–23 cm, przednio-tylny 15–19 cm; wskaźnik klatki piersiowej = wymiar poprzeczny w odsetkach wymiaru
#           przednio-tylnego (dorosły 139) i jego zmiany z wiekiem (zarodek 4-tyg. ok. 60, płód 2-mies. ok. 90, noworodek
#           ok. 105, dorosły 139, ponad 70 lat ok. 129).
# Bochenek nie podaje punktów pomiarowych długości ani wymiarów – położenie linii wymiarowych jest schematyczne.
# Geometria panelu A przejęta z rysunku „klatka_przod” (model w cm, skala K mm/cm); panel B ma te same poziomy (Y w cm).
import sys, os; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
import math
from figlib import Fig, smooth

W, H = 160, 120
K = 1.75                    # mm rysunku / cm (wszystkie panele w tej samej skali)
CX, Y0 = 45.0, 13.0         # panel A: oś symetrii; poziom Y=0 (górny brzeg trzonu Th1) – wspólny dla paneli A i B
f = Fig('klatka_wymiary', W, H,
        caption='klatka piersiowa · wymiary przeciętne wg Bochenka (s. 293) · linie wymiarowe schematyczne')

RIGHT, LEFT = -1, +1        # strona ciała → kierunek na rysunku (prawa strona ciała po lewej)


SX = 0.92                   # model z „klatka_przod” nieco zwężony, żeby szerokości trafiały w przedziały Bochenka


def M(X, Y, s):
    return (CX + s * X * K * SX, Y0 + Y * K)


def poly(pts, close=True):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + (' Z' if close else '')


def bez(pts, t=0.5, n=14):
    m = len(pts)
    Q = [pts[0]] + pts + [pts[-1]]
    out = [pts[0]]
    for i in range(1, m):
        p0, p1, p2, p3 = Q[i - 1], Q[i], Q[i + 1], Q[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) * t / 3, p1[1] + (p2[1] - p0[1]) * t / 3)
        c2 = (p2[0] - (p3[0] - p1[0]) * t / 3, p2[1] - (p3[1] - p1[1]) * t / 3)
        for k in range(1, n + 1):
            u = k / n
            a, b, c, d = (1 - u) ** 3, 3 * (1 - u) ** 2 * u, 3 * (1 - u) * u ** 2, u ** 3
            out.append((a * p1[0] + b * c1[0] + c * c2[0] + d * p2[0], a * p1[1] + b * c1[1] + c * c2[1] + d * p2[1]))
    return out


def resample(pts, n):
    L = [0.0]
    for i in range(1, len(pts)):
        L.append(L[-1] + math.dist(pts[i - 1], pts[i]))
    out, j = [], 0
    for k in range(n + 1):
        s = L[-1] * k / n
        while j < len(L) - 2 and L[j + 1] < s:
            j += 1
        u = (s - L[j]) / max(L[j + 1] - L[j], 1e-9)
        out.append((pts[j][0] + (pts[j + 1][0] - pts[j][0]) * u, pts[j][1] + (pts[j + 1][1] - pts[j][1]) * u))
    return out, L[-1]


def lerp(ctrl, u):
    if u <= ctrl[0][0]:
        return ctrl[0][1]
    for (u0, v0), (u1, v1) in zip(ctrl, ctrl[1:]):
        if u <= u1:
            a = (u - u0) / (u1 - u0)
            a = a * a * (3 - 2 * a)
            return v0 + (v1 - v0) * a
    return ctrl[-1][1]


class Line:
    """linia środkowa w cm (X – od osi w bok, Y – w dół) z normalnymi"""

    def __init__(self, ctrl, n=240):
        self.P, self.L = resample(bez(ctrl, n=20), n)
        self.n = n
        T = []
        for i in range(n + 1):
            a, b = self.P[max(i - 1, 0)], self.P[min(i + 1, n)]
            d = math.dist(a, b)
            T.append(((b[0] - a[0]) / d, (b[1] - a[1]) / d))
        self.T = T
        self.Nr = [(-ty, tx) for tx, ty in T]

    def i(self, u):
        return min(max(int(round(u * self.n)), 0), self.n)

    def pt(self, u, v=0.0):
        i = self.i(u)
        return (self.P[i][0] + self.Nr[i][0] * v, self.P[i][1] + self.Nr[i][1] * v)

    def band(self, w, u0=0.0, u1=1.0, cap0='flat', cap1='flat'):
        """obrys pasma o połowie szerokości w(u) między u0 i u1 (cm)"""
        i0, i1 = self.i(u0), self.i(u1)
        A, B = [], []
        for i in range(i0, i1 + 1):
            u = i / self.n
            p, nr, ww = self.P[i], self.Nr[i], w(u)
            A.append((p[0] + nr[0] * ww, p[1] + nr[1] * ww))
            B.append((p[0] - nr[0] * ww, p[1] - nr[1] * ww))

        def cap(i, sign, kind):
            if kind != 'round':
                return []
            p, t, nr, ww = self.P[i], self.T[i], self.Nr[i], w(i / self.n)
            out = []
            for k in range(1, 12):
                a = math.pi * k / 12
                # od strony A przez czubek do strony B
                v = (nr[0] * math.cos(a) + sign * t[0] * math.sin(a), nr[1] * math.cos(a) + sign * t[1] * math.sin(a))
                out.append((p[0] + v[0] * ww, p[1] + v[1] * ww))
            return out

        return A + cap(i1, +1, cap1) + B[::-1] + cap(i0, -1, cap0)[::-1]


SHAPES = []                 # wielokąty (rysunek, mm) – do szukania pustych miejsc pod podpisy


def draw(pts_cm, cls, sides=(RIGHT, LEFT)):
    for s in sides:
        pp = [M(x, y, s) for x, y in pts_cm]
        if cls != 'shade':
            SHAPES.append(pp)
        f.add(f'<path class="{cls}" d="{poly(pp)}"/>')


def inside(pt, pg):
    x, y = pt
    c = False
    for (x1, y1), (x2, y2) in zip(pg, pg[1:] + pg[:1]):
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            c = not c
    return c


def free_pt(pt):
    return not any(inside(pt, pg) for pg in SHAPES)


# ======================= kręgosłup – część piersiowa (Th1–Th12) =======================
VT = []                       # (górny brzeg, dolny brzeg, połowa szerokości) trzonów
y = 0.0
for n in range(1, 13):
    h = 1.55 + 0.07 * (n - 1)
    b = 1.35 + 0.075 * (n - 1)
    VT.append((y, y + h, b))
    y += h + 0.42 + 0.02 * (n - 1)


def top(n):
    return VT[n - 1][0]


# ======================= mostek (kształt jak w rysunku „mostek_przod”, skala 0,205 cm / jedn.) =======================
KS, YJ = 0.205, 4.35          # cm na jednostkę; poziom wcięcia szyjnego (między Th2 a Th3)


def cr1d(ctrl, yy):
    ys = [c[0] for c in ctrl]
    if yy <= ys[0]:
        return ctrl[0][1]
    if yy >= ys[-1]:
        return ctrl[-1][1]
    i = max(k for k in range(len(ys) - 1) if ys[k] <= yy)
    p0 = ctrl[max(i - 1, 0)][1]; p1 = ctrl[i][1]; p2 = ctrl[i + 1][1]; p3 = ctrl[min(i + 2, len(ctrl) - 1)][1]
    u = (yy - ys[i]) / (ys[i + 1] - ys[i])
    return 0.5 * ((2 * p1) + (-p0 + p2) * u + (2 * p0 - 5 * p1 + 4 * p2 - p3) * u * u + (-p0 + 3 * p1 - 3 * p2 + p3) * u ** 3)


Y_J1, Y_J2, Y_X1, Y_X2 = 32.3, 34.1, 83.2, 84.8
NOTCH = {'II': (33.2, 3.0, 1.15), 'III': (44.6, 2.6, 1.15), 'IV': (55.6, 2.6, 1.15), 'V': (65.6, 2.6, 1.15),
         'VI': (74.2, 2.4, 1.1), 'VII': (84.0, 2.8, 1.1)}
W_MAN = [(28.6, 10.15), (30.0, 9.15), (Y_J1, 8.15)]
W_BODY = [(Y_J2, 7.75), (40, 8.45), (50, 9.25), (60, 9.95), (68, 10.25), (75, 9.85), (80, 8.75), (Y_X1, 7.5)]
W_XI = [(Y_X2, 6.5), (86.5, 6.0), (89, 5.55), (92.5, 4.75), (95.5, 3.55), (97.4, 2.3), (98.5, 1.3)]


def dip(yy):
    d = 0.0
    for yc, h, dep in NOTCH.values():
        u = (yy - yc) / h
        if abs(u) < 1:
            d = max(d, dep * (1 - u * u) ** 0.62)
    return d


def wst(yy):
    if yy <= Y_J1:
        return cr1d(W_MAN, yy)
    if yy < Y_J2:
        a, b = cr1d(W_MAN, Y_J1), cr1d(W_BODY, Y_J2)
        return a + (b - a) * (yy - Y_J1) / (Y_J2 - Y_J1)
    if yy <= Y_X1:
        return cr1d(W_BODY, yy)
    if yy < Y_X2:
        a, b = cr1d(W_BODY, Y_X1), cr1d(W_XI, Y_X2)
        return a + (b - a) * (yy - Y_X1) / (Y_X2 - Y_X1)
    return cr1d(W_XI, yy)


def S2C(x, yy):
    """jednostki mostka → cm (X od osi, Y w dół)"""
    return (abs(x) * KS, YJ + (yy - 9.35) * KS)


def st_half(yy, wf, step=0.5):
    pts = []
    n = int(round((yy[1] - yy[0]) / step))
    for k in range(n + 1):
        q = yy[0] + (yy[1] - yy[0]) * k / n
        pts.append((wf(q) - dip(q), q))
    return pts


JUG = [(0, 9.35), (2.4, 9.05), (4.2, 8.4), (5.4, 7.95)]
CLAV = [(6.5, 7.8), (7.9, 8.45), (9.5, 9.5), (11.2, 10.5), (12.7, 11.2)]
LAT = [(13.75, 11.85), (14.35, 13.0), (14.55, 15.0), (14.35, 17.6), (14.5, 20.2), (14.1, 21.9), (12.6, 24.9), (10.6, 28.0)]
man_h = bez(JUG + CLAV + LAT, n=8) + st_half((28.6, Y_J1), lambda q: cr1d(W_MAN, q))
body_h = st_half((Y_J2, Y_X1), lambda q: cr1d(W_BODY, q))
xi_h = st_half((Y_X2, 89.0), lambda q: cr1d(W_XI, q)) + bez([(5.55, 89.0), (4.75, 92.5), (3.6, 95.4), (2.1, 97.6),
                                                            (0.85, 98.85), (0, 99.2)], n=8)[1:]


def full(half):
    """połowa (x ≥ 0) → zamknięty obrys w cm na rysunku (obie strony)"""
    R = [M(*S2C(x, yy), RIGHT) for x, yy in half]
    Lh = [M(*S2C(x, yy), LEFT) for x, yy in half]
    return R + Lh[::-1]


def st_edge(yy_units):
    """punkt brzegu bocznego mostka (cm) na wysokości yy (jedn.)"""
    return S2C(wst(yy_units) - dip(yy_units), yy_units)


ST = {1: S2C(14.5, 17.6), 2: S2C(wst(33.2), 33.2), 3: st_edge(44.6), 4: st_edge(55.6), 5: st_edge(65.6),
      6: st_edge(74.2), 7: S2C(wst(84.0), 84.0)}

# ======================= żebra =======================
# n: (b – połowa szer. trzonu przy głowie, Yh – głowa, a – najbardziej boczny punkt X, Yl – jego wysokość,
#     cc – połączenie kości z chrząstką (X, Y))
RIB = {
    1: (1.35, 0.75, 5.95, 2.55, (4.45, 5.3)),
    2: (1.45, top(2) + 0.05, 8.0, 5.55, (5.0, 8.95)),
    3: (1.5, top(3) + 0.05, 9.3, 8.45, (5.8, 12.25)),
    4: (1.6, top(4) + 0.05, 10.2, 11.1, (6.5, 14.95)),
    5: (1.65, top(5) + 0.05, 10.8, 13.7, (7.2, 17.55)),
    6: (1.75, top(6) + 0.05, 11.0, 16.3, (7.8, 20.05)),
    7: (1.8, top(7) + 0.05, 11.2, 18.9, (8.45, 22.55)),
    8: (1.9, top(8) + 0.05, 11.25, 21.5, (9.15, 25.05)),
    9: (1.95, top(9) + 0.05, 11.15, 24.1, (9.75, 27.5)),
    10: (2.0, top(10) + 0.4, 10.85, 26.8, (10.15, 29.5)),
}


def rib_ctrl(n):
    b, yh, a, yl, (xc, yc) = RIB[n]
    if n == 1:
        back = [(b - 0.12, yh), (2.3, 0.35), (3.4, 0.12), (4.6, 0.45), (5.5, 1.25), (a, yl)]
    else:
        d = yl - yh
        back = [(b - 0.12, yh), (b + 1.0, yh - 0.05), (b + 2.2, yh + 0.12),
                (b + 2.2 + 0.40 * (a - b - 2.2), yh + 0.20 * d), (b + 2.2 + 0.74 * (a - b - 2.2), yh + 0.48 * d),
                (a - 0.10 * (a - b), yh + 0.80 * d), (a, yl)]
    front = [(a - 0.10 * (a - xc), yl + 0.40 * (yc - yl)), (a - 0.45 * (a - xc), yl + 0.80 * (yc - yl)), (xc, yc)]
    return back + front


RIBW_BACK = {1: 0.5, 2: 0.46, 3: 0.46, 4: 0.46, 5: 0.46, 6: 0.46, 7: 0.46, 8: 0.45, 9: 0.43, 10: 0.42}
RIBW_FRONT = {1: (0.68, 0.95), 2: (0.62, 0.66), 3: (0.62, 0.62), 4: (0.62, 0.62), 5: (0.62, 0.6), 6: (0.6, 0.58),
              7: (0.6, 0.57), 8: (0.57, 0.54), 9: (0.55, 0.5), 10: (0.52, 0.48)}

ribs = {}
for n in RIB:
    ln = Line(rib_ctrl(n))
    i_lat = max(range(ln.n + 1), key=lambda i: ln.P[i][0])
    us = i_lat / ln.n
    wb, (wl, we) = RIBW_BACK[n], RIBW_FRONT[n]

    def wf(u, us=us, wb=wb, wl=wl, we=we):
        if u <= us:
            return lerp([(0, wb + 0.05), (0.06, wb), (us, wl)], u)
        return lerp([(us, wl), (1.0, we)], u)

    ribs[n] = (ln, us, wf)

# żebra XI i XII – tylko część tylna (wolne końce z krótką chrząstką)
FREE = {
    11: [(2.0, top(11) + 0.4), (3.2, top(11) + 0.4), (4.6, top(11) + 0.75), (6.6, top(11) + 1.9), (8.3, top(11) + 3.4),
         (9.4, top(11) + 5.1), (9.9, top(11) + 6.6)],
    12: [(2.1, top(12) + 0.4), (3.3, top(12) + 0.5), (4.6, top(12) + 1.0), (5.9, top(12) + 2.0), (6.9, top(12) + 3.2),
         (7.55, top(12) + 4.35)],
}
free = {n: Line(p) for n, p in FREE.items()}

# ======================= chrząstki żebrowe =======================
CART = {
    1: [RIB[1][4], (3.75, 5.62), ST[1]],
    2: [RIB[2][4], (3.3, 9.12), ST[2]],
    3: [RIB[3][4], (3.8, 11.95), ST[3]],
    4: [RIB[4][4], (4.2, 14.35), ST[4]],
    5: [RIB[5][4], (4.6, 16.75), ST[5]],
    6: [RIB[6][4], (6.6, 20.75), (5.2, 20.25), ST[6]],
    7: [RIB[7][4], (6.9, 23.55), (5.9, 23.9), (4.0, 22.2), ST[7]],
    8: [RIB[8][4], (8.1, 25.75), (7.4, 25.8), (6.0, 24.65), (5.0, 23.6)],
    9: [RIB[9][4], (9.15, 28.0), (8.6, 27.95), (7.6, 26.6), (7.05, 25.75)],
    10: [RIB[10][4], (9.7, 29.75), (9.1, 29.4), (8.5, 28.3)],
}
CART_W = {1: (0.85, 0.8), 2: (0.56, 0.5), 3: (0.52, 0.46), 4: (0.5, 0.45), 5: (0.5, 0.45), 6: (0.48, 0.44),
          7: (0.48, 0.44), 8: (0.42, 0.22), 9: (0.4, 0.2), 10: (0.38, 0.2)}
carts = {}
for n, pts in CART.items():
    # przedłużenie pod mostek / pod chrząstkę wyższą
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    d = math.dist((x1, y1), (x2, y2))
    ext = 0.45 if n <= 7 else 0.3
    pts = pts[:-1] + [(x2 + (x2 - x1) / d * ext, y2 + (y2 - y1) / d * ext)]
    # początek nieco pod końcem kości
    (x0, y0_), (xa, ya) = pts[0], pts[1]
    d0 = math.dist((x0, y0_), (xa, ya))
    pts = [(x0 - (xa - x0) / d0 * 0.15, y0_ - (ya - y0_) / d0 * 0.15)] + pts[1:]
    carts[n] = Line(pts)

# ======================= RYSOWANIE =======================
# 1) kręgosłup (trzony + krążki) – w głębi; żebra zaczynają się przy brzegach trzonów (głowy ukryte za trzonami)
for n, (y0_, y1_, b) in enumerate(VT, start=1):
    if n < 12:
        nb = VT[n][2]
        yd0, yd1 = y1_, VT[n][0]
        disc = [(-(b - 0.12), yd0 - 0.05), (b - 0.12, yd0 - 0.05), (nb - 0.1, yd1 + 0.05), (-(nb - 0.1), yd1 + 0.05)]
        f.add(f'<path class="annulus" d="{poly([M(x, yy, LEFT) for x, yy in disc])}"/>')
    r = 0.25
    body = ([(-b + r, y0_), (b - r, y0_)] + [(b, y0_ + r)] + [(b - 0.13, (y0_ + y1_) / 2)] + [(b, y1_ - r)] +
            [(b - r, y1_), (-b + r, y1_), (-b, y1_ - r), (-b + 0.13, (y0_ + y1_) / 2), (-b, y0_ + r)])
    f.add(f'<path class="bone" d="{poly([M(x, yy, LEFT) for x, yy in bez(body + body[:1], n=6)])}"/>')
    f.add(f'<path class="bonel" d="M{M(-b + 0.15, y0_ + 0.22, LEFT)[0]:.2f},{M(0, y0_ + 0.22, LEFT)[1]:.2f} '
          f'L{M(b - 0.15, y0_ + 0.22, LEFT)[0]:.2f},{M(0, y0_ + 0.22, LEFT)[1]:.2f}"/>')


def deep(ln, wf, u_end):
    """przyciemnienie części tylnej (dwa stopnie: im dalej od boku, tym ciemniej)"""
    draw(ln.band(wf, 0.0, u_end), 'shade')
    draw(ln.band(wf, 0.0, max(u_end - 0.10, 0.02)), 'shade')


# 2) żebra od XII do I: każde żebro w całości (część tylna → bok → część przednia), chrząstka pod końcem kości.
#    Kolejność daje właściwe przesłanianie: część przednia żebra wyższego leży przed częścią tylną żeber niższych.
for n in (12, 11):
    ln = free[n]
    w0 = 0.42 if n == 11 else 0.4
    wfree = (lambda u, w0=w0: lerp([(0, w0 + 0.04), (0.08, w0), (0.7, w0 - 0.04), (1.0, w0 - 0.16)], u))
    i = ln.n
    p, t, nr = ln.P[i], ln.T[i], ln.Nr[i]
    wl = wfree(1.0)
    Lc = 0.85 if n == 11 else 0.7
    tip = [(p[0] + nr[0] * wl - t[0] * 0.1, p[1] + nr[1] * wl - t[1] * 0.1),
           (p[0] + t[0] * Lc * 0.55 + nr[0] * wl * 0.6, p[1] + t[1] * Lc * 0.55 + nr[1] * wl * 0.6),
           (p[0] + t[0] * Lc, p[1] + t[1] * Lc),
           (p[0] + t[0] * Lc * 0.55 - nr[0] * wl * 0.6, p[1] + t[1] * Lc * 0.55 - nr[1] * wl * 0.6),
           (p[0] - nr[0] * wl - t[0] * 0.1, p[1] - nr[1] * wl - t[1] * 0.1)]
    draw(tip, 'cart')
    draw(ln.band(wfree, 0.0, 1.0), 'bone')
    deep(ln, wfree, 0.80)

for n in sorted(ribs, reverse=True):
    ln, us, wf = ribs[n]
    w0, w1 = CART_W[n]
    draw(carts[n].band(lambda u, w0=w0, w1=w1: lerp([(0, w0), (0.7, (w0 + w1) / 2), (1.0, w1)], u)), 'cart')
    draw(ln.band(wf, 0.0, 1.0), 'bone')
    deep(ln, wf, us - 0.02)

# 3) mostek
for yy0, yy1 in ((Y_J1 - 0.5, Y_J2 + 0.5), (Y_X1 - 0.5, Y_X2 + 0.5)):
    band = st_half((yy0, yy1), wst, step=0.25)
    f.add(f'<path class="cart" d="{poly(full(band))}"/>')
for part in (man_h, body_h, xi_h):
    f.add(f'<path class="bone" d="{poly(full(part))}"/>')
for yy in (44.6, 55.6, 65.6):
    x = wst(yy) - dip(yy) - 0.3
    a_, b_ = M(*S2C(x, yy), RIGHT), M(*S2C(x, yy), LEFT)
    f.add(f'<path class="bonel" d="M{a_[0]:.2f},{a_[1]:.2f} Q{CX:.2f},{a_[1] + 0.5:.2f} {b_[0]:.2f},{b_[1]:.2f}"/>')


# =====================================================================================================================
#                                        WYMIARY – pomocnicze
# =====================================================================================================================
def tick_h(x, y, L=1.6):       # kreska końcowa linii wymiarowej poziomej
    f.add(f'<path class="lead" d="M{x:.2f},{y - L:.2f} L{x:.2f},{y + L:.2f}"/>')


def tick_v(x, y, L=1.6):       # kreska końcowa linii wymiarowej pionowej
    f.add(f'<path class="lead" d="M{x - L:.2f},{y:.2f} L{x + L:.2f},{y:.2f}"/>')


def dline(a, b):
    f.add(f'<path class="dim" d="M{a[0]:.2f},{a[1]:.2f} L{b[0]:.2f},{b[1]:.2f}"/>')


def hdim(x1, x2, y):
    dline((x1, y), (x2, y)); tick_h(x1, y); tick_h(x2, y)


def vdim(x, y1, y2):
    dline((x, y1), (x, y2)); tick_v(x, y1); tick_v(x, y2)


def val(x, y, t, anchor='start'):            # wartość liczbowa (pogrubiona)
    f.text(x, y, t, cls='pl', anchor=anchor)


def xs_at(y):
    """przecięcia linii poziomej y z obrysami kształtów panelu A"""
    out = []
    for pg in SHAPES:
        for (x1, y1), (x2, y2) in zip(pg, pg[1:] + pg[:1]):
            if (y1 - y) * (y2 - y) < 0:
                out.append(x1 + (x2 - x1) * (y - y1) / (y2 - y1))
    return sorted(out)


# =====================================================================================================================
#                                        PANEL A – od przodu: wymiar poprzeczny
# =====================================================================================================================
f.text(CX, 3.6, 'od przodu – wymiar poprzeczny', cls='notec')
# 1) otwór górny (między żebrami I)
yA1 = Y0 + 2.0 * K
xx = xs_at(yA1)
xr = min(x for x in xx if x > CX + 2.6 * K)
xl = 2 * CX - xr
hdim(xl, xr, yA1)
val(CX, 7.4, '9–11 cm', anchor='middle')
f.text(CX, 10.2, 'otwór górny', cls='notec')
# 2) na wysokości nasady wyrostka mieczykowatego
yA2 = Y0 + 19.65 * K
xx = xs_at(yA2)
hdim(xx[0], xx[-1], yA2)
dline((24.0, yA2), (xx[0] - 0.4, yA2))
val(23.0, yA2 + 0.9, '20–23 cm', anchor='end')
f.text(23.0, yA2 + 3.7, 'nasada wyrostka', cls='note', anchor='end')
f.text(23.0, yA2 + 6.2, 'mieczykowatego', cls='note', anchor='end')
W2 = (xx[-1] - xx[0]) / K
# 3) na wysokości XII żebra
yA3 = Y0 + 29.5 * K
xx = xs_at(yA3)
hdim(xx[0], xx[-1], yA3)
dline((24.0, yA3), (xx[0] - 0.4, yA3))
val(23.0, yA3 + 0.9, '18–20 cm', anchor='end')
f.text(23.0, yA3 + 3.7, 'XII żebro', cls='note', anchor='end')
W3 = (xx[-1] - xx[0]) / K
W1 = (xr - xl) / K

# =====================================================================================================================
#                                        PANEL B – z boku (od strony lewej, przód w lewo)
# =====================================================================================================================
def cr(pts, closed=False, n=12, t=0.5):
    m = len(pts)
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
        return [(center[0] + w * math.cos(a0 - math.pi * j / k), center[1] + w * math.sin(a0 - math.pi * j / k)) for j in range(1, k)]
    out = list(left)
    if cap1:
        out += capf(left[-1], right[-1], c[-1], w1 / 2)
    out += right[::-1]
    if cap0:
        out += capf(right[0], left[0], c[0], w0 / 2)
    return out


XO = 119.0                  # przednia powierzchnia trzonu Th1 (z = 0)


def FB(z, y):
    """z – w przód od przedniej powierzchni trzonu Th1 (cm, ku przodowi = w lewo), y – w dół od górnego brzegu Th1 (cm)"""
    return (XO - K * z, Y0 + K * y)


def za(y):                  # przednia powierzchnia trzonów (kifoza piersiowa)
    return -2.2 * math.sin(math.pi * min(y, 30) / 30)


def depth(y):
    return 2.0 + 1.3 * min(max(y, 0), 36) / 30


f.text(113.0, 3.6, 'z boku – długość i wymiar przednio-tylny', cls='notec')

# żebra z boku (głowa przy trzonie → do tyłu → w dół i do przodu do granicy z chrząstką)
YH = [0.75] + [VT[n - 1][0] + 0.05 for n in range(2, 13)]
CCY = [5.3, 8.95, 12.25, 14.95, 17.55, 20.05, 22.55, 25.05, 27.5, 29.5, 30.75, VT[11][0] + 4.35]
ZE = [4.4, 5.8, 6.6, 7.1, 7.5, 7.7, 7.6, 7.0, 6.2, 5.2, 1.0, -3.4]
ZANG = [-3.2, -4.3] + [-5.0] * 8 + [-4.8, -4.4]


def rib_side(k):
    yh = YH[k]
    zh = za(yh) - 1.5
    zg = za(yh) + ZANG[k]
    d, ze = CCY[k] - yh, ZE[k]
    D = zh - zg
    return [(zh, yh), (zh - 0.5 * D, yh + 0.1), (zg + 0.18 * D, yh + 0.5), (zg, yh + 1.5), (zg + (ze - zg) * 0.20, yh + 0.45 * d),
            (zg + (ze - zg) * 0.56, yh + 0.83 * d), (ze, yh + d)]


STERN_F = [(6.0, 4.4), (6.25, 4.7), (7.1, 7.0), (7.6, 8.9), (8.4, 12.0), (9.4, 16.0), (10.1, 19.6), (10.25, 20.3), (9.8, 23.4)]
STERN_B = [(9.6, 23.5), (9.3, 20.5), (8.95, 19.6), (8.25, 16.4), (7.2, 12.4), (6.0, 8.9), (4.8, 5.4), (4.85, 4.6)]
SY = [6.0, 9.2, 11.6, 13.8, 15.9, 17.6, 19.6]


def stern_back(y):
    pts = STERN_B[::-1]
    for (z1, y1), (z2, y2) in zip(pts, pts[1:]):
        if y1 <= y <= y2:
            return z1 + (z2 - z1) * (y - y1) / (y2 - y1)
    return pts[-1][0]


def cart_side(k, rib):
    e = rib[-1]
    if k < 7:
        s = (stern_back(SY[k]) + 0.55, SY[k])
        mid = (e[0] + (s[0] - e[0]) * 0.55, e[1] + (s[1] - e[1]) * 0.35 + (0.25 if k >= 4 else 0))
        return [e, mid, s]
    if k < 10:
        tgt = {7: (8.75, 22.3), 8: (7.85, 24.9), 9: (6.9, 27.2)}[k]
        mid = (e[0] + (tgt[0] - e[0]) * 0.6, e[1] + (tgt[1] - e[1]) * 0.25)
        return [e, mid, tgt]
    return None


for k in range(11, -1, -1):
    rb = rib_side(k)
    pts = [FB(*p) for p in rb]
    w0, w1 = (0.75 if k > 0 else 0.9) * K, (1.2 if k < 10 else 0.85) * K
    c = cart_side(k, rb)
    if c:
        f.add(f'<path class="cart" d="{poly(band([FB(*p) for p in c], 0.95 * K, 0.85 * K, cap1=(k >= 7)))}"/>')
    f.add(f'<path class="bone" d="{poly(band(pts, w0, w1, cap0=True, cap1=(k >= 10)))}"/>')
    if k >= 10:                                    # wolne końce XI i XII – krótka chrząstka
        e, p = rb[-1], rb[-2]
        dz, dy = e[0] - p[0], e[1] - p[1]
        L = math.hypot(dz, dy)
        tip = (e[0] + dz / L * 0.8, e[1] + dy / L * 0.8)
        f.add(f'<path class="cart" d="{poly(band([FB(*e), FB(*tip)], 0.7 * K, 0.35 * K, cap1=True))}"/>')
st = STERN_F + STERN_B
f.add(f'<path class="bone" d="{smooth([FB(*p) for p in st], closed=True, t=0.35)}"/>')
for y in (8.95, 19.7):
    a, b = FB(stern_back(y) + 0.05, y), FB(STERN_F[3][0] if y < 10 else 10.1, y)
    f.add(f'<path class="bonel" d="M{a[0]:.2f},{a[1]:.2f} L{b[0]:.2f},{b[1]:.2f}"/>')

# kręgosłup Th1–Th12 (te same poziomy co w panelu A) – na wierzchu, żeby był widoczny
for i in range(11):
    yt, yb = VT[i][1], VT[i + 1][0]
    pts = [(za(yt) - 0.1, yt), (za(yt) - depth(yt) + 0.1, yt), (za(yb) - depth(yb) + 0.1, yb), (za(yb) - 0.1, yb)]
    f.add(f'<path class="annulus" d="{poly([FB(*p) for p in pts])}"/>')
for yt, yb, _ in VT:
    r = 0.3
    fa, fb = za(yt), za(yb)
    pts = [(fa, yt + r), (fa - r * 0.6, yt), (fa - depth(yt) + r * 0.6, yt), (fa - depth(yt), yt + r),
           (fb - depth(yb), yb - r), (fb - depth(yb) + r * 0.6, yb), (fb - r * 0.6, yb), (fb, yb - r)]
    f.add(f'<path class="bone" d="{smooth([FB(*p) for p in pts], closed=True, t=0.3)}"/>')

# 1) wymiar przednio-tylny otworu górnego: przednia powierzchnia trzonu Th1 → wcięcie szyjne mostka
pa, pb = FB(0.05, 0.9), FB(stern_back(4.6) - 0.05, 4.6)
dline(pa, pb)
for p, q in ((pa, pb), (pb, pa)):
    dx, dy = q[0] - p[0], q[1] - p[1]; L = math.hypot(dx, dy); nx, ny = -dy / L * 1.4, dx / L * 1.4
    f.add(f'<path class="lead" d="M{p[0] - nx:.2f},{p[1] - ny:.2f} L{p[0] + nx:.2f},{p[1] + ny:.2f}"/>')
AP1 = math.dist(pa, pb) / K
mtop = ((pa[0] + pb[0]) / 2, (pa[1] + pb[1]) / 2)
val(mtop[0], 7.4, '5–6 cm', anchor='middle')
f.text(mtop[0], 10.2, 'otwór górny', cls='notec')

# 2) długość z tyłu: górny brzeg Th1 → dolny brzeg Th12
yb12 = VT[11][1]
xback = FB(-7.9, 0)[0] + 2.4
dline(FB(za(0) - depth(0) + 0.1, 0), (xback + 1.2, Y0))
dline(FB(za(yb12) - depth(yb12) + 0.1, yb12), (xback + 1.2, Y0 + K * yb12))
vdim(xback, Y0, Y0 + K * yb12)
ym = Y0 + K * yb12 * 0.45
val(xback + 1.4, ym, '27–30 cm')
f.text(xback + 1.4, ym + 2.8, 'długość z tyłu', cls='note')
f.text(xback + 1.4, ym + 5.3, '(Th1–Th12)', cls='note')

# 3) długość z przodu: wcięcie szyjne → koniec wyrostka mieczykowatego
xfr = FB(10.25, 0)[0] - 3.2
p_top, p_bot = FB(6.0, 4.4), FB(9.7, 23.5)
dline(p_top, (xfr - 1.2, p_top[1])); dline(p_bot, (xfr - 1.2, p_bot[1]))
vdim(xfr, p_top[1], p_bot[1])
ym = (p_top[1] + p_bot[1]) / 2
val(xfr - 1.4, ym, '16–19 cm', anchor='end')
f.text(xfr - 1.4, ym + 2.8, 'długość', cls='note', anchor='end')
f.text(xfr - 1.4, ym + 5.3, 'z przodu', cls='note', anchor='end')
LF = (p_bot[1] - p_top[1]) / K

# 4) długość z boku: od góry klatki do najniższego punktu ściany bocznej (wolny koniec XI żebra)
xs_ = 77.0
rb11 = rib_side(10)
y_low = rb11[-1][1] + 0.75
p_low = FB(rb11[-1][0] + 0.55, y_low)
dline(FB(0.0, 0.0), (xs_ - 1.2, Y0)); dline(p_low, (xs_ - 1.2, p_low[1]))
vdim(xs_, Y0, p_low[1])
LB = (p_low[1] - Y0) / K
val(xs_ + 1.4, p_low[1] - 4.8, '32 cm')
f.text(xs_ + 1.4, p_low[1] - 2.0, 'długość z boku', cls='note')

# =====================================================================================================================
#                                        PANEL C – przekrój poprzeczny (nasada wyrostka mieczykowatego)
# =====================================================================================================================
CC, ZF = 52.0, 77.4                 # oś i przednia powierzchnia mostka
ZS = 15.5 / 17.2                    # wymiar przednio-tylny 15,5 cm przy poprzecznym 21,5 cm → wskaźnik ok. 139


def PC(X, Z):
    return (CC + K * X, ZF + K * Z * ZS)


f.text(CC + 8.0, 73.4, 'przekrój poprzeczny na wysokości nasady wyrostka mieczykowatego · widok od góry, przód ku górze',
       cls='notec')
# obrys zewnętrzny i wewnętrzny (połowa prawa w cm: X od osi, Z od przodu)
OUT = [(0.0, 0.0), (2.6, 0.25), (5.4, 1.1), (7.9, 2.7), (9.8, 5.0), (10.75, 8.0), (10.7, 11.0), (9.8, 13.8), (8.0, 16.1),
       (5.6, 17.2), (3.6, 16.9), (2.3, 15.9), (1.3, 15.6), (0.7, 16.6), (0.0, 17.0)]
INN = [(0.0, 1.35), (2.4, 1.55), (5.0, 2.35), (7.2, 3.8), (8.75, 5.8), (9.55, 8.3), (9.5, 11.0), (8.7, 13.4), (7.2, 15.2),
       (5.4, 15.9), (4.0, 15.6), (3.0, 14.7), (2.3, 13.2), (1.6, 11.9), (0.0, 11.6)]


def full(half):
    R = [PC(x, z) for x, z in half]
    Lh = [PC(-x, z) for x, z in reversed(half[1:-1])]
    return R + Lh


outer = cr(full(OUT), closed=True, n=6)
inner = cr(full(INN), closed=True, n=6)
f.add(f'<path class="muscle" d="{poly(outer)}"/>')
f.add(f'<path class="cavity" d="{poly(inner)}"/>')
# przekroje żeber i chrząstek żebrowych w ścianie (schemat)
RIBC = [(4.2, 1.35, 'cart'), (7.15, 2.95, 'cart'), (9.55, 6.3, 'bone'), (10.1, 9.6, 'bone'), (9.55, 12.6, 'bone'),
        (7.7, 15.15, 'bone'), (4.8, 16.45, 'bone')]
for s in (-1, 1):
    for X, Z, cls in RIBC:
        cx, cy = PC(s * X, Z)
        f.add(f'<ellipse class="{cls}" cx="{cx:.2f}" cy="{cy:.2f}" rx="1.25" ry="0.8" '
              f'transform="rotate({math.degrees(math.atan2(Z - 8.6, X)) * 0 :.1f} {cx:.2f} {cy:.2f})"/>')
# mostek
sx0, sy0 = PC(-1.6, 0.0); sx1, sy1 = PC(1.6, 1.35)
f.add(f'<rect class="bone" x="{sx0:.2f}" y="{sy0 - 0.1:.2f}" width="{sx1 - sx0:.2f}" height="{sy1 - sy0 + 0.2:.2f}" rx=".9"/>')
# kręg: trzon, otwór kręgowy, łuk z wyrostkiem kolczystym
body = cr([PC(0, 11.5), PC(1.5, 11.75), PC(2.15, 12.8), PC(1.95, 14.0), PC(1.0, 14.45), PC(0, 14.4), PC(-1.0, 14.45),
           PC(-1.95, 14.0), PC(-2.15, 12.8), PC(-1.5, 11.75)], closed=True, n=5)
f.add(f'<path class="bone" d="{poly(body)}"/>')
arch = cr([PC(-1.3, 14.3), PC(1.3, 14.3), PC(1.55, 15.4), PC(0.6, 16.0), PC(0.35, 17.0), PC(0, 17.25), PC(-0.35, 17.0),
           PC(-0.6, 16.0), PC(-1.55, 15.4)], closed=True, n=5)
f.add(f'<path class="bone" d="{poly(arch)}"/>')
cvx, cvy = PC(0, 15.05)
f.add(f'<ellipse class="cavity" cx="{cvx:.2f}" cy="{cvy:.2f}" rx="{0.75 * K:.2f}" ry="{0.42 * K:.2f}"/>')
# wymiar poprzeczny (pod przekrojem)
yd = PC(0, 17.25)[1] + 2.6
xL, xR = PC(-10.75, 9.0)[0], PC(10.75, 9.0)[0]
dline(PC(-10.75, 9.5), (xL, yd + 1.2)); dline(PC(10.75, 9.5), (xR, yd + 1.2))
hdim(xL, xR, yd)
val(xL - 1.4, yd + 0.9, '20–23 cm', anchor='end')
f.text(xL - 1.4, yd + 3.6, 'wymiar poprzeczny', cls='note', anchor='end')
# wymiar przednio-tylny (z lewej strony przekroju)
xd = xL - 2.6
ytop, ybot = PC(0, 0)[1], PC(5.6, 17.2)[1]
dline(PC(-1.4, 0.0), (xd - 1.2, ytop)); dline(PC(-5.6, 17.2), (xd - 1.2, ybot))
vdim(xd, ytop, ybot)
val(xd - 1.4, (ytop + ybot) / 2 - 0.4, '15–19 cm', anchor='end')
f.text(xd - 1.4, (ytop + ybot) / 2 + 2.4, 'wymiar', cls='note', anchor='end')
f.text(xd - 1.4, (ytop + ybot) / 2 + 4.9, 'przednio-tylny', cls='note', anchor='end')
CW, CAP = (xR - xL) / K, (ybot - ytop) / K

# =====================================================================================================================
#                                        WSKAŹNIK KLATKI PIERSIOWEJ
# =====================================================================================================================
WX = 110.0
f.text(WX, 80.6, 'wskaźnik klatki piersiowej', cls='pl')
f.text(WX, 83.8, '= wymiar poprzeczny wyrażony', cls='note')
f.text(WX, 86.3, 'w odsetkach wymiaru przednio-tylnego', cls='note')
f.text(WX, 88.8, '(poprzeczny ÷ przednio-tylny × 100)', cls='note')
IDX = [(60, 'zarodek', '4 tyg.'), (90, 'płód', '2 mies.'), (105, 'noworodek', ''), (139, 'dorosły', ''), (129, 'ponad', '70 lat')]
HS = 6.6
xc_list = [113.0, 122.4, 132.0, 142.6, 153.2]
for (iv, t1, t2), xc in zip(IDX, xc_list):
    sx = HS * iv / 100 / 21.5
    sz = HS / 17.2
    o = [(xc + x * sx, 93.4 + z * sz) for x, z in [(x, z) for x, z in OUT] + [(-x, z) for x, z in reversed(OUT[1:-1])]]
    i_ = [(xc + x * sx, 93.4 + z * sz) for x, z in [(x, z) for x, z in INN] + [(-x, z) for x, z in reversed(INN[1:-1])]]
    f.add(f'<path class="muscle" d="{poly(cr(o, closed=True, n=5))}"/>')
    f.add(f'<path class="cavity" d="{poly(cr(i_, closed=True, n=5))}"/>')
    val(xc, 104.4, str(iv), anchor='middle')
    f.text(xc, 107.4, t1, cls='notec')
    if t2:
        f.text(xc, 109.9, t2, cls='notec')
f.text(WX, 113.0, 'wartości przybliżone (ok.), oprócz 139;', cls='note')
f.text(WX, 115.4, 'u kobiet wskaźnik nieco mniejszy', cls='note')

# ---------------------------------------------------------------- podpisy (przekrój)
LXC = 76.0
f.label(PC(0.8, 0.6), 'mostek', 'sternum', (LXC, 79.4), side='R')
f.label(PC(9.55, 6.3), 'żebro', 'costa', (LXC, 87.2), side='R')
f.label(PC(1.6, 13.4), 'trzon kręgu', 'corpus vertebrae', (LXC, 94.4), side='R')
f.label(PC(4.3, 15.0), 'bruzda płucna', 'sulcus pulmonalis', (LXC, 101.6), side='R')
f.label(PC(1.9, 16.2), 'bruzda żebrowo-kręgowa', 'sulcus costovertebralis', (LXC, 108.8), side='R')

f.save()
print('A: otwór górny %.1f cm, nasada wyr. mieczyk. %.1f cm, XII żebro %.1f cm' % (W1, W2, W3))
print('B: otwór górny p-t %.1f cm, z przodu %.1f cm, z tyłu %.1f cm, z boku %.1f cm' % (AP1, LF, VT[11][1], LB))
print('C: poprzeczny %.1f cm, p-t %.1f cm, wskaźnik %.0f' % (CW, CAP, CW / CAP * 100))
