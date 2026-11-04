# MECHANIKA ŻEBRA KOSTNEGO – oś szyjki żebra (widok od góry, przód ku górze; prawe żebro po prawej stronie rysunku).
# Dwa panele: żebro górne (typ II–V) i żebro dolne (typ VI–X).
# Wg Bochenka, t. I, s. 293–294: oś ruchu żeber II–V = długa oś szyjki żebra, biegnąca przez oba stawy
# żebrowo-kręgowe (staw głowy żebra + staw żebrowo-poprzeczny); jej kierunek ku dołowi coraz bardziej skośny,
# odpowiednio do wyrostków poprzecznych (Th1 – prawie czołowo, niżej coraz silniej ku tyłowi) → czołowy kąt
# skrzyżowania: żebro I ok. 10°, żebro X ok. 45° (Felix). Żebra VI–X nie poruszają się wokół osi szyjki:
# guzek żebra wsuwa się na wyrostek poprzeczny ku górze i ku tyłowi.
# Kształt kręgu i żebra – uproszczony, własny (na podstawie pol_zebro_kreg_gora.py).
import sys, math, os
sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth, mirror

W, H = 150, 104
S = 0.62                     # mm rysunku / mm kości
f = Fig('zebro_os_ruchu', W, H, caption='kręg piersiowy z prawym żebrem · widok od góry (przód ku górze)')


# ---------------------------------------------------------------- narzędzia
def cr(pts, closed=True, n=12, t=0.5):
    """punkty na krzywej rysowanej przez smooth()"""
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


def poly(pts, close=True):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + (' Z' if close else '')


def unit(v):
    L = math.hypot(*v)
    return (v[0] / L, v[1] / L)


def add(a, b, k=1.0):
    return (a[0] + b[0] * k, a[1] + b[1] * k)


def resample(pts, step=0.25):
    out = [pts[0]]
    for p in pts[1:]:
        q = out[-1]
        d = math.dist(p, q)
        n = max(1, int(d / step))
        for k in range(1, n + 1):
            out.append((q[0] + (p[0] - q[0]) * k / n, q[1] + (p[1] - q[1]) * k / n))
    return out


# ---------------------------------------------------------------- kręg + żebro (współrzędne kości: x w prawo, y ku tyłowi)
BODY_R = [(0, 0), (5.2, 0.35), (9.6, 1.9), (12.7, 4.9), (14.1, 8.8), (14.2, 12.8), (13.5, 16.6), (11.9, 19.6), (8.6, 21.2),
          (4.2, 20.8)]
BODY = BODY_R + [(0, 20.1)] + mirror(BODY_R, 0)[:-1]
BODY_C = cr(BODY, closed=True, n=40)
LAMINA_R = [(11.6, 39.4), (8.0, 41.4), (4.6, 43.8), (2.8, 46.6), (2.2, 51.0), (2.1, 55.0), (2.6, 58.4), (1.7, 60.4), (0.0, 60.8)]
PEDICLE_R = [(0.0, 19.0), (7.5, 19.2), (11.0, 20.0), (12.3, 22.4)]
RT = (12.0, 27.0)            # środek nasady wyrostka poprzecznego
WT, WTIP = 2.9, 3.4          # półszerokość wyrostka poprzecznego i jego zgrubiałego końca


def body_point(alpha):
    """punkt na prawym brzegu trzonu, w którym normalna zewnętrzna ma kierunek alpha (stopnie, ku tyłowi > 0)"""
    best = None
    n = len(BODY_C)
    for i, p in enumerate(BODY_C):
        if p[0] <= 6 or p[1] < 9:
            continue
        a, b = BODY_C[i - 1], BODY_C[(i + 1) % n]
        tx, ty = b[0] - a[0], b[1] - a[1]
        nx, ny = ty, -tx                       # obieg zgodny z ruchem wskazówek (y w dół) → normalna na zewnątrz
        L = math.hypot(nx, ny)
        ang = math.degrees(math.atan2(ny / L, nx / L))
        err = abs(ang - alpha)
        if best is None or err < best[0]:
            best = (err, p, (nx / L, ny / L))
    return best[1], best[2]


def panel(CX, OY, alpha, neck, beta, axis_cls, phiF=-68.0, xcut=40.0):
    """Rysuje kręg z prawym żebrem. alpha – czołowy kąt skrzyżowania (°), neck – odległość środków stawów,
    beta – kierunek trzonu żebra za guzkiem. Zwraca słownik punktów (w mm rysunku)."""
    def P(x, y):
        return (CX + x * S, OY + y * S)

    def T(pts):
        return [P(x, y) for x, y in pts]

    Hj, nH = body_point(alpha)                 # środek stawu głowy żebra (na brzegu trzonu)
    d = (math.cos(math.radians(alpha)), math.sin(math.radians(alpha)))
    nd = (-d[1], d[0])                         # normalna ku tyłowi (strona guzka)
    Fj = add(Hj, d, neck)                      # środek stawu żebrowo-poprzecznego (guzek ↔ wyrostek poprzeczny)

    # wyrostek poprzeczny dobrany tak, by dołek żebrowy (przednia powierzchnia końca) wypadł w Fj
    v = (Fj[0] - RT[0], Fj[1] - RT[1])
    b = WTIP * math.sin(math.radians(phiF))
    a = math.sqrt(v[0] ** 2 + v[1] ** 2 - b * b)
    th = math.atan2(v[1], v[0]) - math.atan2(b, a)
    L = a - WTIP * math.cos(math.radians(phiF))
    u = (math.cos(th), math.sin(th)); n = (-u[1], u[0])
    C = add(RT, u, L)

    def tp(s, w):                               # punkt wyrostka: s – wzdłuż, w – w poprzek (+ ku tyłowi)
        return (RT[0] + u[0] * s + n[0] * w, RT[1] + u[1] * s + n[1] * w)
    tp_ant = [tp(0.30 * L, -WT * 1.02), tp(0.66 * L, -WT)]
    tip = []
    for ph in (-112, -72, -36, 0, 36, 72, 108):
        r = math.radians(ph)
        tip.append((C[0] + WTIP * (math.cos(r) * u[0] + math.sin(r) * n[0]), C[1] + WTIP * (math.cos(r) * u[1] + math.sin(r) * n[1])))
    tp_post = [tp(0.62 * L, WT * 1.02), tp(0.22 * L, WT * 1.25)]
    arch_R = PEDICLE_R + tp_ant + tip + tp_post + LAMINA_R
    arch = arch_R + mirror(arch_R, 0)[1:-1]
    f.add(f'<path class="bone" d="{smooth(T(arch))}"/>')
    # otwór kręgowy, wyrostki stawowe górne, grzebień wyrostka kolczystego
    hx, hy = P(0, 28.0)
    f.add(f'<ellipse class="hole" cx="{hx:.2f}" cy="{hy:.2f}" rx="{7.3 * S:.2f}" ry="{7.0 * S:.2f}"/>')
    for s_ in (-1, 1):
        x, y = P(s_ * 9.2, 31.6)
        f.add(f'<ellipse class="bone2" cx="{x:.2f}" cy="{y:.2f}" rx="{3.2 * S:.2f}" ry="{2.4 * S:.2f}" transform="rotate({s_ * 12} {x:.2f} {y:.2f})"/>')
        f.add(f'<ellipse class="facet" cx="{x + s_ * 0.15:.2f}" cy="{y + 0.55:.2f}" rx="{2.6 * S:.2f}" ry="{1.05 * S:.2f}" transform="rotate({s_ * 12} {x:.2f} {y:.2f})"/>')
    f.add(f'<path class="bonel" d="{poly(T([(0, 46.0), (0, 58.6)]), close=False)}"/>')
    # trzon
    f.add(f'<path class="bone" d="{smooth(T(BODY))}"/>')
    rim = [(x * 0.84, 1.6 + y * 0.84) for x, y in BODY]
    f.add(f'<path class="bonel" d="{smooth(T(rim))}"/>')

    # ---- żebro: linia środkowa + szerokości
    c0 = add(Hj, d, 2.7)                                   # środek głowy
    c1 = add(add(Hj, d, 0.5 * neck), nd, -0.35)            # szyjka
    WP_TUB = 2.6
    c2 = add(Fj, nd, -WP_TUB)                              # okolica guzka (Fj leży na tylnym brzegu)
    bd = (math.cos(math.radians(beta)), math.sin(math.radians(beta)))
    c3 = add(c2, unit(add(d, bd)), 5.0)
    c4 = add(c3, bd, 6.0)
    cl = [c0, c1, c2, c3, c4]
    while cl[-1][0] < xcut + 4:
        cl.append(add(cl[-1], bd, 5.0))
    cen = resample(cr(cl, closed=False, n=30), 0.2)
    # obcięcie na xcut
    cen = [p for p in cen if p[0] <= xcut]
    # półszerokości wzdłuż długości (s – od głowy)
    sl = [0.0]
    for i in range(1, len(cen)):
        sl.append(sl[-1] + math.dist(cen[i - 1], cen[i]))
    s_tub = min(range(len(cen)), key=lambda i: math.dist(cen[i], c2))
    s_tub = sl[s_tub]

    def interp(ctrl, s):
        if s <= ctrl[0][0]:
            return ctrl[0][1]
        for (s0, v0), (s1, v1) in zip(ctrl, ctrl[1:]):
            if s <= s1:
                q = (s - s0) / (s1 - s0)
                q = q * q * (3 - 2 * q)
                return v0 + (v1 - v0) * q
        return ctrl[-1][1]
    WA = [(0, 2.9), (2.2, 2.9), (4.6, 1.95), (s_tub - 3.0, 1.9), (s_tub, 2.3), (s_tub + 5, 3.0), (99, 3.1)]
    WPc = [(0, 2.9), (2.2, 2.9), (4.6, 1.95), (s_tub - 3.5, 1.9), (s_tub - 0.6, WP_TUB), (s_tub + 1.6, WP_TUB), (s_tub + 5.5, 3.1), (99, 3.1)]
    ant, post = [], []
    for i, p in enumerate(cen):
        a_ = cen[max(i - 1, 0)]; b_ = cen[min(i + 1, len(cen) - 1)]
        tx, ty = unit((b_[0] - a_[0], b_[1] - a_[1]))
        nn = (-ty, tx)                                      # normalna ku tyłowi (prawa strona marszu, y w dół)
        ant.append(add(p, nn, -interp(WA, sl[i])))
        post.append(add(p, nn, interp(WPc, sl[i])))
    # zaokrąglona głowa (półkole od tylnego do przedniego brzegu, przez koniec przyśrodkowy)
    t0 = unit((cen[1][0] - cen[0][0], cen[1][1] - cen[0][1]))
    n0 = (-t0[1], t0[0])
    r0 = 2.9
    cap = []
    for k in range(1, 18):
        ph = math.pi * k / 18
        cap.append((cen[0][0] + r0 * (n0[0] * math.cos(ph) - t0[0] * math.sin(ph)),
                    cen[0][1] + r0 * (n0[1] * math.cos(ph) - t0[1] * math.sin(ph))))
    outline = ant + post[::-1] + cap
    f.add(f'<path class="bone" d="{poly(T(outline))}"/>')
    # powierzchnia przekroju na końcu bocznym
    e0, e1 = ant[-1], post[-1]
    te = unit((cen[-1][0] - cen[-2][0], cen[-1][1] - cen[-2][1]))
    mid = ((e0[0] + e1[0]) / 2, (e0[1] + e1[1]) / 2)
    cut = [e0, add(e0, te, -0.9), add(mid, te, -1.15), add(e1, te, -0.9), e1, add(mid, te, 0.25)]
    f.add(f'<path class="bone2" d="{smooth(T(cut))}"/>')
    # brzeg górny (grzebień szyjki) – cienka linia
    k0 = int(len(cen) * 0.22)
    cr_line = [add(cen[i], unit((-(cen[min(i + 1, len(cen) - 1)][1] - cen[max(i - 1, 0)][1]),
                                 (cen[min(i + 1, len(cen) - 1)][0] - cen[max(i - 1, 0)][0]))), 0.35) for i in range(k0, len(cen) - 6, 3)]
    f.add(f'<path class="bonel" d="{poly(T(cr_line), close=False)}"/>')

    # ---- powierzchnie stawowe (szpary stawowe widziane od góry)
    seg = [p for p in BODY_C if p[0] > 4 and math.dist(p, Hj) <= 2.3]
    seg.sort(key=lambda p: p[1])
    inner = offset(seg, 0.45)
    outer_ = offset(seg, -0.75)
    f.add(f'<path class="facet" d="{poly(T(outer_ + inner[::-1]))}"/>')
    # dołek żebrowy wyrostka poprzecznego + powierzchnia guzka
    arc_pts = []
    for ph in range(-104, -30, 4):
        r = math.radians(ph)
        arc_pts.append((C[0] + WTIP * (math.cos(r) * u[0] + math.sin(r) * n[0]), C[1] + WTIP * (math.cos(r) * u[1] + math.sin(r) * n[1])))
    near = [p for p in arc_pts if math.dist(p, Fj) <= 2.6]
    near_in = [(C[0] + (p[0] - C[0]) * (1 - 0.5 / WTIP), C[1] + (p[1] - C[1]) * (1 - 0.5 / WTIP)) for p in near]
    near_out = [(C[0] + (p[0] - C[0]) * (1 + 0.55 / WTIP), C[1] + (p[1] - C[1]) * (1 + 0.55 / WTIP)) for p in near]
    f.add(f'<path class="facet" d="{poly(T(near_out + near_in[::-1]))}"/>')

    pts = dict(H=P(*Hj), F=P(*Fj), d=d, nd=nd, theta=math.degrees(th), L=L, tipC=P(*C), Hb=Hj, Fb=Fj,
               body=P(-7.0, 8.0), tpL=P(-(C[0] - 1.5), C[1] - u[1] * 1.5), tpR=P(C[0] - 1.0, C[1] + 0.5),
               tubB=post[min(range(len(cen)), key=lambda i: math.dist(cen[i], c2))], cut=P(*((e0[0] + e1[0]) / 2, (e0[1] + e1[1]) / 2)),
               ribpost=[P(*p) for p in post], ribant=[P(*p) for p in ant], P=P, neckmid=P(*c1))
    return pts


# ================================================================ PANEL A – żebra górne (II–V): obrót wokół osi szyjki
CX = 52.0
A = panel(CX, 9.0, alpha=21.0, neck=17.4, beta=0.0, axis_cls='axis')
# ================================================================ PANEL B – żebra dolne (VI–X): guzek wsuwa się na wyrostek
B = panel(CX, 58.5, alpha=45.0, neck=17.6, beta=16.0, axis_cls='dim', phiF=-62.0)


def along(Q, r):
    """punkt na osi szyjki w odległości r (mm kości) od środka stawu głowy"""
    return (Q['H'][0] + Q['d'][0] * r * S, Q['H'][1] + Q['d'][1] * r * S)


def arc(c, r, a0, a1, n=24):
    return [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * k / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * k / n)))
            for k in range(n + 1)]


# ---------------- A: oś obrotu (oś szyjki) + płaszczyzna czołowa + kąt
a0, a1 = along(A, -7), along(A, 74)
f.add(f'<path class="axis" d="M{a0[0]:.2f},{a0[1]:.2f} L{a1[0]:.2f},{a1[1]:.2f}"/>')
PA = along(A, 34)
f.add(f'<path class="dim" d="M{PA[0] - 7.0:.2f},{PA[1]:.2f} L{PA[0] + 12.5:.2f},{PA[1]:.2f}"/>')
angA = arc(PA, 5.5, 0, 21)
f.add(f'<path class="dim" style="stroke-dasharray:none" d="{poly(angA, close=False)}"/>')
# symbol obrotu wokół osi (strzałka dwukierunkowa: wdech / wydech)
Cs = along(A, 68)
dd = A['d']; mm_ = (-dd[1], dd[0])
ea, eb = 3.0, 1.25


def ell(t):
    t = math.radians(t)
    return (Cs[0] + ea * math.cos(t) * mm_[0] + eb * math.sin(t) * dd[0], Cs[1] + ea * math.cos(t) * mm_[1] + eb * math.sin(t) * dd[1])


for t0, t1 in ((90, -62), (90, 242)):
    pts_ = [ell(t0 + (t1 - t0) * k / 30) for k in range(31)]
    f.arrow(poly(pts_, close=False))

# ---------------- B: oś szyjki (tylko kierunek szyjki – ruch żeber VI–X nie odbywa się wokół niej) + kąt przy głowie
b0, b1 = along(B, -6), along(B, 17.6)
f.add(f'<path class="dim" d="M{b0[0]:.2f},{b0[1]:.2f} L{b1[0]:.2f},{b1[1]:.2f}"/>')
HB = B['H']
f.add(f'<path class="dim" d="M{HB[0]:.2f},{HB[1]:.2f} L{HB[0] + 15.5:.2f},{HB[1]:.2f}"/>')
angB = arc(HB, 7.0, 0, 45)
f.add(f'<path class="dim" style="stroke-dasharray:none" d="{poly(angB, close=False)}"/>')
# strzałka: guzek wsuwa się na wyrostek poprzeczny ku tyłowi (i ku górze)
FB = B['F']
xa = FB[0] + 1.25
f.arrow(f'M{xa:.2f},{FB[1] - 2.6:.2f} L{xa:.2f},{FB[1] + 3.6:.2f}')

# ---------------- tytuły paneli
f.text(3.0, 6.2, 'żebra górne (II–V)', cls='big')
f.text(3.0, 55.6, 'żebra dolne (VI–X)', cls='big')

# ---------------- podpisy – panel A
TL, TR = 30.0, 104.4
f.label(A['P'](-7.0, 8.0), 'trzon kręgu', 'corpus vertebrae', (TL, 13.0), side='L')
f.label(A['P'](-24.0, 27.6), 'wyrostek poprzeczny', 'processus transversus', (TL, 24.5), side='L')
f.text(TL - 0.7, 31.0, 'skierowany bocznie', cls='note', anchor='end')
f.label(A['H'], 'staw głowy żebra', 'articulatio capitis costae', (TR, 6.0), side='R')
f.label(A['F'], 'staw żebrowo-poprzeczny', 'articulatio costotransversaria', (TR, 14.5), side='R')
f.label((PA[0] + 12.5, PA[1]), 'płaszczyzna czołowa', None, (TR, 24.6), side='R')
mA = arc(PA, 5.5, 10.5, 10.5, 1)[0]
f.label(mA, 'czołowy kąt skrzyżowania', None, (TR, 30.6), side='R')
f.text(TR + 0.7, 34.2, 'żebro I ok. 10°, ku dołowi rośnie', cls='note')
f.label(along(A, 72), 'oś obrotu = oś szyjki żebra', None, (TR, 39.6), side='R')
f.text(TR + 0.7, 43.2, 'wdech: najsilniej ku górze,', cls='note')
f.text(TR + 0.7, 45.9, 'słabiej bocznie, najsłabiej do przodu', cls='note')

# ---------------- podpisy – panel B
f.label(B['P'](-17.0, 30.0), 'wyrostek poprzeczny', 'processus transversus', (TL, 77.0), side='L')
f.text(TL - 0.7, 83.5, 'odchylony ku tyłowi', cls='note', anchor='end')
mB = arc(HB, 7.0, 22.5, 22.5, 1)[0]
f.label(mB, 'czołowy kąt skrzyżowania', None, (TR, 70.0), side='R')
f.text(TR + 0.7, 73.6, 'żebro X ok. 45°', cls='note')
tb = min(B['ribpost'], key=lambda p: math.dist(p, (xa + 0.9, FB[1] + 0.6)))
f.label(tb, 'guzek żebra', 'tuberculum costae', (TR, 80.5), side='R')
f.text(TR + 0.7, 87.6, 'wdech: wsuwa się na wyrostek poprzeczny', cls='note')
f.text(TR + 0.7, 90.3, 'ku górze i ku tyłowi – ruch nie wokół', cls='note')
f.text(TR + 0.7, 93.0, 'osi szyjki; żebro najsilniej ku górze,', cls='note')
f.text(TR + 0.7, 95.7, 'słabiej bocznie, nieco ku tyłowi', cls='note')

if os.environ.get('PTS'):
    for nm, Q in (('A', A), ('B', B)):
        print(nm, 'H', [round(v, 1) for v in Q['H']], 'F', [round(v, 1) for v in Q['F']], 'theta', round(Q['theta'], 1), 'L', round(Q['L'], 1),
              'cut', [round(v, 1) for v in Q['cut']], 'tipC', [round(v, 1) for v in Q['tipC']])
    print('PA', PA, 'Cs', Cs, 'a1', a1, 'tb', tb)
f.save()
