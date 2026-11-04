# MOSTEK – widok z boku (przód w lewo). Trzon ustawiony pionowo; rękojeść odchylona ku tyłowi względem trzonu,
# więc obie części tworzą kąt mostka (otwarty ku tyłowi). Na brzegu bocznym widać wcięcia: obojczykowe i żebrowe I–VII.
# Nazwy wg Bochenka, t. I, s. 278–281 i s. 287. Skala jak w rysunku „mostek_przod”.
import sys; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
import math
from figlib import Fig, smooth

f = Fig('mostek_bok', 120, 104, caption='mostek · widok z boku (przód po lewej)')

OX, OY = 50.5, 33.0       # punkt kąta mostka (przednia powierzchnia, na wysokości połączenia rękojeści z trzonem)
TH = math.radians(18)     # odchylenie rękojeści ku tyłowi względem trzonu
AX = (math.sin(TH), -math.cos(TH))       # oś rękojeści (ku górze)
NX = (math.cos(TH), math.sin(TH))        # w poprzek rękojeści (ku tyłowi)
M0 = (0.28, -1.78)                       # przedni-dolny róg rękojeści (nad warstwą chrząstki)


def T(p):
    return (OX + p[0], OY + p[1])


def TL_(pts):
    return [T(p) for p in pts]


def man(u, v):
    """punkt rękojeści: u – wzdłuż osi od dołu (mm), v – od powierzchni przedniej ku tyłowi (mm)"""
    return (M0[0] + AX[0] * u + NX[0] * v, M0[1] + AX[1] * u + NX[1] * v)


def poly(pts):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + ' Z'


def bez(pts, t=0.5, n=14):
    """próbkowanie otwartej krzywej rysowanej przez smooth()"""
    m = len(pts)
    Q = [pts[0]] + pts + [pts[-1]]
    out = [pts[0]]
    for i in range(1, m):
        p0, p1, p2, p3 = Q[i - 1], Q[i], Q[i + 1], Q[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) * t / 3, p1[1] + (p2[1] - p0[1]) * t / 3)
        c2 = (p2[0] - (p3[0] - p1[0]) * t / 3, p2[1] - (p3[1] - p1[1]) * t / 3)
        for k in range(1, n + 1):
            u = k / n
            a, b, c, d = (1 - u) ** 3, 3 * (1 - u) ** 2 * u, 3 * (1 - u) * u ** 2, u ** 3
            out.append((a * p1[0] + b * c1[0] + c * c2[0] + d * p2[0], a * p1[1] + b * c1[1] + c * c2[1] + d * p2[1]))
    return out


def ell(cx, cy, rx, ry, rot=0.0, n=48):
    out = []
    for k in range(n):
        t = 2 * math.pi * k / n
        x, y = rx * math.cos(t), ry * math.sin(t)
        out.append((cx + x * math.cos(rot) - y * math.sin(rot), cy + x * math.sin(rot) + y * math.cos(rot)))
    return out


# ---------- rękojeść (grubsza, najgrubsza u góry; powierzchnia przednia lekko wypukła, tylna lekko wklęsła) ----------
# jedna gładka linia: powierzchnia przednia → brzeg górny → powierzchnia tylna; dolny brzeg prosty (połączenie z trzonem)
manub = bez([M0, man(6, -0.2), man(11.5, -0.35), man(17.5, -0.2), man(22.6, 0.1),
             man(23.3, 0.9), man(23.75, 2.6), man(23.85, 4.3), man(23.55, 6.0), man(22.8, 7.25),
             man(21.6, 7.55), man(17.5, 6.55), man(11.5, 5.7), man(6.0, 5.25), (5.28, -0.98)])
# ---------- trzon (górny i dolny brzeg prosty – połączenia) ----------
B1 = 49.4
body = (bez([(0.0, 0.0), (-0.12, 12), (-0.18, 25), (-0.1, 38), (0.0, B1)]) +
        bez([(4.4, B1), (4.6, 38), (4.75, 25), (4.9, 12), (5.0, 0.8)]))
# ---------- wyrostek mieczykowaty ----------
X0 = B1 + 1.6
xi = bez([(0.95, X0), (1.1, X0 + 4), (1.5, X0 + 9), (1.95, X0 + 13.0), (2.3, X0 + 14.4), (2.65, X0 + 13.4),
          (3.0, X0 + 9), (3.25, X0 + 4), (3.4, X0)])

# chrząstkozrosty mostkowe (warstwa chrząstki między częściami; rysowana pod kośćmi)
f.add(f'<path class="cart" d="{poly(TL_([(0.28, -1.78), (-0.25, -0.9), (0.0, 0.0), (5.0, 0.8), (5.45, -0.1), (5.28, -0.98)]))}"/>')
f.add(f'<path class="cart" d="{poly(TL_([(0.0, B1), (0.55, B1 + 0.8), (0.95, X0), (3.4, X0), (3.95, B1 + 0.8), (4.4, B1)]))}"/>')

f.add(f'<path class="bone" d="{poly(TL_(manub))}"/>')
f.add(f'<path class="bone" d="{poly(TL_(body))}"/>')
f.add(f'<path class="bone" d="{poly(TL_(xi))}"/>')

# ---------- powierzchnie na brzegu bocznym ----------
# wcięcie obojczykowe – górny koniec rękojeści (zwrócone ku górze i bocznie – widoczne skośnie)
f.add(f'<path class="facet" d="{poly(TL_([man(u, v) for u, v in ell(22.25, 3.75, 1.35, 2.95)]))}"/>')
# wcięcie żebrowe I – podłużne pole chropowate
f.add(f'<path class="bone2" d="{poly(TL_([man(u, v) for u, v in ell(15.0, 3.1, 3.9, 1.85)]))}"/>')
# wcięcie żebrowe II – na granicy rękojeści i trzonu
f.add(f'<path class="facet" d="{poly(TL_(ell(2.6, -0.5, 1.3, 2.9, math.radians(5))))}"/>')
# wcięcia III–VI na trzonie, VII na granicy trzonu i wyrostka mieczykowatego
YN = {'III': 10.7, 'IV': 21.7, 'V': 31.7, 'VI': 40.3}
for k, yc in YN.items():
    f.add(f'<path class="facet" d="{poly(TL_(ell(2.4, yc, 1.65, 2.45)))}"/>')
f.add(f'<path class="facet" d="{poly(TL_(ell(2.2, 50.2, 0.9, 2.65)))}"/>')

# przedłużenie przedniej powierzchni trzonu ku górze – widać załamanie przy kącie mostka
f.add(f'<path class="dim" d="M{OX:.2f},{OY - 1.2:.2f} L{OX:.2f},{OY - 15:.2f}"/>')

# numery wcięć III–VI
for k, yc in YN.items():
    f.text(OX + 5.9, OY + yc + 0.75, k, cls='note')

# ---------- podpisy ----------
TL, TR = 33.0, 82.5
f.label(T(man(10.0, 1.2)), 'rękojeść mostka', 'manubrium sterni', (TL, 19.0), side='L')
f.label(T((-0.05, -0.85)), 'kąt mostka', 'angulus sterni', (TL, 32.5), side='L')
f.label(T((1.0, 26.5)), 'trzon mostka', 'corpus sterni', (TL, 59.0), side='L')
f.label(T((1.9, 59.5)), 'wyrostek mieczykowaty', 'processus xiphoideus', (TL, 90.5), side='L')

f.label(T(man(22.25, 4.9)), 'wcięcie obojczykowe', 'incisura clavicularis', (TR, 6.5), side='R')
f.label(T(man(15.0, 3.9)), 'wcięcie żebrowe I', 'incisura costalis I', (TR, 16.0), side='R')
f.label(T((2.75, -1.6)), 'wcięcie żebrowe II', 'incisura costalis II', (TR, 26.5), side='R')
f.label(T((4.6, -0.2)), 'górne połączenie mostkowe', 'synchondrosis manubriosternalis', (TR, 37.0), side='R')
f.label(T((2.2, 49.4)), 'wcięcie żebrowe VII', 'incisura costalis VII', (TR, 75.5), side='R')
f.label(T((3.75, 50.0)), 'dolne połączenie mostkowe', 'synchondrosis xiphosternalis', (TR, 85.0), side='R')

# orientacja
f.text(OX - 8.0, OY + 64.0, 'przód', cls='notec')
f.text(OX + 12.0, OY + 64.0, 'tył', cls='notec')
f.save()
