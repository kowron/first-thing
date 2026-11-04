# MOSTEK – widok od przodu (prawa strona ciała po lewej stronie rysunku; mostek symetryczny)
# Nazwy wg Bochenka, t. I, s. 278–281 (ryc. 187) i s. 287 (połączenia części mostka).
import sys; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
import math
from figlib import Fig, smooth, mirror

C = 65.0          # oś symetrii
DY = 3.5          # przesunięcie całego mostka w dół (miejsce na podpis wcięcia szyjnego)
f = Fig('mostek_przod', 130, 108, caption='mostek · widok od przodu')

Y_J1, Y_J2 = 32.3, 34.1      # górne połączenie mostkowe (rękojeść / trzon)
Y_X1, Y_X2 = 83.2, 84.8      # dolne połączenie mostkowe (trzon / wyrostek)


def cr1d(ctrl, y):
    """gładka interpolacja (Catmull-Rom) funkcji w(y) zadanej punktami (y, w)"""
    ys = [c[0] for c in ctrl]
    if y <= ys[0]:
        return ctrl[0][1]
    if y >= ys[-1]:
        return ctrl[-1][1]
    i = max(k for k in range(len(ys) - 1) if ys[k] <= y)
    p0 = ctrl[max(i - 1, 0)][1]; p1 = ctrl[i][1]; p2 = ctrl[i + 1][1]; p3 = ctrl[min(i + 2, len(ctrl) - 1)][1]
    u = (y - ys[i]) / (ys[i + 1] - ys[i])
    return 0.5 * ((2 * p1) + (-p0 + p2) * u + (2 * p0 - 5 * p1 + 4 * p2 - p3) * u * u + (-p0 + 3 * p1 - 3 * p2 + p3) * u ** 3)


# wcięcia żebrowe: (środek y, pół-długość, głębokość)
NOTCH = {'II': (33.2, 3.0, 1.15), 'III': (44.6, 2.6, 1.15), 'IV': (55.6, 2.6, 1.15), 'V': (65.6, 2.6, 1.15),
         'VI': (74.2, 2.4, 1.1), 'VII': (84.0, 2.8, 1.1)}


def dip(y):
    """głębokość wcięcia żebrowego (wklęsłość półeliptyczna z łagodnie zaokrąglonymi brzegami)"""
    d = 0.0
    for yc, h, dep in NOTCH.values():
        u = (y - yc) / h
        if abs(u) < 1:
            d = max(d, dep * (1 - u * u) ** 0.62)
    return d


W_BODY = [(Y_J2, 7.75), (40, 8.45), (50, 9.25), (60, 9.95), (68, 10.25), (75, 9.85), (80, 8.75), (Y_X1, 7.5)]
W_XI = [(Y_X2, 6.5), (86.5, 6.0), (89, 5.55), (92.5, 4.75), (95.5, 3.55), (97.4, 2.3), (98.5, 1.3)]


def border(y0, y1, wctrl, step=0.25):
    pts = []
    n = int(round((y1 - y0) / step))
    for k in range(n + 1):
        y = y0 + (y1 - y0) * k / n
        pts.append((-(cr1d(wctrl, y) - dip(y)), y))
    return pts


def A(pts, s=-1):
    """lewa połowa (x względem osi) → bezwzględne; s=+1 – odbicie na prawą stronę"""
    return [(C + (x if s < 0 else -x), y + DY) for x, y in pts]


def poly(pts):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + ' Z'


def bez(pts, t=0.5, n=14):
    """próbkowanie krzywej rysowanej przez smooth() (otwartej)"""
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


# ---------- rękojeść (lewa połowa, od środka wcięcia szyjnego) ----------
JUG = [(0, 9.35), (-2.4, 9.05), (-4.2, 8.4), (-5.4, 7.95)]
CLAV = [(-6.5, 7.8), (-7.9, 8.45), (-9.5, 9.5), (-11.2, 10.5), (-12.7, 11.2)]
LAT = [(-13.75, 11.85), (-14.35, 13.0), (-14.55, 15.0), (-14.35, 17.6), (-14.5, 20.2), (-14.1, 21.9),
       (-12.6, 24.9), (-10.6, 28.0)]
man_top = bez(JUG + CLAV + LAT, n=10)
man_low = border(28.6, Y_J1, [(28.6, 10.15), (30.0, 9.15), (Y_J1, 8.15)])
man_half = man_top + man_low
man = A(man_half) + A(man_half, +1)[::-1]

body_half = border(Y_J2, Y_X1, W_BODY)
body = A(body_half) + A(body_half, +1)[::-1]
# delikatne zaokrąglenie dolnego brzegu trzonu i górnego wyrostka – wystarczy prosta krawędź
xi_half = border(Y_X2, 89.0, W_XI) + bez([(-5.55, 89.0), (-4.75, 92.5), (-3.6, 95.4), (-2.1, 97.6), (-0.85, 98.85), (0, 99.2)], n=10)[1:]
xi = A(xi_half) + A(xi_half, +1)[::-1]

def wfun_all(y):
    if y <= Y_J1:
        return cr1d([(28.6, 10.15), (30.0, 9.15), (Y_J1, 8.15)], y)
    if y < Y_J2:   # w chrząstce – interpolacja między rękojeścią a trzonem
        a = cr1d([(28.6, 10.15), (30.0, 9.15), (Y_J1, 8.15)], Y_J1)
        b = cr1d(W_BODY, Y_J2)
        return a + (b - a) * (y - Y_J1) / (Y_J2 - Y_J1)
    if y <= Y_X1:
        return cr1d(W_BODY, y)
    if y < Y_X2:
        a = cr1d(W_BODY, Y_X1); b = cr1d(W_XI, Y_X2)
        return a + (b - a) * (y - Y_X1) / (Y_X2 - Y_X1)
    return cr1d(W_XI, y)


# chrząstkozrosty mostkowe – warstwa chrząstki między częściami (rysowana pod kośćmi; brzegi wzdłuż wcięć II i VII)
def band(y0, y1):
    n = 12
    L = [(-(wfun_all(y0 + (y1 - y0) * k / n) - dip(y0 + (y1 - y0) * k / n)), y0 + (y1 - y0) * k / n) for k in range(n + 1)]
    return poly(A(L) + A(L, +1)[::-1])


f.add(f'<path class="cart" d="{band(Y_J1 - 0.5, Y_J2 + 0.5)}"/>')
f.add(f'<path class="cart" d="{band(Y_X1 - 0.5, Y_X2 + 0.5)}"/>')

for part in (man, body, xi):
    f.add(f'<path class="bone" d="{poly(part)}"/>')


def lens_y(yc, h, wfun, depth, s, y_lo=None, y_hi=None):
    """powierzchnia wcięcia (sierp) wzdłuż brzegu bocznego, y od yc-h do yc+h"""
    ya, yb = yc - h * 0.98, yc + h * 0.98
    n = 40
    outer, inner = [], []
    for k in range(n + 1):
        y = ya + (yb - ya) * k / n
        x = -(wfun(y) - dip(y))
        u = k / n
        outer.append((x, y))
        inner.append((x + depth * min(1.0, 3.2 * math.sin(math.pi * u)), y))
    return poly(A(outer + inner[::-1], s))


# wcięcia obojczykowe (pokryte chrząstką włóknistą – do połączenia z obojczykiem)
for s in (-1, 1):
    a = bez(CLAV, n=12)
    m = len(a)
    inner = [(x + 0.75 * math.sin(math.pi * i / (m - 1)), y + 1.25 * math.sin(math.pi * i / (m - 1))) for i, (x, y) in enumerate(a)]
    f.add(f'<path class="facet" d="{poly(A(a + inner[::-1], s))}"/>')
# wcięcie żebrowe I – podłużne, chropawe pole (połączenie chrząstkozrostem)
I_arc = bez([(-14.4, 13.4), (-14.55, 15.0), (-14.35, 17.6), (-14.5, 20.2), (-14.15, 21.7)], n=10)
for s in (-1, 1):
    m = len(I_arc)
    inner = [(x + 1.0 * math.sin(math.pi * i / (m - 1)) ** 0.7, y) for i, (x, y) in enumerate(I_arc)]
    f.add(f'<path class="bone2" d="{poly(A(I_arc + inner[::-1], s))}"/>')
# wcięcia żebrowe II–VII – gładkie, pokryte chrząstką szklistą
for k, (yc, h, dep) in NOTCH.items():
    for s in (-1, 1):
        f.add(f'<path class="facet" d="{lens_y(yc, h, wfun_all, 0.6, s)}"/>')

# kresy poprzeczne na powierzchni przedniej trzonu (na poziomie wcięć III, IV, V)
for y in (44.6, 55.6, 65.6):
    w = cr1d(W_BODY, y) - dip(y) - 0.15
    f.add(f'<path class="bonel" d="M{C - w:.2f},{y + DY:.2f} Q{C},{y + DY + 0.9:.2f} {C + w:.2f},{y + DY:.2f}"/>')

# ---------- podpisy ----------
TL, TR = 45.5, 84.5
f.label((C, 9.5 + DY), 'wcięcie szyjne', 'incisura jugularis', (C + 2.3, 3.6), side='R')
f.label((C - 9.0, 10.55 + DY), 'wcięcie obojczykowe', 'incisura clavicularis', (TL, 12.5), side='L')
f.label((C - 4.0, 21.0 + DY), 'rękojeść mostka', 'manubrium sterni', (TL, 23.5), side='L')
f.label((C - 3.0, 33.2 + DY), 'górne połączenie mostkowe', 'synchondrosis manubriosternalis', (TL, 36.0), side='L')
f.label((C - 3.0, 60.0 + DY), 'trzon mostka', 'corpus sterni', (TL, 61.0), side='L')
f.label((C - 2.5, 84.0 + DY), 'dolne połączenie mostkowe', 'synchondrosis xiphosternalis', (TL, 86.0), side='L')
f.label((C - 1.2, 93.0 + DY), 'wyrostek mieczykowaty', 'processus xiphoideus', (TL, 95.5), side='L')


def R(y, inset=0.35):
    """punkt na powierzchni wcięcia po prawej stronie rysunku"""
    return (C + wfun_all(y) - dip(y) - inset, y + DY)


f.label((C + 14.0, 17.6 + DY), 'wcięcie żebrowe I', 'incisura costalis I', (TR, 20.5), side='R')
f.label(R(33.2), 'wcięcie żebrowe II', 'incisura costalis II', (TR, 36.0), side='R')
f.label(R(44.6), 'wcięcie żebrowe III', 'incisura costalis III', (TR, 47.5), side='R')
f.label(R(55.6), 'wcięcie żebrowe IV', 'incisura costalis IV', (TR, 58.0), side='R')
f.label(R(65.6), 'wcięcie żebrowe V', 'incisura costalis V', (TR, 68.0), side='R')
f.label(R(74.2), 'wcięcie żebrowe VI', 'incisura costalis VI', (TR, 77.5), side='R')
f.label(R(84.0), 'wcięcie żebrowe VII', 'incisura costalis VII', (TR, 87.5), side='R')
f.save()
