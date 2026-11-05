# M. PIERSIOWY WIĘKSZY (Bochenek, t. I, s. 678–680, ryc. 443; streszczenie s. 700; oddychanie s. 697).
# Widok od przodu, strona prawa ciała (po lewej stronie rysunku).
# Przyczepy początkowe (s. 678): część obojczykowa – przyśrodkowa połowa obojczyka; część mostkowo-żebrowa –
#   powierzchnia przednia mostka (błona przednia mostka) i chrząstki żeber prawdziwych (często bez I i VII);
#   część brzuszna (czasem jej brak) – blaszka przednia pochewki m. prostego brzucha.
# Przyczep końcowy: grzebień guzka większego kości ramiennej, ścięgno 5–7 cm szerokości.
# Przebieg (s. 679): ścięgno ma warstwę przednią (grubszą: część obojczykowa + górny odcinek części
#   mostkowo-żebrowej) i tylną (cieńszą: większość części mostkowo-żebrowej + część brzuszna); warstwy łączą się
#   u dołu – „kieszonka” otwarta ku górze; włókna górne leżą z przodu, dolne z tyłu (jakby mięsień był skręcony);
#   włókna części obojczykowej zstępują najniżej, części brzusznej wstępują najwyżej.
# Strzałki (niebieskie): przy kości ramiennej – ramię wolne: przyciąga ramię przyśrodkowo (s. 679);
#   przy żebrach – ramię ustalone: mięsień pociąga klatkę piersiową, pomocniczy mięsień wdechowy (s. 680, 697).
# Schemat własny (klatka – dane jak w miesnie_oddechowe.py, większa skala).
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 160, 120
f = Fig('m_piersiowy_wiekszy', W, H,
        caption='m. piersiowy większy (strona prawa) · widok od przodu · schemat przyczepów i „kieszonki ścięgna”')
S = 2.6                      # mm na cm
CX, Y0 = 101.0, 11.0         # oś pośrodkowa; poziom górnego brzegu trzonu Th1
YT, YB = -1.6, 25.6          # przycięcie (cm)
UL, UR = 22.0, -5.2          # przycięcie w poziomie (u: + strona prawa ciała)


def P(u, y):
    """u – odległość od płaszczyzny pośrodkowej w cm (+ = strona prawa ciała, czyli lewa strona rysunku)"""
    return (CX - S * u, Y0 + S * y)


def PS(pts):
    return [P(u, y) for u, y in pts]


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

    def capf(p, q, center, w, k=7):
        a0 = math.atan2(p[1] - center[1], p[0] - center[0])
        da = math.pi
        a1 = math.atan2(q[1] - center[1], q[0] - center[0])
        # kierunek łuku: przez stronę „na zewnątrz” odcinka
        mid_ccw = (center[0] + w * math.cos(a0 + da / 2), center[1] + w * math.sin(a0 + da / 2))
        prev = c[-2] if center == c[-1] else c[1]
        if math.dist(mid_ccw, prev) < w:
            da = -math.pi
        return [(center[0] + w * math.cos(a0 + da * j / k), center[1] + w * math.sin(a0 + da * j / k)) for j in range(1, k)]
    out = list(left)
    if cap1:
        out += capf(left[-1], right[-1], c[-1], w1 / 2)
    out += right[::-1]
    if cap0:
        out += capf(right[0], left[0], c[0], w0 / 2)
    return out


def add(cls, d):
    f.add(f'<path class="{cls}" d="{d}"/>')


def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


def interp(pts, u):
    """y łamanej (u rosnące lub malejące) dla danego u"""
    for (u0, y0), (u1, y1) in zip(pts, pts[1:]):
        if (u0 - u) * (u1 - u) <= 0 and u0 != u1:
            return y0 + (y1 - y0) * (u - u0) / (u1 - u0)
    return pts[0][1] if abs(u - pts[0][0]) < abs(u - pts[-1][0]) else pts[-1][1]


# ---------------------------------------------------------------- klatka od przodu (dane jak w miesnie_oddechowe.py)
RA = [(5.8, 2.0), (9.0, 4.9), (11.3, 7.6), (12.9, 10.2), (14.0, 12.8), (14.7, 15.4), (15.1, 18.0), (15.2, 20.5),
      (15.0, 22.9), (14.6, 25.1), (14.0, 27.0), (12.9, 28.6)]
RJ = [(3.8, 4.6), (5.8, 8.3), (7.2, 11.4), (8.3, 14.2), (9.2, 17.0), (9.9, 19.8), (10.6, 22.6), (11.3, 25.0),
      (12.1, 27.2), (12.9, 29.2), (13.3, 30.0), (12.0, 31.0)]
RW = [(1.5, 1.6), (1.1, 1.3), (0.9, 1.2), (0.9, 1.2), (0.9, 1.15), (0.9, 1.15), (0.9, 1.1), (0.85, 1.05),
      (0.85, 1.0), (0.8, 0.95), (0.75, 0.7), (0.7, 0.65)]
CART = [[(3.8, 4.6), (2.3, 5.3)],
        [(5.8, 8.3), (4.0, 8.8), (2.2, 9.0)],
        [(7.2, 11.4), (4.7, 11.7), (2.3, 11.8)],
        [(8.3, 14.2), (5.3, 14.4), (2.3, 14.3)],
        [(9.2, 17.0), (5.8, 17.0), (2.2, 16.6)],
        [(9.9, 19.8), (6.2, 19.6), (2.0, 18.6)],
        [(10.6, 22.6), (6.7, 22.1), (3.4, 20.8), (1.7, 19.8)],
        [(11.3, 25.0), (8.5, 24.4), (6.3, 22.6)],
        [(12.1, 27.2), (10.0, 26.6), (8.3, 25.0)],
        [(12.9, 29.2), (11.6, 28.8), (10.1, 27.3)]]
STERN_HALF = [(0, 4.5), (1.3, 4.1), (2.5, 3.8), (2.75, 4.9), (2.35, 6.2), (1.65, 8.2), (1.55, 8.9), (1.65, 9.3),
              (1.85, 11.6), (1.95, 14.0), (2.05, 16.4), (1.95, 18.5), (1.5, 19.7), (1.0, 20.1), (0.95, 21.9), (0.45, 23.1)]


def rib_mid(a, j):
    return (a[0] - (a[0] - j[0]) * 0.30, a[1] + (j[1] - a[1]) * 0.60)


def mirror_u(pts):
    return [(-u, y) for u, y in pts]


body = []          # rysunek przycinany


def badd(cls, d):
    body.append(f'<path class="{cls}" d="{d}"/>')


# żebra I–X (obie strony; lewa strona ciała przycięta)
for sd in (1, -1):
    for k in range(10):
        a, j = RA[k], RJ[k]
        pts = [a, rib_mid(a, j), j]
        if sd < 0:
            pts = mirror_u(pts)
        badd('bone', poly(band(PS(pts), RW[k][0] * S, RW[k][1] * S, cap0=True)))
    for k in range(10):
        w = (0.95 if k < 7 else 0.85) * S
        pts = CART[k] if sd > 0 else mirror_u(CART[k])
        badd('cart', poly(band(PS(pts), w, w * (0.95 if k < 7 else 0.85), cap1=(k >= 7))))
# mostek
outline = PS(STERN_HALF) + [P(0, 23.5)] + PS(mirror_u(list(reversed(STERN_HALF[1:]))))
badd('bone', smooth(outline, closed=True, t=0.35))
for y in (8.95, 19.75):
    hw = 1.55 if y < 10 else 1.45
    badd('bonel', line([P(hw, y), P(-hw, y)]))

# pochewka m. prostego brzucha – blaszka przednia (strona prawa ciała; dół przycięty)
SHEATH = [(0.55, 21.0), (1.4, 19.9), (3.2, 19.3), (5.6, 19.0), (7.9, 19.6), (8.6, 21.0), (8.7, 23.5), (8.8, 27.0),
          (0.55, 27.0)]
badd('tendon', poly(PS(cr(SHEATH[:7], n=4) + SHEATH[7:])))
badd('bonel', line(PS([(0.55, 21.0), (0.55, 27.0)])))

# kość ramienna (strona prawa): głowa, guzek większy, guzek mniejszy, bruzda międzyguzkowa, grzebienie
HUM = [(17.2, 6.4), (16.2, 5.2), (15.9, 3.6), (16.6, 2.3), (17.9, 1.7), (19.4, 1.9), (20.6, 2.6), (21.2, 3.9),
       (21.0, 5.6), (20.4, 7.2), (20.2, 10.0), (20.25, 16.0), (20.3, 26.5), (17.7, 26.5), (17.7, 16.0), (17.6, 10.0),
       (17.4, 7.6)]
badd('bone', smooth(PS(HUM), closed=True, t=0.3))
badd('bonel', line(PS(cr([(16.4, 5.0), (17.6, 5.7), (18.5, 5.4)], n=6))))               # szyjka anatomiczna (zarys)
badd('bonel', line(PS(cr([(19.9, 2.4), (19.4, 3.8), (19.6, 5.6), (19.75, 8.0), (19.55, 14.8)], n=8))))   # grzebień guzka większego
badd('bonel', line(PS(cr([(18.7, 5.4), (18.3, 6.6), (18.2, 9.0), (18.25, 13.6)], n=8))))   # grzebień guzka mniejszego
# obojczyk + wyrostek barkowy
CLAV = [(2.7, 4.1), (5.0, 3.45), (8.0, 2.9), (11.0, 2.3), (14.0, 1.55), (16.7, 0.75)]
ACR = [(16.1, 0.0), (17.6, -0.6), (19.6, -0.4), (20.9, 0.4), (20.5, 1.3), (18.6, 1.4), (16.9, 1.6)]


def clav_low(u):
    return interp(CLAV, u) + 0.82


# ================================================================ m. piersiowy większy
# Trzy warstwy rysunku (od tyłu): 1) dolny odcinek części mostkowo-żebrowej + część brzuszna (warstwa tylna ścięgna),
# 2) górny odcinek części mostkowo-żebrowej, 3) część obojczykowa (2 + 3 = warstwa przednia ścięgna).
# Na grzebieniu: część obojczykowa najniżej, część brzuszna najwyżej – włókna skrzyżowane („skręcenie”).
CREST_TOP, CREST_BOT = 6.9, 13.7


def crest(y):
    return (19.75 - 0.2 * (y - 6.0) / 8.0, y)


def fiber(o, e, bend=0.0):
    """włókno od przyczepu początkowego o do końcowego e – lekko wygięte; przedłużone poza oba końce (przycinane)"""
    dx, dy = e[0] - o[0], e[1] - o[1]
    ln = math.hypot(dx, dy) or 1
    o2 = (o[0] - dx / ln * 0.8, o[1] - dy / ln * 0.8)
    e2 = (e[0] + dx / ln * 0.8, e[1] + dy / ln * 0.8)
    m = lerp(o, e, 0.55)
    m = (m[0] - dy / ln * bend, m[1] + dx / ln * bend)
    return cr([o2, m, e2], n=12)


def layer(outline, orig, ins, bend, cid, ten):
    d = smooth(PS(outline), closed=True, t=0.25)
    body.append(f'<defs><clipPath id="{cid}"><path d="{d}"/></clipPath></defs>')
    badd('muscle', d)
    fib = ''.join(f'<path class="musclel" d="{line(PS(fiber(o, e, bend)))}"/>' for o, e in zip(orig, ins))
    fib += f'<path class="tendon" d="{smooth(PS(ten), closed=True, t=0.15)}"/>'
    body.append(f'<g clip-path="url(#{cid})">{fib}</g>')


O_CLAV = [(u, clav_low(u)) for u in (9.7, 8.4, 7.1, 5.8, 4.5, 3.2)]
O_UP = [(1.05, 5.9), (1.05, 7.3), (1.05, 8.7)]
O_LOW = [(1.05, y) for y in (10.4, 12.0, 13.6, 15.2, 16.6)] + [(1.6, 17.8), (3.2, 18.6), (5.0, 19.1)] + \
        [(6.6, 19.9), (7.8, 20.6), (8.8, 21.3)]

# 1) warstwa tylna: cały zarys mięśnia; włókna dolne kończą się najwyżej
SIL = ([(10.2, clav_low(10.2))] + [(u, clav_low(u)) for u in (8.0, 6.0, 4.0)] + [(3.0, 4.95), (1.7, 5.35), (1.05, 6.3),
       (1.0, 10.0), (1.0, 14.0), (1.1, 17.0), (2.2, 18.3), (4.0, 18.95), (5.6, 19.3), (6.7, 19.95), (8.0, 20.75),
       (9.0, 21.3), (10.6, 21.0), (12.8, 19.5), (14.9, 17.4), (16.5, 15.5), (17.6, 14.55), crest(CREST_BOT),
       crest(10.0), crest(CREST_TOP), (18.5, 6.65), (17.5, 7.5), (16.6, 8.8), (15.0, 8.2), (12.6, 6.1), (11.2, 4.35)])
LOW_INS = [crest(10.2 - (10.2 - 7.05) * i / (len(O_LOW) - 1)) for i in range(len(O_LOW))]
layer(SIL, O_LOW, LOW_INS, 0.35, 'cp_l1', [(18.15, 10.4), (17.9, 8.2), (18.3, 6.7), crest(CREST_TOP), crest(10.5)])
# 2) górny odcinek części mostkowo-żebrowej
UP = [(1.05, 5.3), (1.05, 9.3), (6.0, 10.25), (11.0, 10.95), (15.5, 11.35), (18.2, 11.5), crest(11.5), crest(10.25),
      (17.4, 9.95), (13.0, 8.7), (8.0, 7.1), (4.0, 5.85), (1.8, 5.35)]
UP_INS = [crest(10.5), crest(10.85), crest(11.2)]
layer(UP, O_UP, UP_INS, 0.1, 'cp_l2', [(18.2, 10.1), crest(10.2), crest(11.6), (18.3, 11.6)])
# 3) część obojczykowa – włókna równoległe ku dołowi i w bok; kończy się najniżej
CB = ([(10.3, clav_low(10.3) - 0.05)] + [(u, clav_low(u)) for u in (8.0, 6.0, 4.0)] + [(3.0, 4.95), (2.4, 5.3),
      (7.0, 7.45), (12.0, 10.05), (16.0, 12.4), (17.6, 14.55), crest(CREST_BOT), crest(11.0), (17.4, 10.0),
      (15.0, 8.25), (12.6, 6.15), (11.2, 4.4)])
CL_INS = [crest(11.3 + (CREST_BOT - 11.3) * i / (len(O_CLAV) - 1)) for i in range(len(O_CLAV))]
layer(CB, O_CLAV, CL_INS, -0.1, 'cp_l3', [(17.95, 11.0), crest(10.95), crest(CREST_BOT), (18.6, 14.4), (17.9, 14.25),
                                           (17.7, 12.4)])
# dolny brzeg ścięgna – tu obie warstwy łączą się („kieszonka” otwarta ku górze)
badd('bonel', line(PS(cr([(16.9, 14.6), (17.9, 14.75), (18.9, 14.4), crest(13.75)], n=6))))

# obojczyk i wyrostek barkowy (na wierzchu – przykrywa brzeg przyczepu części obojczykowej)
badd('bone', smooth(PS(ACR), closed=True, t=0.35))
badd('bone', poly(band(PS(CLAV), 1.75 * S, 1.2 * S, cap0=True, cap1=True)))

# przycięcie
f.add(f'<defs><clipPath id="cp_pm"><rect x="{CX - S * UL:.2f}" y="{Y0 + S * YT:.2f}" width="{S * (UL - UR):.2f}" '
      f'height="{S * (YB - YT):.2f}"/></clipPath></defs><g clip-path="url(#cp_pm)">{"".join(body)}</g>')

# ================================================================ strzałki
# ramię wolne – mięsień przyciąga ramię przyśrodkowo
f.arrow(line([P(21.9, 20.4), P(18.1, 20.4)]))
# ramię ustalone – mięsień pociąga żebra i mostek (pomocniczy wdech)
f.arrow(line(PS([(3.4, 17.0), (6.4, 15.2)])))
f.arrow(line(PS([(8.4, 20.3), (10.9, 17.9)])))

# ================================================================ podpisy – lewa kolumna (kość ramienna)
XL = 40.0


def note(x, y, t, anchor='start'):
    f.text(x, y, t, cls='note', anchor=anchor)


f.label(P(20.4, 4.0), 'guzek większy', 'tuberculum majus', (XL, 14.0), side='L')
f.label(P(19.65, 5.4), 'grzebień guzka większego', 'crista tuberculi majoris', (XL, 26.0), side='L')
note(XL - 0.7, 32.3, 'przyczep końcowy · ścięgno 5–7 cm', 'end')
f.label(P(18.75, 8.4), 'warstwa tylna ścięgna', None, (XL, 38.0), side='L')
note(XL - 0.7, 41.6, 'część brzuszna i większość', 'end')
note(XL - 0.7, 44.3, 'części mostkowo-żebrowej', 'end')
f.label(P(18.75, 12.4), 'warstwa przednia ścięgna', None, (XL, 49.5), side='L')
note(XL - 0.7, 53.1, 'część obojczykowa i górny odcinek', 'end')
note(XL - 0.7, 55.8, 'części mostkowo-żebrowej', 'end')
f.label(P(18.0, 14.3), '„kieszonka” ścięgna', None, (XL, 61.0), side='L')
note(XL - 0.7, 64.6, 'obie warstwy łączą się u dołu', 'end')
f.label(P(19.0, 23.5), 'kość ramienna', 'humerus', (XL, 72.0), side='L')

# ================================================================ podpisy – prawa kolumna (przyczepy początkowe)
XR = 118.5
f.label(P(5.6, 3.1), 'obojczyk', 'clavicula', (XR, 13.0), side='R')
f.label(P(6.6, 5.3), 'część obojczykowa', 'pars clavicularis', (XR, 21.5), side='R')
note(XR + 0.7, 27.8, 'przyśrodkowa połowa obojczyka')
f.label(P(-0.6, 13.0), 'mostek', 'sternum', (XR, 34.0), side='R')
note(XR + 0.7, 40.3, 'powierzchnia przednia (błona przednia)')
f.label(P(6.0, 13.2), 'część mostkowo-żebrowa', 'pars sternocostalis', (XR, 46.0), side='R')
f.label(P(-3.6, 14.4), 'chrząstka żebrowa', 'cartilago costalis', (XR, 55.0), side='R')
note(XR + 0.7, 61.3, 'żebra prawdziwe – często bez I i VII')
f.label(P(9.2, 18.8), 'część brzuszna', 'pars abdominalis', (XR, 67.0), side='R')
note(XR + 0.7, 73.3, 'czasem jej brak')
f.label(P(4.0, 23.6), 'pochewka m. prostego brzucha', 'vagina m. recti abdominis', (XR, 79.0), side='R')
note(XR + 0.7, 85.3, 'blaszka przednia')

# ================================================================ wstawka: przekrój przez ścięgno końcowe („kieszonka”)
IX, IY = 30.0, 86.0           # lewy górny róg obszaru wstawki
f.text(IX + 8.0, IY + 1.6, 'przekrój ścięgna końcowego (schemat)', cls='notec')
# warstwa przednia (grubsza, po lewej = przód), warstwa tylna (cieńsza, po prawej), połączone u dołu
UX0, UX1, UTOP, UBOT = IX + 3.8, IX + 12.6, IY + 5.0, IY + 25.0
front = [(UX0, UTOP), (UX0 + 2.4, UTOP), (UX0 + 2.4, UBOT - 4.2)]
U_OUT = [(UX0, UTOP), (UX0 + 2.5, UTOP), (UX0 + 2.5, UBOT - 4.6)]
inner = cr([(UX0 + 2.5, UBOT - 4.6), (UX0 + 4.4, UBOT - 2.2), (UX1 - 1.2, UBOT - 4.4)], n=8)
outer = cr([(UX1, UBOT - 4.6), (UX1 - 1.6, UBOT - 0.3), (UX0 + 3.6, UBOT), (UX0 + 0.2, UBOT - 3.4)], n=8)
U = [(UX0, UTOP), (UX0 + 2.5, UTOP)] + inner + [(UX1 - 1.2, UTOP + 2.5), (UX1, UTOP + 2.5)] + outer
f.add(f'<path class="cavity" d="{poly([(UX0 + 2.5, UTOP)] + inner + [(UX1 - 1.2, UTOP + 2.5)])}"/>')
f.add(f'<path class="shade" d="{poly([(UX0 + 2.5, UTOP + 1.5)] + inner + [(UX1 - 1.2, UTOP + 3.5)])}"/>')
f.add(f'<path class="tendon" d="{poly(U)}"/>')
f.text(UX0 - 0.6, UBOT + 3.6, 'przód', cls='note', anchor='middle')
f.text(UX1 + 0.4, UBOT + 3.6, 'tył', cls='note', anchor='middle')
f.label((UX0 + 1.2, UTOP + 7.0), 'warstwa przednia', None, (IX - 4.0, UTOP + 4.0), side='L')
note(IX - 4.7, UTOP + 7.6, 'grubsza', 'end')
f.label((UX1 - 0.6, UTOP + 8.0), 'warstwa tylna', None, (IX + 18.0, UTOP + 4.0), side='R')
note(IX + 18.7, UTOP + 7.6, 'cieńsza')
f.label((UX0 + 5.0, UTOP + 10.5), '„kieszonka”', None, (IX + 18.0, UTOP + 13.5), side='R')
note(IX + 18.7, UTOP + 17.1, 'otwarta ku górze; luźna tkanka')
note(IX + 18.7, UTOP + 19.8, 'łączna i tłuszczowa')

# ================================================================ legenda strzałek
LX, LY = 80.0, 92.0
f.arrow(f'M{LX:.2f},{LY - 0.7:.2f} L{LX + 6:.2f},{LY - 0.7:.2f}')
note(LX + 8.0, LY, 'przy kości ramiennej – ramię wolne: przyciąga ramię przyśrodkowo')
note(LX + 8.0, LY + 2.7, 'i do przodu, opuszcza podniesione ramię, obraca je do wewnątrz')
f.arrow(f'M{LX:.2f},{LY + 8.0:.2f} L{LX + 6:.2f},{LY + 8.0:.2f}')
note(LX + 8.0, LY + 8.7, 'przy żebrach – ramię ustalone (np. chwyt brzegu stołu):')
note(LX + 8.0, LY + 11.4, 'mięsień pociąga klatkę piersiową → pomocniczy mięsień wdechowy')
note(LX + 8.0, LY + 15.4, 'oba mm. piersiowe – pomocnicze mięśnie wdechowe (s. 680, 697)')

f.save()
print('ok')
