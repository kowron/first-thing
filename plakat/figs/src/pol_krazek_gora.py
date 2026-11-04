# KRĄŻEK MIĘDZYKRĘGOWY – przekrój poziomy części lędźwiowej kręgosłupa na wysokości krążka, widok od góry
# (przód ku górze; prawa strona ciała po prawej stronie rysunku).
# Schemat własny wg opisu Bochenka, t. I, s. 249–253 (ryc. 165 tylko do orientacji); nazwy z k_polaczenia.json.
# Pokazane: krążek (pierścień włóknisty z koncentrycznymi blaszkami, jądro miażdżyste ekscentrycznie – bliżej tyłu),
# więzadło podłużne przednie i tylne, kanał kręgowy i otwory międzykręgowe (w głąb – cień), stawy międzykręgowe
# (wyrostki stawowe górne kręgu niższego, dolne kręgu wyższego), więzadła żółte i wyrostek kolczysty (przekrój).
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth, mirror

W, H = 150, 94
S = 1.0                   # mm rysunku / mm kości
CX, OY = 75.0, 7.5        # oś pośrodkowa; przedni brzeg krążka
f = Fig('pol_krazek_gora', W, H,
        caption='krążek międzykręgowy części lędźwiowej · przekrój poziomy · widok od góry (przód ku górze)')


def P(x, y):
    return (CX + x * S, OY + y * S)


def T(pts):
    return [P(x, y) for x, y in pts]


def cr(pts, closed=True, n=12, t=0.5):
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
    """przesunięcie łamanej o d wzdłuż normalnej (d>0 – w prawo od kierunku marszu, układ y w dół)"""
    out = []
    for i, p in enumerate(pl):
        a = pl[max(i - 1, 0)]; b = pl[min(i + 1, len(pl) - 1)]
        tx, ty = b[0] - a[0], b[1] - a[1]
        L = math.hypot(tx, ty) or 1
        out.append((p[0] - ty / L * d, p[1] + tx / L * d))
    return out


def poly(pts, closed=True):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + (' Z' if closed else '')


def sym(half):
    """połowa prawa (od przodu linii pośrodkowej do tyłu) → pełny kontur symetryczny"""
    return half + mirror(half, 0)[1:-1]


def radial(pts_closed, c, nang=240):
    """promień konturu (gęsto próbkowanego) w funkcji kąta wokół punktu c"""
    pol = []
    for x, y in pts_closed:
        pol.append((math.atan2(y - c[1], x - c[0]), math.hypot(x - c[0], y - c[1])))
    pol.sort()
    out = []
    for k in range(nang):
        a = -math.pi + 2 * math.pi * k / nang
        # interpolacja liniowa po kącie (z zawinięciem)
        j = 0
        while j < len(pol) and pol[j][0] < a:
            j += 1
        a0, r0 = pol[j - 1] if j > 0 else (pol[-1][0] - 2 * math.pi, pol[-1][1])
        a1, r1 = pol[j] if j < len(pol) else (pol[0][0] + 2 * math.pi, pol[0][1])
        u = (a - a0) / (a1 - a0) if a1 != a0 else 0
        out.append((a, r0 + (r1 - r0) * u))
    return out


# ================= geometria (mm kości; x – w prawo, y – ku tyłowi; 0,0 = przedni brzeg krążka) =================
disc_R = [(0, 0), (7.0, 0.35), (13.0, 1.5), (18.0, 3.5), (21.8, 6.6), (24.2, 10.6), (25.2, 15.2), (25.0, 19.8),
          (23.6, 24.2), (20.8, 28.0), (16.8, 30.6), (12.0, 31.6), (7.0, 31.0), (3.2, 30.0), (0, 29.7)]
disc = sym(disc_R)
nuc_R = [(0, 12.4), (4.6, 12.8), (8.4, 14.2), (10.6, 16.7), (10.9, 19.6), (9.2, 22.3), (5.6, 23.8), (0, 24.1)]
nuc = sym(nuc_R)
NC = (0.0, 18.4)          # środek jądra – ekscentrycznie, bliżej brzegu tylnego

DY = -2.6                 # elementy tylne bliżej krążka (kanał trójkątny, spłaszczony przednio-tylnie)


def sh(pts):
    return [(x, y + DY) for x, y in pts]


# --- tylna część łuku kręgu wyższego (przekrój): wyrostki stawowe dolne + blaszki + wyrostek kolczysty ---
arch_R = [(0, 53.0), (4.0, 51.6), (8.0, 49.3), (10.9, 46.4), (12.3, 43.0), (13.3, 40.5), (15.2, 41.5), (16.3, 44.3),
          (15.8, 47.6), (14.4, 50.5), (12.2, 53.3), (8.6, 55.7), (5.2, 57.6), (3.1, 60.0), (2.8, 65.0), (3.0, 70.5),
          (3.5, 74.6), (2.7, 77.6), (0, 78.3)]
arch_R = sh(arch_R)
arch = sym(arch_R)
# powierzchnia stawowa wyrostka stawowego dolnego (wypukła, zwrócona do przodu i bocznie)
iap_face = cr(sh([(13.3, 40.5), (15.2, 41.5), (16.3, 44.3), (15.8, 47.6), (14.4, 50.5)]), closed=False, n=10)
GAP = 1.05                 # szerokość szpary stawowej
sap_face = offset(iap_face, -GAP)          # powierzchnia wyrostka stawowego górnego (wklęsła, ku tyłowi i przyśrodkowo)
# wyrostek stawowy górny kręgu niższego (przekrój): część przednia obejmuje od przodu wyrostek dolny
sap_outer = [(14.6, 52.3), (16.4, 53.8), (19.4, 52.8), (22.3, 50.2), (24.1, 46.5), (24.7, 42.4), (23.9, 38.8),
             (21.7, 36.6), (18.0, 35.7), (14.2, 36.5), (11.6, 38.0), (10.7, 39.6)]
sap_outer = sh(sap_outer)
sap_R = cr(sap_outer, closed=False, n=8) + [(11.6, 40.2 + DY)] + sap_face[::-1][:-1] + [(sap_face[-1][0] + 0.1, sap_face[-1][1] + 0.6)]

# --- więzadło żółte (prawa połowa): wzdłuż przedniej powierzchni blaszki aż do wyrostka stawowego górnego ---
flav_R = [(0, 52.6), (4.0, 51.2), (8.0, 48.9), (10.8, 45.9), (12.0, 42.6), (12.0, 40.4), (11.2, 38.9), (10.0, 39.0),
          (9.2, 41.6), (7.6, 44.6), (4.8, 47.2), (1.6, 49.2), (0.45, 50.0), (0, 51.0)]
flav_R = sh(flav_R)

# --- kanał kręgowy + otwory międzykręgowe (cień – przestrzeń w głąb) ---
canal_R = [(0, 29.0), (6.0, 30.2), (12.0, 31.2), (16.8, 30.0), (20.6, 27.4), (22.4, 25.6), (21.0, 29.6), (21.0, 33.0),
           (22.2, 35.4), (18.0, 33.4), (12.5, 35.0), (10.4, 37.4), (8.6, 40.8), (4.6, 44.4), (1.0, 46.9), (0, 47.9)]

# ================= rysowanie =================
# 1. cień kanału i otworów międzykręgowych
f.add(f'<path class="shade" d="{smooth(T(sym(canal_R)))}"/>')

# 2. krążek: pierścień włóknisty z blaszkami + jądro miażdżyste
disc_pts = cr(disc, closed=True, n=14)
nuc_pts = cr(nuc, closed=True, n=14)
f.add(f'<path class="annulus" d="{smooth(T(disc))}"/>')
rO = radial(disc_pts, NC)
rN = radial(nuc_pts, NC)
for t in (0.13, 0.26, 0.385, 0.505, 0.62, 0.73, 0.835):
    ring = []
    for (a, ro), (_, rn) in zip(rO, rN):
        r = ro + (rn - ro) * t
        ring.append((NC[0] + r * math.cos(a), NC[1] + r * math.sin(a)))
    f.add(f'<path class="annulus" d="{poly(T(ring))}"/>')
f.add(f'<path class="nucleus" d="{smooth(T(nuc))}"/>')

# 3. więzadło podłużne przednie (na przedniej powierzchni krążka)
seg = [p for p in disc_pts if p[1] < 7.2]
seg.sort(key=lambda p: p[0])
inn = offset(seg, -0.05)
outer = []
for i, p in enumerate(seg):
    u = abs(p[0]) / 22.0
    w = 1.9 * (1 - u ** 2.2) + 0.25
    outer.append(offset(seg, -w)[i])
f.add(f'<path class="lig" d="{smooth(T(outer[::6] + [outer[-1]] + inn[::-1][::6] + [inn[0]]))}"/>')

# 4. więzadło podłużne tylne (na tylnej powierzchni krążka, w kanale kręgowym; na krążku poszerzone)
segp = [p for p in disc_pts if p[1] > 27.0 and abs(p[0]) <= 12.6]
segp.sort(key=lambda p: p[0])
innp = offset(segp, 0.05)
outp = []
for i, p in enumerate(segp):
    u = abs(p[0]) / 12.6
    w = 1.35 * (1 - u ** 2.4) + 0.2
    outp.append(offset(segp, w)[i])
f.add(f'<path class="lig" d="{smooth(T(outp[::5] + [outp[-1]] + innp[::-1][::5] + [innp[0]]))}"/>')

# 5. łuk kręgu wyższego (przekrój) + wyrostki stawowe górne kręgu niższego (przekrój)
f.add(f'<path class="bone2" d="{smooth(T(arch))}"/>')
for s in (1, -1):
    sap = [(s * x, y) for x, y in sap_R]
    f.add(f'<path class="bone2" d="{poly(T(sap))}"/>')
    # chrząstka stawowa na obu powierzchniach + szpara stawowa (jama stawowa)
    fa = [(s * x, y) for x, y in iap_face]
    fb = [(s * x, y) for x, y in sap_face]
    f.add(f'<path class="cavity" d="{poly(T(fa + fb[::-1]))}"/>')
    ca = offset(iap_face, -0.36)
    cb = offset(sap_face, 0.36)
    f.add(f'<path class="facet" d="{poly(T([(s * x, y) for x, y in iap_face + ca[::-1]]))}"/>')
    f.add(f'<path class="facet" d="{poly(T([(s * x, y) for x, y in sap_face + cb[::-1]]))}"/>')
    # więzadło żółte
    fl = [(s * x, y) for x, y in flav_R]
    f.add(f'<path class="lig" d="{smooth(T(fl))}"/>')
# grzebień wyrostka kolczystego – linia pośrodkowa
f.add(f'<path class="bonel" d="{poly(T(sh([(0, 61.0), (0, 75.5)])), closed=False)}"/>')

# ================= podpisy =================
TL, TR = 40.0, 110.0
f.label(P(-6.0, -1.25), 'więzadło podłużne przednie', 'ligamentum longitudinale anterius', (TL, 4.5), side='L')
f.label(P(-17.5, 9.0), 'pierścień włóknisty', 'annulus fibrosus', (TL, 15.0), side='L')
f.label(P(-5.5, 19.5), 'jądro miażdżyste', 'nucleus pulposus', (TL, 26.0), side='L')
f.label(P(-21.0, 37.6), 'otwór międzykręgowy', 'foramen intervertebrale', (TL, 40.0), side='L')
f.label(P(-21.0, 46.0), 'wyrostek stawowy górny', 'processus articularis superior', (TL, 52.0), side='L')
f.label(P(-11.5, 51.2), 'wyrostek stawowy dolny', 'processus articularis inferior', (TL, 64.0), side='L')

f.label(P(19.0, 12.0), 'krążek międzykręgowy', 'discus intervertebralis', (TR, 9.0), side='R')
f.label(P(6.0, 31.0), 'więzadło podłużne tylne', 'ligamentum longitudinale posterius', (TR, 22.0), side='R')
f.label(P(5.0, 40.0), 'kanał kręgowy', 'canalis vertebralis', (TR, 34.0), side='R')
f.label(P(9.0, 45.0), 'więzadło żółte', 'ligamentum flavum', (TR, 46.0), side='R')
f.label(P(1.5, 68.0), 'wyrostek kolczysty', 'processus spinosus', (TR, 66.0), side='R')
f.save()
