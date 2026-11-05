# M. POPRZECZNY KLATKI PIERSIOWEJ – przednia ściana klatki piersiowej widziana od tyłu (od strony jamy klatki).
# Widok od tyłu: prawa strona ciała po prawej stronie rysunku. Bochenek, t. I, s. 688–689 (ryc. 450), s. 697, 700.
#  * położony do tyłu od mostka i przylegających chrząstek żebrowych; płaski, bardzo cienki, trójkątny, zanikowy;
#  * przyczep początkowy: powierzchnia tylna wyrostka mieczykowatego i części dolnej trzonu mostka;
#  * włókna większej, dolnej części – poprzecznie; części górnej – skośnie ku górze i bocznie;
#  * przyczep końcowy: przeważnie 5 zębów na granicy chrzęstno-kostnej żeber VI–II; górne pasma mijają
#    przeważnie dwa międzyżebrza;
#  * między nim a mostkiem / chrząstkami / mm. międzyżebrowymi – naczynia piersiowe wewnętrzne (wzdłuż mostka);
#  * ku dołowi łączy się bezpośrednio z m. poprzecznym brzucha (u obu włókna poprzeczne);
#  * czynność: część dolna zmniejsza kąt przyczepu chrząstki żebrowej do mostka – wydech.
# Geometria klatki (cm) jak w miesnie_oddechowe.py / oddychanie_wymiary.py; przepona usunięta.
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 160, 98
f = Fig('m_poprzeczny_klatki', W, H,
        caption='m. poprzeczny klatki piersiowej · przednia ściana klatki piersiowej od tyłu (prawa strona ciała po prawej) · przepona usunięta')
S = 3.05
CX, Y0 = 74.0, -1.0
YCUT = 27.2                     # dolne cięcie (cm)


def cr(pts, n=12, t=0.5):
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


def poly(pts, close=True):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + (' Z' if close else '')


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
        a1 = math.atan2(q[1] - center[1], q[0] - center[0])
        da = a1 - a0
        while da > 0: da -= 2 * math.pi
        if abs(da) < math.pi * 0.9: da += 2 * math.pi
        da = -math.pi if da < 0 else math.pi
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


def Pt(u, y, side):
    """side=+1 – prawa strona ciała (prawa strona rysunku, widok od tyłu)"""
    return (CX + side * S * u, Y0 + S * y)


def PS(pts, side):
    return [Pt(u, y, side) for u, y in pts]


# ---------------------------------------------------------------- dane klatki (cm; u – od płaszczyzny pośrodkowej)
RA = [(5.8, 2.0), (9.0, 4.9), (11.3, 7.6), (12.9, 10.2), (14.0, 12.8), (14.7, 15.4), (15.1, 18.0), (15.2, 20.5)]
RJ = [(3.8, 4.6), (5.8, 8.3), (7.2, 11.4), (8.3, 14.2), (9.2, 17.0), (9.9, 19.8), (10.6, 22.6), (11.3, 25.0)]
RW = [1.5, 1.1, 0.9, 0.9, 0.9, 0.9, 0.9, 0.85]
CART = [[(3.8, 4.6), (2.3, 5.3)],
        [(5.8, 8.3), (4.0, 8.8), (2.2, 9.0)],
        [(7.2, 11.4), (4.7, 11.7), (2.3, 11.8)],
        [(8.3, 14.2), (5.3, 14.4), (2.3, 14.3)],
        [(9.2, 17.0), (5.8, 17.0), (2.2, 16.6)],
        [(9.9, 19.8), (6.2, 19.6), (2.0, 18.6)],
        [(10.6, 22.6), (6.7, 22.1), (3.4, 20.8), (1.7, 19.8)],
        [(11.3, 25.0), (8.5, 24.4), (6.3, 22.6)]]
STERN_HALF = [(0, 4.5), (1.3, 4.1), (2.5, 3.8), (2.75, 4.9), (2.35, 6.2), (1.65, 8.2), (1.55, 8.9), (1.65, 9.3),
              (1.85, 11.6), (1.95, 14.0), (2.05, 16.4), (1.95, 18.5), (1.5, 19.7), (1.0, 20.1), (0.95, 21.9), (0.45, 23.1)]
UCUT = 11.6


def rib_mid(a, j):
    return (a[0] - (a[0] - j[0]) * 0.30, a[1] + (j[1] - a[1]) * 0.60)


def axis(k):
    """oś żebra k (cm): od mostka przez chrząstkę i granicę chrzęstno-kostną do bocznego cięcia"""
    c = list(reversed(cr(CART[k], n=10)))                 # od mostka do RJ
    b = cr([RJ[k], rib_mid(RA[k], RJ[k]), RA[k]], n=24)   # od RJ do RA
    uend = min(UCUT, RA[k][0] - 0.45)
    b2 = [p for p in b if p[0] <= uend]
    if b2[-1][0] < uend:
        # dociągnięcie do uend
        for p, q in zip(b, b[1:]):
            if p[0] <= uend <= q[0]:
                t = (uend - p[0]) / (q[0] - p[0])
                b2.append((uend, p[1] + (q[1] - p[1]) * t))
                break
    return c, b2


AX = [axis(k) for k in range(8)]


def y_on(k, u):
    pts = AX[k][0] + AX[k][1][1:]
    if u <= pts[0][0]:
        return pts[0][1]
    for p, q in zip(pts, pts[1:]):
        if (p[0] - u) * (q[0] - u) <= 0 and p[0] != q[0]:
            return p[1] + (q[1] - p[1]) * (u - p[0]) / (q[0] - p[0])
    return pts[-1][1]


def uend(k):
    return AX[k][1][-1][0]


# ---------------------------------------------------------------- 1. mm. międzyżebrowe (tło przestrzeni)
for sd in (-1, 1):
    for k in range(7):
        top = [(0.0, y_on(k, 0.0))] + AX[k][0] + AX[k][1][1:]
        bot = [(0.0, y_on(k + 1, 0.0))] + AX[k + 1][0] + AX[k + 1][1][1:]
        if k == 6:          # przestrzeń VII–VIII: chrząstka VIII dochodzi do chrząstki VII
            bot = [(6.3, 22.6)] + AX[7][0][1:] + AX[7][1][1:]
        pg = top + list(reversed(bot))
        add('muscle', poly(PS(pg, sd)))
        # włókna: ku dołowi i bocznie (w stronę kręgosłupa)
        d = []
        u = 2.5
        while u < min(uend(k), uend(k + 1)) - 0.6:
            y0 = y_on(k, u) + RW[k] * 0.45
            u1 = u + 0.9
            y1 = y_on(k + 1, u1) - RW[k + 1] * 0.45
            if k == 6 and u1 < 6.3:
                u += 0.42
                continue
            a, b = Pt(u, y0, sd), Pt(u1, y1, sd)
            d.append(f'M{a[0]:.2f},{a[1]:.2f} L{b[0]:.2f},{b[1]:.2f}')
            u += 0.42
        add('musclel', ' '.join(d))

# ---------------------------------------------------------------- 2. żebra (kość żebrowa) i chrząstki
for sd in (-1, 1):
    for k in range(8):
        cpts, bpts = AX[k]
        bb = PS(bpts, sd)
        add('bone', poly(band(bb, RW[k] * S, RW[k] * S * 0.95, n=4)))
        # powierzchnia przekroju na bocznym końcu
        e, e0 = bb[-1], bb[-2]
        ang = math.degrees(math.atan2(e[1] - e0[1], e[0] - e0[0]))
        f.add(f'<ellipse class="bone2" cx="{e[0]:.2f}" cy="{e[1]:.2f}" rx=".75" ry="{RW[k] * S * 0.5:.2f}" '
              f'transform="rotate({ang:.1f} {e[0]:.2f} {e[1]:.2f})"/>')
    for k in range(8):
        w = 0.95 * S
        add('cart', poly(band(PS(CART[k], sd), w, w * (0.95 if k < 7 else 0.8), cap1=(k == 7))))

# ---------------------------------------------------------------- 3. mostek (powierzchnia tylna)
outline = PS(STERN_HALF, -1) + [Pt(0, 23.5, -1)] + PS(list(reversed(STERN_HALF[1:])), 1)
add('bone', smooth(outline, closed=True, t=0.35))
for y, hw_ in ((8.95, 1.55), (19.75, 1.45)):
    add('bonel', poly([Pt(hw_, y, -1), Pt(hw_, y, 1)], close=False))

# ---------------------------------------------------------------- 4. t. piersiowa wewnętrzna (między ścianą a mięśniem)
for sd in (-1, 1):
    ITA = PS([(3.15, 4.9), (3.0, 9.0), (2.95, 13.0), (3.0, 17.0), (3.2, 21.0)], sd)
    add('artery', poly(band(ITA, 0.75, 0.7, n=10)))

# ---------------------------------------------------------------- 5. m. poprzeczny brzucha (ku dołowi – przedłużenie)
for sd in (-1, 1):
    TA = [(0.25, 22.05), (2.4, 21.6), (4.6, 21.25), (6.7, 21.45), (8.6, 22.0), (10.6, 22.95), (11.15, 24.6),
          (11.35, YCUT), (0.25, YCUT)]
    add('muscle', poly(PS(cr(TA[:7], n=6) + TA[7:], sd)))
    d = []
    yy = 22.3
    while yy < YCUT - 0.2:
        ul = 0.5
        ur = min(10.9, 6.0 + (yy - 21.4) * 2.2)
        if ur > ul + 0.5:
            a, b = Pt(ul, yy, sd), Pt(ur, yy + 0.08, sd)
            d.append(f'M{a[0]:.2f},{a[1]:.2f} L{b[0]:.2f},{b[1]:.2f}')
        yy += 0.42
    add('musclel', ' '.join(d))

# ---------------------------------------------------------------- 6. m. poprzeczny klatki piersiowej – wachlarz 5 zębów (II–VI)
#  początek: tylna powierzchnia dolnej części trzonu mostka i wyrostka mieczykowatego (pasmo przy linii pośrodkowej)
ORG = [(13.5, 15.0), (15.0, 16.7), (16.7, 18.4), (18.4, 20.2), (20.2, 22.05)]   # odcinki początku (y0, y1) dla żeber II..VI
TOOTH = []
for sd in (-1, 1):
    for i, k in enumerate(range(1, 6)):
        y0, y1 = ORG[i]
        j = RJ[k]
        tw = 0.36 + 0.06 * i                   # połowa szerokości zęba
        tip = (j[0] + 0.25, j[1])
        # kierunek pasma
        dx, dy = tip[0] - 0.25, tip[1] - (y0 + y1) / 2
        ln = math.hypot(dx, dy)
        nx, ny = -dy / ln, dx / ln
        ta = (tip[0] + nx * tw, tip[1] + ny * tw)
        tb = (tip[0] - nx * tw, tip[1] - ny * tw)
        oa, ob = (0.25, y0), (0.25, y1)
        # lekko wklęsłe brzegi (wachlarz)
        ma = ((oa[0] + ta[0]) / 2 + nx * 0.15, (oa[1] + ta[1]) / 2 + ny * 0.15)
        mb = ((ob[0] + tb[0]) / 2 - nx * 0.15, (ob[1] + tb[1]) / 2 - ny * 0.15)
        if ta[1] > tb[1]:
            ta, tb = tb, ta
        shape = cr([oa, ((oa[0] + ta[0]) / 2, (oa[1] + ta[1]) / 2 - 0.05), ta], n=6) + \
            [(tip[0] + 0.15, tip[1])] + cr([tb, ((ob[0] + tb[0]) / 2, (ob[1] + tb[1]) / 2 + 0.05), ob], n=6)
        add('muscle', poly(PS(shape, sd)))
        d = []
        for q in range(7):
            t = (q + 0.5) / 7
            o = (0.3, y0 + (y1 - y0) * t)
            e = (ta[0] + (tb[0] - ta[0]) * t, ta[1] + (tb[1] - ta[1]) * t)
            a, b = Pt(*o, sd), Pt(e[0] - 0.1, e[1], sd)
            d.append(f'M{a[0]:.2f},{a[1]:.2f} L{b[0]:.2f},{b[1]:.2f}')
        add('musclel', ' '.join(d))
        if sd == 1:
            TOOTH.append(tip)

# strzałka: część dolna ciągnie granicę chrzęstno-kostną ku mostkowi (wydech) – lewa strona ciała
a, b = Pt(8.6, 21.05, -1), Pt(5.4, 21.35, -1)
f.arrow(f'M{a[0]:.2f},{a[1]:.2f} L{b[0]:.2f},{b[1]:.2f}', red=True)

# ---------------------------------------------------------------- numery żeber (przy bocznych końcach, lewa strona rysunku)
ROM = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']
NUMY = []
for k in range(8):
    u, y = AX[k][1][-1]
    x, yy = Pt(u + 0.3, y, 1)
    f.text(x, yy + 0.75, ROM[k], cls='note')
    NUMY.append((round(x, 1), round(yy, 1)))

# ---------------------------------------------------------------- podpisy
XL, XR = 36.5, 117.0


def note(x, y, t, anchor):
    f.text(x, y, t, cls='note', anchor=anchor)


def lab(at, pl, la, to, side, nts=()):
    f.label(at, pl, la, to, side=side)
    x = to[0] + (0.7 if side == 'R' else -0.7)
    for i, t in enumerate(nts):
        note(x, to[1] + (6.3 if la else 3.6) + 2.6 * i, t, 'start' if side == 'R' else 'end')


def gap_pt(k, u, side):
    return Pt(u, (y_on(k, u) + y_on(k + 1, u)) / 2, side)


# lewa kolumna (lewa strona ciała)
lab(Pt(1.0, 6.2, -1), 'rękojeść mostka', 'manubrium sterni', (XL, 5.0), 'L')
lab(Pt(3.0, 7.2, -1), 't. piersiowa wewnętrzna', 'a. thoracica interna', (XL, 14.0), 'L', ('między ścianą a mięśniem',))
lab(Pt(5.6, 11.75, -1), 'chrząstka żebrowa', 'cartilago costalis', (XL, 26.5), 'L')
lab(Pt(1.1, 12.6, -1), 'trzon mostka', 'corpus sterni', (XL, 36.0), 'L')
lab(Pt(10.2, y_on(4, 10.2), -1), 'kość żebrowa', 'os costale', (XL, 46.0), 'L')
lab(Pt(0.0, 22.85, -1), 'wyrostek mieczykowaty', 'processus xiphoideus', (XL, 62.0), 'L')
lab(Pt(6.0, 24.6, -1), 'm. poprzeczny brzucha', 'm. transversus abdominis', (XL, 74.0), 'L',
    ('ku górze łączy się', 'bezpośrednio z m. poprzecznym', 'klatki piersiowej'))
# prawa kolumna (prawa strona ciała)
lab(Pt(RJ[1][0] + 0.05, RJ[1][1], 1), 'granica chrzęstno-kostna', None, (XR, 21.5), 'R',
    ('5 zębów: żebra II–VI', 'górne pasma mijają 2 międzyżebrza'))
lab(Pt(3.2, 11.1, 1), 'część górna', None, (XR, 33.5), 'R', ('włókna skośnie ku górze i bocznie',))
lab(Pt(3.4, 16.25, 1), 'm. poprzeczny klatki piersiowej', 'm. transversus thoracis', (XR, 43.0), 'R',
    ('początek: tylna powierzchnia', 'wyrostka mieczykowatego', 'i dolnej części trzonu mostka'))
lab(Pt(6.5, 20.4, 1), 'część dolna (większa)', None, (XR, 61.0), 'R', ('włókna poprzeczne · wydech',))
lab(gap_pt(5, 10.3, 1), 'mm. międzyżebrowe wewnętrzne', 'mm. intercostales interni', (92.0, 86.0), 'R')

f.save()
print('ok')
