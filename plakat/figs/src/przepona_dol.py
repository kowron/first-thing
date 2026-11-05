# PRZEPONA – widok od dołu i od przodu (od strony jamy brzusznej); przód (mostek) ku górze rysunku,
# prawa strona ciała po lewej stronie rysunku. Schemat własny wg opisu Bochenka s. 690–695.
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth, mirror

W, H = 160, 124
C = 80.0                      # oś pośrodkowa
f = Fig('przepona_dol', W, H, caption='przepona · widok od dołu i od przodu (od strony jamy brzusznej) · rozwór aortowy przed trzonem Th12, nad L1 · prawa strona ciała po lewej')


# ---------- pomocnicze ----------
def cr(pts, closed=True, n=14, t=0.5):
    """punkty na krzywej Catmull-Rom (ta sama krzywa co smooth)."""
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


def ray(poly, o, ang):
    dx, dy = math.cos(ang), math.sin(ang)
    best = None
    for i in range(len(poly)):
        (x1, y1), (x2, y2) = poly[i], poly[(i + 1) % len(poly)]
        ex, ey = x2 - x1, y2 - y1
        den = dx * ey - dy * ex
        if abs(den) < 1e-12:
            continue
        tt = ((x1 - o[0]) * ey - (y1 - o[1]) * ex) / den
        uu = ((x1 - o[0]) * dy - (y1 - o[1]) * dx) / den
        if tt > 0 and 0 <= uu <= 1 and (best is None or tt < best):
            best = tt
    return (o[0] + best * dx, o[1] + best * dy) if best is not None else None


def lerp(a, b, u):
    return (a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u)


def offset(pl, d):
    """przesunięcie łamanej o d wzdłuż normalnej (d>0 – na lewo od kierunku marszu)."""
    out = []
    for i, p in enumerate(pl):
        a = pl[max(i - 1, 0)]; b = pl[min(i + 1, len(pl) - 1)]
        tx, ty = b[0] - a[0], b[1] - a[1]
        L = math.hypot(tx, ty) or 1
        out.append((p[0] - ty / L * d, p[1] + tx / L * d))
    return out


def P(pts):
    return ' '.join(f'{x:.2f},{y:.2f}' for x, y in pts)


def poly_path(pts):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + ' Z'


# ---------- geometria ----------
# obwód (przyczepy do chrząstek żeber VII–XII) – połowa lewa rysunku, od wyrostka mieczykowatego w dół
Lh = [(C, 13.4), (72.0, 13.8), (62.4, 15.6), (53.2, 19.4), (46.0, 24.8), (41.2, 31.8), (38.6, 40.4), (38.2, 49.6),
      (39.6, 58.2), (42.0, 64.6), (44.6, 68.8)]
# brzeg tylny: wzdłuż XII żebra → więz. łukowate boczne (nad m. czworobocznym lędźwi) → przyśrodkowe (nad m. lędźwiowym)
RIBY = lambda x: 66.2 + (C - abs(x - C) and 0) if False else None
LAT = [(49.6, 68.9), (54.5, 66.1), (61.1, 71.6)]          # łuk boczny: XII żebro → wyrostek żebrowy L1
MED = [(61.1, 71.6), (67.3, 66.6), (73.0, 69.6)]           # łuk przyśrodkowy: wyrostek żebrowy L1 → trzon L1
MID = [(76.3, 64.4), (C + 0.4, 61.4), (84.5, 64.4)]        # więz. łukowate pośrodkowe (przed aortą)

def mir(pts):
    return [(2 * C - x, y) for x, y in pts]

LATr, MEDr = mir(LAT), mir(MED)
arcL = cr(LAT, closed=False, n=8) + cr(MED, closed=False, n=8)[1:]
arcR = cr(MEDr[::-1], closed=False, n=8) + cr(LATr[::-1], closed=False, n=8)[1:]

# odnogi – część arkusza mięśniowego (prawa do L3, lewa do L2)
crR_lat = [(73.0, 69.6), (73.3, 76.0), (73.9, 84.0), (74.7, 92.0), (75.6, 98.8)]
crR_med = [(78.2, 98.6), (77.9, 90.0), (77.5, 80.0), (77.0, 70.0), (76.3, 64.4)]
crL_med = [(84.5, 64.4), (83.8, 70.0), (83.4, 76.0), (83.3, 84.0), (83.5, 88.6)]
crL_lat = [(86.0, 88.8), (86.6, 82.0), (87.0, 76.0), (87.0, 69.6)]

outer = (Lh + [(46.6, 68.8)] + arcL + cr(crR_lat, closed=False, n=6)[1:] + [(76.9, 100.2)] + cr(crR_med, closed=False, n=6)
         + cr(MID, closed=False, n=8)[1:] + cr(crL_med, closed=False, n=6)[1:] + [(84.8, 89.8)] + cr(crL_lat, closed=False, n=6)
         + arcR[1:] + [(2 * C - 46.6, 68.8)] + mirror(Lh[1:], C))

# środek ścięgnisty – liść koniczyny (płatek przedni, prawy, lewy)
T = [(C, 23.4), (86.6, 24.0), (91.6, 26.6), (94.0, 30.6), (99.4, 31.4), (105.6, 34.6), (109.8, 40.4), (110.4, 47.0),
     (107.6, 52.6), (102.2, 54.4), (97.6, 51.4), (92.4, 47.2), (86.8, 44.6), (C, 43.2), (73.2, 44.3), (66.8, 47.6),
     (61.0, 52.6), (55.6, 55.6), (50.0, 53.2), (47.4, 47.0), (48.4, 40.4), (53.2, 34.4), (60.0, 31.2), (65.6, 30.4),
     (68.2, 26.4), (73.4, 24.0)]

# ---------- 1. trzony L1–L3 ----------
def body(cy, hw=7.0, hh=4.0):
    pts = [(C - hw, cy - hh + 0.4), (C - hw + 1.2, cy - hh), (C, cy - hh - 0.25), (C + hw - 1.2, cy - hh), (C + hw, cy - hh + 0.4),
           (C + hw - 0.6, cy), (C + hw, cy + hh - 0.4), (C + hw - 1.2, cy + hh), (C, cy + hh + 0.25), (C - hw + 1.2, cy + hh),
           (C - hw, cy + hh - 0.4), (C - hw + 0.6, cy)]
    return smooth(pts, closed=True, t=0.35)

VB = {'L1': 76.0, 'L2': 86.4, 'L3': 96.8}
for k, cy in VB.items():
    f.add(f'<path class="bone" d="{body(cy)}"/>')
for y in (81.2, 91.6, 102.0):
    f.add(f'<rect class="annulus" x="{C - 6.6:.2f}" y="{y - 0.85:.2f}" width="13.2" height="1.7" rx=".5"/>')
f.add(f'<path class="bone" d="M{C - 7:.2f},106.6 L{C - 7:.2f},103.7 Q{C - 7:.2f},102.85 {C - 5.8:.2f},102.85 '
      f'L{C + 5.8:.2f},102.85 Q{C + 7:.2f},102.85 {C + 7:.2f},103.7 L{C + 7:.2f},106.6"/>')

# trzon Th12 (widoczny w rozworze aortowym)
f.add(f'<path class="bone" d="M{C - 6.8:.2f},70.2 L{C - 6.8:.2f},61.5 L{C + 6.8:.2f},61.5 L{C + 6.8:.2f},70.2 Z"/>')
f.add(f'<rect class="annulus" x="{C - 6.6:.2f}" y="{70.85 - 0.85:.2f}" width="13.2" height="1.7" rx=".5"/>')

# ---------- 1b. żebra XII i wyrostki żebrowe L1 (częściowo zakryte) ----------
for s in (-1, 1):
    rib = [(C + s * 12.0, 65.4), (C + s * 20, 66.4), (C + s * 28, 67.7), (C + s * 34.0, 68.7), (C + s * 38.4, 69.6)]
    up = [(x, y - 1.15) for x, y in rib]
    lo = [(x, y + 1.15) for x, y in rib]
    tip = (C + s * 39.7, 70.1)
    f.add(f'<path class="bone" d="{smooth(up + [tip] + lo[::-1], closed=True)}"/>')
for s in (-1, 1):
    pr = [(C + s * 6.6, 72.6), (C + s * 13.8, 72.4), (C + s * 18.4, 71.5), (C + s * 19.8, 72.5), (C + s * 19.2, 74.2),
          (C + s * 13.6, 75.2), (C + s * 6.6, 76.2)]
    f.add(f'<path class="bone" d="{smooth(pr, closed=True, t=0.35)}"/>')

# ---------- 2. arkusz mięśniowy przepony ----------
f.add(f'<path class="muscle" d="{poly_path(outer)}"/>')

# włókna: od obwodu do środka ścięgnistego
ten_poly = cr(T, n=10)
O = (C, 40.0)
fib = []
outer_front = cr(Lh + mirror(Lh[1:], C)[:0], closed=False, n=10)
for deg in list(range(-171, -10, 7)) + [-6, 186, 193]:
    a = math.radians(deg)
    p, q = ray(outer, O, a), ray(ten_poly, O, a)
    if p and q and abs(p[0] - C) > 7.5:
        fib.append((lerp(p, q, 0.05), lerp(q, p, 0.03)))
# część lędźwiowa boczna: od łuków ku płatkom bocznym
for s in (-1, 1):
    arc = arcL if s < 0 else arcR
    for u in (0.08, 0.2, 0.33, 0.47, 0.6, 0.73, 0.86):
        p = arc[int(u * (len(arc) - 1))]
        tgt = (C + s * (abs(p[0] - C) * 0.92 + 2.0), 46.0)
        q = ray(ten_poly, p, math.atan2(tgt[1] - p[1], tgt[0] - p[0]))
        if q:
            fib.append((lerp(p, q, 0.06), lerp(q, p, 0.03)))
# odnogi: włókna ku rozworom i środkowi ścięgnistemu
crus_fib = [((74.6, 90.0), (71.2, 46.0)), ((75.6, 82.0), (74.5, 45.0)), ((76.3, 72.0), (78.4, 47.0)),
            ((76.6, 66.0), (80.4, 54.6)), ((85.4, 86.0), (90.6, 47.6)), ((85.2, 76.0), (88.6, 56.0)), ((84.6, 67.0), (84.0, 56.4))]
for a, b in crus_fib:
    q = ray(ten_poly, a, math.atan2(b[1] - a[1], b[0] - a[0]))
    end = b if (q is None or math.dist(a, q) > math.dist(a, b)) else lerp(q, a, 0.03)
    fib.append((a, end))
for a, b in fib:
    f.add(f'<path class="musclel" d="M{a[0]:.2f},{a[1]:.2f} L{b[0]:.2f},{b[1]:.2f}"/>')

# końce ścięgniste odnóg (na trzonach)
f.add(f'<path class="tendon" d="{smooth([(74.4, 90.5), (78.0, 90.5), (78.2, 98.6), (76.9, 100.2), (75.6, 98.8)], closed=True, t=0.3)}"/>')
f.add(f'<path class="tendon" d="{smooth([(83.3, 84.6), (86.4, 84.6), (86.0, 88.8), (84.8, 89.8), (83.5, 88.6)], closed=True, t=0.3)}"/>')

# środek ścięgnisty
f.add(f'<path class="tendon" d="{smooth(T, closed=True)}"/>')

# ---------- 3. m. lędźwiowy większy i m. czworoboczny lędźwi (wychodzą spod więzadeł łukowatych) ----------
for s in (-1, 1):
    m_b2t = cr(MED, closed=False, n=8)[::-1] if s < 0 else cr(MEDr[::-1], closed=False, n=8)   # od trzonu do wyrostka
    l_t2r = cr(LAT, closed=False, n=8)[::-1] if s < 0 else cr(LATr[::-1], closed=False, n=8)   # od wyrostka do żebra
    psoas = m_b2t + [(C + s * 18.9, 82), (C + s * 19.4, 91.6), (C + s * 8.3, 91.6), (C + s * 7.6, 82)]
    ql = l_t2r + [(C + s * 32.2, 80), (C + s * 32.5, 91.6), (C + s * 21.5, 91.6), (C + s * 21.0, 82)]
    for shp in (psoas, ql):
        f.add(f'<path class="muscle" d="{poly_path(shp)}"/>')
        f.add(f'<path class="shade" d="{poly_path(shp)}"/>')
    for k in (0.3, 0.55, 0.8):
        a = lerp((C + s * 7.6, 76), (C + s * 18.9, 77), k)
        f.add(f'<path class="musclel" d="M{a[0]:.2f},{a[1]:.2f} L{a[0] + s * 0.5:.2f},90.8"/>')
        b = lerp((C + s * 21.0, 76), (C + s * 32.2, 74), k)
        f.add(f'<path class="musclel" d="M{b[0]:.2f},{b[1]:.2f} L{b[0] + s * 0.3:.2f},90.8"/>')

# ---------- 4. otwory ----------
# otwór żyły głównej (granica płatka prawego i przedniego) – ż. główna dolna
f.add('<ellipse class="hole" cx="69.6" cy="35.0" rx="3.3" ry="2.8"/>')
f.add('<ellipse class="vein" cx="69.6" cy="35.2" rx="2.6" ry="2.15"/>')
# rozwór przełykowy – przełyk
for r in (4.7, 5.8):
    f.add(f'<ellipse class="musclel" cx="84.6" cy="50.9" rx="{r:.2f}" ry="{r * 0.86:.2f}"/>')
f.add('<ellipse class="hole" cx="84.6" cy="50.8" rx="3.7" ry="3.1"/>')
f.add('<ellipse class="organ" cx="84.6" cy="51.0" rx="2.9" ry="2.35"/>')
f.add('<ellipse class="cavity" cx="84.6" cy="51.0" rx="1.0" ry="0.55"/>')
# rozwór aortowy – kikut aorty pod więzadłem łukowatym pośrodkowym
f.add('<path class="artery" d="M77.4,62.6 L77.4,67.9 A3.05,1.3 0 0 0 83.5,67.9 L83.5,62.6 Z"/>')
f.add('<ellipse class="artery" cx="80.45" cy="67.9" rx="3.05" ry="1.3"/>')
f.add('<ellipse class="shade" cx="80.45" cy="67.9" rx="3.05" ry="1.3"/>')

# ---------- 5. więzadła łukowate ----------
f.add(f'<path class="lig" d="{smooth([(75.8, 64.9), (77.5, 62.2), (80.4, 61.0), (83.3, 62.2), (85.0, 64.9), (84.0, 65.3), (80.4, 62.5), (76.8, 65.3)], closed=True, t=0.4)}"/>')
for s in (-1, 1):
    med = MED if s < 0 else MEDr
    lat = LAT if s < 0 else LATr
    for arc in (med, lat):
        a_up = cr(arc, closed=False, n=8)
        band = offset(a_up, -0.55 * s * -1) + offset(a_up, 0.55 * s * -1)[::-1]
        f.add(f'<path class="lig" d="{poly_path(band)}"/>')

# ---------- 6. trójkąty – pola bez włókien mięśniowych ----------
for s in (-1, 1):   # lędźwiowo-żebrowe: podstawa na XII żebrze, wierzchołek ku środkowi ścięgnistemu
    tri = [(C + s * 30.0, 67.9), (C + s * 34.0, 68.6), (C + s * 31.6, 62.0)]
    f.add(f'<path class="cavity" d="{poly_path(tri)}"/>')
for s in (-1, 1):   # mostkowo-żebrowe: wąskie szczeliny po bokach części mostkowej
    tri = [(C + s * 4.4, 13.5), (C + s * 7.0, 13.9), (C + s * 5.3, 20.4)]
    f.add(f'<path class="cavity" d="{poly_path(tri)}"/>')
for dx in (-2.4, -0.8, 0.8, 2.4):   # włókna części mostkowej
    f.add(f'<path class="musclel" d="M{C + dx:.2f},14.4 L{C + dx * 1.12:.2f},22.8"/>')

# ---------- 7. łuk żebrowy (chrząstki żeber VII–XII) i wyrostek mieczykowaty ----------
for s in (-1, 1):
    half = Lh if s < 0 else mir(Lh)
    rim = cr(half, closed=False, n=10)
    rim = [p for p in rim if abs(p[0] - C) > 2.6]
    out = offset(rim, 1.9 if s < 0 else -1.9)
    inn = offset(rim, -0.35 if s < 0 else 0.35)
    f.add(f'<path class="cart" d="{poly_path(inn + out[::-1])}"/>')
xi = [(C - 3.0, 7.0), (C + 3.0, 7.0), (C + 2.5, 12.4), (C, 14.4), (C - 2.5, 12.4)]
f.add(f'<path class="bone" d="{smooth(xi, closed=True, t=0.3)}"/>')

# poziomy kręgów
for k, cy in VB.items():
    f.text(C, cy + 0.75, k, cls='notec')

# płatki środka ścięgnistego
f.text(C, 30.2, 'płatek przedni', cls='notec')
f.text(56.0, 46.0, 'płatek prawy', cls='notec')
f.text(102.4, 43.0, 'płatek lewy', cls='notec')

# ---------- podpisy ----------
# lewa strona rysunku (prawa strona ciała)
f.label((78.2, 9.6), 'wyrostek mieczykowaty', 'processus xiphoideus', (52, 4.6), side='L')
f.label((74.7, 16.2), 'trójkąt mostkowo-żebrowy', 'trigonum sternocostale', (52, 13.2), side='L')
f.label((46.2, 34.0), 'część żebrowa', 'pars costalis', (33, 26.0), side='L')
f.label((68.4, 35.6), 'otwór żyły głównej', 'foramen venae cavae', (33, 38.5), side='L')
f.label((41.6, 70.2), 'żebro XII', 'costa XII', (33, 62.5), side='L')
f.label((37.4, 51.0), 'chrząstki żeber VII–XII', 'cartilagines costales', (33, 50.2), side='L')
f.label((54.5, 66.9), 'więzadło łukowate boczne', 'lig. arcuatum laterale', (46, 79.5), side='L')
f.label((67.3, 67.4), 'więzadło łukowate przyśrodkowe', 'lig. arcuatum mediale', (46, 88.5), side='L')
f.label((75.6, 82.5), 'odnoga prawa', 'crus dextrum', (46, 106.5), side='L')
f.label((52.6, 90.8), 'm. czworoboczny lędźwi', 'm. quadratus lumborum', (46, 97.5), side='L')
f.label((68.4, 90.8), 'm. lędźwiowy większy', 'm. psoas major', (46, 115.5), side='L')
# prawa strona rysunku (lewa strona ciała)
f.label((81.6, 18.6), 'część mostkowa', 'pars sternalis', (104, 8.6), side='R')
f.label((97.2, 38.4), 'środek ścięgnisty', 'centrum tendineum', (127, 30.5), side='R')
f.label((86.0, 49.8), 'rozwór przełykowy', 'hiatus esophageus', (127, 46.5), side='R')
f.label((93.4, 60.4), 'część lędźwiowa', 'pars lumbalis', (127, 55.0), side='R')
f.label((111.6, 66.4), 'trójkąt lędźwiowo-żebrowy', 'trigonum lumbocostale', (122, 62.5), side='R')
f.label((80.4, 61.5), 'więzadło łukowate pośrodkowe', 'lig. arcuatum medianum', (114, 79.5), side='R')
f.label((81.8, 66.2), 'rozwór aortowy (Th12)', 'hiatus aorticus', (114, 88.5), side='R')
f.label((85.3, 78.0), 'odnoga lewa', 'crus sinistrum', (114, 97.5), side='R')

f.save()
