# WDECH I WYDECH – klatka piersiowa powiększa się we wszystkich trzech kierunkach (Bochenek s. 696–697).
# Lewy panel: klatka od przodu (prawa strona ciała po lewej) – wymiar poprzeczny i długościowy (przepona).
# Prawy panel: klatka od strony lewej (przód w lewo) – wymiar przednio-tylny (mostek), przepona, kręgosłup.
# Kości i przepona narysowane w położeniu wydechowym; linia przerywana = położenie przy wdechu.
# Strzałki: niebieskie – ruch przy wdechu, czerwone – ruch przy wydechu. Schemat własny (ruchy nieco powiększone).
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 162, 79
f = Fig('oddychanie_wymiary', W, H,
        caption='klatka piersiowa przy wydechu i przy wdechu · od przodu (prawa strona ciała po lewej) i od strony lewej (przód w lewo)')


# ---------------------------------------------------------------- pomocnicze
def cr(pts, closed=False, n=12, t=0.5):
    """punkty na krzywej Catmull-Rom (ta sama krzywa co smooth)."""
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
    """pasmo o szerokości w0→w1 wzdłuż krzywej przez pts (zamknięty wielokąt)."""
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

    def capf(p, q, center, w, k=7):     # półokrąg od p do q wokół center
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


def rot(p, o, deg):
    a = math.radians(deg)
    x, y = p[0] - o[0], p[1] - o[1]
    return (o[0] + x * math.cos(a) - y * math.sin(a), o[1] + x * math.sin(a) + y * math.cos(a))


# ================================================================ PANEL A – klatka od przodu
S = 1.45                 # mm na cm
CX, Y0 = 61.0, 11.5      # oś pośrodkowa, poziom górnego brzegu Th1


def FA(u, y, side=-1):
    """u – odległość od płaszczyzny pośrodkowej (cm), side=-1 prawa strona ciała (lewa strona rysunku)."""
    return (CX + side * S * u, Y0 + S * y)


# żebra (połowa klatki): A – najbardziej boczny punkt, J – granica z chrząstką (lub wolny koniec XI–XII)
RA = [(5.8, 2.0), (9.0, 4.9), (11.3, 7.6), (12.9, 10.2), (14.0, 12.8), (14.7, 15.4), (15.1, 18.0), (15.2, 20.5),
      (15.0, 22.9), (14.6, 25.1), (14.0, 27.0), (12.9, 28.6)]
RJ = [(3.8, 4.6), (5.8, 8.3), (7.2, 11.4), (8.3, 14.2), (9.2, 17.0), (9.9, 19.8), (10.6, 22.6), (11.3, 25.0),
      (12.1, 27.2), (12.9, 29.2), (13.3, 30.0), (12.0, 31.0)]
RW = [(1.5, 1.6), (1.1, 1.3), (0.9, 1.2), (0.9, 1.2), (0.9, 1.15), (0.9, 1.15), (0.9, 1.1), (0.85, 1.05),
      (0.85, 1.0), (0.8, 0.95), (0.75, 0.7), (0.7, 0.65)]
# chrząstki żebrowe (od J do mostka / do chrząstki wyżej)
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


def rib_mid(a, j):
    return (a[0] - (a[0] - j[0]) * 0.30, a[1] + (j[1] - a[1]) * 0.60)


def front_cage(tf, draw=True):
    """rysuje klatkę od przodu (tf: (u, y) -> punkt przy danej stronie)"""
    shapes = []
    for side in (-1, 1):
        T = lambda p: tf(p[0], p[1], side)
        for k in range(12):
            a, j = RA[k], RJ[k]
            pts = [T(a), T(rib_mid(a, j)), T(j)]
            shapes.append(('bone', poly(band(pts, RW[k][0] * S, RW[k][1] * S, cap0=True, cap1=(k >= 10)))))
        for k in range(12):
            w = (0.95 if k < 10 else 0.6) * S
            shapes.append(('cart', poly(band([T(p) for p in CART[k]], w, w * (0.95 if k < 7 else 0.8), cap1=(k >= 7)))))
    # mostek
    half = [(0, 4.5), (1.3, 4.1), (2.5, 3.8), (2.75, 4.9), (2.35, 6.2), (1.65, 8.2), (1.55, 8.9), (1.65, 9.3),
            (1.85, 11.6), (1.95, 14.0), (2.05, 16.4), (1.95, 18.5), (1.5, 19.7), (1.0, 20.1), (0.95, 21.9), (0.45, 23.1)]
    outline = [tf(u, y, -1) for u, y in half] + [tf(0, 23.5, -1)] + [tf(u, y, 1) for u, y in reversed(half[1:])]
    shapes.append(('bone', smooth(outline, closed=True, t=0.35)))
    for y in (8.95, 19.75):
        hw = 1.55 if y < 10 else 1.45
        p, q = tf(hw, y, -1), tf(hw, y, 1)
        shapes.append(('bonel', f'M{p[0]:.2f},{p[1]:.2f} L{q[0]:.2f},{q[1]:.2f}'))
    if draw:
        for cls, d in shapes:
            f.add(f'<path class="{cls}" d="{d}"/>')
    return shapes


# przepona od przodu (wydech): przyczep boczny → kopuła prawa → środek ścięgnisty → kopuła lewa → przyczep boczny
DIA_E = [(14.3, 28.4), (13.6, 24.5), (11.6, 19.8), (8.6, 17.2), (5.6, 16.7), (2.6, 17.6), (0.0, 18.2),
         (-2.6, 18.0), (-5.8, 17.6), (-8.8, 18.3), (-11.7, 20.9), (-13.6, 25.2), (-14.3, 28.6)]
DIA_I = [(15.2, 28.2), (14.6, 25.8), (12.4, 23.5), (9.0, 22.0), (5.6, 21.6), (2.6, 21.6), (0.0, 21.4),
         (-2.6, 21.7), (-5.8, 22.4), (-9.0, 23.1), (-12.6, 24.5), (-14.7, 26.3), (-15.3, 28.4)]


def FAs(u, y):          # u ze znakiem: + prawa strona ciała (lewa strona rysunku)
    return (CX - S * u, Y0 + S * y)


# kontur boczny klatki przy wdechu (linia przerywana): żebra unoszą się i odchylają ku bokom
def side_contour():
    pts = [(9.0, 4.9), (11.3, 7.6), (12.9, 10.2), (14.0, 12.8), (14.7, 15.4), (15.1, 18.0), (15.2, 20.5),
           (15.0, 22.9), (14.6, 25.1), (14.0, 27.0), (13.3, 30.0)]
    return [(u * 1.06 + 0.55, y - 0.6) for u, y in pts]


# kolejność: przepona (wydech) pod klatką? – przepona na wierzchu, żeby była czytelna
front_cage(lambda u, y, side: FA(u, y, side))

# przepona – wydech (pasmo mięśniowe z odcinkiem ścięgnistym pośrodku)
dia_pts = [FAs(u, y) for u, y in DIA_E]
f.add(f'<path class="muscle" d="{poly(band(dia_pts, 1.05, n=12))}"/>')
ten = [FAs(u, y) for u, y in DIA_E[4:9]]
f.add(f'<path class="tendon" d="{poly(band(ten, 1.05, n=12))}"/>')
# przepona – wdech (linia przerywana)
f.add(f'<path class="capsule" d="{smooth([FAs(u, y) for u, y in DIA_I], closed=False)}"/>')

# kontur klatki przy wdechu – obie strony
for side in (-1, 1):
    cont = [FA(u, y, side) for u, y in side_contour()]
    f.add(f'<path class="capsule" d="{smooth(cont, closed=False)}"/>')
# łuk żebrowy przy wdechu (unosi się i rozchyla)
arc_i = [(14.65, 29.4), (13.0, 29.0), (10.6, 27.1), (8.0, 24.6), (5.2, 21.9), (2.5, 19.6), (0.0, 18.9)]
for side in (-1, 1):
    f.add(f'<path class="capsule" d="{smooth([FA(u, y, side) for u, y in arc_i], closed=False)}"/>')

# wymiar poprzeczny (linia pomocnicza) na wysokości żeber VIII–IX
yT = 19.3
pL, pR = FA(15.0, yT, -1), FA(15.0, yT, 1)
f.add(f'<path class="dim" d="M{pL[0]:.2f},{pL[1]:.2f} L{pR[0]:.2f},{pR[1]:.2f}"/>')
# strzałki boczne: wdech na zewnątrz (niebieska), wydech do środka (czerwona)
for side in (-1, 1):
    x0 = CX + side * S * 16.95
    yb, yr = Y0 + S * yT - 1.25, Y0 + S * yT + 1.25
    f.arrow(f'M{x0:.2f},{yb:.2f} L{x0 + side * 6.6:.2f},{yb:.2f}')
    f.arrow(f'M{x0 + side * 7.0:.2f},{yr:.2f} L{x0 + side * 0.6:.2f},{yr:.2f}', red=True)

# strzałki przepony (kopuła prawa): wdech w dół, wydech w górę
xd = CX - S * 6.2
yE = Y0 + S * 16.75
yI = Y0 + S * 21.6
f.arrow(f'M{xd - 1.2:.2f},{yE + 1.2:.2f} L{xd - 1.2:.2f},{yI + 0.2:.2f}')
f.arrow(f'M{xd + 1.3:.2f},{yI - 0.2:.2f} L{xd + 1.3:.2f},{yE + 1.0:.2f}', red=True)

# ================================================================ PANEL B – klatka z boku (od strony lewej, przód w lewo)
XO, YB = 118.0, 11.5     # przednia powierzchnia trzonu Th1 (z = 0)


def FB(z, y):
    """z – w przód od przedniej powierzchni trzonu Th1 (cm, + ku przodowi = w lewo), y – w dół od górnego brzegu Th1."""
    return (XO - S * z, YB + S * y)


def za(y):
    """przednia powierzchnia trzonów (kifoza piersiowa, potem łagodna lordoza)"""
    if y <= 30:
        return -2.2 * math.sin(math.pi * y / 30)
    return 0.25 * (y - 30)


def depth(y):
    return 2.0 + 1.3 * min(max(y, 0), 36) / 30


# kręgosłup: Th1–Th12, L1–L2
bodies = []
y = 0.0
for k in range(14):
    h = 1.95 + 0.045 * k if k < 12 else 2.6
    disc = 0.5 if k < 11 else 0.8
    bodies.append((y, y + h))
    y += h + disc


def body_path(yt, yb, r=0.35):
    fa, fb = za(yt), za(yb)
    pts = [(fa, yt + r), (fa - r * 0.6, yt), (fa - depth(yt) + r * 0.6, yt), (fa - depth(yt), yt + r),
           (fb - depth(yb), yb - r), (fb - depth(yb) + r * 0.6, yb), (fb - r * 0.6, yb), (fb, yb - r)]
    return smooth([FB(*p) for p in pts], closed=True, t=0.3)


for i in range(len(bodies) - 1):          # krążki
    yt, yb = bodies[i][1], bodies[i + 1][0]
    pts = [(za(yt) - 0.1, yt), (za(yt) - depth(yt) + 0.1, yt), (za(yb) - depth(yb) + 0.1, yb), (za(yb) - 0.1, yb)]
    f.add(f'<path class="annulus" d="{poly([FB(*p) for p in pts])}"/>')
for yt, yb in bodies:
    f.add(f'<path class="bone" d="{body_path(yt, yb)}"/>')

# żebra z boku
YH = [0.9] + [(k - 1) * 2.45 + 0.4 for k in range(2, 13)]
DROP = [3.9, 5.2, 6.2, 6.6, 7.0, 7.4, 7.8, 7.8, 7.6, 7.0, 5.0, 3.6]
ZE = [4.4, 5.8, 6.6, 7.1, 7.5, 7.7, 7.6, 7.0, 6.2, 5.2, 1.0, -3.4]
ZANG = [-3.2, -4.3] + [-5.0] * 8 + [-4.8, -4.4]


def rib_side(k, ang=0.0):
    yh = YH[k]
    zh = za(yh) - 1.5
    zg = za(yh) + ZANG[k] if k >= 2 else ZANG[k] + za(yh)
    d, ze = DROP[k], ZE[k]
    pts = [(zh, yh), (zh - 1.9, yh + 0.1), (zg, yh + 0.8), (zg + (ze - zg) * 0.20, yh + 0.45 * d),
           (zg + (ze - zg) * 0.56, yh + 0.83 * d), (ze, yh + d)]
    if ang:
        pts = [rot(p, (zh, yh), ang) for p in pts]
    return pts


# chrząstki z boku: od końca żebra do mostka (I–VII) albo do chrząstki wyżej (VIII–X)
STERN_F = [(6.0, 4.4), (6.25, 4.7), (7.1, 7.0), (7.6, 8.9), (8.4, 12.0), (9.4, 16.0), (10.1, 19.6), (10.25, 20.3), (9.8, 23.4)]
STERN_B = [(9.6, 23.5), (9.3, 20.5), (8.95, 19.6), (8.25, 16.4), (7.2, 12.4), (6.0, 8.9), (4.8, 5.4), (4.85, 4.6)]
SY = [5.3, 9.0, 11.8, 14.3, 16.6, 18.6, 19.7]


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


RIBS_E = [rib_side(k) for k in range(12)]
for k in range(12):
    pts = [FB(*p) for p in RIBS_E[k]]
    w0, w1 = (1.25 if k > 0 else 1.5) * S, (1.15 if k < 10 else 0.8) * S
    f.add(f'<path class="bone" d="{poly(band(pts, w0, w1, cap0=True, cap1=(k >= 10)))}"/>')
    c = cart_side(k, RIBS_E[k])
    if c:
        f.add(f'<path class="cart" d="{poly(band([FB(*p) for p in c], 0.95 * S, 0.85 * S, cap1=(k >= 7)))}"/>')

# mostek z boku
st = STERN_F + STERN_B
f.add(f'<path class="bone" d="{smooth([FB(*p) for p in st], closed=True, t=0.35)}"/>')
for y in (8.95, 19.7):
    a, b = FB(stern_back(y) + 0.05, y), FB(STERN_F[3][0] if y < 10 else 10.1, y)
    f.add(f'<path class="bonel" d="M{a[0]:.2f},{a[1]:.2f} L{b[0]:.2f},{b[1]:.2f}"/>')

# przepona z boku (wydech) i przy wdechu
DS_E = [(8.7, 22.8), (7.2, 19.6), (4.6, 17.4), (2.0, 16.9), (-1.0, 17.7), (-3.4, 20.6), (-4.7, 24.6), (-5.2, 28.4), (-5.0, 31.2)]
DS_I = [(9.4, 21.9), (7.5, 21.5), (4.6, 22.8), (1.6, 23.4), (-1.4, 24.0), (-3.7, 25.9), (-4.9, 28.6), (-5.2, 31.3)]
f.add(f'<path class="muscle" d="{poly(band([FB(*p) for p in DS_E], 1.05, n=12))}"/>')
ten2 = [FB(*p) for p in DS_E[1:5]]
f.add(f'<path class="tendon" d="{poly(band(ten2, 1.05, n=12))}"/>')
f.add(f'<path class="capsule" d="{smooth([FB(*p) for p in DS_I], closed=False)}"/>')

# mostek i żebro VII przy wdechu – obrót żeber ku górze wokół ich tylnych końców
ANG = -11.0
k7 = 6
r7 = rib_side(k7, ANG)
h1 = (za(YH[0]) - 1.5, YH[0]); h7 = (za(YH[k7]) - 1.5, YH[k7])
s1 = (stern_back(SY[0]) + 0.55, SY[0]); s7 = (stern_back(SY[6]) + 0.55, SY[6])
s1n, s7n = rot(s1, h1, ANG * 0.8), rot(s7, h7, ANG)
# przekształcenie sztywne mostka: (s1, s7) → (s1n, s7n)
a0 = math.atan2(s7[1] - s1[1], s7[0] - s1[0]); a1 = math.atan2(s7n[1] - s1n[1], s7n[0] - s1n[0])


def stern_tf(p):
    q = rot(p, s1, math.degrees(a1 - a0))
    return (q[0] + s1n[0] - s1[0], q[1] + s1n[1] - s1[1])


st_i = [stern_tf(p) for p in st]
f.add(f'<path class="capsule" d="{smooth([FB(*p) for p in st_i], closed=True, t=0.35)}"/>')
f.add(f'<path class="capsule" d="{poly(band([FB(*p) for p in r7], 1.15 * S, 1.15 * S))}"/>')
c7 = cart_side(k7, r7)
c7[-1] = stern_tf(c7[-1])
f.add(f'<path class="capsule" d="{poly(band([FB(*p) for p in c7], 0.9 * S))}"/>')

# wymiar przednio-tylny (linia pomocnicza) na wysokości połączenia mostka z wyrostkiem mieczykowatym
yAP = 18.2
pa, pb = FB(10.4, yAP), FB(-7.05, yAP)
f.add(f'<path class="dim" d="M{pa[0]:.2f},{pa[1]:.2f} L{pb[0]:.2f},{pb[1]:.2f}"/>')
# strzałki mostka: wdech – ku przodowi i ku górze, wydech – ku tyłowi i ku dołowi
q0 = FB(10.3, 15.6)
f.arrow(f'M{q0[0] - 0.4:.2f},{q0[1] - 0.9:.2f} L{q0[0] - 6.4:.2f},{q0[1] - 3.6:.2f}')
f.arrow(f'M{q0[0] - 5.5:.2f},{q0[1] - 0.3:.2f} L{q0[0] - 0.3:.2f},{q0[1] + 2.1:.2f}', red=True)
# strzałki przepony z boku
xd2 = FB(1.0, 0)[0]
yE2, yI2 = FB(0, 17.3)[1], FB(0, 23.6)[1]
f.arrow(f'M{xd2 - 1.2:.2f},{yE2 + 1.2:.2f} L{xd2 - 1.2:.2f},{yI2:.2f}')
f.arrow(f'M{xd2 + 1.3:.2f},{yI2 - 0.2:.2f} L{xd2 + 1.3:.2f},{yE2 + 1.1:.2f}', red=True)
# strzałki kręgosłupa (nad Th1): wdech – prostuje się i wydłuża (w górę), wydech – zgina (w dół)
xs = FB(-1.0, 0)[0]
f.arrow(f'M{xs - 1.2:.2f},{YB - 0.8:.2f} L{xs - 1.2:.2f},{YB - 7.2:.2f}')
f.arrow(f'M{xs + 1.3:.2f},{YB - 7.4:.2f} L{xs + 1.3:.2f},{YB - 1.0:.2f}', red=True)

# ---------------------------------------------------------------- legenda
LY = 69.5
lx = 17.0
f.add(f'<rect class="bone" x="{lx:.2f}" y="{LY - 1.6:.2f}" width="5.2" height="2.2" rx=".5"/>')
f.text(lx + 6.6, LY + 0.3, 'położenie przy wydechu', cls='note')
lx2 = lx + 37.0
f.add(f'<path class="capsule" d="M{lx2:.2f},{LY - 0.5:.2f} L{lx2 + 5.6:.2f},{LY - 0.5:.2f}"/>')
f.text(lx2 + 6.8, LY + 0.3, 'położenie przy wdechu', cls='note')
lx3 = lx2 + 35.0
f.arrow(f'M{lx3:.2f},{LY - 0.5:.2f} L{lx3 + 7.0:.2f},{LY - 0.5:.2f}')
f.text(lx3 + 8.4, LY + 0.3, 'ruch przy wdechu', cls='note')
lx4 = lx3 + 30.0
f.arrow(f'M{lx4:.2f},{LY - 0.5:.2f} L{lx4 + 7.0:.2f},{LY - 0.5:.2f}', red=True)
f.text(lx4 + 8.4, LY + 0.3, 'ruch przy wydechu', cls='note')

# tytuły paneli
f.text(CX, 4.4, 'od przodu', cls='notec')
f.text(104.0, 4.4, 'z boku', cls='notec')

# ---------------------------------------------------------------- podpisy
# panel A (lewa kolumna)
f.label(FA(10.9, 6.9, -1), 'żebra', 'costae', (31.5, 15.0), side='L')
f.label(FA(0.0, 13.0, -1), 'mostek', 'sternum', (31.5, 24.5), side='L')
f.label(FA(10.4, 18.6, -1), 'przepona', 'diaphragma', (31.5, 34.0), side='L')
f.label((CX - S * 15.2 - 3.4, Y0 + S * yT + 1.25), 'wymiar poprzeczny', None, (31.5, 45.5), side='L')
f.text(30.8, 49.3, 'żebra unoszą się –', cls='note', anchor='end')
f.text(30.8, 52.0, 'klatka poszerza się', cls='note', anchor='end')
f.label((xd - 1.2, Y0 + S * 19.6), 'wymiar długościowy', None, (31.5, 58.5), side='L')
f.text(30.8, 62.3, 'przepona kurczy się', cls='note', anchor='end')
f.text(30.8, 65.0, 'i obniża', cls='note', anchor='end')
# panel B (prawa kolumna)
f.label(FB(-2.0, 1.2), 'kręgosłup', 'columna vertebralis', (131.0, 9.5), side='R')
f.text(131.7, 16.0, 'prostuje się – klatka', cls='note')
f.text(131.7, 18.7, 'wydłuża się', cls='note')
f.label(pb, 'wymiar przednio-tylny', None, (131.0, 30.5), side='R')
f.text(131.7, 34.3, 'żebra unoszą się –', cls='note')
f.text(131.7, 37.0, 'klatka pogłębia się', cls='note')
f.label(FB(-4.6, 22.6), 'przepona', 'diaphragma', (131.0, 46.0), side='R')
f.save()
print('ok')
