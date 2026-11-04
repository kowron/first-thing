# ŻEBRO DRUGIE (prawe, kość żebrowa) – widok od góry, przód ku górze rysunku.
# Orientacja jak w rysunku „zebro_I”: prawa strona ciała po prawej stronie rysunku → koniec tylny (głowa, szyjka)
# i koniec przedni leżą przyśrodkowo (po lewej), żebro wygina się łukiem bocznie (w prawo).
# Od góry widać powierzchnię zewnętrzną (wypukłą, skierowaną ku górze i nieco bocznie) z guzowatością m. zębatego
# przedniego (część środkowa) i – do tyłu i nieco ku górze od niej – przyczepem m. pochyłego tylnego.
# Wewnątrz łuku: zarys żebra I w tej samej skali (porównanie długości i wygięcia; „podobnie wygięte”).
# Rysunek własny, schematyczny; nazwy wg karty „Żebro II” (Bochenek, t. I, s. 277, ryc. 185).
import sys, os; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
import math
from figlib import Fig

W, H = 150, 104
S = 0.75                    # mm rysunku / mm kości
X0, Y0 = 22.0, 76.5         # rysunek ← kość: X w bok (w prawo), Y do przodu (w górę)
f = Fig('zebro_II', W, H, caption='prawe żebro II (kość żebrowa) · widok od góry (przód ku górze); wewnątrz zarys żebra I')


def T(X, Y):
    return (X0 + X * S, Y0 - Y * S)


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
    """żebro widziane od góry: linia środkowa + szerokości po stronie wklęsłej (in) i wypukłej (out)"""

    def __init__(self, ctrl, w_in, w_out, n=600, tf=T):
        self.N = n
        self.C, self.LEN = resample(bez([tf(*p) for p in ctrl], n=24), n)
        self.U = [k / n for k in range(n + 1)]
        self.TAN = [self._tan(i) for i in range(n + 1)]
        self.NIN = [(ty, -tx) for tx, ty in self.TAN]      # normalna ku stronie wklęsłej
        self.w_in, self.w_out = w_in, w_out

    def _tan(self, i):
        a, b = self.C[max(i - 1, 0)], self.C[min(i + 1, self.N)]
        d = math.dist(a, b)
        return ((b[0] - a[0]) / d, (b[1] - a[1]) / d)

    def ipt(self, u):
        return min(max(int(round(u * self.N)), 0), self.N)

    def edge(self, i, side, extra=0.0):
        c, n = self.C[i], self.NIN[i]
        w = (self.w_in(self.U[i]) if side > 0 else self.w_out(self.U[i])) + extra
        return (c[0] + side * n[0] * w, c[1] + side * n[1] * w)

    def at(self, u):
        x = min(max(u, 0.0), 1.0) * self.N
        i = min(int(x), self.N - 1)
        a = x - i
        C, NI = self.C, self.NIN
        c = (C[i][0] + (C[i + 1][0] - C[i][0]) * a, C[i][1] + (C[i + 1][1] - C[i][1]) * a)
        n = (NI[i][0] + (NI[i + 1][0] - NI[i][0]) * a, NI[i][1] + (NI[i + 1][1] - NI[i][1]) * a)
        return c, n

    def UV(self, u, v, extra=0.0):
        """u – wzdłuż żebra (0 głowa … 1 koniec przedni); v – w poprzek (+1 brzeg wklęsły, −1 brzeg wypukły)"""
        c, n = self.at(u)
        w = (self.w_in(u) if v >= 0 else self.w_out(u)) * abs(v) + extra
        s = 1 if v >= 0 else -1
        return (c[0] + s * n[0] * w, c[1] + s * n[1] * w)

    def field(self, u0, du, v0, dv, n=48):
        return [self.UV(u0 + du * math.cos(2 * math.pi * k / n), v0 + dv * math.sin(2 * math.pi * k / n)) for k in range(n)]

    def outline(self, end_flat=0.30):
        N, C, TAN, NIN = self.N, self.C, self.TAN, self.NIN
        inner = [self.edge(i, +1) for i in range(N + 1)]
        outer = [self.edge(i, -1) for i in range(N + 1)]
        c0, t0 = C[0], TAN[0]
        self.r0 = r0 = (self.w_in(0) + self.w_out(0)) / 2
        cap_head = []
        for k in range(1, 24):
            a = math.pi * k / 24
            nx, ny = NIN[0]
            v = (-nx * math.cos(a) - t0[0] * math.sin(a), -ny * math.cos(a) - t0[1] * math.sin(a))
            cap_head.append((c0[0] + v[0] * r0, c0[1] + v[1] * r0))
        cE, tE = C[N], TAN[N]
        self.rE = rE = (self.w_in(1) + self.w_out(1)) / 2
        cap_end = []
        for k in range(1, 18):
            a = math.pi * k / 18
            nx, ny = NIN[N]
            v = (-nx * math.cos(a) + tE[0] * math.sin(a) * end_flat, -ny * math.cos(a) + tE[1] * math.sin(a) * end_flat)
            cap_end.append((cE[0] + v[0] * rE, cE[1] + v[1] * rE))
        self.cap_head = cap_head
        return outer + cap_end + inner[::-1] + cap_head[::-1]


# ================= zarys żebra I (te same dane co w rysunku „zebro_I”; przesunięty do wnętrza łuku żebra II) =========
CTRL_I = [(13, -1), (20, -5), (28, -9), (35, -10.5), (42, -9), (48, -5), (53, 1), (57, 9), (59, 18), (58.5, 27),
          (56, 35), (51.5, 42), (45.5, 48), (38.5, 52.5), (32, 55)]
DX_I, DY_I = 7.0, 15.0
W_IN_I = [(0, 5.0), (0.03, 4.4), (0.07, 3.3), (0.13, 3.3), (0.2, 4.5), (0.3, 5.5), (0.42, 6.5), (0.55, 7.3),
          (0.7, 8.1), (0.85, 8.9), (1.0, 9.6)]
W_OUT_I = [(0, 5.0), (0.03, 4.4), (0.07, 3.3), (0.13, 3.5), (0.2, 4.8), (0.3, 5.8), (0.42, 6.8), (0.55, 7.6),
           (0.7, 8.4), (0.85, 9.2), (1.0, 10.0)]
rib1 = Rib([(x + DX_I, y + DY_I) for x, y in CTRL_I],
           lambda u: (lerp(W_IN_I, u) + bump(u, 0.60, 2.1, 0.02)) * S,
           lambda u: (lerp(W_OUT_I, u) + bump(u, 0.17, 3.0, 0.028)) * S)
out1 = rib1.outline()
f.add(f'<path class="shade" d="{poly(out1)}"/>')
f.add(f'<path class="dim" d="{poly(out1)}"/>')

# ================= żebro II =================
# linia środkowa (mm kości; początek: środek trzonu kręgu, X – w bok, Y – do przodu)
CTRL = [(14, -1), (21.5, -6.5), (29.5, -12), (38, -15.8), (47, -17.4), (56, -16), (65, -11.5), (73, -4.5), (80, 4),
        (85.5, 14), (88.5, 25), (89, 36), (87, 47), (82.5, 58), (76, 68), (68, 76.5), (59.5, 83), (51, 88)]
U_TUB = 0.112          # guzek żebra – na brzegu wypukłym (tylnym)
U_TUBR = 0.575         # guzowatość m. zębatego przedniego – część środkowa powierzchni zewnętrznej
W_IN = [(0, 4.7), (0.02, 4.3), (0.05, 3.3), (0.1, 3.3), (0.16, 4.4), (0.25, 5.5), (0.4, 6.1), (0.6, 6.2), (0.8, 6.2),
        (0.92, 6.5), (1.0, 6.9)]
W_OUT = [(0, 4.7), (0.02, 4.3), (0.05, 3.4), (0.1, 3.6), (0.16, 4.7), (0.25, 5.7), (0.4, 6.3), (0.6, 6.4), (0.8, 6.4),
         (0.92, 6.7), (1.0, 7.1)]
rib = Rib(CTRL,
          lambda u: lerp(W_IN, u) * S,
          lambda u: (lerp(W_OUT, u) + bump(u, U_TUB, 2.9, 0.022) + bump(u, U_TUBR, 0.7, 0.05)) * S)
outline = rib.outline()
f.add(f'<path class="bone" d="{poly(outline)}"/>')
N, C, TAN, NIN, U = rib.N, rib.C, rib.TAN, rib.NIN, rib.U
ipt, edge, UV = rib.ipt, rib.edge, rib.UV

# brzeg wypukły zaokrąglony (powierzchnia zewnętrzna przechodzi w wewnętrzną) – pas cienia wzdłuż brzegu
ia, ib = ipt(0.15), ipt(0.985)
sh_o = [edge(i, -1, -0.12) for i in range(ia, ib + 1)]
sh_i = []
for i in range(ia, ib + 1):
    u = U[i]
    taper = min(1.0, (u - 0.15) / 0.06, (0.985 - u) / 0.05)
    sh_i.append(edge(i, -1, -0.12 - 1.2 * S * taper))
f.add(f'<path class="shade" d="{poly(sh_o + sh_i[::-1])}"/>')

# guzowatość m. zębatego przedniego – nieznaczna, chropowata (lekko wyniesione pole z kreseczkami)
F_TUBR = rib.field(U_TUBR, 0.078, -0.30, 0.58)
f.add(f'<path class="bone2" d="{poly(F_TUBR)}"/>')
# przyczep m. zębatego przedniego: dolna część 1. zęba i cały 2. ząb – na guzowatości
F_SER1 = rib.field(U_TUBR - 0.040, 0.020, -0.42, 0.30)
F_SER2 = rib.field(U_TUBR + 0.020, 0.034, -0.36, 0.36)
# przyczep m. pochyłego tylnego – do tyłu i nieco ku górze (ku brzegowi wklęsłemu) od guzowatości
F_SCP = rib.field(0.405, 0.055, 0.20, 0.40)
for fp in (F_SER1, F_SER2, F_SCP):
    f.add(f'<path class="muscle" d="{poly(fp)}"/>')
# kreseczki chropowatości na guzowatości (poza polami mięśnia)
for uu, vv in [(U_TUBR - 0.068, -0.05), (U_TUBR - 0.070, -0.45), (U_TUBR + 0.068, -0.05), (U_TUBR + 0.066, -0.50),
               (U_TUBR - 0.012, 0.14), (U_TUBR + 0.030, 0.12)]:
    a_, b_ = UV(uu - 0.006, vv + 0.07), UV(uu + 0.006, vv - 0.07)
    f.add(f'<path class="bonel" d="M{a_[0]:.2f},{a_[1]:.2f} L{b_[0]:.2f},{b_[1]:.2f}"/>')

# koniec przedni: chropowata, wgłębiona powierzchnia do połączenia z chrząstką żebrową
cE, tE, rE = C[N], TAN[N], rib.rE
ang = math.degrees(math.atan2(NIN[N][1], NIN[N][0]))
ex, ey = cE[0] + tE[0] * 0.15, cE[1] + tE[1] * 0.15
f.add(f'<ellipse class="bone2" cx="{ex:.2f}" cy="{ey:.2f}" rx="{rE * 0.92:.2f}" ry="{rE * 0.24:.2f}" '
      f'transform="rotate({ang:.1f} {ex:.2f} {ey:.2f})"/>')

# głowa: powierzchnia stawowa na końcu przyśrodkowym (od góry widać jej górną część)
t0, r0 = TAN[0], rib.r0
arc = [rib.cap_head[k] for k in range(3, 21)]
m = len(arc)
cres = [(x + t0[0] * r0 * 0.55 * math.sin(math.pi * k / (m - 1)), y + t0[1] * r0 * 0.55 * math.sin(math.pi * k / (m - 1)))
        for k, (x, y) in enumerate(arc)]
f.add(f'<path class="facet" d="{poly(arc + cres[::-1])}"/>')
# granica głowy i szyjki
ih = ipt(0.035)
a_, b_ = edge(ih, +1, -0.2), edge(ih, -1, -0.2)
f.add(f'<path class="bonel" d="M{a_[0]:.2f},{a_[1]:.2f} Q{C[ih][0] - TAN[ih][0] * 0.5:.2f},{C[ih][1] - TAN[ih][1] * 0.5:.2f} {b_[0]:.2f},{b_[1]:.2f}"/>')

# guzek żebra: powierzchnia stawowa guzka (od góry widoczna jako wąski rąbek na brzegu tylnym)
ta, tb = ipt(U_TUB - 0.026), ipt(U_TUB + 0.010)
lens_o = [edge(i, -1, -0.1) for i in range(ta, tb + 1)]
mm_ = len(lens_o)
lens_i = [edge(i, -1, -0.1 - 0.8 * math.sin(math.pi * k / (mm_ - 1)) ** 0.8) for k, i in enumerate(range(ta, tb + 1))]
f.add(f'<path class="facet" d="{poly(lens_o + lens_i[::-1])}"/>')


# ---------- podpisy ----------
def cen(pts):
    return (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))


P_HEAD = UV(0.0, 0.0)
P_HEAD = (P_HEAD[0] - TAN[0][0] * r0 * 0.3, P_HEAD[1] - TAN[0][1] * r0 * 0.3)
P_NECK = C[ipt(0.065)]
P_TUB = UV(U_TUB, -1.0, -0.6)
P_END = (ex - tE[0] * 0.05, ey - tE[1] * 0.05)
P_RIB2 = UV(0.885, -0.2)
P_OUTS = UV(0.73, -0.2)
P_SCP = cen(F_SCP)
P_TUBR = UV(U_TUBR - 0.068, -0.25)
P_SER = cen(F_SER2)
P_RIB1 = rib1.UV(0.47, 0.9)

TL, TR = 26.0, 100.0
f.label(P_END, 'koniec przedni', None, (TL + 14, 9.0), side='L')
f.text(TL + 13.3, 12.6, '(do chrząstki żebrowej)', cls='note', anchor='end')
f.label(P_HEAD, 'głowa żebra', 'caput costae', (TL, 74.0), side='L')
f.label(P_NECK, 'szyjka żebra', 'collum costae', (TL, 84.0), side='L')
f.label(P_TUB, 'guzek żebra', 'tuberculum costae', (TL, 94.0), side='L')

f.label(P_RIB2, 'żebro II', 'costa II', (TR, 7.0), side='R')
f.label(P_OUTS, 'powierzchnia zewnętrzna', None, (TR, 19.0), side='R')
f.text(TR + 0.7, 22.6, '(wypukła; ku górze i nieco bocznie)', cls='note')
f.label(P_SER, 'przyczep m. zębatego przedniego', 'm. serratus anterior', (TR, 33.0), side='R')
f.label(P_TUBR, 'guzowatość m. zębatego przedniego', 'tuberositas m. serrati anterioris', (TR, 58.0), side='R')
f.label(P_SCP, 'przyczep m. pochyłego tylnego', 'm. scalenus posterior', (TR, 75.0), side='R')
f.label(P_RIB1, 'żebro I', 'costa I', (TL, 44.0), side='L')
f.text(TL - 0.7, 50.3, '(zarys – porównanie)', cls='note', anchor='end')

if os.environ.get('PTS'):
    for nm, p in [('head', P_HEAD), ('neck', P_NECK), ('tub', P_TUB), ('end', P_END), ('rib2', P_RIB2), ('outs', P_OUTS),
                  ('scp', P_SCP), ('tubr', P_TUBR), ('ser', P_SER), ('rib1', P_RIB1)]:
        print(f'{nm:5s} ({p[0]:.1f}, {p[1]:.1f})')
    xs = [p[0] for p in outline]; ys = [p[1] for p in outline]
    print('bbox II', round(min(xs), 1), round(max(xs), 1), round(min(ys), 1), round(max(ys), 1), 'LEN', round(rib.LEN / S))
    xs = [p[0] for p in out1]; ys = [p[1] for p in out1]
    print('bbox I', round(min(xs), 1), round(max(xs), 1), round(min(ys), 1), round(max(ys), 1), 'LEN', round(rib1.LEN / S))

f.save()
