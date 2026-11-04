# STAW KRZYŻOWO-BIODROWY I WIĘZADŁA MIEDNICY – rysunek zbiorczy grupy „Połączenia z kośćmi miednicznymi”.
# A – prawa połowa miednicy z kręgami L4–L5 widziana od tyłu (prawa strona ciała po prawej stronie rysunku): więzadło
#     biodrowo-lędźwiowe, więzadła krzyżowo-biodrowe grzbietowe, więzadło krzyżowo-guzowe (z wyrostkiem sierpowatym),
#     więzadło krzyżowo-kolcowe, otwory kulszowe większy i mniejszy.
# B – przekrój poziomy przez prawy staw krzyżowo-biodrowy (schemat; widok od góry, przód ku górze): od przodu więzadła
#     brzuszne, szczelinowata jama stawowa między powierzchniami uchowatymi (chrząstka grubsza na kości krzyżowej), za nią
#     więzadła międzykostne między guzowatościami, najbardziej z tyłu – więzadła grzbietowe.
# Schemat własny wg opisu Bochenka, t. I, s. 527–532 (ryc. 340–343 oglądane tylko dla położenia struktur); s. 255 (więzadło
# biodrowo-lędźwiowe). Zarys kości krzyżowej – jak w rysunku kr_sacrum_tyl. Nazwy z k_polaczenia.json.
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 150, 112
f = Fig('pol_krzyzowo_biodrowy', W, H,
        caption='A – prawa połowa miednicy z L4–L5, widok od tyłu · B – przekrój poziomy prawego stawu krzyżowo-biodrowego (od góry)')


def poly(pts, closed=True):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + (' Z' if closed else '')


def cr(pts, closed=False, n=10, t=0.5):
    """punkty na krzywej rysowanej przez smooth() (Catmull-Rom)"""
    m = len(pts)
    Q = (pts[-1:] + pts + pts[:2]) if closed else ([pts[0]] + pts + [pts[-1]])
    out = []
    for i in (range(1, m + 1) if closed else range(1, m)):
        p0, p1, p2, p3 = Q[i - 1], Q[i], Q[i + 1], Q[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) * t / 3, p1[1] + (p2[1] - p0[1]) * t / 3)
        c2 = (p2[0] - (p3[0] - p1[0]) * t / 3, p2[1] - (p3[1] - p1[1]) * t / 3)
        for k in range(n):
            u = k / n
            a, b, c, d = (1 - u) ** 3, 3 * u * (1 - u) ** 2, 3 * u * u * (1 - u), u ** 3
            out.append((a * p1[0] + b * c1[0] + c * c2[0] + d * p2[0], a * p1[1] + b * c1[1] + c * c2[1] + d * p2[1]))
    if not closed:
        out.append(pts[-1])
    return out


def offset(pl, d):
    out = []
    for i, p in enumerate(pl):
        a = pl[max(i - 1, 0)]; b = pl[min(i + 1, len(pl) - 1)]
        tx, ty = b[0] - a[0], b[1] - a[1]
        L = math.hypot(tx, ty) or 1
        out.append((p[0] - ty / L * d, p[1] + tx / L * d))
    return out


def mir(pts):
    return [(-x, y) for x, y in pts]


def band(a0, a1, b0, b1, bulge=0.0, n=8):
    """pasmo więzadła: od odcinka a0–a1 (przyczep 1) do odcinka b0–b1 (przyczep 2); bulge – wygięcie boków"""
    def side(p, q, s):
        m = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
        dx, dy = q[0] - p[0], q[1] - p[1]
        L = math.hypot(dx, dy) or 1
        m = (m[0] - dy / L * s, m[1] + dx / L * s)
        return cr([p, m, q], n=n)
    s1 = side(a0, b0, bulge)
    s2 = side(a1, b1, -bulge)
    return s1 + s2[::-1]


def fibers(a0, a1, b0, b1, k=3):
    out = []
    for i in range(1, k + 1):
        u = i / (k + 1)
        p = (a0[0] + (a1[0] - a0[0]) * u, a0[1] + (a1[1] - a0[1]) * u)
        q = (b0[0] + (b1[0] - b0[0]) * u, b0[1] + (b1[1] - b0[1]) * u)
        out.append((p, q))
    return out


# ======================================================================= A. widok od tyłu (mm kości: x – bocznie w prawo, y – w dół)
SA = 0.37
XMIN, YTOP, YBOT = -16.0, -82.0, 159.0
XA, YA = 4.0 - XMIN * SA, 3.0 - YTOP * SA        # x = 0: płaszczyzna pośrodkowa; y = 0: poziom podstawy kości krzyżowej


def PA(x, y):
    return (XA + x * SA, YA + y * SA)


def TA(pts):
    return [PA(x, y) for x, y in pts]


ax0, ay0 = PA(XMIN, YTOP)
ax1, ay1 = PA(140, YBOT)
f.add(f'<defs><clipPath id="cp_kb_a"><rect x="{ax0:.2f}" y="{ay0:.2f}" width="{ax1 - ax0:.2f}" height="{ay1 - ay0:.2f}"/></clipPath></defs>')
f.add('<g clip-path="url(#cp_kb_a)">')

# --- trzony L4, L5 i krążki (w głębi, za łukami)
for y0, y1 in ((-100.0, -58.0), (-46.0, -18.0)):
    f.add(f'<path class="bone" d="{smooth(TA([(-25.0, y0 + 1.0), (0, y0), (25.0, y0 + 1.0), (26.4, (y0 + y1) / 2), (25.0, y1 - 0.6), (0, y1), (-25.0, y1 - 0.6), (-26.4, (y0 + y1) / 2)]))}"/>')
for y0, y1 in ((-58.0, -46.0), (-18.0, -7.0)):
    f.add(f'<path class="annulus" d="{smooth(TA([(-25.0, y0), (0, y0 + 0.3), (25.0, y0), (27.2, (y0 + y1) / 2), (25.0, y1), (0, y1 - 0.3), (-25.0, y1), (-27.2, (y0 + y1) / 2)]))}"/>')

# --- kość krzyżowa (zarys jak kr_sacrum_tyl, tu x > 0 – strona prawa)
TOP = [(0, -7.0), (6.0, -6.9), (10.8, -6.4)]
SAP = [(12.0, -7.4), (13.0, -9.4), (15.2, -10.6), (17.8, -10.6), (20.0, -9.2), (21.3, -6.4), (21.9, -2.6), (22.8, 0.8)]
NOTCH = [(24.8, 2.0), (27.8, 1.2)]
LATT = [(31.2, -1.8), (35.2, -5.8), (39.2, -8.4), (43.4, -8.0), (47.4, -5.2), (50.8, -0.8), (53.3, 4.6), (54.8, 10.5), (55.3, 16.5)]
LAT = [(55.0, 22.0), (53.4, 27.6), (50.8, 33.2), (47.6, 39.0), (44.6, 45.0), (41.6, 51.6), (38.5, 58.6), (35.2, 65.6),
       (31.8, 72.4), (28.4, 78.6), (25.6, 83.2), (23.6, 85.9), (21.6, 87.0), (17.8, 87.7), (14.2, 89.0), (11.6, 91.6), (9.9, 94.6),
       (8.4, 97.2), (4.0, 98.4)]
half = TOP + SAP + NOTCH + LATT + LAT
sac = half + [(0, 98.5)] + mir(half)[::-1][1:]
f.add(f'<path class="bone" d="{smooth(TA(sac))}"/>')
for cx, cy, rx, ry in [(21.5, 23.0, 3.0, 3.9), (19.6, 42.0, 2.8, 3.5), (18.2, 59.5, 2.5, 3.0), (17.0, 74.5, 2.2, 2.6)]:
    for sg in (-1, 1):
        x, y = PA(sg * cx, cy)
        f.add(f'<ellipse class="hole" cx="{x:.2f}" cy="{y:.2f}" rx="{rx * SA:.2f}" ry="{ry * SA:.2f}"/>')
f.add(f'<path class="bonel" d="{poly(TA([(0, 10.0), (0, 72.0)]), closed=False)}"/>')
ICR = [(15.2, 9.6), (15.1, 30.6), (13.8, 42.0), (12.6, 59.5), (11.0, 74.6), (10.0, 81.6)]
LCR = [(29.6, 12.0), (33.0, 23.0), (28.6, 35.0), (30.8, 42.0), (26.6, 53.4), (28.6, 59.5), (24.6, 70.2), (26.2, 74.5), (22.6, 83.4)]
for sg in (-1, 1):
    f.add(f'<path class="bonel" d="{smooth(TA([(sg * x, y) for x, y in ICR]), closed=False)}"/>')
    f.add(f'<path class="bonel" d="{smooth(TA([(sg * x, y) for x, y in LCR]), closed=False)}"/>')
f.add(f'<path class="bone2" d="{smooth(TA([(-5.6, 97.0), (-5.0, 84.0), (-3.4, 75.0), (0, 72.6), (3.4, 75.0), (5.0, 84.0), (5.6, 97.0), (0, 98.6)]))}"/>')
for sg in (-1, 1):
    f.add(f'<path class="bone" d="{smooth(TA([(sg * x, y) for x, y in [(12.0, -7.4), (13.0, -9.4), (15.2, -10.6), (17.8, -10.6), (20.0, -9.2), (21.3, -6.4), (21.9, -2.6), (22.0, 1.5), (20.8, 5.5), (18.4, 8.4), (15.4, 9.4), (13.0, 7.6), (12.0, 4.0), (11.6, -0.5), (11.6, -4.5)]]))}"/>')

# --- kość guziczna
CO = [(0, 99.6), (4.6, 99.4), (8.6, 100.4), (11.4, 101.6), (12.0, 104.0), (9.6, 106.4), (7.8, 108.4), (7.6, 112.0), (6.0, 115.0),
      (5.2, 118.6), (3.8, 122.6), (2.0, 125.6)]
f.add(f'<path class="bone" d="{smooth(TA(CO + [(0, 126.4)] + mir(CO)[::-1][1:-1]))}"/>')
for y in (108.6, 115.4, 121.4):
    f.add(f'<path class="bonel" d="{poly(TA([(-6.0, y), (6.0, y)]), closed=False)}"/>')

# --- kość miedniczna prawa (od tyłu)
PSIS, PIIS = (41.6, 6.0), (50.0, 45.6)
SPINA = (51.0, 103.6)
HIP = [PSIS, (41.4, -4.0), (42.6, -14.0), (44.6, -20.0), (49.0, -28.0), (57.0, -38.6), (68.0, -46.0), (82.0, -51.4), (96.0, -53.0),
       (109.0, -50.0), (119.0, -43.6), (126.0, -33.0), (129.0, -21.0), (128.0, -9.0), (124.6, 1.0), (120.0, 12.0), (115.0, 24.0),
       (112.4, 34.0), (110.0, 44.0), (108.6, 54.0), (110.6, 64.0), (113.0, 76.0), (113.4, 88.0), (110.6, 99.0), (105.0, 108.0),
       (100.0, 118.0), (97.6, 128.0), (97.0, 138.0), (94.4, 147.0), (88.0, 154.0), (79.0, 156.4), (70.0, 155.0), (60.0, 154.0),
       (50.0, 152.0), (42.0, 149.0), (37.6, 145.6), (40.0, 142.0), (46.0, 141.0), (54.0, 140.4), (59.0, 138.0), (60.4, 133.0), (61.6, 124.0), (61.2, 116.0), (58.6, 109.6), (55.0, 106.0), SPINA, (55.4, 100.0),
       (62.0, 94.6), (67.0, 86.0), (69.4, 76.0), (68.6, 66.0), (65.0, 58.0), (59.0, 51.4), (53.0, 48.0), PIIS, (47.6, 38.0),
       (45.6, 30.0), (43.6, 22.0), (42.4, 14.0)]
f.add(f'<path class="bone" d="{smooth(TA(HIP))}"/>')
# brzeg wewnętrzny grzebienia biodrowego, kresa pośladkowa tylna, cień panewki (powierzchnia ucieka ku bokowi)
f.add(f'<path class="bonel" d="{smooth(TA([(44.6, 2.0), (46.0, -12.0), (52.0, -26.0), (60.0, -35.6), (70.0, -42.0), (83.0, -47.0), (96.0, -48.6), (109.0, -45.6), (118.0, -39.6), (124.0, -30.0)]), closed=False)}"/>')
f.add(f'<path class="bonel" d="{smooth(TA([(62.0, -40.0), (60.0, -22.0), (56.0, 0.0), (54.0, 22.0), (53.6, 40.0)]), closed=False)}"/>')
f.add(f'<path class="bonel" d="{smooth(TA([(118.0, -40.0), (104.0, -20.0), (90.0, 6.0), (78.0, 34.0), (72.0, 52.0)]), closed=False)}"/>')
f.add(f'<path class="shade" d="{smooth(TA([(126.0, -33.0), (129.0, -21.0), (128.0, -9.0), (124.6, 1.0), (120.0, 12.0), (115.0, 24.0), (112.4, 34.0), (110.0, 44.0), (106.0, 40.0), (110.0, 26.0), (116.0, 10.0), (121.0, -6.0), (123.0, -22.0)]))}"/>')
f.add(f'<path class="shade" d="{smooth(TA([(108.6, 54.0), (110.6, 64.0), (113.0, 76.0), (113.4, 88.0), (110.6, 99.0), (105.0, 108.0), (101.0, 104.0), (104.6, 92.0), (105.6, 78.0), (104.6, 64.0)]))}"/>')
f.add(f'<path class="bonel" d="{smooth(TA([(66.0, 130.0), (64.6, 141.0), (70.0, 150.6), (81.0, 152.6), (91.0, 146.0), (93.4, 135.0), (88.0, 125.6), (77.0, 122.6)]))}"/>')

# --- przestrzenie międzyłukowe (w głębi)
for pts in ([(-7.0, -54.0), (7.0, -54.0), (9.0, -44.0), (9.4, -42.0), (-9.4, -42.0), (-9.0, -44.0)],
            [(-8.0, -14.6), (8.0, -14.6), (11.0, -7.4), (-11.0, -7.4)]):
    f.add(f'<path class="hole" d="{poly(TA(pts))}"/>')
    f.add(f'<path class="shade" d="{poly(TA(pts))}"/>')

# --- kręgi L5 i L4 od tyłu: blaszki łuku, wyrostki stawowe górne i dolne, wyrostki żebrowe (poprzeczne), wyrostek kolczysty
ARCH = [(0, -41.0), (5.0, -41.4), (9.0, -42.0), (9.6, -48.0), (12.0, -53.0), (16.4, -54.4), (19.6, -51.0), (20.4, -46.0),
        (20.0, -41.4), (26.0, -41.4), (34.0, -41.0), (40.0, -39.4), (44.4, -36.6), (45.2, -32.4), (43.4, -29.4), (36.0, -29.6),
        (28.0, -29.2), (21.6, -28.4), (19.0, -25.0), (18.6, -18.0), (17.4, -9.0), (15.0, -5.0), (12.0, -4.6), (9.8, -7.0),
        (9.2, -13.0), (8.4, -19.0), (5.0, -21.0), (3.6, -20.6), (3.6, -17.0), (2.6, -13.6)]


def arch(dy, tp=1.0, iap_dx=0.0):
    pts = []
    for x, y in ARCH:
        if x > 20.5 and -42.0 < y < -28.0:
            x = 20.5 + (x - 20.5) * tp
        if y > -26.0 and x > 4.0:
            x += iap_dx
        pts.append((x, y + dy))
    return pts + [(0, -13.0 + dy)] + mir(pts)[::-1][1:]


f.add(f'<path class="bone" d="{smooth(TA(arch(0.0)))}"/>')
f.add(f'<path class="bone" d="{smooth(TA(arch(-40.0, 1.05, -2.6)))}"/>')
for dy in (0.0, -40.0):
    f.add(f'<path class="bonel" d="{poly(TA([(0, -38.6 + dy), (0, -16.0 + dy)]), closed=False)}"/>')

# --- otwory kulszowe (prześwit) – pod więzadłami
GSF = cr([PIIS, (53.0, 48.0), (59.0, 51.4), (65.0, 58.0), (68.6, 66.0), (69.4, 76.0), (67.0, 86.0), (62.0, 94.6), (55.4, 100.0),
          (51.0, 102.6), (46.0, 96.0), (38.6, 88.0), (40.6, 76.0), (44.4, 62.0), (47.0, 50.0)], closed=True, n=6)
f.add(f'<path class="hole" d="{poly(TA(GSF))}"/>')
LSF = cr([(52.0, 104.6), (55.0, 106.0), (58.6, 109.6), (61.2, 116.0), (61.6, 124.0), (60.6, 130.0), (55.0, 124.0), (49.6, 116.0),
          (47.0, 109.0)], closed=True, n=6)
f.add(f'<path class="hole" d="{poly(TA(LSF))}"/>')

# --- więzadło krzyżowo-kolcowe (do przodu od krzyżowo-guzowego): od brzegu bocznego dolnej części kości krzyżowej i górnych
#     kręgów guzicznych, zwężając się, do kolca kulszowego
SSP = [(24.0, 78.0), (36.0, 86.0), (46.0, 95.0), (52.2, 101.4), (52.0, 105.2), (42.0, 107.6), (26.0, 108.6), (14.0, 108.0),
       (10.6, 104.4), (16.0, 92.0)]
f.add(f'<path class="lig" d="{smooth(TA(SSP))}"/>')
for p, q in [((22.0, 90.0), (50.6, 102.4)), ((16.0, 100.0), (50.6, 104.0)), ((14.0, 106.0), (49.6, 105.2))]:
    f.add(f'<path class="bonel" d="{poly(TA([p, q]), closed=False)}"/>')

# --- więzadło krzyżowo-guzowe: wachlarzowato od kolców biodrowych tylnych, brzegu bocznego kości krzyżowej i dwóch górnych
#     kręgów guzicznych; zbieżnie w dół, do przodu i bocznie, potem szersze – do guza kulszowego; wyrostek sierpowaty
STB = [(40.0, 26.0), (44.6, 30.0), (47.6, 44.0), (46.0, 58.0), (41.6, 74.0), (37.6, 90.0), (38.6, 102.0), (43.6, 113.0),
       (52.0, 120.0), (58.0, 127.0), (61.6, 132.0), (63.6, 139.0), (60.6, 142.4), (52.0, 143.4), (44.0, 143.8), (38.6, 144.6),
       (40.6, 141.6), (47.0, 140.0), (53.6, 138.6), (56.0, 134.0), (52.0, 128.0), (44.0, 120.0), (34.0, 114.0), (22.0, 110.4), (13.0, 108.4),
       (9.6, 104.0), (14.0, 97.0), (22.0, 88.0), (28.0, 76.0), (33.0, 62.0), (36.0, 48.0), (38.0, 36.0)]
f.add(f'<path class="lig" d="{smooth(TA(STB))}"/>')
for pts in ([(44.0, 36.0), (42.6, 60.0), (37.6, 84.0), (40.6, 104.0), (50.0, 117.0), (59.0, 128.0), (61.6, 142.0)],
            [(39.6, 42.0), (37.0, 64.0), (32.6, 84.0), (35.0, 102.0), (46.0, 116.0), (56.0, 130.0)],
            [(18.0, 106.0), (32.0, 110.0), (44.0, 117.0), (53.0, 127.0), (57.6, 140.0)],
            [(42.0, 142.8), (52.0, 141.6), (59.6, 139.6)]):
    f.add(f'<path class="bonel" d="{smooth(TA(pts), closed=False)}"/>')

# --- więzadła krzyżowo-biodrowe grzbietowe: szereg pasm od grzebieni krzyżowych pośredniego i bocznego skośnie ku górze do
#     talerza kości biodrowej (od kolca tylnego górnego do dolnego); górne – krótsze, bardziej skośne (głębiej), dolne –
#     dłuższe, bardziej strome (powierzchownie)
DORS = [((15.4, 4.0), (16.4, 15.0), (42.0, 8.4), (42.6, 14.6), 0.9),
        ((17.4, 18.0), (19.4, 29.0), (43.0, 16.8), (44.2, 23.4), 0.9)]
for a0, a1, b0, b1, bu in DORS:
    f.add(f'<path class="lig" d="{smooth(TA(band(a0, a1, b0, b1, bu)))}"/>')
    for p, q in fibers(a0, a1, b0, b1, 2):
        f.add(f'<path class="bonel" d="{poly(TA([p, q]), closed=False)}"/>')
LONG = ((23.6, 44.0), (29.0, 60.0), (44.0, 24.0), (47.6, 39.0))
f.add(f'<path class="lig" d="{smooth(TA(band(*LONG, bulge=-0.8)))}"/>')
for p, q in fibers(*LONG, k=3):
    f.add(f'<path class="bonel" d="{poly(TA([p, q]), closed=False)}"/>')

# --- więzadło biodrowo-lędźwiowe: od wyrostków poprzecznych L4 i L5 do tylnej części grzebienia biodrowego; część większa –
#     ku talerzowi i górnej powierzchni części bocznych kości krzyżowej (tu widoczna nad skrzydłem kości krzyżowej)
IL = [((38.0, -79.0), (46.6, -73.4), (59.0, -40.0), (66.0, -45.4), 1.0),
      ((40.6, -38.6), (45.0, -31.0), (46.6, -24.4), (52.0, -33.4), 0.4),
      ((27.0, -29.4), (40.0, -30.0), (31.6, -3.0), (44.0, -7.4), 0.8)]
for a0, a1, b0, b1, bu in IL:
    f.add(f'<path class="lig" d="{smooth(TA(band(a0, a1, b0, b1, bu)))}"/>')
    for p, q in fibers(a0, a1, b0, b1, 2):
        f.add(f'<path class="bonel" d="{poly(TA([p, q]), closed=False)}"/>')
f.add('</g>')
f.text(*PA(-6.2, -31.0), 'L5', cls='notec')
f.text(*PA(-6.2, -71.0), 'L4', cls='notec')
f.text(*PA(122.0, -58.0), 'A', cls='big')

# ======================================================================= B. przekrój poziomy prawego stawu krzyżowo-biodrowego
SB = 0.425
U0, U1, V0, V1 = -2.0, 88.0, -10.0, 72.0
XB, YB0 = 52.0 - U0 * SB, 72.0 - V0 * SB


def PB(x, y):
    return (XB + x * SB, YB0 + y * SB)


def TB(pts):
    return [PB(x, y) for x, y in pts]


bx0, by0 = PB(U0, V0)
bx1, by1 = PB(U1, V1)
f.add(f'<defs><clipPath id="cp_kb_b"><rect x="{bx0:.2f}" y="{by0:.2f}" width="{bx1 - bx0:.2f}" height="{by1 - by0:.2f}" rx="2.2"/></clipPath></defs>')
f.add('<g clip-path="url(#cp_kb_b)">')
JF, JB = (51.0, 12.0), (41.0, 39.0)    # przedni i tylny koniec szpary stawowej (z przodu bocznie, z tyłu przyśrodkowo)


def jline(off, n=24):
    out = []
    for k in range(n + 1):
        u = k / n
        out.append((JF[0] + (JB[0] - JF[0]) * u + 0.8 * math.sin(math.pi * 2 * u), JF[1] + (JB[1] - JF[1]) * u))
    return offset(out, off)


SAC_S = jline(1.25)       # kość krzyżowa pod chrząstką (przyśrodkowo)
SAC_C = jline(-0.15)      # powierzchnia chrząstki na kości krzyżowej (grubsza)
ILI_C = jline(-0.6)       # powierzchnia chrząstki na kości biodrowej
ILI_S = jline(-1.3)       # kość biodrowa pod chrząstką (bocznie)
# kość krzyżowa: trzon S1 i część boczna (przekrój), kanał krzyżowy, grzebienie na powierzchni grzbietowej
SACB = ([(-6.0, -0.4), (0.0, -0.6), (8.0, -0.2), (16.0, 1.2), (22.0, 3.0), (30.0, 5.0), (38.0, 7.0), (45.0, 9.2), (49.6, 10.8)] + SAC_S +
        [(39.4, 41.6), (37.6, 45.0), (34.0, 47.6), (30.6, 49.4), (27.6, 48.0), (22.0, 46.6), (17.0, 46.0), (14.6, 48.4), (12.0, 47.6),
         (8.0, 49.6), (4.0, 51.6), (1.6, 52.4), (1.0, 56.0), (0.0, 58.0), (-6.0, 58.0)])
f.add(f'<path class="bone2" d="{poly(TB(SACB))}"/>')
# zarys trzonu S1 (granica z częścią boczną), kanał krzyżowy, kanał nerwu krzyżowego
f.add(f'<path class="bonel" d="{smooth(TB([(19.0, 2.4), (22.4, 10.0), (22.0, 19.0), (18.0, 25.0), (10.0, 27.6), (0.0, 28.0)]), closed=False)}"/>')
f.add(f'<path class="hole" d="{smooth(TB([(-6.0, 29.6), (0.0, 29.4), (7.0, 29.8), (12.6, 31.4), (10.6, 36.4), (5.6, 41.0), (0.0, 43.6), (-6.0, 43.6)]))}"/>')
f.add(f'<path class="hole" d="{smooth(TB([(20.0, 29.0), (24.4, 27.6), (28.0, 30.6), (26.4, 35.0), (21.6, 35.6), (18.8, 32.6)]))}"/>')
# kość biodrowa: powierzchnia uchowata, guzowatość biodrowa, tylna część (kolce tylne), talerz ku przodowi i bocznie (przecięty)
ILB = (ILI_S[::-1] + [(43.6, 42.6), (46.2, 48.0), (47.0, 54.0), (45.4, 59.0), (41.6, 62.6), (38.4, 65.4), (39.0, 69.4),
                       (45.0, 70.6), (53.0, 67.4), (61.0, 59.0), (68.0, 46.0), (74.0, 32.0), (80.0, 17.0), (86.0, 2.0),
                       (92.0, -12.0), (96.0, -20.0), (86.0, -20.0), (80.0, -14.0), (72.0, -6.6), (64.0, 0.6), (58.0, 6.4), (54.4, 10.0)])
f.add(f'<path class="bone2" d="{poly(TB(ILB))}"/>')
f.add(f'<path class="facet" d="{poly(TB(SAC_S + SAC_C[::-1]))}"/>')
f.add(f'<path class="facet" d="{poly(TB(ILI_C + ILI_S[::-1]))}"/>')
f.add(f'<path class="cavity" d="{poly(TB(SAC_C + ILI_C[::-1]))}"/>')
# więzadła międzykostne – wąska szczelina między guzowatością krzyżową a biodrową; krótkie, krzyżujące się pasma
IO = [SAC_S[-1], (39.4, 41.6), (37.6, 45.0), (35.0, 48.6), (33.6, 52.0), (36.0, 57.0), (40.0, 60.6), (45.4, 59.0), (47.0, 54.0),
      (46.2, 48.0), (43.6, 42.6), ILI_S[-1]]
f.add(f'<path class="lig" d="{poly(TB(IO))}"/>')
for p, q in [((39.0, 43.0), (45.4, 50.0)), ((37.0, 47.0), (46.4, 55.0)), ((35.6, 52.0), (43.6, 59.0)), ((44.6, 44.6), (37.6, 51.0)),
             ((46.0, 50.0), (36.4, 56.0)), ((46.0, 55.6), (40.0, 59.6))]:
    f.add(f'<path class="bonel" d="{poly(TB([p, q]), closed=False)}"/>')
# więzadła grzbietowe – najbardziej z tyłu: od grzebieni krzyżowych do tylnej części kości biodrowej
DO = cr([(12.0, 48.0), (20.0, 47.4), (28.0, 48.8), (33.6, 52.0), (36.0, 57.0), (40.0, 60.6), (38.4, 65.4), (36.6, 66.6),
         (30.0, 62.0), (22.0, 57.4), (14.0, 54.0), (9.6, 51.4)], closed=True, n=5)
f.add(f'<path class="lig" d="{poly(TB(DO))}"/>')
for p, q in [((14.0, 50.4), (37.4, 63.6)), ((22.0, 51.0), (38.6, 61.6))]:
    f.add(f'<path class="bonel" d="{poly(TB([p, q]), closed=False)}"/>')
# więzadła brzuszne – cienkie pasma na przodzie stawu: od powierzchni miednicznej części bocznej kości krzyżowej do przedniego
# brzegu powierzchni uchowatej kości biodrowej
VE = cr([(38.0, 6.6), (45.0, 8.4), (51.0, 10.6), (56.0, 8.6), (61.0, 4.6), (62.0, 2.6), (56.6, 5.6), (51.4, 7.6), (45.0, 5.8), (38.6, 4.4)],
        closed=True, n=5)
f.add(f'<path class="lig" d="{poly(TB(VE))}"/>')
f.add(f'<path class="bonel" d="{poly(TB([(40.0, 5.6), (51.0, 9.0), (59.0, 5.0)]), closed=False)}"/>')
f.add('</g>')
f.add(f'<rect x="{bx0:.2f}" y="{by0:.2f}" width="{bx1 - bx0:.2f}" height="{by1 - by0:.2f}" rx="2.2" class="dim"/>')
f.text(*PB(2.0, 16.0), 'kość krzyżowa', cls='note')
f.text(*PB(53.0, 36.2), 'kość', cls='note')
f.text(*PB(48.0, 42.0), 'biodrowa', cls='note')
f.text(bx0 + 0.8, by1 - 1.6, 'B', cls='big')

# ======================================================================= podpisy
TR = XA + 131 * SA + 3.0
# A – wszystkie podpisy w prawej kolumnie (kolejność wg wysokości)
f.label(PA(48.0, -62.0), 'więzadło biodrowo-lędźwiowe', 'ligamentum iliolumbale', (TR, 5.0), side='R')
f.label(PA(41.8, 3.0), 'kolec biodrowy tylny górny', 'spina iliaca posterior superior', (TR, 12.0), side='R')
f.label(PA(30.0, 18.6), 'więzadła krzyżowo-biodrowe grzbietowe', 'ligamenta sacroiliaca dorsalia', (TR, 19.0), side='R')
f.label(PA(50.4, 44.6), 'kolec biodrowy tylny dolny', 'spina iliaca posterior inferior', (TR, 26.0), side='R')
f.label(PA(58.0, 72.0), 'otwór kulszowy większy', 'foramen ischiadicum majus', (TR, 33.0), side='R')
f.label(PA(44.0, 100.0), 'więzadło krzyżowo-kolcowe', 'ligamentum sacrospinale', (TR, 40.0), side='R')
f.label(PA(55.6, 117.0), 'otwór kulszowy mniejszy', 'foramen ischiadicum minus', (TR, 47.0), side='R')
f.label(PA(59.0, 129.0), 'więzadło krzyżowo-guzowe', 'ligamentum sacrotuberale', (TR, 54.0), side='R')
f.label(PA(84.0, 140.0), 'guz kulszowy', 'tuber ischiadicum', (TR, 61.0), side='R')
# B – podpisy po prawej stronie wstawki
TRB = bx1 + 2.4
f.label(PB(54.0, 7.4), 'więzadła krzyżowo-biodrowe brzuszne', 'ligamenta sacroiliaca ventralia', (TRB, 72.0), side='R')
f.label(PB(48.4, 20.0), 'jama stawowa', 'cavitas articularis', (TRB, 79.5), side='R')
f.label(PB(43.6, 31.0), 'powierzchnia uchowata', 'facies auricularis', (TRB, 87.0), side='R')
f.label(PB(41.0, 52.0), 'więzadła krzyżowo-biodrowe międzykostne', 'ligamenta sacroiliaca interossea', (TRB, 94.5), side='R')
f.label(PB(30.0, 60.0), 'więzadła krzyżowo-biodrowe grzbietowe', 'ligamenta sacroiliaca dorsalia', (TRB, 102.0), side='R')
f.save()
