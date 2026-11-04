# Kość krzyżowa z kręgiem L5 i kością guziczną – widok z boku (od strony lewej; przód w lewo), ustawienie jak w postawie
# pionowej. Schemat własny. Nazwy wg Bochenka, t. I: s. 232–236 (kształt, kifoza krzyżowa, kąt lędźwiowo-krzyżowy, wzgórek,
# podstawa, wierzchołek, powierzchnie miedniczna i grzbietowa, powierzchnia uchowata, guzowatość krzyżowa, wyrostki stawowe
# górne), ryc. 147 (s. 235), streszczenie s. 249 (wierzchołek kąta leży na krążku L5/S1, tj. na wzgórku), ryc. 347 (s. 538).
# Lista podpisów: k_kregoslup.json, karta „Kształt i położenie kości krzyżowej” (+ powierzchnia uchowata i guzowatość
# krzyżowa z karty „Części boczne kości krzyżowej”, która nie ma osobnego rysunku).
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 150, 108
S = 0.55                  # mm rysunku / mm kości
X0, Y0 = 68.0, 34.5       # położenie środka powierzchni górnej trzonu S1 na rysunku

f = Fig('kr_sacrum_bok', W, H, caption='kość krzyżowa z L5 i kością guziczną · widok z boku (od strony lewej, przód w lewo)')

# ======================= oś kości krzyżowej i guzicznej (mm kości; x – do tyłu, y – w dół) =======================
SAC_LEN = 104.0
KEYS = [(0, 46), (30, 38), (60, 22), (85, 4), (104, -12), (118, -26), (140, -46)]   # (s, θ) – θ: odchylenie osi od pionu


def theta(s):
    if s <= KEYS[0][0]:
        return math.radians(KEYS[0][1])
    for (a, ta), (b, tb) in zip(KEYS, KEYS[1:]):
        if s <= b:
            t = (s - a) / (b - a); t = t * t * (3 - 2 * t)
            return math.radians(ta + (tb - ta) * t)
    return math.radians(KEYS[-1][1])


DS = 0.25
AX = [(0.0, 0.0)]
for k in range(int(150 / DS)):
    th = theta(k * DS); x, y = AX[-1]
    AX.append((x + math.sin(th) * DS, y + math.cos(th) * DS))


def frame(s):
    th = theta(s)
    u, n = (math.sin(th), math.cos(th)), (math.cos(th), -math.sin(th))      # u – w dół wzdłuż osi, n – do tyłu
    if s < 0:
        c = (s * u[0], s * u[1])
    else:
        k = min(len(AX) - 2, int(s / DS)); t = s / DS - k
        c = (AX[k][0] + (AX[k + 1][0] - AX[k][0]) * t, AX[k][1] + (AX[k + 1][1] - AX[k][1]) * t)
    return c, u, n


def Dsac(s):                                   # głębokość (przednio-tylna) trzonów
    t = min(1.0, max(0.0, s / SAC_LEN))
    return 31.0 - 17.0 * t


def SP(s, p):
    """punkt kości krzyżowej: s – wzdłuż osi od powierzchni górnej S1, p – od powierzchni miednicznej ku tyłowi"""
    c, u, n = frame(s)
    a = p - Dsac(s) / 2
    return (c[0] + a * n[0], c[1] + a * n[1])


def CP(s, q):
    """punkt kości guzicznej: q – odsunięcie od osi (+ do tyłu)"""
    c, u, n = frame(s)
    return (c[0] + q * n[0], c[1] + q * n[1])


def G(pt):                                     # mm kości → rysunek
    return (X0 + pt[0] * S, Y0 + pt[1] * S)


def GL(pts):
    return [G(p) for p in pts]


# ======================= kręg L5 (układ własny: x do tyłu od przedniej powierzchni trzonu, y w dół) =======================
PHI = math.radians(26.0)                       # nachylenie dolnej powierzchni trzonu L5 (tył wyżej)
A = SP(0, 0)                                   # przedni brzeg powierzchni górnej S1
B = SP(0, 31)                                  # tylny brzeg powierzchni górnej S1
MID = math.radians(36.0)
A5 = (A[0] - 16.5 * math.sin(MID), A[1] - 16.5 * math.cos(MID))    # przedni-dolny róg trzonu L5 (krążek z przodu ~16,5 mm)


def L5(x, y):
    yy = y - 28.5
    return (A5[0] + x * math.cos(PHI) + yy * math.sin(PHI), A5[1] - x * math.sin(PHI) + yy * math.cos(PHI))


L5O = [(4.6, 0.3), (13, 1.1), (22, 2.3), (31, 3.6), (34.6, 4.4),                      # powierzchnia górna trzonu (klin)
       (36.2, 5.6), (38.2, 7.0), (40.2, 6.4), (41.2, 3.2),                              # wcięcie kręgowe górne
       (42.0, -1.0), (43.0, -5.6), (44.8, -8.6), (47.2, -9.4), (49.4, -8.6), (50.6, -6.2), (51.0, -4.0),   # wyr. stawowy górny
       (53.0, -3.2), (54.8, -1.0), (55.0, 1.8), (53.8, 4.0),                            # wyrostek suteczkowaty
       (55.0, 6.4), (59.6, 8.6), (65.0, 11.0), (70.4, 13.6), (73.6, 15.0),              # blaszka → wyrostek kolczysty
       (75.8, 17.2), (76.4, 21.0), (75.6, 24.8), (73.4, 26.6),
       (69.0, 26.0), (64.6, 24.6), (61.2, 24.4),
       (59.4, 26.4), (58.6, 29.6), (57.4, 32.6), (55.6, 35.0), (53.4, 36.0), (51.2, 35.2),  # wyrostek stawowy dolny
       (49.6, 32.8), (48.6, 29.2), (47.8, 25.6), (46.6, 22.4),
       (44.8, 19.8), (42.2, 18.4), (39.4, 18.2), (36.8, 19.4), (35.2, 21.8),             # wcięcie kręgowe dolne
       (34.4, 24.6), (34.0, 28.0), (26, 28.7), (16, 28.9), (8, 28.8), (1.0, 28.4),     # powierzchnia dolna trzonu
       (0.2, 26.6), (1.3, 20.0), (2.8, 13.0), (3.4, 6.0), (3.8, 1.4)]
f.add(f'<path class="bone" d="{smooth(GL([L5(x, y) for x, y in L5O]))}"/>')
# listewki brzeżne trzonu
f.add(f'<path class="bonel" d="{smooth(GL([L5(x, y) for x, y in [(5.0, 1.9), (14, 2.7), (23, 3.8), (33.6, 5.6)]]), closed=False)}"/>')
f.add(f'<path class="bonel" d="{smooth(GL([L5(x, y) for x, y in [(1.4, 26.8), (12, 27.2), (24, 27.2), (33.6, 26.6)]]), closed=False)}"/>')
# wyrostek poprzeczny – krótki i silny, widoczny od strony końca
tp = [L5(x, y) for x, y in [(40.2, 6.6), (43.6, 3.4), (48.0, 3.0), (51.4, 5.2), (52.4, 9.4), (51.4, 13.4), (48.0, 15.6),
                             (43.8, 15.4), (40.8, 12.6), (39.8, 9.4)]]
f.add(f'<path class="bone" d="{smooth(GL(tp))}"/>')
f.add(f'<path class="bonel" d="{smooth(GL([L5(x, y) for x, y in [(42.6, 11.8), (45.4, 13.6), (49.0, 13.0)]]), closed=False)}"/>')
# powierzchnia stawowa wyrostka stawowego dolnego L5 (wypukła, zwrócona do przodu) – staw z wyrostkiem stawowym górnym S1
fi = [L5(x, y) for x, y in [(47.6, 24.6), (48.4, 28.8), (49.4, 32.4), (51.0, 34.8), (52.6, 35.6), (52.0, 33.0), (51.0, 29.6),
                             (50.3, 26.2), (49.7, 23.4)]]
f.add(f'<path class="facet" d="{smooth(GL(fi))}"/>')
# zgrubiały koniec wyrostka kolczystego
f.add(f'<path class="bonel" d="{smooth(GL([L5(x, y) for x, y in [(73.0, 17.4), (73.8, 21.0), (73.0, 24.0)]]), closed=False)}"/>')

# ======================= kość krzyżowa (zarys w układzie s, p) =======================
POST = [(13.0, 49.2), (16, 48.6), (21, 45.6), (26, 43.6), (31, 43.8), (35, 41.6), (41, 37.4), (46, 35.6), (50, 35.4),
        (54, 33.4), (60, 29.6), (64, 28.0), (68, 27.4), (72, 25.4), (78, 22.4)]          # grzebień pośrodkowy (4 guzki)
LOW = [(83, 20.0), (88, 18.6), (93, 17.8)]
OUT = ([(0.0, 0.2), (-0.4, 8), (-0.6, 16), (-0.6, 24), (-0.2, 30.6), (1.4, 32.6),            # pow. górna S1 (pod krążkiem)
        (-2.0, 33.6), (-7.0, 34.6), (-11.6, 36.0), (-14.0, 39.0), (-13.4, 43.2), (-10.4, 45.8),   # wyrostek stawowy górny
        (-6.0, 46.8), (-2.0, 46.8), (2.0, 46.6), (6.0, 46.8), (9.0, 47.4), (11.2, 48.6)]       # (za nim wyr. stawowy dolny L5)
       + POST + LOW +
       [(97.6, 17.6), (100.6, 16.6), (101.4, 14.6),                                             # rożek krzyżowy
        (100.0, 12.6), (102.6, 11.2), (104.4, 8.4), (104.6, 4.0), (104.0, 0.4),                  # wierzchołek
        (96.0, -0.4), (86.0, -0.2), (74.0, 0.1), (60.0, 0.2), (46.0, 0.0), (32.0, -0.2), (18.0, 0.2), (8.0, 0.4),
        (3.0, -0.2)])
sac = [SP(s, p) for s, p in OUT]
f.add(f'<path class="bone" d="{smooth(GL(sac))}"/>')

# pas powierzchni grzbietowej (uciekającej ku tyłowi) – cień między grzebieniem krzyżowym bocznym a pośrodkowym
LCR = [(22, 41.6), (28, 39.4), (34, 37.2), (40, 34.4), (46, 31.8), (52, 29.6), (58, 27.0), (64, 24.6), (70, 22.6),
       (76, 20.4), (82, 18.2), (88, 16.6), (94, 15.8)]
band = [SP(s, p) for s, p in LCR] + [SP(s, p) for s, p in reversed([q for q in POST if q[0] >= 21] + LOW)]
f.add(f'<path class="shade" d="{smooth(GL(band))}"/>')
f.add(f'<path class="bonel" d="{smooth(GL([SP(s, p) for s, p in LCR]), closed=False)}"/>')

# guzowatość krzyżowa – chropowate pole ku tyłowi od powierzchni uchowatej
TUB = [(2.4, 30.4), (0.6, 35.4), (0.4, 41.0), (1.6, 45.0), (5.0, 46.0), (9.6, 46.4), (14.4, 45.0), (19.6, 41.4),
       (25.0, 37.2), (29.6, 31.6), (28.4, 26.8), (22.4, 24.2), (15.6, 24.4), (10.8, 27.6), (6.0, 29.6)]
f.add(f'<path class="shade" d="{smooth(GL([SP(s, p) for s, p in TUB]))}"/>')
STR = [(3.4, 34.6, 30), (2.6, 40.2, -40), (4.2, 45.2, 60), (7.8, 33.2, -20), (7.4, 38.6, 45), (8.6, 43.8, -60),
       (12.2, 31.4, 70), (12.2, 36.8, -10), (12.8, 42.0, 35), (16.6, 29.6, -50), (16.8, 34.6, 20), (17.6, 39.6, 55),
       (21.2, 28.6, -30), (21.8, 33.4, 10), (25.6, 30.2, -70), (25.2, 35.4, 40)]
for s, p, r in STR:
    x, y = G(SP(s, p))
    dx, dy = 0.42 * math.cos(math.radians(r)), 0.42 * math.sin(math.radians(r))
    f.add(f'<path class="bonel" d="M{x - dx:.2f},{y - dy:.2f} L{x + dx:.2f},{y + dy:.2f}"/>')

# powierzchnia uchowata – kształt ucha: krótkie ramię górne (do tyłu), długie dolne (ku dołowi i do tyłu), kąt zwrócony do przodu
AUR = [(17.0, 3.6), (11.0, 4.4), (5.6, 6.4), (2.6, 10.6), (1.6, 16.6), (2.0, 23.0), (3.8, 27.6), (7.0, 29.2), (10.0, 27.6),
       (12.4, 23.0), (15.4, 18.0), (19.6, 15.4), (25.0, 15.8), (31.0, 18.6), (37.4, 21.8), (43.2, 24.2), (47.4, 23.8),
       (48.6, 20.6), (46.0, 16.4), (41.0, 12.6), (34.6, 9.0), (28.0, 6.4), (22.0, 4.4)]
f.add(f'<path class="facet" d="{smooth(GL([SP(s, p) for s, p in AUR]))}"/>')

# ======================= krążek L5/S1 =======================
disc = [A, L5(0, 28.5), L5(34.0, 28.0), B]
DA = G(A); DA5 = G(L5(0, 28.5)); DB5 = G(L5(34.0, 28.0)); DB = G(B)
mf = ((DA[0] + DA5[0]) / 2 - 1.8, (DA[1] + DA5[1]) / 2 + 0.2)          # przednia krawędź krążka wpukla się do przodu
mb = ((DB[0] + DB5[0]) / 2 + 0.5, (DB[1] + DB5[1]) / 2)
f.add(f'<path class="annulus" d="M{DA[0]:.2f},{DA[1]:.2f} Q{mf[0] * 2 - (DA[0] + DA5[0]) / 2:.2f},{mf[1] * 2 - (DA[1] + DA5[1]) / 2:.2f} '
      f'{DA5[0]:.2f},{DA5[1]:.2f} L{DB5[0]:.2f},{DB5[1]:.2f} Q{mb[0] * 2 - (DB[0] + DB5[0]) / 2:.2f},{mb[1] * 2 - (DB[1] + DB5[1]) / 2:.2f} '
      f'{DB[0]:.2f},{DB[1]:.2f} Z"/>')
PROM = mf                                     # wzgórek – najbardziej do przodu wysunięta krawędź krążka

# ======================= kość guziczna =======================
CO = [(106.4, 8.6, 12.0), (116.6, 6.6, 9.4), (124.6, 5.4, 7.6), (130.0, 4.6, 6.0)]     # Co3 i Co4 zrośnięte     # (s górne, wysokość, głębokość)
# chrząstkozrost krzyżowo-guziczny
a1, a2 = CP(104.3, -6.8), CP(104.3, 5.0)
b1, b2 = CP(106.4, -5.6), CP(106.4, 5.0)
f.add(f'<path class="cart" d="{smooth(GL([a1, a2, b2, b1]), t=0.2)}"/>')
for i, (s0, hh, dd) in enumerate(CO):
    s1 = s0 + hh
    pts = [CP(s0, -dd / 2 + 0.6), CP(s0 - 0.2, 0), CP(s0, dd / 2 - 0.6), CP(s0 + 0.8, dd / 2), CP((s0 + s1) / 2, dd / 2 - 0.5),
           CP(s1 - 0.8, dd / 2), CP(s1, dd / 2 - 0.8), CP(s1 + 0.2, 0), CP(s1, -dd / 2 + 0.8), CP(s1 - 0.8, -dd / 2),
           CP((s0 + s1) / 2, -dd / 2 + 0.5), CP(s0 + 0.8, -dd / 2)]
    if i == 0:   # Co1 z rożkiem guzicznym (ku górze, do rożka krzyżowego)
        pts = [CP(s0 + 0.2, -5.4), CP(s0, 0), CP(s0 + 0.2, 4.4), CP(s0 - 1.2, 5.2), CP(s0 - 3.4, 5.8), CP(s0 - 4.4, 7.0),
               CP(s0 - 4.0, 8.4), CP(s0 - 2.2, 8.8), CP(s0 + 0.6, 8.2), CP(s0 + 3.2, 6.8), CP(s0 + 6.0, 6.0),
               CP(s1 - 0.6, 5.2), CP(s1, 2.0), CP(s1 + 0.2, -1.0), CP(s1, -4.4), CP(s1 - 1.6, -6.0), CP(s0 + 4.2, -6.2),
               CP(s0 + 1.2, -6.0)]
    f.add(f'<path class="bone" d="{smooth(GL(pts), t=0.55)}"/>')
for s0, s1 in ((115.0, 116.6), (123.2, 124.6)):
    pts = [CP(s0, -3.4), CP(s0, 3.4), CP(s1, 3.0), CP(s1, -3.0)]
    f.add(f'<path class="cart" d="{smooth(GL(pts), t=0.2)}"/>')

# ======================= kąt lędźwiowo-krzyżowy (ryc. 347: wierzchołek na wzgórku) =======================
uL = (L5(3.8, 1.4)[0] - L5(0.2, 26.6)[0], L5(3.8, 1.4)[1] - L5(0.2, 26.6)[1])
nl = math.hypot(*uL); uL = (uL[0] / nl, uL[1] / nl)                       # kierunek przedniej powierzchni L5 (ku górze)
q1, q2 = SP(10, 0), SP(46, 0)
uS = (q2[0] - q1[0], q2[1] - q1[1]); ns = math.hypot(*uS); uS = (uS[0] / ns, uS[1] / ns)   # pow. miedniczna S1–S2
V = PROM
R1, R2 = 50.0 * S, 24.0 * S
e1 = (V[0] + uL[0] * R1, V[1] + uL[1] * R1)
e2 = (V[0] + uS[0] * R2, V[1] + uS[1] * R2)
f.add(f'<path class="dim" d="M{e1[0]:.2f},{e1[1]:.2f} L{V[0]:.2f},{V[1]:.2f} L{e2[0]:.2f},{e2[1]:.2f}"/>')
RA = 6.0 * S
a_1 = (V[0] + uL[0] * RA, V[1] + uL[1] * RA); a_2 = (V[0] + uS[0] * RA, V[1] + uS[1] * RA)
f.add(f'<path class="lead" d="M{a_1[0]:.2f},{a_1[1]:.2f} A{RA:.2f},{RA:.2f} 0 0 1 {a_2[0]:.2f},{a_2[1]:.2f}"/>')
ang = math.degrees(math.acos(uL[0] * uS[0] + uL[1] * uS[1]))

# oznaczenie kręgu L5
c5 = G(L5(17, 15.5)); f.text(c5[0], c5[1] + 0.8, 'L5', cls='notec')

# ======================= kifoza krzyżowa – klamra po stronie wypukłej (tylnej) =======================
BR = [(46, 35.6), (54, 33.4), (62, 29.0), (70, 26.4), (78, 22.4), (86, 19.4), (94, 17.6), (100, 16.4)]
OFF = 6.5
br = [SP(s_, p_ + OFF) for s_, p_ in BR] + [CP(s_, q_ + OFF) for s_, q_ in [(108, 7.4), (116, 4.4), (124, 2.0), (129, 0.4), (132.0, -0.6)]]
brg = GL(br)
d = smooth(brg, closed=False)
t0a, t0b = G(SP(46, 35.6 + OFF)), G(SP(46, 35.6 + OFF - 5.0))
t1a, t1b = G(CP(132.0, -0.6 + OFF)), G(CP(132.0, -0.6 + OFF - 3.0))
d += f' M{t0a[0]:.2f},{t0a[1]:.2f} L{t0b[0]:.2f},{t0b[1]:.2f} M{t1a[0]:.2f},{t1a[1]:.2f} L{t1b[0]:.2f},{t1b[1]:.2f}'
f.add(f'<path class="lead" d="{d}"/>')
KM = G(SP(78, 22.4 + OFF))

# ======================= podpisy =======================
TL, TR = 47.0, 104.0
def note(x, y, t, side):
    f.text(x + (0.7 if side == 'R' else -0.7), y, t, cls='note', anchor='start' if side == 'R' else 'end')

f.label(a_1, 'kąt lędźwiowo-krzyżowy', 'angulus lumbosacralis', (TL, 22.0), side='L')
note(TL, 22.0 + 6.4, '120–170°', 'L')
f.label(V, 'wzgórek', 'promontorium', (TL, 36.0), side='L')
f.label(G(SP(40, 15.0)), 'powierzchnia uchowata', 'facies auricularis', (TL, 49.0), side='L')
f.label(G(SP(62, 0.2)), 'powierzchnia miedniczna', 'facies pelvina', (TL, 61.0), side='L')
f.label(G(SP(102.4, 2.2)), 'wierzchołek kości krzyżowej', 'apex ossis sacri', (TL, 74.0), side='L')
f.label(G(CP(120.0, -3.6)), 'kość guziczna', 'os coccygis', (TL, 88.0), side='L')

f.label(G(SP(2.0, 31.0)), 'podstawa kości krzyżowej', 'basis ossis sacri', (TR, 24.0), side='R')
f.label(G(SP(13.0, 38.0)), 'guzowatość krzyżowa', 'tuberositas sacralis', (TR, 32.0), side='R')
f.label(G(SP(29.0, 41.6)), 'powierzchnia grzbietowa', 'facies dorsalis', (TR, 40.0), side='R')
f.label(KM, 'kifoza krzyżowa', 'kyphosis sacralis', (TR, 66.0), side='R')
note(TR, 66.0 + 6.4, 'wypukłość ku tyłowi', 'R')
f.save()
