# TRZY MIĘŚNIE PŁASKIE BRZUCHA – przyczepy i kierunek włókien. Trzy panele, ten sam schemat lewej strony tułowia
# w widoku z boku (przód w lewo; ściana przednia z pochewką m. prostego widoczna z ukosa jako pas przy przednim brzegu).
# Wg Bochenka t. I:
#  m. skośny zewnętrzny (s. 704–706): najczęściej 8 wiązek z pow. zewnętrznej żeber V–XII; włókna skośnie do przodu
#    i ku dołowi; część mięsista kończy się linią pionową (bocznie od m. prostego), która nieco powyżej kolca biodrowego
#    przedniego górnego załamuje się w linię poziomą („kąt mięśniowy”); rozcięgno → blaszka przednia pochewki, kresa
#    biała; dolne pęczki → więzadło pachwinowe; najbardziej tylne i dolne włókna → warga zewnętrzna grzebienia
#    biodrowego; brzeg tylny wolny (trójkąt lędźwiowy).
#  m. skośny wewnętrzny (s. 707): z powięzi piersiowo-lędźwiowej, kresy pośredniej grzebienia, bocznych ⅔ więzadła
#    pachwinowego; włókna tylne ku górze i do przodu → brzegi dolne żeber XII–X; główna masa rozbieżnie przyśrodkowo:
#    górne wstępują równolegle do końców chrząstek X–VIII, środkowe poziomo, dolne nieco ku dołowi; bocznie od
#    m. prostego linią łukowatą przechodzą w rozcięgno (pochewka m. prostego, kresa biała).
#  m. poprzeczny (s. 708): 6 zębów z pow. wewnętrznej chrząstek żebrowych VII–XII (między zębami przepony), linia
#    połączenia blaszek powięzi piersiowo-lędźwiowej, warga wewnętrzna grzebienia, boczna połowa więzadła pachwinowego;
#    włókna poprzecznie do kresy półksiężycowatej (wklęsłej, najgłębiej ku pępkowi), tam rozcięgno.
# Kolejność warstw na żebrach: m. skośny zewn. NA żebrach (pow. zewnętrzna), wewn. KOŃCZY SIĘ na brzegach dolnych,
# poprzeczny POD chrząstkami (pow. wewnętrzna) – stąd kolejność rysowania mięśnia i żeber w panelach.
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig

W, H = 160, 122
PW = 160.0 / 3                       # szerokość panelu
f = Fig('mm_brzucha_przyczepy', W, H,
        caption='trzy mięśnie płaskie brzucha – lewa strona tułowia, widok z boku (przód w lewo); schemat')


# ---------------------------------------------------------------- pomocnicze
def cr(pts, n=10, t=0.5):
    m = len(pts)
    if m < 3:
        out = []
        for i in range(m - 1):
            for k in range(n):
                u = k / n
                out.append((pts[i][0] + (pts[i + 1][0] - pts[i][0]) * u, pts[i][1] + (pts[i + 1][1] - pts[i][1]) * u))
        return out + [pts[-1]]
    PP = [pts[0]] + pts + [pts[-1]]
    out = []
    for i in range(1, m):
        p0, p1, p2, p3 = PP[i - 1], PP[i], PP[i + 1], PP[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) * t / 3, p1[1] + (p2[1] - p0[1]) * t / 3)
        c2 = (p2[0] - (p3[0] - p1[0]) * t / 3, p2[1] - (p3[1] - p1[1]) * t / 3)
        for k in range(n):
            u = k / n
            a = (1 - u) ** 3; b = 3 * u * (1 - u) ** 2; c = 3 * u * u * (1 - u); d = u ** 3
            out.append((a * p1[0] + b * c1[0] + c * c2[0] + d * p2[0], a * p1[1] + b * c1[1] + c * c2[1] + d * p2[1]))
    out.append(pts[-1])
    return out


def offset(pl, d):
    out = []
    for i, p in enumerate(pl):
        a = pl[max(i - 1, 0)]; b = pl[min(i + 1, len(pl) - 1)]
        tx, ty = b[0] - a[0], b[1] - a[1]
        L = math.hypot(tx, ty) or 1
        dd = d(i / (len(pl) - 1)) if callable(d) else d
        out.append((p[0] + ty / L * dd, p[1] - tx / L * dd))
    return out


def ribbon(center, w, n=10):
    c = cr(center, n=n)
    return offset(c, w / 2) + offset(c, -w / 2)[::-1]


def inside(p, poly_):
    x, y = p; c = False
    for (x1, y1), (x2, y2) in zip(poly_, poly_[1:] + poly_[:1]):
        if (y1 > y) != (y2 > y):
            if x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
                c = not c
    return c


def interp_y(line, x):
    """y linii (lista punktów) dla danego x"""
    for (x0, y0), (x1, y1) in zip(line, line[1:]):
        if (x0 - x) * (x1 - x) <= 0 and x0 != x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return None


class Panel:
    def __init__(self, px):
        self.px = px

    def T(self, p):
        return (self.px + p[0], p[1])

    def poly(self, pts, close=True):
        return 'M' + ' L'.join(f'{x + self.px:.2f},{y:.2f}' for x, y in pts) + (' Z' if close else '')

    def add(self, cls, pts, close=True, style=None):
        st = f' style="{style}"' if style else ''
        f.add(f'<path class="{cls}"{st} d="{self.poly(pts, close)}"/>')

    def fibers(self, region, lines, cls='musclel', step=0.25):
        """rysuje odcinki linii (listy punktów) obcięte do wnętrza wielokąta region"""
        for ln in lines:
            pts = cr(ln, n=12) if len(ln) > 2 else ln
            # zagęszczenie
            dense = []
            for a, b in zip(pts, pts[1:]):
                n = max(1, int(math.dist(a, b) / step))
                for k in range(n):
                    dense.append((a[0] + (b[0] - a[0]) * k / n, a[1] + (b[1] - a[1]) * k / n))
            dense.append(pts[-1])
            seg = []
            for p in dense:
                if inside(p, region):
                    seg.append(p)
                else:
                    if len(seg) > 3:
                        self.add(cls, seg, close=False)
                    seg = []
            if len(seg) > 3:
                self.add(cls, seg, close=False)


# ---------------------------------------------------------------- wspólny szkielet (współrzędne panelu)
FRONT = [(9.0, 24.0), (7.8, 34.0), (6.4, 46.0), (5.6, 58.0), (5.6, 68.0), (6.6, 78.0), (8.8, 88.0), (11.0, 95.6)]
SHW = 3.6                                   # pas pochewki m. prostego (ściana przednia widziana z ukosa)
front = cr(FRONT, n=10)
sheath_back = [(x + SHW, y) for x, y in front]


def sb_x(y):
    return interp_y([(q[1], q[0]) for q in sheath_back], y)


RIBS = {}
for i, k in enumerate(['V', 'VI', 'VII', 'VIII', 'IX', 'X']):
    yb = 17.0 + 5.0 * i
    xj, yj = 22.6 + 2.5 * i, 28.0 + 6.0 * i
    bone = [(50.0, yb), (37.0, yb + 0.48 * (yj - yb) + 1.0), (xj, yj)]
    RIBS[k] = [bone, None]
RIBS['V'][1] = [(22.6, 28.0), (16.4, 28.8), (11.6, 27.6)]
RIBS['VI'][1] = [(25.1, 34.0), (19.0, 34.6), (13.6, 32.6), (11.4, 30.8)]
RIBS['VII'][1] = [(27.6, 40.0), (21.6, 40.2), (16.4, 37.6), (12.6, 33.4)]
RIBS['VIII'][1] = [(30.1, 46.0), (25.0, 45.8), (20.8, 43.0), (17.6, 39.6)]
RIBS['IX'][1] = [(32.6, 52.0), (28.4, 51.8), (24.8, 49.0), (21.8, 45.0)]
RIBS['X'][1] = [(35.1, 58.0), (31.6, 58.2), (28.4, 55.4), (25.8, 51.2)]
RIBS['XI'] = [[(50.0, 47.0), (44.6, 53.4), (40.4, 59.6)], None]
RIBS['XII'] = [[(50.0, 52.0), (47.6, 57.0), (45.6, 61.0)], None]
RW, CWD = 2.5, 2.1
ORDER = ['V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']


def rib_line(k):
    b, c = RIBS[k]
    return cr(b, n=12) + (cr(c, n=12)[1:] if c else [])


def rib_lower(k):
    return offset(rib_line(k), -RW / 2)


CREST = [(50.0, 76.6), (43.0, 73.8), (36.0, 73.0), (29.0, 74.6), (24.2, 77.8), (21.0, 81.6)]
ASIS = CREST[-1]
CRW = 2.6
crest = cr(CREST, n=10)
crest_in = offset(crest, -CRW / 2)          # warga wewnętrzna – dalsza (przyśrodkowa), w rzucie górna linia
crest_out = offset(crest, CRW / 2)          # warga zewnętrzna – bliższa (boczna), w rzucie dolna linia
TUB = (14.4, 93.2)                          # guzek łonowy
LIG = [ASIS, ((ASIS[0] + TUB[0]) / 2 + 0.5, (ASIS[1] + TUB[1]) / 2 + 0.2), TUB]
FASC_X = 46.6
Y_BOT = 99.2


def lig_pt(t):
    return (ASIS[0] + (TUB[0] - ASIS[0]) * t, ASIS[1] + (TUB[1] - ASIS[1]) * t)


def skeleton_back(P):
    # kość miedniczna z boku: talerz poniżej grzebienia, kolce przednie, panewka, gałąź górna kości łonowej (odcięta u dołu)
    hip = (crest_out + [(21.8, 84.0), (21.0, 86.0), (22.2, 88.4), (24.0, 91.2), (19.6, 92.6), (15.6, 93.0), (13.6, 94.2),
                              (12.2, Y_BOT), (50.0, Y_BOT), (50.0, crest_out[0][1])])
    P.add('bone', hip)
    f.add(f'<circle class="bone2" cx="{P.px + 30.6:.2f}" cy="95.4" r="4.4"/>')      # panewka
    f.add(f'<circle class="bonel" cx="{P.px + 30.6:.2f}" cy="95.4" r="3.2"/>')
    P.add('bonel', [(38.0, 82.0), (42.0, 79.6), (47.0, 78.8)], close=False)      # kresa pośladkowa (szczegół)
    # pas pochewki m. prostego (ściana przednia) i powięź piersiowo-lędźwiowa (z tyłu)
    P.add('tendon', [p for p in front if p[1] >= 26.0] + [p for p in sheath_back if p[1] >= 26.0][::-1])
    P.add('tendon', [(FASC_X, interp_y(crest_in, FASC_X) + 0.2), (FASC_X, 59.0), (50.0, 56.6), (50.0, crest_in[0][1])])
    # dolny koniec mostka z wyrostkiem mieczykowatym (widok z boku)
    P.add('bone', [(8.4, 15.0), (11.6, 15.0), (12.0, 28.0), (11.0, 33.4), (10.0, 34.6), (9.4, 30.0), (9.0, 24.0)])


def ribs(P, which=ORDER):
    for k in which:
        b, c = RIBS[k]
        P.add('bone', ribbon(b, RW, n=8))
        if k in ('XI', 'XII'):
            tip = b[-1]
            f.add(f'<circle class="bone" cx="{tip[0] + P.px:.2f}" cy="{tip[1]:.2f}" r="{RW / 2:.2f}"/>')
            P.add('bone', ribbon([b[-2], b[-1]], RW - 0.5, n=2), style='stroke:none')
    for k in which[::-1]:
        if RIBS[k][1]:
            P.add('cart', ribbon(RIBS[k][1], CWD, n=8))


def crest_and_lig(P):
    P.add('bone', crest_in + crest_out[::-1])
    P.add('bonel', crest, close=False)                       # kresa pośrednia
    P.add('lig', ribbon(LIG, 1.2, n=4))


def rib_numbers(P, which):
    for k in which:
        b, _ = RIBS[k]
        f.text(P.px + 50.7, b[0][1] + 0.9, k, cls='note')


def title(P, pl, la):
    f.text(P.px + 2.0, 4.0, pl, cls='pl')
    f.text(P.px + 2.0, 6.9, la, cls='la')


ROW1, ROW2 = 103.0, 110.0


def tick(P, t, txt):
    """kreska na więzadle pachwinowym: koniec przyczepu (od kolca biodrowego) + ułamek"""
    a = lig_pt(t)
    d = (TUB[0] - ASIS[0], TUB[1] - ASIS[1]); L_ = math.hypot(*d); n = (d[1] / L_, -d[0] / L_)
    P.add('dim', [(a[0] - n[0] * 1.6, a[1] - n[1] * 1.6), (a[0] + n[0] * 2.2, a[1] + n[1] * 2.2)], close=False, style='stroke-dasharray:none;stroke-width:.35')
    f.text(P.px + a[0] + n[0] * 2.6 + 0.4, a[1] + n[1] * 2.6 + 0.6, txt, cls='note')


# ---------------------------------------------------------------- PANEL 1: m. skośny zewnętrzny
P1 = Panel(0.0)
skeleton_back(P1)
ribs(P1)
crest_and_lig(P1)
TEETH_X = {'V': 20.6, 'VI': 23.6, 'VII': 26.6, 'VIII': 29.6, 'IX': 32.8, 'X': 36.2, 'XI': 41.2, 'XII': 46.4}
serr = []
for i, k in enumerate(ORDER):
    x = TEETH_X[k]
    y = interp_y(rib_line(k), x)
    if i > 0:
        xp = TEETH_X[ORDER[i - 1]]
        yp = interp_y(rib_line(ORDER[i - 1]), xp + 2.0)
        serr.append((xp + 2.0, (yp + y) / 2 + 1.2))            # wcięcie w przestrzeni międzyżebrowej
    serr.append((x, y - 0.5))                                  # ząb na powierzchni zewnętrznej żebra
KM = (14.6, 79.4)                                              # kąt mięśniowy
crest_seg = [p for p in crest_out if 23.6 <= p[0] <= 43.8]
EO = ([(15.2, 30.6)] + serr + [(45.4, 64.0), (44.6, 69.0)] + crest_seg + [(22.8, 80.4), KM, (13.6, 66.0), (13.4, 50.0), (13.8, 38.0)])
APO1 = [(15.2, 30.6), (13.8, 38.0), (13.4, 50.0), (13.6, 66.0), KM, (22.8, 80.4), ASIS, TUB] + [p for p in sheath_back[::-1] if 29.0 <= p[1] <= TUB[1] + 0.6]
P1.add('tendon', APO1)
P1.add('muscle', EO)
dirEO = (-0.62, 0.78)
lines = [[(10.0 + k * 2.4, 18.0), (10.0 + k * 2.4 + dirEO[0] * 100, 18.0 + dirEO[1] * 100)] for k in range(0, 34)]
P1.fibers(EO, lines)
P1.fibers(APO1, lines, cls='tendon')
rib_numbers(P1, ORDER)
title(P1, 'm. skośny zewnętrzny brzucha', 'm. obliquus externus abdominis')
f.label(P1.T((TEETH_X['VII'], interp_y(rib_line('VII'), TEETH_X['VII']))), 'żebra V–XII – pow. zewnętrzna', None, P1.T((15.0, 12.0)), side='R')
f.text(P1.px + 15.7, 15.6, '8 zębów; rozcięgno → blaszka przednia')
f.label(P1.T((36.0, interp_y(crest_out, 36.0))), 'warga zewnętrzna', 'labium externum', P1.T((51.4, ROW1)), side='L')
f.label(P1.T(lig_pt(0.45)), 'więzadło pachwinowe', 'ligamentum inguinale', P1.T((3.0, ROW2)), side='R')
f.text(P1.px + 3.7, ROW2 + 6.2, 'dolne pęczki rozcięgna')

# ---------------------------------------------------------------- PANEL 2: m. skośny wewnętrzny
P2 = Panel(PW - 1.1)
skeleton_back(P2)
crest_and_lig(P2)
lowXII = [p for p in rib_lower('XII') if p[0] <= FASC_X + 0.1]
lowXI = [p for p in rib_lower('XI') if 41.6 <= p[0] <= 46.0]
lowX = [p for p in rib_lower('X') if 21.0 <= p[0] <= 41.0]
ARC_IO = [(20.0, 50.6), (17.6, 58.0), (16.6, 68.0), (16.8, 78.0), (17.6, 88.2)]   # łuk: mięsień → rozcięgno
IOend = lig_pt(0.66)
crest_mid = [p for p in crest if 21.4 <= p[0] <= FASC_X]
IO = (lowXII + [(44.6, 62.4)] + lowXI + [(39.6, 60.8)] + lowX + cr(ARC_IO, n=6)[1:-1] + [IOend, ASIS] + crest_mid[::-1] +
      [(FASC_X, interp_y(crest, FASC_X)), (FASC_X, 59.0)])
APO2 = ([lowX[-1], ARC_IO[0]] + cr(ARC_IO, n=6)[1:-1] + [IOend, TUB] + [p for p in sheath_back[::-1] if 40.0 <= p[1] <= TUB[1] + 0.6])
P2.add('tendon', APO2)
P2.add('muscle', IO)
O = (49.0, 84.0)
lines = []
for ang in range(-178, -106, 6):
    a = math.radians(ang)
    lines.append([O, (O[0] + 90 * math.cos(a), O[1] + 90 * math.sin(a))])
P2.fibers(IO, lines)
P2.fibers(APO2, [[(22.0, y), (4.0, y + (y - 64.0) * 0.14)] for y in [46.0 + 4.0 * k for k in range(12)]], cls='tendon')
ribs(P2)
rib_numbers(P2, ['X', 'XI', 'XII'])
title(P2, 'm. skośny wewnętrzny brzucha', 'm. obliquus internus abdominis')
f.label(P2.T((44.0, interp_y(rib_lower('XI'), 44.0) + 0.3)), 'żebra X–XII – brzegi dolne', None, P2.T((15.0, 12.0)), side='R')
f.text(P2.px + 15.7, 15.6, 'włókna tylne ku górze i do przodu')
f.label(P2.T((48.3, 66.0)), 'powięź piersiowo-lędźwiowa', 'fascia thoracolumbalis', P2.T((51.4, ROW1)), side='L')
f.label(P2.T((31.0, interp_y(crest, 31.0))), 'kresa pośrednia', 'linea intermedia', P2.T((3.0, ROW2)), side='R')
f.text(P2.px + 3.7, ROW2 + 6.2, '+ boczne ⅔ więzadła pachwinowego')
tick(P2, 0.66, '⅔')

# ---------------------------------------------------------------- PANEL 3: m. poprzeczny
P3 = Panel(2 * PW - 2.3)
skeleton_back(P3)
SEMI = [(12.6, 33.0), (15.0, 42.0), (17.6, 52.0), (19.0, 62.0), (19.2, 68.0), (18.6, 76.0), (17.8, 84.0), (17.4, 88.8)]
TAend = lig_pt(0.5)
top = [(13.4, 34.4), (20.0, 38.6), (26.4, 44.0), (32.0, 50.0), (37.4, 55.2), (42.4, 59.4), (FASC_X, 59.6)]
TA = (cr(top, n=6) + [(FASC_X, interp_y(crest_in, FASC_X))] + [p for p in crest_in if 21.0 <= p[0] <= FASC_X] + [ASIS, TAend] +
      cr(SEMI, n=6)[::-1][:-1])
APO3 = cr(SEMI, n=6) + [TAend, TUB] + [p for p in sheath_back[::-1] if 31.0 <= p[1] <= TUB[1] + 0.6]
P3.add('tendon', APO3)
P3.add('muscle', TA)
lines = [[(52.0, y), (4.0, y)] for y in [35.6 + 2.6 * k for k in range(22)]]
P3.fibers(TA, lines)
P3.fibers(APO3, lines, cls='tendon')
crest_and_lig(P3)
ribs(P3)
rib_numbers(P3, ['VII', 'VIII', 'IX', 'X', 'XI', 'XII'])
title(P3, 'm. poprzeczny brzucha', 'm. transversus abdominis')
f.label(P3.T((30.0, 49.4)), 'chrząstki żebrowe VII–XII', None, P3.T((15.0, 12.0)), side='R')
f.text(P3.px + 15.7, 15.6, 'pow. wewnętrzna – 6 zębów')
f.label(P3.T((36.0, interp_y(crest_in, 36.0))), 'warga wewnętrzna', 'labium internum', P3.T((51.4, ROW1)), side='L')
f.label(P3.T((18.4, 78.0)), 'kresa półksiężycowata', 'linea semilunaris', P3.T((3.0, ROW2)), side='R')
f.text(P3.px + 3.7, ROW2 + 6.2, 'tu włókna przechodzą w rozcięgno')
tick(P3, 0.5, '½')

f.save()
print('ok')
