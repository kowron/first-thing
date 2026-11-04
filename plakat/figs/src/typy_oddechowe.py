# TYPY ODDECHOWE (Bochenek, t. I, s. 696–697, streszczenie s. 701).
# Typ oddechowy żebrowy albo piersiowy – poruszają się żebra:
#   A – oddychanie żebrowe dolne = mechanizm żebrowo-przeponowy (dolne żebra unosząc się odchylają się silnie ku bokom,
#       dolna część klatki poszerza się; przewietrza głównie dolne części płuc) – widok od przodu;
#   B – oddychanie żebrowe górne = mechanizm żebrowo-mostkowy (górne żebra wraz z mostkiem; gdy dolna część klatki
#       jest ograniczona w ruchach, np. przez pasek; przewietrza silniej górne części płuc) – widok z boku.
# Typ oddechowy brzuszny albo przeponowy – bez bezpośredniego udziału żeber:
#   C – przepona obniża się, zawartość jamy brzusznej kieruje się ku przedniej ścianie brzucha i nieco ją uwypukla,
#       głównie powyżej pępka; przy wydechu przepona wpukla się w obręb klatki (sprężystość płuc + napięcie mm. brzucha).
# Linia ciągła – położenie przy wydechu, przerywana – przy wdechu. Strzałki: niebieska – wdech, czerwona – wydech.
# Schemat własny (ruchy nieco powiększone); kształty klatki jak w oddychanie_wymiary.py (spójność rysunków).
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 150, 108
f = Fig('typy_oddechowe', W, H,
        caption='typy oddechowe · klatka od przodu (prawa strona ciała po lewej) i od strony lewej (przód w lewo) · schemat')
S = 1.15                 # mm na cm


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


def rot(p, o, deg):
    a = math.radians(deg)
    x, y = p[0] - o[0], p[1] - o[1]
    return (o[0] + x * math.cos(a) - y * math.sin(a), o[1] + x * math.sin(a) + y * math.cos(a))


def sstep(t):
    t = min(max(t, 0.0), 1.0)
    return t * t * (3 - 2 * t)


def add(cls, d):
    f.add(f'<path class="{cls}" d="{d}"/>')


# ================================================================ dane klatki od przodu (cm; u – od płaszczyzny pośrodkowej)
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
# przepona od przodu (u ze znakiem: + prawa strona ciała)
DIA_E = [(14.3, 28.4), (13.6, 24.5), (11.6, 19.8), (8.6, 17.2), (5.6, 16.7), (2.6, 17.6), (0.0, 18.2),
         (-2.6, 18.0), (-5.8, 17.6), (-8.8, 18.3), (-11.7, 20.9), (-13.6, 25.2), (-14.3, 28.6)]


def rib_mid(a, j):
    return (a[0] - (a[0] - j[0]) * 0.30, a[1] + (j[1] - a[1]) * 0.60)


def front_cage(tf):
    for side in (-1, 1):
        T = lambda p: tf(p[0], p[1], side)
        for k in range(12):
            a, j = RA[k], RJ[k]
            add('bone', poly(band([T(a), T(rib_mid(a, j)), T(j)], RW[k][0] * S, RW[k][1] * S, cap0=True, cap1=(k >= 10))))
        for k in range(12):
            w = (0.95 if k < 10 else 0.6) * S
            add('cart', poly(band([T(p) for p in CART[k]], w, w * (0.95 if k < 7 else 0.8), cap1=(k >= 7))))
    outline = [tf(u, y, -1) for u, y in STERN_HALF] + [tf(0, 23.5, -1)] + [tf(u, y, 1) for u, y in reversed(STERN_HALF[1:])]
    add('bone', smooth(outline, closed=True, t=0.35))
    for y in (8.95, 19.75):
        hw = 1.55 if y < 10 else 1.45
        p, q = tf(hw, y, -1), tf(hw, y, 1)
        add('bonel', f'M{p[0]:.2f},{p[1]:.2f} L{q[0]:.2f},{q[1]:.2f}')


# ================================================================ dane klatki z boku (cm; z – ku przodowi od przedniej pow. trzonu Th1)
def za(y):
    """przednia powierzchnia trzonów (kifoza piersiowa, potem lordoza lędźwiowa)"""
    if y <= 30:
        return -2.2 * math.sin(math.pi * y / 30)
    return 0.25 * (y - 30)


def depth(y):
    return 2.0 + 1.3 * min(max(y, 0), 36) / 30


BODIES = []
_y = 0.0
for k in range(17):                     # Th1–Th12, L1–L5
    h = 1.95 + 0.045 * k if k < 12 else 2.6
    BODIES.append((_y, _y + h))
    _y += h + (0.5 if k < 11 else 0.8)

YH = [0.9] + [(k - 1) * 2.45 + 0.4 for k in range(2, 13)]
DROP = [3.9, 5.2, 6.2, 6.6, 7.0, 7.4, 7.8, 7.8, 7.6, 7.0, 5.0, 3.6]
ZE = [4.4, 5.8, 6.6, 7.1, 7.5, 7.7, 7.6, 7.0, 6.2, 5.2, 1.0, -3.4]
ZANG = [-3.2, -4.3] + [-5.0] * 8 + [-4.8, -4.4]
STERN_F = [(6.0, 4.4), (6.25, 4.7), (7.1, 7.0), (7.6, 8.9), (8.4, 12.0), (9.4, 16.0), (10.1, 19.6), (10.25, 20.3), (9.8, 23.4)]
STERN_B = [(9.6, 23.5), (9.3, 20.5), (8.95, 19.6), (8.25, 16.4), (7.2, 12.4), (6.0, 8.9), (4.8, 5.4), (4.85, 4.6)]
SY = [5.3, 9.0, 11.8, 14.3, 16.6, 18.6, 19.7]
DS_E = [(8.7, 22.8), (7.2, 19.6), (4.6, 17.4), (2.0, 16.9), (-1.0, 17.7), (-3.4, 20.6), (-4.7, 24.6), (-5.2, 28.4), (-5.0, 31.2)]


def rib_side(k, ang=0.0):
    yh = YH[k]
    zh = za(yh) - 1.5
    zg = za(yh) + ZANG[k]
    d, ze = DROP[k], ZE[k]
    pts = [(zh, yh), (zh - 1.9, yh + 0.1), (zg, yh + 0.8), (zg + (ze - zg) * 0.20, yh + 0.45 * d),
           (zg + (ze - zg) * 0.56, yh + 0.83 * d), (ze, yh + d)]
    if ang:
        pts = [rot(p, (zh, yh), ang) for p in pts]
    return pts


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


def lung_side():
    """płuco w rzucie bocznym (cm): szczyt → brzeg przedni (za mostkiem) → podstawa (na przeponie) → brzeg tylny."""
    front = [(1.2, -1.9), (3.2, -0.6), (4.3, 2.6)] + [(stern_back(y) - 0.7, y) for y in (6.0, 9.0, 12.0, 15.0, 18.0)] + \
            [(8.0, 20.6)]
    base = [(x, y - 0.75) for x, y in cr(DS_E, n=6)[1:]]
    back = [(-5.6, 28.0), (-6.6, 23.0), (-7.2, 17.0), (-7.0, 11.0), (-5.9, 5.5), (-4.1, 1.6), (-1.6, -1.2)]
    return front, base, back


def side_panel(FB, n_vert=14, abdomen=None):
    """klatka z boku. abdomen – funkcja rysująca jamę brzuszną (pod kośćmi) albo None"""
    fr, base, back = lung_side()
    add('organ', poly([FB(*p) for p in cr(fr, n=6)] + [FB(*p) for p in base] + [FB(*p) for p in cr(back, n=6)]))
    if abdomen:
        abdomen()
    bodies = BODIES[:n_vert]
    for i in range(len(bodies) - 1):
        yt, yb = bodies[i][1], bodies[i + 1][0]
        pts = [(za(yt) - 0.1, yt), (za(yt) - depth(yt) + 0.1, yt), (za(yb) - depth(yb) + 0.1, yb), (za(yb) - 0.1, yb)]
        add('annulus', poly([FB(*p) for p in pts]))
    for yt, yb in bodies:
        r = 0.35
        fa, fb = za(yt), za(yb)
        pts = [(fa, yt + r), (fa - r * 0.6, yt), (fa - depth(yt) + r * 0.6, yt), (fa - depth(yt), yt + r),
               (fb - depth(yb), yb - r), (fb - depth(yb) + r * 0.6, yb), (fb - r * 0.6, yb), (fb, yb - r)]
        add('bone', smooth([FB(*p) for p in pts], closed=True, t=0.3))
    ribs = [rib_side(k) for k in range(12)]
    for k in range(12):
        pts = [FB(*p) for p in ribs[k]]
        w0, w1 = (1.25 if k > 0 else 1.5) * S, (1.15 if k < 10 else 0.8) * S
        add('bone', poly(band(pts, w0, w1, cap0=True, cap1=(k >= 10))))
        c = cart_side(k, ribs[k])
        if c:
            add('cart', poly(band([FB(*p) for p in c], 0.95 * S, 0.85 * S, cap1=(k >= 7))))
    st = STERN_F + STERN_B
    add('bone', smooth([FB(*p) for p in st], closed=True, t=0.35))
    for y in (8.95, 19.7):
        a, b = FB(stern_back(y) + 0.05, y), FB(STERN_F[3][0] if y < 10 else 10.1, y)
        add('bonel', f'M{a[0]:.2f},{a[1]:.2f} L{b[0]:.2f},{b[1]:.2f}')
    return ribs


def diaphragm_side(FB, pts=DS_E):
    add('muscle', poly(band([FB(*p) for p in pts], 1.0 * S, n=12)))
    add('tendon', poly(band([FB(*p) for p in pts[1:5]], 1.0 * S, n=12)))


# ================================================================ układ
YTOP = 25.5                               # górny brzeg trzonu Th1 (wszystkie panele)
CXA = 28.0                                # A – oś pośrodkowa
XOB = 76.0                                # B – przednia powierzchnia trzonu Th1
XOC = 116.5                               # C – przednia powierzchnia trzonu Th1
YCUT = 52.0                               # C – dolna linia cięcia (cm)

# ================================================================ PANEL A – oddychanie żebrowe dolne (od przodu)


def FA(u, y, side=-1):
    return (CXA + side * S * u, YTOP + S * y)


def FAs(u, y):
    return (CXA - S * u, YTOP + S * y)


def low_tf(u, y):
    """wdech w typie żebrowym dolnym: dolne żebra unoszą się i silnie odchylają ku bokom"""
    w = sstep((y - 15.0) / 9.0)
    return (u * (1 + 0.10 * w), y - 0.9 * w)


# płuca od przodu (pod żebrami)
LUNG_F = [(2.6, -2.0), (4.4, -2.3), (6.4, -0.6), (8.4, 3.0), (10.6, 6.2), (12.3, 9.2), (13.4, 12.2), (14.0, 15.2),
          (14.3, 18.2), (14.2, 21.2), (13.8, 24.3)]


def lung_front(side):
    s = -side                            # znak u w DIA_E: + prawa strona ciała
    dia = [(abs(u), y - 0.75) for u, y in cr(DIA_E, n=8) if u * s > 1.2]
    dia.sort(key=lambda p: -p[0])
    med = [(3.0, 16.0), (2.2, 11.0), (1.9, 6.0), (2.0, 1.0)] if side < 0 else \
        [(6.0, 17.0), (4.6, 13.0), (2.4, 9.0), (1.9, 4.0), (2.0, 0.5)]
    pts = LUNG_F + [p for p in dia if p[0] < 13.6 and (side < 0 or p[0] > 6.4)] + med
    return [FA(u, y, side) for u, y in pts]


for sd in (-1, 1):
    add('organ', smooth(lung_front(sd), closed=True, t=0.4))
front_cage(lambda u, y, side: FA(u, y, side))
# przepona (wydech)
add('muscle', poly(band([FAs(u, y) for u, y in DIA_E], 1.0 * S, n=12)))
add('tendon', poly(band([FAs(u, y) for u, y in DIA_E[4:9]], 1.0 * S, n=12)))
# wdech: zarys boczny dolnych żeber i łuk żebrowy (dolne żebra unoszą się i odchylają ku bokom)
ARCH = [(12.9, 29.2), (11.6, 28.8), (10.1, 27.3), (8.3, 25.0), (6.3, 22.6), (3.4, 20.8), (1.7, 19.8)]
for sd in (-1, 1):
    cont = [low_tf(u, y) for u, y in RA[5:11]] + [low_tf(13.6, 29.6)]
    add('capsule', smooth([FA(u + 0.55, y, sd) for u, y in cont], closed=False))
    add('capsule', smooth([FA(*low_tf(u, y), sd) for u, y in ARCH], closed=False))
# strzałki: wdech – dolne żebra ku bokom (niebieska), wydech – do środka (czerwona)
yT = YTOP + S * 23.0
for sd in (-1, 1):
    x0 = CXA + sd * S * 16.7
    f.arrow(f'M{x0:.2f},{yT - 1.2:.2f} L{x0 + sd * 5.2:.2f},{yT - 1.2:.2f}')
    f.arrow(f'M{x0 + sd * 5.6:.2f},{yT + 1.2:.2f} L{x0 + sd * 0.5:.2f},{yT + 1.2:.2f}', red=True)

# ================================================================ PANEL B – oddychanie żebrowe górne (z boku)


def FB_B(z, y):
    return (XOB - S * z, YTOP + S * y)


ribsB = side_panel(FB_B, n_vert=14)
diaphragm_side(FB_B)
# wdech: żebra I–V i mostek unoszą się (obrót ku górze wokół tylnych końców); żebra – linie osiowe
ANGS = [-6.0, -8.0, -9.0, -9.5, -9.5]
hh = [(za(YH[k]) - 1.5, YH[k]) for k in range(5)]
s1 = (stern_back(SY[0]) + 0.55, SY[0]); s5 = (stern_back(SY[4]) + 0.55, SY[4])
s1n, s5n = rot(s1, hh[0], ANGS[0]), rot(s5, hh[4], ANGS[4])
a0 = math.atan2(s5[1] - s1[1], s5[0] - s1[0]); a1 = math.atan2(s5n[1] - s1n[1], s5n[0] - s1n[0])


def stern_tf(p):
    q = rot(p, s1, math.degrees(a1 - a0))
    return (q[0] + s1n[0] - s1[0], q[1] + s1n[1] - s1[1])


add('capsule', smooth([FB_B(*stern_tf(p)) for p in STERN_F + STERN_B], closed=True, t=0.35))
for k in range(5):
    r = rib_side(k, ANGS[k])
    c = cart_side(k, r)
    c[-1] = stern_tf(cart_side(k, rib_side(k))[-1])
    cl = cr(r, n=8)[10:] + cr(c, n=6)[1:]
    add('capsule', line([FB_B(*p) for p in cl]))
# strzałki mostka: wdech – ku przodowi i ku górze, wydech – ku tyłowi i ku dołowi
q0 = FB_B(10.3, 14.0)
f.arrow(f'M{q0[0] - 0.6:.2f},{q0[1] - 1.0:.2f} L{q0[0] - 6.0:.2f},{q0[1] - 3.5:.2f}')
f.arrow(f'M{q0[0] - 5.2:.2f},{q0[1] - 0.1:.2f} L{q0[0] - 0.4:.2f},{q0[1] + 2.1:.2f}', red=True)

# ================================================================ PANEL C – typ brzuszny (z boku)


def FB_C(z, y):
    return (XOC - S * z, YTOP + S * y)


# przednia ściana brzucha (linia środkowa pasma, cm) – wydech i wdech (uwypuklenie głównie powyżej pępka)
YUMB = 42.0
WALL_E = [(9.0, 23.2), (9.6, 27.0), (10.1, 31.0), (10.4, 35.0), (10.5, 39.0), (10.4, 42.0), (10.2, 46.0), (9.8, 50.0),
          (9.3, YCUT + 1.5)]
WALL_I = [(9.0, 23.2), (10.4, 27.0), (11.5, 31.0), (12.1, 35.0), (12.0, 38.5), (11.3, 42.0), (10.7, 46.0), (10.1, 50.0),
          (9.4, YCUT + 1.5)]
DS_I = [(9.0, 22.2), (7.6, 21.8), (4.8, 23.0), (1.6, 23.6), (-1.4, 24.2), (-3.7, 26.0), (-4.9, 28.6), (-5.2, 31.3)]


def post_abd(y):
    return za(y) - depth(y) - 2.0


def abdomen_C():
    # jama brzuszna: od dolnej powierzchni przepony do linii cięcia, od ściany przedniej do tylnej
    top = [(x, y + 0.5) for x, y in cr(DS_E, n=6)]
    front = [(z - 0.6, y) for z, y in cr(WALL_E, n=6) if y > 24.0]
    back = [(post_abd(y), y) for y in (YCUT + 2, 48.0, 44.0, 40.0, 36.0, 32.5)]
    pts = [FB_C(*p) for p in front] + [FB_C(*p) for p in back] + [FB_C(*p) for p in top[::-1]]
    add('organ', poly(pts))
    add('shade', poly(pts))


ribsC = side_panel(FB_C, n_vert=17, abdomen=abdomen_C)
# kość krzyżowa (część górna)
yL5 = BODIES[16][1]
yS = yL5 + 0.8
zA = za(yL5)
sac = [(zA + 0.1, yS), (zA - 1.2, YCUT + 2.5), (zA - 6.4, YCUT + 2.5), (zA - 3.9, yS)]
add('annulus', poly([FB_C(zA - 0.1, yL5), FB_C(zA - depth(yL5) + 0.1, yL5), FB_C(zA - 3.8, yS), FB_C(zA, yS)]))
add('bone', smooth([FB_C(*p) for p in sac], closed=True, t=0.2))
diaphragm_side(FB_C)
# ściana brzucha (mięśnie brzucha) – pasmo; pępek – wcięcie powierzchni przedniej
add('muscle', poly(band([FB_C(*p) for p in WALL_E], 1.2 * S, n=10)))
pu = FB_C(10.4 + 0.62, YUMB)
f.add(f'<path class="cavity" d="M{pu[0] - 0.15:.2f},{pu[1] - 1.1:.2f} L{pu[0] + 0.85:.2f},{pu[1]:.2f} '
      f'L{pu[0] - 0.15:.2f},{pu[1] + 1.1:.2f}"/>')
# wdech: przepona niżej, ściana brzucha uwypuklona
add('capsule', poly(band([FB_C(*p) for p in DS_I], 1.0 * S, n=12)))
add('capsule', smooth([FB_C(z + 0.6, y) for z, y in WALL_I], closed=False))
# strzałki: przepona (w dół / w górę), ściana brzucha (do przodu / do tyłu)
xd = FB_C(2.0, 0)[0]
yE, yI = FB_C(0, 17.4)[1], FB_C(0, 23.4)[1]
f.arrow(f'M{xd - 1.1:.2f},{yE + 1.2:.2f} L{xd - 1.1:.2f},{yI:.2f}')
f.arrow(f'M{xd + 1.2:.2f},{yI - 0.2:.2f} L{xd + 1.2:.2f},{yE + 1.1:.2f}', red=True)
pw = FB_C(12.4, 34.0)
f.arrow(f'M{pw[0] + 0.2:.2f},{pw[1] - 1.2:.2f} L{pw[0] - 4.6:.2f},{pw[1] - 1.2:.2f}')
f.arrow(f'M{pw[0] - 5.0:.2f},{pw[1] + 1.2:.2f} L{pw[0] - 0.2:.2f},{pw[1] + 1.2:.2f}', red=True)

# przycięcie panelu C u dołu
YCLIP = YTOP + S * YCUT
body = ''.join(f.body)
f.body = [f'<defs><clipPath id="cp_typy"><rect x="0" y="0" width="{W}" height="{YCLIP:.2f}"/></clipPath></defs>'
          f'<g clip-path="url(#cp_typy)">{body}</g>']

# ================================================================ nagłówki
XB_C = 74.0                              # środek kolumny B
XC_C = 121.0                             # środek kolumny C
f.text(51.0, 5.6, 'typ żebrowy (piersiowy)', cls='big', anchor='middle')
f.text(51.0, 9.3, 'poruszają się żebra', cls='notec')
f.text(XC_C, 5.6, 'typ brzuszny (przeponowy)', cls='big', anchor='middle')
f.text(XC_C, 9.3, 'bez bezpośredniego udziału żeber', cls='notec')
f.text(CXA, 15.4, 'oddychanie żebrowe dolne', cls='pl', anchor='middle')
f.text(CXA, 18.7, 'mechanizm żebrowo-przeponowy · od przodu', cls='notec')
f.text(XB_C, 15.4, 'oddychanie żebrowe górne', cls='pl', anchor='middle')
f.text(XB_C, 18.7, 'mechanizm żebrowo-mostkowy · z boku', cls='notec')
f.text(XC_C, 15.4, 'oddychanie brzuszne', cls='pl', anchor='middle')
f.text(XC_C, 18.7, 'przepona i ściana brzucha · z boku', cls='notec')

# ================================================================ opisy pod panelami
NY = 91.2
for x, lines in ((CXA, ['dolne żebra unoszą się i silnie odchylają', 'ku bokom – dolna część klatki poszerza się;',
                        'przewietrza głównie dolne części płuc']),
                 (XB_C, ['górne żebra unoszą się wraz z mostkiem;', 'gdy dolna część klatki jest ograniczona',
                         'w ruchach (np. pasek); przewietrza', 'silniej górne części płuc']),
                 (XC_C, ['przepona obniża się, zawartość jamy brzusznej', 'uwypukla przednią ścianę brzucha, głównie',
                         'powyżej pępka; wydech: przepona wpukla się', 'do klatki (sprężystość płuc, mięśnie brzucha)'])):
    for i, t in enumerate(lines):
        f.text(x, NY + i * 2.7, t, cls='notec')
f.text(W / 2, 103.0, 'oddychanie spokojne – zazwyczaj czysty typ brzuszny · oddech wzmożony – typ mieszany '
                     '(żebrowo-przeponowy)', cls='notec')

# ================================================================ legenda (pod panelem A)
LX, LY = 6.0, 75.0
f.add(f'<rect class="bone" x="{LX:.2f}" y="{LY - 1.6:.2f}" width="5.2" height="2.2" rx=".5"/>')
f.text(LX + 6.6, LY + 0.3, 'położenie przy wydechu')
f.add(f'<path class="capsule" d="M{LX:.2f},{LY + 2.6:.2f} L{LX + 5.4:.2f},{LY + 2.6:.2f}"/>')
f.text(LX + 6.6, LY + 3.4, 'położenie przy wdechu')
f.arrow(f'M{LX:.2f},{LY + 5.7:.2f} L{LX + 5.4:.2f},{LY + 5.7:.2f}')
f.text(LX + 6.6, LY + 6.5, 'ruch przy wdechu')
f.arrow(f'M{LX:.2f},{LY + 8.8:.2f} L{LX + 5.4:.2f},{LY + 8.8:.2f}', red=True)
f.text(LX + 6.6, LY + 9.6, 'ruch przy wydechu')

# ================================================================ podpisy
f.label(FA(8.3, 25.0, -1), 'łuk żebrowy', 'arcus costalis', (3.5, 66.0), side='R')
f.label(FAs(-8.4, 18.6), 'przepona', 'diaphragma', (52.5, 66.0), side='L')
f.label(FB_B(9.75, 19.2), 'mostek', 'sternum', (56.0, 73.5), side='R')
f.label(FB_B(1.5, 7.4), 'żebra', 'costae', (86.5, 33.0), side='R')
f.label(FB_C(-4.9, 25.5), 'przepona', 'diaphragma', (126.0, 52.5), side='R')
f.label(FB_C(-2.1, 40.0), 'jama brzuszna', 'cavitas abdominalis', (126.0, 72.0), side='R')
f.label(FB_C(11.0, YUMB), 'pępek', 'umbilicus', (95.5, 73.5), side='L')
f.label(FB_C(10.3, 46.5), 'przednia ściana brzucha', None, (95.5, 81.5), side='L')

f.save()
print('ok')
