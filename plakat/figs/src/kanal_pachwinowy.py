# KANAŁ PACHWINOWY – schemat własny wg Bochenka t. I, s. 721–726 (ryciny 468–472 tylko do orientacji).
#  A – widok od przodu, strona prawa ciała (bocznie = lewo rysunku). Rozcięgno m. skośnego zewnętrznego pokazane jako
#      półprzezroczyste: w głębi kanał z powrózkiem, pierścień głęboki, dolny brzeg m. skośnego wewnętrznego, naczynia
#      nabrzuszne dolne. Wg s. 722: kanał nad przyśrodkową częścią więzadła pachwinowego, od tyłu-góry-boku do przodu-dołu-
#      przyśrodkowo; kąt z więzadłem ok. 15°, długość 4–5 cm. S. 725: pierścień głęboki mniej więcej w połowie więzadła,
#      ok. 2 cm nad nim, w powięzi poprzecznej, bocznie od naczyń nabrzusznych dolnych. S. 724: pierścień powierzchowny
#      nieco bocznie i powyżej guzka łonowego; odnoga przyśrodkowa (nad otworem), boczna (przechodzi w więzadło pachwinowe),
#      włókna międzyodnogowe (od przodu), więzadło zagięte (od tyłu i od dołu – niewidoczne w tym widoku).
#  B – przekrój przez środek kanału, prostopadły do jego osi (przód w lewo). Ściany wg s. 725: przednia – rozcięgno
#      m. skośnego zewn.; tylna – powięź poprzeczna (wzmocniona więzadłem międzydołkowym i sierpem pachwinowym); górna
#      (strop) – dolne włókna m. skośnego wewn. i m. poprzecznego; dolna (dno) – więzadło pachwinowe z włóknami odnogi
#      bocznej, rynienka otwarta ku górze. Zawartość (s. 726): powrózek nasienny – w kanale osłonięty powięzią nasienną
#      wewnętrzną (z powięzi poprzecznej) i dźwigaczem jądra (z mm. skośnego wewn. i poprzecznego); powięź dźwigacza jądra
#      powstaje dopiero przy pierścieniu powierzchownym. W powrózku: nasieniowód, tętnice, splot wiciowaty, nerw.
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig

W, H = 160, 124
f = Fig('kanal_pachwinowy', W, H,
        caption='kanał pachwinowy · A – od przodu (strona prawa), B – przekrój prostopadły do osi kanału (przód w lewo)')


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


def poly(pts, close=True):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + (' Z' if close else '')


def ribbon(center, w, n=10):
    c = cr(center, n=n)
    a = offset(c, (lambda s: w(s) / 2) if callable(w) else w / 2)
    b = offset(c, (lambda s: -w(s) / 2) if callable(w) else -w / 2)
    return a + b[::-1]


def add(p, v, k=1.0):
    return (p[0] + v[0] * k, p[1] + v[1] * k)


def unit(v):
    L = math.hypot(*v)
    return (v[0] / L, v[1] / L)


def ellipse_pts(c, rx, ry, ang, n=48):
    ca, sa = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    return [(c[0] + rx * math.cos(2 * math.pi * k / n) * ca - ry * math.sin(2 * math.pi * k / n) * sa,
             c[1] + rx * math.cos(2 * math.pi * k / n) * sa + ry * math.sin(2 * math.pi * k / n) * ca) for k in range(n)]


def resample(pts, n):
    L = [0.0]
    for i in range(1, len(pts)):
        L.append(L[-1] + math.dist(pts[i - 1], pts[i]))
    out, j = [], 0
    for k in range(n + 1):
        s = L[-1] * k / n
        while j < len(L) - 2 and L[j + 1] < s:
            j += 1
        u = (s - L[j]) / max(L[j + 1] - L[j], 1e-9)
        out.append((pts[j][0] + (pts[j + 1][0] - pts[j][0]) * u, pts[j][1] + (pts[j + 1][1] - pts[j][1]) * u))
    return out, L[-1]


# =====================================================================  A · WIDOK OD PRZODU
AY1 = 64.5                                   # dolna granica panelu A
ASIS = (48.0, 8.0)
TUB = (103.0, 50.6)
dS = unit((TUB[0] - ASIS[0], TUB[1] - ASIS[1]))           # kierunek więzadła (przyśrodkowo w dół)
nS = (dS[1], -dS[0])                                       # normalna ku górze
LIG_LEN = math.dist(ASIS, TUB)
MMCM = LIG_LEN / 13.0                                      # więzadło ≈ 13 cm → mm rysunku na 1 cm


def L(t, h=0.0):
    """punkt nad więzadłem: t – ułamek długości od kolca, h – wysokość nad więzadłem (mm); lekkie ugięcie więzadła ku dołowi"""
    sag = 1.4 * math.sin(math.pi * t)
    p = (ASIS[0] + dS[0] * LIG_LEN * t, ASIS[1] + dS[1] * LIG_LEN * t)
    return add(p, nS, h - sag)


LIG_C = [L(k / 8) for k in range(9)]
ang_lig = math.degrees(math.atan2(dS[1], dS[0]))
dC = (math.cos(math.radians(ang_lig + 15)), math.sin(math.radians(ang_lig + 15)))   # oś kanału: 15° do więzadła
nC = (dC[1], -dC[0])
S0 = L(0.915, 0.8 * MMCM)                                  # wyjście kanału: pierścień powierzchowny (nieco bocznie i powyżej guzka)
CANAL_LEN = 4.6 * MMCM
D = add(S0, dC, -CANAL_LEN)                                # pierścień głęboki
tD = ((D[0] - ASIS[0]) * dS[0] + (D[1] - ASIS[1]) * dS[1]) / LIG_LEN
hD = (D[0] - L(tD)[0]) * nS[0] + (D[1] - L(tD)[1]) * nS[1]
print('pierścień głęboki: t=%.2f długości więzadła, %.1f cm nad więzadłem; kanał %.1f cm' % (tD, hD / MMCM, CANAL_LEN / MMCM))
CW = 6.6                                                   # grubość powrózka (ok. 1,2–1,3 cm)

# ---------- kości: kolec biodrowy przedni górny (fragment talerza) i kość łonowa
ILIUM = [(44.0, 2.0), (45.6, 4.0), (47.2, 6.2), ASIS, (48.8, 10.0), (48.0, 12.0), (48.6, 14.6), (47.4, 16.6), (44.0, 16.6)]
f.add(f'<path class="bone" d="{poly(cr(ILIUM[:8], n=6) + ILIUM[8:])}"/>')
PUB = [(85.0, 57.2), (93.0, 55.2), (99.0, 53.4), (101.6, 51.6), (103.0, 50.9), (104.6, 51.4), (109.0, 52.2), (113.6, 52.2),
       (113.6, AY1), (104.0, AY1), (101.0, 61.8), (93.0, 60.6), (85.0, 61.0)]
f.add(f'<path class="bone" d="{poly(PUB)}"/>')
f.add(f'<path class="bonel" d="M85.0,57.2 L85.0,61.0"/>')
f.add(f'<path class="cart" d="{poly([(113.6, 52.2), (116.4, 52.2), (116.4, AY1), (113.6, AY1)])}"/>')    # spojenie łonowe

# ---------- warstwy głębokie (widoczne przez półprzezroczyste rozcięgno)
# naczynia nabrzuszne dolne: spod więzadła ku górze, przyśrodkowo od pierścienia głębokiego, do m. prostego
VES = [L(0.69, -4.2), L(0.69, 2.4), add(D, (6.4, 3.4)), add(D, (6.2, -2.2)), add(D, (9.0, -12.0)), (101.0, 2.0)]
f.add(f'<path class="vein" d="{poly(ribbon([add(p, (0.8, 0.2)) for p in VES], 0.85))}"/>')
f.add(f'<path class="artery" d="{poly(ribbon([add(p, (-0.5, -0.1)) for p in VES], 0.75))}"/>')
# m. skośny wewnętrzny – dolny pas: z bocznej części więzadła (bocznie od pierścienia głębokiego), łukiem nad
# pierścieniem głębokim i powrózkiem do grzebienia łonowego (strop kanału); górny brzeg pasa – odcięty
ARCH = ([add(D, dC, -(CW / 2 + 3.2)), add(add(D, dC, -2.4), nC, CW / 2 + 2.2), add(D, nC, CW / 2 + 2.8)] +
        [add(add(D, dC, CANAL_LEN * k), nC, CW / 2 + 2.0 + 0.3 * k) for k in (0.35, 0.65, 0.88)] + [(108.4, 51.2)])
arch = cr(ARCH, n=8)
BAND = 8.0
low = [L(0.06 + 0.02 * k) for k in range(21)] + arch
top_arch = offset(arch, BAND)
top_lat = [L(0.06 + 0.02 * k, BAND) for k in range(19)]
IOP = low + top_arch[::-1][1:] + top_lat[::-1]
f.add(f'<path class="muscle" d="{poly(IOP)}"/>')
for k in range(1, 4):                                      # włókna: z więzadła przyśrodkowo, łukiem, nieco ku dołowi
    fr = k / 4
    lat_pts = [L(0.06 + 0.02 * j, BAND * fr) for j in range(19)]
    f.add(f'<path class="musclel" d="{poly(lat_pts[2:] + offset(arch, BAND * fr)[2:-3], close=False)}"/>')
# pierścień głęboki (otwór w powięzi poprzecznej) i powrózek w kanale
ringD = ellipse_pts(D, CW / 2 + 0.9, CW / 2 + 1.3, ang_lig + 15)
f.add(f'<path class="cavity" d="{poly(ringD)}"/>')
END = add(S0, dC, 0.8)
cap = [add(add(D, nC, CW / 2 * math.cos(math.pi * k / 16)), dC, -CW / 2 * 0.85 * math.sin(math.pi * k / 16)) for k in range(17)]
f.add(f'<path class="organ" d="{poly([add(END, nC, -CW / 2), add(END, nC, CW / 2)] + cap)}"/>')
f.add(f'<path class="capsule" d="{poly(ringD[14:38], close=False)}"/>')

# ---------- rozcięgno m. skośnego zewnętrznego (półprzezroczyste) z pierścieniem powierzchownym
KM = (ASIS[0] + 4.0 * MMCM, ASIS[1] - 2.6)                 # kąt mięśniowy: 3–5 cm przyśrodkowo od kolca, nieco powyżej
EO_M = [(44.0, 2.0), (KM[0], 2.0), KM, (49.8, KM[1]), (47.0, 3.6)]
# pierścień: szczyt bocznie u góry, podstawa na grzebieniu łonowym (odnoga boczna → guzek, przyśrodkowa → spojenie)
AP = add(S0, dC, -6.4)
BL = (102.6, 50.6)
BM = (109.4, 51.8)
crus_lat = cr([AP, add(add(AP, dC, 6.4), nC, -3.9), BL], n=8)          # brzeg dolny-boczny
crus_med = cr([AP, add(add(AP, dC, 7.4), nC, 3.4), BM], n=8)           # brzeg górny-przyśrodkowy
ring = crus_lat + [(106.0, 51.9)] + crus_med[::-1][:-1]
apon = ([(KM[0], 2.0), (116.4, 2.0), (116.4, 52.2), (113.6, 52.2), (BM[0], BM[1] + 0.2), (BL[0], BL[1] + 0.2)] +
        [L(0.98 - 0.02 * k) for k in range(49)] + [(49.8, KM[1]), KM])
f.add(f'<path class="tendon" style="fill-opacity:.66;fill-rule:evenodd" d="{poly(apon)} {poly(ring)}"/>')
f.add(f'<path class="muscle" d="{poly(EO_M)}"/>')
for k in range(1, 4):
    y0 = 2.0 + k * (KM[1] - 2.0) / 4.0
    f.add(f'<path class="musclel" d="M{46.0 + k * 1.2:.2f},{y0 - 1.0:.2f} L{KM[0] - 0.5:.2f},{y0 + 1.0:.2f}"/>')
# włókna rozcięgna – skośnie ku dołowi i przyśrodkowo
def inside_ring(p, pad=1.2):
    cx = sum(q[0] for q in ring) / len(ring); cy = sum(q[1] for q in ring) / len(ring)
    return math.dist(p, (cx, cy)) < 8.6 + pad


for k in range(8):
    a0 = (KM[0] + 3.0 + k * 6.0, 2.4)
    pts = [a0]
    for j in range(1, 90):
        p = add(a0, dS, j * 0.8)
        t = ((p[0] - ASIS[0]) * dS[0] + (p[1] - ASIS[1]) * dS[1]) / LIG_LEN
        h = (p[0] - L(t)[0]) * nS[0] + (p[1] - L(t)[1]) * nS[1]
        if p[0] > 112.0 or h < 1.4 or inside_ring(p) or p[1] > 50.5:
            break
        pts.append(p)
    if len(pts) > 3:
        f.add(f'<path class="tendon" d="{poly(pts, close=False)}"/>')
# więzadło pachwinowe
f.add(f'<path class="lig" d="{poly(ribbon(LIG_C, 1.3))}"/>')

# powrózek nasienny po wyjściu z pierścienia powierzchownego (ku mosznie)
CORD_OUT = [add(S0, dC, -2.6), add(S0, dC, 1.6), (105.2, 54.6), (106.0, 60.0), (106.4, AY1 + 2.0)]
f.add(f'<path class="organ" d="{poly(ribbon(CORD_OUT, CW + 0.4, n=8))}"/>')
for k in range(4):                                         # pętle włókien dźwigacza jądra
    y = 50.2 + 3.4 * k
    x = 103.6 + (y - 50.0) * 0.22
    f.add(f'<path class="musclel" d="M{x - 3.0:.2f},{y - 1.0:.2f} Q{x:.2f},{y + 1.5:.2f} {x + 3.2:.2f},{y - 1.1:.2f}"/>')

# odnogi pierścienia powierzchownego (brzegi otworu w rozcięgnie) i włókna międzyodnogowe (od przodu, nad szczytem)
f.add(f'<path class="lig" d="{poly(ribbon(crus_lat + [TUB], 1.5, n=2))}"/>')
f.add(f'<path class="lig" d="{poly(ribbon(crus_med + [(112.0, 52.2)], 1.5, n=2))}"/>')
for k, r in enumerate((1.2, 2.7, 4.2)):
    c0 = add(AP, dC, -r * 0.30)
    a0 = add(add(c0, nC, 2.8 + r * 0.45), dC, 1.4)
    b0 = add(add(c0, nC, -2.8 - r * 0.45), dC, 1.4)
    m0 = add(c0, dC, -r * 0.8)
    f.add(f'<path class="ligl" d="M{a0[0]:.2f},{a0[1]:.2f} Q{m0[0]:.2f},{m0[1]:.2f} {b0[0]:.2f},{b0[1]:.2f}"/>')

# oś kanału i kąt z więzadłem (pomocniczo) – po stronie bocznej pierścienia głębokiego
E1 = add(D, dC, -14.0)
E2 = add(D, dS, -14.0)
f.add(f'<path class="dim" d="M{S0[0]:.2f},{S0[1]:.2f} L{E1[0]:.2f},{E1[1]:.2f}"/>')
f.add(f'<path class="dim" d="M{D[0]:.2f},{D[1]:.2f} L{E2[0]:.2f},{E2[1]:.2f}"/>')
R = 12.0
a1 = add(D, dS, -R); a2 = add(D, dC, -R)
f.add(f'<path class="dim" style="stroke-dasharray:none" d="M{a1[0]:.2f},{a1[1]:.2f} A{R},{R} 0 0 1 {a2[0]:.2f},{a2[1]:.2f}"/>')
f.text((a1[0] + a2[0]) / 2 - 1.0, (a1[1] + a2[1]) / 2 - 0.4, '15°', cls='note', anchor='end')
mC = add(add(D, dC, CANAL_LEN * 0.5), nC, -(CW / 2 + 2.2))

# ---------- tytuł i noty panelu A
f.text(2.0, 5.0, 'A · widok od przodu', cls='big')
f.text(2.0, 8.6, 'strona prawa; rozcięgno m. skośnego')
f.text(2.0, 11.2, 'zewnętrznego półprzezroczyste')

# ---------- podpisy A
TL, TR = 43.0, 118.0
f.label(add(D, dC, -(CW / 2 + 1.2)), 'pierścień pachwinowy głęboki', 'annulus inguinalis profundus', (TL, 19.0), side='L')
f.text(TL - 0.7, 25.8, 'w powięzi poprzecznej, ok. 2 cm nad', anchor='end')
f.text(TL - 0.7, 28.4, 'połową więzadła pachwinowego', anchor='end')
f.label(L(0.30), 'więzadło pachwinowe', 'ligamentum inguinale', (TL, 36.0), side='L')
f.text(TL - 0.7, 42.8, 'kolec biodrowy przedni górny →', anchor='end')
f.text(TL - 0.7, 45.4, 'guzek łonowy', anchor='end')
f.label(add(add(D, dC, CANAL_LEN * 0.55), nC, -1.0), 'kanał pachwinowy', 'canalis inguinalis', (TL, 50.0), side='L')
f.text(TL - 0.7, 56.6, '4–5 cm; od tyłu, góry i boku → do', anchor='end')
f.text(TL - 0.7, 59.2, 'przodu, w dół i przyśrodkowo', anchor='end')

f.label((97.7, 8.0), 'naczynia nabrzuszne dolne', 'vasa epigastrica inferiora', (TR, 6.0), side='R')
f.text(TR + 0.7, 12.6, 'przyśrodkowo od pierścienia')
f.text(TR + 0.7, 15.2, 'głębokiego')
f.label(add(add(AP, dC, -2.2), nC, 1.0), 'włókna międzyodnogowe', 'fibrae intercrurales', (TR, 21.0), side='R')
f.label(add(add(AP, dC, 3.2), nC, 0.4), 'pierścień powierzchowny', 'annulus inguinalis superficialis', (TR, 29.4), side='R')
f.text(TR + 0.7, 35.8, 'otwór w rozcięgnie m. skośnego zewn.')
f.label(crus_med[9], 'odnoga przyśrodkowa', 'crus mediale', (TR, 40.4), side='R')
f.label(crus_lat[11], 'odnoga boczna', 'crus laterale', (TR, 48.6), side='R')
f.label((106.0, 61.0), 'powrózek nasienny', 'funiculus spermaticus', (TR, 56.8), side='R')
f.text(TR + 0.7, 63.2, 'u kobiety: więzadło obłe macicy')

# =====================================================================  B · PRZEKRÓJ
BY0 = 70.0
# otrzewna (za powięzią poprzeczną)
PER = [(91.4, BY0 + 1.0), (91.4, 96.0), (92.2, 102.0), (94.2, 106.6), (97.0, 110.4), (98.6, 113.6)]
f.add(f'<path class="organ" d="{poly(ribbon(PER, 0.7))}"/>')
# powięź poprzeczna – ściana tylna; przyczepia się do więzadła pachwinowego
FT = [(86.8, BY0 + 1.0), (86.8, 88.0), (86.4, 96.0), (85.2, 101.6), (83.6, 103.6)]
f.add(f'<path class="tendon" d="{poly(ribbon(FT, 0.7))}"/>')
# m. skośny wewnętrzny i m. poprzeczny – dolne włókna (strop kanału); przekrój poprzeczny włókien
IOB = [(62.6, BY0 + 1.0), (73.6, BY0 + 1.0), (73.6, 84.0), (72.4, 87.4), (69.4, 88.6), (65.6, 87.6), (62.8, 85.0)]
TAB = [(74.6, BY0 + 1.0), (85.6, BY0 + 1.0), (85.6, 84.4), (84.0, 86.8), (80.6, 87.6), (77.0, 86.6), (74.6, 83.6)]
f.add(f'<path class="muscle" d="{poly(IOB[:2] + cr(IOB[2:], n=6))}"/>')
f.add(f'<path class="muscle" d="{poly(TAB[:2] + cr(TAB[2:], n=6))}"/>')
f.add(f'<path class="shade" d="{poly(TAB[:2] + cr(TAB[2:], n=6))}"/>')
for (x0, x1, y1) in ((63.6, 72.6, 85.8), (75.6, 84.6, 85.0)):
    for i in range(4):
        for j in range(5):
            x = x0 + (i + 0.5) * (x1 - x0) / 4 + (0.8 if j % 2 else 0)
            y = BY0 + 3.0 + j * 3.0
            if y < y1 - 1.0 and x < x1 - 0.4:
                f.add(f'<circle class="musclel" cx="{x:.2f}" cy="{y:.2f}" r="0.42"/>')
# rozcięgno m. skośnego zewnętrznego – ściana przednia; w dole przechodzi w więzadło pachwinowe (dno, rynienka)
EOB = [(60.6, BY0 + 1.0), (60.6, 96.0), (61.4, 101.6), (64.4, 105.4), (69.6, 106.8), (75.4, 106.2), (80.4, 104.6), (84.4, 103.0)]
f.add(f'<path class="tendon" d="{poly(ribbon(EOB[:3], 1.3))}"/>')
f.add(f'<path class="lig" d="{poly(ribbon(EOB[1:], lambda s: 1.3 + 1.6 * math.sin(math.pi * min(1.0, s * 1.15))))}"/>')
# powrózek nasienny w kanale
C0 = (73.2, 96.4)
f.add(f'<circle class="muscle" cx="{C0[0]}" cy="{C0[1]}" r="6.9"/>')          # dźwigacz jądra
f.add(f'<circle class="tendon" cx="{C0[0]}" cy="{C0[1]}" r="5.8"/>')          # powięź nasienna wewnętrzna
f.add(f'<circle class="cavity" cx="{C0[0]}" cy="{C0[1]}" r="5.2"/>')
for a in range(0, 360, 30):                                                     # pęczki dźwigacza
    x = C0[0] + 6.35 * math.cos(math.radians(a)); y = C0[1] + 6.35 * math.sin(math.radians(a))
    f.add(f'<circle class="musclel" cx="{x:.2f}" cy="{y:.2f}" r="0.3"/>')
DD = (75.6, 99.2)
f.add(f'<circle class="muscle" cx="{DD[0]}" cy="{DD[1]}" r="1.55"/>')          # nasieniowód – gruba cewa mięśniowa
f.add(f'<circle class="cavity" cx="{DD[0]}" cy="{DD[1]}" r="0.42"/>')
f.add(f'<circle class="artery" cx="77.6" cy="97.2" r="0.36"/>')                # t. nasieniowodu
f.add(f'<circle class="artery" cx="70.4" cy="94.6" r="0.75"/>')                # t. jądrowa
for (x, y, r) in ((72.6, 92.6, 0.7), (69.2, 97.2, 0.75), (71.4, 98.4, 0.62), (73.6, 95.2, 0.6), (75.2, 93.4, 0.55), (68.6, 93.6, 0.5)):
    f.add(f'<circle class="vein" cx="{x}" cy="{y}" r="{r}"/>')                 # splot wiciowaty
f.add(f'<circle class="nerve" cx="76.8" cy="94.8" r="0.5"/>')                  # gałąź płciowa n. płciowo-udowego

# tytuł i noty panelu B
f.text(2.0, BY0 + 4.0, 'B · przekrój przez kanał', cls='big')
f.text(2.0, BY0 + 7.6, 'prostopadle do jego osi; przód w lewo')

TLB, TRB = 52.0, 104.0
f.label((60.6, 78.0), 'rozcięgno m. skośnego zewnętrznego', None, (TLB, 81.0), side='L')
f.text(TLB - 0.7, 84.4, 'ściana przednia (zwłaszcza włókna', anchor='end')
f.text(TLB - 0.7, 87.0, 'międzyodnogowe)', anchor='end')
f.label((66.6, 99.8), 'dźwigacz jądra', 'm. cremaster', (TLB, 93.0), side='L')
f.label(DD, 'nasieniowód', 'ductus deferens', (TLB, 101.6), side='L')

f.label((68.0, 76.0), 'm. skośny wewnętrzny brzucha', 'm. obliquus internus abdominis', (TRB, 72.6), side='R')
f.label((80.0, 79.0), 'm. poprzeczny brzucha', 'm. transversus abdominis', (TRB, 79.6), side='R')
f.text(TRB + 0.7, 86.2, 'dolne włókna obu mięśni: ściana górna (strop)')
f.label((86.8, 92.0), 'powięź poprzeczna', 'fascia transversalis', (TRB, 90.6), side='R')
f.text(TRB + 0.7, 97.2, 'ściana tylna; wzmocniona więzadłem')
f.text(TRB + 0.7, 99.8, 'międzydołkowym i sierpem pachwinowym')
f.text(92.8, 84.8, 'otrzewna', cls='note')
f.label((76.0, 106.4), 'więzadło pachwinowe', 'ligamentum inguinale', (TRB, 105.0), side='R')
f.text(TRB + 0.7, 111.6, 'ściana dolna (dno) – z włóknami odnogi')
f.text(TRB + 0.7, 114.2, 'bocznej tworzy rynienkę otwartą ku górze')
f.label((68.4, 100.6), 'powięź nasienna wewnętrzna', 'fascia spermatica interna', (TLB, 110.4), side='L')

f.save()
print('ok')
