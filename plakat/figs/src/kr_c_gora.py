# Kręg szyjny typowy (C3–C6) – widok od góry (przód ku górze). Nazwy wg Bochenka (s. 222–224, ryc. 135).
import sys; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth, mirror

W, H = 150, 76
CX, OY, S = 75, 17.0, 1.2          # oś symetrii, przedni brzeg trzonu, skala (mm rysunku / mm kości)
def T(pts): return [(CX + x * S, OY + y * S) for x, y in pts]
def P(x, y): return (CX + x * S, OY + y * S)

f = Fig('kr_c_gora', W, H, caption='kręg szyjny typowy (C3–C6) · widok od góry (przód ku górze)')

# --- łuk z wyrostkami (lewa połowa w mm kości, potem odbicie) ---
L = [(0, 3), (-8, 3), (-10, 3.0), (-14, 2.4), (-17.8, 1.3), (-19.9, 0.0), (-21.2, -1.0), (-22.6, -0.6), (-23.2, 1.0),
     (-22.4, 3.4), (-21.6, 5.3), (-22.3, 6.9), (-24.0, 7.8), (-25.3, 9.0), (-25.2, 10.7), (-23.6, 11.6),
     (-21.0, 12.1), (-20.0, 13.2), (-20.5, 15.2), (-20.7, 18.0), (-20.3, 21.2), (-18.9, 23.5),
     (-16.6, 24.7), (-14.0, 24.8), (-11.3, 25.6), (-8.0, 28.1), (-4.9, 30.9), (-3.4, 33.3), (-2.9, 36.0), (-3.4, 38.2),
     (-4.0, 39.5), (-3.6, 40.9), (-2.2, 41.2), (-1.1, 40.0), (-0.5, 38.5), (0, 38.0)]
Lt = T(L)
R = mirror(Lt, CX)
# prawa część wyrostka kolczystego nieco krótsza (części końcowe zwykle asymetryczne)
yc = OY + 38.0 * S
R = [(x, y - (y - yc) * 0.3) if y > yc else (x, y) for x, y in R]
f.add(f'<path class="bone" d="{smooth(Lt + R[1:])}"/>')

# otwór kręgowy – duży, trójkątny
F = T([(0, 12.6), (-8.4, 12.6), (-11.2, 13.4), (-12.6, 15.2), (-12.0, 17.4), (-8.8, 21.2), (-5.0, 25.2), (-1.8, 28.4)])
f.add(f'<path class="hole" d="{smooth(F + [P(0, 29.3)] + mirror(F, CX)[:-1])}"/>')

for s in (-1, 1):
    # bruzda nerwu rdzeniowego (na górnej powierzchni wyrostka poprzecznego, bocznie od otworu)
    g = T([(s * 15.6, 4.9), (s * 18.6, 4.1), (s * 20.9, 4.0), (s * 21.3, 5.4), (s * 21.5, 6.9), (s * 19.4, 8.7), (s * 15.6, 9.3)])
    f.add(f'<path class="bone2" d="{smooth(g)}"/>')
    # otwór wyrostka poprzecznego
    x, y = P(s * 14.3, 7.1)
    f.add(f'<circle class="hole" cx="{x:.2f}" cy="{y:.2f}" r="{2.55 * S:.2f}"/>')
    # wyrostek stawowy górny: powierzchnia stawowa (zwrócona ku górze i do tyłu)
    x, y = P(s * 16.5, 18.6)
    f.add(f'<ellipse class="bone2" cx="{x:.2f}" cy="{y:.2f}" rx="{3.8 * S:.2f}" ry="{3.3 * S:.2f}" transform="rotate({s * 14} {x:.2f} {y:.2f})"/>')
    f.add(f'<ellipse class="facet" cx="{x:.2f}" cy="{y + 0.45:.2f}" rx="{3.2 * S:.2f}" ry="{2.6 * S:.2f}" transform="rotate({s * 14} {x:.2f} {y:.2f})"/>')

# --- trzon: poprzecznie ustawiony czworobok o zaokrąglonych brzegach ---
B = T([(0, -0.35), (-5.5, -0.2), (-8.6, 0.6), (-9.7, 2.6), (-9.8, 7.0), (-9.4, 11.2), (-8.2, 12.8), (-5, 13.2)])
f.add(f'<path class="bone" d="{smooth(B + [P(0, 13.0)] + mirror(B, CX)[:-1])}"/>')
# listewka brzeżna (gładki brzeg powierzchni górnej)
Bi = T([(0, 1.0), (-5.3, 1.1), (-7.3, 1.8), (-7.9, 3.6), (-7.9, 7.4), (-7.5, 10.6), (-6.4, 11.7), (-3.5, 11.9)])
f.add(f'<path class="bonel" d="{smooth(Bi + [P(0, 11.8)] + mirror(Bi, CX)[:-1])}"/>')
# uniesione boczne brzegi powierzchni górnej (powierzchnia górna wklęsła w kierunku czołowym)
for s in (-1, 1):
    u = T([(s * 9.78, 4.0), (s * 9.75, 8.0), (s * 9.3, 11.3), (s * 8.2, 12.8), (s * 7.4, 12.2), (s * 7.8, 10.2), (s * 8.9, 6.6)])
    f.add(f'<path class="bone2" d="{smooth(u)}"/>')

# --- podpisy ---
TL, TR = 41, 109
f.label(P(-21.3, -0.2), 'guzek przedni', 'tuberculum anterius', (TL, 13.5), side='L')
f.label(P(-19.0, 6.4), 'bruzda nerwu rdzeniowego', 'sulcus nervi spinalis', (TL, 22.5), side='L')
f.label(P(-24.6, 9.4), 'guzek tylny', 'tuberculum posterius', (TL, 31.5), side='L')
f.label(P(-18.4, 11.0), 'wyrostek poprzeczny', 'processus transversus', (TL, 40.5), side='L')
f.label(P(-4.5, 20.0), 'otwór kręgowy', 'foramen vertebrale', (TL, 49.5), side='L')
f.label(P(3.5, 5.0), 'trzon kręgu', 'corpus vertebrae', (TR, 12.5), side='R')
f.label(P(14.3, 7.1), 'otwór wyrostka poprzecznego', 'foramen transversarium', (TR, 21.5), side='R')
f.label(P(10.6, 12.4), 'nasada łuku kręgu', 'pediculus arcus vertebrae', (TR, 30.5), side='R')
f.label(P(17.0, 19.1), 'wyrostek stawowy górny', 'processus articularis superior', (TR, 39.5), side='R')
f.label(P(8.6, 27.4), 'blaszka łuku kręgu', 'lamina arcus vertebrae', (TR, 48.5), side='R')
f.label(P(2.6, 36.6), 'wyrostek kolczysty', 'processus spinosus', (TR, 57.5), side='R')
f.text(P(5.2, 40.6)[0], P(5.2, 40.6)[1], 'koniec rozdwojony', cls='note')
f.save()
