# ŻEBRA XI i XII (prawe) w porównaniu z żebrem X – widok od tyłu (nieco od strony przyśrodkowej, by widać było
# powierzchnie stawowe głów). Widok od tyłu: prawa strona ciała po prawej stronie rysunku → głowy (przyśrodkowo) po lewej.
# Żebra ułożone jedno pod drugim jak w szkielecie (głowy na kolejnych kręgach Th10, Th11, Th12).
# Żebro X: głowa z dwiema powierzchniami stawowymi (grzebień głowy), szyjka, guzek z powierzchnią stawową, kąt –
# pokazana tylko część tylna (przerwane). Żebra XI i XII: cienkie listewki, mała głowa bez grzebienia (jedna powierzchnia
# stawowa), niemal bez szyjki, guzka, kąta; z przodu zaostrzone, zakończone małą chrząstką żebrową.
# Rysunek własny, schematyczny; nazwy wg karty „Żebra XI i XII” (Bochenek, t. I, s. 274–278, ryc. 186).
import sys, os; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
import math
from figlib import Fig

W, H = 150, 88
S = 0.6                     # mm rysunku / mm kości
OX, OY = 62.0, 14.0         # środek głowy żebra X (x – przyśrodkowy brzeg głowy)
DY = 27.0                   # odstęp głów kolejnych żeber (wysokość kręgu z krążkiem), mm kości
f = Fig('zebra_XI_XII', W, H,
        caption='prawe żebra X, XI i XII · widok od tyłu (nieco od strony przyśrodkowej); żebro X przerwane za kątem')


def T(x, y):
    return (OX + x * S, OY + y * S)


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


def bump(u, uc, h, s):
    return h * math.exp(-((u - uc) / s) ** 2)


def poly(pts, close=True):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + (' Z' if close else '')


class Rib:
    """żebro w widoku od tyłu: linia środkowa + połowa wysokości ku górze (up) i ku dołowi (lo)"""

    def __init__(self, ctrl, dy, w_up, w_lo, n=500):
        self.N = n
        self.C, self.LEN = resample(bez([T(x, y + dy) for x, y in ctrl], n=24), n)
        self.U = [k / n for k in range(n + 1)]
        self.TAN = [self._tan(i) for i in range(n + 1)]
        self.NUP = [(ty, -tx) for tx, ty in self.TAN]          # normalna ku górze
        self.w_up, self.w_lo = w_up, w_lo

    def _tan(self, i):
        a, b = self.C[max(i - 1, 0)], self.C[min(i + 1, self.N)]
        d = math.dist(a, b)
        return ((b[0] - a[0]) / d, (b[1] - a[1]) / d)

    def ipt(self, u):
        return min(max(int(round(u * self.N)), 0), self.N)

    def edge(self, i, side, extra=0.0):
        c, n = self.C[i], self.NUP[i]
        w = (self.w_up(self.U[i]) if side > 0 else self.w_lo(self.U[i])) + extra
        return (c[0] + side * n[0] * w, c[1] + side * n[1] * w)

    def UV(self, u, v, extra=0.0):
        i = self.ipt(u)
        c, n = self.C[i], self.NUP[i]
        w = (self.w_up(u) if v >= 0 else self.w_lo(u)) * abs(v) + extra
        s = 1 if v >= 0 else -1
        return (c[0] + s * n[0] * w, c[1] + s * n[1] * w)

    def build(self, end='round', end_flat=0.35):
        N, C, TAN, NUP = self.N, self.C, self.TAN, self.NUP
        self.upper = [self.edge(i, +1) for i in range(N + 1)]
        self.lower = [self.edge(i, -1) for i in range(N + 1)]
        c0, t0 = C[0], TAN[0]
        self.r0 = r0 = (self.w_up(0) + self.w_lo(0)) / 2
        head = []                                   # od brzegu dolnego przez szczyt głowy do górnego
        for k in range(1, 30):
            a = math.pi * k / 30
            v = (-NUP[0][0] * math.cos(a) - t0[0] * math.sin(a), -NUP[0][1] * math.cos(a) - t0[1] * math.sin(a))
            head.append((c0[0] + v[0] * r0, c0[1] + v[1] * r0))
        self.head = head
        cE, tE = C[N], TAN[N]
        rE = (self.w_up(1) + self.w_lo(1)) / 2
        endc = []
        if end == 'round':
            for k in range(1, 14):
                a = math.pi * k / 14
                v = (NUP[N][0] * math.cos(a) + tE[0] * math.sin(a) * end_flat, NUP[N][1] * math.cos(a) + tE[1] * math.sin(a) * end_flat)
                endc.append((cE[0] + v[0] * rE, cE[1] + v[1] * rE))
        else:                                       # przerwanie – lekko poszarpana krawędź
            for k in range(1, 6):
                a = k / 6
                p = (self.upper[N][0] + (self.lower[N][0] - self.upper[N][0]) * a,
                     self.upper[N][1] + (self.lower[N][1] - self.upper[N][1]) * a)
                j = (0.55, -0.45, 0.4, -0.5, 0.3)[k - 1] * S
                endc.append((p[0] + tE[0] * j, p[1] + tE[1] * j))
        self.rE = rE
        self.outline = self.upper + endc + self.lower[::-1] + head
        return self.outline


def head_facets(rib, split=None):
    """powierzchnie stawowe głowy na przyśrodkowym końcu (widoczne nieco od strony przyśrodkowej).
    split=None → jedna powierzchnia; split=k → dwie, rozdzielone grzebieniem (k – indeks punktu łuku głowy)"""
    t0, r0 = rib.TAN[0], rib.r0
    arc = rib.head[2:-2]
    m = len(arc)

    def cres(pts, depth):
        mm = len(pts)
        inn = [(x + t0[0] * r0 * depth * math.sin(math.pi * k / (mm - 1)) ** 0.7,
                y + t0[1] * r0 * depth * math.sin(math.pi * k / (mm - 1)) ** 0.7) for k, (x, y) in enumerate(pts)]
        return pts + inn[::-1]

    if split is None:
        f.add(f'<path class="facet" d="{poly(cres(arc, 0.62))}"/>')
        return None
    lo, up = arc[:split], arc[split + 1:]
    f.add(f'<path class="facet" d="{poly(cres(lo, 0.62))}"/>')
    f.add(f'<path class="facet" d="{poly(cres(up, 0.55))}"/>')
    # grzebień głowy – krótki wał między powierzchniami
    p = arc[split]
    q = (p[0] + t0[0] * r0 * 0.75, p[1] + t0[1] * r0 * 0.75)
    f.add(f'<path class="bonel" d="M{p[0] - t0[0] * 0.25:.2f},{p[1] - t0[1] * 0.25:.2f} L{q[0]:.2f},{q[1]:.2f}"/>')
    return p


# ================= żebro X (część tylna) =================
CX = [(4.5, 0.0), (11, -0.6), (18, -0.3), (25, 1.0), (33, 3.4), (43, 7.3), (53, 12.3), (63, 18.0), (73, 24.0),
      (82, 30.0), (88, 34.0)]
U_TUB_X = 0.215
WX_UP = [(0, 5.2), (0.04, 5.0), (0.09, 3.4), (0.17, 3.5), (0.26, 4.6), (0.45, 5.3), (1.0, 5.6)]
WX_LO = [(0, 5.2), (0.04, 5.0), (0.09, 3.4), (0.17, 3.6), (0.26, 4.8), (0.45, 5.4), (1.0, 5.6)]
ribX = Rib(CX, 0.0, lambda u: lerp(WX_UP, u) * S,
           lambda u: (lerp(WX_LO, u) + bump(u, U_TUB_X, 2.6, 0.035)) * S)
ribX.build(end='break')

# ================= żebro XI =================
CXI = [(4.2, 0.0), (11, 0.4), (20, 2.0), (31, 5.2), (43, 9.6), (55, 15.0), (66, 21.4), (76, 28.8), (84, 37.0),
       (90, 46.0), (94, 55.0), (96, 63.0)]
WXI = [(0, 3.9), (0.03, 3.7), (0.08, 2.9), (0.16, 3.0), (0.3, 3.3), (0.6, 3.2), (0.85, 2.6), (1.0, 1.9)]
ribXI = Rib(CXI, DY, lambda u: lerp(WXI, u) * S, lambda u: lerp(WXI, u) * S)
ribXI.build(end='round', end_flat=0.12)

# ================= żebro XII =================
CXII = [(4.0, 0.0), (11, 0.6), (20, 2.6), (30, 6.0), (40, 10.5), (49, 16.0), (57, 22.5), (63, 29.5), (67, 36.5)]
WXII = [(0, 3.7), (0.04, 3.5), (0.1, 2.9), (0.2, 3.0), (0.4, 3.1), (0.75, 2.6), (1.0, 1.8)]
ribXII = Rib(CXII, 2 * DY, lambda u: lerp(WXII, u) * S, lambda u: lerp(WXII, u) * S)
ribXII.build(end='round', end_flat=0.12)


# ---------- chrząstki żebrowe XI i XII: krótkie zaostrzenie na końcu (rysowane pod kością) ----------
def cart_tip(rib, L):
    N = rib.N
    cE, tE, nE = rib.C[N], rib.TAN[N], rib.NUP[N]
    rE = rib.rE
    pts = [rib.edge(rib.ipt(0.985), +1, -0.05)]
    for k in range(1, 12):
        a = k / 12
        w = rE * (1 - a ** 1.6) ** 0.9 * 1.02
        pts.append((cE[0] + tE[0] * L * a + nE[0] * w, cE[1] + tE[1] * L * a + nE[1] * w))
    pts.append((cE[0] + tE[0] * L, cE[1] + tE[1] * L))
    for k in range(11, 0, -1):
        a = k / 12
        w = rE * (1 - a ** 1.6) ** 0.9 * 1.02
        pts.append((cE[0] + tE[0] * L * a - nE[0] * w, cE[1] + tE[1] * L * a - nE[1] * w))
    pts.append(rib.edge(rib.ipt(0.985), -1, -0.05))
    f.add(f'<path class="cart" d="{poly(pts)}"/>')
    return (cE[0] + tE[0] * L * 0.45, cE[1] + tE[1] * L * 0.45)


P_CART_XI = cart_tip(ribXI, 11.0 * S)
P_CART_XII = cart_tip(ribXII, 9.0 * S)

for rb in (ribX, ribXI, ribXII):
    f.add(f'<path class="bone" d="{poly(rb.outline)}"/>')

# ---------- żebro X: szczegóły końca tylnego ----------
# przerwanie – powierzchnia złamu
cE, tE, nE = ribX.C[ribX.N], ribX.TAN[ribX.N], ribX.NUP[ribX.N]
ang = math.degrees(math.atan2(nE[1], nE[0]))
f.add(f'<ellipse class="bone2" cx="{cE[0] + tE[0] * 0.1:.2f}" cy="{cE[1] + tE[1] * 0.1:.2f}" rx="{ribX.rE * 0.95:.2f}" '
      f'ry="{ribX.rE * 0.30:.2f}" transform="rotate({ang:.1f} {cE[0] + tE[0] * 0.1:.2f} {cE[1] + tE[1] * 0.1:.2f})"/>')
# głowa: dwie powierzchnie stawowe (górna mniejsza) rozdzielone grzebieniem głowy
P_CREST = head_facets(ribX, split=13)
# granica głowy i szyjki
for rb, uu in ((ribX, 0.05), (ribXI, 0.045), (ribXII, 0.05)):
    i = rb.ipt(uu)
    a_, b_ = rb.edge(i, +1, -0.2), rb.edge(i, -1, -0.2)
    q = (rb.C[i][0] - rb.TAN[i][0] * 0.45, rb.C[i][1] - rb.TAN[i][1] * 0.45)
    f.add(f'<path class="bonel" d="M{a_[0]:.2f},{a_[1]:.2f} Q{q[0]:.2f},{q[1]:.2f} {b_[0]:.2f},{b_[1]:.2f}"/>')
# guzek żebra: wyniosłość w dolnej części końca szyjki; powierzchnia stawowa w części przyśrodkowej guzka
gt = ribX.UV(U_TUB_X + 0.004, -0.55)
f.add(f'<ellipse class="facet" cx="{gt[0] - 0.6:.2f}" cy="{gt[1]:.2f}" rx="1.35" ry="1.05"/>')
arc_t = [ribX.UV(U_TUB_X + du, v) for du, v in [(-0.03, -0.95), (-0.02, -0.15), (0.0, 0.1), (0.025, -0.1), (0.04, -0.9)]]
f.add(f'<path class="bonel" d="{poly(bez(arc_t, n=8), close=False)}"/>')
# kąt żebra: linia na powierzchni zewnętrznej
U_ANG = 0.66
a_, b_ = ribX.edge(ribX.ipt(U_ANG - 0.02), +1, -0.15), ribX.edge(ribX.ipt(U_ANG + 0.015), -1, -0.15)
f.add(f'<path class="bonel" d="M{a_[0]:.2f},{a_[1]:.2f} Q{ribX.C[ribX.ipt(U_ANG)][0] + 0.5:.2f},{ribX.C[ribX.ipt(U_ANG)][1] - 0.2:.2f} {b_[0]:.2f},{b_[1]:.2f}"/>')

# ---------- żebra XI i XII: jedna powierzchnia stawowa głowy (bez grzebienia) ----------
head_facets(ribXI)
head_facets(ribXII)


# ---------- podpisy ----------
def headpt(rb, k, inset=0.55):
    p = rb.head[k]
    t0, r0 = rb.TAN[0], rb.r0
    return (p[0] + t0[0] * r0 * inset * 0.5, p[1] + t0[1] * r0 * inset * 0.5)


P_FSUP = headpt(ribX, 21)
P_FINF = headpt(ribX, 6)
P_FXI = headpt(ribXI, 15)
P_FXII = headpt(ribXII, 15)
P_FTUB = (gt[0] - 0.6, gt[1])
P_ANG = ribX.UV(U_ANG - 0.005, 0.85)
P_X = ribX.UV(0.85, 0.0)
P_XI = ribXI.UV(0.70, 0.0)
P_XII = ribXII.UV(0.55, 0.0)

TL = 57.0
f.label(P_FSUP, 'powierzchnia stawowa głowy żebra górna', 'facies articularis capitis costae superior', (TL, 4.5), side='L')
f.label(P_CREST, 'grzebień głowy żebra', 'crista capitis costae', (TL, 13.5), side='L')
f.label(P_FINF, 'powierzchnia stawowa głowy żebra dolna', 'facies articularis capitis costae inferior', (TL, 22.5), side='L')
f.label(P_FXI, 'powierzchnia stawowa głowy żebra', 'facies articularis capitis costae', (TL, 37.5), side='L')
f.label(P_FXII, '', None, (TL, 37.5), side='L')
f.text(TL - 0.7, 44.0, '(XI, XII – jedna, bez grzebienia)', cls='note', anchor='end')
f.text(TL - 0.7, 58.0, 'XI i XII – cienkie listewki kostne:', cls='note', anchor='end')
f.text(TL - 0.7, 61.0, 'niemal bez szyjki, guzka, kąta', cls='note', anchor='end')
f.text(TL - 0.7, 64.0, 'i bruzdy żebra', cls='note', anchor='end')
f.label(P_FTUB, 'powierzchnia stawowa guzka żebra', 'facies articularis tuberculi costae', (80.0, 4.5), side='R')
f.label(P_ANG, 'kąt żebra', 'angulus costae', (123.0, 16.0), side='R')
f.label(P_X, 'żebro X', 'costa X', (123.0, 30.0), side='R')
f.label(P_XI, 'żebro XI', 'costa XI', (123.0, 50.0), side='R')
f.label(P_CART_XI, 'chrząstka żebrowa', 'cartilago costalis', (123.0, 72.0), side='R')
f.label(P_XII, 'żebro XII', 'costa XII', (80.0, 76.0), side='L')

if os.environ.get('PTS'):
    for nm, p in [('fsup', P_FSUP), ('finf', P_FINF), ('crest', P_CREST), ('fxi', P_FXI), ('fxii', P_FXII), ('ftub', P_FTUB),
                  ('ang', P_ANG), ('X', P_X), ('XI', P_XI), ('XII', P_XII), ('cartXI', P_CART_XI), ('cartXII', P_CART_XII)]:
        print(f'{nm:7s} ({p[0]:.1f}, {p[1]:.1f})')
    for nm, rb in (('X', ribX), ('XI', ribXI), ('XII', ribXII)):
        xs = [p[0] for p in rb.outline]; ys = [p[1] for p in rb.outline]
        print(nm, 'bbox', round(min(xs), 1), round(max(xs), 1), round(min(ys), 1), round(max(ys), 1), 'LEN', round(rb.LEN / S))

f.save()
