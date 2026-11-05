# M. NAJSZERSZY GRZBIETU (Bochenek, t. I, s. 652–655, ryc. 433–434; streszczenie s. 675; oddychanie s. 697;
# kość ramienna s. 449; grzebień biodrowy s. 521). Widok od tyłu, strona lewa ciała (po lewej stronie rysunku).
# Przyczepy początkowe (s. 652): 1) wyrostki kolczyste sześciu dolnych kręgów piersiowych (Th7–Th12), pięciu kręgów
#   lędźwiowych i grzebień krzyżowy pośrodkowy (pars vertebralis) – płaskim, szerokim ścięgnem = blaszka tylna albo
#   powierzchowna powięzi piersiowo-lędźwiowej; 2) tylna trzecia część wargi zewnętrznej grzebienia biodrowego
#   (pars iliaca); 3) 3–4 pasma z powierzchni zewnętrznej żebra IX lub X, XI i XII (pars costalis), wchodzą między
#   pasma m. skośnego zewnętrznego brzucha; 4) często nieznaczna część – kąt dolny łopatki (pars scapularis).
# Przebieg: pęczki biegną silnie zbieżnie do dołu pachowego (górne bardziej poprzecznie, dolne stromo ku górze),
#   dochodzą do m. obłego większego, owijają się dokoła niego (z jego powierzchni tylnej na przednią) i przechodzą
#   w czworokątne ścięgno → grzebień guzka mniejszego kości ramiennej, do przodu od m. obłego większego.
# Oddychanie (s. 654–655, 697): przy ustalonych ramionach – dźwigacz dolnych żeber (wiązki żebrowe) = pomocniczy
#   mięsień wdechowy (strzałki niebieskie); brzeg boczny (części boczne) twardnieje przy kaszlu / utrudnionym wydechu,
#   naciska bocznie na żebra przy ustalonym stawie ramiennym – „mięsień kaszlu” (strzałki czerwone).
# Schemat własny, uproszczony; strona prawa ciała – tylko kościec.
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 160, 108
f = Fig('m_najszerszy_grzbietu', W, H,
        caption='m. najszerszy grzbietu (strona lewa) · widok od tyłu · schemat przyczepów i działania oddechowego')
S = 1.8                      # mm na cm
CX, Y0 = 84.0, 7.0           # oś pośrodkowa; poziom szczytu wyrostka kolczystego Th1
YT, YB = -3.0, 50.0          # przycięcie (cm)
UL, UR = 24.0, -15.0         # przycięcie w poziomie (u: + strona lewa ciała = lewa strona rysunku)


def P(u, y):
    """widok od tyłu: u – odległość od płaszczyzny pośrodkowej w cm (+ = strona lewa ciała = lewa strona rysunku)"""
    return (CX - S * u, Y0 + S * y)


def PS(pts):
    return [P(u, y) for u, y in pts]


def M(pts):
    return [(-u, y) for u, y in pts]


def cr(pts, closed=False, n=12, t=0.5):
    m = len(pts)
    if m < 3:
        out = []
        for i in range(m - 1):
            for k in range(n):
                u = k / n
                out.append((pts[i][0] + (pts[i + 1][0] - pts[i][0]) * u, pts[i][1] + (pts[i + 1][1] - pts[i][1]) * u))
        return out + [pts[-1]]
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


def band(pts, w0, w1=None, n=10, cap0=False, cap1=False):
    w1 = w0 if w1 is None else w1
    c = cr(pts, n=n)
    L = [0.0]
    for i in range(1, len(c)):
        L.append(L[-1] + math.dist(c[i - 1], c[i]))
    tot = L[-1] or 1
    left, right = [], []
    for i, p in enumerate(c):
        a = c[max(i - 1, 0)]; b = c[min(i + 1, len(c) - 1)]
        tx, ty = b[0] - a[0], b[1] - a[1]
        ln = math.hypot(tx, ty) or 1
        nx, ny = -ty / ln, tx / ln
        w = (w0 + (w1 - w0) * L[i] / tot) / 2
        left.append((p[0] + nx * w, p[1] + ny * w))
        right.append((p[0] - nx * w, p[1] - ny * w))

    def capf(p, q, center, other, w, k=7):
        a0 = math.atan2(p[1] - center[1], p[0] - center[0])
        out = []
        for da in (math.pi, -math.pi):
            mid = (center[0] + w * math.cos(a0 + da / 2), center[1] + w * math.sin(a0 + da / 2))
            if math.dist(mid, other) > math.dist(center, other):
                return [(center[0] + w * math.cos(a0 + da * j / k), center[1] + w * math.sin(a0 + da * j / k))
                        for j in range(1, k)]
        return out
    out = list(left)
    if cap1:
        out += capf(left[-1], right[-1], c[-1], c[-2], w1 / 2)
    out += right[::-1]
    if cap0:
        out += capf(right[0], left[0], c[0], c[1], w0 / 2)
    return out


def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


body = []


def badd(cls, d):
    body.append(f'<path class="{cls}" d="{d}"/>')


# ---------------------------------------------------------------- poziomy kręgów (szczyty wyrostków kolczystych, cm)
TH = {k: 2.3 * (k - 1) for k in range(1, 13)}
LU = {k: TH[12] + 3.5 * k for k in range(1, 6)}

# ---------------------------------------------------------------- żebra (widok od tyłu; obie strony)
RIB_LAT = [7.2, 10.4, 12.4, 13.7, 14.5, 15.0, 15.2, 15.1, 14.8, 14.1, 13.6, 12.6]
RIB_DROP = [2.2, 3.4, 4.3, 5.0, 5.6, 6.1, 6.5, 6.8, 6.9, 6.7, 5.6, 4.6]
RIB_W = [1.3, 1.25, 1.2, 1.15, 1.15, 1.1, 1.1, 1.05, 1.0, 0.95, 0.8, 0.7]


def rib_pts(k):
    i = k - 1
    y0 = TH[k] - 1.2 + 0.08 * k          # przy wyrostku poprzecznym (wyżej niż szczyt wyrostka kolczystego)
    ul = RIB_LAT[i]
    dr = RIB_DROP[i]
    return [(1.9, y0), (4.6, y0 + 0.25 * dr), (ul * 0.72, y0 + 0.5 * dr), (ul, y0 + dr)]


for sd in (1, -1):
    for k in range(1, 13):
        pts = rib_pts(k) if sd > 0 else M(rib_pts(k))
        badd('bone', poly(band(PS(pts), RIB_W[k - 1] * S, RIB_W[k - 1] * S * 0.9, cap1=True)))

# ---------------------------------------------------------------- kręgosłup (Th1–L5) i kość krzyżowa
for k in range(1, 13):
    yv = TH[k]
    for sd in (1, -1):        # wyrostki poprzeczne
        pts = [(0.6, yv - 1.6), (2.1, yv - 1.45), (2.7, yv - 1.2)]
        badd('bone', poly(band(PS(pts if sd > 0 else M(pts)), 0.85 * S, 0.8 * S, cap1=True)))
    badd('bone', smooth(PS([(0.0, yv - 2.6), (0.75, yv - 2.3), (0.95, yv - 1.6), (0.5, yv - 0.4), (0.0, yv + 0.05),
                            (-0.5, yv - 0.4), (-0.95, yv - 1.6), (-0.75, yv - 2.3)]), closed=True, t=0.3))
for k in range(1, 6):
    yv = LU[k]
    for sd in (1, -1):
        pts = [(0.8, yv - 2.0), (2.6, yv - 2.1), (4.2, yv - 2.0)]
        badd('bone', poly(band(PS(pts if sd > 0 else M(pts)), 0.95 * S, 0.8 * S, cap1=True)))
    badd('bone', smooth(PS([(0.0, yv - 3.1), (1.0, yv - 2.9), (1.1, yv - 1.4), (0.85, yv - 0.1), (0.0, yv + 0.1),
                            (-0.85, yv - 0.1), (-1.1, yv - 1.4), (-1.0, yv - 2.9)]), closed=True, t=0.3))
SAC = [(0.0, 44.4), (2.6, 44.6), (5.0, 45.3), (5.2, 47.5), (4.6, 50.5), (3.6, 53.5), (2.3, 56.2), (1.0, 58.4)]
badd('bone', smooth(PS(SAC + M(list(reversed(SAC[1:])))), closed=True, t=0.35))
for y in (46.8, 49.6, 52.4):
    badd('bone', smooth(PS([(0.0, y - 0.8), (0.55, y - 0.4), (0.4, y + 0.6), (0.0, y + 0.85), (-0.4, y + 0.6),
                            (-0.55, y - 0.4)]), closed=True, t=0.3))
    for sd in (1, -1):
        cxu, cyy = P(sd * (2.1 - (y - 46.8) * 0.08), y + 0.6)
        f_hole = f'<circle class="hole" cx="{cxu:.2f}" cy="{cyy:.2f}" r="{0.45 * S:.2f}"/>'
        body.append(f_hole)
# talerze kości biodrowych
ILI = [(4.6, 51.0), (4.3, 48.4), (4.7, 46.6), (6.0, 44.2), (8.1, 41.9), (10.4, 40.4), (12.3, 39.9), (13.6, 40.6),
       (14.1, 42.4), (13.6, 45.6), (12.4, 49.4), (11.2, 53.0), (9.5, 57.5), (6.0, 58.5)]
for sd in (1, -1):
    badd('bone', smooth(PS(ILI if sd > 0 else M(ILI)), closed=True, t=0.3))
    crest_line = [(4.7, 46.9), (6.2, 44.6), (8.2, 42.4), (10.4, 40.95), (12.3, 40.5), (13.5, 41.0)]
    badd('bonel', line(PS(cr(crest_line if sd > 0 else M(crest_line), n=6))))

# ---------------------------------------------------------------- łopatki, kość ramienna (lewa)
SCAP = [(6.0, 0.4), (8.4, 0.9), (11.2, 1.6), (13.6, 2.0), (14.6, 2.6), (14.9, 4.4), (14.2, 5.6), (13.0, 8.0),
        (11.4, 11.2), (9.7, 14.3), (8.9, 15.4), (8.3, 14.9), (7.0, 11.0), (6.3, 6.5), (6.0, 3.0)]
SPINE = [(6.1, 4.4), (8.5, 3.7), (11.5, 2.6), (14.3, 1.2), (16.6, 0.0), (18.3, -0.5)]
HUM = [(16.0, 1.2), (17.1, -0.3), (19.1, -0.6), (20.6, 0.4), (21.1, 2.4), (20.9, 4.4), (21.0, 8.0), (22.0, 16.0),
       (23.6, 30.0), (20.8, 30.0), (19.4, 16.0), (18.4, 8.0), (17.6, 5.2), (16.4, 3.6)]
badd('bone', smooth(PS(HUM), closed=True, t=0.3))
for sd in (1, -1):
    badd('bone', smooth(PS(SCAP if sd > 0 else M(SCAP)), closed=True, t=0.3))
    sp = SPINE if sd > 0 else M(SPINE)
    badd('bone', poly(band(PS(sp), 0.8 * S, 1.6 * S, cap0=True, cap1=True)))

# ---------------------------------------------------------------- powięź piersiowo-lędźwiowa (blaszka powierzchowna)
APO = [(0.3, TH[7] - 1.0), (1.4, TH[7] - 0.6), (1.6, 17.5), (2.1, 21.5), (3.2, 25.5), (5.0, 29.5), (6.8, 33.3),
       (8.3, 36.8), (9.3, 39.6), (8.6, 41.7), (6.4, 43.7), (4.9, 46.0), (4.5, 48.5), (3.0, 51.5), (1.4, 54.0),
       (0.3, 55.0)]
apo_d = smooth(PS(APO), closed=True, t=0.25)
badd('tendon', apo_d)
# prążkowanie blaszki ścięgnistej (kierunek włókien)
stri = []
for i in range(1, 15):
    t = i / 15
    yy = TH[7] + (52.0 - TH[7]) * t
    o = (0.3, yy)
    e = (1.4 + 8.4 * min(t * 1.25, 1.0), TH[7] + (39.0 - TH[7]) * min(t * 1.18, 1.0) - 0.5)
    stri.append(f'<path class="bonel" d="{line(PS([o, e]))}"/>')
body.append(f'<defs><clipPath id="cp_apo"><path d="{apo_d}"/></clipPath></defs><g clip-path="url(#cp_apo)">{"".join(stri)}</g>')
# wyrostki kolczyste przebijają się przez powięź (przyczep)
for k in range(7, 13):
    yv = TH[k]
    badd('bonel', smooth(PS([(0.0, yv - 2.0), (0.5, yv - 1.5), (0.35, yv - 0.4), (0.0, yv), (-0.35, yv - 0.4),
                             (-0.5, yv - 1.5)]), closed=True, t=0.3))
for k in range(1, 6):
    yv = LU[k]
    badd('bonel', smooth(PS([(0.0, yv - 2.6), (0.7, yv - 2.2), (0.6, yv - 0.4), (0.0, yv), (-0.6, yv - 0.4),
                             (-0.7, yv - 2.2)]), closed=True, t=0.3))
for y in (46.8, 49.6):
    badd('bonel', smooth(PS([(0.0, y - 0.8), (0.55, y - 0.4), (0.4, y + 0.6), (0.0, y + 0.85), (-0.4, y + 0.6),
                             (-0.55, y - 0.4)]), closed=True, t=0.3))

# ---------------------------------------------------------------- m. obły większy (cały – część przy łopatce zostanie przykryta)
TM = [(8.6, 12.6), (10.4, 11.4), (12.6, 9.6), (15.0, 7.4), (17.0, 5.8), (17.9, 6.2), (17.9, 9.0), (16.6, 9.8),
      (14.0, 11.4), (11.6, 13.4), (9.8, 15.0), (9.0, 15.1)]
tm_d = smooth(PS(TM), closed=True, t=0.3)
badd('muscle', tm_d)
for a, b in (((9.4, 13.0), (17.6, 7.0)), ((9.6, 14.2), (17.6, 8.3))):
    badd('musclel', line(PS([a, b])))

# ---------------------------------------------------------------- m. najszerszy grzbietu
# wiązki żebrowe (żebra X, XI, XII) – pasma od powierzchni zewnętrznej żeber; rysowane pod brzuścem,
# widać je jako „języczki” przy końcach żeber, bocznie od brzegu mięśnia
SLIPS = []
for k in (12, 11, 10):
    e = rib_pts(k)[-1]
    pts = [(e[0] - 0.1, e[1] + 0.15), (e[0] - 0.6, e[1] - 2.6), (e[0] - 1.0, e[1] - 5.4)]
    SLIPS.append(pts)
    badd('muscle', poly(band(PS(pts), 1.5 * S, 1.7 * S, cap0=True)))
    badd('musclel', line(PS(pts)))
# zarys brzuśca (od przyczepu na powięzi, przez grzebień biodrowy i żebra, do dołu pachowego)
LD = [(1.4, TH[7] - 0.6), (3.8, TH[7] - 0.1), (6.4, 14.6), (8.3, 15.75), (9.3, 15.85), (10.9, 14.7), (12.8, 12.7),
      (14.8, 10.9), (16.4, 9.7), (17.3, 9.6), (17.5, 11.0), (17.0, 13.2), (16.0, 16.5), (14.8, 20.5), (13.2, 24.0),
      (11.7, 27.5), (10.9, 30.5), (10.7, 34.0), (10.8, 37.5), (11.3, 39.7), (10.4, 40.7), (9.3, 39.6), (8.3, 36.8),
      (6.8, 33.3), (5.0, 29.5), (3.2, 25.5), (2.1, 21.5), (1.6, 17.5)]
ld_d = smooth(PS(LD), closed=True, t=0.25)
badd('muscle', ld_d)
# włókna – zbieżnie do dołu pachowego: górne poprzecznie, dolne stromo ku górze
CONV = (17.2, 10.4)
fib = []
src = [(1.6, 13.4), (1.7, 16.5), (2.0, 20.0), (2.8, 23.8), (4.0, 27.4), (5.6, 30.9), (7.2, 34.4), (8.5, 37.4),
       (9.6, 39.9), (10.9, 40.2), (11.6, 32.0)]
for i, o in enumerate(src):
    e = (CONV[0], CONV[1] - 1.0 + 0.2 * i)
    m = lerp(o, e, 0.5)
    m = (m[0] + 0.25 * i * 0.15, m[1] + 0.4 + 0.12 * i)
    fib.append(f'<path class="musclel" d="{line(PS(cr([o, m, e], n=10)))}"/>')
# część łopatkowa (często) – nieznaczna wiązka od kąta dolnego łopatki
fib.append(f'<path class="musclel" d="{line(PS(cr([(8.95, 15.5), (12.6, 13.6), (16.9, 10.0)], n=8)))}"/>')
body.append(f'<defs><clipPath id="cp_ld"><path d="{ld_d}"/></clipPath></defs><g clip-path="url(#cp_ld)">{"".join(fib)}</g>')

# m. obły większy – część przy kości ramiennej leży NA ścięgnie m. najszerszego (ścięgno owija się dokoła niego)
body.append(f'<defs><clipPath id="cp_tm"><rect x="{CX - S * 19:.2f}" y="{Y0 + S * 4:.2f}" width="{S * 4.6:.2f}" '
            f'height="{S * 8.2:.2f}"/></clipPath></defs><g clip-path="url(#cp_tm)"><path class="muscle" d="{tm_d}"/>'
            f'<path class="musclel" d="{line(PS([(9.4, 13.0), (17.6, 7.0)]))}"/>'
            f'<path class="musclel" d="{line(PS([(9.6, 14.2), (17.6, 8.3)]))}"/></g>')
# ścięgno końcowe – ukryte (do przodu od m. obłego większego i od kości) – zarys przerywany
body.append(f'<path class="dim" d="{smooth(PS([(15.6, 9.2), (16.6, 7.6), (18.1, 5.0), (18.8, 4.5), (19.2, 9.9), (17.5, 11.0)]), closed=True, t=0.2)}"/>')
# grzebień guzka mniejszego – na przedniej stronie kości (widoczny „przez kość”: linia przerywana)
body.append(f'<path class="dim" d="{line(PS([(18.5, 3.9), (18.85, 7.0), (19.25, 10.4)]))}"/>')

# przycięcie
f.add(f'<defs><clipPath id="cp_all"><rect x="{CX - S * UL:.2f}" y="{Y0 + S * YT:.2f}" width="{S * (UL - UR):.2f}" '
      f'height="{S * (YB - YT):.2f}"/></clipPath></defs><g clip-path="url(#cp_all)">{"".join(body)}</g>')

# ---------------------------------------------------------------- strzałki
# wdech (niebieskie): ramiona ustalone – wiązki żebrowe dźwigają dolne żebra
for pts in (SLIPS[0], SLIPS[2]):
    a = lerp(pts[0], pts[1], 0.15)
    b = lerp(pts[1], pts[2], 0.6)
    f.arrow(line(PS([a, b])))
# wydech (czerwone): przy kaszlu brzeg boczny naciska bocznie na żebra
for y, u0, u1 in ((16.8, 19.4, 16.3), (21.6, 19.9, 15.0)):
    f.arrow(line([P(u0, y), P(u1, y)]), red=True)

# ---------------------------------------------------------------- podpisy – lewa kolumna
XL = 40.0


def note(x, y, t, anchor='start'):
    f.text(x, y, t, cls='note', anchor=anchor)


f.label(P(19.6, 2.6), 'kość ramienna', 'humerus', (XL, 6.0), side='L')
f.label(P(18.75, 6.0), 'grzebień guzka mniejszego', 'crista tuberculi minoris', (XL, 15.0), side='L')
note(XL - 0.7, 21.3, 'przyczep końcowy – na przedniej', 'end')
note(XL - 0.7, 24.0, 'stronie kości (linia przerywana)', 'end')
f.label(P(16.6, 7.5), 'm. obły większy', 'm. teres major', (XL, 29.5), side='L')
note(XL - 0.7, 35.8, 'ścięgno owija się dokoła niego', 'end')
f.label(P(17.2, 10.6), 'fałd pachowy tylny', 'plica axillaris posterior', (XL, 41.5), side='L')
f.label(P(16.0, 15.0), 'brzeg boczny', None, (XL, 50.5), side='L')
note(XL - 0.7, 54.1, '„mięsień kaszlu” – twardnieje', 'end')
note(XL - 0.7, 56.8, 'przy kaszlu (wydech)', 'end')
f.label(P(13.5, 27.6), 'przyczepy żebrowe', 'pars costalis', (XL, 63.0), side='L')
note(XL - 0.7, 69.3, '3–4 pasma: żebro IX lub X,', 'end')
note(XL - 0.7, 72.0, 'XI i XII', 'end')
f.label(P(10.8, 39.7), 'przyczep biodrowy', 'pars iliaca', (XL, 78.5), side='L')
note(XL - 0.7, 84.8, 'tylna ⅓ wargi zewnętrznej', 'end')
f.label(P(13.0, 41.0), 'grzebień biodrowy', 'crista iliaca', (XL, 91.0), side='L')

# ---------------------------------------------------------------- podpisy – prawa kolumna
XR = 114.0
f.label(P(-10.5, 6.5), 'łopatka', 'scapula', (XR, 8.0), side='R')
f.label(P(8.95, 15.0), 'kąt dolny łopatki', 'angulus inferior', (XR, 18.0), side='R')
note(XR + 0.7, 24.3, 'pars scapularis – często, nieznaczna część')
f.label(P(1.0, 21.0), 'przyczep kręgosłupowy', 'pars vertebralis', (XR, 32.0), side='R')
note(XR + 0.7, 38.3, 'wyrostki kolczyste Th7–Th12 i L1–L5')
f.label(P(-9.0, 27.35), 'żebro XII', 'costa XII', (XR, 46.0), side='R')
f.label(P(4.6, 36.0), 'powięź piersiowo-lędźwiowa', 'fascia thoracolumbalis', (XR, 57.0), side='R')
note(XR + 0.7, 63.3, 'blaszka powierzchowna = ścięgno')
note(XR + 0.7, 66.0, 'początkowe mięśnia')
f.label(P(-0.3, 46.9), 'grzebień krzyżowy pośrodkowy', 'crista sacralis mediana', (XR, 92.0), side='R')

# poziomy kręgów
for nm, yv in (('Th7', TH[7]), ('Th12', TH[12]), ('L5', LU[5])):
    x, y = P(-1.25, yv - 0.5)
    f.text(x, y, nm, cls='note')

# ---------------------------------------------------------------- legenda strzałek
LX, LY = 114.0, 73.0
f.arrow(f'M{LX:.2f},{LY - 0.7:.2f} L{LX + 5.5:.2f},{LY - 0.7:.2f}')
note(LX + 7.0, LY, 'wdech: ramiona ustalone – wiązki')
note(LX + 7.0, LY + 2.7, 'żebrowe dźwigają dolne żebra')
f.arrow(f'M{LX:.2f},{LY + 7.3:.2f} L{LX + 5.5:.2f},{LY + 7.3:.2f}', red=True)
note(LX + 7.0, LY + 8.0, 'wydech: kaszel – brzeg boczny')
note(LX + 7.0, LY + 10.7, 'naciska bocznie na żebra')
note(LX + 7.0, LY + 13.4, '(staw ramienny ustalony)')

f.save()
print('ok')
