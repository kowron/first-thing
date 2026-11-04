# Kość guziczna – widok od przodu (A) oraz widok z boku (od strony lewej, przód w lewo) razem z dolnym odcinkiem kości
# krzyżowej (B): połączenie rożków guzicznych z rożkami krzyżowymi i chrząstkozrost krzyżowo-guziczny. Schemat własny.
# Nazwy wg Bochenka, t. I: s. 237 (kość guziczna, ryc. 149 – widok od przodu: cornu coccygeum, processus transversus),
# s. 235 (rożki krzyżowe; ryc. 147 – cornu sacrale, cornu coccygeum), s. 218 (chrząstkozrost – synchondrosis), s. 249.
# Lista podpisów: k_kregoslup.json, karta „Kość guziczna”.
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth, mirror

W, H = 150, 71
K = 1.3                     # mm rysunku / mm kości (oba widoki w tej samej skali)

f = Fig('kr_coccyx', W, H, caption='kość guziczna · A – widok od przodu · B – widok z boku (od strony lewej, przód w lewo)')

# ======================================= A. WIDOK OD PRZODU =======================================
CXF, YF = 60.0, 22.0         # oś symetrii, poziom powierzchni górnej Co1 (podstawy)
def F(x, y): return (CXF + x * K, YF + y * K)
def FL(pts): return [F(x, y) for x, y in pts]

# rożki guziczne – wyrostki stawowe górne Co1, sterczą ku górze za podstawą (widoczne ponad nią)
for sg in (-1, 1):
    corn = [(sg * x, y) for x, y in [(3.6, 0.6), (3.4, -2.6), (3.0, -5.4), (3.2, -7.4), (4.4, -8.4), (5.8, -8.0),
                                      (6.6, -6.2), (6.8, -3.4), (7.0, -0.6), (6.6, 1.6)]]
    f.add(f'<path class="bone" d="{smooth(FL(corn))}"/>')
    f.add(f'<path class="shade" d="{smooth(FL([(sg * x, y) for x, y in [(3.7, 0.4), (3.5, -2.6), (3.2, -5.6), (4.3, -5.0), (4.6, -2.2), (4.8, 0.6)]]))}"/>')
# łączna linia tylnego brzegu powierzchni górnej między rożkami (dno „litery U”)
f.add(f'<path class="bonel" d="{smooth(FL([(-3.6, -0.2), (-1.8, -1.0), (0, -1.2), (1.8, -1.0), (3.6, -0.2)]), closed=False)}"/>')

# Co1 – trzon z szczątkowymi wyrostkami poprzecznymi (połowa lewa rysunku + odbicie)
CO1 = [(0, -0.4), (-3.8, -0.4), (-6.0, 0.0), (-6.8, 0.8),
       (-8.6, 0.8), (-10.6, 1.0), (-12.0, 2.0), (-12.4, 3.6), (-11.6, 5.2), (-9.8, 5.8), (-7.8, 5.4),   # wyrostek poprzeczny
       (-6.6, 6.2), (-5.8, 8.0), (-5.4, 9.2), (-3.0, 9.6)]
co1 = CO1 + [(0, 9.7)] + mirror(CO1, 0)[:-1]
f.add(f'<path class="bone" d="{smooth(FL(co1))}"/>')
for sg in (-1, 1):   # cień pod wyrostkiem poprzecznym
    f.add(f'<path class="shade" d="{smooth(FL([(sg * x, y) for x, y in [(-7.2, 5.6), (-9.6, 5.8), (-11.4, 5.0), (-12.2, 3.6), (-11.0, 4.4), (-9.0, 4.6)]]))}"/>')
# podstawa kości guzicznej – owalna powierzchnia górna Co1 (widziana nieco od góry)
x, y = F(0, 0.4)
f.add(f'<ellipse class="bone2" cx="{x:.2f}" cy="{y:.2f}" rx="{5.6 * K:.2f}" ry="{1.25 * K:.2f}"/>')

# chrząstkozrosty Co1–Co2 i Co2–Co3 (dalsze połączenia skostniałe)
for y0, y1, w0, w1 in ((9.5, 10.9, 5.0, 4.6), (17.5, 18.6, 3.9, 3.5)):
    f.add(f'<path class="cart" d="{smooth(FL([(-w0, y0), (w0, y0), (w1, y1), (-w1, y1)]), t=0.15)}"/>')
# Co2, Co3 + Co4 (zrośnięte) – szczątkowe trzony
CO2 = [(0, 10.6), (-4.4, 10.7), (-4.9, 11.6), (-4.6, 13.6), (-4.3, 15.8), (-4.0, 17.4), (-2.0, 17.8)]
f.add(f'<path class="bone" d="{smooth(FL(CO2 + [(0, 17.9)] + mirror(CO2, 0)[:-1]))}"/>')
CO34 = [(0, 18.4), (-3.4, 18.5), (-3.8, 19.4), (-3.5, 21.6), (-3.1, 23.3), (-2.8, 23.8),     # Co3
        (-2.9, 24.5), (-2.6, 26.0), (-1.9, 27.4), (-0.9, 28.1)]                               # Co4 → wierzchołek
f.add(f'<path class="bone" d="{smooth(FL(CO34 + [(0, 28.3)] + mirror(CO34, 0)[:-1]))}"/>')
f.add(f'<path class="bonel" d="{smooth(FL([(-2.8, 23.9), (-1.0, 24.3), (1.0, 24.3), (2.8, 23.9)]), closed=False)}"/>')  # ślad zrostu Co3/Co4

for t, yy in (('Co1', 7.6), ('Co2', 15.8), ('Co3', 22.2), ('Co4', 27.0)):
    xx, yp = F(0, yy); f.text(xx, yp, t, cls='notec')
xa, ya = F(0, 31.6); f.text(xa, ya, 'A · od przodu', cls='notec')

# ======================================= B. WIDOK Z BOKU =======================================
# oś kości krzyżowej i guzicznej – ta sama geometria co w figs/src/kr_sacrum_bok.py (ustawienie jak w postawie pionowej)
SAC_LEN = 104.0
KEYS = [(0, 46), (30, 38), (60, 22), (85, 4), (104, -12), (118, -26), (140, -46)]


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
    u, n = (math.sin(th), math.cos(th)), (math.cos(th), -math.sin(th))
    k = min(len(AX) - 2, int(s / DS)); t = s / DS - k
    return (AX[k][0] + (AX[k + 1][0] - AX[k][0]) * t, AX[k][1] + (AX[k + 1][1] - AX[k][1]) * t), u, n


def SP(s, p):                 # kość krzyżowa: p – od powierzchni miednicznej ku tyłowi
    c, u, n = frame(s); a = p - (31.0 - 17.0 * min(1.0, s / SAC_LEN)) / 2
    return (c[0] + a * n[0], c[1] + a * n[1])


def CP(s, q):                 # kość guziczna: q – od osi ku tyłowi
    c, u, n = frame(s)
    return (c[0] + q * n[0], c[1] + q * n[1])


REF = SP(104.0, 0.0)          # punkt odniesienia: przedni brzeg wierzchołka kości krzyżowej
XB, YB = 93.0, 26.0          # jego położenie na rysunku
def B(pt): return (XB + (pt[0] - REF[0]) * K, YB + (pt[1] - REF[1]) * K)
def BL(pts): return [B(p) for p in pts]

S_CUT = 90.0
LOW = [(S_CUT, 19.2), (92, 18.8), (95.2, 18.6), (98.2, 18.8), (100.8, 18.2), (102.0, 16.4),   # rożek krzyżowy
       (101.6, 14.2), (100.2, 12.8),                                                                      # wcięcie
       (100.8, 11.4), (102.8, 10.4), (104.2, 8.0), (104.8, 4.4), (104.4, 1.0), (103.2, -0.2),              # wierzchołek
       (98.0, -0.3), (92.0, -0.2), (S_CUT, 0.0)]
# przełamanie (kość krzyżowa narysowana tylko w dolnym odcinku) – falista linia
BRK = [(S_CUT + 0.6 * math.sin(i * 1.3), i * 19.2 / 8) for i in range(9)]
sac = BL([SP(s, p) for s, p in LOW + BRK[1:-1]])
f.add(f'<path class="bone" d="{smooth(sac, t=0.4)}"/>')
# pas powierzchni grzbietowej (ku tyłowi) – grzebień krzyżowy boczny
LCR = [(S_CUT + 0.4, 16.2), (92, 15.8), (95.4, 15.6)]
band = [SP(s, p) for s, p in LCR] + [SP(s, p) for s, p in [(95.2, 18.6), (92, 18.8), (S_CUT + 0.4, 19.2)]]
f.add(f'<path class="shade" d="{smooth(BL(band))}"/>')
f.add(f'<path class="bonel" d="{smooth(BL([SP(s, p) for s, p in LCR]), closed=False)}"/>')

# chrząstkozrost krzyżowo-guziczny (wierzchołek kości krzyżowej ↔ podstawa kości guzicznej)
f.add(f'<path class="cart" d="{smooth(BL([CP(104.5, -6.9), CP(104.6, 5.0), CP(106.4, 4.6), CP(106.5, -5.8)]), t=0.15)}"/>')
# Co1 z rożkiem guzicznym
s0, s1 = 106.4, 115.0
co1 = [CP(s0 + 0.2, -5.4), CP(s0, 0), CP(s0 + 0.2, 4.4), CP(s0 - 1.2, 5.2), CP(s0 - 3.4, 5.8), CP(s0 - 4.4, 7.0),
       CP(s0 - 4.0, 8.4), CP(s0 - 2.2, 8.8), CP(s0 + 0.6, 8.2), CP(s0 + 3.2, 6.8), CP(s0 + 6.0, 6.0),
       CP(s1 - 0.6, 5.2), CP(s1, 2.0), CP(s1 + 0.2, -1.0), CP(s1, -4.4), CP(s1 - 1.6, -6.0), CP(s0 + 4.2, -6.2),
       CP(s0 + 1.2, -6.0)]
f.add(f'<path class="bone" d="{smooth(BL(co1), t=0.55)}"/>')
# chrząstkozrosty Co1–Co2, Co2–Co3
for a, b, w in ((115.0, 116.6, 4.0), (123.2, 124.6, 3.2)):
    f.add(f'<path class="cart" d="{smooth(BL([CP(a, -w), CP(a, w), CP(b, w - 0.3), CP(b, -w + 0.3)]), t=0.15)}"/>')


def seg(s0, s1, d0, d1):
    return [CP(s0, -d0 / 2 + 0.6), CP(s0 - 0.2, 0), CP(s0, d0 / 2 - 0.6), CP(s0 + 0.8, d0 / 2),
            CP((s0 + s1) / 2, (d0 + d1) / 4 - 0.4), CP(s1 - 0.8, d1 / 2), CP(s1, d1 / 2 - 0.8), CP(s1 + 0.2, 0),
            CP(s1, -d1 / 2 + 0.8), CP(s1 - 0.8, -d1 / 2), CP((s0 + s1) / 2, -(d0 + d1) / 4 + 0.4), CP(s0 + 0.8, -d0 / 2)]


f.add(f'<path class="bone" d="{smooth(BL(seg(116.6, 123.2, 9.4, 8.6)), t=0.55)}"/>')
co34 = [CP(124.6, -3.2), CP(124.4, 0), CP(124.6, 3.2), CP(125.6, 3.8), CP(128.6, 3.2), CP(130.0, 2.6), CP(131.8, 2.6),
        CP(133.8, 2.0), CP(135.2, 0.6), CP(135.4, -1.0), CP(134.4, -2.4), CP(131.6, -2.8), CP(129.8, -3.0),
        CP(127.6, -3.6), CP(125.4, -3.8)]
f.add(f'<path class="bone" d="{smooth(BL(co34), t=0.5)}"/>')
f.add(f'<path class="bonel" d="{smooth(BL([CP(130.0, 2.4), CP(129.9, 0), CP(129.8, -2.8)]), closed=False)}"/>')   # zrost Co3/Co4

xb, yb = B(SP(94.6, 9.4)); f.text(xb, yb + 0.8, 'kość krzyżowa', cls='notec')
xc, yc = B(CP(110.6, -0.6)); f.text(xc, yc + 0.8, 'Co1', cls='notec')
xa, ya = F(0, 31.6); f.text(110.0, ya, 'B · z boku', cls='notec')

# ======================================= podpisy =======================================
TL, TR = 40.5, 123.0
# A – od przodu
f.label(F(0, -0.9), 'podstawa kości guzicznej', None, (CXF + 1.6, 4.2), side='R')
f.label(F(-5.0, -5.2), 'rożki guziczne', 'cornua coccygea', (TL, 13.0), side='L')
f.label(F(-10.4, 3.2), 'wyrostek poprzeczny', 'processus transversus', (TL, 25.0), side='L')
f.label(F(-4.0, 10.2), 'chrząstkozrost', 'synchondrosis', (TL, 36.0), side='L')
f.text(TL - 0.7, 36.0 + 6.4, 'Co1–Co2, Co2–Co3; tak samo', cls='note', anchor='end')
f.text(TL - 0.7, 36.0 + 9.0, 'podstawa – wierzchołek k. krzyżowej', cls='note', anchor='end')
f.label(F(-0.8, 27.9), 'wierzchołek kości guzicznej', None, (TL, 57.0), side='L')
# B – z boku
f.label(B(SP(100.4, 17.2)), 'rożki krzyżowe', 'cornua sacralia', (TR, 21.0), side='R')
f.label(B(CP(103.0, 8.0)), 'rożki guziczne', 'cornua coccygea', (TR, 29.5), side='R')
f.save()
