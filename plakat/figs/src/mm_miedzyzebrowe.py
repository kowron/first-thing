# MIĘŚNIE MIĘDZYŻEBROWE – schemat przestrzeni międzyżebrowej („ściana rozwinięta”; przód w lewo, kręgosłup w prawo).
# Bochenek, t. I, s. 685–688 (ryc. 447–449), streszczenie s. 700; dźwigacze żeber s. 671.
#  * mm. międzyżebrowe zewnętrzne: od guzków żeber do bocznych końców chrząstek żebrowych; z tyłu łączą się
#    z dźwigaczami żeber; z przodu – błony międzyżebrowe zewnętrzne (ten sam kierunek włókien); włókna ku dołowi
#    i do mostka (s. 685);
#  * mm. międzyżebrowe wewnętrzne: od okolicy kątów żeber do mostka; włókna ku dołowi i w stronę kręgosłupa;
#    dwie warstwy: zewnętrzna – mm. międzyżebrowe pośrednie (do mostka), wewnętrzna – mm. międzyżebrowe najgłębsze
#    (kończą się na granicy chrzęstno-kostnej); ku tyłowi, w przedłużeniu mm. pośrednich aż do kręgosłupa – błony
#    międzyżebrowe wewnętrzne (s. 686–687); naczynia i nerwy oddzielają warstwę najgłębszą (s. 688, 700);
#  * mm. podżebrowe: powierzchnia wewnętrzna dolnych żeber w okolicy kątów, włókna jak w mm. wewnętrznych,
#    mijają 1–2 żebra (s. 687);
#  * mm. dźwigacze żeber: wyrostki poprzeczne → następne żebro, włókna ku bokowi i ku dołowi (s. 671).
# U góry: lewa ściana od zewnątrz; u dołu: prawa ściana od wewnątrz (w obu widokach przód po lewej) –
# w środku pasek „co wypełnia przestrzeń” wyrównany do punktów orientacyjnych żebra.
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig

W, H = 160, 124
f = Fig('mm_miedzyzebrowe', W, H,
        caption='przestrzenie międzyżebrowe · ściana klatki „rozwinięta” (schemat), przód w lewo · '
                'u góry od zewnątrz, u dołu od wewnątrz')

# punkty orientacyjne wzdłuż żebra (x, mm rysunku)
XS0, XS1 = 12.0, 21.0      # mostek (brzeg boczny = XS1)
XCC = 45.0                 # granica chrzęstno-kostna (boczny koniec chrząstki)
XANG = 102.0               # kąt żebra
XTUB = 117.0               # guzek żebra
XV0, XV1 = 127.0, 139.0    # kręgosłup
XI1 = 97.0                 # tylny brzeg mm. najgłębszych (nieco bocznie od kąta)
XWIN = (50.0, 90.0)        # okno w warstwie mm. zewnętrznych (widok od zewnątrz)


def interp(ctrl, x):
    if x <= ctrl[0][0]:
        return ctrl[0][1]
    for (x0, v0), (x1, v1) in zip(ctrl, ctrl[1:]):
        if x <= x1:
            a = (x - x0) / (x1 - x0)
            a = a * a * (3 - 2 * a)
            return v0 + (v1 - v0) * a
    return ctrl[-1][1]


PITCH = [(12, 10.6), (45, 11.3), (75, 11.6), (102, 10.9), (117, 10.2), (139, 9.8)]
GOFF = [(12, -1.2), (45, 0.0), (75, -0.5), (102, -1.8), (117, -2.6), (139, -3.2)]
HW = [(12, 1.65), (43, 1.65), (47, 2.05), (100, 2.05), (117, 1.95), (139, 1.6)]


def yc(Y, k, x):
    return Y + k * interp(PITCH, x) + interp(GOFF, x)


def hw(x):
    return interp(HW, x)


def ylo(Y, k, x):          # dolny brzeg żebra k
    return yc(Y, k, x) + hw(x)


def yup(Y, k, x):          # górny brzeg żebra k
    return yc(Y, k, x) - hw(x)


def P(pts, close=True):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + (' Z' if close else '')


def xs(a, b, n=24):
    return [a + (b - a) * i / n for i in range(n + 1)]


def space(Y, k, a, b, inset=0.0):
    """wielokąt przestrzeni międzyżebrowej między żebrem k i k+1, od x=a do x=b"""
    top = [(x, ylo(Y, k, x) - 0.15) for x in xs(a, b)]
    bot = [(x, yup(Y, k + 1, x) + 0.15) for x in xs(a, b)][::-1]
    return top + bot


def fibres(Y, k, a, b, dx, step=1.15, out=None):
    """włókna: od dolnego brzegu żebra k do górnego brzegu żebra k+1, przesunięte o dx (dx<0 – ku przodowi)"""
    res = []
    x = a - abs(dx) - step
    while x < b + abs(dx) + step:
        x0, x1 = x, x + dx
        # przycięcie do [a, b] wzdłuż odcinka
        p0 = (x0, ylo(Y, k, x0) + 0.15)
        p1 = (x1, yup(Y, k + 1, x1) - 0.15)
        t0, t1 = 0.0, 1.0
        for lim, sgn in ((a, 1), (b, -1)):
            d0 = sgn * (p0[0] - lim)
            d1 = sgn * (p1[0] - lim)
            if d0 < 0 and d1 < 0:
                t0, t1 = 1, 0
                break
            if d0 < 0:
                t0 = max(t0, d0 / (d0 - d1))
            elif d1 < 0:
                t1 = min(t1, d0 / (d0 - d1))
        if t1 - t0 > 0.05:
            q0 = (p0[0] + (p1[0] - p0[0]) * t0, p0[1] + (p1[1] - p0[1]) * t0)
            q1 = (p0[0] + (p1[0] - p0[0]) * t1, p0[1] + (p1[1] - p0[1]) * t1)
            res.append(f'M{q0[0]:.2f},{q0[1]:.2f} L{q1[0]:.2f},{q1[1]:.2f}')
        x += step
    return ' '.join(res)


def sheet(Y, k, a, b, cls, dx, fcls, step=1.15):
    f.add(f'<path class="{cls}" d="{P(space(Y, k, a, b))}"/>')
    d = fibres(Y, k, a, b, dx, step)
    if d:
        f.add(f'<path class="{fcls}" d="{d}"/>')


def rib(Y, k, x_end, cap=True):
    """żebro k: chrząstka (XS1→XCC) i kość żebrowa (XCC→x_end)"""
    top = [(x, yup(Y, k, x)) for x in xs(XS1 - 0.6, XCC + 0.4, 12)]
    bot = [(x, ylo(Y, k, x)) for x in xs(XS1 - 0.6, XCC + 0.4, 12)][::-1]
    f.add(f'<path class="cart" d="{P(top + bot)}"/>')
    top = [(x, yup(Y, k, x)) for x in xs(XCC, x_end, 30)]
    bot = [(x, ylo(Y, k, x)) for x in xs(XCC, x_end, 30)][::-1]
    capp = []
    if cap:
        c = (x_end, yc(Y, k, x_end))
        r = hw(x_end)
        capp = [(c[0] + r * 0.8 * math.sin(math.pi * j / 10), c[1] - r * math.cos(math.pi * j / 10)) for j in range(1, 10)]
    f.add(f'<path class="bone" d="{P(top + capp + bot)}"/>')
    # brzeg chrzęstno-kostny
    f.add(f'<path class="bonel" d="M{XCC:.2f},{yup(Y, k, XCC) + 0.1:.2f} L{XCC:.2f},{ylo(Y, k, XCC) - 0.1:.2f}"/>')


def sternum(Y0, Y1):
    f.add(f'<path class="bone" d="M{XS0:.2f},{Y0:.2f} L{XS1:.2f},{Y0:.2f} L{XS1:.2f},{Y1:.2f} L{XS0:.2f},{Y1:.2f} Z"/>')


def clip_begin(cid, x0, y0, x1, y1):
    f.add(f'<defs><clipPath id="{cid}"><rect x="{x0:.2f}" y="{y0:.2f}" width="{x1 - x0:.2f}" height="{y1 - y0:.2f}" rx="1.4"/>'
          f'</clipPath></defs><g clip-path="url(#{cid})">')


def clip_end(x0, y0, x1, y1):
    f.add('</g>')
    f.add(f'<rect class="dim" x="{x0:.2f}" y="{y0:.2f}" width="{x1 - x0:.2f}" height="{y1 - y0:.2f}" rx="1.4"/>')


KS = (-1, 0, 1, 2)          # przestrzenie: -1 i 2 – częściowo widoczne (przycięte)

# =============================================================== 1. WIDOK OD ZEWNĄTRZ (lewa ściana, przód w lewo)
YT = 23.0
T_Y0, T_Y1 = 17.4, 48.6
clip_begin('cp_mz1', XS0, T_Y0, XV1, T_Y1)
for k in KS:
    # błona międzyżebrowa zewnętrzna (mostek → granica chrzęstno-kostna); włókna ku dołowi i do przodu (dx<0)
    sheet(YT, k, XS1, XCC, 'lig', -3.6, 'lig')
    if k == 0:
        # okno: usunięty m. zewnętrzny → widać m. międzyżebrowy wewnętrzny (włókna ku dołowi i ku tyłowi)
        sheet(YT, k, XCC, XTUB, 'muscle', 3.6, 'musclel')
        a, b = XWIN
        sheet(YT, k, XCC, a, 'muscle', -3.6, 'musclel')
        sheet(YT, k, b, XTUB, 'muscle', -3.6, 'musclel')
        # cień przy brzegach cięcia (grubość warstwy zewnętrznej)
        for xa, xb in ((a, a + 1.1), (b - 1.1, b)):
            f.add(f'<path class="shade" d="{P(space(YT, k, xa, xb))}"/>')
        for xx in (a, b):
            f.add(f'<path class="musclel" d="M{xx:.2f},{ylo(YT, k, xx):.2f} L{xx:.2f},{yup(YT, k + 1, xx):.2f}"/>')
    else:
        sheet(YT, k, XCC, XTUB, 'muscle', -3.6, 'musclel')
    # do przodu od guzka (między guzkiem a kręgosłupem): błona międzyżebrowa wewnętrzna (głębiej)
    sheet(YT, k, XTUB, XV0 + 0.5, 'lig', 3.0, 'lig')
for k in (-1, 0, 1, 2, 3):
    rib(YT, k, XTUB + 1.6)
    f.add(f'<path class="bonel" d="M{XANG + 0.7:.2f},{yup(YT, k, XANG + 0.7) + 0.35:.2f} L{XANG - 0.7:.2f},{ylo(YT, k, XANG - 0.7) - 0.35:.2f}"/>')
sternum(T_Y0, T_Y1)
# kręgosłup: wyrostki poprzeczne (na nich guzki żeber) i łuki kręgów
f.add(f'<path class="bone" d="M{XV0:.2f},{T_Y0:.2f} L{XV1 + 2:.2f},{T_Y0:.2f} L{XV1 + 2:.2f},{T_Y1:.2f} L{XV0:.2f},{T_Y1:.2f} Z"/>')
for k in (-1, 0, 1, 2, 3):
    yv = yc(YT, k, XV0) + 4.9
    f.add(f'<path class="bonel" d="M{XV0 + 0.4:.2f},{yv:.2f} L{XV1 + 2:.2f},{yv + 0.4:.2f}"/>')
TP = {}
for k in (-1, 0, 1, 2, 3):
    y0 = yc(YT, k, XTUB) - 0.3
    pts = [(XTUB - 0.6, y0), (XTUB + 0.2, y0 - 1.7), (XV0 + 1.5, y0 - 1.9), (XV0 + 1.8, y0 + 1.8), (XTUB + 0.2, y0 + 1.7)]
    TP[k] = (XTUB, y0)
    f.add(f'<path class="bone" d="M{pts[0][0]:.2f},{pts[0][1]:.2f} Q{pts[1][0] - 0.8:.2f},{pts[1][1]:.2f} {pts[1][0]:.2f},{pts[1][1]:.2f} '
          f'L{pts[2][0]:.2f},{pts[2][1]:.2f} L{pts[3][0]:.2f},{pts[3][1]:.2f} L{pts[4][0]:.2f},{pts[4][1]:.2f} '
          f'Q{pts[4][0] - 0.8:.2f},{pts[4][1]:.2f} {pts[0][0]:.2f},{pts[0][1]:.2f} Z"/>')
# mm. dźwigacze żeber: wyrostek poprzeczny (poziom żebra k) → żebro k+1 bocznie od guzka; włókna ku bokowi i ku dołowi
LEV = {}
for k in (-1, 0, 1, 2):
    ox, oy = XTUB + 3.2, yc(YT, k, XTUB) + 1.6
    i0, i1 = 104.5, XTUB - 1.0
    ins = [(x, yup(YT, k + 1, x) + 0.9) for x in xs(i0, i1, 10)]
    shape = [(ox - 0.6, oy - 0.3), (ox + 1.0, oy + 0.2)] + ins[::-1]
    f.add(f'<path class="muscle" d="{P(shape)}"/>')
    d = ' '.join(f'M{ox + 0.2:.2f},{oy:.2f} L{x:.2f},{y - 0.2:.2f}' for x, y in ins[1::2])
    f.add(f'<path class="musclel" d="{d}"/>')
    LEV[k] = (ox, oy, ins)
clip_end(XS0, T_Y0, XV1, T_Y1)

# strzałki kierunku włókien
def fib_arrow(Y, k, x, dx, red=False, m=0.22):
    p0 = (x, ylo(Y, k, x))
    p1 = (x + dx, yup(Y, k + 1, x + dx))
    a = (p0[0] + (p1[0] - p0[0]) * m, p0[1] + (p1[1] - p0[1]) * m)
    b = (p0[0] + (p1[0] - p0[0]) * (1 - m), p0[1] + (p1[1] - p0[1]) * (1 - m))
    f.arrow(f'M{a[0]:.2f},{a[1]:.2f} L{b[0]:.2f},{b[1]:.2f}', red=red)


fib_arrow(YT, 1, 84.0, -5.5)                 # zewnętrzne: ku dołowi i do przodu
fib_arrow(YT, 0, 78.0, 5.5, red=True)        # wewnętrzne (w oknie): ku dołowi i ku tyłowi

# =============================================================== 2. PASEK „CO WYPEŁNIA PRZESTRZEŃ”
GY = 52.3                                    # wiersz punktów orientacyjnych
for x, t in ((16.5, 'mostek'), (XCC, 'granica chrzęstno-kostna'), (XANG, 'kąt żebra'), (XTUB, 'guzek żebra'),
             ((XV0 + XV1) / 2, 'kręgosłup')):
    f.text(x, GY, t, cls='notec')
BY = [54.6, 58.9, 63.2]                      # wiersze pasków
BH = 3.4
B_Y0, B_Y1 = 76.0 - 5.6, 0
for x in (XS1, XCC, XANG, XTUB, XV0):
    f.add(f'<path class="dim" d="M{x:.2f},{GY + 0.9:.2f} L{x:.2f},{BY[-1] + BH + 1.0:.2f}"/>')


def bar(row, a, b, cls, txt=None, tcls='note'):
    y = BY[row]
    f.add(f'<rect class="{cls}" x="{a:.2f}" y="{y:.2f}" width="{b - a:.2f}" height="{BH:.2f}" rx=".6"/>')
    if txt:
        f.text((a + b) / 2, y + BH / 2 + 0.75, txt, cls='notec')


bar(0, XS1, XCC, 'lig', 'błona')
bar(0, XCC, XTUB, 'muscle', 'mm. międzyżebrowe zewnętrzne')
bar(1, XS1, XANG, 'muscle', 'mm. międzyżebrowe wewnętrzne – warstwa zewnętrzna (pośrednie)')
bar(1, XANG, XV0, 'lig', 'błona')
bar(2, XCC, XI1, 'muscle', 'warstwa wewnętrzna (najgłębsze)')
f.text(XV0 + 1.6, BY[0] + BH / 2 + 0.75, 'najbardziej', cls='note')
f.text(XV0 + 1.6, BY[0] + BH / 2 + 3.2, 'zewnętrznie', cls='note')
f.text(XV0 + 1.6, BY[2] + BH / 2 + 0.75, 'najgłębiej', cls='note')

# =============================================================== 3. WIDOK OD WEWNĄTRZ (prawa ściana, przód w lewo)
YB = 76.0
B_Y0, B_Y1 = 70.4, 101.6
clip_begin('cp_mz2', XS0, B_Y0, XV1, B_Y1)
for k in KS:
    # warstwa zewnętrzna mm. wewnętrznych (pośrednie): mostek → kąt żebra; włókna ku dołowi i ku tyłowi (dx>0)
    sheet(YB, k, XS1, XANG + 0.3, 'muscle', 3.6, 'musclel')
    # błona międzyżebrowa wewnętrzna: kąt → kręgosłup
    sheet(YB, k, XANG, XV0 + 0.5, 'lig', 3.6, 'lig')
    if k != 0:
        # warstwa wewnętrzna (najgłębsze): od okolicy kąta do granicy chrzęstno-kostnej
        f.add(f'<path class="shade" d="{P(space(YB, k, XCC - 0.9, XI1 + 0.9))}"/>')
        sheet(YB, k, XCC, XI1, 'muscle', 3.6, 'musclel', step=0.85)
    else:
        # przestrzeń 0: warstwa najgłębsza usunięta – zostawione kikuty przy obu końcach
        for xa, xb in ((XCC, XCC + 2.2), (XI1 - 2.2, XI1)):
            f.add(f'<path class="shade" d="{P(space(YB, k, xa - 0.8, xb + 0.8))}"/>')
            sheet(YB, k, xa, xb, 'muscle', 3.6, 'musclel', step=0.85)
for k in (-1, 0, 1, 2, 3):
    rib(YB, k, XV0 + 1.0)
sternum(B_Y0, B_Y1)
# trzony kręgów (od strony jamy klatki piersiowej) z krążkami
f.add(f'<path class="bone" d="M{XV0:.2f},{B_Y0:.2f} L{XV1 + 2:.2f},{B_Y0:.2f} L{XV1 + 2:.2f},{B_Y1:.2f} L{XV0:.2f},{B_Y1:.2f} Z"/>')
for k in (-1, 0, 1, 2, 3):
    yv = yc(YB, k, XV0) + 5.0
    f.add(f'<path class="annulus" d="M{XV0:.2f},{yv - 0.8:.2f} L{XV1 + 2:.2f},{yv - 0.6:.2f} L{XV1 + 2:.2f},{yv + 0.9:.2f} '
          f'L{XV0:.2f},{yv + 0.7:.2f} Z"/>')
    # głowa żebra przy trzonie
    c = (XV0 + 0.6, yc(YB, k, XV0) - 0.2)
    f.add(f'<ellipse class="facet" cx="{c[0]:.2f}" cy="{c[1]:.2f}" rx=".9" ry="1.5"/>')
# naczynia i nerw międzyżebrowy w przestrzeni 0 (warstwa najgłębsza usunięta): od góry ż., t., n.
VAN = []
for cls, dy, w in (('vein', -0.2, 0.7), ('artery', 0.6, 0.5), ('nerve', 1.35, 0.5)):
    pts = [(x, ylo(YB, 0, x) + dy) for x in xs(XS1 - 0.5, XV0 + 0.5, 40)]
    up = [(x, y - w / 2) for x, y in pts]
    dn = [(x, y + w / 2) for x, y in pts][::-1]
    f.add(f'<path class="{cls}" d="{P(up + dn)}"/>')
    VAN.append(pts)
# mm. podżebrowe: powierzchnia wewnętrzna żebra 0 w okolicy kąta → mijają żebro 1 → brzeg górny żebra 2
SUB_O = [(x, ylo(YB, 0, x) - 1.2) for x in xs(91.0, 104.0, 8)]
SUB_I = [(x, yup(YB, 2, x) + 0.6) for x in xs(97.5, 113.0, 8)]
f.add(f'<path class="muscle" d="{P(SUB_O + SUB_I[::-1])}"/>')
d = ' '.join(f'M{a[0]:.2f},{a[1]:.2f} L{b[0]:.2f},{b[1]:.2f}' for a, b in zip(SUB_O, SUB_I))
f.add(f'<path class="musclel" d="{d}"/>')
clip_end(XS0, B_Y0, XV1, B_Y1)
fib_arrow(YB, 1, 33.0, 5.0, red=True, m=0.2)          # wewnętrzne: ku dołowi i ku tyłowi

# =============================================================== nagłówki (pionowo, z lewej)
for (y0, y1), t in (((T_Y0, T_Y1), 'OD ZEWNĄTRZ'), ((B_Y0, B_Y1), 'OD WEWNĄTRZ')):
    ym = (y0 + y1) / 2
    f.add(f'<text class="big" text-anchor="middle" transform="translate(6.6,{ym:.2f}) rotate(-90)">{t}</text>')

# =============================================================== podpisy
# widok od zewnątrz – nad rysunkiem
f.label((27.0, (ylo(YT, 0, 27) + yup(YT, 1, 27)) / 2), 'błony międzyżebrowe zewnętrzne', 'membranae intercostales externae',
        (24.0, 4.5), side='R')
f.label((70.0, (ylo(YT, 0, 70) + yup(YT, 1, 70)) / 2), 'mm. międzyżebrowe wewnętrzne', 'mm. intercostales interni',
        (68.4, 11.4), side='L')
f.label((96.0, (ylo(YT, 0, 96) + yup(YT, 1, 96)) / 2 + 0.6), 'mm. międzyżebrowe zewnętrzne', 'mm. intercostales externi',
        (98.0, 4.5), side='R')
lx, ly = 114.0, yup(YT, 1, 114.0) - 0.9
f.label((lx, ly), 'mm. dźwigacze żeber', 'mm. levatores costarum', (123.0, 11.4), side='R')
# widok od wewnątrz – pod rysunkiem
f.label((30.0, (ylo(YB, 1, 30) + yup(YB, 2, 30)) / 2 + 1.2), 'mm. międzyżebrowe pośrednie', 'mm. intercostales intermedii',
        (14.0, 105.4), side='R')
f.label((55.0, VAN[2][int((55.0 - XS1 + 0.5) / (XV0 - XS1 + 1.0) * 40)][1]), 'n. międzyżebrowy', 'n. intercostalis',
        (58.0, 112.2), side='R')
f.label((70.0, (ylo(YB, 1, 70) + yup(YB, 2, 70)) / 2), 'mm. międzyżebrowe najgłębsze', 'mm. intercostales intimi',
        (64.0, 105.4), side='R')
f.label((106.0, yup(YB, 2, 106.0) - 2.2), 'mm. podżebrowe', 'mm. subcostales', (108.4, 112.2), side='R')
f.label((123.5, (ylo(YB, 1, 123.5) + yup(YB, 2, 123.5)) / 2), 'błony międzyżebrowe wewnętrzne', 'membranae intercostales internae',
        (112.0, 105.4), side='R')

f.save()
print('ok')
