# TRZY KRZYWIZNY ŻEBRA (prawe żebro VII, kość żebrowa) – schemat, wg Bochenka, t. I, s. 275:
#   1. krzywizna płaszczyzny – łuk wypukły bocznie; promień z tyłu mniejszy, bocznie i z przodu większy,
#   2. krzywizna obrotu – skręcenie wzdłuż żebra: gdy części tylne i środkowe stoją pionowo,
#      części przednie zwracają powierzchnię zewnętrzną ku górze,
#   3. krzywizna brzegu – lekkie esowate skręcenie względem płaszczyzny poziomej; żebro ułożone na płaszczyźnie:
#      patrząc z boku, część tylna unosi się nad powierzchnię podpory.
# Jeden model przestrzenny żebra (linia środkowa jak w zebro_typowe.py, przekroje spłaszczone, skręcenie części
# przedniej, uniesienie części tylnej) rzutowany na trzy sposoby: od góry (panel 1), od tyłu i z boku (panel 2),
# od tyłu (panel 3). Krzywizny nieco wyolbrzymione dla czytelności.
import sys, os, math
sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 150, 105
f = Fig('zebro_krzywizny', W, H, caption='trzy krzywizny żebra · prawe żebro VII (kość żebrowa) · schemat')


# ======================================================================= narzędzia
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


def sstep(a):
    a = min(max(a, 0.0), 1.0)
    return a * a * (3 - 2 * a)


def lerp(ctrl, u):
    if u <= ctrl[0][0]:
        return ctrl[0][1]
    for (u0, v0), (u1, v1) in zip(ctrl, ctrl[1:]):
        if u <= u1:
            return v0 + (v1 - v0) * sstep((u - u0) / (u1 - u0))
    return ctrl[-1][1]


def poly(pts, close=True):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + (' Z' if close else '')


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def circ3(a, b, c):
    ax, ay = a; bx, by = b; cx, cy = c
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
    return (ux, uy), math.dist((ux, uy), a)


# ======================================================================= model żebra (mm kości)
# X – w bok od linii pośrodkowej, Y – do przodu, Z – do góry. Linia środkowa jak w zebro_typowe.py (żebro VII).
CTRL = [(15, 1.5), (23, -3.5), (31, -8.5), (39, -13.5), (47, -18), (55, -21.5), (62, -23.4), (69, -23.6),
        (79, -21.6), (91, -16.2), (103, -7.5), (114, 5), (122.5, 21), (127.5, 40), (128.8, 60), (126.5, 81),
        (120.5, 101), (111, 119), (99.5, 133.5), (88, 144)]
N = 300
C2, LEN = resample(bez(CTRL, n=24), N)
U = [k / N for k in range(N + 1)]


def tan2(i):
    a, b = C2[max(i - 1, 0)], C2[min(i + 1, N)]
    d = math.dist(a, b)
    return ((b[0] - a[0]) / d, (b[1] - a[1]) / d)


T2 = [tan2(i) for i in range(N + 1)]
NOUT = [(ty, -tx) for tx, ty in T2]          # normalna pozioma ku stronie wypukłej (powierzchnia zewnętrzna)

U_TUB, U_ANG = 0.112, 0.205                  # guzek, kąt żebra
H_T = [(0, 10.5), (0.02, 10.5), (0.06, 8.0), (0.09, 8.2), (0.14, 10.5), (0.2, 12.0), (0.35, 13.0), (0.6, 13.5),
       (0.8, 14.5), (0.93, 15.5), (1.0, 16.5)]                       # wysokość przekroju (brzeg górny – dolny)
T_T = [(0, 10.0), (0.025, 10.0), (0.05, 7.0), (0.09, 7.2), (0.15, 8.6), (0.25, 8.2), (0.5, 7.8), (0.8, 7.8),
       (1.0, 8.4)]                                                   # grubość (pow. zewnętrzna – wewnętrzna)
TH_MAX = 70.0                                                        # krzywizna obrotu: skręcenie części przedniej
Z_MAX = 12.0                                                         # krzywizna brzegu: uniesienie części tylnej


def theta(u):
    return math.radians(TH_MAX * sstep((u - 0.55) / 0.45))


def zlow(u):
    return Z_MAX * sstep((0.42 - u) / 0.30)


NA = 48
ANG = [2 * math.pi * k / NA for k in range(NA)]


def sec2d(u, k=1.0):
    """przekrój w układzie lokalnym (a – ku powierzchni zewnętrznej, b – ku brzegowi górnemu)"""
    h, t = lerp(H_T, u) * k, lerp(T_T, u) * k
    tub = 4.2 * math.exp(-((u - U_TUB) / 0.022) ** 2) * k
    out = []
    for al in ANG:
        c, s = math.cos(al), math.sin(al)
        a = t / 2 * math.copysign(abs(c) ** 0.8, c)
        b = h / 2 * math.copysign(abs(s) ** 0.8, s)
        a *= 1 + 0.2 * b / (h / 2)                       # brzeg górny grubszy, dolny cieńszy
        if c > 0:                                        # guzek: ku tyłowi (strona zewnętrzna) i ku dołowi
            a += tub * c * c * math.exp(-((b / (h / 2) + 0.3) / 0.6) ** 2)
        out.append((a, b))
    return out


def frame(i, u):
    th = theta(u)
    n0 = (NOUT[i][0], NOUT[i][1], 0.0)
    Nv = (math.cos(th) * n0[0], math.cos(th) * n0[1], math.sin(th))
    Hv = (-math.sin(th) * n0[0], -math.sin(th) * n0[1], math.cos(th))
    return Nv, Hv


def section3d(i, u=None, base=None, k=1.0, dz=None):
    u = U[i] if u is None else u
    cx, cy = C2[i] if base is None else base
    Nv, Hv = frame(i, u)
    pts = [(cx + a * Nv[0] + b * Hv[0], cy + a * Nv[1] + b * Hv[1], a * Nv[2] + b * Hv[2]) for a, b in sec2d(u, k)]
    if dz is None:
        dz = zlow(u) - min(p[2] for p in pts)
    return [(x, y, z + dz) for x, y, z in pts], dz


SECS, CEN, DZ = [], [], []
for i in range(N + 1):
    s, dz = section3d(i)
    SECS.append(s)
    DZ.append(dz)
    CEN.append((C2[i][0], C2[i][1], dz))
# zaokrąglenie głowy (czapeczka za końcem tylnym)
RCAP = 5.0
CAP, CAPC = [], []
for k in range(1, 9):
    sd = RCAP * k / 8
    kk = max(math.sqrt(max(1 - (sd / RCAP) ** 2, 0)), 0.12)
    bx, by = C2[0][0] - T2[0][0] * sd * 0.9, C2[0][1] - T2[0][1] * sd * 0.9
    s, _ = section3d(0, 0.0, (bx, by), kk, DZ[0] + lerp(H_T, 0) / 2 * (1 - kk))
    CAP.append(s)
    CAPC.append((bx, by, DZ[0] + lerp(H_T, 0) / 2))


# ======================================================================= rzutowanie i obrys
class View:
    def __init__(self, phi, elev, s, ox, oy, top=False):
        if top:                                   # od góry, przód ku górze rysunku, bok w prawo
            self.R, self.Uv, self.D = (1, 0, 0), (0, 1, 0), (0, 0, 1)
        else:                                     # od tyłu (phi=0) obrócony o phi ku bokowi; elev – z góry
            p, e = math.radians(phi), math.radians(elev)
            self.R = (math.cos(p), math.sin(p), 0.0)
            self.D = (math.sin(p) * math.cos(e), -math.cos(p) * math.cos(e), math.sin(e))
            d, r = self.D, self.R
            self.Uv = (d[1] * r[2] - d[2] * r[1], d[2] * r[0] - d[0] * r[2], d[0] * r[1] - d[1] * r[0])
        self.s, self.ox, self.oy = s, ox, oy

    def p(self, P):
        return (self.ox + self.s * dot(P, self.R), self.oy - self.s * dot(P, self.Uv))

    def depth(self, P):
        return dot(P, self.D)


def smooth_chain(ch, w=3):
    """wygładzenie łańcucha punktów skrajnych (średnia ruchoma; końce bez zmian)"""
    n = len(ch)
    out = []
    for k in range(n):
        m = min(w, k, n - 1 - k)
        seg = ch[k - m:k + m + 1]
        out.append((sum(p[0] for p in seg) / len(seg), sum(p[1] for p in seg) / len(seg)))
    return out


def outline(view, secs, cens):
    """obrys bryły zakreślonej przez kolejne przekroje (lewy i prawy brzeg + łuki na końcach)"""
    P = [[view.p(q) for q in s] for s in secs]
    Cc = [view.p(c) for c in cens]
    n = len(P)
    L, R, tl = [], [], []
    for k in range(n):
        a, b = Cc[max(k - 1, 0)], Cc[min(k + 1, n - 1)]
        tx, ty = b[0] - a[0], b[1] - a[1]
        d = math.hypot(tx, ty) or 1e-9
        tx, ty = tx / d, ty / d
        tl.append((tx, ty))
        nx, ny = -ty, tx
        vals = [q[0] * nx + q[1] * ny for q in P[k]]
        L.append(vals.index(max(vals)))
        R.append(vals.index(min(vals)))

    def arc(k, i0, i1, forward):
        pts, m = P[k], len(P[k])
        A = [pts[(i0 + j) % m] for j in range((i1 - i0) % m + 1)]
        B = [pts[(i0 - j) % m] for j in range((i0 - i1) % m + 1)]
        c, (tx, ty) = Cc[k], tl[k]
        sc = lambda Z: sum((x - c[0]) * tx + (y - c[1]) * ty for x, y in Z) / len(Z)
        return (A if sc(A) > sc(B) else B) if forward else (A if sc(A) < sc(B) else B)

    left = smooth_chain([P[k][L[k]] for k in range(n)])
    right = smooth_chain([P[k][R[k]] for k in range(n)])
    return left + arc(n - 1, L[-1], R[-1], True)[1:-1] + right[::-1] + arc(0, R[0], L[0], False)[1:-1]


def chunks(view, i0, i1):
    """podział na odcinki tam, gdzie żebro w rzucie zawraca (biegnie wprost od patrzącego / do niego)"""
    Cc = [view.p(CEN[i]) for i in range(N + 1)]

    def ratio(i):
        a, b = max(i - 1, 0), min(i + 1, N)
        d3 = math.dist(CEN[a], CEN[b])
        return math.dist(Cc[a], Cc[b]) / (view.s * d3)

    def tdir(i):
        a, b = max(i - 1, 0), min(i + 1, N)
        return (Cc[b][0] - Cc[a][0], Cc[b][1] - Cc[a][1])

    cuts = [i0]
    for i in range(i0 + 6, i1 - 5):
        r = ratio(i)
        if r < 0.35 and r <= ratio(i - 1) and r <= ratio(i + 1):
            t0, t1 = tdir(i - 6), tdir(i + 6)
            cosang = (t0[0] * t1[0] + t0[1] * t1[1]) / (math.hypot(*t0) * math.hypot(*t1) + 1e-9)
            if cosang < -0.2 and i - cuts[-1] > 6:
                cuts.append(i)
    cuts.append(i1)
    return list(zip(cuts, cuts[1:]))


def draw_rib(view, cap=True, endface=True, extra=None):
    """rysuje żebro w danym rzucie (malarsko: dalsze odcinki najpierw); extra(i0, i1) → dodatkowe elementy odcinka"""
    items = []
    for a, b in chunks(view, 0, N):
        secs, cens = SECS[a:b + 1], CEN[a:b + 1]
        if a == 0 and cap:
            secs, cens = CAP[::-1] + secs, CAPC[::-1] + cens
        el = [f'<path class="bone" d="{poly(outline(view, secs, cens))}"/>']
        if a == 0 and cap:                         # powierzchnia stawowa głowy żebra (koniec przyśrodkowy głowy)
            el.append(f'<path class="facet" d="{poly(outline(view, CAP[3:][::-1], CAPC[3:][::-1]))}"/>')
        if b == N and endface and dot((T2[N][0], T2[N][1], 0), view.D) > 0.05:
            el.append(f'<path class="bone2" d="{poly([view.p(q) for q in SECS[N]])}"/>')
        if extra:
            el += extra(view, a, b)
        dep = sum(view.depth(CEN[i]) for i in range(a, b + 1)) / (b - a + 1)
        items.append((dep, el))
    for _, el in sorted(items, key=lambda t: t[0]):
        for e in el:
            f.add(e)


def surf(i, a_frac, b_frac):
    """punkt na powierzchni przekroju i: a_frac, b_frac ∈ [-1, 1] (część grubości / wysokości)"""
    u = U[i]
    Nv, Hv = frame(i, u)
    h, t = lerp(H_T, u), lerp(T_T, u)
    a, b = a_frac * t / 2, b_frac * h / 2
    c = CEN[i]
    return (c[0] + a * Nv[0] + b * Hv[0], c[1] + a * Nv[1] + b * Hv[1], c[2] + a * Nv[2] + b * Hv[2])


def ipt(u):
    return min(int(round(u * N)), N)


def cen_mid(i):
    """środek przekroju i (punkt na osi bryły)"""
    s = SECS[i]
    return (sum(p[0] for p in s) / len(s), sum(p[1] for p in s) / len(s), sum(p[2] for p in s) / len(s))


# ======================================================================= PANEL 1 – krzywizna płaszczyzny (od góry)
S1 = 0.37
V1 = View(0, 0, S1, 23.5, 69.5, top=True)
f.text(3.0, 5.6, '1. krzywizna płaszczyzny', cls='big')
f.text(3.0, 9.2, 'łuk wypukły bocznie · widok od góry (przód ku górze)', cls='note')
draw_rib(V1, endface=False)

# okręgi krzywizny (dopasowane do linii środkowej): z tyłu mniejszy, bocznie i z przodu większy
c1, r1 = circ3(C2[ipt(0.15)], C2[ipt(0.23)], C2[ipt(0.31)])
c2, r2 = circ3(C2[ipt(0.5)], C2[ipt(0.72)], C2[ipt(0.94)])


def circle_pts(c, r, a0, a1, n=90):
    a0, a1 = math.radians(a0), math.radians(a1)
    return [V1.p((c[0] + r * math.cos(a0 + (a1 - a0) * k / n), c[1] + r * math.sin(a0 + (a1 - a0) * k / n), 0))
            for k in range(n + 1)]


f.add(f'<path class="dim" d="{poly(circle_pts(c1, r1, 0, 360), True)}"/>')
f.add(f'<path class="dim" d="{poly(circle_pts(c2, r2, -50, 64), False)}"/>')
uR1, uR2 = 0.235, 0.75
P1c, P1e = V1.p((c1[0], c1[1], 0)), V1.p((C2[ipt(uR1)][0], C2[ipt(uR1)][1], 0))
P2c, P2e = V1.p((c2[0], c2[1], 0)), V1.p((C2[ipt(uR2)][0], C2[ipt(uR2)][1], 0))
for (cx, cy), (ex, ey) in ((P1c, P1e), (P2c, P2e)):
    f.add(f'<path class="dim" style="stroke-dasharray:none;stroke-width:.3" d="M{cx:.2f},{cy:.2f} L{ex:.2f},{ey:.2f}"/>')
    f.add(f'<path class="dim" style="stroke-dasharray:none;stroke-width:.3" d="M{cx - 1:.2f},{cy:.2f} L{cx + 1:.2f},{cy:.2f} '
          f'M{cx:.2f},{cy - 1:.2f} L{cx:.2f},{cy + 1:.2f}"/>')

# podpisy panelu 1
TL1 = 21.5
f.label(V1.p(cen_mid(ipt(0.012))), 'głowa żebra', 'caput costae', (TL1, 59.5), side='L')
f.label(V1.p(cen_mid(ipt(0.07))), 'szyjka żebra', 'collum costae', (TL1, 68.5), side='L')
f.label(V1.p(surf(ipt(U_TUB), 1.25, -0.3)), 'guzek żebra', 'tuberculum costae', (TL1, 77.5), side='L')
f.label(V1.p(surf(ipt(U_ANG), 1.0, 0)), 'kąt żebra', 'angulus costae', (40.0, 91.0), side='L')
f.label(V1.p(cen_mid(ipt(0.995))), 'koniec przedni', None, (38.0, 15.0), side='L')
mx, my = P1c[0] + (P1e[0] - P1c[0]) * 0.55, P1c[1] + (P1e[1] - P1c[1]) * 0.55
f.label((mx, my), 'promień mniejszy', None, (53.0, 88.0), side='R')
f.text(53.7, 91.6, 'z tyłu', cls='note')
mx, my = P2c[0] + (P2e[0] - P2c[0]) * 0.6, P2c[1] + (P2e[1] - P2c[1]) * 0.6
f.label((mx, my), 'promień większy', None, (52.5, 34.5), side='L')
f.text(51.8, 38.1, 'bocznie i z przodu', cls='note', anchor='end')

# ======================================================================= PANEL 2 – krzywizna obrotu
X2 = 77.0
f.text(X2, 5.6, '2. krzywizna obrotu', cls='big')
f.text(X2, 9.2, 'skręcenie wzdłuż żebra · widok od tyłu i z boku', cls='note')
V2 = View(50, 14, 0.385, 78.0, 19.0)              # od tyłu i z boku (50°), nieco z góry (14°)


def upper_edge(view, a, b):
    """linia brzegu górnego (granica z powierzchnią zewnętrzną) – tylko tam, gdzie widoczna"""
    out, cur = [], []
    for i in range(max(a, ipt(0.08)), min(b, N - 1) + 1):
        Nv, Hv = frame(i, U[i])
        nrm = [0.55 * Nv[j] + 0.83 * Hv[j] for j in range(3)]
        if dot(nrm, view.D) > 0.05:
            cur.append(view.p(surf(i, 0.62, 0.86)))
        elif cur:
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    return [f'<path class="bonel" d="{poly(c, False)}"/>' for c in out if len(c) > 2]


draw_rib(V2, extra=upper_edge)
SEC_U = [0.28, 0.55, 0.80, 1.0]
SEC_X = [86.0, 102.0, 119.0, 137.0]
SY = 38.0
SEC_T = ['część tylna', 'część środkowa', 'część przednia', 'koniec przedni']
# przekrój trzonu (kształt jak we wstawce zebro_typowe; tu powierzchnia zewnętrzna po prawej)
SEC = [(0.0, -6.8), (1.7, -6.3), (2.6, -4.7), (2.9, -2.2), (2.85, 0.3), (2.6, 1.35), (1.55, 2.0), (0.8, 3.0),
       (0.65, 4.6), (1.05, 5.75), (1.25, 6.5), (0.55, 7.25), (-0.6, 6.4), (-1.7, 4.4), (-2.45, 1.9), (-2.8, -1.0),
       (-2.6, -4.0), (-1.7, -6.0)]
# ten sam przekrój bez bruzdy (bruzda żebra z tyłu najgłębsza, ku przodowi stopniowo zanika – s. 275)
SEC0 = [(0.0, -6.8), (1.7, -6.3), (2.6, -4.7), (2.9, -2.2), (2.85, 0.3), (2.55, 1.4), (2.25, 2.6), (1.95, 3.8),
        (1.6, 4.9), (1.3, 5.9), (1.0, 6.6), (0.55, 7.25), (-0.6, 6.4), (-1.7, 4.4), (-2.45, 1.9), (-2.8, -1.0),
        (-2.6, -4.0), (-1.7, -6.0)]
SULC = [1.0, 0.75, 0.35, 0.0]                      # głębokość bruzdy w kolejnych przekrojach
SECP = []
for u, x, t1, g in zip(SEC_U, SEC_X, SEC_T, SULC):
    i = ipt(u)
    th = theta(u)
    k = 0.9 * lerp(H_T, u) / 14.0
    pts = []
    for (sx1, sy1), (sx0, sy0) in zip(SEC, SEC0):
        sx, sy = g * sx1 + (1 - g) * sx0, g * sy1 + (1 - g) * sy0
        a, b = -sx * k, -sy * k                    # a – ku pow. zewnętrznej (w prawo), b – do góry
        ra = a * math.cos(th) - b * math.sin(th)
        rb = a * math.sin(th) + b * math.cos(th)
        pts.append((x + ra, SY - rb))
    SECP.append(pts)
    f.add(f'<path class="bone2" d="{smooth(pts)}"/>')
    # strzałka: kierunek, w który zwrócona jest powierzchnia zewnętrzna
    ax, ay = x + 3.3 * math.cos(th), SY - 3.3 * math.sin(th)
    f.arrow(f'M{ax:.2f},{ay:.2f} L{ax + 4.6 * math.cos(th):.2f},{ay - 4.6 * math.sin(th):.2f}')
    # znacznik miejsca przekroju na żebrze + linia łącząca z nazwą
    q0, q1 = V2.p(surf(i, 0, 1.2)), V2.p(surf(i, 0, -1.2))
    f.add(f'<path class="dim" style="stroke-dasharray:none" d="M{q0[0]:.2f},{q0[1]:.2f} L{q1[0]:.2f},{q1[1]:.2f}"/>')
    lo = max(q0[1], q1[1])
    dx = 4.5 if u > 0.95 else 0.0                  # przy końcu przednim omija strzałkę
    top = min(p[1] for p in pts if p[0] >= x + dx - 2.5) - 1.0
    f.add(f'<path class="dim" d="M{q1[0]:.2f},{lo:.2f} L{x + dx:.2f},{top:.2f}"/>')
    f.text(x, SY + 10.5, t1, cls='notec')
# „pionowo” / „ku górze”
YB = SY + 13.0
for xa_, xb_, t in ((SEC_X[0] - 6, SEC_X[1] + 7.5, 'pionowo'), (SEC_X[2] - 7, SEC_X[3] + 8, 'ku górze')):
    f.add(f'<path class="dim" style="stroke-dasharray:none" d="M{xa_:.2f},{YB - 1:.2f} L{xa_:.2f},{YB:.2f} L{xb_:.2f},{YB:.2f} L{xb_:.2f},{YB - 1:.2f}"/>')
    f.text((xa_ + xb_) / 2, YB + 2.9, 'powierzchnia zewnętrzna', cls='notec')
    f.text((xa_ + xb_) / 2, YB + 5.5, t, cls='notec')
f.label(V2.p(surf(ipt(0.47), 1.0, -0.25)), 'powierzchnia zewnętrzna', None, (99.0, 14.5), side='R')

# ======================================================================= PANEL 3 – krzywizna brzegu
Y3 = 61.2
f.text(X2, Y3, '3. krzywizna brzegu', cls='big')
f.text(X2, Y3 + 3.6, 'lekkie esowate skręcenie względem płaszczyzny poziomej', cls='note')
f.text(X2, Y3 + 6.2, 'żebro położone na płaszczyźnie · widok od tyłu', cls='note')
S3 = 0.50
BASE = 88.0
V3 = View(0, 0, S3, 75.0, BASE)                    # od tyłu, poziomo
xa, xb = 78.0, 148.0
f.add(f'<path class="shade" d="M{xa},{BASE} L{xb},{BASE} L{xb},{BASE + 2.6} L{xa},{BASE + 2.6} Z"/>')
f.add(f'<path class="dim" style="stroke-dasharray:none;stroke-width:.3" d="M{xa},{BASE} L{xb},{BASE}"/>')


def angle_line(view, a, b):
    ia = ipt(U_ANG)
    if a <= ia <= b:
        p0, p1 = view.p(surf(ia + 2, 1.0, 0.85)), view.p(surf(ia - 3, 1.0, -0.85))
        return [f'<path class="bonel" d="M{p0[0]:.2f},{p0[1]:.2f} L{p1[0]:.2f},{p1[1]:.2f}"/>']
    return []


draw_rib(V3, extra=lambda v, a, b: angle_line(v, a, b) + upper_edge(v, a, b))
# uniesienie części tylnej nad podporę
gx = V3.p(surf(ipt(0.05), 0, -1.0))[0]
gy = V3.p(surf(ipt(0.05), 0, -1.0))[1]
f.arrow(f'M{gx:.2f},{BASE - 0.4:.2f} L{gx:.2f},{gy + 1.0:.2f}')
f.text(79.5, BASE + 2.0, 'podpora (płaszczyzna)', cls='note')
f.label(V3.p(surf(ipt(0.012), 0, 0.6)), 'głowa żebra', 'caput costae', (90.0, 71.6), side='R')
f.label(V3.p(surf(ipt(U_ANG), 1.0, 0.75)), 'kąt żebra', 'angulus costae', (118.0, 71.6), side='R')
f.label(V3.p(surf(ipt(0.26), 0, -1.0)), 'część tylna unosi się', None, (110.5, 95.6), side='L')
f.text(109.8, 99.2, 'nad powierzchnię podpory', cls='note', anchor='end')
f.label(V3.p(surf(ipt(0.985), 0, 0.0)), 'koniec przedni', None, (126.0, 95.6), side='R')
f.text(126.7, 99.2, '(w głębi)', cls='note')

if os.environ.get('PTS'):
    print('r1', round(r1, 1), 'c1', [round(v, 1) for v in c1], ' r2', round(r2, 1), 'c2', [round(v, 1) for v in c2])
    for v, nm in ((V1, 'V1'), (V2, 'V2'), (V3, 'V3')):
        xs = [v.p(q)[0] for s in SECS for q in s]
        ys = [v.p(q)[1] for s in SECS for q in s]
        print(nm, 'x', round(min(xs), 1), round(max(xs), 1), 'y', round(min(ys), 1), round(max(ys), 1))
        for u in (0, U_TUB, U_ANG, 0.28, 0.55, 0.8, 0.97, 1.0):
            print('   u', u, [round(c, 1) for c in v.p(cen_mid(ipt(u)))])

f.save()
