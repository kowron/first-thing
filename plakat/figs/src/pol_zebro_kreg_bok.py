# POŁĄCZENIA ŻEBER Z KRĘGOSŁUPEM – widok od strony lewej (przód w lewo).
# Kręgi piersiowe Th4–Th6: żebro V usunięte (otwarty staw głowy żebra: dołek żebrowy dolny Th4, krążek, dołek żebrowy górny Th5,
# kikut więzadła śródstawowego; dołek żebrowy wyrostka poprzecznego Th5), żebro VI na miejscu z więzadłem promienistym głowy żebra
# i więzadłem żebrowo-poprzecznym górnym (do wyrostka poprzecznego Th5).
# Wstawka: przekrój czołowy stawu głowy żebra VI (widok od przodu) – grzebień głowy, więzadło śródstawowe, dwie jamy stawowe.
# Schemat własny wg opisu Bochenka, t. I, s. 283–285 (ryc. 190 oglądana tylko dla położenia struktur); nazwy z k_polaczenia.json.
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 150, 102
S = 1.0                      # mm rysunku / mm kości (widok główny)
X0 = 49.0                    # x rysunku dla x kości = 0 (przednia powierzchnia trzonów)
YW0, YW1 = 12.0, 62.0        # okno widoku (y kości): od dolnej części Th4 do dolnej części Th6
Y0 = 3.0                     # y rysunku dla y kości = YW0
f = Fig('pol_zebro_kreg_bok', W, H,
        caption='kręgi piersiowe Th4–Th6 z żebrem VI (żebro V usunięte) · widok od strony lewej (przód w lewo)')


def P(x, y):
    return (X0 + x * S, Y0 + (y - YW0) * S)


def T(pts):
    return [P(x, y) for x, y in pts]


def line(pts):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts)


def poly(pts):
    return line(pts) + ' Z'


TOPS = {'Th3': -22.5, 'Th4': 0.0, 'Th5': 22.5, 'Th6': 45.0, 'Th7': 67.5}   # górna powierzchnia trzonu (y kości)


def body(t):
    return [(0.7, t + 0.05), (6.0, t - 0.2), (12.0, t - 0.25), (18.0, t - 0.2), (22.6, t + 0.0), (23.8, t + 0.7),
            (24.1, t + 3.0), (23.7, t + 9.0), (24.1, t + 15.0), (23.9, t + 17.3), (22.8, t + 18.1), (18.0, t + 18.25),
            (12.0, t + 18.3), (6.0, t + 18.25), (0.7, t + 18.0), (-0.2, t + 17.0), (0.4, t + 13.0), (0.9, t + 9.0),
            (0.4, t + 5.0), (-0.2, t + 1.0)]


def disc(t):          # krążek pod trzonem o górze t
    return [(0.6, t + 17.9), (12.0, t + 18.2), (22.8, t + 18.0), (23.9, t + 18.6), (24.1, t + 20.25), (23.9, t + 21.9),
            (22.8, t + 22.5), (12.0, t + 22.3), (0.6, t + 22.6), (-0.6, t + 21.6), (-0.9, t + 20.25), (-0.6, t + 18.9)]


def arch(t):          # nasada łuku, wyrostki stawowe, blaszka i wyrostek kolczysty (widok z boku)
    d = [(23.4, 1.0), (25.5, 1.7), (27.6, 1.3),                                        # nasada – wcięcie kręgowe górne
         (28.4, -0.6), (28.8, -3.2), (29.6, -5.2), (31.0, -6.0), (32.6, -5.6), (33.5, -3.4), (33.8, -0.6),  # wyr. stawowy górny
         (34.6, 1.6), (36.2, 3.6),
         (38.6, 6.8), (41.2, 12.0), (43.8, 18.6), (45.8, 25.0), (47.1, 30.6), (47.6, 33.8), (47.2, 36.0), (46.0, 36.6),
         (45.0, 35.4), (43.2, 30.0), (41.0, 24.2), (39.4, 20.0),                       # wyrostek kolczysty
         (38.2, 17.6), (37.9, 21.4), (37.2, 23.4), (36.0, 24.3), (34.6, 24.1), (33.7, 22.2), (33.3, 18.0), (33.0, 14.0),  # wyr. stawowy dolny
         (31.6, 11.6), (29.6, 10.2), (27.0, 9.6), (24.8, 9.9), (23.4, 10.6)]           # wcięcie kręgowe dolne
    return [(x, t + y) for x, y in d]


def tproc(t):         # wyrostek poprzeczny (biegnie ku tyłowi i bocznie – ku patrzącemu)
    d = [(29.4, 1.8), (32.6, 0.4), (36.6, -0.2), (40.6, -0.4), (43.8, 0.0), (45.6, 1.6), (46.2, 4.4), (45.9, 7.8),
         (44.6, 10.2), (42.4, 10.9), (39.4, 10.2), (36.4, 9.8), (33.2, 10.2), (30.4, 9.8), (29.0, 6.2)]
    return [(x, t + y) for x, y in d]


def contour_front(y):
    """przednia powierzchnia słupa trzonów i krążków (x kości) – do więzadła podłużnego przedniego"""
    t = 0.0
    while t + 22.5 <= y:
        t += 22.5
    while t > y:
        t -= 22.5
    dy = y - t
    if dy <= 18.0:
        return 0.95 * math.sin(math.pi * dy / 18.0) - 0.2
    u = (dy - 18.0) / 4.5
    return -0.2 - 0.7 * math.sin(math.pi * u)


# ======================================================================= widok główny (w oknie)
mx0, my0 = P(-12, YW0)
mx1, my1 = P(70, YW1)
f.add(f'<defs><clipPath id="cp_zkb_main"><rect x="{mx0:.2f}" y="{my0:.2f}" width="{mx1 - mx0:.2f}" height="{my1 - my0:.2f}"/></clipPath></defs>')
f.add('<g clip-path="url(#cp_zkb_main)">')

# łuki (od góry: wyrostki kolczyste wyższych kręgów schodzą za niższe)
for k in ('Th3', 'Th4', 'Th5', 'Th6'):
    t = TOPS[k]
    f.add(f'<path class="bone" d="{smooth(T(arch(t)))}"/>')
    # powierzchnia stawowa wyrostka stawowego górnego (zwrócona ku tyłowi – widoczna z boku jako pasek)
    fac = [(32.9, t - 4.8), (33.6, t - 3.2), (33.9, t - 0.4), (33.2, t - 0.3), (32.9, t - 3.0), (32.3, t - 4.6)]
    f.add(f'<path class="facet" d="{smooth(T(fac))}"/>')
    # grzbiet wyrostka kolczystego
    f.add(f'<path class="bonel" d="{smooth(T([(39.6, t + 10.5), (42.4, t + 18.0), (44.6, t + 25.5), (46.0, t + 32.5)]), closed=False)}"/>')

# krążki, potem trzony
for k in ('Th3', 'Th4', 'Th5', 'Th6'):
    f.add(f'<path class="annulus" d="{smooth(T(disc(TOPS[k])))}"/>')
for k in ('Th4', 'Th5', 'Th6', 'Th7'):
    t = TOPS[k]
    f.add(f'<path class="bone" d="{smooth(T(body(t)))}"/>')
    for yy in (t + 1.15, t + 16.85):     # brzegi pierścieni nasadowych
        f.add(f'<path class="bonel" d="{smooth(T([(1.4, yy), (8.0, yy + 0.12), (15.8, yy + 0.05)]), closed=False)}"/>')

# więzadło podłużne przednie (pasmo na przedniej powierzchni trzonów i krążków)
ys = [YW0 - 2 + 0.5 * i for i in range(int((YW1 - YW0 + 4) / 0.5) + 1)]
left = [(contour_front(y) - 1.7, y) for y in ys]
right = [(contour_front(y) + 1.9 + 0.25 * math.sin(y / 3.1), y) for y in ys]
f.add(f'<path class="lig" d="{poly(T(left + right[::-1]))}"/>')
for off in (-0.6, 0.7):
    f.add(f'<path class="bonel" d="{line(T([(contour_front(y) + off, y) for y in ys[::4]]))}"/>')

# ---- otwarty staw głowy żebra V (żebro usunięte): dołek dolny Th4, krążek, dołek górny Th5, kikut więzadła śródstawowego
f.add(f'<path class="shade" d="{smooth(T([(17.6, 17.4), (20.8, 16.6), (24.0, 17.4), (24.2, 23.0), (20.8, 23.8), (17.4, 23.0)]))}"/>')
a, b = P(17.7, 18.05), P(23.95, 18.05)
f.add(f'<path class="facet" d="M{a[0]:.2f},{a[1]:.2f} A{3.12 * S:.2f},{3.0 * S:.2f} 0 0,1 {b[0]:.2f},{b[1]:.2f} Z"/>')
a, b = P(17.5, 22.45), P(23.95, 22.45)
f.add(f'<path class="facet" d="M{a[0]:.2f},{a[1]:.2f} A{3.22 * S:.2f},{3.5 * S:.2f} 0 0,0 {b[0]:.2f},{b[1]:.2f} Z"/>')
c = P(20.8, 20.25)
f.add(f'<ellipse class="lig" cx="{c[0]:.2f}" cy="{c[1]:.2f}" rx="{2.9 * S:.2f}" ry="{0.72 * S:.2f}"/>')
# brzeg przyczepu torebki stawowej wokół panewki
f.add(f'<path class="capsule" d="{smooth(T([(16.6, 17.6), (18.2, 14.2), (21.2, 13.6), (24.4, 15.0), (25.0, 20.25), (24.4, 25.6), (21.2, 27.0), (18.0, 26.4), (16.4, 22.8)]))}"/>')

# ---- wyrostki poprzeczne (Th5 – wolny dołek żebrowy; Th6 – z guzkiem żebra VI)
for k in ('Th5', 'Th6'):
    t = TOPS[k]
    f.add(f'<path class="bone" d="{smooth(T(tproc(t)))}"/>')
    f.add(f'<path class="bonel" d="{smooth(T([(34.0, t + 2.0), (38.5, t + 1.2), (42.6, t + 1.3)]), closed=False)}"/>')
c = P(42.0, TOPS['Th5'] + 5.6)
f.add(f'<ellipse class="facet" cx="{c[0]:.2f}" cy="{c[1]:.2f}" rx="{2.0 * S:.2f}" ry="{2.7 * S:.2f}" transform="rotate(-10 {c[0]:.2f} {c[1]:.2f})"/>')

# ---- więzadło żebrowo-poprzeczne górne: grzebień szyjki żebra VI → dolny brzeg wyrostka poprzecznego Th5
lcs = [(28.4, 42.2), (30.6, 38.0), (32.4, 34.0), (33.8, 32.5), (37.6, 32.3), (41.9, 33.2), (41.7, 35.2), (40.0, 39.6),
       (39.0, 46.2), (35.6, 45.0), (31.8, 43.4)]
f.add(f'<path class="lig" d="{smooth(T(lcs))}"/>')
for p, q in [((30.4, 41.6), (34.4, 33.1)), ((32.8, 42.6), (36.4, 33.0)), ((35.2, 43.7), (38.4, 33.2)), ((37.6, 44.8), (40.4, 33.6))]:
    f.add(f'<path class="bonel" d="{line(T([p, q]))}"/>')

# ---- żebro VI (głowa na wysokości krążka Th5/Th6, guzek przy wyrostku poprzecznym Th6)
rib = [(18.6, 39.2), (20.6, 38.4), (23.0, 38.7), (26.2, 40.1), (30.2, 41.9), (34.2, 43.6), (37.8, 45.0), (41.0, 46.3),
       (44.2, 47.6), (47.0, 49.0), (48.9, 50.6), (49.7, 53.4), (49.3, 56.2), (47.9, 57.8), (45.6, 57.6), (42.8, 56.8),
       (40.0, 55.6), (37.2, 53.6), (34.0, 51.4), (30.4, 49.6), (27.0, 48.2), (24.2, 47.5), (21.8, 47.6), (19.6, 46.9),
       (18.0, 45.2), (17.4, 42.9), (17.7, 40.7)]
f.add(f'<path class="bone" d="{smooth(T(rib))}"/>')
c = P(48.5, 53.8)
f.add(f'<ellipse class="bone2" cx="{c[0]:.2f}" cy="{c[1]:.2f}" rx="{1.45 * S:.2f}" ry="{3.9 * S:.2f}" transform="rotate(-8 {c[0]:.2f} {c[1]:.2f})"/>')
f.add(f'<path class="bonel" d="{smooth(T([(24.2, 40.5), (30.5, 43.0), (37.5, 46.0), (43.5, 48.6)]), closed=False)}"/>')

# ---- więzadło promieniste głowy żebra VI – trzy płaskie pasma rozbieżne ku przodowi: do trzonu Th5, do krążka, do trzonu Th6
BANDS = [  # (przyczep na głowie: górny, dolny), (przyczep przedni: górny, dolny)
    (((19.6, 38.9), (18.0, 41.9)), ((10.2, 33.9), (9.4, 37.9))),
    (((17.6, 41.3), (17.6, 44.2)), ((8.3, 41.1), (8.3, 44.4))),
    (((18.0, 43.6), (19.6, 46.6)), ((9.4, 47.6), (10.2, 51.6))),
]
order = (1, 0, 2)
for i in order:
    (h0, h1), (a0, a1) = BANDS[i]
    m0 = ((h0[0] + a0[0]) / 2, (h0[1] + a0[1]) / 2 + (0.35 if i == 0 else (-0.35 if i == 2 else 0)))
    m1 = ((h1[0] + a1[0]) / 2, (h1[1] + a1[1]) / 2 + (0.35 if i == 0 else (-0.35 if i == 2 else 0)))
    ends = [(a0[0] - 0.55, a0[1] + 0.3 * (a1[1] - a0[1])), (a1[0] - 0.55, a1[1] - 0.3 * (a1[1] - a0[1]))]
    shape = [h0, m0, a0, ends[0], ends[1], a1, m1, h1, (h1[0] + 1.6, (h0[1] + h1[1]) / 2 + 0.8), (h0[0] + 1.6, (h0[1] + h1[1]) / 2 - 0.8)]
    f.add(f'<path class="lig" d="{smooth(T(shape))}"/>')
    for u in (0.28, 0.62):
        p = (h0[0] + (h1[0] - h0[0]) * u + 0.6, h0[1] + (h1[1] - h0[1]) * u)
        q = (a0[0] + (a1[0] - a0[0]) * u - 0.2, a0[1] + (a1[1] - a0[1]) * u)
        f.add(f'<path class="bonel" d="{line(T([p, q]))}"/>')

f.text(*P(3.6, 17.0), 'Th4')
f.text(*P(11.0, 31.0), 'Th5')
f.text(*P(11.0, 57.4), 'Th6')
f.add('</g>')

# ======================================================================= wstawka: przekrój czołowy stawu głowy żebra VI
SI = 2.0
IX, IY = 81.0, 78.0          # punkt (u=0, v=0): boczna powierzchnia trzonów na wysokości środka krążka
U0, U1, V0, V1 = -10.0, 14.0, -8.6, 8.6


def Q(u, v):
    return (IX + u * SI, IY + v * SI)


def QT(pts):
    return [Q(u, v) for u, v in pts]


qx0, qy0 = Q(U0, V0)
qx1, qy1 = Q(U1, V1)
f.add(f'<defs><clipPath id="cp_zkb_ins"><rect x="{qx0:.2f}" y="{qy0:.2f}" width="{qx1 - qx0:.2f}" height="{qy1 - qy0:.2f}" rx="2.2"/></clipPath></defs>')
f.add('<g clip-path="url(#cp_zkb_ins)">')
HD = 2.0                     # połowa grubości krążka
A1, A2 = (-3.6, -HD), (0.3, -6.2)          # ściana górna panewki (dołek żebrowy dolny Th5)
B1, B2 = (-3.6, HD), (0.3, 6.2)            # ściana dolna panewki (dołek żebrowy górny Th6)
# trzony (powierzchnia przekroju) i krążek
th5 = [(-30, -30), (0.0, -30), (0.25, -18), (-0.15, -11), A2, A1, (-30, -HD)]
th6 = [(-30, HD), B1, B2, (-0.15, 11), (0.25, 18), (0.0, 30), (-30, 30)]
f.add(f'<path class="bone2" d="{poly(QT(th5))}"/>')
f.add(f'<path class="bone2" d="{poly(QT(th6))}"/>')
f.add(f'<path class="annulus" d="{poly(QT([(-30, -HD), A1, (-3.4, 0), B1, (-30, HD)]))}"/>')
for v in (-1.1, 1.1):        # blaszki pierścienia włóknistego
    f.add(f'<path class="bonel" d="{line(QT([(-9.4, v * 0.95), (-6.5, v), (-4.2, v * 0.9)]))}"/>')


def along(p, q, s, n):
    """punkt na odcinku p→q w ułamku s, przesunięty o n wzdłuż normalnej (w stronę wnętrza panewki = ku bokowi)"""
    dx, dy = q[0] - p[0], q[1] - p[1]
    L = math.hypot(dx, dy)
    nx, ny = dy / L, -dx / L
    if nx < 0:
        nx, ny = -nx, -ny
    return (p[0] + dx * s + nx * n, p[1] + dy * s + ny * n)


def band(p, q, n0, n1, s0=0.0, s1=1.0):
    a = [along(p, q, s0 + (s1 - s0) * k / 8, n0) for k in range(9)]
    b = [along(p, q, s0 + (s1 - s0) * k / 8, n1) for k in range(9)]
    return poly(QT(a + b[::-1]))


# chrząstka stawowa na trzonach, jamy stawowe, chrząstka głowy żebra
for p, q in ((A1, A2), (B1, B2)):
    f.add(f'<path class="facet" d="{band(p, q, 0.0, 0.5, 0.06, 1.0)}"/>')
    f.add(f'<path class="cavity" d="{band(p, q, 0.5, 0.82, 0.30, 1.0)}"/>')
# głowa i szyjka żebra (przekrój)
cr_u = -1.8                  # grzebień głowy
hu = along(A1, A2, 0.30, 0.82)
hl = along(B1, B2, 0.30, 0.82)
ue = along(A1, A2, 1.0, 0.82)
le = along(B1, B2, 1.0, 0.82)
head = ([(cr_u, -0.62), hu] + [along(A1, A2, s, 0.82) for s in (0.5, 0.7, 0.9)] + [ue, (ue[0] + 1.4, ue[1] - 0.55), (4.6, -6.9),
        (7.4, -5.6), (10.5, -4.6), (14.0, -4.2), (16.0, -4.1), (16.0, 3.9), (14.0, 4.0), (10.5, 4.4), (7.4, 5.4), (4.6, 6.7),
        (le[0] + 1.4, le[1] + 0.55), le] + [along(B1, B2, s, 0.82) for s in (0.9, 0.7, 0.5)] + [hl, (cr_u, 0.62)])
f.add(f'<path class="bone2" d="{poly(QT(head))}"/>')
for p, q in ((A1, A2), (B1, B2)):
    f.add(f'<path class="facet" d="{band(p, q, 0.82, 1.28, 0.30, 1.0)}"/>')
# więzadło śródstawowe: od grzebienia głowy do krążka
f.add(f'<path class="lig" d="{poly(QT([(-3.45, -0.72), (cr_u + 0.05, -0.62), (cr_u + 0.05, 0.62), (-3.45, 0.72), (-3.36, 0)]))}"/>')
for v in (-0.3, 0.0, 0.3):
    f.add(f'<path class="bonel" d="{line(QT([(-3.3, v * 1.1), (cr_u - 0.1, v)]))}"/>')
# torebka stawowa (z przodu i z tyłu przekroju nie widać – tu jej górny i dolny odcinek)
f.add(f'<path class="capsule" d="{smooth(QT([(-0.1, -8.0), (1.6, -8.4), (3.6, -7.9), (5.0, -6.9)]), closed=False)}"/>')
f.add(f'<path class="capsule" d="{smooth(QT([(-0.1, 8.0), (1.6, 8.4), (3.6, 7.9), (5.0, 6.7)]), closed=False)}"/>')
f.text(*Q(-8.8, -6.4), 'Th5')
f.text(*Q(-8.6, 6.0), 'Th6')
f.add('</g>')
f.text(IX + (U0 + U1) / 2 * SI, qy0 - 1.6, 'przekrój czołowy stawu głowy żebra VI (widok od przodu)', cls='notec')

# ======================================================================= podpisy
TL, TR = 45.0, 101.2
f.label(P(20.8, 16.3), 'dołek żebrowy dolny', 'fovea costalis inferior', (TL, 4.0), side='L')
f.label(P(-0.9, 25.0), 'więzadło podłużne przednie', 'ligamentum longitudinale anterius', (TL, 13.5), side='L')
f.label(P(20.8, 24.6), 'dołek żebrowy górny', 'fovea costalis superior', (TL, 22.0), side='L')
f.label(P(5.0, 33.5), 'trzon kręgu', 'corpus vertebrae', (TL, 30.5), side='L')
f.label(P(11.0, 36.8), 'więzadło promieniste głowy żebra', 'ligamentum capitis costae radiatum', (TL, 39.0), side='L')
f.label(P(3.6, 43.6), 'krążek międzykręgowy', 'discus intervertebralis', (TL, 47.5), side='L')

f.label(P(38.0, 27.6), 'wyrostek poprzeczny', 'processus transversus', (TR, 17.0), side='R')
f.label(P(37.4, 38.2), 'więzadło żebrowo-poprzeczne górne', 'ligamentum costotransversarium superius', (TR, 29.0), side='R')

# wstawka
TLI, TRI = 58.5, 112.0
f.label(Q(*along(A1, A2, 0.62, 0.66)), 'jama stawowa', 'cavitas articularis', (TLI, 66.5), side='L')
f.label(Q(-2.7, 0.15), 'więzadło śródstawowe głowy żebra', 'ligamentum capitis costae intraarticulare', (TLI, 82.0), side='L')
f.label(Q(cr_u + 0.45, -0.25), 'grzebień głowy', 'crista capitis', (TRI, 70.0), side='R')
f.label(Q(6.5, 1.6), 'głowa żebra', 'caput costae', (TRI, 82.0), side='R')
f.save()
