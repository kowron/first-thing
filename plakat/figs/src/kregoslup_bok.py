# Kręgosłup w całości – widok z boku (od strony lewej; przód w lewo). Schemat własny.
# Liczby kręgów, podział na odcinki, krzywizny i wzgórek wg Bochenka (s. 219–220, 232–234, 263–265).
# Oś trzonów liczona z kątów nachylenia θ (od pionu; θ>0 = oś biegnie ku dołowi i do tyłu).
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 100, 196
S = 0.236                  # mm rysunku / mm kości
X0, Y0 = 41.0, 4.6         # położenie wierzchołka zęba C2 na rysunku

# ---------------- kręgi (wymiary w mm kości: wysokość przednia, tylna, głębokość trzonu, krążek pod spodem) --------
V = []
def add(name, reg, h, D, disc, hp=None, beta=0.0, L=0.0):
    V.append(dict(name=name, reg=reg, h=h, hp=hp if hp else h, D=D, disc=disc, beta=beta, L=L))
add('C2', 'C2', 24, 15.0, 5)
for i, (D, b) in enumerate([(15.5, 8), (16.0, 8), (16.5, 10), (17.0, 13)]):
    add(f'C{i + 3}', 'C', 14, D, 5, beta=b, L=14 + 2 * i)
add('C7', 'C7', 15, 17.0, 5, beta=18, L=30)
T = [(16, 17.0, 4, 20, 34), (17, 18.5, 4, 28, 36), (17.5, 20.0, 4, 36, 38), (18, 21.5, 4, 44, 39), (18.5, 23.0, 5, 50, 40),
     (19, 24.0, 5, 55, 41), (19.5, 25.5, 5, 58, 41), (20, 26.5, 5.5, 60, 41), (21, 27.5, 5.5, 52, 37), (22, 28.5, 6, 42, 33),
     (23, 29.5, 6, 30, 29), (24, 31.0, 8, 14, 26)]
for i, (h, D, d, b, L) in enumerate(T):
    add(f'Th{i + 1}', 'T', h, D, d, beta=b, L=L)
for i, (h, D, d) in enumerate([(26, 32.5, 10), (27, 33.5, 11), (27, 34.5, 11), (27, 35.0, 12), (28.5, 35.0, 12)]):
    add(f'L{i + 1}', 'L', h, D, d, hp=(24.5 if i == 4 else None))

# kąty osi (θ, stopnie) w punktach kontrolnych: (nazwa kręgu, ułamek wysokości trzonu, θ)
KEYS = [('C2', 0.0, -14), ('C4', 1.2, 0), ('C7', 0.5, 15), ('Th1', 1.0, 19), ('Th7', 0.5, 0), ('Th12', 0.9, -19),
        ('L3', 0.6, 0), ('L5', 0.5, 20)]

# położenie trzonów wzdłuż osi (s – długość łuku od wierzchołka zęba)
s = 15.0                   # ząb C2 ma ok. 15 mm
for v in V:
    v['s0'] = s; v['s1'] = s + v['h']; s = v['s1'] + v['disc']
S_SAC = s                  # początek kości krzyżowej (powierzchnia górna trzonu S1)
byname = {v['name']: v for v in V}
keys_s = [(byname[n]['s0'] + fr * byname[n]['h'], th) for n, fr, th in KEYS]
# kość krzyżowa i guziczna – kąty wzdłuż dalszej osi
SAC_LEN, CO_LEN = 104.0, 34.0
keys_s += [(S_SAC + 2, 47), (S_SAC + 30, 40), (S_SAC + 60, 22), (S_SAC + 85, 4), (S_SAC + SAC_LEN, -12),
           (S_SAC + SAC_LEN + 12, -28), (S_SAC + SAC_LEN + CO_LEN, -48)]

def theta(sv):
    if sv <= keys_s[0][0]: return math.radians(keys_s[0][1])
    for (a, ta), (b, tb) in zip(keys_s, keys_s[1:]):
        if sv <= b:
            t = (sv - a) / (b - a); t = t * t * (3 - 2 * t)        # gładkie przejście
            return math.radians(ta + (tb - ta) * t)
    return math.radians(keys_s[-1][1])

# całkowanie osi (punkty co 0.5 mm)
DS = 0.5
NPTS = int((S_SAC + SAC_LEN + CO_LEN + 10) / DS)
AX = [(0.0, 0.0)]
for k in range(NPTS):
    th = theta(k * DS)
    x, y = AX[-1]
    AX.append((x + math.sin(th) * DS, y + math.cos(th) * DS))
def axis_pt(sv):
    k = max(0, min(len(AX) - 2, int(sv / DS))); t = sv / DS - k
    return (AX[k][0] + (AX[k + 1][0] - AX[k][0]) * t, AX[k][1] + (AX[k + 1][1] - AX[k][1]) * t)
def frame(sv):
    th = theta(sv)
    return axis_pt(sv), (math.sin(th), math.cos(th)), (math.cos(th), -math.sin(th))   # punkt, u (w dół), n (do tyłu)
def G(x, y):                                  # mm kości → rysunek
    return (X0 + x * S, Y0 + y * S)

# lokalne współrzędne kręgu: p – od tylnej powierzchni trzonu do tyłu, q – od górnej powierzchni trzonu w dół
def loc(v, p, q):
    c, u, n = frame((v['s0'] + v['s1']) / 2)
    a = v['D'] / 2 + p; b = q - v['h'] / 2
    return G(c[0] + a * n[0] + b * u[0], c[1] + a * n[1] + b * u[1])
def locA(v, p, q):                            # p liczone od przedniej powierzchni trzonu
    return loc(v, p - v['D'], q)

def rot(pts, beta_loc, ox, oy):               # obrót punktów (p,q) o kąt (stopnie) wokół (ox,oy) w układzie lokalnym
    b = math.radians(beta_loc)
    return [(ox + (p - ox) * math.cos(b) - (q - oy) * math.sin(b), oy + (p - ox) * math.sin(b) + (q - oy) * math.cos(b))
            for p, q in pts]

f = Fig('kregoslup_bok', W, H, caption='kręgosłup · widok z boku (od strony lewej, przód w lewo)')

# ---------------- części tylne kręgów (łuk, wyrostki) ----------------
def post_cerv(v):
    th_loc = math.degrees(theta((v['s0'] + v['s1']) / 2))
    L = v['L']
    sp = [(13.2, 2.6), (16.5, 3.4)]
    tipq = 6.0
    # wyrostek kolczysty – oś pod kątem beta do poziomu → w układzie lokalnym beta+θ
    spine = [(13.0, 3.0), (13.0 + L * 0.55, 4.2), (13.0 + L, 5.4), (13.0 + L + 1.2, 7.0), (13.0 + L + 0.4, 8.6),
             (13.0 + L - 0.6, 9.2), (13.0 + L + 0.6, 10.4), (13.0 + L - 0.6, 11.8), (13.0 + L - 3.0, 11.4),
             (13.0 + L * 0.5, 10.6), (13.0, 11.8)]
    if v['name'] == 'C7':
        spine = [(13.0, 3.0), (13.0 + L * 0.6, 4.6), (13.0 + L - 1.0, 5.6), (13.0 + L + 1.2, 7.4), (13.0 + L + 1.0, 10.2),
                 (13.0 + L - 1.4, 11.2), (13.0 + L * 0.55, 10.4), (13.0, 11.8)]
    spine = rot(spine, v['beta'] + th_loc - 8, 13.0, 7.0)
    pts = ([(-1.0, 1.8), (2.0, 1.8), (4.2, 1.0), (5.0, -1.2), (5.2, -3.0), (7.0, -2.8), (12.2, 0.6)] + spine +
           [(12.8, 15.2), (11.4, 15.8), (6.4, 12.0), (5.0, 10.6), (4.6, 8.6), (3.0, 7.6), (1.4, 8.2), (-1.0, 9.0)])
    return [loc(v, p, q) for p, q in pts]

def post_thor(v, k):
    h = v['h']; th_loc = math.degrees(theta((v['s0'] + v['s1']) / 2))
    L = v['L']; w0, w1 = 4.4, 2.6
    spine = [(12.0, 1.8), (12.0 + L * 0.5, 2.0 + (4.4 - w0) * 0), (12.0 + L, 1.6), (12.0 + L + 1.6, 2.6),
             (12.0 + L + 1.8, 4.6), (12.0 + L + 0.4, 5.8), (12.0 + L * 0.5, 6.4), (12.0, 9.0)]
    if v['name'] in ('Th11', 'Th12'):
        spine = [(12.0, 1.2), (12.0 + L * 0.6, 0.6), (12.0 + L, 0.4), (12.0 + L + 1.4, 2.4), (12.0 + L + 1.4, 7.4),
                 (12.0 + L - 0.2, 9.4), (12.0 + L * 0.55, 9.6), (12.0, 11.0)]
    spine = rot(spine, v['beta'] + th_loc, 12.0, 4.0)
    pts = ([(-1.0, 1.6), (2.6, 1.2), (5.0, 0.2), (5.6, -2.6), (7.4, -4.2), (9.8, -3.8), (11.0, -1.4)] + spine +
           [(12.2, h - 3.0), (12.0, h + 1.6), (10.6, h + 3.4), (8.6, h + 3.0), (7.6, h + 0.6), (7.2, h - 3.0),
            (5.6, h * 0.55), (3.0, h * 0.5), (-1.0, h * 0.55)])
    return [loc(v, p * k, q) for p, q in pts]

def post_lumb(v):
    kq = v['h'] / 27.0; kp = v['D'] / 34.0
    pts = [(-1, 2.1), (2.2, 3.1), (4.4, 3.4), (6.2, 2.4), (7.0, -1.4), (7.8, -5.6), (8.8, -9.4), (10.6, -11.8), (13.0, -12.6),
           (15.2, -11.8), (16.4, -9.4), (16.9, -7.2), (18.9, -6.4), (20.9, -4.4), (21.2, -1.6), (20.0, 0.6), (19.6, 2.6),
           (22.0, 4.6), (28.0, 4.2), (36.0, 3.4), (44.0, 2.8), (49.6, 2.6), (52.6, 4.2), (53.7, 8.0), (53.8, 12.8),
           (53.2, 17.6), (51.4, 21.4), (48.2, 22.6), (42.6, 21.4), (36.4, 19.6), (30.8, 19.0), (27.0, 20.0), (25.0, 23.4),
           (24.2, 28.4), (23.4, 33.0), (22.0, 36.0), (19.8, 37.4), (17.4, 36.8), (15.6, 34.4), (14.6, 30.6), (14.0, 26.6),
           (13.2, 22.8), (11.8, 19.8), (9.4, 17.9), (6.4, 17.3), (3.6, 18.2), (1.6, 20.4), (0.5, 22.8), (-1, 23.5)]
    th_loc = math.degrees(theta((v['s0'] + v['s1']) / 2))
    # wyrostek kolczysty ma pozostać prawie poziomy: obrót części tylnej względem trzonu o -θ (częściowo)
    out = []
    for p, q in pts:
        if p > 19.0:
            (p, q), = rot([(p, q)], th_loc * 0.6, 19.0, 10.0)
        out.append(loc(v, p * kp, q * kq))
    return out

def post_C2(v):
    pts = [(-1.0, -2.0), (2.6, -1.4), (6.0, -0.4), (8.4, 1.6), (10.2, 4.6), (12.6, 6.4), (16.0, 6.8), (22.0, 7.4),
           (27.0, 8.2), (29.2, 9.6), (29.4, 11.6), (28.2, 12.6), (29.0, 14.0), (28.0, 15.8), (25.6, 16.0), (20.0, 14.8),
           (15.6, 14.6), (13.2, 16.2), (12.6, 19.6), (12.0, 22.6), (10.4, 24.4), (8.6, 23.6), (7.6, 20.4), (6.6, 15.2),
           (4.6, 12.0), (2.0, 11.0), (-1.0, 11.6)]
    th_loc = math.degrees(theta((v['s0'] + v['s1']) / 2))
    pts = rot(pts, v['beta'] + th_loc + 4, 8.0, 6.0)
    return [loc(v, p, q) for p, q in pts]

# kolejność: piersiowe i szyjne od dołu (wyrostki kolczyste dachówkowato zachodzą), potem lędźwiowe od góry
order = [v for v in V if v['reg'] in ('C2', 'C', 'C7', 'T')][::-1] + [v for v in V if v['reg'] == 'L']
for v in order:
    if v['reg'] == 'T':
        pts = post_thor(v, 1.0 + 0.012 * (v['D'] - 17))
    elif v['reg'] == 'L':
        pts = post_lumb(v)
    elif v['reg'] == 'C2':
        pts = post_C2(v)
    else:
        pts = post_cerv(v)
    f.add(f'<path class="bone" d="{smooth(pts)}"/>')

# ---------------- kość krzyżowa ----------------
def sac_D(t):    # głębokość części trzonowej (t: 0 u podstawy → 1 przy wierzchołku)
    return 32.0 - 18.0 * t
def sac_P(t):    # grubość części tylnej (kanał krzyżowy, ściana grzbietowa, grzebienie)
    return 24.0 - 17.0 * t ** 0.8
front, back = [], []
NS = 26
for i in range(NS + 1):
    t = i / NS; sv = S_SAC + t * SAC_LEN
    c, u, n = frame(sv)
    D = sac_D(t)
    front.append(G(c[0] - D / 2 * n[0], c[1] - D / 2 * n[1]))
    pb = D / 2 + sac_P(t)
    back.append(G(c[0] + pb * n[0], c[1] + pb * n[1]))
# wyrostek stawowy górny S1 – sterczy ku górze za trzonem
c, u, n = frame(S_SAC)
def sl(p, q):    # lokalnie dla S1: p od tylnej powierzchni trzonu, q od powierzchni górnej
    D = sac_D(0); a = D / 2 + p; b = q
    return G(c[0] + a * n[0] + b * u[0], c[1] + a * n[1] + b * u[1])
sap = [sl(4.0, 0.6), sl(6.0, -6.0), sl(8.6, -10.4), sl(12.0, -11.2), sl(14.6, -8.6), sl(16.2, -3.0), sl(20.0, 0.4)]
# guzki grzebienia krzyżowego pośrodkowego (falisty brzeg tylny)
bk = []
for i, p in enumerate(back):
    if 3 <= i <= 17 and i % 3 == 0:
        t = i / NS; sv = S_SAC + t * SAC_LEN; c2, u2, n2 = frame(sv)
        bk.append((p[0] + 0.55 * n2[0], p[1] + 0.55 * n2[1]))
    else:
        bk.append(p)
sac = sap + bk[1:] + front[::-1]
f.add(f'<path class="bone" d="{smooth(sac)}"/>')
# powierzchnia uchowata (część boczna, górna połowa) – zarys
def sacpt(t, frac):   # punkt wewnątrz kości: frac 0 = przód, 1 = tył
    sv = S_SAC + t * SAC_LEN; c2, u2, n2 = frame(sv)
    D = sac_D(t); a = -D / 2 + frac * (D + sac_P(t))
    return G(c2[0] + a * n2[0], c2[1] + a * n2[1])
aur = [sacpt(0.10, 0.50), sacpt(0.08, 0.68), sacpt(0.14, 0.80), sacpt(0.26, 0.74), sacpt(0.36, 0.62), sacpt(0.46, 0.60),
       sacpt(0.50, 0.52), sacpt(0.44, 0.44), sacpt(0.32, 0.46), sacpt(0.22, 0.42)]
f.add(f'<path class="bone2" d="{smooth(aur)}"/>')
# kresy poprzeczne – miejsca zrośnięcia trzonów S1–S5
for t in (0.27, 0.50, 0.70, 0.86):
    a, b = sacpt(t, 0.0), sacpt(t, 0.30)
    f.add(f'<path class="bonel" d="M{a[0]:.2f},{a[1]:.2f} L{b[0]:.2f},{b[1]:.2f}"/>')

# ---------------- kość guziczna (4 szczątkowe kręgi) ----------------
co = [(8.5, 12.0), (7.5, 9.5), (6.0, 7.5), (5.0, 6.0)]
sv = S_SAC + SAC_LEN + 2.2
co_boxes = []
for i, (hh, DD) in enumerate(co):
    s0, s1 = sv, sv + hh
    pts = []
    for (sx, fr) in [(s0, -0.5), (s0, 0.5), (s1, 0.5), (s1, -0.5)]:
        c2, u2, n2 = frame(sx); pts.append(G(c2[0] + fr * DD * n2[0], c2[1] + fr * DD * n2[1]))
    co_boxes.append(pts)
    sv = s1 + 1.4
for i, pts in enumerate(co_boxes):
    # zaokrąglony czworobok
    a, b, c3, d = pts
    def mid(p, q, t=0.5): return (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)
    poly = [mid(a, b, .2), mid(a, b, .8), mid(b, c3, .2), mid(b, c3, .8), mid(c3, d, .2), mid(c3, d, .8), mid(d, a, .2), mid(d, a, .8)]
    f.add(f'<path class="bone" d="{smooth(poly, t=0.6)}"/>')

# ---------------- krążki międzykręgowe i trzony ----------------
def body_corners(v):
    c, u, n = frame((v['s0'] + v['s1']) / 2)
    D, ha, hp = v['D'], v['h'], v['hp']
    def P(fr, hh, sgn): return G(c[0] + fr * D / 2 * n[0] + sgn * hh / 2 * u[0], c[1] + fr * D / 2 * n[1] + sgn * hh / 2 * u[1])
    return P(-1, ha, -1), P(1, hp, -1), P(1, hp, 1), P(-1, ha, 1)     # przód-góra, tył-góra, tył-dół, przód-dół
bodies = [v for v in V]
for v, w in zip(bodies, bodies[1:]):
    a1, b1, c1, d1 = body_corners(v); a2, b2, c2_, d2 = body_corners(w)
    f.add(f'<path class="annulus" d="M{d1[0]:.2f},{d1[1]:.2f} L{c1[0]:.2f},{c1[1]:.2f} L{b2[0]:.2f},{b2[1]:.2f} L{a2[0]:.2f},{a2[1]:.2f} Z"/>')
# krążek L5–S1
a1, b1, c1, d1 = body_corners(V[-1])
f.add(f'<path class="annulus" d="M{d1[0]:.2f},{d1[1]:.2f} L{c1[0]:.2f},{c1[1]:.2f} L{back[0][0] * 0 + sl(0, 0)[0]:.2f},{sl(0, 0)[1]:.2f} L{front[0][0]:.2f},{front[0][1]:.2f} Z"/>')

def body_path(v):
    a, b, c3, d = body_corners(v)
    def mid(p, q, t): return (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)
    # lekko wklęsła powierzchnia przednia
    cc, u, n = frame((v['s0'] + v['s1']) / 2)
    m = mid(a, d, 0.5); inset = 0.035 * v['D'] * S
    m = (m[0] + n[0] * inset, m[1] + n[1] * inset)
    poly = [mid(a, b, .12), mid(a, b, .88), mid(b, c3, .1), mid(b, c3, .9), mid(c3, d, .12), mid(c3, d, .88),
            mid(d, a, .1), m, mid(d, a, .9)]
    return smooth(poly, t=0.45)
for v in V:
    if v['name'] == 'C2':
        continue
    f.add(f'<path class="bone" d="{body_path(v)}"/>')

# C2: trzon z zębem
v = byname['C2']
c2pts = [locA(v, 1.0, 0.6), locA(v, 4.0, -1.0), locA(v, 4.6, -6.0), locA(v, 4.4, -11.0), locA(v, 6.0, -14.2),
         locA(v, 9.0, -15.0), locA(v, 11.4, -13.6), locA(v, 12.4, -9.0), locA(v, 12.6, -3.0), locA(v, 14.0, -0.6),
         locA(v, 15.0, 2.0), locA(v, 15.2, 10.0), locA(v, 15.0, 20.0), locA(v, 14.0, 24.0), locA(v, 8.0, 24.3),
         locA(v, 1.4, 24.8), locA(v, -0.6, 23.0), locA(v, 0.0, 14.0), locA(v, 0.4, 6.0)]
f.add(f'<path class="bone" d="{smooth(c2pts)}"/>')

# C1 – łuk przedni, część boczna, łuk tylny z guzkiem tylnym (na wierzchu, bo leży bocznie od zęba)
v = byname['C2']
c1 = [locA(v, -1.6, -11.0), locA(v, 2.0, -12.4), locA(v, 8.0, -13.0), locA(v, 13.0, -12.6), locA(v, 15.4, -11.4),
      locA(v, 17.0, -10.0), locA(v, 24.0, -10.2), locA(v, 31.0, -10.4), locA(v, 35.0, -11.8), locA(v, 37.6, -11.0),
      locA(v, 38.0, -8.0), locA(v, 36.4, -5.8), locA(v, 32.0, -6.0), locA(v, 24.0, -5.8), locA(v, 18.0, -5.4),
      locA(v, 15.6, -2.2), locA(v, 12.0, -1.0), locA(v, 5.0, -1.0), locA(v, 1.8, -2.4), locA(v, -1.4, -4.4),
      locA(v, -2.6, -7.6)]
f.add(f'<path class="bone" d="{smooth(c1)}"/>')

print('extent', min(p[0] for p in AX) * S + X0, max(p[0] for p in AX) * S + X0, AX[-1][1] * S + Y0)
f.save()
