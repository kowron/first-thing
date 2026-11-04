# WYMIARY RUCHÓW ŻEBER (mechanika kości żebrowej) – Bochenek, t. I, s. 293–295. Schemat własny.
# Klatka piersiowa od strony lewej (przód w lewo), położenie wydechowe. Strzałki niebieskie = przesunięcie przy wdechu
# (zmierzone na zwłokach, s. 295), długość proporcjonalna do wartości:
#   ku górze – najsilniej żebro IV (ok. 35 mm), najsłabiej I i X (25 mm);
#   bocznie – najsilniej żebra dolne (22 mm), najsłabiej żebro I (10 mm)  [ruch prostopadły do rysunku – tylko liczby];
#   do przodu – maleje od żebra I do V (z ok. 15 do 1 mm), potem ruch ku tyłowi rośnie od żebra VI do X (z 2 do 8 mm).
# Żebra, dla których Bochenek podaje wartości (I, IV, V, VI, X), narysowane w pełni; pozostałe – w tle.
# Typy ruchów (s. 293–294, tekst): I – ruch dokoła szyjki + ruch ślizgowy (ku górze > do przodu > bocznie);
#   II–V – obrót dokoła osi szyjki żebra (tekst: ryc. 199 a, żebro III); ku górze > bocznie > do przodu;
#   VI–X – guzek żebra wsuwa się na wyrostek poprzeczny ku górze i ku tyłowi (tekst: ryc. 199 b, żebro VIII);
#   ku górze > bocznie > nieco ku tyłowi. Żebra XI i XII – ruchy bez większego znaczenia dla mechaniki klatki.
#   (Podpis ryc. 199 przypisuje oba ruchy stronom lewej/prawej ryciny – rysunek trzyma się tekstu.)
# Kształt klatki z boku – geometria jak w figs/src/oddychanie_wymiary.py (skopiowana, większa skala).
import sys, math, os
sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 150, 100
f = Fig('zebra_ruchy_wymiary', W, H,
        caption='żebra przy wdechu – przesunięcia kości żebrowych (na zwłokach) · klatka od strony lewej (przód w lewo)')


# ---------------------------------------------------------------- pomocnicze
def cr(pts, closed=False, n=12, t=0.5):
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
    for i in (range(1, m + 1) if closed else range(1, m)):
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


def poly(pts, close=True):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + (' Z' if close else '')


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
        return [(center[0] + w * math.cos(a0 + math.pi * j / k), center[1] + w * math.sin(a0 + math.pi * j / k)) for j in range(1, k)]
    out = list(left)
    if cap1:
        out += capf(left[-1], right[-1], c[-1], w1 / 2)
    out += right[::-1]
    if cap0:
        out += capf(right[0], left[0], c[0], w0 / 2)
    return out


# ================================================================ klatka z boku (od strony lewej, przód w lewo)
S = 1.85                     # mm rysunku / cm
XO, YB = 84.0, 14.0          # przednia powierzchnia trzonu Th1 (z = 0), górny brzeg Th1 (y = 0)


def FB(z, y):
    """z – w przód od przedniej powierzchni trzonu Th1 (cm, + ku przodowi = w lewo), y – w dół (cm)"""
    return (XO - S * z, YB + S * y)


def za(y):
    if y <= 30:
        return -2.2 * math.sin(math.pi * y / 30)
    return 0.25 * (y - 30)


def depth(y):
    return 2.0 + 1.3 * min(max(y, 0), 36) / 30


bodies = []
y = 0.0
for k in range(13):
    h = 1.95 + 0.045 * k if k < 12 else 2.6
    disc = 0.5 if k < 11 else 0.8
    bodies.append((y, y + h))
    y += h + disc


def body_path(yt, yb, r=0.35):
    fa, fb = za(yt), za(yb)
    pts = [(fa, yt + r), (fa - r * 0.6, yt), (fa - depth(yt) + r * 0.6, yt), (fa - depth(yt), yt + r),
           (fb - depth(yb), yb - r), (fb - depth(yb) + r * 0.6, yb), (fb - r * 0.6, yb), (fb, yb - r)]
    return smooth([FB(*p) for p in pts], closed=True, t=0.3)


for i in range(len(bodies) - 1):
    yt, yb = bodies[i][1], bodies[i + 1][0]
    pts = [(za(yt) - 0.1, yt), (za(yt) - depth(yt) + 0.1, yt), (za(yb) - depth(yb) + 0.1, yb), (za(yb) - 0.1, yb)]
    f.add(f'<path class="annulus" d="{poly([FB(*p) for p in pts])}"/>')
for yt, yb in bodies:
    f.add(f'<path class="bone" d="{body_path(yt, yb)}"/>')

YH = [0.9] + [(k - 1) * 2.45 + 0.4 for k in range(2, 13)]
DROP = [3.9, 5.2, 6.2, 6.6, 7.0, 7.4, 7.8, 7.8, 7.6, 7.0, 5.0, 3.6]
ZE = [4.4, 5.8, 6.6, 7.1, 7.5, 7.7, 7.6, 7.0, 6.2, 5.2, 1.0, -3.4]
ZANG = [-3.2, -4.3] + [-5.0] * 8 + [-4.8, -4.4]


def rib_side(k):
    yh = YH[k]
    zh = za(yh) - 1.3
    if k == 10:                       # żebro XI – krótsze, koniec wolny
        return [(zh, yh), (zh - 1.6, yh - 0.05), (za(yh) - 6.2, yh + 0.5), (za(yh) - 6.3, yh + 1.8), (za(yh) - 4.6, yh + 3.6),
                (za(yh) - 1.8, yh + 4.9), (za(yh) + 0.6, yh + 5.4)]
    if k == 11:                       # żebro XII – najkrótsze, koniec wolny
        return [(zh, yh), (zh - 1.5, yh - 0.05), (za(yh) - 5.6, yh + 0.6), (za(yh) - 5.6, yh + 1.9), (za(yh) - 4.6, yh + 3.2),
                (za(yh) - 3.4, yh + 3.9)]
    zg = za(yh) + ZANG[k]
    d, ze = DROP[k], ZE[k]
    return [(zh, yh), (zh - 1.6, yh - 0.05), (zg + 0.35, yh + 0.35), (zg - 0.05, yh + 1.3), (zg + (ze - zg) * 0.16, yh + 0.40 * d),
            (zg + (ze - zg) * 0.52, yh + 0.80 * d), (ze, yh + d)]


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


KEY = {0, 3, 4, 5, 9}                    # żebra I, IV, V, VI, X – z wartościami u Bochenka
RIBS = [rib_side(k) for k in range(12)]
for k in range(11, -1, -1):
    pts = [FB(*p) for p in RIBS[k]]
    w0, w1 = 0.75 * S, (1.05 if k < 10 else 0.75) * S
    c = cart_side(k, RIBS[k])
    if c:
        f.add(f'<path class="cart" d="{poly(band([FB(*p) for p in c], 0.85 * S, 0.75 * S, cap1=(k >= 7)))}"/>')
    f.add(f'<path class="bone" d="{poly(band(pts, w0, w1, n=14, cap0=True, cap1=(k >= 10)))}"/>')

st = STERN_F + STERN_B
f.add(f'<path class="bone" d="{smooth([FB(*p) for p in st], closed=True, t=0.35)}"/>')
for y in (8.95, 19.7):
    a, b = FB(stern_back(y) + 0.05, y), FB(STERN_F[3][0] if y < 10 else 10.1, y)
    f.add(f'<path class="bonel" d="M{a[0]:.2f},{a[1]:.2f} L{b[0]:.2f},{b[1]:.2f}"/>')

# numery żeber przy końcach przednich kości żebrowych (w tle – przy wszystkich)
ROM = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']

# ================================================================ strzałki przesunięć (koniec przedni kości żebrowej)
K = 0.36                     # mm strzałki na 1 mm przesunięcia
END = {k: FB(*RIBS[k][-1]) for k in range(12)}


def up(k, mm, dx=0.0):
    x, y = END[k]
    f.arrow(f'M{x + dx:.2f},{y - 0.6:.2f} L{x + dx:.2f},{y - 0.6 - mm * K:.2f}')


def horiz(k, mm, sign, dy=0.0):        # sign = -1 do przodu (w lewo), +1 ku tyłowi (w prawo)
    x, y = END[k]
    f.arrow(f'M{x + sign * 0.6:.2f},{y + dy:.2f} L{x + sign * (0.6 + mm * K):.2f},{y + dy:.2f}')


up(0, 25); horiz(0, 15, -1)
up(3, 35, dx=0.9)
up(9, 25); horiz(9, 8, +1)

# ================================================================ klamry typów ruchu (przy stawach żebrowo-kręgowych)
XBR = 100.0


def vbracket(y0, y1, x=XBR, tick=1.1):
    f.add(f'<path class="lead" d="M{x - tick:.2f},{y0:.2f} L{x:.2f},{y0:.2f} L{x:.2f},{y1:.2f} L{x - tick:.2f},{y1:.2f}"/>')
    return (x, (y0 + y1) / 2)


HEAD = {k: FB(*RIBS[k][0]) for k in range(12)}
bI = vbracket(HEAD[0][1] - 1.4, HEAD[0][1] + 1.9)
bII = vbracket(HEAD[1][1] - 0.7, HEAD[4][1] + 1.9)
bVI = vbracket(HEAD[5][1] - 1.0, HEAD[9][1] + 2.1)
bXI = vbracket(HEAD[10][1] - 1.3, HEAD[11][1] + 2.0)

# ================================================================ podpisy
TL, TR = 50.0, 104.0


def notes(x, y, lines, side):
    for k, t in enumerate(lines):
        f.text(x + (0.7 if side == 'R' else -0.7), y + 6.6 + 2.6 * k, t, cls='note', anchor='start' if side == 'R' else 'end')


def notes1(x, y, lines, side):      # podpis bez łaciny – notatki tuż pod nazwą
    notes(x, y - 2.9, lines, side)


f.label(END[0], 'żebro I', 'costa I', (TL, 11.0), side='L')
notes(TL, 11.0, ['ku górze 25 mm (najsłabiej)', 'do przodu ok. 15 mm', 'bocznie 10 mm (najsłabiej)'], 'L')
f.label(END[3], 'żebro IV', 'costa IV', (TL, 29.0), side='L')
notes(TL, 29.0, ['ku górze ok. 35 mm (najsilniej)'], 'L')
f.label(END[4], 'żebro V', 'costa V', (TL, 40.0), side='L')
notes(TL, 40.0, ['do przodu ok. 1 mm'], 'L')
f.label(END[5], 'żebro VI', 'costa VI', (TL, 51.0), side='L')
notes(TL, 51.0, ['ku tyłowi 2 mm'], 'L')
f.label(END[9], 'żebro X', 'costa X', (TL, 62.0), side='L')
notes(TL, 62.0, ['ku górze 25 mm (najsłabiej)', 'ku tyłowi 8 mm', 'bocznie: najsilniej żebra dolne (22 mm)'], 'L')

f.label(bI, 'typ żebra I', None, (TR, 10.0), side='R')
notes1(TR, 10.0, ['ruch dokoła szyjki i ślizgowy względem', 'wyrostka poprzecznego;', 'ku górze > do przodu > bocznie'], 'R')
f.label(bII, 'typ żeber II–V', None, (TR, 26.0), side='R')
notes1(TR, 26.0, ['obrót dokoła osi szyjki żebra (np. żebro III);', 'ku górze > bocznie > do przodu'], 'R')
f.label(bVI, 'typ żeber VI–X', None, (TR, 41.5), side='R')
notes1(TR, 41.5, ['guzek żebra wsuwa się na wyrostek', 'poprzeczny ku górze i ku tyłowi', '(np. żebro VIII);',
                  'ku górze > bocznie > nieco ku tyłowi'], 'R')
f.label(bXI, 'żebra wolne', 'costae fluitantes', (TR, 60.0), side='R')
notes(TR, 60.0, ['XI i XII – ruchy bez większego znaczenia', 'dla mechaniki klatki piersiowej'], 'R')

# ================================================================ legenda
LY = 84.5
lx = 22.0
f.arrow(f'M{lx:.2f},{LY - 0.6:.2f} L{lx + 7.0:.2f},{LY - 0.6:.2f}')
f.text(lx + 8.6, LY + 0.2, 'przesunięcie przy wdechu (na zwłokach); długość strzałki proporcjonalna do wartości', cls='note')
f.text(lx + 8.6, LY + 2.9, 'do przodu – maleje od żebra I do V, potem przechodzi w ruch ku tyłowi, rosnący od żebra VI do X', cls='note')
f.text(lx + 8.6, LY + 5.6, 'ruch boczny – prostopadle do płaszczyzny rysunku (podano tylko liczby)', cls='note')
f.text(lx + 8.6, LY + 8.3, 'im dalej ku tyłowi leży punkt kości żebrowej, tym mniejszy zakres jego ruchu', cls='note')
sb0 = lx + 98.0
f.add(f'<path class="lead" d="M{sb0:.2f},{LY - 1.4:.2f} L{sb0:.2f},{LY - 0.6:.2f} L{sb0 + 10 * K:.2f},{LY - 0.6:.2f} L{sb0 + 10 * K:.2f},{LY - 1.4:.2f}"/>')
f.text(sb0 + 10 * K + 1.0, LY + 0.2, '10 mm', cls='note')

if os.environ.get('PTS'):
    for k in range(12):
        print(ROM[k], [round(v, 1) for v in END[k]], 'head', [round(v, 1) for v in FB(*RIBS[k][0])])
f.save()
