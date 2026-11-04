# STAWY MOSTKOWO-ŻEBROWE – mostek z mostkowymi końcami chrząstek żebrowych I–VII, widok od przodu.
# Prawa strona ciała (po lewej stronie rysunku) – nienaruszona: więzadła promieniste mostkowo-żebrowe (przednie), splatające się
# w błonę mostka, i więzadła żebrowo-mieczykowe. Lewa strona ciała (po prawej stronie rysunku) – przednia warstwa zdjęta (przekrój
# czołowy): chrząstkozrost mostkowo-żebrowy żebra I, stawy mostkowo-żebrowe II–VII z jamami stawowymi, więzadło śródstawowe
# mostkowo-żebrowe w stawie chrząstki II (od przyśrodkowego końca chrząstki do połączenia rękojeści z trzonem – dzieli jamę na dwie
# komory), chrząstkozrosty mostkowe w przekroju.
# Schemat własny wg opisu Bochenka, t. I, s. 285–287 (ryc. 193 oglądana tylko dla położenia struktur). Zarys mostka – jak w rysunku
# mostek_przod (w skali 0,9). Nazwy z k_polaczenia.json (karty: Stawy mostkowo-żebrowe, Chrząstkozrost mostkowo-żebrowy żebra I).
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 150, 100
C = 75.0          # oś (płaszczyzna pośrodkowa)
K = 0.9           # skala względem rysunku mostek_przod
Y0 = 2.6          # przesunięcie w pionie
f = Fig('pol_mostkowo_zebrowe', W, H,
        caption='stawy mostkowo-żebrowe · widok od przodu · po lewej stronie ciała (z prawej na rysunku) przednia warstwa zdjęta')


def poly(pts, closed=True):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + (' Z' if closed else '')


def cr1d(ctrl, y):
    ys = [c[0] for c in ctrl]
    if y <= ys[0]:
        return ctrl[0][1]
    if y >= ys[-1]:
        return ctrl[-1][1]
    i = max(k for k in range(len(ys) - 1) if ys[k] <= y)
    p0 = ctrl[max(i - 1, 0)][1]; p1 = ctrl[i][1]; p2 = ctrl[i + 1][1]; p3 = ctrl[min(i + 2, len(ctrl) - 1)][1]
    u = (y - ys[i]) / (ys[i + 1] - ys[i])
    return 0.5 * ((2 * p1) + (-p0 + p2) * u + (2 * p0 - 5 * p1 + 4 * p2 - p3) * u * u + (-p0 + 3 * p1 - 3 * p2 + p3) * u ** 3)


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


# ---------------- geometria mostka (jednostki rysunku mostek_przod: x względem osi, y od góry) ----------------
Y_J1, Y_J2 = 32.3, 34.1      # górne połączenie mostkowe
Y_X1, Y_X2 = 83.2, 84.8      # dolne połączenie mostkowe
NOTCH = {'II': (33.2, 3.0, 1.15), 'III': (44.6, 2.6, 1.15), 'IV': (55.6, 2.6, 1.15), 'V': (65.6, 2.6, 1.15),
         'VI': (74.2, 2.4, 1.1), 'VII': (84.0, 2.8, 1.1)}
W_MAN = [(28.6, 10.15), (30.0, 9.15), (Y_J1, 8.15)]
W_BODY = [(Y_J2, 7.75), (40, 8.45), (50, 9.25), (60, 9.95), (68, 10.25), (75, 9.85), (80, 8.75), (Y_X1, 7.5)]
W_XI = [(Y_X2, 6.5), (86.5, 6.0), (89, 5.55), (92.5, 4.75), (95.5, 3.55), (97.4, 2.3), (98.5, 1.3)]


def dip(y):
    d = 0.0
    for yc, h, dep in NOTCH.values():
        u = (y - yc) / h
        if abs(u) < 1:
            d = max(d, dep * (1 - u * u) ** 0.62)
    return d


def wfun(y):
    if y <= Y_J1:
        return cr1d(W_MAN, y)
    if y < Y_J2:
        a = cr1d(W_MAN, Y_J1); b = cr1d(W_BODY, Y_J2)
        return a + (b - a) * (y - Y_J1) / (Y_J2 - Y_J1)
    if y <= Y_X1:
        return cr1d(W_BODY, y)
    if y < Y_X2:
        a = cr1d(W_BODY, Y_X1); b = cr1d(W_XI, Y_X2)
        return a + (b - a) * (y - Y_X1) / (Y_X2 - Y_X1)
    return cr1d(W_XI, y)


def edge(y):
    """odległość brzegu bocznego (z wcięciami) od osi"""
    return wfun(y) - dip(y)


def G(x, y):
    """jednostki mostek_przod (x względem osi) → rysunek"""
    return (C + K * x, Y0 + K * y)


def GL(pts):
    return [G(x, y) for x, y in pts]


JUG = [(0, 9.35), (-2.4, 9.05), (-4.2, 8.4), (-5.4, 7.95)]
CLAV = [(-6.5, 7.8), (-7.9, 8.45), (-9.5, 9.5), (-11.2, 10.5), (-12.7, 11.2)]
LAT = [(-13.75, 11.85), (-14.35, 13.0), (-14.55, 15.0), (-14.35, 17.6), (-14.5, 20.2), (-14.1, 21.9), (-12.6, 24.9), (-10.6, 28.0)]


def border(y0, y1, step=0.25):
    pts = []
    n = int(round((y1 - y0) / step))
    for k in range(n + 1):
        y = y0 + (y1 - y0) * k / n
        pts.append((-edge(y), y))
    return pts


man_half = bez(JUG + CLAV + LAT, n=10) + border(28.6, Y_J1)
body_half = border(Y_J2, Y_X1)
xi_half = border(Y_X2, 89.0) + bez([(-5.55, 89.0), (-4.75, 92.5), (-3.6, 95.4), (-2.1, 97.6), (-0.85, 98.85), (0, 99.2)], n=10)[1:]


def full(half):
    return half + [(-x, y) for x, y in half[::-1]]


def band_sync(y0, y1):
    n = 12
    L = [(-edge(y0 + (y1 - y0) * k / n), y0 + (y1 - y0) * k / n) for k in range(n + 1)]
    return L + [(-x, y) for x, y in L[::-1]]


# ---------------- chrząstki żebrowe (mostkowe końce, przecięte bocznie) ----------------
# (nazwa, środek przyczepu y, pół-wysokość, kąt odejścia (° w dół), długość, zgięcie)
CART = [('I', 17.6, 4.2, 24, 9.5, 0), ('II', 33.2, 3.1, 2, 10.0, 0), ('III', 44.6, 2.7, 5, 10.0, 0),
        ('IV', 55.6, 2.7, 9, 10.0, 0), ('V', 65.6, 2.7, 15, 10.0, 0), ('VI', 74.2, 2.6, 25, 10.0, -1.0),
        ('VII', 84.0, 2.8, 35, 10.0, -2.0)]


def cart_poly(name, yc, hh, ang, L, bend, side, inset):
    """chrząstka po stronie side (-1 – lewa strona rysunku, +1 – prawa); inset – przesunięcie końca przyśrodkowego
    względem brzegu wcięcia (<0 – wsunięty pod brzeg mostka, >0 – odsunięty o szerokość jamy stawowej)"""
    # koniec przyśrodkowy – wzdłuż wcięcia (lub wcięcia żebrowego I – pionowy brzeg rękojeści)
    n = 14
    med = []
    for k in range(n + 1):
        y = yc - hh + 2 * hh * k / n
        if name == 'I':
            x = edge(y) - 0.2
        else:
            x = edge(y)
        med.append((side * (x + inset), y))
    a = math.radians(ang)
    d = (side * math.cos(a), math.sin(a))
    nrm = (-d[1] * side, d[0] * side)                     # „w dół” względem osi chrząstki
    # oś chrząstki: od środka końca przyśrodkowego, z łagodnym zgięciem w dół
    x0 = side * wfun(yc)
    axis = []
    for k in range(9):
        t = k / 8
        s = L * t / K
        axis.append((x0 + d[0] * s, yc + d[1] * s + bend * t * t))
    top, bot = [], []
    for i, (x, y) in enumerate(axis):
        hw = hh * (1 - 0.12 * i / 8)
        # kierunek lokalny
        j0, j1 = axis[max(i - 1, 0)], axis[min(i + 1, 8)]
        tx, ty = j1[0] - j0[0], j1[1] - j0[1]
        Lt = math.hypot(tx, ty)
        nx, ny = -ty / Lt * side, tx / Lt * side
        if side < 0:
            nx, ny = -nx, -ny
        # nx, ny – normalna skierowana ku dołowi
        if ny < 0:
            nx, ny = -nx, -ny
        top.append((x - nx * hw, y - ny * hw))
        bot.append((x + nx * hw, y + ny * hw))
    pts = med + bot[1:] + top[::-1][:-1]
    return pts, axis, top, bot


# ======================================================================= rysowanie
# 1. chrząstki – strona nienaruszona (lewa na rysunku) i przecięta (prawa)
CARTS = {}
for name, yc, hh, ang, L, bend in CART:
    for side in (-1, 1):
        inset = -0.6 if side < 0 or name == 'I' else 0.55
        if name == 'I' and side > 0:
            inset = -0.4
        pts, axis, top, bot = cart_poly(name, yc, hh, ang, L, bend, side, inset)
        CARTS[(name, side)] = (pts, axis, top, bot)
        f.add(f'<path class="cart" d="{poly(GL(pts))}"/>')
        # powierzchnia przecięcia chrząstki (koniec boczny)
        e0, e1 = top[-1], bot[-1]
        mx, my = (e0[0] + e1[0]) / 2, (e0[1] + e1[1]) / 2
        cx, cy = G(mx, my)
        rr = math.hypot(e1[0] - e0[0], e1[1] - e0[1]) / 2 * K
        angd = math.degrees(math.atan2((e1[1] - e0[1]), (e1[0] - e0[0])))
        f.add(f'<ellipse class="cart" cx="{cx:.2f}" cy="{cy:.2f}" rx="{rr:.2f}" ry="{rr * 0.36:.2f}" transform="rotate({angd:.1f} {cx:.2f} {cy:.2f})"/>')

# 2. mostek: chrząstkozrosty mostkowe (pod kośćmi), części mostka
f.add(f'<path class="cart" d="{poly(GL(band_sync(Y_J1 - 0.5, Y_J2 + 0.5)))}"/>')
f.add(f'<path class="cart" d="{poly(GL(band_sync(Y_X1 - 0.5, Y_X2 + 0.5)))}"/>')
for half in (man_half, body_half, xi_half):
    f.add(f'<path class="bone" d="{poly(GL(full(half)))}"/>')

# 3. strona przecięta (prawa na rysunku): powierzchnia przekroju kości, chrząstkozrosty w przekroju, jamy stawowe
f.add(f'<defs><clipPath id="cp_mz_r"><rect x="{C:.2f}" y="0" width="{W - C:.2f}" height="{H:.2f}"/></clipPath></defs>')
f.add('<g clip-path="url(#cp_mz_r)">')
for half in (man_half, body_half, xi_half):
    f.add(f'<path class="bone2" d="{poly(GL(full(half)))}"/>')
# warstwa chrząstki szklistej na powierzchniach części mostka + płytka włóknista (w przekroju jedna warstwa chrząstki)
f.add(f'<path class="cart" d="{poly(GL(band_sync(Y_J1 - 0.35, Y_J2 + 0.35)))}"/>')
f.add(f'<path class="cart" d="{poly(GL(band_sync(Y_X1 - 0.35, Y_X2 + 0.35)))}"/>')
f.add('</g>')
# stawy II–VII (prawa strona rysunku): chrząstka stawowa wcięcia, jama stawowa (szczelina), koniec chrząstki żebrowej
GAPW = 0.55
for name, (yc, h, dep) in NOTCH.items():
    ys = [yc - h * 0.98 + 2 * h * 0.98 * k / 30 for k in range(31)]
    s_edge = [(edge(y), y) for y in ys]
    lining = [(edge(y) - 0.5 * math.sin(math.pi * k / 30) ** 0.5, y) for k, y in enumerate(ys)]
    f.add(f'<path class="facet" d="{poly(GL(s_edge + lining[::-1]))}"/>')
    cav = [(edge(y) + GAPW * math.sin(math.pi * k / 30) ** 0.6, y) for k, y in enumerate(ys)]
    f.add(f'<path class="cavity" d="{poly(GL(s_edge + cav[::-1]))}"/>')
# więzadło śródstawowe w stawie chrząstki II – od przyśrodkowego końca chrząstki do połączenia rękojeści z trzonem
yc2 = NOTCH['II'][0]
xe = edge(yc2)
f.add(f'<path class="lig" d="{poly(GL([(xe - 1.6, yc2 - 0.55), (xe + GAPW + 0.9, yc2 - 0.42), (xe + GAPW + 0.9, yc2 + 0.42), (xe - 1.6, yc2 + 0.55)]))}"/>')
# chrząstkozrost żebra I (prawa strona rysunku) – chrząstka zlewa się z rękojeścią (bez jamy stawowej): chrząstka wnika we wcięcie
pts, axis, top, bot = cart_poly('I', 17.6, 4.2, 24, 9.5, 0, 1, -0.9)
f.add(f'<path class="cart" d="{poly(GL(pts))}"/>')
e0, e1 = top[-1], bot[-1]
cx, cy = G((e0[0] + e1[0]) / 2, (e0[1] + e1[1]) / 2)
rr = math.hypot(e1[0] - e0[0], e1[1] - e0[1]) / 2 * K
angd = math.degrees(math.atan2((e1[1] - e0[1]), (e1[0] - e0[0])))
f.add(f'<ellipse class="cart" cx="{cx:.2f}" cy="{cy:.2f}" rx="{rr:.2f}" ry="{rr * 0.36:.2f}" transform="rotate({angd:.1f} {cx:.2f} {cy:.2f})"/>')

# 4. strona nienaruszona (lewa na rysunku): więzadła promieniste mostkowo-żebrowe → błona mostka; więzadła żebrowo-mieczykowe
# błona mostka – pasmo splecionych włókien wzdłuż linii pośrodkowej (przecięte w płaszczyźnie pośrodkowej)
mem = [(-3.6, 29.0), (-3.0, 40.0), (-3.4, 52.0), (-3.6, 64.0), (-3.0, 76.0), (-1.6, 80.6), (0.0, 80.6), (0.0, 29.0)]
f.add(f'<path class="lig" d="{smooth(GL(mem[:6]), closed=False)} L{G(0.0, 80.6)[0]:.2f},{G(0.0, 80.6)[1]:.2f} L{G(0.0, 29.0)[0]:.2f},{G(0.0, 29.0)[1]:.2f} Z"/>')
for y0 in range(31, 78, 4):
    f.add(f'<path class="bonel" d="{poly(GL([(-3.0, y0), (0.0, y0 + 3.0)]), closed=False)}"/>')
    f.add(f'<path class="bonel" d="{poly(GL([(-3.0, y0 + 3.0), (0.0, y0)]), closed=False)}"/>')
# więzadła promieniste mostkowo-żebrowe (przednie): od mostkowych końców chrząstek II–VII rozbieżnie na mostek, ku błonie mostka
for name, yc, hh, ang, L, bend in CART[1:]:
    xe = -wfun(yc)
    spread = hh + (1.8 if name != 'VII' else 0.9)
    fan = [(xe - 1.6, yc - hh * 0.75), (xe + 0.6, yc - hh * 0.95), (-3.2, yc - spread), (-2.4, yc - spread * 0.3),
           (-2.4, yc + spread * 0.3), (-3.2, yc + spread), (xe + 0.6, yc + hh * 0.95), (xe - 1.6, yc + hh * 0.75)]
    f.add(f'<path class="lig" d="{smooth(GL(fan))}"/>')
    for v in (-0.66, -0.22, 0.22, 0.66):
        f.add(f'<path class="bonel" d="{poly(GL([(xe - 1.0, yc + v * hh * 0.8), (-2.8, yc + v * spread * 1.2)]), closed=False)}"/>')
# więzadła żebrowo-mieczykowe: z dolnego końca trzonu i przedniej powierzchni chrząstek VI–VII skośnie w dół na przód wyrostka
for (a0, a1, b0, b1) in [((-6.9, 80.6), (-5.9, 82.8), (-2.1, 88.0), (-1.2, 89.8)),
                         ((-11.4, 85.8), (-10.4, 88.0), (-3.0, 90.4), (-2.5, 92.0))]:
    shp = [a0, ((a0[0] + b0[0]) / 2, (a0[1] + b0[1]) / 2 - 0.1), b0, b1, ((a1[0] + b1[0]) / 2, (a1[1] + b1[1]) / 2 + 0.1), a1]
    f.add(f'<path class="lig" d="{smooth(GL(shp))}"/>')
    f.add(f'<path class="bonel" d="{poly(GL([((a0[0] + a1[0]) / 2, (a0[1] + a1[1]) / 2), ((b0[0] + b1[0]) / 2, (b0[1] + b1[1]) / 2)]), closed=False)}"/>')

# numery chrząstek (przy końcach bocznych)
for name, yc, hh, ang, L, bend in CART:
    pts, axis, top, bot = CARTS[(name, 1)]
    x, y = axis[6]
    cx, cy = G(x, y)
    f.text(cx, cy + 0.75, name, cls='notec')

# ======================================================================= podpisy
TL, TR = 54.0, 95.6
# lewa strona rysunku (prawa strona ciała – nienaruszona)
f.label(G(-7.0, 17.0), 'rękojeść mostka', 'manubrium sterni', (TL, 12.0), side='L')
f.label(G(-17.6, 20.6), 'chrząstka żebrowa', 'cartilago costalis', (TL - 1.0, 22.0), side='L')
f.label(G(-6.6, 44.6), 'więzadło promieniste mostkowo-żebrowe', 'ligamentum sternocostale radiatum', (TL + 1.0, 36.0), side='L')
f.label(G(-1.2, 52.6), 'błona mostka', 'membrana sterni', (TL + 1.0, 48.0), side='L')
f.label(G(-6.9, 89.0), 'więzadła żebrowo-mieczykowe', 'ligamenta costoxiphoidea', (TL + 1.0, 79.5), side='L')
f.label(G(-1.6, 96.0), 'wyrostek mieczykowaty', 'processus xiphoideus', (TL + 2.0, 89.0), side='L')
# prawa strona rysunku (lewa strona ciała – przekrój)
f.label(G(13.4, 17.6), 'chrząstkozrost mostkowo-żebrowy żebra I', 'synchondrosis sternocostalis costae primae', (C + 15.6, 3.6), side='R')
f.label(G(edge(33.2) + 0.2, 33.2), 'więzadło śródstawowe mostkowo-żebrowe', 'ligamentum sternocostale intraarticulare', (TR - 1.8, 27.0), side='R')
f.label(G(edge(44.6) + 0.25, 44.6), 'staw mostkowo-żebrowy', 'articulatio sternocostalis', (TR, 39.0), side='R')
f.label(G(edge(55.6) + 0.25, 56.2), 'jama stawowa', 'cavitas articularis', (TR, 50.0), side='R')
f.label(G(4.0, 62.0), 'trzon mostka', 'corpus sterni', (TR, 61.0), side='R')
f.save()
