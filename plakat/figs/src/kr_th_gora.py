# Kręg piersiowy typowy (środkowy odcinek) – widok od góry (przód ku górze).
# Nazwy i cechy wg Bochenka (s. 228–231, ryc. 140) – karta „Kręg piersiowy typowy” w k_kregoslup.json.
# Na podstawie wzoru figs/src/wzor_th_gora.py (kształty przerysowane wg karty).
import sys; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth, mirror

W, H = 150, 86
CX, OY, S = 66, 10.0, 1.0          # oś symetrii, przedni brzeg trzonu, skala
def T(pts): return [(CX + x * S, OY + y * S) for x, y in pts]
def P(x, y): return (CX + x * S, OY + y * S)
def M(pts): return mirror(pts, CX)

f = Fig('kr_th_gora', W, H, caption='kręg piersiowy typowy · widok od góry (przód ku górze)')

# --- łuk z wyrostkami (lewa połowa, potem odbicie) ---
L = [(0, 21.0), (-6.0, 21.0), (-10.2, 21.0),                                          # (pod trzonem)
     (-11.3, 23.4), (-11.1, 25.6), (-11.7, 27.4),                                       # nasada łuku – silnie zwężona
     (-14.6, 28.6), (-18.4, 30.0), (-22.0, 31.6), (-25.0, 32.6),                        # wyrostek poprzeczny – brzeg przedni
     (-27.2, 32.4), (-29.2, 33.2), (-30.4, 35.0), (-30.5, 37.4), (-29.6, 39.4),         # koniec zgrubiały
     (-27.6, 40.6), (-25.2, 40.6), (-22.0, 39.8), (-18.6, 39.0), (-15.6, 39.4),          # brzeg tylny
     (-12.8, 40.6), (-9.8, 42.4), (-6.8, 44.6), (-4.3, 47.2),                            # blaszka łuku
     (-3.0, 50.5), (-2.2, 55.0), (-1.6, 59.5), (-1.0, 63.4), (-0.5, 66.0)]               # wyrostek kolczysty
Lt = T(L)
f.add(f'<path class="bone" d="{smooth(Lt + [P(0, 66.8)] + M(Lt))}"/>')
# otwór kręgowy – okrągły, stosunkowo mały
x, y = P(0, 28.4)
f.add(f'<ellipse class="hole" cx="{x:.2f}" cy="{y:.2f}" rx="{7.3 * S:.2f}" ry="{7.0 * S:.2f}"/>')
# grzebień wyrostka kolczystego (linia pośrodkowa)
f.add(f'<path class="bonel" d="M{CX},{P(0, 50.0)[1]:.2f} L{CX},{P(0, 64.0)[1]:.2f}"/>')

for s in (-1, 1):
    # wyrostek stawowy górny – powierzchnia stawowa w płaszczyźnie czołowej, zwrócona ku tyłowi
    # (obie powierzchnie leżą na łuku walca, którego oś biegnie do przodu od otworu kręgowego)
    x, y = P(s * 10.5, 32.2)
    f.add(f'<ellipse class="bone2" cx="{x:.2f}" cy="{y:.2f}" rx="{3.7 * S:.2f}" ry="{2.7 * S:.2f}" transform="rotate({-s * 16} {x:.2f} {y:.2f})"/>')
    x2, y2 = P(s * 10.7, 33.5)
    f.add(f'<ellipse class="facet" cx="{x2:.2f}" cy="{y2:.2f}" rx="{3.1 * S:.2f}" ry="{1.2 * S:.2f}" transform="rotate({-s * 16} {x2:.2f} {y2:.2f})"/>')
    # dołek żebrowy wyrostka poprzecznego – na przedniej powierzchni zgrubiałego końca
    x, y = P(s * 27.9, 33.5)
    f.add(f'<ellipse class="facet" cx="{x:.2f}" cy="{y:.2f}" rx="{2.3 * S:.2f}" ry="{1.25 * S:.2f}" transform="rotate({s * 22} {x:.2f} {y:.2f})"/>')

# --- trzon: sercowaty (wymiar poprzeczny ≈ strzałkowy) + listewka brzeżna ---
B = [(0, 0), (-4.2, 0.35), (-8.2, 1.9), (-11.3, 4.6), (-13.2, 8.4), (-13.9, 12.6), (-13.5, 16.6), (-11.9, 20.0),
     (-9.0, 22.4), (-5.4, 23.2), (-2.3, 22.6)]
Bt = T(B)
f.add(f'<path class="bone" d="{smooth(Bt + [P(0, 22.0)] + M(Bt)[:-1])}"/>')
Bi = T([(0, 1.8), (-4.0, 2.1), (-7.4, 3.5), (-10.0, 5.9), (-11.6, 9.2), (-12.1, 12.7), (-11.7, 16.0), (-10.4, 18.8),
        (-8.0, 20.7), (-5.1, 21.4), (-2.3, 20.9)])
f.add(f'<path class="bonel" d="{smooth(Bi + [P(0, 20.4)] + M(Bi)[:-1])}"/>')
# dołki żebrowe górne – na krawędzi górnej trzonu, tuż u nasady łuku
for s in (-1, 1):
    x, y = P(s * 12.55, 18.9)
    f.add(f'<ellipse class="facet" cx="{x:.2f}" cy="{y:.2f}" rx="{2.5 * S:.2f}" ry="{1.25 * S:.2f}" transform="rotate({-s * 64} {x:.2f} {y:.2f})"/>')

# --- podpisy ---
TL, TR = 33.0, 99.0
f.label(P(-4.0, 9.0), 'trzon kręgu', 'corpus vertebrae', (TL, 13.5), side='L')
f.label(P(-12.6, 18.9), 'dołek żebrowy górny', 'fovea costalis superior', (TL, 24.0), side='L')
f.label(P(-9.0, 24.6), 'nasada łuku kręgu', 'pediculus arcus vertebrae', (TL, 34.5), side='L')
f.label(P(-20.0, 35.2), 'wyrostek poprzeczny', 'processus transversus', (TL, 45.5), side='L')
f.label(P(-5.6, 40.4), 'blaszka łuku kręgu', 'lamina arcus vertebrae', (TL, 56.5), side='L')
f.label(P(3.0, 27.0), 'otwór kręgowy', 'foramen vertebrale', (TR, 21.5), side='R')
f.label(P(28.0, 33.5), 'dołek żebrowy wyrostka poprzecznego', 'fovea costalis processus transversi', (TR, 32.5), side='R')
f.label(P(10.7, 33.5), 'wyrostek stawowy górny', 'processus articularis superior', (TR, 55.5), side='R')
f.label(P(0.7, 59.0), 'wyrostek kolczysty', 'processus spinosus', (TR, 67.5), side='R')
f.save()
