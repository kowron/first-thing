# Oś czasu powstawania krzywizn kręgosłupa w płaszczyźnie pośrodkowej – sylwetki z boku (od strony lewej; przód w lewo).
# Schemat własny. Etapy i wiek wyłącznie wg Bochenka (s. 265–266):
#  · płód i noworodek – kształt kifotyczny odziedziczony po niższych ssakach (wzmaga go położenie płodu w macicy);
#    ogólna kifoza już u 3-tygodniowego zarodka, a z nią kifoza piersiowa – przypuszczalnie pierwsza krzywizna;
#    od 5. miesiąca życia płodowego – jako druga – krzywizna krzyżowa (ostateczny kształt znacznie później);
#  · ok. 4. miesiąca osesek uczy się dźwigać głowę – skurcz mięśni karku → lordoza szyi (względy ortoptyczne);
#  · siadanie, głównie pierwsze próby powstawania i chodzenia (10–15 miesiąc) → lordoza lędźwiowa, przypuszczalnie ostatnia
#    (względy statyczne);
#  · krzywizny szyjna i piersiowa ustalone do 6–7 roku życia, lędźwiowa dopiero w okresie dojrzewania płciowego.
# Proporcje kręgów jak u dorosłego (schemat); kręgi krzyżowe osobno aż do okresu pokwitania (Bochenek s. 241).
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 230, 100
f = Fig('krzywizny_os_czasu', W, H,
        caption='powstawanie krzywizn kręgosłupa w płaszczyźnie pośrodkowej · sylwetki z boku (przód w lewo) · oś wieku nie w skali')
BASE = 66.0                # poziom wierzchołka kości guzicznej (sylwetki stoją na wspólnej linii)


def R(x, y, a):            # obrót o kąt a (rad), +a = zgodnie z ruchem wskazówek zegara na rysunku (oś y w dół)
    return (x * math.cos(a) - y * math.sin(a), x * math.sin(a) + y * math.cos(a))


# ------------------------------------------------------------------ kręgi (mm kości; proporcje dorosłego)
def vert_table():
    V = []
    def add(name, reg, h, D, disc, A=9.0, L=0.0, beta=0.0, w=5.0, hp=None):
        V.append(dict(name=name, reg=reg, h=h, hp=hp or h, D=D, disc=disc, A=A, L=L, beta=beta, w=w))
    add('C2', 'C2', 24, 15.0, 5, A=10, L=22, beta=8, w=9)
    for i, D in enumerate([15.5, 16.0, 16.5, 17.0]):
        add(f'C{i + 3}', 'C', 14, D, 5, L=14 + 2 * i, beta=10 + i, w=5)
    add('C7', 'C', 15, 17.0, 5, L=28, beta=16, w=6)
    T = [(16, 17.0, 4, 20, 32), (17, 18.5, 4, 28, 34), (17.5, 20.0, 4, 36, 36), (18, 21.5, 4, 44, 37), (18.5, 23.0, 5, 50, 38),
         (19, 24.0, 5, 55, 39), (19.5, 25.5, 5, 58, 39), (20, 26.5, 5.5, 58, 39), (21, 27.5, 5.5, 50, 35), (22, 28.5, 6, 40, 31),
         (23, 29.5, 6, 28, 28), (24, 31.0, 8, 14, 25)]
    for i, (h, D, d, b, L) in enumerate(T):
        add(f'Th{i + 1}', 'T', h, D, d, L=L, beta=b, w=5.5)
    for i, (h, D, d) in enumerate([(26, 32.5, 10), (27, 33.5, 11), (27, 34.5, 11), (27, 35.0, 12), (28.5, 35.0, 12)]):
        add(f'L{i + 1}', 'L', h, D, d, A=12, L=24, beta=0, w=0.62 * h, hp=(24.5 if i == 4 else None))
    return V

SAC = [(26, 30, 4.5), (22, 26, 4.0), (18, 21, 3.5), (15, 16.5, 3.0), (12, 12.5, 2.4)]     # S1–S5 osobno: h, D, krążek
CO = [(8.0, 10.5, 1.6), (7.0, 8.6, 1.5), (6.0, 7.0, 1.4), (5.0, 5.6, 0.0)]                 # Co1–Co4


class Spine:
    """Kręgosłup wzdłuż osi o zadanym przebiegu kąta θ(s) (od pionu; θ>0 – oś biegnie ku dołowi i do tyłu)."""

    def __init__(self, keys, sac_keys, fused):
        self.V = vert_table()
        self.fused = fused
        s = 15.0                                   # ząb C2
        for v in self.V:
            v['s0'] = s; v['s1'] = s + v['h']; s = v['s1'] + v['disc']
        self.S_SAC = s
        self.by = {v['name']: v for v in self.V}
        self.SAC_LEN = 104.0 if fused else sum(h + d for h, D, d in SAC)
        self.END = self.S_SAC + self.SAC_LEN + 2.0 + sum(h + d for h, D, d in CO)
        ks = [(self.by[n]['s0'] + fr * self.by[n]['h'], th) for n, fr, th in keys]
        ks += [(self.S_SAC + ds, th) for ds, th in sac_keys]
        self.ks = ks
        DS = 0.5; self.DS = DS
        AX = [(0.0, 0.0)]
        for k in range(int((self.END + 12) / DS)):
            th = self.theta(k * DS); x, y = AX[-1]
            AX.append((x + math.sin(th) * DS, y + math.cos(th) * DS))
        self.AX = AX

    def theta(self, sv):
        ks = self.ks
        if sv <= ks[0][0]: return math.radians(ks[0][1])
        for (a, ta), (b, tb) in zip(ks, ks[1:]):
            if sv <= b:
                t = (sv - a) / (b - a); t = t * t * (3 - 2 * t)
                return math.radians(ta + (tb - ta) * t)
        return math.radians(ks[-1][1])

    def axis_pt(self, sv):
        AX, DS = self.AX, self.DS
        k = max(0, min(len(AX) - 2, int(sv / DS))); t = sv / DS - k
        return (AX[k][0] + (AX[k + 1][0] - AX[k][0]) * t, AX[k][1] + (AX[k + 1][1] - AX[k][1]) * t)

    def frame(self, sv):
        th = self.theta(sv)
        return self.axis_pt(sv), (math.sin(th), math.cos(th)), (math.cos(th), -math.sin(th))

    # --- ułożenie na rysunku
    def place(self, S, cx, rot_to=None):
        self.S = S
        top = self.axis_pt(0.0); sac = self.axis_pt(self.S_SAC)
        ang = math.atan2(sac[0] - top[0], sac[1] - top[1])      # nachylenie odcinka ząb–S1 względem pionu
        self.psi = (ang - rot_to) if rot_to is not None else 0.0
        self.ox, self.oy = 0.0, 0.0
        # dopasowanie: wierzchołek k. guzicznej na BASE, środek sylwetki (oś) na cx
        xs = [self.Gr(*self.axis_pt(sv))[0] for sv in range(0, int(self.END), 10)]
        end = self.Gr(*self.axis_pt(self.END))
        self.ox = cx - (min(xs) + max(xs)) / 2
        self.oy = BASE - end[1]
        return ang

    def Gr(self, x, y):
        X, Y = R(x, y, self.psi)
        return (self.ox + X * self.S, self.oy + Y * self.S)

    def L(self, sv, p, q=0.0):
        """Punkt w układzie lokalnym: p – wzdłuż normalnej (+ do tyłu) od osi, q – wzdłuż osi (+ w dół) od punktu sv."""
        c, u, n = self.frame(sv)
        return self.Gr(c[0] + p * n[0] + q * u[0], c[1] + p * n[1] + q * u[1])


def body_poly(sp, sv0, sv1, D, ha, hp):
    sc = (sv0 + sv1) / 2
    a, b = sp.L(sc, -D / 2, -ha / 2), sp.L(sc, D / 2, -hp / 2)
    c, d = sp.L(sc, D / 2, hp / 2), sp.L(sc, -D / 2, ha / 2)
    def mid(p, q, t): return (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)
    return [mid(a, b, .14), mid(a, b, .86), mid(b, c, .14), mid(b, c, .86), mid(c, d, .14), mid(c, d, .86),
            mid(d, a, .14), mid(d, a, .86)], (a, b, c, d)


def post_poly(sp, v):
    """Łuk z wyrostkiem kolczystym (uproszczony): p od tylnej powierzchni trzonu, q od górnej powierzchni."""
    h, A, Lp, w = v['h'], v['A'], v['L'], v['w']
    b = math.radians(v['beta'])
    q0 = 0.42 * h
    tip = (A + Lp * math.cos(b), q0 + Lp * math.sin(b))
    ux, uy = math.cos(b), math.sin(b); nx, ny = -uy, ux
    def P(t, half):     # punkt na wyrostku: t – ułamek długości, half – połowa szerokości (ujemna = górny brzeg)
        x = A + Lp * t * ux + half * nx; y = q0 + Lp * t * uy + half * ny
        return (x, y)
    w0 = max(w, 0.5 * h)
    pts = [(-0.6, 0.12 * h), (A * 0.55, 0.02 * h), P(0.0, -w0 / 2), P(0.55, -w / 2), P(0.94, -w * 0.42), P(1.0, 0.0),
           P(0.94, w * 0.42), P(0.55, w / 2), P(0.0, w0 / 2), (A * 0.55, 0.86 * h), (-0.6, 0.74 * h)]
    sc = (v['s0'] + v['s1']) / 2
    return [sp.L(sc, v['D'] / 2 + p, q - h / 2) for p, q in pts]


def draw_spine(sp):
    """Rysuje kręgosłup; zwraca słownik pomocniczy (kontury części tylnych do klamer)."""
    V = sp.V
    back_ext = []                      # (s, największe odsunięcie do tyłu w mm kości)
    # części tylne – od dołu do góry (dachówkowato)
    for v in V[::-1]:
        pts = post_poly(sp, v)
        f.add(f'<path class="bone" d="{smooth(pts, t=0.45)}"/>')
        sc = (v['s0'] + v['s1']) / 2
        b = math.radians(v['beta'])
        back_ext.append((sc, v['D'] / 2 + v['A'] + v['L'] * math.cos(b)))
    # C1: łuk tylny z guzkiem tylnym
    c1b = [sp.L(8, 9.5, -3.0), sp.L(8, 20, -4.2), sp.L(8, 27.5, -3.4), sp.L(8, 28.5, 1.2), sp.L(8, 20, 2.4), sp.L(8, 9.5, 2.6)]
    f.add(f'<path class="bone" d="{smooth(c1b)}"/>')
    back_ext.append((8, 29.0))
    # kość krzyżowa i guziczna
    S0 = sp.S_SAC
    sac_shapes = []
    if sp.fused:
        def sD(t): return 32.0 - 18.0 * t
        def sP(t): return 24.0 - 17.0 * t ** 0.8
        fr, bk = [], []
        for i in range(25):
            t = i / 24; sv = S0 + t * sp.SAC_LEN
            fr.append(sp.L(sv, -sD(t) / 2)); bk.append(sp.L(sv, sD(t) / 2 + sP(t)))
            back_ext.append((sv, sD(t) / 2 + sP(t)))
        sap = [sp.L(S0, 16 + 4.0, 0.6), sp.L(S0, 16 + 6.5, -7.0), sp.L(S0, 16 + 11.5, -9.5), sp.L(S0, 16 + 15.5, -4.0),
               sp.L(S0, 16 + 20.0, 0.4)]
        f.add(f'<path class="bone" d="{smooth(sap + bk[1:] + fr[::-1])}"/>')
        for t in (0.27, 0.50, 0.70, 0.86):      # kresy poprzeczne (miejsca zrostu trzonów)
            sv = S0 + t * sp.SAC_LEN
            a, b2 = sp.L(sv, -sD(t) / 2), sp.L(sv, -sD(t) / 2 + 0.3 * (sD(t) + sP(t)))
            f.add(f'<path class="bonel" d="M{a[0]:.2f},{a[1]:.2f} L{b2[0]:.2f},{b2[1]:.2f}"/>')
        s = S0 + sp.SAC_LEN + 2.0
        sac_front0 = fr[0]
    else:
        s = S0
        for i, (h, D, d) in enumerate(SAC):
            v = dict(s0=s, s1=s + h, h=h, D=D, A=6.0, L=7.0 + 1.0 * (4 - i), beta=25, w=0.5 * h)
            f.add(f'<path class="bone" d="{smooth(post_poly(sp, v), t=0.45)}"/>')
            back_ext.append((s + h / 2, D / 2 + 6 + 7 + (4 - i)))
            sac_shapes.append((s, s + h, D, d)); s += h + d
        sac_front0 = sp.L(S0, -SAC[0][1] / 2)
    co_shapes = []
    for h, D, d in CO:
        co_shapes.append((s, s + h, D, d)); back_ext.append((s + h / 2, D / 2)); s += h + d
    # krążki
    bodies = [(v['s0'], v['s1'], v['D'], v['h'], v['hp']) for v in V]
    if not sp.fused:
        bodies += [(a, b2, D, b2 - a, b2 - a) for a, b2, D, d in sac_shapes]
    for (a0, a1, Da, ha, hpa), (b0, b1, Db, hb, hpb) in zip(bodies, bodies[1:]):
        _, (p1, q1, r1, t1) = body_poly(sp, a0, a1, Da, ha, hpa)
        _, (p2, q2, r2, t2) = body_poly(sp, b0, b1, Db, hb, hpb)
        f.add(f'<path class="annulus" d="M{t1[0]:.2f},{t1[1]:.2f} L{r1[0]:.2f},{r1[1]:.2f} L{q2[0]:.2f},{q2[1]:.2f} L{p2[0]:.2f},{p2[1]:.2f} Z"/>')
    if sp.fused:
        v = V[-1]
        _, (p1, q1, r1, t1) = body_poly(sp, v['s0'], v['s1'], v['D'], v['h'], v['hp'])
        q2, p2 = sp.L(S0, 16.0), sp.L(S0, -16.0)
        f.add(f'<path class="annulus" d="M{t1[0]:.2f},{t1[1]:.2f} L{r1[0]:.2f},{r1[1]:.2f} L{q2[0]:.2f},{q2[1]:.2f} L{p2[0]:.2f},{p2[1]:.2f} Z"/>')
    # trzony
    for v in V:
        if v['name'] == 'C2':
            continue
        poly, _ = body_poly(sp, v['s0'], v['s1'], v['D'], v['h'], v['hp'])
        f.add(f'<path class="bone" d="{smooth(poly, t=0.45)}"/>')
    if not sp.fused:
        for a, b2, D, d in sac_shapes:
            poly, _ = body_poly(sp, a, b2, D, b2 - a, b2 - a)
            f.add(f'<path class="bone" d="{smooth(poly, t=0.45)}"/>')
    for a, b2, D, d in co_shapes:
        poly, _ = body_poly(sp, a, b2, D, b2 - a, b2 - a)
        f.add(f'<path class="bone" d="{smooth(poly, t=0.6)}"/>')
    # C2 z zębem
    v = sp.by['C2']; sc = (v['s0'] + v['s1']) / 2
    def A2(p, q): return sp.L(sc, p - 7.5, q - 12.0)        # p od przedniej powierzchni, q od górnej powierzchni trzonu
    c2 = [A2(0.6, 0.8), A2(3.6, -1.0), A2(4.4, -10.5), A2(7.4, -14.6), A2(11.0, -13.2), A2(11.8, -2.0), A2(15.0, 1.5),
          A2(15.0, 20.0), A2(13.6, 24.0), A2(1.0, 24.6), A2(-0.4, 14.0)]
    f.add(f'<path class="bone" d="{smooth(c2)}"/>')
    # C1: łuk przedni
    c1a = [sp.L(8, -12.5, -3.4), sp.L(8, -7.6, -3.8), sp.L(8, -6.6, 0.0), sp.L(8, -7.6, 3.4), sp.L(8, -12.5, 3.0), sp.L(8, -14.0, 0.0)]
    f.add(f'<path class="bone" d="{smooth(c1a)}"/>')
    back_ext.sort()
    return dict(back=back_ext, sac_front0=sac_front0)


# ------------------------------------------------------------------ czaszka (schemat; początek układu = kłykcie potyliczne)
ADULT = [(-80, 60), (-86, 46), (-85, 30), (-90, 18), (-93, 4), (-99, -12), (-103, -24), (-96, -40), (-102, -52), (-98, -76),
         (-83, -102), (-55, -122), (-18, -132), (22, -128), (56, -110), (80, -82), (90, -50), (84, -26), (62, -8), (30, 2),
         (14, 12), (2, 6), (-12, 2), (-18, 12), (-22, 34), (-28, 48), (-52, 56)]
ADULT_ORB = (-78, -34, 12.5, 11.5)
INFANT = [(-60, 33), (-63, 25), (-64, 15), (-68, 6), (-71, -4), (-69, -14), (-77, -24), (-86, -48), (-79, -78), (-55, -100),
          (-18, -110), (22, -106), (56, -88), (80, -60), (88, -30), (80, -10), (56, 1), (24, 5), (10, 8), (-2, 4), (-9, 4),
          (-12, 15), (-16, 25), (-36, 31)]
INFANT_ORB = (-56, -16, 11.0, 10.5)


def skull_pts(mix):
    """mix: 0 – czaszka noworodka, 1 – czaszka dorosłego (proste mieszanie konturów o tej samej liczbie punktów)."""
    A = ADULT[:]; I = INFANT[:]
    # wyrównanie liczby punktów (dorosły ma o 3 więcej) – dopełnienie konturu dziecka punktami pośrednimi
    while len(I) < len(A):
        k = len(I) - 1
        I.insert(k, ((I[k - 1][0] + I[k][0]) / 2, (I[k - 1][1] + I[k][1]) / 2))
    pts = [(i[0] + (a[0] - i[0]) * mix, i[1] + (a[1] - i[1]) * mix) for a, i in zip(A, I)]
    orb = tuple(i + (a - i) * mix for a, i in zip(ADULT_ORB, INFANT_ORB))
    return pts, orb


def draw_skull(J, length, droop_deg, mix):
    pts, (ox, oy, rx, ry) = skull_pts(mix)
    xs = [p[0] for p in pts]
    k = length / (max(xs) - min(xs))
    d = math.radians(droop_deg)
    def T(x, y):
        X = x * math.cos(d) + y * math.sin(d); Y = -x * math.sin(d) + y * math.cos(d)
        return (J[0] + X * k, J[1] + Y * k)
    P = [T(x, y) for x, y in pts]
    f.add(f'<path class="bone" d="{smooth(P)}"/>')
    o = T(ox, oy)
    f.add(f'<ellipse class="hole" cx="{o[0]:.2f}" cy="{o[1]:.2f}" rx="{rx * k:.2f}" ry="{ry * k:.2f}" '
          f'transform="rotate({-droop_deg:.1f} {o[0]:.2f} {o[1]:.2f})"/>')
    return T


# ------------------------------------------------------------------ etapy
SAC_ADULT = [(2, 47), (30, 40), (60, 22), (85, 4), (104, -12), (116, -28), (138, -48)]
STAGES = [
    dict(key='nb', cx=21.0, S=0.046, head=19.0, droop=26, mix=0.0, fused=False,
         keys=[('C2', 0.0, 30), ('C7', 0.5, 22), ('Th1', 0.5, 20), ('Th7', 0.5, 10), ('Th12', 0.5, 0), ('L3', 0.5, -6),
               ('L5', 0.5, -10)],
         sac=[(2, -14), (40, -22), (80, -32), (110, -40), (125, -48), (146, -55)]),
    dict(key='m4', cx=68.0, S=0.051, head=20.0, droop=-4, mix=0.06, fused=False,
         keys=[('C2', 0.0, -3), ('C4', 0.5, 4), ('C7', 0.5, 12), ('Th1', 0.8, 14), ('Th7', 0.5, 6), ('Th12', 0.5, -2),
               ('L3', 0.5, -8), ('L5', 0.5, -12)],
         sac=[(2, -15), (40, -23), (80, -33), (110, -41), (125, -49), (146, -56)]),
    dict(key='m12', cx=114.0, S=0.057, head=20.5, droop=0, mix=0.2, fused=False,
         keys=[('C2', 0.0, -9), ('C4', 1.0, 0), ('C7', 0.5, 12), ('Th1', 0.9, 15), ('Th7', 0.5, 2), ('Th12', 0.9, -11),
               ('L3', 0.6, -2), ('L5', 0.5, 9)],
         sac=[(2, 26), (40, 18), (80, 4), (110, -10), (125, -24), (146, -38)]),
    dict(key='y7', cx=160.0, S=0.064, head=19.0, droop=0, mix=0.6, fused=False,
         keys=[('C2', 0.0, -13), ('C4', 1.2, 0), ('C7', 0.5, 15), ('Th1', 1.0, 19), ('Th7', 0.5, 0), ('Th12', 0.9, -17),
               ('L3', 0.6, 0), ('L5', 0.5, 16)],
         sac=[(2, 40), (40, 30), (80, 12), (110, -6), (125, -22), (146, -40)]),
    dict(key='ad', cx=206.0, S=0.069, head=14.0, droop=0, mix=1.0, fused=True,
         keys=[('C2', 0.0, -14), ('C4', 1.2, 0), ('C7', 0.5, 15), ('Th1', 1.0, 19), ('Th7', 0.5, 0), ('Th12', 0.9, -19),
               ('L3', 0.6, 0), ('L5', 0.5, 20)],
         sac=SAC_ADULT),
]

ref = Spine(STAGES[-1]['keys'], SAC_ADULT, True)
top, sac = ref.axis_pt(0.0), ref.axis_pt(ref.S_SAC)
ANG_REF = math.atan2(sac[0] - top[0], sac[1] - top[1])

INFO = {}
for st in STAGES:
    sp = Spine(st['keys'], st['sac'], st['fused'])
    sp.place(st['S'], st['cx'], rot_to=ANG_REF)
    # czaszka (rysowana pod kręgosłupem): staw szczytowo-potyliczny nad zębem, nieco do tyłu
    J = sp.L(0.0, 3.0, -5.0)
    T = draw_skull(J, st['head'], st['droop'] + math.degrees(sp.psi) * 0, st['mix'])
    aux = draw_spine(sp)
    INFO[st['key']] = dict(sp=sp, aux=aux, J=J, T=T, st=st)


# ------------------------------------------------------------------ znaczniki krzywizn (po stronie wypukłej)
def back_off(aux, sv):
    pts = aux['back']
    best = 0.0
    for s_, o in pts:                 # największe odsunięcie w otoczeniu ±25 mm (wygładzenie)
        if abs(s_ - sv) < 25:
            best = max(best, o - 0.012 * (s_ - sv) ** 2)
    return best


def marker(key, s_a, s_b, side, fixed, gap=9.0):
    I = INFO[key]; sp, aux = I['sp'], I['aux']
    N = 40
    pts = []
    for i in range(N + 1):
        sv = s_a + (s_b - s_a) * i / N
        if side < 0:
            v = None
            for vv in sp.V:
                if vv['s0'] - 6 <= sv: v = vv
            D = v['D'] if v else 15
            if sv > sp.S_SAC: D = 30
            o = -(D / 2 + gap)
        else:
            o = back_off(aux, sv) + gap
        pts.append(sp.L(sv, o))
    # wygładzenie
    sm = [pts[0]] + [((pts[i - 1][0] + 2 * pts[i][0] + pts[i + 1][0]) / 4, (pts[i - 1][1] + 2 * pts[i][1] + pts[i + 1][1]) / 4)
                     for i in range(1, N)] + [pts[-1]]
    d = 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in sm)
    for sv, p in ((s_a, sm[0]), (s_b, sm[-1])):
        c, u, n = sp.frame(sv)
        tk = 1.0 * side
        nn = R(n[0], n[1], sp.psi)
        d += f' M{p[0]:.2f},{p[1]:.2f} L{p[0] - nn[0] * tk:.2f},{p[1] - nn[1] * tk:.2f}'
    f.add(f'<path class="{"lead" if fixed else "dim"}" d="{d}"/>')
    return sm[N // 2], sm


def segs(key):
    sp = INFO[key]['sp']; b = sp.by
    return dict(C=(0.0, b['C7']['s1']), T=(b['Th1']['s0'], b['Th12']['s1']), L=(b['L1']['s0'], b['L5']['s1']),
                S=(sp.S_SAC, sp.END), ALL=(0.0, sp.END), TS=(b['Th1']['s0'], sp.END))

M = {}
g = segs('nb');  M['nb_all'] = marker('nb', *g['ALL'], +1, False)
g = segs('m4');  M['m4_C'] = marker('m4', *g['C'], -1, False); M['m4_TS'] = marker('m4', *g['TS'], +1, False)
for k, fx in (('m12', dict(C=0, T=0, L=0, S=0)), ('y7', dict(C=1, T=1, L=0, S=0)), ('ad', dict(C=1, T=1, L=1, S=1))):
    g = segs(k)
    M[k + '_C'] = marker(k, *g['C'], -1, fx['C'])
    M[k + '_T'] = marker(k, *g['T'], +1, fx['T'])
    M[k + '_L'] = marker(k, *g['L'], -1, fx['L'])
    M[k + '_S'] = marker(k, *g['S'], +1, fx['S'])

# ------------------------------------------------------------------ przyczyny: mięśnie karku, uwypuklenie lędźwi
I = INFO['m4']; sp = I['sp']
occ = I['T'](70, -14)                      # okolica guzowatości potylicznej
c7 = sp.L(sp.by['C7']['s0'] + 7, sp.by['C7']['D'] / 2 + 9 + 26, 0)
mid = sp.L(sp.by['C4']['s0'], 52, 0)
mus = [occ, mid, c7]
f.add(f'<path class="muscle" d="{smooth([occ, (mid[0] + 0.9, mid[1]), (c7[0] + 0.6, c7[1] + 0.5), (c7[0] - 0.3, c7[1] + 0.2), (mid[0] - 0.4, mid[1]), (occ[0] - 0.9, occ[1] + 0.6)])}"/>')
# łuk – unoszenie głowy
hc = I['T'](-10, -60)
f.arrow(f'M{hc[0] - 6.5:.2f},{hc[1] + 3.5:.2f} Q{hc[0] - 4.5:.2f},{hc[1] - 6.0:.2f} {hc[0] + 3.0:.2f},{hc[1] - 7.5:.2f}')

I = INFO['m12']; sp = I['sp']
pL = sp.L(sp.by['L3']['s0'] + 13, -(sp.by['L3']['D'] / 2 + 9), 0)
f.arrow(f'M{pL[0] + 0.2:.2f},{pL[1]:.2f} L{pL[0] - 4.2:.2f},{pL[1]:.2f}')

# ------------------------------------------------------------------ podpisy krzywizn (nowa krzywizna przy sylwetce)
def P(key, nm):
    return M[f'{key}_{nm}'][0]

def note(x, y, t, side='R'):
    f.text(x + (0.7 if side == 'R' else -0.7), y, t, cls='note', anchor='start' if side == 'R' else 'end')

I = INFO['nb']; sp = I['sp']
a = P('nb', 'all'); tx = 34.0
f.label(a, 'ogólna kifoza', None, (tx, 40.5), side='R')
note(tx, 43.6, 'już u 3-tyg. zarodka; z nią'); note(tx, 46.2, 'kifoza piersiowa – przypuszczalnie')
note(tx, 48.8, 'pierwsza krzywizna')
ps = sp.L(sp.S_SAC + 30, 0.0)
f.label(ps, 'krzywizna krzyżowa', 'kyphosis sacralis', (tx, 55.0), side='R')
note(tx, 61.2, 'od 5. mies. życia płodowego –'); note(tx, 63.8, 'druga z kolei')

I = INFO['m4']; sp = I['sp']
a = P('m4', 'C'); f.label(a, 'lordoza szyi', 'lordosis cervicalis', (a[0] - 8.0, 27.0), side='L')
f.label(mid, 'mięśnie karku', None, (mid[0] + 8.5, 24.5), side='R')

I = INFO['m12']; sp = I['sp']
f.label((pL[0] - 4.6, pL[1]), 'lordoza lędźwiowa', 'lordosis lumbalis', (pL[0] - 10.0, 58.0), side='L')
note(pL[0] - 10.0, 64.2, 'przypuszczalnie ostatnia', 'L')

# ------------------------------------------------------------------ opisy etapów – przyczyny (pod sylwetkami)
TXT = {
    'nb': ['płód i noworodek',
           'kształt odziedziczony po niższych',
           'ssakach; wzmaga go położenie',
           'i warunki przestrzenne płodu w macicy'],
    'm4': ['dźwiganie głowy',
           'punkt ciężkości głowy – do przodu od',
           'stawu szczytowo-potylicznego; skurcz',
           'mięśni karku zgina szyję do tyłu'],
    'm12': ['siadanie, wstawanie, chodzenie',
            'lędźwie uwypuklają się do przodu:',
            'tułów nie przewraca się do przodu',
            'pod masą swej górnej części'],
    'y7': ['ustalenie krzywizn',
           'szyjna i piersiowa – ustalone',
           'kształt klinowaty: w kifozach – trzony,',
           'w lordozach – krążki'],
    'ad': ['ustalenie krzywizny',
           'lędźwiowa – ustalona dopiero',
           'w okresie dojrzewania płciowego',
           '→ wężowaty kształt dorosłego'],
}
TY = 70.5
for k, lines in TXT.items():
    x = INFO[k]['st']['cx']
    f.text(x, TY, lines[0], cls='pl', anchor='middle')
    for i, t in enumerate(lines[1:]):
        f.text(x, TY + 3.3 + i * 2.6, t, cls='notec', anchor='middle')
f.text(INFO['m4']['st']['cx'], TY + 3.3 + 3 * 2.6, '(względy ortoptyczne: pole widzenia)', cls='notec', anchor='middle')
f.text(INFO['m12']['st']['cx'], TY + 3.3 + 3 * 2.6, '(względy statyczne)', cls='notec', anchor='middle')

# ------------------------------------------------------------------ oś wieku
AY = 87.5
f.add(f'<path class="lead" d="M3,{AY} L{W - 4.5:.2f},{AY}"/>')
f.add(f'<path class="dot" d="M{W - 2.2:.2f},{AY} L{W - 5.0:.2f},{AY - 1.1:.2f} L{W - 5.0:.2f},{AY + 1.1:.2f} Z"/>')
TICKS = [(INFO['nb']['st']['cx'], ['urodzenie']), (INFO['m4']['st']['cx'], ['ok. 4. miesiąca']),
         (INFO['m12']['st']['cx'], ['10–15 miesiąc']), (INFO['y7']['st']['cx'], ['do 6–7 roku życia']),
         (INFO['ad']['st']['cx'], ['okres dojrzewania płciowego'])]
for x, lab in TICKS:
    f.add(f'<path class="lead" d="M{x:.2f},{AY - 1.0} L{x:.2f},{AY + 1.0}"/>')
    for i, t in enumerate(lab):
        f.text(x, AY + 4.0 + i * 2.6, t, cls='pl', anchor='middle')
f.text(W - 3.0, AY - 1.8, 'wiek', cls='note', anchor='end')
f.text(5.0, AY - 1.8, '← życie płodowe', cls='note', anchor='start')

# ------------------------------------------------------------------ legenda (lewy górny róg)
LY = 5.0
f.add(f'<path class="dim" d="M4,{LY} L11,{LY}"/>'); f.text(12.2, LY + 0.7, 'krzywizna przejściowa (jeszcze nieustalona)', cls='note')
f.add(f'<path class="lead" d="M4,{LY + 3.4} L11,{LY + 3.4}"/>'); f.text(12.2, LY + 4.1, 'krzywizna ustalona', cls='note')
f.text(4.0, LY + 7.8, 'znacznik z przodu – lordoza (wypukłość do przodu),', cls='note')
f.text(4.0, LY + 10.4, 'z tyłu – kifoza (wypukłość ku tyłowi)', cls='note')
f.save()
for k, I in INFO.items():
    print(k, 'psi', round(math.degrees(I['sp'].psi), 1), 'J', [round(t, 1) for t in I['J']])
