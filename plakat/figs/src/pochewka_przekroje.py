# POCHEWKA M. PROSTEGO BRZUCHA – dwa przekroje poprzeczne przez przednią ścianę brzucha (schemat własny wg opisu
# Bochenka s. 717–721; ryc. 465–466 tylko do orientacji w kolejności warstw). Przód (skóra) ku górze rysunku.
#   A – powyżej kresy łukowatej: blaszka przednia = rozcięgno m. skośnego zewn. + blaszka przednia rozcięgna m. skośnego
#       wewn. (2 warstwy zrośnięte); blaszka tylna = blaszka tylna rozcięgna m. skośnego wewn. + rozcięgno m. poprzecznego.
#   B – poniżej kresy łukowatej: blaszka przednia = rozcięgna obu mm. skośnych i m. poprzecznego (3 warstwy);
#       blaszki tylnej brak – tylna powierzchnia m. prostego przylega bezpośrednio do powięzi poprzecznej.
# Kresa biała: skrzyżowanie włókien ścięgnistych strony prawej i lewej (w A blaszka przednia przechodzi w tylną strony
# przeciwnej – „X”). Rozcięgno m. skośnego wewnętrznego wyróżnione klasą lig, pozostałe rozcięgna – tendon.
# Układ: wspólna geometria „pasa” ściany: punkt = krzywa odniesienia R(u) + d·normalna (d – głębokość od przodu).
import sys, math, random; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig

W, H = 86, 96
f = Fig('pochewka_przekroje', W, H,
        caption='przekroje poprzeczne przedniej ściany brzucha · przód ku górze')


def ss(e0, e1, x):
    t = (x - e0) / (e1 - e0)
    t = 0.0 if t < 0 else (1.0 if t > 1 else t)
    return t * t * (3 - 2 * t)


def lerp(a, b, t):
    return a + (b - a) * t


def frange(a, b, step=0.25):
    n = max(2, int(abs(b - a) / step) + 1)
    return [a + (b - a) * i / (n - 1) for i in range(n)]


# grubości warstw (mm na rysunku)
SKIN, FAT, SLIT, FSUP = 0.9, 3.0, 0.6, 0.25     # skóra, tkanka podskórna, szczelina, odstęp powięzi powierzchownej od mięśnia
D_TIP = 3.3                                      # głębokość kąta bocznego pochewki (rozdwojenie rozcięgna m. sk. wewn.)
EO_L, IO_L, TA_L = (0.0, 2.0), (2.2, 4.4), (4.6, 6.4)   # mięśnie szerokie bocznie (głębokość od – do)
BL = TA_L[1]                                     # tylna powierzchnia ściany bocznie


class Sec:
    def __init__(s, kind, oy, cx=43.0, ya=19.0, a=0.0042, b=3.4e-6, U=37.0,
                 m0=1.8, m1=16.0, RT=2.0, RB=2.0, bulge=0.7, bulge_b=0.9, ta=0.45, dext=None):
        s.kind, s.oy, s.cx, s.ya, s.a, s.b, s.U = kind, oy, cx, ya, a, b, U
        s.m0, s.m1, s.RT, s.RB, s.bulge, s.bulge_b, s.ta = m0, m1, RT, RB, bulge, bulge_b, ta
        s.dext = dext

    # --- krzywa odniesienia i odwzorowanie (u, d) -> (x, y)
    def Y(s, u):
        return s.ya + s.a * u * u + s.b * u ** 4

    def dY(s, u):
        return 2 * s.a * u + 4 * s.b * u ** 3

    def P(s, u, d):
        k = s.dY(u); N = math.hypot(1.0, k)
        return (s.cx + u - d * k / N, s.oy + s.Y(u) + d / N)

    # --- profile głębokości
    def bump(s, u):
        v = (abs(u) - s.m0) / (s.m1 - s.m0)
        return math.sin(math.pi * v ** 0.8) ** 1.1 if 0 < v < 1 else 0.0

    def fb(s, u):            # przednia powierzchnia warstwy mięśniowo-rozcięgnowej (bruzda pośrodkowa między mm. prostymi)
        return -s.bulge * s.bump(u) * ss(s.m0 - 0.3, s.m0 + 2.5, abs(u))

    def bb(s, u):            # tylna powierzchnia ściany (A: rozcięgno m. poprzecznego; B: m. prosty)
        au = math.sqrt(u * u + 0.6)
        v = (au + s.m0) / (s.m1 + s.m0)
        hb = math.sin(math.pi * v ** 0.8) ** 1.1 if v < 1 else 0.0
        return BL + s.bulge_b * hb

    def conv(s, u, L=8.0, p=2.2):
        t = (abs(u) - (s.m1 - L)) / L
        return 0.0 if t <= 0 else (1.0 if t >= 1 else t ** p)

    def Lf(s, u):            # wewnętrzna powierzchnia blaszki przedniej (granica z m. prostym)
        if s.kind == 'A':
            return lerp(s.fb(u) + 2 * s.ta, D_TIP, s.conv(u))
        return s.fb(u) + 3 * s.ta

    def Lb(s, u):            # wewnętrzna powierzchnia blaszki tylnej (A) / tylna powierzchnia m. prostego (B)
        if s.kind == 'A':
            return lerp(s.bb(u) - 2 * s.ta, D_TIP, s.conv(u))
        return lerp(s.bb(u), s.fb(u) + 3 * s.ta + 0.3, s.conv(u))

    # --- rysowanie
    def poly(s, pts_ud):
        return 'M' + ' L'.join('%.2f,%.2f' % s.P(u, d) for u, d in pts_ud) + ' Z'

    def line(s, pts_ud):
        return 'M' + ' L'.join('%.2f,%.2f' % s.P(u, d) for u, d in pts_ud)

    def band(s, u0, u1, top, bot, cls, step=0.25):
        us = frange(u0, u1, step)
        pts = [(u, top(u)) for u in us] + [(u, bot(u)) for u in reversed(us)]
        f.add(f'<path class="{cls}" d="{s.poly(pts)}"/>')

    def muscle(s, j, top, bot, side, taper=2.6):
        """brzusiec mięśnia szerokiego od u=j (koniec przyśrodkowy, zaostrzony) do cięcia u=U"""
        sg = 1 if side > 0 else -1
        us = frange(j, s.U, 0.25)

        def w(u):
            return math.sqrt(ss(j, j + taper, u))
        T = [(sg * u, (top(sg * u) + bot(sg * u)) / 2 - (bot(sg * u) - top(sg * u)) / 2 * w(u)) for u in us]
        B = [(sg * u, (top(sg * u) + bot(sg * u)) / 2 + (bot(sg * u) - top(sg * u)) / 2 * w(u)) for u in us]
        f.add(f'<path class="muscle" d="{s.poly(T + B[::-1])}"/>')

    def sheath(s, u):
        """granice przestrzeni zajętej przez m. prosty (u >= 0)"""
        if s.kind == 'A':
            return s.Lf(u), s.Lb(u)
        sf = ss(s.m1 - 1, s.m1 + 6, u)
        return lerp(s.fb(u) + 3 * s.ta, TA_L[1], sf), s.bb(u)

    def rect_profile(s, u):
        """górna i dolna granica m. prostego (u >= 0) z zaokrąglonym końcem przyśrodkowym (i bocznym w B)"""
        t0, b0 = s.sheath(u)
        top, bot = t0 + 0.12, b0 - 0.12
        if s.kind == 'B':
            ue, RL = s.m1 + 1.0, 3.6
            te, be = s.sheath(ue)
            de = (te + be) / 2
            x = (u - (ue - RL)) / RL
            if x > 0:
                k = 1 - math.sqrt(max(0.0, 1 - min(1.0, x) ** 2))
                top += (de - top) * k
                bot -= (bot - de) * k
        de = s.dext if s.dext is not None else (s.Lf(s.m0) + s.Lb(s.m0)) / 2
        x = u - s.m0
        if x < s.RT:
            top += (de - t0) * (1 - math.sqrt(max(0.0, 1 - (1 - x / s.RT) ** 2)))
        if x < s.RB:
            bot -= (b0 - de) * (1 - math.sqrt(max(0.0, 1 - (1 - x / s.RB) ** 2)))
        return top, bot

    def rectus(s, side):
        sg = 1 if side > 0 else -1
        us = frange(s.m0, s.m1 + (1.0 if s.kind == 'B' else 0.0), 0.12)
        T, B = [], []
        for u in us:
            t, b = s.rect_profile(u)
            if b - t < 0.08 and u > s.m1 - 3:
                break
            T.append((sg * u, t)); B.append((sg * u, b))
        # koniec boczny – ostry kąt
        tip = (sg * (abs(T[-1][0]) + 0.25), (T[-1][1] + B[-1][1]) / 2)
        f.add(f'<path class="muscle" d="{s.poly(T + [tip] + B[::-1])}"/>')
        return T, B

    def knot(s):
        """kresa biała – pole ścięgniste między końcami przyśrodkowymi mm. prostych"""
        up = s.m0 + max(s.RT, s.RB)
        R, L = [], []
        for u in frange(s.m0, up, 0.1):
            t, b = s.rect_profile(u)
            R.append((u, t, b))
        top_edge = s.fb(0) + (0.2 if s.kind == 'A' else 3 * s.ta - 0.2)
        right = [(u, t) for u, t, b in reversed(R)] + [(u, b) for u, t, b in R]
        bot = s.bb(0) - (0.2 if s.kind == 'A' else 0.0)
        pts = [(-up, top_edge), (up, top_edge)] + [(u, max(d, top_edge)) for u, d in right]
        pts += [(up, bot), (-up, bot)] + [(-u, max(d, top_edge)) for u, d in reversed(right)]
        f.add(f'<path class="tendon" d="{s.poly(pts)}"/>')


def superficial(S):
    U = S.U
    sk_in = lambda u: S.fb(u) - FSUP - SLIT - FAT
    S.band(-U, U, lambda u: sk_in(u) - SKIN, sk_in, 'organ')                      # skóra
    S.band(-U, U, sk_in, lambda u: S.fb(u) - FSUP - SLIT, 'shade')               # tkanka podskórna
    rnd = random.Random(7 if S.kind == 'A' else 11)
    for row, dd in enumerate((0.95, 2.05)):                                       # zraziki tłuszczu (2 rzędy)
        u = -U + 1.2 + (1.05 if row % 2 else 0.0)
        while u < U - 0.9:
            d0 = sk_in(u) + dd + (rnd.random() - 0.5) * 0.3
            x, y = S.P(u, d0)
            ang = math.degrees(math.atan(S.dY(u))) + (rnd.random() - 0.5) * 16
            rx = 0.62 + rnd.random() * 0.16
            ry = 0.38 + rnd.random() * 0.08
            f.add(f'<ellipse class="cavity" cx="{x:.2f}" cy="{y:.2f}" rx="{rx:.2f}" ry="{ry:.2f}" '
                  f'transform="rotate({ang:.1f} {x:.2f} {y:.2f})"/>')
            u += 2.1 + (rnd.random() - 0.5) * 0.5
    us = frange(-U, U, 0.3)
    f.add(f'<path class="capsule" d="{S.line([(u, S.fb(u) - FSUP - SLIT) for u in us])}"/>')   # powięź podskórna
    f.add(f'<path class="capsule" d="{S.line([(u, S.fb(u) - FSUP) for u in us])}"/>')          # powięź powierzchowna


def deep(S):
    U, ta = S.U, S.ta
    us = frange(-U, U, 0.3)
    ft = 0.3 if S.kind == 'A' else 0.15
    S.band(-U, U, lambda u: S.bb(u) + ft + 0.6, lambda u: S.bb(u) + ft + 1.05, 'organ')      # otrzewna
    f.add(f'<path class="capsule" d="{S.line([(u, S.bb(u) + ft) for u in us])}"/>')         # powięź poprzeczna


def section_A(S):
    U, ta, m0, m1 = S.U, S.ta, S.m0, S.m1
    superficial(S)
    deep(S)
    S.knot()
    # m. poprzeczny: rozcięgno za m. prostym (ciągłe przez linię pośrodkową) + brzuśce
    ta_top = lambda u: lerp(S.bb(u) - ta, TA_L[0], ss(m1, m1 + 6, abs(u)))
    S.band(-U, U, ta_top, S.bb, 'tendon')
    for sd in (-1, 1):
        S.muscle(m1 + 2.0, ta_top, S.bb, sd)
    # m. skośny wewnętrzny: część boczna (rozcięgno do kąta pochewki) + brzusiec
    io_top = lambda u: lerp(D_TIP - ta, IO_L[0], ss(m1, m1 + 6, abs(u)))
    io_bot = lambda u: lerp(D_TIP + ta, IO_L[1], ss(m1, m1 + 6, abs(u)))
    for sd in (-1, 1):
        if sd > 0:
            S.band(m1 - 0.05, U, io_top, io_bot, 'lig')
        else:
            S.band(-U, -m1 + 0.05, io_top, io_bot, 'lig')
    # blaszki rozcięgna m. sk. wewnętrznego: przednia strony jednej -> (skrzyżowanie w kresie białej) -> tylna strony drugiej
    for sd in (1, -1):
        us = frange(m1, -m1, 0.15) if sd > 0 else frange(-m1, m1, 0.15)

        def cen(u, sd=sd):
            sig = ss(sd * (m0 + 0.7), -sd * (m0 + 0.7), u)   # 0 po stronie początkowej, 1 po przeciwnej
            return lerp(S.Lf(u) - ta / 2, S.Lb(u) + ta / 2, sig)
        T, B = [], []
        for i, u in enumerate(us):
            u0 = us[max(0, i - 1)]; u1 = us[min(len(us) - 1, i + 1)]
            sl = (cen(u1) - cen(u0)) / (u1 - u0)
            h = ta / 2 * math.sqrt(1 + sl * sl)
            T.append((u, cen(u) - h)); B.append((u, cen(u) + h))
        f.add(f'<path class="lig" d="{S.poly(T + B[::-1])}"/>')
    for sd in (-1, 1):
        S.muscle(m1 + 1.2, io_top, io_bot, sd)
    # m. skośny zewnętrzny: rozcięgno przed m. prostym (ciągłe) + brzuśce
    eo_bot = lambda u: lerp(S.fb(u) + ta, EO_L[1], ss(m1 - 1, m1 + 7, abs(u)))
    S.band(-U, U, S.fb, eo_bot, 'tendon')
    for sd in (-1, 1):
        S.muscle(m1 + 3.5, S.fb, eo_bot, sd)
    # mm. proste
    for sd in (-1, 1):
        S.rectus(sd)


def section_B(S):
    U, ta, m0, m1 = S.U, S.ta, S.m0, S.m1
    superficial(S)
    deep(S)
    S.knot()
    sf = lambda u: ss(m1 - 1, m1 + 6, abs(u))          # rozejście się rozcięgien ku mięśniom (bocznie od m. prostego)
    # m. poprzeczny: rozcięgno biegnie do przodu od m. prostego (najgłębsza warstwa blaszki przedniej)
    ta_top = lambda u: lerp(S.fb(u) + 2 * ta, TA_L[0], sf(u))
    ta_bot = lambda u: lerp(S.fb(u) + 3 * ta, TA_L[1], sf(u))
    S.band(-U, U, ta_top, ta_bot, 'tendon', step=0.15)
    for sd in (-1, 1):
        S.muscle(m1 + 4.5, ta_top, ta_bot, sd)
    # m. skośny wewnętrzny: całe rozcięgno do przodu od m. prostego
    io_top = lambda u: lerp(S.fb(u) + ta, IO_L[0], sf(u))
    io_bot = lambda u: lerp(S.fb(u) + 2 * ta, IO_L[1], sf(u))
    S.band(-U, U, io_top, io_bot, 'lig', step=0.15)
    for sd in (-1, 1):
        S.muscle(m1 + 3.5, io_top, io_bot, sd)
    # m. skośny zewnętrzny
    eo_bot = lambda u: lerp(S.fb(u) + ta, EO_L[1], ss(m1 - 1, m1 + 8, abs(u)))
    S.band(-U, U, S.fb, eo_bot, 'tendon')
    for sd in (-1, 1):
        S.muscle(m1 + 4.5, S.fb, eo_bot, sd)
    # kresa biała – skrzyżowanie włókien (cienkie linie)
    for sd in (-1, 1):
        a = S.P(sd * 2.2, S.fb(0) + 3 * ta - 0.05)
        b = S.P(-sd * 0.45, S.bb(0) - 0.5)
        f.add(f'<path class="tendon" d="M{a[0]:.2f},{a[1]:.2f} L{b[0]:.2f},{b[1]:.2f}"/>')
    for sd in (-1, 1):
        S.rectus(sd)


A = Sec('A', 0.0, ya=24.5, a=0.003, b=4e-6, U=36.0, m0=1.9, m1=19.0, RT=2.4, RB=2.4, bulge=0.9, bulge_b=1.1, ta=0.5)
B = Sec('B', 61.0, ya=14.5, a=0.003, b=4e-6, U=36.0, m0=0.8, m1=16.5, RT=2.8, RB=0.8, bulge=0.5, bulge_b=1.4, ta=0.45)
B.dext = B.bb(0) - 0.8
section_A(A)
section_B(B)

# ---------- tytuły przekrojów i liczby warstw pochewki ----------
f.text(2.0, 4.4, 'A · powyżej kresy łukowatej', cls='big')
f.text(83.7, 56.6, 'blaszka przednia: 2 warstwy', cls='note', anchor='end')
f.text(83.7, 59.2, 'blaszka tylna: 2 warstwy', cls='note', anchor='end')
f.text(2.0, B.oy + 4.4, 'B · poniżej kresy łukowatej', cls='big')
f.text(2.0, B.oy + 8.2, 'blaszka przednia: 3 warstwy', cls='note')
f.text(2.0, B.oy + 10.7, 'blaszka tylna: brak', cls='note')

# ---------- podpisy: A (warstwy wspólne + pochewka powyżej kresy łukowatej) ----------
P = A.P
# góra – lewa strona (warstwy powierzchowne)
f.label(P(-33.6, -FSUP), 'powięź powierzchowna brzucha', 'fascia superficialis abdominis', (4.6, 8.1), side='R')
f.label(P(-31.0, -FSUP - SLIT), 'powięź podskórna', 'fascia subcutanea', (8.0, 13.6), side='R')
# góra – prawa strona
f.label(P(5.3, A.fb(5.3) + A.ta), 'blaszka przednia', 'lamina anterior', (50.0, 2.6), side='R')
f.label(P(10.5, (A.Lf(10.5) + A.Lb(10.5)) / 2), 'm. prosty brzucha', 'm. rectus abdominis', (55.0, 8.1), side='R')
f.label(P(14.0, -FSUP - SLIT - FAT / 2), 'tkanka podskórna', 'tela subcutanea', (57.5, 13.6), side='R')
f.label(P(28.6, -FSUP - SLIT - FAT - SKIN / 2), 'skóra', 'cutis', (76.0, 19.1), side='R')
# dół – środek
f.label(P(0.0, A.bb(0) - 1.6), 'kresa biała', 'linea alba', (41.4, 38.8), side='L')
f.label(P(9.5, A.bb(9.5) - A.ta), 'blaszka tylna', 'lamina posterior', (53.5, 44.3), side='R')
f.label(P(13.0, A.bb(13.0) + 0.3 + 0.825), 'otrzewna', 'peritoneum', (55.0, 38.8), side='R')
# dół – lewy koniec przekroju (powierzchnia cięcia mięśni szerokich)
f.label(P(-35.5, (TA_L[0] + TA_L[1]) / 2), 'm. poprzeczny brzucha', 'm. transversus abdominis', (13.2, 44.3), side='R')
f.label(P(-35.5, (IO_L[0] + IO_L[1]) / 2), 'm. skośny wewnętrzny brzucha', 'm. obliquus internus abdominis', (8.1, 49.8), side='R')
f.label(P(-35.5, (EO_L[0] + EO_L[1]) / 2), 'm. skośny zewnętrzny brzucha', 'm. obliquus externus abdominis', (4.2, 55.3), side='R')

# ---------- podpisy: B (tylko różnice) ----------
P = B.P
f.label(P(5.0, B.fb(5.0) + 1.5 * B.ta), 'blaszka przednia', 'lamina anterior', (50.0, B.oy + 2.6), side='R')
f.label(P(-6.0, B.bb(-6.0) + 0.15), 'powięź poprzeczna', 'fascia transversalis', (38.5, B.oy + 27.5), side='R')

f.save()
