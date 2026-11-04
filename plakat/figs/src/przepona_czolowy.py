# PRZEPONA – przekrój czołowy tułowia (schemat własny wg opisu Bochenka s. 691–695).
# Widok od przodu: prawa strona ciała po lewej stronie rysunku. Linia ciągła (pasmo mięśnia) – wydech,
# linia przerywana – wdech (maksymalny zakres wg Bochenka: do trzech żeber, kopuła prawa Th8 → Th11).
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 160, 112
C = 80.0                      # oś pośrodkowa
YT, YB = 6.0, 103.5           # linie cięcia u góry i u dołu
f = Fig('przepona_czolowy', W, H,
        caption='przepona · przekrój czołowy tułowia (schemat) · linia ciągła – wydech, przerywana – wdech · '
                'prawa strona ciała po lewej')


# ---------- pomocnicze (jak w przepona_dol.py) ----------
def cr(pts, closed=False, n=12, t=0.5):
    m = len(pts)
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


def offset_var(pl, dfun):
    """przesunięcie łamanej wzdłuż normalnej o d = dfun(punkt) (d>0 – w dół przy marszu w prawo)."""
    out = []
    for i, p in enumerate(pl):
        a = pl[max(i - 1, 0)]; b = pl[min(i + 1, len(pl) - 1)]
        tx, ty = b[0] - a[0], b[1] - a[1]
        L = math.hypot(tx, ty) or 1
        d = dfun(p)
        out.append((p[0] - ty / L * d, p[1] + tx / L * d))
    return out


def poly(pts):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + ' Z'


def line(pts):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts)


def interp(prof, y):
    """liniowa interpolacja wartości z profilu [(y, v), ...]"""
    for (y0, v0), (y1, v1) in zip(prof, prof[1:]):
        if y0 <= y <= y1:
            return v0 + (v1 - v0) * (y - y0) / (y1 - y0)
    return prof[0][1] if y < prof[0][0] else prof[-1][1]


def y_at(pl, x, lo=None, hi=None):
    """y krzywej (łamanej) dla danego x – pierwsze trafienie w zakresie y [lo, hi]."""
    for (x0, y0), (x1, y1) in zip(pl, pl[1:]):
        if (x0 - x) * (x1 - x) <= 0 and x0 != x1:
            y = y0 + (y1 - y0) * (x - x0) / (x1 - x0)
            if (lo is None or y >= lo) and (hi is None or y <= hi):
                return y
    return None


# ---------- ściana tułowia ----------
HW_IN = [(0, 24.4), (6, 25.0), (16, 28.0), (28, 30.3), (40, 31.6), (52, 32.1), (64, 31.9), (74, 31.2), (84, 30.2),
         (94, 29.6), (110, 29.4)]
TH_W = [(0, 3.5), (72, 3.5), (80, 3.0), (110, 3.0)]
ys = [YT - 3 + k * 1.0 for k in range(int(YB - YT + 7))]


def wall_in(s, y):            # s = -1 strona prawa ciała (lewa rysunku), +1 lewa
    return C + s * interp(HW_IN, y)


def wall_out(s, y):
    return C + s * (interp(HW_IN, y) + interp(TH_W, y))


# ---------- przepona: linia środkowa (wydech) ----------
EXP = [(48.4, 75.4), (50.0, 69.0), (51.1, 63.0), (52.6, 57.0), (54.4, 51.6), (56.8, 46.6), (59.8, 42.6), (63.4, 40.0),
       (67.4, 39.6), (71.4, 40.7), (75.4, 42.5), (79.2, 43.8), (83.0, 44.3), (86.8, 43.9), (90.4, 43.1), (94.0, 42.2),
       (97.6, 42.0), (101.4, 43.0), (104.7, 45.4), (107.2, 49.8), (108.8, 55.6), (109.6, 62.0), (110.1, 68.6),
       (111.5, 75.6)]
# wdech (głęboki): kopuły niżej, spłaszczone, przepona odchyla się od ściany; przyczepy te same
INS = [(48.4, 75.4), (50.3, 69.2), (52.8, 63.6), (56.0, 58.6), (59.9, 54.6), (63.8, 52.3), (67.6, 51.6), (71.8, 51.9),
       (76.2, 52.5), (80.5, 52.9), (85.5, 53.1), (91.0, 53.5), (96.5, 54.1), (101.2, 55.4), (104.8, 58.2), (107.4, 63.4),
       (109.4, 69.0), (111.5, 75.6)]
cE = cr(EXP, n=16)
cI = cr(INS, n=16)

TEN = (66.5, 96.0)            # zasięg środka ścięgnistego (x)


def thick(p):
    x, y = p
    d_ten = min(abs(x - TEN[0]), abs(x - TEN[1]))
    inside = TEN[0] < x < TEN[1]
    if inside:
        t = 1.25
    else:
        t = 1.25 + 0.65 * min(1.0, d_ten / 3.0)
    if y > 68:                 # zwężenie przy przyczepie do ściany
        t *= max(0.62, 1 - (y - 68) / 16)
    return t


upE = offset_var(cE, lambda p: -thick(p) / 2)       # powierzchnia górna (piersiowa)
loE = offset_var(cE, lambda p: thick(p) / 2)        # powierzchnia dolna (brzuszna)

# szczyty kopuł (wydech) – najwyższe punkty powierzchni górnej
apR = min((p for p in upE if 55 < p[0] < 78), key=lambda p: p[1])
apL = min((p for p in upE if 88 < p[0] < 106), key=lambda p: p[1])
yI_R = y_at(cI, apR[0], 45, 60)                      # linia wdechu pod szczytem kopuły prawej
print('szczyt kopuły prawej', apR, ' lewej', apL, ' wdech pod prawą', yI_R)

# ---------- 1. płuca ----------
GAP = 0.55


def lung(s):
    # brzeg boczny: wzdłuż ściany (przesunięty do środka o GAP), od góry do wierzchołka zachyłka
    tipy = 57.6
    lat = [(wall_in(s, y) - s * GAP, y) for y in ys if YT - 3 <= y <= tipy - 1.2]
    # powierzchnia przeponowa płuca: górna powierzchnia przepony podniesiona o GAP
    if s < 0:
        dia = [p for p in offset_var(cE, lambda p: -thick(p) / 2 - GAP) if p[0] < C and p[1] < tipy]
    else:
        dia = [p for p in offset_var(cE, lambda p: -thick(p) / 2 - GAP) if p[0] > C and p[1] < tipy][::-1]
    xw = wall_in(s, tipy - 1.2) - s * GAP
    tip = (xw + (dia[0][0] - xw) * 0.45 + s * 0.0, tipy)
    return lat, tip, dia


# serce + osierdzie (kontur serca; dół na środku ścięgnistym)
def dia_top(x, extra=0.0):
    return y_at(offset_var(cE, lambda p: -thick(p) / 2 - extra), x, 35, 48)


HEART_R = [(C - 7.0, YT - 3), (C - 7.4, 12.0), (C - 8.2, 18.0), (C - 9.4, 24.0), (C - 10.1, 30.5), (C - 10.0, 36.0)]
HEART_L = [(C + 14.6, 36.5), (C + 15.0, 31.0), (C + 13.2, 25.0), (C + 10.4, 20.0), (C + 8.2, 16.4), (C + 6.6, 12.0),
           (C + 5.6, YT - 3)]
x_hr, x_ha = C - 9.2, C + 14.0                     # gdzie serce siada na przeponie (prawy brzeg, koniuszek)


def heart_outline(grow):
    right = [(x - grow, y) for x, y in HEART_R]
    left = [(x + grow, y) for x, y in HEART_L]
    bot = [(x, dia_top(x, 0.05)) for x in [x_hr - grow + k * (x_ha + grow - x_hr + grow) / 30 for k in range(31)]]
    # zaokrąglenie przejścia brzeg prawy → dół i dół → koniuszek
    pts = right + [(x_hr - grow - 0.5, bot[0][1] - 2.2)] + bot + [(x_ha + grow + 0.9, bot[-1][1] - 1.4)] + left
    return pts


peri = heart_outline(1.0)
heart = heart_outline(0.0)

# płuca (osierdzie rysujemy później na wierzchu)
for s_ in (-1, 1):
    lat, tip, dia = lung(s_)
    if s_ < 0:
        dia = [p for p in dia if p[0] < x_hr - 1.0 - GAP]
        med = [(x - 1.0 - GAP, y) for x, y in HEART_R][::-1]          # z dołu do góry
    else:
        dia = [p for p in dia if p[0] > x_ha + 1.0 + GAP]
        med = [(x + 1.0 + GAP, y) for x, y in HEART_L]                # z dołu do góry
    pts = lat + [tip] + dia + med
    f.add(f'<path class="organ" d="{poly(pts)}"/>')
    LUNG_DBG = (tip, dia[0], dia[-1], med[0])
    print('płuco', s_, 'wierzchołek', tuple(round(v, 2) for v in tip), 'przepona od', tuple(round(v, 2) for v in dia[0]),
          'do', tuple(round(v, 2) for v in dia[-1]))

# ---------- 2. narządy jamy brzusznej ----------
# wątroba: góra = dolna powierzchnia przepony (od końca płata lewego do przyczepu), bok = ściana brzucha
XLT = C + 20.2                                       # koniec płata lewego
liv_top = [p for p in loE if p[0] < XLT and not (p[0] < 52 and p[1] > 74.6)][::-1]
liv_side = [(wall_in(-1, y) + 0.05, y) for y in ys if 75.5 <= y <= 84.0]
liv_low = [(C - 28.0, 86.6), (C - 22.0, 87.0), (C - 13.5, 84.0), (C - 6.0, 78.5), (C + 0.5, 71.5), (C + 5.5, 63.5),
           (C + 10.0, 56.0), (C + 14.5, 50.5), (C + 18.6, 46.2)]
liver = liv_top + liv_side + cr(liv_low, n=6)
f.add(f'<path class="organ" d="{poly(liver)}"/>')
f.add(f'<path class="shade" d="{poly(liver)}"/>')

# żołądek: dno pod kopułą lewą (między płatem lewym wątroby a śledzioną), trzon w dół, część odźwiernikowa w prawo
fund = [p for p in loE if C + 20.6 <= p[0] <= C + 24.2 and p[1] < 50]
stom_lat = [(C + 22.0, 50.4), (C + 20.8, 56.0), (C + 20.6, 63.0), (C + 20.2, 70.0), (C + 18.4, 76.6), (C + 13.8, 81.6),
            (C + 7.0, 84.4), (C + 0.2, 84.6), (C - 5.0, 83.0), (C - 8.4, 81.0)]
stom_med = [(C - 7.6, 79.4), (C - 4.4, 78.0), (C + 1.8, 72.4), (C + 6.6, 64.6), (C + 11.0, 57.4), (C + 15.6, 51.8),
            (C + 20.0, 46.8)]
stomach = fund + cr(stom_lat, n=6) + cr(stom_med, n=6)
f.add(f'<path class="organ" d="{poly(stomach)}"/>')

# śledziona: przy bocznej części kopuły lewej, przylega do przepony (na wierzchu żołądka)
spl_lat = [p for p in loE if p[0] > C + 20 and 49.6 <= p[1] <= 70.0]
spleen = spl_lat + [(C + 26.5, 72.2), (C + 22.6, 69.0), (C + 21.4, 63.5), (C + 21.6, 57.5), (C + 22.8, 52.8),
                    (C + 25.0, 49.8)]
f.add(f'<path class="organ" d="{smooth(spleen[::2], closed=True, t=0.35)}"/>')
f.add(f'<path class="shade" d="{smooth(spleen[::2], closed=True, t=0.35)}"/>')

# ---------- 3. przepona (wydech) ----------
iT0 = next(i for i, p in enumerate(cE) if p[0] >= TEN[0])
iT1 = next(i for i, p in enumerate(cE) if p[0] >= TEN[1])
for a, b, cls in ((0, iT0 + 1, 'muscle'), (iT1, len(cE), 'muscle'), (iT0, iT1 + 1, 'tendon')):
    seg = upE[a:b] + loE[a:b][::-1]
    f.add(f'<path class="{cls}" d="{poly(seg)}"/>')
# włókna mięśniowe wzdłuż pasma (część żebrowa)
for a, b in ((4, iT0 - 4), (iT1 + 4, len(cE) - 5)):
    f.add(f'<path class="musclel" d="{line(cE[a:b])}"/>')

# ---------- 4. osierdzie i serce ----------
f.add(f'<path class="organ" d="{smooth(peri, closed=True, t=0.35)}"/>')
f.add(f'<path class="organ" d="{smooth(heart, closed=True, t=0.35)}"/>')
f.add(f'<path class="shade" d="{smooth(heart, closed=True, t=0.35)}"/>')

# ---------- 5. ściana klatki piersiowej i brzucha (na wierzchu – przyczepy przepony chowają się pod nią) ----------
for s in (-1, 1):
    inner = [(wall_in(s, y), y) for y in ys]
    outer = [(wall_out(s, y), y) for y in ys]
    band = inner + outer[::-1]
    f.add(f'<path class="muscle" d="{poly(band)}"/>')
    f.add(f'<path class="shade" d="{poly(band)}"/>')
    # warstwy mięśni brzucha (poniżej łuku żebrowego)
    for u in (0.34, 0.67):
        lay = [(wall_in(s, y) + s * u * interp(TH_W, y), y) for y in ys if y >= 79.5]
        f.add(f'<path class="musclel" d="{line(lay)}"/>')
    # żebra w przekroju
    for k, yc in enumerate([7.6, 15.4, 23.2, 31.0, 38.8, 46.6, 54.4, 62.2, 70.0]):
        xc = (wall_in(s, yc) + wall_out(s, yc)) / 2
        dx = wall_in(s, yc + 1) - wall_in(s, yc - 1)
        ang = math.degrees(math.atan2(dx, 2.0))
        f.add(f'<ellipse class="bone" cx="{xc:.2f}" cy="{yc:.2f}" rx="0.95" ry="1.75" '
              f'transform="rotate({-ang:.1f} {xc:.2f} {yc:.2f})"/>')

# ---------- 6. przepona – wdech (linia przerywana) ----------
f.add(f'<path class="capsule" d="{line(cI)}"/>')

# strzałka ruchu kopuły prawej (wydech → wdech)
xa = apR[0]
ya0 = y_at(loE, xa, 38, 46) + 0.9
f.arrow(f'M{xa:.2f},{ya0:.2f} L{xa:.2f},{yI_R - 1.1:.2f}')

# ---------- 7. poziomy ----------
y_cad = apR[1] - 4.4                              # zwłoki – o międzyżebrze wyżej (IV chrząstka)
yL = apL[1]
xl = 42.4                                         # koniec linii poziomów po lewej
f.add(f'<path class="dim" d="M{xl:.2f},{y_cad:.2f} L{xa:.2f},{y_cad:.2f}"/>')
f.add(f'<path class="dim" d="M{xl:.2f},{apR[1]:.2f} L{xa:.2f},{apR[1]:.2f}"/>')
f.add(f'<path class="dim" d="M{xl:.2f},{yI_R:.2f} L{xa:.2f},{yI_R:.2f}"/>')
xr = 117.8
f.add(f'<path class="dim" d="M{apL[0]:.2f},{yL:.2f} L{xr:.2f},{yL:.2f}"/>')

f.text(41.6, y_cad + 0.75, 'zwłoki: IV chrząstka żebrowa', anchor='end')
f.text(41.6, apR[1] + 0.75, 'kopuła prawa – wydech:', anchor='end')
f.text(41.6, apR[1] + 3.35, 'górny brzeg V chrząstki · do Th8', anchor='end')
f.text(41.6, yI_R + 0.75, 'wdech: do VII żebra · do Th11', anchor='end')
f.text(118.6, yL + 0.75, 'kopuła lewa – wydech:')
f.text(118.6, yL + 3.35, 'dolny brzeg V chrząstki')

# ---------- podpisy ----------
# lewa strona rysunku (prawa strona ciała)
f.label((57.0, 19.0), 'płuco prawe', 'pulmo dexter', (41.2, 13.0), side='L')
zach = (wall_in(-1, 65.0) + 0.75, 65.0)
f.label(zach, 'zachyłek żebrowo-przeponowy', 'recessus costodiaphragmaticus', (41.9, 61.6), side='L')
f.label((60.0, 70.0), 'wątroba', 'hepar', (41.2, 77.0), side='L')
# prawa strona rysunku (lewa strona ciała)
f.label((106.0, 21.0), 'płuco lewe', 'pulmo sinister', (118.8, 10.5), side='R')
f.label((C + 14.35, 27.0), 'osierdzie', 'pericardium', (118.8, 19.0), side='R')
f.label((C + 8.0, 31.0), 'serce', 'cor', (118.8, 27.5), side='R')
f.label((C + 7.0, y_at(cE, C + 7.0, 40, 48)), 'środek ścięgnisty', 'centrum tendineum', (118.8, 50.0), side='R')
pp = min((p for p in cE if p[0] > 100), key=lambda p: abs(p[1] - 60.0))
f.label(pp, 'przepona', 'diaphragma', (118.8, 58.5), side='R')
f.label((C + 26.0, 66.0), 'śledziona', 'splen', (118.8, 69.0), side='R')
f.label((C + 12.0, 79.5), 'żołądek', 'gaster', (118.8, 86.0), side='R')

# przycięcie wszystkiego, co przecięte u góry i u dołu
body = ''.join(f.body)
f.body = [f'<defs><clipPath id="cp_przepona_czolowy"><rect x="0" y="{YT:.2f}" width="{W}" height="{YB - YT:.2f}"/>'
          f'</clipPath></defs><g clip-path="url(#cp_przepona_czolowy)">{body}</g>']
f.save()
