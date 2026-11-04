# ŻEBRO PIERWSZE (prawe) – widok od góry, przód ku górze rysunku.
# Widok od góry: prawa strona ciała po prawej stronie rysunku → koniec tylny (głowa, szyjka) i koniec przedni
# leżą przyśrodkowo (po lewej), żebro wygina się łukiem bocznie (w prawo). Brzeg wewnętrzny – wklęsły, cienki;
# brzeg zewnętrzny – wypukły, gruby (zaokrąglony – delikatny cień). Pola przyczepów mięśni – klasa muscle.
# Rysunek własny, schematyczny; nazwy wg karty „Żebro I” (Bochenek, t. I, s. 276–277, ryc. 185).
import sys, os; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
import math
from figlib import Fig, smooth

W, H = 150, 94
S = 0.8                     # mm rysunku / mm kości
X0, Y0 = 45.6, 58.5         # rysunek ← kość: X w bok (w prawo), Y do przodu (w górę)
f = Fig('zebro_I', W, H, caption='prawe żebro I (kość żebrowa) · widok od góry (przód ku górze)')


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


# ---------- linia środkowa żebra (mm kości; początek: środek trzonu Th1) ----------
CTRL = [(13, -1), (20, -5), (28, -9), (35, -10.5), (42, -9), (48, -5), (53, 1), (57, 9), (59, 18), (58.5, 27),
        (56, 35), (51.5, 42), (45.5, 48), (38.5, 52.5), (32, 55)]
N = 600
C, LEN = resample(bez([T(*p) for p in CTRL], n=24), N)
U = [k / N for k in range(N + 1)]


def tangent(i):
    a, b = C[max(i - 1, 0)], C[min(i + 1, N)]
    d = math.dist(a, b)
    return ((b[0] - a[0]) / d, (b[1] - a[1]) / d)


TAN = [tangent(i) for i in range(N + 1)]
NIN = [(ty, -tx) for tx, ty in TAN]          # normalna ku stronie wklęsłej (brzeg wewnętrzny)

U_TUB = 0.17          # guzek żebra – na brzegu zewnętrznym (tylnym)
U_SCA = 0.60          # guzek m. pochyłego przedniego – na brzegu wewnętrznym
W_IN = [(0, 5.0), (0.03, 4.4), (0.07, 3.3), (0.13, 3.3), (0.2, 4.5), (0.3, 5.5), (0.42, 6.5), (0.55, 7.3),
        (0.7, 8.1), (0.85, 8.9), (1.0, 9.6)]
W_OUT = [(0, 5.0), (0.03, 4.4), (0.07, 3.3), (0.13, 3.5), (0.2, 4.8), (0.3, 5.8), (0.42, 6.8), (0.55, 7.6),
         (0.7, 8.4), (0.85, 9.2), (1.0, 10.0)]


def w_in(u):
    return (lerp(W_IN, u) + bump(u, U_SCA, 2.1, 0.02)) * S


def w_out(u):
    return (lerp(W_OUT, u) + bump(u, U_TUB, 3.0, 0.028)) * S


def at(u):
    """punkt linii środkowej, styczna i normalna dla dowolnego u (interpolacja)"""
    x = min(max(u, 0.0), 1.0) * N
    i = min(int(x), N - 1)
    a = x - i
    c = (C[i][0] + (C[i + 1][0] - C[i][0]) * a, C[i][1] + (C[i + 1][1] - C[i][1]) * a)
    n = (NIN[i][0] + (NIN[i + 1][0] - NIN[i][0]) * a, NIN[i][1] + (NIN[i + 1][1] - NIN[i][1]) * a)
    return c, n


def UV(u, v, extra=0.0):
    """u – wzdłuż żebra (0 głowa … 1 koniec przedni); v – w poprzek (+1 brzeg wewnętrzny, −1 brzeg zewnętrzny)"""
    c, n = at(u)
    w = (w_in(u) if v >= 0 else w_out(u)) * abs(v) + extra
    s = 1 if v >= 0 else -1
    return (c[0] + s * n[0] * w, c[1] + s * n[1] * w)


def edge(i, side, extra=0.0):
    c, n = C[i], NIN[i]
    w = (w_in(U[i]) if side > 0 else w_out(U[i])) + extra
    return (c[0] + side * n[0] * w, c[1] + side * n[1] * w)


def ipt(u):
    return min(int(round(u * N)), N)


def field(u0, du, v0, dv, n=48, rot=0.0):
    """owalne pole na powierzchni żebra (współrzędne u, v)"""
    pts = []
    for k in range(n):
        a = 2 * math.pi * k / n
        uu, vv = du * math.cos(a), dv * math.sin(a)
        pts.append(UV(u0 + uu * math.cos(rot) - vv * math.sin(rot) * du / dv * 0,
                      v0 + vv))
    return pts


inner = [edge(i, +1) for i in range(N + 1)]
outer = [edge(i, -1) for i in range(N + 1)]

# zaokrąglona głowa
c0, t0 = C[0], TAN[0]
r0 = (w_in(0) + w_out(0)) / 2
cap_head = []
for k in range(1, 24):
    a = math.pi * k / 24
    nx, ny = NIN[0]
    v = (-nx * math.cos(a) - t0[0] * math.sin(a), -ny * math.cos(a) - t0[1] * math.sin(a))
    cap_head.append((c0[0] + v[0] * r0, c0[1] + v[1] * r0))
# szeroki, lekko wypukły koniec przedni
cE, tE = C[N], TAN[N]
rE = (w_in(1) + w_out(1)) / 2
cap_end = []
for k in range(1, 18):
    a = math.pi * k / 18
    nx, ny = NIN[N]
    v = (-nx * math.cos(a) + tE[0] * math.sin(a) * 0.30, -ny * math.cos(a) + tE[1] * math.sin(a) * 0.30)
    cap_end.append((cE[0] + v[0] * rE, cE[1] + v[1] * rE))
# cap_end biegnie od brzegu zewnętrznego do wewnętrznego
outline = outer + cap_end + inner[::-1] + cap_head[::-1]
f.add(f'<path class="bone" d="{poly(outline)}"/>')

# ---------- brzeg zewnętrzny gruby, zaokrąglony – pas cienia wzdłuż brzegu ----------
ia, ib = ipt(0.22), ipt(0.985)
sh_o = [edge(i, -1, -0.12) for i in range(ia, ib + 1)]
sh_i = []
for k, i in enumerate(range(ia, ib + 1)):
    u = U[i]
    taper = min(1.0, (u - 0.22) / 0.06, (0.985 - u) / 0.05)
    sh_i.append(edge(i, -1, -0.12 - 1.5 * S * taper))
f.add(f'<path class="shade" d="{poly(sh_o + sh_i[::-1])}"/>')

# ---------- bruzdy na powierzchni górnej (przebiegają w poprzek żebra) ----------
def groove(uc, du, k, deep):
    vs = [-0.97 + 1.94 * j / 20 for j in range(21)]
    a = [UV(uc - du + k * v, v) for v in vs]
    b = [UV(uc + du + k * v, v) for v in vs]
    for _ in range(deep):
        f.add(f'<path class="shade" d="{poly(a + b[::-1])}"/>')
    f.add(f'<path class="bonel" d="{poly(a, close=False)}"/>')
    f.add(f'<path class="bonel" d="{poly(b, close=False)}"/>')


U_ART, U_VEN = 0.515, 0.688
groove(U_ART, 0.024, 0.006, 2)          # bruzda tętnicy podobojczykowej – nieco głębsza
groove(U_VEN, 0.019, -0.004, 1)         # bruzda żyły podobojczykowej – płytka

# ---------- pola przyczepów mięśni ----------
F_MED = field(0.372, 0.062, 0.12, 0.52)        # m. pochyły środkowy – chropowate pole za bruzdą tętnicy
F_SER = field(0.452, 0.050, -0.80, 0.15)       # m. zębaty przedni (1. ząb) – tylna część brzegu zewnętrznego
F_SCA = field(U_SCA, 0.026, 0.70, 0.27)        # m. pochyły przedni – na guzku m. pochyłego przedniego
F_SUB = field(0.918, 0.052, -0.02, 0.50)       # m. podobojczykowy – koniec przedni
for fp in (F_MED, F_SER, F_SCA, F_SUB):
    f.add(f'<path class="muscle" d="{poly(fp)}"/>')

# ---------- koniec przedni: powierzchnia do połączenia z chrząstką żebrową ----------
ang = math.degrees(math.atan2(NIN[N][1], NIN[N][0]))
ex, ey = cE[0] + tE[0] * 0.15, cE[1] + tE[1] * 0.15
f.add(f'<ellipse class="bone2" cx="{ex:.2f}" cy="{ey:.2f}" rx="{rE * 0.92:.2f}" ry="{rE * 0.22:.2f}" '
      f'transform="rotate({ang:.1f} {ex:.2f} {ey:.2f})"/>')

# ---------- głowa: niepodzielona powierzchnia stawowa (na końcu przyśrodkowym) ----------
arc = [cap_head[k] for k in range(3, 21)]
m = len(arc)
cres = []
for k, (x, y) in enumerate(arc):
    a = math.sin(math.pi * k / (m - 1))
    cres.append((x + t0[0] * r0 * 0.55 * a, y + t0[1] * r0 * 0.55 * a))
f.add(f'<path class="facet" d="{poly(arc + cres[::-1])}"/>')
# granica głowy i szyjki
ih = ipt(0.045)
a_, b_ = edge(ih, +1, -0.2), edge(ih, -1, -0.2)
f.add(f'<path class="bonel" d="M{a_[0]:.2f},{a_[1]:.2f} Q{C[ih][0] - TAN[ih][0] * 0.5:.2f},{C[ih][1] - TAN[ih][1] * 0.5:.2f} {b_[0]:.2f},{b_[1]:.2f}"/>')

# ---------- guzek żebra: powierzchnia stawowa guzka (widoczna z góry tylko jako wąski rąbek) ----------
ta, tb = ipt(U_TUB - 0.03), ipt(U_TUB + 0.012)
lens_o = [edge(i, -1, -0.1) for i in range(ta, tb + 1)]
mm_ = len(lens_o)
lens_i = [edge(i, -1, -0.1 - 0.9 * math.sin(math.pi * k / (mm_ - 1)) ** 0.8) for k, i in enumerate(range(ta, tb + 1))]
f.add(f'<path class="facet" d="{poly(lens_o + lens_i[::-1])}"/>')

# ---------- podpisy ----------
TL, TR = 47.6, 103.6


def cen(pts):
    return (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))


P_SUB = cen(F_SUB)
P_INB = UV(0.80, 1.0, -0.15)
P_STB = UV(U_SCA, 1.0, -0.25)
P_SCA = cen(F_SCA)
P_MED = cen(F_MED)
P_NECK = C[ipt(0.095)]
P_HEAD = UV(0.0, 0.0)
P_HEAD = (P_HEAD[0] - TAN[0][0] * r0 * 0.35, P_HEAD[1] - TAN[0][1] * r0 * 0.35)
P_OUTB = UV(0.76, -1.0, 0.15)
P_VEN = UV(U_VEN, -0.45)
P_ART = UV(U_ART, -0.42)
P_SER = cen(F_SER)
P_TUB = UV(U_TUB, -1.0, -0.6)

YS = dict(sub=12.0, inb=21.5, stb=39.5, sca=31.0, med=48.0, neck=72.0, head=63.0,
          outb=17.0, ven=26.0, art=35.0, ser=44.0, tub=70.0)
f.label(P_SUB, 'przyczep m. podobojczykowego', 'm. subclavius', (TL, YS['sub']), side='L')
f.label(P_INB, 'brzeg wewnętrzny', None, (TL, YS['inb']), side='L')
f.label(P_STB, 'guzek m. pochyłego przedniego', 'tuberculum m. scaleni anterioris', (TL, YS['stb']), side='L')
f.label(P_SCA, 'przyczep m. pochyłego przedniego', 'm. scalenus anterior', (TL, YS['sca']), side='L')
f.label(P_MED, 'przyczep m. pochyłego środkowego', 'm. scalenus medius', (TL, YS['med']), side='L')
f.label(P_NECK, 'szyjka żebra', 'collum costae', (TL, YS['neck']), side='L')
f.label(P_HEAD, 'głowa żebra', 'caput costae', (TL, YS['head']), side='L')
f.label(P_OUTB, 'brzeg zewnętrzny', None, (TR, YS['outb']), side='R')
f.label(P_VEN, 'bruzda żyły podobojczykowej', 'sulcus venae subclaviae', (TR, YS['ven']), side='R')
f.label(P_ART, 'bruzda tętnicy podobojczykowej', 'sulcus arteriae subclaviae', (TR, YS['art']), side='R')
f.label(P_SER, 'przyczep m. zębatego przedniego', 'm. serratus anterior', (TR, YS['ser']), side='R')
f.label(P_TUB, 'guzek żebra', 'tuberculum costae', (TR, YS['tub']), side='R')

if os.environ.get('PTS'):
    for nm, p in [('sub', P_SUB), ('inb', P_INB), ('stb', P_STB), ('sca', P_SCA), ('med', P_MED), ('neck', P_NECK),
                  ('head', P_HEAD), ('outb', P_OUTB), ('ven', P_VEN), ('art', P_ART), ('ser', P_SER), ('tub', P_TUB)]:
        print(f'{nm:5s} ({p[0]:.1f}, {p[1]:.1f})')
    xs = [p[0] for p in outline]; ys = [p[1] for p in outline]
    print('bbox', min(xs), max(xs), min(ys), max(ys), 'LEN', LEN / S)

f.save()
