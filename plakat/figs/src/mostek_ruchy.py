# RUCHY MOSTKA – żebro I i mostek w położeniu wydechu i wdechu, widok od strony lewej (przód w lewo).
# Schemat własny (idea jak ryc. 200/4 u Bochenka, t. I, s. 295–296 i 298).
# Ruchy mostka są bierne (zależą od ruchów żeber). W zasadzie przesunięcie równoległe ku górze i do przodu,
# nie „czyste” – dolne części mostka przesuwają się silniej do przodu niż górne (tu: przesunięcie + niewielki obrót
# mostka dołem do przodu; kość żebrowa I obraca się ku górze dokoła tylnego końca). Dodatkowo nieznaczny obrót rękojeści
# względem trzonu (lub odwrotnie) w chrząstkozroście
# górnym, dokoła osi poprzecznej przez przyczepy mostkowe żeber II – zmiana kąta mostka (we wdechu spłaszcza się).
# Wartości kąta mostka celowo pominięte (karta „Kąt mostka”). Więzadła mostkowo-mieczykowego (s. 295) nie rysujemy –
# w opisie połączeń (s. 287) i w streszczeniu (s. 298) są tylko więzadła żebrowo-mieczykowe.
# Kości w położeniu wydechu; linia przerywana – położenie wdechu; strzałki niebieskie – ruch przy wdechu.
import sys, math
sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 134, 101
f = Fig('mostek_ruchy', W, H, caption='żebro I i mostek przy wydechu i przy wdechu · widok od strony lewej (przód w lewo)')


# ---------------------------------------------------------------- narzędzia
def cr(pts, n=14, t=0.5):
    m = len(pts)
    Q = [pts[0]] + pts + [pts[-1]]
    out = []
    for i in range(1, m):
        p0, p1, p2, p3 = Q[i - 1], Q[i], Q[i + 1], Q[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) * t / 3, p1[1] + (p2[1] - p0[1]) * t / 3)
        c2 = (p2[0] - (p3[0] - p1[0]) * t / 3, p2[1] - (p3[1] - p1[1]) * t / 3)
        for k in range(n):
            u = k / n
            a, b, c, d = (1 - u) ** 3, 3 * u * (1 - u) ** 2, 3 * u * u * (1 - u), u ** 3
            out.append((a * p1[0] + b * c1[0] + c * c2[0] + d * p2[0], a * p1[1] + b * c1[1] + c * c2[1] + d * p2[1]))
    out.append(pts[-1])
    return out


def poly(pts, close=True):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + (' Z' if close else '')


def unit(v):
    L = math.hypot(*v) or 1.0
    return (v[0] / L, v[1] / L)


def add(a, b, k=1.0):
    return (a[0] + b[0] * k, a[1] + b[1] * k)


def rot(p, o, deg):
    """obrót punktu p wokół o; deg > 0 – zgodnie z ruchem wskazówek zegara na rysunku (oś y w dół)"""
    a = math.radians(deg)
    x, y = p[0] - o[0], p[1] - o[1]
    return (o[0] + x * math.cos(a) - y * math.sin(a), o[1] + x * math.sin(a) + y * math.cos(a))


def band(c, w0, w1=None, cap0=False):
    w1 = w0 if w1 is None else w1
    L = [0.0]
    for i in range(1, len(c)):
        L.append(L[-1] + math.dist(c[i - 1], c[i]))
    tot = L[-1] or 1
    A, B = [], []
    for i, p in enumerate(c):
        a = c[max(i - 1, 0)]; b = c[min(i + 1, len(c) - 1)]
        tx, ty = unit((b[0] - a[0], b[1] - a[1]))
        w = (w0 + (w1 - w0) * L[i] / tot) / 2
        A.append((p[0] - ty * w, p[1] + tx * w))
        B.append((p[0] + ty * w, p[1] - tx * w))
    out = list(A) + B[::-1]
    if cap0:
        a = c[0]; b = c[1]
        tx, ty = unit((b[0] - a[0], b[1] - a[1]))
        nx, ny = ty, -tx
        for k in range(1, 12):
            ph = math.pi * k / 12
            out.append((a[0] + w0 / 2 * (nx * math.cos(ph) - tx * math.sin(ph)), a[1] + w0 / 2 * (ny * math.cos(ph) - ty * math.sin(ph))))
    return out


# ---------------------------------------------------------------- geometria (położenie wydechu)
A = (64.0, 41.0)                       # kąt mostka – przedni punkt połączenia rękojeści z trzonem
TM, TB, TX = 24.0, 10.0, 6.0           # odchylenie od pionu: rękojeść (górą ku tyłowi), trzon i wyrostek (dołem ku przodowi)
um = (math.sin(math.radians(TM)), -math.cos(math.radians(TM)))        # oś rękojeści ku górze
nm = (math.cos(math.radians(TM)), math.sin(math.radians(TM)))         # ku tyłowi (prostopadle do osi rękojeści)
ub = (-math.sin(math.radians(TB)), math.cos(math.radians(TB)))       # oś trzonu ku dołowi
nb = (math.cos(math.radians(TB)), math.sin(math.radians(TB)))         # ku tyłowi
ux = (-math.sin(math.radians(TX)), math.cos(math.radians(TX)))
nx_ = (math.cos(math.radians(TX)), math.sin(math.radians(TX)))
LM, LB, LX = 16.5, 32.0, 10.0
GAP = 0.5


def P(o, u, n, s, v):
    return (o[0] + u[0] * s + n[0] * v, o[1] + u[1] * s + n[1] * v)


# rękojeść: przednia powierzchnia lekko wypukła, tylna lekko wklęsła, brzeg górny najgrubszy
M0 = add(A, um, GAP)
man_front = [P(M0, um, nm, s, -0.35 * math.sin(math.pi * s / LM)) for s in (0, 3.5, 7, 10.5, 13.5, 15.6)]
man_top = [P(M0, um, nm, LM - 0.1, 0.9), P(M0, um, nm, LM + 0.15, 2.8), P(M0, um, nm, LM - 0.25, 4.7)]
man_back = [P(M0, um, nm, s, (4.5 + 1.0 * s / LM) - 0.4 * math.sin(math.pi * s / LM)) for s in (15.4, 12, 8.5, 5, 2, 0)]
MAN = man_front + man_top + man_back
NOTCH = man_top[1]
# trzon
B0 = add(A, ub, GAP)
bod_front = [P(B0, ub, nb, s, -0.2 * math.sin(math.pi * s / LB)) for s in (0, 6.5, 13, 19.5, 26, LB)]
bod_back = [P(B0, ub, nb, s, 3.6 - 0.5 * s / LB) for s in (LB, 24, 16, 8, 0)]
BOD = bod_front + bod_back
# wyrostek mieczykowaty
X0 = add(P(B0, ub, nb, LB, 0.4), ux, GAP)
xi_front = [P(X0, ux, nx_, s, 0.0 + 0.3 * s / LX) for s in (0, 3.5, 7, 9.2)]
xi_tip = [P(X0, ux, nx_, LX, 1.1)]
xi_back = [P(X0, ux, nx_, s, 2.3 - 0.7 * s / LX) for s in (9.2, 6, 3, 0)]
XI = xi_front + xi_tip + xi_back
# chrząstkozrosty (klin chrząstki między częściami)
SYN_M = [man_front[0], man_back[-1], bod_back[-1], bod_front[0]]
SYN_X = [bod_front[-1], bod_back[0], xi_back[-1], xi_front[0]]
# oś poprzeczna (przez przyczepy mostkowe żeber II) – w środku chrząstkozrostu górnego
XA = ((A[0] + (man_back[-1][0] + bod_back[-1][0]) / 2) / 2, (A[1] + (man_back[-1][1] + bod_back[-1][1]) / 2) / 2)

# żebro I (kość) i jego chrząstka
HP = (97.0, 16.0)                      # tylny koniec żebra I (staw głowy przy Th1) – biegun obrotu kości żebrowej
RIB = [(98.6, 15.5), (93.0, 16.8), (87.4, 19.2), (82.0, 22.4), (77.0, 26.4)]
J1 = RIB[-1]
S1 = P(M0, um, nm, 10.6, 2.7)          # przyczep chrząstki I na rękojeści (wcięcie żebrowe I)

# położenie wdechu: mostek – przesunięcie ku górze i do przodu + nieznaczny obrót (dolna część silniej do przodu)
SHIFT = (-1.6, -3.0)
PSI = 4.0                              # obrót całego mostka dokoła wcięcia szyjnego (dołem do przodu)
PHI = 4.0                              # dodatkowy obrót trzonu względem rękojeści dokoła osi poprzecznej (spłaszczenie kąta mostka)
THETA = 8.5                            # obrót kości żebrowej I ku górze dokoła tylnego końca


def insp_upper(p):
    q = rot(p, NOTCH, PSI)
    return (q[0] + SHIFT[0], q[1] + SHIFT[1])


XA_I = insp_upper(XA)


def insp_lower(p):
    return rot(insp_upper(p), XA_I, PHI)


def insp_rib(p):
    return rot(p, HP, THETA)


# ---------------------------------------------------------------- kręgosłup (fragment: Th1–Th3)
for k in range(3):
    y0 = 12.0 + k * 7.2
    xf = 92.0 + 0.45 * k
    if k < 2:
        f.add(f'<path class="annulus" d="{poly([(xf + 0.55, y0 + 5.5), (xf + 9.5, y0 + 5.5), (xf + 9.95, y0 + 7.3), (xf + 1.0, y0 + 7.3)])}"/>')
    f.add(f'<rect class="bone" x="{xf:.2f}" y="{y0:.2f}" width="9.6" height="5.6" rx=".8"/>')
f.text(102.8, 15.9, 'Th1', cls='note')

# ---------------------------------------------------------------- mostek – położenie wydechu
f.add(f'<path class="cart" d="{poly(SYN_M)}"/>')
f.add(f'<path class="cart" d="{poly(SYN_X)}"/>')
f.add(f'<path class="bone" d="{smooth(MAN, closed=True, t=0.4)}"/>')
f.add(f'<path class="bone" d="{smooth(BOD, closed=True, t=0.25)}"/>')
f.add(f'<path class="bone" d="{smooth(XI, closed=True, t=0.4)}"/>')
# chrząstka żebra II (przecięta) przy chrząstkozroście górnym
f.add(f'<ellipse class="cart" cx="{XA[0]:.2f}" cy="{XA[1]:.2f}" rx="1.35" ry="1.05" transform="rotate(-15 {XA[0]:.2f} {XA[1]:.2f})"/>')

# żebro I – położenie wydechu
rib_c = cr(RIB, n=16)
f.add(f'<path class="bone" d="{poly(band(rib_c, 2.8, 2.6, cap0=True))}"/>')
cart_c = cr([J1, ((J1[0] + S1[0]) / 2 + 0.15, (J1[1] + S1[1]) / 2 - 0.15), S1], n=10)
f.add(f'<path class="cart" d="{poly(band(cart_c, 2.6, 2.4))}"/>')

# ---------------------------------------------------------------- położenie wdechu (linia przerywana)
f.add(f'<path class="capsule" d="{smooth([insp_upper(p) for p in MAN], closed=True, t=0.4)}"/>')
f.add(f'<path class="capsule" d="{smooth([insp_lower(p) for p in BOD], closed=True, t=0.25)}"/>')
f.add(f'<path class="capsule" d="{smooth([insp_lower(p) for p in XI], closed=True, t=0.4)}"/>')
rib_i = [insp_rib(p) for p in rib_c]
f.add(f'<path class="capsule" d="{poly(band(rib_i, 2.8, 2.6, cap0=True))}"/>')
J1i, S1i = insp_rib(J1), insp_upper(S1)
cart_i = cr([J1i, ((J1i[0] + S1i[0]) / 2 + 0.15, (J1i[1] + S1i[1]) / 2 - 0.15), S1i], n=10)
f.add(f'<path class="capsule" d="{poly(band(cart_i, 2.6, 2.4))}"/>')

# oś poprzeczna (widoczna jako punkt) – położenie wydechu
f.add(f'<circle class="axis" style="stroke-dasharray:none" cx="{XA[0]:.2f}" cy="{XA[1]:.2f}" r=".7"/>')
f.add(f'<circle class="dot" style="fill:#d23c3c" cx="{XA[0]:.2f}" cy="{XA[1]:.2f}" r=".25"/>')
f.text(XA[0] + 2.4, XA[1] + 3.4, 'II', cls='note')

# ---------------------------------------------------------------- strzałki ruchu (wdech)
# wcięcie szyjne (górny koniec rękojeści)
top_i = insp_upper(NOTCH)
d = (top_i[0] - NOTCH[0], top_i[1] - NOTCH[1])
o1 = add(man_front[-1], (-1.0, 0.15), 1.9)
f.arrow(f'M{o1[0]:.2f},{o1[1]:.2f} L{o1[0] + d[0] * 1.5:.2f},{o1[1] + d[1] * 1.5:.2f}')
# dolny koniec trzonu
lo_e = bod_front[-1]
lo_i = insp_lower(lo_e)
d2 = (lo_i[0] - lo_e[0], lo_i[1] - lo_e[1])
o2 = add(lo_e, (-1.0, 0.3), 1.6)
f.arrow(f'M{o2[0]:.2f},{o2[1]:.2f} L{o2[0] + d2[0]:.2f},{o2[1] + d2[1]:.2f}')

print('przesunięcie: wcięcie szyjne %.1f mm, dolny koniec trzonu %.1f mm' % (math.hypot(*d), math.hypot(*d2)))
v1 = (man_front[-1][0] - man_front[0][0], man_front[-1][1] - man_front[0][1])
v2 = (bod_front[-1][0] - bod_front[0][0], bod_front[-1][1] - bod_front[0][1])
print('kąt mostka (wydech) %.0f°, (wdech) %.0f°' % (
    math.degrees(math.acos((v1[0] * v2[0] + v1[1] * v2[1]) / math.hypot(*v1) / math.hypot(*v2))),
    math.degrees(math.acos((v1[0] * v2[0] + v1[1] * v2[1]) / math.hypot(*v1) / math.hypot(*v2))) + PHI))

# ---------------------------------------------------------------- legenda
LY = 93.0
lx = 20.0
f.add(f'<rect class="bone" x="{lx:.2f}" y="{LY - 1.6:.2f}" width="5.2" height="2.2" rx=".5"/>')
f.text(lx + 6.6, LY + 0.3, 'położenie przy wydechu', cls='note')
lx2 = lx + 36.0
f.add(f'<path class="capsule" d="M{lx2:.2f},{LY - 0.5:.2f} L{lx2 + 5.6:.2f},{LY - 0.5:.2f}"/>')
f.text(lx2 + 6.8, LY + 0.3, 'położenie przy wdechu', cls='note')
lx3 = lx2 + 35.0
f.arrow(f'M{lx3:.2f},{LY - 0.5:.2f} L{lx3 + 7.0:.2f},{LY - 0.5:.2f}')
f.text(lx3 + 8.4, LY + 0.3, 'ruch przy wdechu', cls='note')

# ---------------------------------------------------------------- podpisy
TL, TR = 38.5, 93.0
f.label(P(M0, um, nm, 7.5, 2.0), 'rękojeść mostka', 'manubrium sterni', (TL, 25.5), side='L')
f.label(A, 'kąt mostka', 'angulus sterni', (TL, 37.5), side='L')
f.text(TL - 0.7, 44.7, 'we wdechu spłaszcza się', cls='note', anchor='end')
f.label(P(B0, ub, nb, 13.0, 1.3), 'trzon mostka', 'corpus sterni', (TL, 51.0), side='L')
am = add(o2, d2, 0.42)
f.label(am, 'przesunięcie równoległe', None, (TL, am[1] - 0.6), side='L')
f.text(TL - 0.7, am[1] + 3.5, 'ku górze i do przodu; dolne', cls='note', anchor='end')
f.text(TL - 0.7, am[1] + 6.2, 'części mostka silniej do przodu', cls='note', anchor='end')
f.label(P(X0, ux, nx_, 6.0, 0.9), 'wyrostek mieczykowaty', 'processus xiphoideus', (TL, 83.0), side='L')

rm = cr(RIB, n=16)[int(16 * 2.3)]
f.label(rm, 'żebro I', 'costa I', (rm[0] + 2.4, 5.2), side='R')
f.label(XA, 'oś poprzeczna', None, (TR, 35.5), side='R')
f.text(TR + 0.7, 39.6, 'przez przyczepy mostkowe żeber II;', cls='note')
f.text(TR + 0.7, 42.3, 'obrót rękojeści względem trzonu', cls='note')
f.text(TR + 0.7, 45.0, '(lub odwrotnie) – zmiana kąta mostka', cls='note')
sm = ((man_back[-1][0] + bod_back[-1][0]) / 2 - 0.1, (man_back[-1][1] + bod_back[-1][1]) / 2)
f.label(sm, 'górne połączenie mostkowe', 'synchondrosis s. symphysis manubriosternalis', (TR, 52.0), side='R')
sx = ((bod_back[0][0] + xi_back[-1][0]) / 2, (bod_back[0][1] + xi_back[-1][1]) / 2)
f.label(sx, 'dolne połączenie mostkowe', 'synchondrosis xiphosternalis', (TR, 66.5), side='R')
f.text(TR + 0.7, 73.7, 'ruchy mniej istotne', cls='note')

f.save()
