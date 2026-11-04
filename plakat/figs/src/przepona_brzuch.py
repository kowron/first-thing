# TŁOCZNIA BRZUSZNA (prelum abdominis) – schemat strzałkowy tułowia (przód w lewo) + wstawka: przekrój poprzeczny brzucha.
# Wg Bochenka s. 716 (pkt 3 „Współdziałanie mięśni brzucha”) i s. 709 (czynność m. poprzecznego brzucha):
#  - miednica i klatka piersiowa ustalone;
#  - kurczą się razem: przepona, mięśnie dna miednicy i mięśnie powłok brzucha (największy udział – m. poprzeczny,
#    dzięki poprzecznemu kierunkowi włókien) → objętość jamy brzusznej maleje, ciśnienie w niej rośnie;
#  - tłocznia w pełni wyzyskana, gdy powietrze zatrzymane w płucach przez zamknięcie szpary głośni: płuca podpierają
#    przeponę jak poduszki wypełnione powietrzem i nie dają jej uwypuklić się w obręb klatki piersiowej.
# Strzałki: niebieskie – skurcz mięśni (nacisk na zawartość jamy brzusznej), czerwone – płuca podpierają przeponę.
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 150, 108
YTOP = 2.6                    # górne cięcie (szyja)
f = Fig('przepona_brzuch', W, H,
        caption='tłocznia brzuszna (prelum abdominis) · schemat strzałkowy tułowia (przód w lewo) i przekrój poprzeczny brzucha')


# ---------- pomocnicze ----------
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


def offset(pl, d):
    """przesunięcie łamanej o d wzdłuż normalnej (d>0 – w lewo od kierunku marszu w układzie ekranu)."""
    out = []
    for i, p in enumerate(pl):
        a = pl[max(i - 1, 0)]; b = pl[min(i + 1, len(pl) - 1)]
        tx, ty = b[0] - a[0], b[1] - a[1]
        L = math.hypot(tx, ty) or 1
        dd = d(p) if callable(d) else d
        out.append((p[0] + ty / L * dd, p[1] - tx / L * dd))
    return out


def poly(pts):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + ' Z'


def line(pts):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts)


def interp(prof, y):
    for (y0, v0), (y1, v1) in zip(prof, prof[1:]):
        if y0 <= y <= y1:
            return v0 + (v1 - v0) * (y - y0) / (y1 - y0)
    return prof[0][1] if y < prof[0][0] else prof[-1][1]


def y_at(pl, x, lo=None, hi=None):
    for (x0, y0), (x1, y1) in zip(pl, pl[1:]):
        if (x0 - x) * (x1 - x) <= 0 and x0 != x1:
            y = y0 + (y1 - y0) * (x - x0) / (x1 - x0)
            if (lo is None or y >= lo) and (hi is None or y <= hi):
                return y
    return None


def x_at(pl, y, lo=None, hi=None):
    for (x0, y0), (x1, y1) in zip(pl, pl[1:]):
        if (y0 - y) * (y1 - y) <= 0 and y0 != y1:
            x = x0 + (x1 - x0) * (y - y0) / (y1 - y0)
            if (lo is None or x >= lo) and (hi is None or x <= hi):
                return x
    return None


# =====================================================================  RYSUNEK GŁÓWNY (przód w lewo)
# ---------- kręgosłup: przednia powierzchnia trzonów x = XS(y) ----------
XS = [(-2, 69.6), (11, 70.6), (20, 72.9), (30, 74.0), (40, 73.3), (50, 70.9), (58, 68.4), (66, 67.6), (73.6, 68.7)]


def xs(y):
    return interp(XS, y)


levels = []                    # (nazwa, góra, dół, głębokość)
y = 0.6
for i, nm in enumerate(['C5', 'C6', 'C7']):
    levels.append((nm, y, y + 1.9, 3.0)); y += 1.9 + 0.7
for i in range(12):
    h = 2.45 + 0.05 * i
    levels.append((f'Th{i + 1}', y, y + h, 3.4 + 0.05 * i)); y += h + 0.75
for i in range(5):
    levels.append((f'L{i + 1}', y, y + 3.4, 4.7)); y += 3.4 + 1.25
print('dół L5 / promontorium', round(y - 1.25, 2))
Y_PROM = y - 1.25


def vbody(yt, yb, d, r=0.45):
    xt, xb = xs(yt), xs(yb)
    pts = [(xt, yt + r), (xt + r * 0.6, yt), (xt + d - r * 0.6, yt), (xt + d, yt + r),
           (xb + d, yb - r), (xb + d - r * 0.6, yb), (xb + r * 0.6, yb), (xb, yb - r)]
    return smooth(pts, closed=True, t=0.3)


for (n1, t1, b1, d1), (n2, t2, b2, d2) in zip(levels, levels[1:]):
    pts = [(xs(b1) + 0.1, b1), (xs(b1) + d1 - 0.1, b1), (xs(t2) + d2 - 0.1, t2), (xs(t2) + 0.1, t2)]
    f.add(f'<path class="annulus" d="{poly(pts)}"/>')
for nm, t1, b1, d1 in levels:
    f.add(f'<path class="bone" d="{vbody(t1, b1, d1)}"/>')
# krążek L5/S1
f.add(f'<path class="annulus" d="{poly([(xs(Y_PROM - 1.25) + .1, Y_PROM - 1.25), (xs(Y_PROM - 1.25) + 4.6, Y_PROM - 1.25), (73.4, Y_PROM + 0.1), (68.8, Y_PROM + 0.1)])}"/>')

# kość krzyżowa i guziczna (przekrój pośrodkowy)
SAC_F = [(68.7, Y_PROM), (70.4, 78.0), (72.4, 82.5), (73.6, 87.0), (73.6, 90.6)]
SAC_B = [(76.2, 90.4), (77.6, 86.0), (77.6, 81.0), (76.6, 76.8), (74.4, Y_PROM - 0.3)]
f.add(f'<path class="bone" d="{smooth(SAC_F + SAC_B, closed=True, t=0.4)}"/>')
for yy in (78.4, 82.6, 86.6):            # linie zrostu kręgów krzyżowych
    xa_ = x_at(cr(SAC_F, n=8), yy); xb_ = x_at(cr(SAC_B[::-1], n=8)[::-1], yy)
    if xa_ and xb_:
        f.add(f'<path class="bonel" d="M{xa_ + .3:.2f},{yy:.2f} L{xb_ - .3:.2f},{yy + .9:.2f}"/>')
COC = [(73.4, 91.4), (75.6, 91.2), (75.0, 93.4), (73.0, 95.4), (71.0, 96.0), (71.6, 94.4), (72.8, 92.8)]
f.add(f'<path class="bone" d="{smooth(COC, closed=True, t=0.35)}"/>')
COCCYX_TIP = (71.2, 95.6)

# ---------- spojenie łonowe ----------
SYM_C = (43.4, 87.6)
f.add(f'<ellipse class="bone" cx="{SYM_C[0]:.2f}" cy="{SYM_C[1]:.2f}" rx="2.3" ry="4.4" transform="rotate(-24 {SYM_C[0]:.2f} {SYM_C[1]:.2f})"/>')
f.add(f'<ellipse class="cart" cx="{SYM_C[0]:.2f}" cy="{SYM_C[1]:.2f}" rx="0.9" ry="3.7" transform="rotate(-24 {SYM_C[0]:.2f} {SYM_C[1]:.2f})"/>')

# ---------- przednia ściana brzucha (mięśnie powłok brzucha) ----------
WALL_IN = [(42.3, 42.6), (40.9, 47.0), (40.0, 53.0), (39.6, 60.0), (39.7, 67.0), (40.4, 74.0), (41.8, 80.0), (43.6, 84.0)]
wall_in = cr(WALL_IN, n=10)
wall_out = offset(wall_in, -2.5)       # na zewnątrz (w lewo)
f.add(f'<path class="muscle" d="{poly(wall_in + wall_out[::-1])}"/>')
f.add(f'<path class="musclel" d="{line(offset(wall_in, -1.25)[2:-2])}"/>')

# ---------- dno miednicy ----------
FLOOR = [(45.6, 89.6), (49.0, 92.6), (53.6, 95.6), (58.6, 97.4), (63.6, 97.2), (68.0, 96.2), (71.0, 95.4)]
floor = cr(FLOOR, n=10)
floor_lo = offset(floor, -2.0)
f.add(f'<path class="muscle" d="{poly(floor + floor_lo[::-1])}"/>')
f.add(f'<path class="musclel" d="{line(offset(floor, -1.0)[2:-2])}"/>')

# ---------- przepona (położenie wdechowe, skurcz) ----------
DIA = [(42.6, 42.4), (44.4, 39.9), (47.6, 38.0), (52.0, 37.0), (57.0, 37.4), (61.8, 39.2), (65.6, 42.2), (68.0, 46.0),
       (69.2, 50.4), (69.3, 54.8), (68.8, 59.4), (68.3, 62.6)]
cD = cr(DIA, n=14)
TEN = (47.6, 60.4)


def dthick(p):
    x, yy = p
    if TEN[0] < x < TEN[1] and yy < 41:
        return 1.2
    return 1.8


upD = offset(cD, lambda p: dthick(p) / 2)       # strona piersiowa (górna/tylna)
loD = offset(cD, lambda p: -dthick(p) / 2)      # strona brzuszna

# ---------- jama brzuszna (zawartość) ----------
ab = (loD[1:] + [(xs(yy) - 0.35, yy) for yy in [63 + 0.5 * k for k in range(int((Y_PROM - 63) / 0.5) + 1)]]
      + [(x - 0.35, yy) for x, yy in cr(SAC_F, n=6)[1:]] + [(73.0, 92.0)] + floor[::-1][1:] + [(45.0, 88.6)]
      + wall_in[::-1][1:])
f.add(f'<path class="organ" d="{poly(ab)}"/>')

# ---------- płuca i drogi oddechowe ----------
GAP = 0.6
ST_B = [(47.1, 17.4), (46.0, 22.0), (44.9, 27.0), (43.9, 32.0), (43.1, 36.6), (43.0, 38.8)]   # tylna pow. mostka
lung_front = [(x + GAP, yy) for x, yy in cr(ST_B, n=6)]
lung_top = [(47.8, 15.4), (49.4, 11.9), (52.6, 9.7), (56.8, 9.1), (61.4, 9.8), (65.8, 11.2), (69.0, 12.6)]
lung_back = [(xs(yy) - GAP, yy) for yy in [13.5 + 0.5 * k for k in range(int((48.6 - 13.5) / 0.5) + 1)]]
dia_up = [p for p in offset(cD, lambda p: dthick(p) / 2 + GAP) if p[1] < 48.4]
lung = lung_front[::-1][:-1] + cr(lung_top, n=6) + lung_back + [(69.9, 49.2)] + dia_up[::-1] + [(43.6, 40.6)]
f.add(f'<path class="organ" d="{poly(lung)}"/>')
# drogi oddechowe: krtań (szersza), tchawica, rozwidlenie na oskrzela główne
TR = [(63.2, 1.0), (63.3, 6.0), (63.9, 11.0), (65.0, 16.5), (66.2, 22.4)]
ctr = cr(TR, n=10)
# tchawica z rozwidleniem na oskrzela główne – jeden kontur (ściana) i jedno światło
cA = cr([(66.2, 21.6), (65.7, 24.6), (64.3, 27.6)], n=8)
cB = cr([(66.2, 21.6), (67.1, 24.6), (68.0, 27.4)], n=8)


def airway(wt, wb, ycar):
    tr_ant = [p for p in offset(ctr, -wt) if p[1] < 21.0]
    tr_post = [p for p in offset(ctr, wt) if p[1] < 21.0][::-1]
    a_ant = [p for p in offset(cA, -wb) if p[1] >= 23.0]
    a_post = [p for p in offset(cA, wb) if p[1] >= ycar][::-1]
    b_ant = [p for p in offset(cB, -wb) if p[1] >= ycar]
    b_post = [p for p in offset(cB, wb) if p[1] >= 23.0][::-1]
    return tr_ant + a_ant + a_post + b_ant + b_post + tr_post


f.add(f'<path class="cart" d="{poly(airway(1.6, 1.15, 24.4))}"/>')
f.add(f'<path class="cavity" d="{poly(airway(0.8, 0.5, 23.4))}"/>')
for yy in [11.6 + 1.6 * k for k in range(7)]:       # chrząstki tchawicy
    xc = x_at(ctr, yy)
    if xc:
        f.add(f'<path class="bonel" d="M{xc - 1.55:.2f},{yy:.2f} L{xc - 0.8:.2f},{yy + 0.15:.2f} M{xc + 0.8:.2f},{yy + 0.15:.2f} L{xc + 1.55:.2f},{yy + 0.3:.2f}"/>')
# krtań (odcinek szerszy) ze zwartymi fałdami głosowymi – szpara głośni zamknięta
lar = [p for p in ctr if p[1] <= 9.6]
f.add(f'<path class="cart" d="{poly(offset(lar, 2.5) + offset(lar, -2.5)[::-1])}"/>')
f.add(f'<path class="cavity" d="{poly(offset(lar, 1.2) + offset(lar, -1.2)[::-1])}"/>')
GL_Y = 5.6
xg = x_at(ctr, GL_Y)
for s_ in (-1, 1):
    f.add(f'<path class="muscle" d="M{xg + s_ * 1.25:.2f},{GL_Y - 1.5:.2f} Q{xg + s_ * 0.5:.2f},{GL_Y - 0.4:.2f} {xg:.2f},{GL_Y:.2f} '
          f'L{xg:.2f},{GL_Y + 0.3:.2f} Q{xg + s_ * 0.6:.2f},{GL_Y + 1.0:.2f} {xg + s_ * 1.25:.2f},{GL_Y + 1.9:.2f} Z"/>')

# ---------- przepona (na wierzchu płuc i jamy brzusznej) ----------
iT0 = next(i for i, p in enumerate(cD) if p[0] >= TEN[0])
iT1 = next(i for i, p in enumerate(cD) if p[0] >= TEN[1])
for a, b, cls in ((0, iT0 + 1, 'muscle'), (iT1, len(cD), 'muscle'), (iT0, iT1 + 1, 'tendon')):
    f.add(f'<path class="{cls}" d="{poly(upD[a:b] + loD[a:b][::-1])}"/>')
for a, b in ((2, iT0 - 1), (iT1 + 2, len(cD) - 3)):
    f.add(f'<path class="musclel" d="{line(cD[a:b])}"/>')

# ---------- mostek z wyrostkiem mieczykowatym ----------
ST_F = [(44.6, 17.0), (43.6, 22.0), (42.4, 27.0), (41.3, 32.0), (40.6, 36.6), (40.6, 38.8)]
XIPH = [(40.7, 39.2), (41.2, 42.0), (42.0, 43.4), (42.6, 43.0), (42.4, 41.2), (42.6, 39.2)]
f.add(f'<path class="bone" d="{smooth(ST_F + [(41.6, 39.4)] + ST_B[::-1] + [(46.9, 16.6)], closed=True, t=0.3)}"/>')
f.add(f'<path class="bone" d="{smooth(XIPH, closed=True, t=0.3)}"/>')
f.add(f'<path class="bonel" d="M{interp([(17, 44.6), (22, 43.6)], 21.2):.2f},21.2 L{interp([(17, 47.1), (22, 46.0)], 21.4):.2f},21.4"/>')

# ---------- strzałki ----------
# skurcz przepony – w dół
for x0 in (50.0, 57.8):
    y0 = y_at(loD, x0, 30, 46) + 0.9
    f.arrow(f'M{x0:.2f},{y0:.2f} L{x0:.2f},{y0 + 5.2:.2f}')
# skurcz mięśni powłok brzucha – ku tyłowi
for y0 in (53.0, 62.0, 71.0):
    x0 = x_at(wall_in, y0) + 0.9
    f.arrow(f'M{x0:.2f},{y0:.2f} L{x0 + 5.4:.2f},{y0:.2f}')
# skurcz mięśni dna miednicy – ku górze
for x0 in (55.0, 62.2):
    y0 = y_at(floor, x0) - 0.9
    f.arrow(f'M{x0:.2f},{y0:.2f} L{x0:.2f},{y0 - 5.0:.2f}')
# płuca podpierają przeponę
for x0 in (50.0, 57.8):
    y1 = y_at(upD, x0, 30, 46) - 0.8
    f.arrow(f'M{x0:.2f},{y1 - 5.6:.2f} L{x0:.2f},{y1:.2f}', red=True)

# ---------- podpisy (lewa kolumna) ----------
TL = 33.6
f.label((xg - 0.55, GL_Y + 0.15), 'szpara głośni zamknięta', None, (TL, 5.8), side='L')
f.label((53.0, 19.0), 'płuca', None, (TL, 14.6), side='L')
f.text(TL - 0.7, 18.0, 'powietrze zatrzymane;', anchor='end')
f.text(TL - 0.7, 20.6, 'jak poduszki podpierają', anchor='end')
f.text(TL - 0.7, 23.2, 'przeponę', anchor='end')
f.label((41.9, 30.0), 'klatka piersiowa', None, (TL, 27.4), side='L')
f.text(TL - 0.7, 31.0, 'ustalona', anchor='end')
f.label((44.2, 40.6), 'przepona', 'diaphragma', (TL, 37.2), side='L')
f.label((38.8, 58.0), 'mięśnie powłok brzucha', None, (TL, 50.2), side='L')
f.text(TL - 0.7, 54.2, 'największy udział:', anchor='end')
f.text(TL - 0.7, 56.8, 'm. poprzeczny brzucha', anchor='end')
f.label((52.0, 66.0), 'jama brzuszna', None, (TL, 66.6), side='L')
f.text(TL - 0.7, 70.0, 'objętość maleje,', anchor='end')
f.text(TL - 0.7, 72.6, 'ciśnienie rośnie', anchor='end')
f.label((42.2, 88.6), 'miednica', None, (TL, 81.6), side='L')
f.text(TL - 0.7, 85.2, 'ustalona', anchor='end')
f.label((50.0, 94.6), 'mięśnie dna miednicy', None, (TL, 94.0), side='L')

# =====================================================================  WSTAWKA: przekrój poprzeczny brzucha
# (na wysokości L3, widok od góry, przód ku górze; schemat)
CX, CY, SC = 121.0, 32.0, 1.12


def Q(x, y):
    return (CX + SC * x, CY + SC * y)


def mirror_l(pts):
    return [(-x, y) for x, y in pts]


f.text(CX, 8.0, 'przekrój poprzeczny brzucha', cls='notec')
f.text(CX, 10.6, '(od góry, przód ku górze)', cls='notec')

# kontur jamy brzusznej (prawa połowa rysunku, od przodu ku tyłowi)
CAV_R = [(0, -10.9), (4.4, -10.6), (8.8, -9.7), (13.0, -7.6), (16.4, -4.3), (18.3, -0.3), (18.5, 3.5), (17.0, 6.6),
         (14.4, 7.6), (11.6, 6.5), (9.6, 4.4), (8.2, 2.2), (6.4, 1.5), (4.4, 1.8), (2.6, 1.2), (0, 0.9)]
cav_r = cr(CAV_R, n=8)
cav = cav_r + [(-x, y) for x, y in cav_r[::-1]][1:-1]
# odcinek ściany bocznej (od brzegu m. prostego do m. czworobocznego lędźwi) – po nim biegną 3 mięśnie płaskie
lat_r = cr([(8.2, -9.85), (13.0, -7.6), (16.4, -4.3), (18.3, -0.3), (18.5, 3.5), (17.0, 6.6), (14.6, 7.7)], n=10)
LAYERS = [(0.0, 0.9, 0), (0.9, 1.9, 4), (1.9, 2.9, 9)]     # (od, do, ile punktów krócej z tyłu): poprzeczny, skośny wewn., skośny zewn.

# mięśnie grzbietu (prostownik), łuk kręgu z wyrostkami, trzon L3
for s_ in (-1, 1):
    er = [(s_ * 1.4, 9.0), (s_ * 4.6, 8.4), (s_ * 8.6, 9.2), (s_ * 9.6, 12.2), (s_ * 7.0, 14.6), (s_ * 1.4, 14.4)]
    f.add(f'<path class="muscle" d="{smooth([Q(*p) for p in er], closed=True, t=0.4)}"/>')
    f.add(f'<path class="shade" d="{smooth([Q(*p) for p in er], closed=True, t=0.4)}"/>')
f.add(f'<path class="bone" d="{poly([Q(-0.8, 7.0), Q(0.8, 7.0), Q(0.6, 14.6), Q(-0.6, 14.6)])}"/>')
f.add(f'<path class="bone" d="{smooth([Q(*p) for p in [(-10.2, 7.6), (-6.0, 6.0), (-3.4, 5.2), (0, 5.6), (3.4, 5.2), (6.0, 6.0), (10.2, 7.6), (9.8, 8.5), (5.4, 7.6), (2.4, 8.4), (0, 9.0), (-2.4, 8.4), (-5.4, 7.6), (-9.8, 8.5)]], closed=True, t=0.35)}"/>')
f.add(f'<ellipse class="hole" cx="{CX:.2f}" cy="{CY + SC * 6.8:.2f}" rx="{SC * 1.6:.2f}" ry="{SC * 1.1:.2f}"/>')
f.add(f'<path class="bone" d="{smooth([Q(*p) for p in [(-3.8, 4.8), (-4.3, 2.6), (-2.6, 1.0), (0, 0.6), (2.6, 1.0), (4.3, 2.6), (3.8, 4.8), (0, 5.4)]], closed=True, t=0.4)}"/>')
# m. lędźwiowy większy i m. czworoboczny lędźwi
for s_ in (-1, 1):
    ps = [(s_ * 4.2, 2.0), (s_ * 6.4, 1.2), (s_ * 8.6, 2.4), (s_ * 9.6, 4.6), (s_ * 8.2, 6.4), (s_ * 5.0, 5.6)]
    f.add(f'<path class="muscle" d="{smooth([Q(*p) for p in ps], closed=True, t=0.4)}"/>')
    ql = [(s_ * 10.0, 8.6), (s_ * 10.4, 6.8), (s_ * 12.4, 6.4), (s_ * 15.0, 7.4), (s_ * 15.2, 9.0), (s_ * 12.4, 9.8)]
    f.add(f'<path class="muscle" d="{smooth([Q(*p) for p in ql], closed=True, t=0.4)}"/>')

# zawartość jamy brzusznej
f.add(f'<path class="organ" d="{poly([Q(*p) for p in cav])}"/>')

# trzy mięśnie płaskie (obie strony)
for s_ in (-1, 1):
    base = [(s_ * x, y) for x, y in lat_r]
    if s_ < 0:
        base_m = base[::-1]          # marsz w kierunku przeciwnym do ruchu wskazówek zegara → odwrócone normalne
    for d0, d1, cut in LAYERS:
        seg = base[:len(base) - cut]
        o0 = offset(seg, d0 * s_)
        o1 = offset(seg, d1 * s_)
        f.add(f'<path class="muscle" d="{poly([Q(*p) for p in o0 + o1[::-1]])}"/>')
        if d0 > 0.5:             # mm. skośne lekko przyciemnione – m. poprzeczny (warstwa najgłębsza) wyróżniony
            f.add(f'<path class="shade" d="{poly([Q(*p) for p in o0 + o1[::-1]])}"/>')
    # włókna m. poprzecznego – poprzecznie (okrężnie)
    mid = offset(base, 0.45 * s_)[2:-1]
    f.add(f'<path class="musclel" d="{line([Q(*p) for p in mid])}"/>')
# m. prosty brzucha w pochewce i kresa biała
for s_ in (-1, 1):
    rc = Q(s_ * 4.35, -12.15)
    f.add(f'<ellipse class="tendon" cx="{rc[0]:.2f}" cy="{rc[1]:.2f}" rx="{SC * 4.35:.2f}" ry="{SC * 1.95:.2f}"/>')
    f.add(f'<ellipse class="muscle" cx="{rc[0]:.2f}" cy="{rc[1]:.2f}" rx="{SC * 3.85:.2f}" ry="{SC * 1.5:.2f}"/>')
    f.add(f'<ellipse class="shade" cx="{rc[0]:.2f}" cy="{rc[1]:.2f}" rx="{SC * 3.85:.2f}" ry="{SC * 1.5:.2f}"/>')
f.text(CX, CY - 4.4, 'jama brzuszna', cls='notec')
f.text(CX, CY - 1.8, 'ciśnienie rośnie', cls='notec')
# strzałki skurczu – ściany „sznurują” brzuch ku środkowi
ARW = [((18.0, -1.0), (12.0, -1.6)), ((14.4, -6.4), (9.6, -3.6)), ((4.4, -10.1), (4.4, -6.2))]
for s_ in (-1, 1):
    for (x0, y0), (x1, y1) in ARW:
        a, b = Q(s_ * x0, y0), Q(s_ * x1, y1)
        f.arrow(f'M{a[0]:.2f},{a[1]:.2f} L{b[0]:.2f},{b[1]:.2f}')

# podpisy wstawki
pt = Q(-18.5 - 0.45, 4.6)
f.label(pt, 'm. poprzeczny brzucha', 'm. transversus abdominis', (88.2, 56.0), side='R')
f.text(88.9, 62.6, 'poprzeczny kierunek włókien –')
f.text(88.9, 65.2, 'największy udział w tłoczni,')
f.text(88.9, 67.8, 'przy współudziale pozostałych')
f.text(88.9, 70.4, 'mięśni brzucha')

# ---------- legenda ----------
LY = 80.6
lx = 96.0
f.arrow(f'M{lx:.2f},{LY - 0.6:.2f} L{lx + 6.6:.2f},{LY - 0.6:.2f}')
f.text(lx + 8.0, LY + 0.3, 'skurcz mięśni – nacisk')
f.text(lx + 8.0, LY + 2.9, 'na zawartość jamy brzusznej')
f.arrow(f'M{lx:.2f},{LY + 6.4:.2f} L{lx + 6.6:.2f},{LY + 6.4:.2f}', red=True)
f.text(lx + 8.0, LY + 7.3, 'płuca (powietrze zatrzymane)')
f.text(lx + 8.0, LY + 9.9, 'podpierają przeponę')
f.text(lx, LY + 16.0, 'Tłocznia jest szczególnie skuteczna, gdy')
f.text(lx, LY + 18.6, 'klatka piersiowa i miednica zbliżają się do siebie.')

# przycięcie u góry (szyja)
body = ''.join(f.body)
f.body = [f'<defs><clipPath id="cp_przepona_brzuch"><rect x="0" y="{YTOP:.2f}" width="{W}" height="{H - YTOP:.2f}"/>'
          f'</clipPath></defs><g clip-path="url(#cp_przepona_brzuch)">{body}</g>']
f.save()
print('ok')
