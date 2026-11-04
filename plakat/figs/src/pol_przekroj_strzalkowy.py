# Połączenia kręgów – część lędźwiowa kręgosłupa (L2–L4) w przekroju pośrodkowym; połowa prawa widziana od strony lewej,
# przód w lewo. Schemat własny wg opisu Bochenka s. 249–254 (ryc. 166 tylko do orientacji).
# Pokazane: trzony (przekrój), krążki (pierścień włóknisty z blaszkami, jądro miażdżyste bliżej tyłu), więzadła podłużne,
# kanał kręgowy (w głębi nasady łuków prawej strony i otwory międzykręgowe), łuki z wyrostkami kolczystymi (przekrój),
# więzadła żółte, międzykolcowe i nadkolcowe.
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig

W, H = 150, 110
S, X0, Y0 = 0.74, 44.0, 12.9        # skala (mm rysunku / mm kości), położenie początku układu
YT, YB = -4.5, 103.5                # linie cięcia u góry i u dołu (w mm kości; środek krążków L1/L2 i L4/L5)
VB = [0.0, 36.0, 72.0]              # górna powierzchnia trzonów L2, L3, L4 (brzeg tylny)


def P(x, y):
    return (X0 + x * S, Y0 + y * S)


def T(pts):
    return [P(x, y) for x, y in pts]


def path(pts, closed=True):
    q = T(pts)
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in q) + (' Z' if closed else '')


def cr(pts, closed=False, n=10, t=0.5):
    """punkty na krzywej Catmull-Rom (ta sama krzywa co smooth() z figlib)"""
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


f = Fig('pol_przekroj_strzalkowy', W, H,
        caption='część lędźwiowa kręgosłupa (L2–L4) · przekrój pośrodkowy · widok od strony lewej (przód w lewo)')

# wszystko, co przecięte u góry i u dołu, przycinamy prostą linią cięcia
x1, y1 = P(-6, YT); x2, y2 = P(92, YB)
f.add(f'<defs><clipPath id="cp_pol_przekroj"><rect x="{x1:.2f}" y="{y1:.2f}" width="{x2 - x1:.2f}" height="{y2 - y1:.2f}"/></clipPath></defs>')
f.add('<g clip-path="url(#cp_pol_przekroj)">')


# ---------- geometria trzonu ----------
def body_pts(y0):
    a, b = y0 + 0.75, y0              # powierzchnia górna: przód, tył
    c, d = y0 + 26.25, y0 + 27.0      # powierzchnia dolna: przód, tył
    return [(0.15, a + 1.5), (1.3, a + 0.1), (9, a + 0.5), (17, (a + b) / 2 + 0.8), (25, b + 0.35), (32.7, b + 0.05),
            (33.95, b + 1.4), (33.4, b + 7), (33.2, (b + d) / 2), (33.4, d - 7), (33.95, d - 1.4),
            (32.7, d - 0.05), (25, d - 0.35), (17, (c + d) / 2 - 0.8), (9, c - 0.5), (1.3, c - 0.1), (0.15, c - 1.5),
            (1.2, c - 7), (1.55, (a + c) / 2), (1.2, a + 7)]


def disc_geom(yu):
    """krążek pod trzonem, którego górna powierzchnia (z tyłu) leży na yu: zwraca (krzywa przednia, tylna, środek)"""
    cF, cB = yu + 26.25, yu + 27.0          # dolna powierzchnia trzonu wyższego
    dF, dB = yu + 36.75, yu + 36.0          # górna powierzchnia trzonu niższego
    m = yu + 31.5
    Fr = cr([(-0.05, cF + 0.25), (-0.95, m), (-0.05, dF - 0.25)], n=12)
    Bk = cr([(34.0, cB + 0.25), (34.95, m), (34.0, dB - 0.25)], n=12)
    return Fr, Bk, m, (cF, cB, dF, dB)


DISCS = [-36.0, 0.0, 36.0, 72.0]            # krążki: L1/L2 (przecięty), L2/L3, L3/L4, L4/L5 (przecięty)

# ---------- 1. kanał kręgowy (w głębi) ----------
f.add(f'<path class="shade" d="{path([(33.0, YT - 2), (50.6, YT - 2), (50.6, YB + 2), (33.0, YB + 2)])}"/>')

# otwory międzykręgowe prawej strony widziane przez kanał (pod wcięciem kręgowym dolnym, za krążkiem)
FOR = {}
for y0 in [-36.0] + VB:
    fo = [(40.6, y0 + 14.5), (43.4, y0 + 15.2), (45.0, y0 + 17.8), (45.1, y0 + 22.6), (44.0, y0 + 28.0), (42.4, y0 + 32.4),
          (40.4, y0 + 34.6), (38.4, y0 + 33.6), (36.9, y0 + 29.2), (35.9, y0 + 23.4), (35.8, y0 + 18.4), (37.6, y0 + 15.2)]
    FOR[y0] = fo
    f.add(f'<path class="hole" d="{path(cr(fo, closed=True, n=6))}"/>')


# ---------- 2. łuki z wyrostkami kolczystymi (przekrój) ----------
def arch_pts(y0):
    return [(49.9, y0 + 4.2), (51.4, y0 + 2.9), (53.4, y0 + 2.5), (56.5, y0 + 3.2), (60.5, y0 + 4.5), (65.5, y0 + 4.9),
            (71.0, y0 + 5.2), (76.4, y0 + 5.6), (80.6, y0 + 6.0), (83.2, y0 + 8.0), (84.4, y0 + 11.8), (84.2, y0 + 16.2),
            (82.6, y0 + 19.6), (79.6, y0 + 20.8), (75.0, y0 + 19.9), (69.6, y0 + 18.6), (64.2, y0 + 18.2),
            (59.4, y0 + 19.4), (56.0, y0 + 21.2), (53.2, y0 + 23.4), (51.6, y0 + 25.6), (50.5, y0 + 26.9),
            (49.5, y0 + 26.0), (49.4, y0 + 20.0), (49.5, y0 + 12.0)]


ARCHES = [-36.0] + VB + [108.0]

# więzadła międzykolcowe (wypełnienie przestrzeni między wyrostkami kolczystymi) + włókna skośne
for y0 in ARCHES[:-1]:
    isp = [(50.8, y0 + 17.0), (85.0, y0 + 17.0), (85.0, y0 + 44.0), (50.8, y0 + 44.0)]
    f.add(f'<path class="lig" d="{path(isp)}"/>')
    for k, x in enumerate((56.5, 61.5, 66.5, 71.5, 76.0)):
        a = (x, y0 + 19.0)
        b = (x + 6.5, y0 + 41.5)
        f.add(f'<path class="lig" d="{path([a, b], closed=False)}"/>')

# więzadła żółte – między łukami, po stronie kanału
for y0 in ARCHES[:-1]:
    fl = [(49.6, y0 + 14.6), (48.0, y0 + 17.6), (47.3, y0 + 22.5), (47.1, y0 + 29.0), (47.4, y0 + 35.0), (48.3, y0 + 38.8),
          (49.8, y0 + 40.6), (51.6, y0 + 40.4), (53.0, y0 + 38.6), (53.1, y0 + 34.0), (52.6, y0 + 29.6), (51.6, y0 + 25.5),
          (50.6, y0 + 20.5), (50.2, y0 + 15.5)]
    f.add(f'<path class="lig" d="{path(cr(fl, closed=True, n=6))}"/>')

# ---------- 3. krążki międzykręgowe ----------
for yu in DISCS:
    Fr, Bk, m, (cF, cB, dF, dB) = disc_geom(yu)
    top = [(33.0, cB - 1.6), (17.0, (cF + cB) / 2 - 2.0), (1.0, cF - 1.6)]
    bot = [(1.0, dF + 1.6), (17.0, (dF + dB) / 2 + 2.0), (33.0, dB + 1.6)]
    f.add(f'<path class="annulus" d="{path(Fr + bot + Bk[::-1] + top)}"/>')
    # blaszki pierścienia włóknistego – łuki od trzonu do trzonu, wypukłe ku obwodowi (od środka ku zewnątrz)
    def ytop(x): return cF + (cB - cF) * x / 34 - 0.8 * math.sin(math.pi * x / 34) - 0.6
    def ybot(x): return dF + (dB - dF) * x / 34 + 0.8 * math.sin(math.pi * x / 34) + 0.6
    for xe, xm in ((12.5, 11.1), (10.1, 8.6), (7.6, 6.0), (5.0, 3.4), (2.5, 0.9)):
        arc = cr([(xe, ytop(xe)), (xm, m), (xe, ybot(xe))], n=10)
        f.add(f'<path class="annulus" d="{path(arc, closed=False)}"/>')
    for xe, xm in ((25.6, 27.3), (28.2, 29.8), (30.6, 32.1), (32.6, 33.9)):
        arc = cr([(xe, ytop(xe)), (xm, m), (xe, ybot(xe))], n=10)
        f.add(f'<path class="annulus" d="{path(arc, closed=False)}"/>')
    # jądro miażdżyste – ekscentrycznie, bliżej brzegu tylnego
    nu = [(13.6, m + 0.1), (15.0, m - 2.5), (19.6, m - 3.25), (24.4, m - 2.8), (26.4, m - 0.1), (25.0, m + 2.7),
          (20.2, m + 3.2), (15.4, m + 2.6)]
    f.add(f'<path class="nucleus" d="{path(cr(nu, closed=True, n=8))}"/>')

# ---------- 4. więzadła podłużne ----------
# przednie: na przedniej powierzchni trzonów i krążków
post, ant = [], []
for yu in DISCS:
    Fr, Bk, m, (cF, cB, dF, dB) = disc_geom(yu)
    post += [(1.2, cF - 6.0)] + [(x + 0.35, y) for x, y in Fr] + [(1.2, dF + 6.0)]
    ant += [(-1.25, cF - 13.0), (-2.0, m)]
ant += [(-1.25, 72 + 36 + 13.0)]
antc = cr(ant, n=10)
f.add(f'<path class="lig" d="{path(antc + post[::-1])}"/>')
# tylne: na tylnej powierzchni trzonów i krążków, wewnątrz kanału kręgowego
postP, antP = [], []
for yu in DISCS:
    Fr, Bk, m, (cF, cB, dF, dB) = disc_geom(yu)
    antP += [(32.8, cB - 6.0)] + [(x - 0.35, y) for x, y in Bk] + [(32.8, dB + 6.0)]
    postP += [(35.2, cB - 13.0), (35.8, m)]
postP += [(35.2, 72 + 36 + 13.0)]
postPc = cr(postP, n=10)
f.add(f'<path class="lig" d="{path(antP + postPc[::-1])}"/>')

# ---------- 5. trzony kręgów (przekrój) ----------
for y0 in VB:
    bp = cr(body_pts(y0), closed=True, n=8)
    f.add(f'<path class="bone2" d="{path(bp)}"/>')
    # cienka warstwa istoty zbitej
    cx, cy = 17.0, y0 + 13.5
    inner = [(cx + (x - cx) * 0.93, cy + (y - cy) * 0.925) for x, y in body_pts(y0)]
    f.add(f'<path class="bonel" d="{path(cr(inner, closed=True, n=8))}"/>')

# ---------- 6. łuki i wyrostki kolczyste (przekrój) ----------
for y0 in ARCHES:
    f.add(f'<path class="bone2" d="{path(cr(arch_pts(y0), closed=True, n=6))}"/>')

# ---------- 7. więzadło nadkolcowe ----------
a_e, p_e = [], []
for y0 in [-36.0] + VB + [108.0]:
    a_e += [(84.15, y0 + 12.5), (83.5, y0 + 30.0)]
    p_e += [(86.5, y0 + 12.5), (86.1, y0 + 30.0)]
f.add(f'<path class="lig" d="{path(cr(a_e, n=8) + cr(p_e, n=8)[::-1])}"/>')

f.add('</g>')

# oznaczenia kręgów
for y0, nm in zip(VB, ('L2', 'L3', 'L4')):
    x, y = P(17.0, y0 + 14.2)
    f.text(x, y, nm, cls='notec')

# ---------- podpisy ----------
TL, TR = 39.5, 111.0
# lewa kolumna – struktury przednie
f.label(P(8.0, 10.0), 'trzon kręgu', 'corpus vertebrae', (TL, 17.0), side='L')
f.label(P(4.0, 31.5), 'krążek międzykręgowy', 'discus intervertebralis', (TL, 33.5), side='L')
f.label(P(-1.3, 48.0), 'więzadło podłużne przednie', 'ligamentum longitudinale anterius', (TL, 45.0), side='L')
f.label(P(6.0, 65.0), 'pierścień włóknisty', 'annulus fibrosus', (TL, 57.0), side='L')
f.label(P(17.0, 68.6), 'jądro miażdżyste', 'nucleus pulposus', (TL, 66.5), side='L')
# prawa kolumna – łuki, wyrostki i więzadła tylne
f.label(P(85.3, 7.5), 'więzadło nadkolcowe', 'ligamentum supraspinale', (TR, 13.0), side='R')
f.label(P(70.0, 13.5), 'wyrostek kolczysty', 'processus spinosus', (TR, 22.5), side='R')
f.label(P(78.0, 29.5), 'więzadło międzykolcowe', 'ligamentum interspinale', (TR, 32.0), side='R')
f.label(P(50.7, 24.0), 'łuk kręgu', 'arcus vertebrae', (TR, 41.5), side='R')
f.label(P(40.2, 60.0), 'otwór międzykręgowy', 'foramen intervertebrale', (TR, 59.0), side='R')
f.label(P(49.3, 67.0), 'więzadło żółte', 'ligamentum flavum', (TR, 68.5), side='R')
# nad i pod rysunkiem – kanał kręgowy i więzadło podłużne tylne
f.label(P(42.0, 6.0), 'kanał kręgowy', 'canalis vertebralis', (80.5, 3.5), side='R')
f.label(P(35.0, 100.5), 'więzadło podłużne tylne', 'ligamentum longitudinale posterius', (66.5, 94.5), side='L')

f.save()
