# PRZEPONA – część lędźwiowa, więzadła łukowate i otwory. Widok od przodu (od strony jamy brzusznej, trzewia i przednia
# część przepony usunięte); prawa strona ciała po lewej stronie rysunku. U dołu: przekrój poprzeczny przez rozwór aortowy
# na wysokości Th12, widziany od dołu (przód ku górze, prawa strona ciała po lewej).
# Schemat własny wg opisu Bochenka t. I, s. 690–693 i 700–701:
#  – odnoga prawa od trzonów L1–L3, lewa od L1–L2; na wysokości Th12 przechodzą jedna w drugą i z kręgosłupem
#    ograniczają rozwór aortowy (aorta + przewód piersiowy – do tyłu i na prawo od aorty);
#  – więz. łukowate pośrodkowe = przednie ograniczenie rozworu aortowego (z przyśrodkowych brzegów obu odnóg);
#  – więz. łukowate przyśrodkowe: trzon L1 (lub L2) → wyrostek żebrowy L1, nad m. lędźwiowym większym;
#  – więz. łukowate boczne: wyrostek żebrowy L1 → XII żebro, nad m. czworobocznym lędźwi;
#  – rozwór przełykowy: ku górze i nieco na lewo od aortowego, w części lędźwiowej (otoczony włóknami mięśniowymi);
#  – otwór żyły głównej: w środku ścięgnistym, na prawo i do przodu od rozworu przełykowego;
#  – trójkąt lędźwiowo-żebrowy: między częścią lędźwiową a żebrową, nad XII żebrem, wierzchołkiem ku górze.
# Poziomów Th8/Th10 dla otworu ż. głównej i rozworu przełykowego Bochenek nie podaje – nie zaznaczono ich.
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 160, 121
C = 80.0                       # oś w układzie geometrii
K, CN = 0.8, 81.0              # rysunek główny zwężony poziomo (K) i przesunięty na oś CN – miejsce na podpisy
f = Fig('przepona_wiezadla', W, H,
        caption='przepona · więzadła łukowate i otwory · widok od przodu (od strony jamy brzusznej) · prawa strona ciała po lewej')


# ---------------------------------------------------------------- pomocnicze
def cr(pts, closed=False, n=10, t=0.5):
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


def poly(pts):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + ' Z'


def line(pts):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts)


def mir(pts):
    return [(2 * C - x, y) for x, y in pts]


def offset(pl, d):
    out = []
    for i, p in enumerate(pl):
        a = pl[max(i - 1, 0)]; b = pl[min(i + 1, len(pl) - 1)]
        tx, ty = b[0] - a[0], b[1] - a[1]
        L = math.hypot(tx, ty) or 1
        out.append((p[0] - ty / L * d, p[1] + tx / L * d))
    return out


def lerp(a, b, u):
    return (a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u)


def ray(polyg, o, ang):
    dx, dy = math.cos(ang), math.sin(ang)
    best = None
    for i in range(len(polyg)):
        (x1, y1), (x2, y2) = polyg[i], polyg[(i + 1) % len(polyg)]
        ex, ey = x2 - x1, y2 - y1
        den = dx * ey - dy * ex
        if abs(den) < 1e-12:
            continue
        tt = ((x1 - o[0]) * ey - (y1 - o[1]) * ex) / den
        uu = ((x1 - o[0]) * dy - (y1 - o[1]) * dx) / den
        if tt > 1e-6 and 0 <= uu <= 1 and (best is None or tt < best):
            best = tt
    return (o[0] + best * dx, o[1] + best * dy) if best is not None else None


# ---------------------------------------------------------------- geometria (połowa lewa rysunku = prawa strona ciała)
VB = {'Th12': (40.0, 48.0), 'L1': (50.0, 58.0), 'L2': (60.0, 68.0), 'L3': (70.0, 78.0)}
YCUT = 81.0                                   # dolny brzeg rysunku głównego (mięśnie ucięte)


def rib_y(dx):                                # górny brzeg XII żebra w odległości dx od osi
    return 44.2 + (dx - 7.0) / 33.0 * 15.0


TP_TIP = (C - 18.4, 53.9)                     # koniec wyrostka żebrowego L1
MED = [(C - 7.5, 55.0), (C - 10.4, 51.4), (C - 14.2, 50.5), (C - 17.4, 52.2), TP_TIP]          # trzon L1 → wyr. żebrowy L1
R32 = (C - 32.0, rib_y(32.0))
LAT = [TP_TIP, (C - 21.0, 51.0), (C - 25.5, 49.8), (C - 29.6, 51.3), R32]                        # wyr. żebrowy L1 → XII żebro
MID = [(C - 5.3, 45.4), (C - 3.4, 41.0), (C + 0.6, 39.3), (C + 4.6, 41.0), (C + 6.4, 45.4)]    # więz. łukowate pośrodkowe

medL, latL = cr(MED, n=8), cr(LAT, n=8)
medR, latR = mir(medL), mir(latL)                      # strona prawa rysunku – ta sama kolejność (trzon → wyrostek → żebro)

# odnogi: prawa (lewa strona rysunku) do L3, lewa do L2
CR_R_lat = [(C - 7.5, 55.0), (C - 6.6, 62.0), (C - 6.0, 70.0), (C - 5.7, 77.6)]
CR_R_med = [(C - 1.7, 77.9), (C - 2.2, 70.0), (C - 3.0, 60.0), (C - 4.2, 51.0), (C - 5.3, 45.4)]
CR_L_med = [(C + 6.4, 45.4), (C + 5.0, 51.0), (C + 3.9, 58.0), (C + 3.2, 66.4)]
CR_L_lat = [(C + 7.4, 66.6), (C + 7.6, 61.0), (C + 7.5, 55.0)]

# brzeg zewnętrzny (boczny + kopuły) – lewa połowa rysunku od XII żebra ku górze do osi
RIB_TOP = [(C - 32.0, rib_y(32.0)), (C - 36.0, rib_y(36.0)), (C - 39.4, rib_y(39.4))]
SIDE = [(C - 40.8, 57.0), (C - 42.6, 46.0), (C - 43.4, 34.0), (C - 41.8, 22.0), (C - 37.0, 12.6), (C - 29.0, 6.6),
        (C - 19.0, 4.6), (C - 10.0, 6.4), (C, 8.0)]
SIDE_R = [(C + 10.0, 6.8), (C + 19.5, 5.4), (C + 29.5, 7.4), (C + 37.4, 13.4), (C + 42.0, 22.6), (C + 43.4, 34.0),
          (C + 42.6, 46.0), (C + 40.8, 57.0)]

# porządek obwodu (zgodnie z ruchem wskazówek zegara na rysunku): łuk pośrodkowy → odnoga lewa → więzadła prawej strony
# rysunku → bok prawy → kopuły → bok lewy → więzadła lewej strony rysunku → odnoga prawa → z powrotem do łuku

ring = []
ring += cr(MID, n=8)                                                     # (C-5.3,45.4) → (C+6.4,45.4)
ring += cr(CR_L_med, n=6)[1:]                                            # w dół przyśrodkowym brzegiem odnogi lewej
ring += [(C + 5.3, 67.4)]
ring += cr(CR_L_lat, n=6)                                                # w górę bocznym brzegiem odnogi lewej
ring += medR[1:]                                                         # więz. łukowate przyśrodkowe (lewa strona ciała)
ring += latR[1:]                                                         # więz. łukowate boczne
ring += mir(RIB_TOP)[1:]                                                 # wzdłuż XII żebra
ring += cr([mir(RIB_TOP)[-1]] + SIDE_R[::-1], n=8)[1:]                   # bok → kopuła lewa (strona ciała)
ring += cr([(C + 10.0, 6.8), (C, 8.0)] + SIDE[::-1][1:], n=8)[1:]          # siodło → kopuła prawa → bok
ring += cr([SIDE[0]] + RIB_TOP[::-1], n=6)[1:]                           # wzdłuż XII żebra ku osi
ring += latL[::-1][1:]                                                   # więz. łukowate boczne (od żebra do wyrostka)
ring += medL[::-1][1:]                                                   # więz. łukowate przyśrodkowe (do trzonu L1)
ring += cr(CR_R_lat, n=6)[1:]                                            # w dół bocznym brzegiem odnogi prawej
ring += [(C - 3.7, 78.6)]
ring += cr(CR_R_med, n=6)                                                # w górę do łuku pośrodkowego

# środek ścięgnisty (górna część rysunku; dolny brzeg z płatkami)
TEN_LOW = [(C - 33.0, 15.6), (C - 27.0, 20.6), (C - 19.0, 21.4), (C - 12.0, 18.6), (C - 6.8, 15.2), (C, 14.2),
           (C + 6.8, 15.6), (C + 12.6, 19.2), (C + 20.0, 21.8), (C + 28.0, 20.8), (C + 33.6, 16.0)]
TEN_TOP = [(C + 33.6, 16.0), (C + 30.0, 9.8), (C + 20.0, 6.9), (C + 10.0, 8.0), (C, 9.2), (C - 10.0, 7.6),
           (C - 19.0, 6.1), (C - 29.0, 8.4), (C - 33.0, 15.6)]
ten_poly = cr(TEN_LOW, n=8) + cr(TEN_TOP, n=8)[1:-1]

HIO = (C + 3.6, 27.6)                        # rozwór przełykowy
FVC = (C - 9.6, 13.4)                        # otwór żyły głównej

def T(p):
    """punkt z układu geometrii → punkt na rysunku (zwężenie poziome K, oś CN)"""
    return (CN + (p[0] - C) * K, p[1])


f.add(f'<g transform="translate({CN - C * K:.3f},0) scale({K},1)">')

# ---------------------------------------------------------------- 1. kości: XII żebra, wyrostki żebrowe L1, trzony
def body(y0, y1, hw=7.2):
    cy = (y0 + y1) / 2
    pts = [(C - hw, y0 + 0.5), (C - hw + 1.3, y0), (C, y0 - 0.25), (C + hw - 1.3, y0), (C + hw, y0 + 0.5),
           (C + hw - 0.6, cy), (C + hw, y1 - 0.5), (C + hw - 1.3, y1), (C, y1 + 0.25), (C - hw + 1.3, y1),
           (C - hw, y1 - 0.5), (C - hw + 0.6, cy)]
    return smooth(pts, closed=True, t=0.35)


for s in (-1, 1):                                    # XII żebra (od trzonu Th12 ku bokowi i w dół)
    rib = [(C + s * dx, rib_y(dx) + 1.25) for dx in (6.0, 12.0, 20.0, 28.0, 34.0, 39.0)]
    up = [(x, y - 1.25) for x, y in rib]
    lo = [(x, y + 1.25) for x, y in rib]
    tip = (C + s * 40.8, rib_y(40.8) + 1.3)
    f.add(f'<path class="bone" d="{smooth(up + [tip] + lo[::-1], closed=True, t=0.4)}"/>')


def tp(s):                                           # wyrostek żebrowy L1
    return [(C + s * 6.6, 52.6), (C + s * 13.0, 52.8), (C + s * 18.0, 52.6), (C + s * 20.4, 53.6), (C + s * 20.2, 55.8),
            (C + s * 17.8, 56.6), (C + s * 12.6, 56.2), (C + s * 6.6, 56.8)]


for s in (-1, 1):
    f.add(f'<path class="bone" d="{smooth(tp(s), closed=True, t=0.35)}"/>')
for k, (y0, y1) in VB.items():
    f.add(f'<path class="bone" d="{body(y0, y1)}"/>')
for y in (49.0, 59.0, 69.0, 79.0):
    f.add(f'<rect class="annulus" x="{C - 6.9:.2f}" y="{y - 0.85:.2f}" width="13.8" height="1.7" rx=".5"/>')
f.add(f'<path class="bone" d="M{C - 7.2:.2f},{YCUT:.2f} L{C - 7.2:.2f},80.6 Q{C - 7.2:.2f},79.9 {C - 5.9:.2f},79.9 '
      f'L{C + 5.9:.2f},79.9 Q{C + 7.2:.2f},79.9 {C + 7.2:.2f},80.6 L{C + 7.2:.2f},{YCUT:.2f}"/>')

# ---------------------------------------------------------------- 2. m. lędźwiowy większy i m. czworoboczny lędźwi (spod więzadeł)
for s in (-1, 1):
    med = medL if s < 0 else medR                    # trzon → wyrostek
    lat = latL if s < 0 else latR                    # wyrostek → żebro
    psoas = med + [(C + s * 16.4, 57.4), (C + s * 18.0, 66.0), (C + s * 20.6, YCUT), (C + s * 8.0, YCUT), (C + s * 7.6, 66.0)]
    ql = ([(C + s * 20.6, 56.4)] + lat[2:] + [(C + s * 33.2, 62.0), (C + s * 34.4, 72.0), (C + s * 35.0, YCUT),
                                             (C + s * 23.0, YCUT), (C + s * 21.8, 66.0), (C + s * 21.0, 59.0)])
    for shp in (ql, psoas):
        f.add(f'<path class="muscle" d="{poly(shp)}"/>')
        f.add(f'<path class="shade" d="{poly(shp)}"/>')
    for k in (0.25, 0.5, 0.75):                       # przebieg włókien (z góry na dół)
        a = lerp((C + s * 9.0, 56.5), (C + s * 15.6, 57.0), k)
        f.add(f'<path class="musclel" d="M{a[0]:.2f},{a[1]:.2f} L{a[0] + s * (1.0 + 2.6 * k):.2f},{YCUT - 0.3:.2f}"/>')
        b = lerp((C + s * 23.0, 57.5), (C + s * 31.6, 59.0), k)
        f.add(f'<path class="musclel" d="M{b[0]:.2f},{b[1]:.2f} L{b[0] + s * (1.0 + 1.6 * k):.2f},{YCUT - 0.3:.2f}"/>')
# koniec wyrostka żebrowego L1 widoczny między m. lędźwiowym większym a m. czworobocznym lędźwi
for s in (-1, 1):
    tipp = [(C + s * 16.2, 53.0), (C + s * 18.0, 52.6), (C + s * 20.4, 53.6), (C + s * 20.2, 55.8), (C + s * 17.8, 56.6),
            (C + s * 16.4, 56.4)]
    f.add(f'<path class="bone" d="{smooth(tipp, closed=True, t=0.3)}"/>')

# ---------------------------------------------------------------- 3. arkusz mięśniowy przepony
f.add(f'<path class="muscle" d="{poly(ring)}"/>')
# odnogi lekko przyciemnione (pasma mięśniowe na trzonach)
for shp in ([(C - 7.5, 55.0)] + cr(CR_R_lat, n=6)[1:] + [(C - 3.7, 78.6)] + cr(CR_R_med, n=6)[:-2],
            cr(CR_L_med, n=6)[2:] + [(C + 5.3, 67.4)] + cr(CR_L_lat, n=6)):
    f.add(f'<path class="shade" d="{poly(shp)}"/>')

fib = []
for s in (-1, 1):                                    # część lędźwiowa: od więzadeł łukowatych ku środkowi ścięgnistemu
    arcs = (medL + latL[1:]) if s < 0 else (medR + latR[1:])
    for u in (0.1, 0.25, 0.4, 0.55, 0.7, 0.85, 0.97):
        p = arcs[int(u * (len(arcs) - 1))]
        tgt = (C + s * (abs(p[0] - C) * 0.72 + 4.0), 18.0)
        q = ray(ten_poly, p, math.atan2(tgt[1] - p[1], tgt[0] - p[0]))
        if q:
            fib.append((lerp(p, q, 0.04), lerp(q, p, 0.02)))
    for yy in (54.0, 46.0, 38.0, 30.0, 23.0):        # część żebrowa: od boku ku górze i przyśrodkowo
        p = ray(ring, (C + s * 30.0, yy), 0 if s > 0 else math.pi)
        if p:
            tgt = (C + s * 27.0, 12.0)
            q = ray(ten_poly, p, math.atan2(tgt[1] - p[1], tgt[0] - p[0]))
            if q:
                fib.append((lerp(p, q, 0.04), lerp(q, p, 0.02)))
for a, b in fib:
    f.add(f'<path class="musclel" d="M{a[0]:.2f},{a[1]:.2f} L{b[0]:.2f},{b[1]:.2f}"/>')
# włókna odnóg: wzdłuż odnogi ku górze, obok rozworu aortowego, dalej ku rozworowi przełykowemu
for d in (-1.0, 0.0, 1.0):
    pr = [(C - 4.2 + d * 0.9, 66.0), (C - 5.0 + d * 0.9, 56.0), (C - 6.6 + d * 0.8, 47.0), (C - 5.6 + d * 1.2, 38.0),
          (C - 2.0 + d * 1.6, 31.5)]
    pl = [(C + 5.4 + d * 0.8, 58.0), (C + 6.4 + d * 0.8, 51.0), (C + 8.0 + d * 0.8, 45.0), (C + 8.6 + d * 1.2, 38.0),
          (C + 8.8 + d * 1.6, 32.0)]
    for c_ in (pr, pl):
        f.add(f'<path class="musclel" d="{line(cr(c_, n=6))}"/>')
for r in (4.9, 6.1):                                 # pęczki rozstępujące się wokół rozworu przełykowego
    f.add(f'<ellipse class="musclel" cx="{HIO[0]:.2f}" cy="{HIO[1]:.2f}" rx="{r * 0.84:.2f}" ry="{r:.2f}"/>')
for dx in (-5.0, -1.6, 1.8, 5.2):
    a = (HIO[0] + dx * 0.9, HIO[1] - 5.4)
    b = (HIO[0] + dx * 1.6, 15.6 + abs(dx) * 0.2)
    f.add(f'<path class="musclel" d="M{a[0]:.2f},{a[1]:.2f} L{b[0]:.2f},{b[1]:.2f}"/>')
# granica części lędźwiowej i żebrowej (od wierzchołka trójkąta lędźwiowo-żebrowego) – linia pomocnicza
for s in (-1, 1):
    f.add(f'<path class="dim" d="M{C + s * 35.4:.2f},47.0 Q{C + s * 34.0:.2f},32.0 {C + s * 31.0:.2f},{18.6:.2f}"/>')

# ścięgniste końce odnóg na trzonach (prawa – do L3, lewa – do L2)
f.add(f'<path class="tendon" d="{smooth([(C - 6.0, 66.0), (C - 2.4, 66.0), (C - 1.8, 76.4), (C - 3.6, 78.8), (C - 5.6, 76.4)], closed=True, t=0.3)}"/>')
f.add(f'<path class="tendon" d="{smooth([(C + 3.4, 58.6), (C + 7.6, 58.6), (C + 7.4, 65.2), (C + 5.4, 67.6), (C + 3.3, 65.2)], closed=True, t=0.3)}"/>')

# środek ścięgnisty
f.add(f'<path class="tendon" d="{poly(ten_poly)}"/>')

# ---------------------------------------------------------------- 4. otwory
f.add(f'<ellipse class="hole" cx="{FVC[0]:.2f}" cy="{FVC[1]:.2f}" rx="3.6" ry="2.8"/>')        # otwór żyły głównej
f.add(f'<ellipse class="vein" cx="{FVC[0]:.2f}" cy="{FVC[1] + 0.15:.2f}" rx="2.9" ry="2.2"/>')
f.add(f'<ellipse class="hole" cx="{HIO[0]:.2f}" cy="{HIO[1]:.2f}" rx="3.7" ry="3.9"/>')          # rozwór przełykowy
f.add(f'<ellipse class="organ" cx="{HIO[0]:.2f}" cy="{HIO[1] + 0.1:.2f}" rx="2.95" ry="3.1"/>')
f.add(f'<ellipse class="cavity" cx="{HIO[0]:.2f}" cy="{HIO[1] + 0.1:.2f}" rx="0.7" ry="1.2"/>')
# rozwór aortowy – aorta wychodzi spod więzadła łukowatego pośrodkowego (ucięta); niżej widać trzon Th12
f.add(f'<path class="artery" d="M{C - 3.2:.2f},40.4 L{C - 3.2:.2f},43.0 A3.8,1.15 0 0 0 {C + 4.4:.2f},43.0 L{C + 4.4:.2f},40.4 Z"/>')
f.add(f'<ellipse class="artery" cx="{C + 0.6:.2f}" cy="43.0" rx="3.8" ry="1.15"/>')
f.add(f'<ellipse class="shade" cx="{C + 0.6:.2f}" cy="43.0" rx="3.8" ry="1.15"/>')

# ---------------------------------------------------------------- 5. więzadła łukowate (pasma)
mid_c = cr(MID, n=10)
f.add(f'<path class="lig" d="{poly(offset(mid_c, 0.75) + offset(mid_c, -0.75)[::-1])}"/>')
for arc in (medL, latL, medR, latR):
    f.add(f'<path class="lig" d="{poly(offset(arc, 0.65) + offset(arc, -0.65)[::-1])}"/>')

# ---------------------------------------------------------------- 6. trójkąty lędźwiowo-żebrowe (nad XII żebrem)
for s in (-1, 1):
    tri = [(C + s * 33.2, rib_y(33.2) + 0.1), (C + s * 38.6, rib_y(38.6) + 0.1), (C + s * 35.4, 47.2)]
    f.add(f'<path class="cavity" d="{smooth(tri, closed=True, t=0.12)}"/>')

f.add('</g>')

# ---------------------------------------------------------------- 7. napisy w rysunku głównym
for k, (y0, y1) in VB.items():
    x = {'Th12': C + 0.6, 'L1': C + 0.8, 'L2': C + 0.6, 'L3': C + 2.4}[k]
    y = y1 - 0.9 if k == 'Th12' else (y0 + y1) / 2 + 0.75
    f.text(T((x, 0))[0], y, k, cls='notec')
f.text(T((C + 17.0, 0))[0], 13.4, 'środek ścięgnisty', cls='notec')
f.text(T((C - 19.0, 0))[0], 38.6, 'część lędźwiowa', cls='notec')

# ---------------------------------------------------------------- 8. PRZEKRÓJ przez rozwór aortowy (Th12), widok od dołu
A = (CN + 0.6, 96.9)                               # środek aorty
f.text(CN, 85.4, 'przekrój przez rozwór aortowy (Th12) · widok od dołu', cls='notec')


def P(r, deg, o=None):
    o = o or A
    a = math.radians(deg)
    return (o[0] + r * math.cos(a), o[1] + r * math.sin(a))


vb = [(CN - 9.6, 105.9), (CN - 6.0, 103.5), (CN, 103.0), (CN + 6.0, 103.5), (CN + 9.6, 105.9), (CN + 10.2, 109.9),
      (CN + 7.0, 113.4), (CN, 114.0), (CN - 7.0, 113.4), (CN - 10.2, 109.9)]
f.add(f'<path class="bone" d="{smooth(vb, closed=True, t=0.45)}"/>')
f.add(f'<path class="bone2" d="{smooth([(CN - 7.6, 106.9), (CN, 105.2), (CN + 7.6, 106.9), (CN + 8.0, 109.7), (CN, 112.0), (CN - 8.0, 109.7)], closed=True, t=0.45)}"/>')
for s in (-1, 1):                                  # odnogi: półksiężyce po bokach aorty, oparte na trzonie
    inner = [P(4.4, 90 - s * a) for a in (50, 75, 105, 132, 156)]
    tipp = P(5.1, 90 - s * 164)
    outer = [P(7.3, 90 - s * a) for a in (150, 124, 96, 70)]
    base = [(CN + s * 8.0, 105.4), (CN + s * 4.4, 104.0)]
    shp = cr(inner + [tipp] + outer + base, closed=True, n=6)
    f.add(f'<path class="muscle" d="{poly(shp)}"/>')
    for a in (82, 110, 136):
        p, q = P(5.1, 90 - s * a), P(6.7, 90 - s * a)
        f.add(f'<path class="musclel" d="M{p[0]:.2f},{p[1]:.2f} L{q[0]:.2f},{q[1]:.2f}"/>')
lig = [P(4.75, a) for a in range(236, 306, 4)]      # więzadło łukowate pośrodkowe – przednie ograniczenie
f.add(f'<path class="lig" d="{poly(offset(lig, 0.7) + offset(lig, -0.7)[::-1])}"/>')
f.add(f'<circle class="artery" cx="{A[0]:.2f}" cy="{A[1]:.2f}" r="3.5"/>')
f.add(f'<circle class="cavity" cx="{A[0]:.2f}" cy="{A[1]:.2f}" r="2.3"/>')
DT = (CN - 1.6, 101.8)                             # przewód piersiowy – do tyłu i na prawo od aorty
f.add(f'<circle class="organ" cx="{DT[0]:.2f}" cy="{DT[1]:.2f}" r="0.85"/>')
f.text(CN + 0.6, 88.5, 'z przodu: więzadło łukowate pośrodkowe', cls='notec')
f.text(CN - 8.0, 95.2, 'odnoga prawa', cls='note', anchor='end')
f.text(CN + 9.2, 95.2, 'odnoga lewa', cls='note')
f.text(CN, 116.9, 'z tyłu: kręgosłup (trzon Th12)', cls='notec')

# ---------------------------------------------------------------- podpisy
LX, RX = 44.0, 118.0
# lewa kolumna (prawa strona ciała)
f.label(T((FVC[0] - 1.6, FVC[1] + 1.2)), 'otwór żyły głównej', 'foramen venae cavae', (LX, 10.0), side='L')
f.label(T((C - 39.6, 30.0)), 'część żebrowa', 'pars costalis', (LX, 25.0), side='L')
f.label(T((C - 25.5, 49.8)), 'więzadło łukowate boczne', 'lig. arcuatum laterale', (LX, 40.6), side='L')
f.label(T((C - 10.4, 51.6)), 'więzadło łukowate przyśrodkowe', 'lig. arcuatum mediale', (LX, 50.4), side='L')
f.label(T((C - 28.0, 66.0)), 'm. czworoboczny lędźwi', 'm. quadratus lumborum', (LX, 60.4), side='L')
f.label(T((C - 14.0, 67.0)), 'm. lędźwiowy większy', 'm. psoas major', (LX, 70.0), side='L')
f.label(T((C - 3.8, 74.0)), 'odnoga prawa', 'crus dextrum', (LX, 79.6), side='L')
f.label(DT, 'przewód piersiowy', None, (LX, 101.8), side='L')
# prawa kolumna (lewa strona ciała)
f.label(T((HIO[0] + 2.6, HIO[1] - 1.8)), 'rozwór przełykowy', 'hiatus esophageus', (RX, 22.0), side='R')
f.label(T((C + 2.6, 39.5)), 'więzadło łukowate pośrodkowe', 'lig. arcuatum medianum', (RX, 31.0), side='R')
f.label(T((C + 2.8, 42.0)), 'rozwór aortowy', 'hiatus aorticus', (RX, 40.4), side='R')
f.label(T((C + 35.6, 50.6)), 'trójkąt lędźwiowo-żebrowy', 'trigonum lumbocostale', (RX, 49.4), side='R')
f.label(T((C + 39.4, rib_y(39.4) + 1.3)), 'żebro XII', 'costa XII', (RX, 58.6), side='R')
f.label(T((C + 19.2, 54.8)), 'wyrostek żebrowy L1', 'processus costalis', (RX, 67.4), side='R')
f.label(T((C + 5.4, 62.4)), 'odnoga lewa', 'crus sinistrum', (RX, 76.4), side='R')
f.label((A[0] + 3.0, A[1] + 1.4), 'aorta', 'aorta', (RX, 101.0), side='R')

f.save()
print('ok')
