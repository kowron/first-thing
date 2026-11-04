# ŻEBRO TYPOWE (prawe żebro VII, kość żebrowa) – widok od dołu, przód ku górze rysunku.
# Prawa strona ciała → bok rysunku po lewej (widok od dołu, przód u góry); kręgosłup po prawej.
# Od dołu widać: wypukłość żebra (krzywizna płaszczyzny), głowę, szyjkę, guzek, kąt, trzon, bruzdę żebra
# (przy dolnym brzegu powierzchni wewnętrznej → od dołu po stronie wklęsłej) i koniec przedni.
# Wstawka: przekrój poprzeczny trzonu (położenie bruzdy). Nazwy wg Bochenka, t. I, s. 274–275 (ryc. 184).
import sys, os; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
import math
from figlib import Fig, smooth

W, H = 140, 104
S = 0.5                    # mm rysunku / mm kości
X0, Y0 = 112.0, 82.0       # punkt odniesienia (X=0, Y=0 kości)
f = Fig('zebro_typowe', W, H, caption='żebro typowe (prawe żebro VII) · widok od dołu (przód ku górze)')


def T(X, Y):
    """kość (X – w bok od linii pośrodkowej, Y – do przodu; mm) → rysunek"""
    return (X0 - X * S, Y0 - Y * S)


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
    """liniowo-gładka interpolacja wartości zadanych w punktach (u, v)"""
    if u <= ctrl[0][0]:
        return ctrl[0][1]
    for (u0, v0), (u1, v1) in zip(ctrl, ctrl[1:]):
        if u <= u1:
            a = (u - u0) / (u1 - u0)
            a = a * a * (3 - 2 * a)            # wygładzenie (smoothstep)
            return v0 + (v1 - v0) * a
    return ctrl[-1][1]


def bump(u, uc, h, s):
    return h * math.exp(-((u - uc) / s) ** 2)


def poly(pts, close=True):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + (' Z' if close else '')


# ---------- linia środkowa żebra (rzut na płaszczyznę poprzeczną), mm kości ----------
CTRL = [(15, 1.5), (23, -3.5), (31, -8.5), (39, -13.5), (47, -18), (55, -21.5), (62, -23.4), (69, -23.6),
        (79, -21.6), (91, -16.2), (103, -7.5), (114, 5), (122.5, 21), (127.5, 40), (128.8, 60), (126.5, 81),
        (120.5, 101), (111, 119), (99.5, 133.5), (88, 144)]
N = 600
C, LEN = resample(bez([T(*p) for p in CTRL], n=24), N)
U = [k / N for k in range(N + 1)]


def tangent(i):
    a, b = C[max(i - 1, 0)], C[min(i + 1, N)]
    d = math.dist(a, b)
    return ((b[0] - a[0]) / d, (b[1] - a[1]) / d)


TAN = [tangent(i) for i in range(N + 1)]
NIN = [(-ty, tx) for tx, ty in TAN]        # normalna ku stronie wklęsłej (wnętrze klatki)

# szerokość widoczna od dołu (mm kości): strona wewnętrzna / zewnętrzna od linii środkowej
W_IN = [(0, 5.6), (0.012, 5.6), (0.04, 3.4), (0.1, 3.4), (0.2, 5.0), (0.32, 4.6), (0.46, 4.3), (0.6, 4.3), (0.72, 4.9),
        (0.84, 6.3), (0.93, 7.6), (1.0, 8.4)]
W_OUT = [(0, 5.6), (0.012, 5.6), (0.04, 3.5), (0.1, 3.6), (0.2, 5.6), (0.32, 4.8), (0.46, 4.3), (0.6, 4.3), (0.72, 4.9),
         (0.84, 6.3), (0.93, 7.6), (1.0, 8.6)]
U_TUB = 0.112                               # guzek żebra – na stronie tylnej (zewnętrznej łuku)


def w_in(u):
    return lerp(W_IN, u) * S


def w_out(u):
    return (lerp(W_OUT, u) + bump(u, U_TUB, 4.6, 0.02) + bump(u, 0.205, 0.8, 0.03)) * S


def edge(i, side, extra=0.0):
    c, n = C[i], NIN[i]
    w = (w_in(U[i]) if side > 0 else w_out(U[i])) + extra
    return (c[0] + side * n[0] * w, c[1] + side * n[1] * w)


def ipt(u):
    return min(int(round(u * N)), N)


inner = [edge(i, +1) for i in range(N + 1)]
outer = [edge(i, -1) for i in range(N + 1)]

# zaokrąglony koniec tylny (głowa) i lekko wypukły koniec przedni
i0 = 0
c0, t0 = C[0], TAN[0]
r0 = (w_in(0) + w_out(0)) / 2
cap_head = []
for k in range(1, 24):
    a = math.pi * k / 24
    # półkole od krawędzi zewnętrznej przez czubek (kierunek –t0) do wewnętrznej
    nx, ny = NIN[0]
    v = (-nx * math.cos(a) - t0[0] * math.sin(a), -ny * math.cos(a) - t0[1] * math.sin(a))
    cap_head.append((c0[0] + v[0] * r0 * 1.0, c0[1] + v[1] * r0 * 1.0))
cE, tE = C[N], TAN[N]
rE = (w_in(1) + w_out(1)) / 2
cap_end = []
for k in range(1, 18):
    a = math.pi * k / 18
    nx, ny = NIN[N]
    v = (nx * math.cos(a) + tE[0] * math.sin(a) * 0.32, ny * math.cos(a) + tE[1] * math.sin(a) * 0.32)
    cap_end.append((cE[0] + v[0] * rE, cE[1] + v[1] * rE))

outline = outer + cap_end + inner[::-1] + cap_head
f.add(f'<path class="bone" d="{poly(outline)}"/>')

# ---------- bruzda żebra: pas po stronie wklęsłej (przy dolnym brzegu powierzchni wewnętrznej) ----------
G = [(0.115, 0.0), (0.15, 2.3), (0.3, 2.5), (0.5, 1.9), (0.66, 1.0), (0.78, 0.0)]
ia, ib = ipt(0.115), ipt(0.78)
g_in = [edge(i, +1, -0.18) for i in range(ia, ib + 1)]
g_lip = []
for i in range(ia, ib + 1):
    c, n = C[i], NIN[i]
    w = w_in(U[i]) - lerp(G, U[i]) * S - 0.18
    g_lip.append((c[0] + n[0] * w, c[1] + n[1] * w))
f.add(f'<path class="shade" d="{poly(g_in + g_lip[::-1])}"/>')
f.add(f'<path class="bonel" d="{poly(g_lip, close=False)}"/>')

# ---------- koniec przedni: chropowata, wgłębiona powierzchnia do połączenia z chrząstką ----------
ang = math.degrees(math.atan2(NIN[N][1], NIN[N][0]))
ex, ey = cE[0] + tE[0] * 0.25, cE[1] + tE[1] * 0.25
f.add(f'<ellipse class="bone2" cx="{ex:.2f}" cy="{ey:.2f}" rx="{rE * 0.93:.2f}" ry="{rE * 0.27:.2f}" '
      f'transform="rotate({ang:.1f} {ex:.2f} {ey:.2f})"/>')
f.add(f'<ellipse class="bonel" cx="{ex:.2f}" cy="{ey:.2f}" rx="{rE * 0.62:.2f}" ry="{rE * 0.13:.2f}" '
      f'transform="rotate({ang:.1f} {ex:.2f} {ey:.2f})"/>')

# ---------- głowa: powierzchnia stawowa na czubku (od dołu widać jej dolną część) ----------
arc = [cap_head[k] for k in range(2, 22)]
m = len(arc)
crescent_in = []
for k, (x, y) in enumerate(arc):
    a = math.sin(math.pi * k / (m - 1))
    crescent_in.append((x + t0[0] * r0 * 0.62 * a, y + t0[1] * r0 * 0.62 * a))
f.add(f'<path class="facet" d="{poly(arc + crescent_in[::-1])}"/>')
# szyjka – lekko zaznaczona granica głowy
ih = ipt(0.045)
a_, b_ = edge(ih, +1, -0.25), edge(ih, -1, -0.25)
f.add(f'<path class="bonel" d="M{a_[0]:.2f},{a_[1]:.2f} Q{C[ih][0] - TAN[ih][0] * 0.6:.2f},{C[ih][1] - TAN[ih][1] * 0.6:.2f} {b_[0]:.2f},{b_[1]:.2f}"/>')

# ---------- guzek: powierzchnia stawowa guzka (przyśrodkowa część guzka) ----------
ta, tb = ipt(U_TUB - 0.03), ipt(U_TUB + 0.004)
lens_o = [edge(i, -1, -0.12) for i in range(ta, tb + 1)]
mm_ = len(lens_o)
lens_i = []
for k, i in enumerate(range(ta, tb + 1)):
    a = math.sin(math.pi * k / (mm_ - 1)) ** 0.8
    lens_i.append(edge(i, -1, -0.12 - 1.15 * a))
f.add(f'<path class="facet" d="{poly(lens_o + lens_i[::-1])}"/>')

# ---------- kąt żebra: linia kąta na powierzchni zewnętrznej ----------
ik = ipt(0.205)
a_, b_ = edge(ik, -1, -0.15), edge(ik, +1, -0.9)
f.add(f'<path class="bonel" d="M{a_[0]:.2f},{a_[1]:.2f} L{b_[0]:.2f},{b_[1]:.2f}"/>')

# ---------- wstawka: przekrój poprzeczny trzonu (bok w lewo, góra ku górze) ----------
QX, QY, QS = 26.0, 26.5, 1.85
SEC = [(0.0, -6.8), (1.7, -6.3), (2.6, -4.7), (2.9, -2.2), (2.85, 0.3), (2.6, 1.35), (1.55, 2.0), (0.8, 3.0),
       (0.65, 4.6), (1.05, 5.75), (1.25, 6.5), (0.55, 7.25), (-0.6, 6.4), (-1.7, 4.4), (-2.45, 1.9), (-2.8, -1.0),
       (-2.6, -4.0), (-1.7, -6.0)]
secp = [(QX + x * QS, QY + y * QS) for x, y in SEC]
f.add(f'<path class="bone2" d="{smooth(secp)}"/>')
f.text(QX, QY - 6.6 * QS - 7.2, 'przekrój poprzeczny trzonu', cls='notec')
f.text(QX, QY - 6.6 * QS - 1.6, 'brzeg górny', cls='notec')
f.text(QX, QY + 6.8 * QS + 3.4, 'brzeg dolny', cls='notec')
f.text(QX - 3.0 * QS - 1.4, QY - 1.2, 'powierzchnia', cls='note', anchor='end')
f.text(QX - 3.0 * QS - 1.4, QY + 1.6, 'zewnętrzna', cls='note', anchor='end')
f.text(QX + 3.0 * QS + 1.4, QY - 2.6, 'powierzchnia', cls='note')
f.text(QX + 3.0 * QS + 1.4, QY + 0.2, 'wewnętrzna', cls='note')
f.text(QX + 2.3 * QS + 1.4, QY + 4.4 * QS + 0.8, 'bruzda', cls='note')

# ---------- podpisy ----------
TR = 110.0
f.label(edge(ipt(0.0), -1, -1.2), 'głowa żebra', 'caput costae', (TR, 76.0), side='R')
f.label(C[ipt(0.05)], 'szyjka żebra', 'collum costae', (TR, 84.5), side='R')
f.label(outer[ipt(U_TUB)], 'guzek żebra', 'tuberculum costae', (TR, 93.0), side='R')
ig = ipt(0.36)
gpt = edge(ig, +1, -0.55)
f.label(gpt, 'bruzda żebra', 'sulcus costae', (TR, 66.0), side='R')
f.label((ex - tE[0] * 0.1, ey - tE[1] * 0.1), 'koniec przedni', None, (84.0, 6.0), side='R')
f.text(84.7, 9.9, '(powierzchnia do chrząstki)', cls='note')
f.label(C[ipt(0.56)], 'trzon żebra', 'corpus costae', (40.0, 58.0), side='L')
f.label(outer[ipt(0.205)], 'kąt żebra', 'angulus costae', (40.0, 90.0), side='L')

if os.environ.get('PTS'):
    for u in (0, 0.045, 0.08, U_TUB, 0.205, 0.3, 0.45, 0.55, 0.7, 0.85, 1.0):
        i = ipt(u)
        print(f'u={u:.3f}  c=({C[i][0]:.1f},{C[i][1]:.1f})  in=({inner[i][0]:.1f},{inner[i][1]:.1f})  out=({outer[i][0]:.1f},{outer[i][1]:.1f})')
    print('LEN', LEN / S)

f.save()
