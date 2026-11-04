# Kręg lędźwiowy typowy – widok od góry (przód ku górze). Nazwy wg Bochenka (s. 220–222, 231–232, ryc. 144).
import sys; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth, mirror

W, H = 150, 88
CX, OY, S = 75, 8.0, 0.8           # oś symetrii, przedni brzeg trzonu, skala (mm rysunku / mm kości)
def T(pts): return [(CX + x * S, OY + y * S) for x, y in pts]
def P(x, y): return (CX + x * S, OY + y * S)
def M(pts): return mirror(pts, CX)

f = Fig('kr_l_gora', W, H, caption='kręg lędźwiowy typowy · widok od góry (przód ku górze)')

# --- wyrostki stawowe dolne (niżej, wystają spod blaszek – ciemniejsze) ---
for s in (-1, 1):
    ia = T([(s * 6.0, 54.5), (s * 10.5, 54.0), (s * 14.0, 55.5), (s * 15.2, 58.5), (s * 14.2, 61.8), (s * 11.4, 63.4),
            (s * 8.2, 62.6), (s * 6.0, 59.5)])
    f.add(f'<path class="bone2" d="{smooth(ia)}"/>')

# --- łuk: nasady, wyrostki żebrowe, blaszki, wyrostek kolczysty (lewa połowa, potem odbicie) ---
A = [(0, 27.0), (-10.0, 27.0), (-17.0, 27.6), (-21.0, 29.2), (-24.0, 31.6), (-28.5, 33.2), (-33.5, 34.6), (-38.0, 35.6),
     (-41.2, 36.4), (-43.0, 38.2), (-42.8, 40.4), (-41.0, 41.6), (-37.8, 41.6), (-33.8, 41.0), (-30.6, 41.2), (-28.6, 42.2),
     (-27.8, 44.4), (-26.2, 46.0), (-24.2, 45.6), (-22.8, 47.2), (-22.4, 50.5), (-21.2, 54.0), (-18.4, 56.6), (-14.8, 57.2),
     (-10.4, 56.4), (-6.2, 55.6), (-3.7, 58.0), (-3.0, 63.0), (-2.75, 70.0), (-3.0, 76.5), (-3.9, 80.2), (-4.4, 83.6),
     (-3.6, 86.3), (-1.6, 87.3), (0, 87.4)]
At = T(A)
f.add(f'<path class="bone" d="{smooth(At + M(At)[1:-1])}"/>')
# grzbiet wyrostka kolczystego (płytka w płaszczyźnie pośrodkowej widziana od góry)
f.add(f'<path class="bonel" d="{smooth(T([(0, 57.5), (0, 70.0), (0, 84.5)]), closed=False)}"/>')

# --- otwór kręgowy: trójkątny, spłaszczony przednio-tylnie ---
F = T([(0, 30.6), (-6.0, 30.6), (-11.0, 30.8), (-13.0, 32.0), (-13.2, 34.4), (-11.8, 37.4), (-8.6, 40.8), (-4.4, 44.0)])
f.add(f'<path class="hole" d="{smooth(F + [P(0, 45.2)] + M(F)[:-1])}"/>')

# --- trzon: powierzchnia górna płaska, nerkowata ---
B = [(0, 0), (-8.0, 0.3), (-15.0, 1.9), (-20.0, 4.6), (-23.1, 9.0), (-24.3, 15.0), (-23.7, 21.2), (-21.6, 26.6),
     (-18.0, 30.6), (-13.0, 32.6), (-7.0, 32.2), (-3.0, 31.3)]
Bt = T(B)
f.add(f'<path class="bone" d="{smooth(Bt + [P(0, 31.0)] + M(Bt)[:-1])}"/>')
# listewka brzeżna – gładki brzeg powierzchni górnej
Bi = T([(0, 2.6), (-7.6, 2.9), (-13.8, 4.3), (-18.0, 6.8), (-20.6, 10.6), (-21.6, 15.2), (-21.0, 20.6), (-19.2, 25.0),
        (-16.2, 28.2), (-12.2, 29.8), (-7.0, 29.6), (-3.0, 28.8)])
f.add(f'<path class="bonel" d="{smooth(Bi + [P(0, 28.6)] + M(Bi)[:-1])}"/>')

# --- wyrostki stawowe górne (sterczą ku górze) z wyrostkami suteczkowatymi ---
for s in (-1, 1):
    sa = T([(s * 19.4, 39.4), (s * 22.4, 42.0), (s * 23.5, 45.8), (s * 23.4, 49.6), (s * 24.6, 51.4), (s * 25.0, 54.2),
            (s * 23.6, 56.6), (s * 20.8, 57.3), (s * 18.2, 56.2), (s * 15.6, 54.6), (s * 13.6, 51.6), (s * 13.1, 47.6),
            (s * 13.9, 43.6), (s * 16.0, 40.4)])
    f.add(f'<path class="bone" d="{smooth(sa)}"/>')
    # powierzchnia stawowa – wklęsła, zwrócona do tyłu i przyśrodkowo
    fa = T([(s * 15.6, 41.0), (s * 13.7, 44.2), (s * 13.25, 48.0), (s * 13.9, 51.6), (s * 15.9, 54.5), (s * 18.4, 56.0),
            (s * 18.9, 54.4), (s * 17.2, 52.6), (s * 15.9, 50.0), (s * 15.6, 46.8), (s * 16.2, 43.6), (s * 17.3, 41.6)])
    f.add(f'<path class="facet" d="{smooth(fa)}"/>')
    # zarys wyrostka suteczkowatego (guzek na stronie bocznej wyrostka stawowego górnego)
    f.add(f'<path class="bonel" d="{smooth(T([(s * 23.2, 50.2), (s * 22.4, 52.6), (s * 22.6, 55.2), (s * 23.6, 56.4)]), closed=False)}"/>')

# --- podpisy ---
TL, TR = 38.0, 112.0
f.label(P(-12.0, 12.0), 'trzon kręgu', 'corpus vertebrae', (TL, 12.5), side='L')
f.label(P(-16.0, 35.6), 'nasada łuku kręgu', 'pediculus arcus vertebrae', (TL, 24.5), side='L')
f.label(P(-34.0, 38.0), 'wyrostek żebrowy', 'processus costalis', (TL, 36.5), side='L')
f.label(P(-26.6, 44.6), 'wyrostek dodatkowy', 'processus accessorius', (TL, 48.0), side='L')
f.label(P(-10.6, 60.0), 'wyrostek stawowy dolny', 'processus articularis inferior', (TL, 59.5), side='L')
f.label(P(-2.0, 74.0), 'wyrostek kolczysty', 'processus spinosus', (TL, 71.0), side='L')
f.label(P(4.0, 37.0), 'otwór kręgowy', 'foramen vertebrale', (TR, 24.5), side='R')
f.label(P(14.0, 47.6), 'wyrostek stawowy górny', 'processus articularis superior', (TR, 42.5), side='R')
f.label(P(24.0, 53.6), 'wyrostek suteczkowaty', 'processus mamillaris', (TR, 53.5), side='R')
f.label(P(7.6, 50.4), 'blaszka łuku kręgu', 'lamina arcus vertebrae', (TR, 64.5), side='R')
f.save()
