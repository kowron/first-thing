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
        caption='tłocznia brzuszna · schemat strzałkowy tułowia (przód w lewo) i przekrój poprzeczny brzucha')


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
for dx in (-0.2, 0.2):
    pass
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
       (69.0, 50.4), (68.8, 54.8), (68.0, 59.4), (67.4, 62.6)]
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
lung_top = [(47.8, 15.4), (50.0, 12.3), (54.0, 10.4), (58.4, 10.8)]
lung_back = [(xs(yy) - GAP, yy) for yy in [13 + 0.5 * k for k in range(int((48.6 - 13) / 0.5) + 1)]]
dia_up = [p for p in offset(cD, lambda p: dthick(p) / 2 + GAP) if p[1] < 48.4]
lung = lung_front[::-1][:-1] + cr(lung_top, n=6) + lung_back + [(69.9, 49.2)] + dia_up[::-1] + [(43.6, 40.6)]
lung = cr([(45.1, 39.2), (44.0, 36.6)], n=2)[:0] + lung
f.add(f'<path class="organ" d="{poly(lung)}"/>')
# tchawica i krtań
TR = [(63.2, 2.0), (63.4, 7.0), (64.2, 12.0), (65.6, 18.0), (66.6, 24.0)]
ctr = cr(TR, n=8)
tr_a = offset(ctr, 1.6); tr_b = offset(ctr, -1.6)
f.add(f'<path class="cart" d="{poly(tr_a + tr_b[::-1])}"/>')
f.add(f'<path class="cavity" d="{poly(offset(ctr, 0.8) + offset(ctr, -0.8)[::-1])}"/>')
for yy in [12.5 + 1.6 * k for k in range(7)]:       # chrząstki tchawicy
    xc = x_at(ctr, yy)
    if xc:
        f.add(f'<path class="bonel" d="M{xc - 1.55:.2f},{yy:.2f} L{xc - 0.8:.2f},{yy + 0.15:.2f} M{xc + 0.8:.2f},{yy + 0.15:.2f} L{xc + 1.55:.2f},{yy + 0.3:.2f}"/>')
# oskrzela główne (krótkie odcinki w płucu)
f.add(f'<path class="cart" d="{poly(offset(cr([(66.6, 23.6), (64.6, 27.4), (61.6, 30.2)], n=6), 1.0) + offset(cr([(66.6, 23.6), (64.6, 27.4), (61.6, 30.2)], n=6), -1.0)[::-1])}"/>')
# krtań: chrząstka tarczowata (przód) i zamknięta szpara głośni (zwarte fałdy głosowe)
LX = [(60.2, 2.0), (60.0, 5.0), (60.6, 8.2), (61.8, 10.4)]
f.add(f'<path class="cart" d="{poly(cr(LX, n=6) + offset(cr(LX, n=6), 1.4)[::-1])}"/>')
GL_Y = 6.3
xg = x_at(ctr, GL_Y)
f.add(f'<path class="muscle" d="M{xg - 1.7:.2f},{GL_Y - 1.0:.2f} L{xg + 0.15:.2f},{GL_Y - 0.15:.2f} L{xg + 0.15:.2f},{GL_Y + 0.25:.2f} '
      f'L{xg - 1.7:.2f},{GL_Y + 1.2:.2f} Z"/>')
f.add(f'<path class="muscle" d="M{xg + 1.7:.2f},{GL_Y - 1.0:.2f} L{xg - 0.15:.2f},{GL_Y - 0.15:.2f} L{xg - 0.15:.2f},{GL_Y + 0.25:.2f} '
      f'L{xg + 1.7:.2f},{GL_Y + 1.2:.2f} Z"/>')

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
f.label((xg - 1.0, GL_Y + 0.1), 'szpara głośni zamknięta', None, (TL, 6.4), side='L')
f.label((53.0, 19.0), 'płuca', None, (TL, 14.6), side='L')
f.text(TL - 0.7, 18.0, 'powietrze zatrzymane – ', anchor='end')
f.text(TL - 0.7, 20.6, 'podpierają przeponę', anchor='end')
f.label((41.9, 30.0), 'klatka piersiowa (ustalona)', None, (TL, 27.6), side='L')
f.label((44.2, 40.6), 'przepona', 'diaphragma', (TL, 37.2), side='L')
f.label((38.8, 58.0), 'mięśnie powłok brzucha', None, (TL, 50.2), side='L')
f.text(TL - 0.7, 53.6, 'największy udział:', anchor='end')
f.text(TL - 0.7, 56.2, 'm. poprzeczny brzucha', anchor='end')
f.label((52.0, 66.0), 'jama brzuszna', None, (TL, 66.6), side='L')
f.text(TL - 0.7, 70.0, 'objętość maleje,', anchor='end')
f.text(TL - 0.7, 72.6, 'ciśnienie rośnie', anchor='end')
f.label((42.2, 85.0), 'miednica (ustalona)', None, (TL, 82.0), side='L')
f.label((50.0, 94.6), 'mięśnie dna miednicy', None, (TL, 94.0), side='L')

# =====================================================================  WSTAWKA: przekrój poprzeczny brzucha
CX, CY = 122.0, 30.0
A0, B0 = 19.0, 11.6            # półosie wewnętrznej powierzchni ściany (jama brzuszna)


def E(t, d=0.0, sx=1.0):
    """punkt elipsy (t w stopniach; -90 = przód/góra rysunku), d – przesunięcie na zewnątrz."""
    r = math.radians(t)
    return (CX + (A0 + d) * math.cos(r) * sx, CY + (B0 + d) * math.sin(r))


f.text(CX, 8.4, 'przekrój poprzeczny brzucha', cls='notec')
f.text(CX, 11.0, 'widok od góry · przód ku górze', cls='notec')
# mięśnie grzbietu (prostownik) i wyrostek kolczysty
for s in (-1, 1):
    er = [(CX + s * 1.6, 40.6), (CX + s * 4.6, 39.4), (CX + s * 8.4, 40.6), (CX + s * 9.4, 44.2), (CX + s * 6.6, 46.6),
          (CX + s * 1.6, 46.4)]
    f.add(f'<path class="muscle" d="{smooth(er, closed=True, t=0.4)}"/>')
    f.add(f'<path class="shade" d="{smooth(er, closed=True, t=0.4)}"/>')
f.add(f'<path class="bone" d="M{CX - 0.9:.2f},38.4 L{CX + 0.9:.2f},38.4 L{CX + 0.7:.2f},46.4 L{CX - 0.7:.2f},46.4 Z"/>')
# łuk kręgu i trzon L3
f.add(f'<path class="bone" d="{smooth([(CX - 4.6, 37.6), (CX - 2.6, 35.6), (CX + 2.6, 35.6), (CX + 4.6, 37.6), (CX + 3.0, 39.6), (CX - 3.0, 39.6)], closed=True, t=0.4)}"/>')
f.add(f'<ellipse class="hole" cx="{CX:.2f}" cy="37.7" rx="1.5" ry="1.1"/>')
f.add(f'<path class="bone" d="{smooth([(CX - 3.9, 35.4), (CX - 4.2, 32.4), (CX - 2.4, 30.4), (CX, 30.0), (CX + 2.4, 30.4), (CX + 4.2, 32.4), (CX + 3.9, 35.4), (CX, 35.9)], closed=True, t=0.4)}"/>')
# m. lędźwiowy większy i m. czworoboczny lędźwi
for s in (-1, 1):
    ps = [(CX + s * 3.8, 31.6), (CX + s * 6.4, 29.8), (CX + s * 8.6, 31.4), (CX + s * 8.6, 34.6), (CX + s * 5.6, 35.6),
          (CX + s * 4.0, 34.8)]
    f.add(f'<path class="muscle" d="{smooth(ps, closed=True, t=0.4)}"/>')
    ql = [(CX + s * 7.8, 36.2), (CX + s * 10.6, 35.0), (CX + s * 13.6, 36.4), (CX + s * 12.8, 38.4), (CX + s * 9.0, 38.6)]
    f.add(f'<path class="muscle" d="{smooth(ql, closed=True, t=0.4)}"/>')
# trzy mięśnie płaskie: skośny zewnętrzny (zewn.), skośny wewnętrzny, poprzeczny (wewn.) – od brzegu m. prostego do tyłu
T0, T1 = -62.0, 44.0
LAY = [(1.6, 2.6, 'muscle'), (0.75, 1.6, 'muscle'), (0.0, 0.75, 'muscle')]       # (d_wewn, d_zewn)


def band_e(t0, t1, d0, d1, s):
    ts = [t0 + (t1 - t0) * k / 40 for k in range(41)]
    inner = [E(t if s > 0 else 180 - t, d0) for t in ts]
    outer = [E(t if s > 0 else 180 - t, d1) for t in ts]
    return inner + outer[::-1]


for s in (-1, 1):
    for d0, d1, cls in LAY:
        tt1 = T1 if d0 < 0.5 else (T1 - 6 if d0 < 1.0 else T1 - 14)
        f.add(f'<path class="{cls}" d="{poly(band_e(T0, tt1, d0, d1, s))}"/>')
    # włókna m. poprzecznego – poprzecznie (okrężnie)
    ts = [T0 + 2 + (T1 - 2 - T0 - 2) * k / 40 for k in range(41)]
    f.add(f'<path class="musclel" d="{line([E(t if s > 0 else 180 - t, 0.375) for t in ts])}"/>')
    # rozcięgno m. poprzecznego do tyłu (do m. czworobocznego lędźwi)
    pa = E(T1 if s > 0 else 180 - T1, 0.375)
    f.add(f'<path class="tendon" d="M{pa[0]:.2f},{pa[1] - 0.3:.2f} L{CX + s * 13.4:.2f},{36.0:.2f} L{CX + s * 13.6:.2f},{36.7:.2f} '
          f'L{pa[0] + s * 0.3:.2f},{pa[1] + 0.4:.2f} Z"/>')
# m. prosty brzucha (w pochewce) i kresa biała
for s in (-1, 1):
    rc = (CX + s * 4.4, CY - B0 - 1.1)
    f.add(f'<ellipse class="muscle" cx="{rc[0]:.2f}" cy="{rc[1]:.2f}" rx="4.3" ry="1.75"/>')
    f.add(f'<ellipse class="shade" cx="{rc[0]:.2f}" cy="{rc[1]:.2f}" rx="4.3" ry="1.75"/>')
f.add(f'<path class="tendon" d="M{CX - 0.35:.2f},{CY - B0 - 2.6:.2f} L{CX + 0.35:.2f},{CY - B0 - 2.6:.2f} L{CX + 0.35:.2f},{CY - B0 + 0.3:.2f} L{CX - 0.35:.2f},{CY - B0 + 0.3:.2f} Z"/>')
# jama brzuszna (zawartość)
cav = [E(t, -0.05) for t in range(-90, 46, 4)] + [(CX + 13.2, 35.4), (CX + 9.0, 35.2), (CX + 5.4, 36.0), (CX + 4.4, 34.8),
       (CX + 3.6, 31.0), (CX, 29.6), (CX - 3.6, 31.0), (CX - 4.4, 34.8), (CX - 5.4, 36.0), (CX - 9.0, 35.2), (CX - 13.2, 35.4)] \
      + [E(t, -0.05) for t in range(134, 271, 4)]
f.add(f'<path class="organ" d="{poly(cav)}"/>')
f.text(CX, CY - 1.0, 'jama brzuszna', cls='notec')
f.text(CX, CY + 1.6, 'ciśnienie rośnie', cls='notec')
# strzałki skurczu (sznurowanie ku środkowi)
for t in (-30, 10, 190, 150):
    p0 = E(t, -0.7)
    p1 = E(t, -5.8)
    f.arrow(f'M{p0[0]:.2f},{p0[1]:.2f} L{p1[0]:.2f},{p1[1]:.2f}')
for s in (-1, 1):
    p0 = (CX + s * 4.4, CY - B0 + 0.9)
    f.arrow(f'M{p0[0]:.2f},{p0[1]:.2f} L{p0[0]:.2f},{p0[1] + 4.4:.2f}')

# podpisy wstawki
pt = E(16, 0.375)
f.label(pt, 'm. poprzeczny brzucha', 'm. transversus abdominis', (113.0, 52.6), side='R')
f.text(113.7, 59.2, 'włókna biegną poprzecznie –')
f.text(113.7, 61.8, 'największy udział w tłoczni')
po = E(196, 2.1)
f.label(po, 'm. skośny zewnętrzny brzucha', 'm. obliquus externus abdominis', (101.0, 68.0), side='R')

# ---------- legenda ----------
LY = 80.0
lx = 96.0
f.arrow(f'M{lx:.2f},{LY - 0.6:.2f} L{lx + 6.6:.2f},{LY - 0.6:.2f}')
f.text(lx + 8.0, LY + 0.3, 'skurcz mięśni – nacisk')
f.text(lx + 8.0, LY + 2.9, 'na zawartość jamy brzusznej')
f.arrow(f'M{lx:.2f},{LY + 6.4:.2f} L{lx + 6.6:.2f},{LY + 6.4:.2f}', red=True)
f.text(lx + 8.0, LY + 7.3, 'płuca (powietrze zatrzymane)')
f.text(lx + 8.0, LY + 9.9, 'podpierają przeponę')

# przycięcie u góry (szyja)
body = ''.join(f.body)
f.body = [f'<defs><clipPath id="cp_przepona_brzuch"><rect x="0" y="{YTOP:.2f}" width="{W}" height="{H - YTOP:.2f}"/>'
          f'</clipPath></defs><g clip-path="url(#cp_przepona_brzuch)">{body}</g>']
f.save()
print('ok')
