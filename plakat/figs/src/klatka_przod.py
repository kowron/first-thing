# KLATKA PIERSIOWA – widok od przodu (prawa strona ciała po lewej stronie rysunku).
# Ściany: z przodu mostek, z boków żebra (oddzielone przestrzeniami międzyżebrowymi), z tyłu część piersiowa kręgosłupa
# (widoczna w otworze górnym i między łukami żebrowymi). Model uproszczony: każde żebro to pasmo, którego część przednia
# (kość żebrowa – krem, chrząstka żebrowa – niebieska) leży przed częścią tylną (ciemniejszy krem – widoczna w głębi,
# w przestrzeniach międzyżebrowych). Wymiary wg Bochenka (s. 290–293): wcięcie szyjne na poziomie Th2/Th3,
# podstawa wyrostka mieczykowatego Th9/Th10, kąt podmostkowy ok. 90°, chrząstki: I lekko zstępuje, II pozioma,
# III–V coraz bardziej wstępują, dalsze – kąt w obrębie chrząstki; VIII–X dochodzą do chrząstki wyższej, XI–XII wolne.
# Rysunek własny, schematyczny; nazwy wg kart „Ściany i kształt klatki” i pokrewnych (Bochenek, t. I, s. 273–298, ryc. 196).
import sys, os; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
import math
from figlib import Fig

W, H = 150, 117
K = 3.0                     # mm rysunku / cm
CX, Y0 = 75.0, 10.5         # oś symetrii; poziom Y=0 (górny brzeg trzonu Th1)
f = Fig('klatka_przod', W, H, caption='klatka piersiowa · widok od przodu')

RIGHT, LEFT = -1, +1        # strona ciała → kierunek na rysunku (prawa strona ciała po lewej)


def M(X, Y, s):
    return (CX + s * X * K, Y0 + Y * K)


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

# 4) kąt podmostkowy – łuk pomocniczy między łukami żebrowymi (wierzchołek u podstawy wyrostka mieczykowatego)
APEX = (0.0, YJ + (84.0 - 9.35) * KS)
R_ANG, TH_ANG = 4.4, 52
arc = [M(R_ANG * math.sin(math.radians(t)), APEX[1] + R_ANG * math.cos(math.radians(t)), LEFT)
       for t in range(-TH_ANG, TH_ANG + 1, 4)]
f.add(f'<path class="dim" d="{poly(arc, close=False)}"/>')

# 5) numery żeber (po lewej stronie ciała – na części przedniej / na końcu żeber XI i XII)
ROM = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
NUM_U = {1: 0.42, 2: 0.35, 3: 0.33, 4: 0.33, 5: 0.33, 6: 0.33, 7: 0.33, 8: 0.36, 9: 0.40, 10: 0.45}
NUMS = {}
for n in range(1, 11):
    ln, us, wf = ribs[n]
    NUMS[n] = M(*ln.pt(us + NUM_U[n] * (1 - us)), LEFT)
NUMS[11] = M(*free[11].pt(0.80), LEFT)
NUMS[12] = M(*free[12].pt(0.78), LEFT)
for n, (x, y) in NUMS.items():
    f.text(x, y + 0.75, ROM[n - 1], cls='notec')

# ---------- podpisy ----------
P_AP = M(2.7, 3.0, RIGHT)
ln4, us4, _ = ribs[4]
P_OS = M(*ln4.pt(us4 + 0.42 * (1 - us4)), RIGHT)
P_CC = M(*RIB[5][4], RIGHT)
P_CART = M(*carts[6].pt(0.62), RIGHT)
P_ARC = M(*carts[8].pt(0.70, -0.30), RIGHT)
P_XII = M(*free[12].pt(0.62), RIGHT)

P_SPINE = M(0.5, 2.75, LEFT)
P_SP = M(5.8, 6.2, LEFT)
P_ST = M(0.45, 11.0, LEFT)
ln6, us6, _ = ribs[6]
P_RIB = M(*ln6.pt(us6 + 0.62 * (1 - us6)), LEFT)
P_ANG = M(R_ANG * math.sin(math.radians(22)), APEX[1] + R_ANG * math.cos(math.radians(22)), LEFT)
P_VB = M(0.9, 25.3, LEFT)

f.label(P_AP, 'otwór górny klatki piersiowej', 'apertura thoracis superior', (53.0, 8.0), side='L')
f.label(P_OS, 'kość żebrowa', 'os costale', (37.0, 36.0), side='L')
f.label(P_CC, 'granica kości i chrząstki', None, (36.0, 55.0), side='L')
f.label(P_CART, 'chrząstka żebrowa', 'cartilago costalis', (36.0, 68.0), side='L')
f.label(P_ARC, 'łuk żebrowy', 'arcus costalis', (36.0, 84.0), side='L')
f.label(P_XII, 'żebro XII', 'costa XII', (36.0, 100.0), side='L')

f.label(P_SPINE, 'kręgosłup – część piersiowa', None, (98.0, 8.0), side='R')
f.text(98.7, 11.6, '(ściana tylna)', cls='note')
f.label(P_SP, 'przestrzenie międzyżebrowe', 'spatia intercostalia', (104.0, 26.0), side='R')
f.label(P_ST, 'mostek', 'sternum', (108.0, 40.0), side='R')
f.text(108.7, 46.3, '(ściana przednia)', cls='note')
f.label(P_RIB, 'żebro', 'costa', (114.0, 58.0), side='R')
f.text(114.7, 64.3, '(ściany boczne)', cls='note')
f.label(P_ANG, 'kąt podmostkowy', 'angulus infrasternalis', (114.0, 78.0), side='R')
f.label(P_VB, 'trzon kręgu', 'corpus vertebrae', (114.0, 92.0), side='R')

if os.environ.get('PTS'):
    for n in sorted(ribs):
        ln, us, wf = ribs[n]
        print(n, 'lat', [round(v, 2) for v in ln.P[ln.i(us)]], 'us', round(us, 3))
    print('ST', {k: tuple(round(v, 2) for v in p) for k, p in ST.items()})
    print('VT', [(round(a, 2), round(b, 2)) for a, b, c in VT])

f.save()
