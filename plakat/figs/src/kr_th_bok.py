# Kręg piersiowy typowy (środkowy odcinek) – widok z boku (od strony lewej; przód w lewo). Schemat własny.
# Nazwy i cechy wg Bochenka (s. 221–222, 228–231): karty „Kręg piersiowy typowy” i „Budowa ogólna kręgu”
# w k_kregoslup.json. Trzon klinowaty (z przodu nieco niższy), dołki żebrowe górny (większy) i dolny na krawędziach
# trzonu tuż u nasady łuku, dołek żebrowy na przedniej powierzchni zgrubiałego końca wyrostka poprzecznego,
# wcięcie górne płytkie, dolne głębokie, wyrostek kolczysty długi, silnie pochylony ku dołowi.
import sys; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 150, 68
X0, Y0, S = 40.5, 16.5, 1.0          # x=0: przednia powierzchnia trzonu, y=0: górna powierzchnia trzonu
def T(pts): return [(X0 + x * S, Y0 + y * S) for x, y in pts]
def P(x, y): return (X0 + x * S, Y0 + y * S)

f = Fig('kr_th_bok', W, H, caption='kręg piersiowy typowy · widok z boku (od strony lewej, przód w lewo)')

# --- zarys: trzon, wcięcie górne, wyrostek stawowy górny, wyrostek kolczysty, wyrostek stawowy dolny, wcięcie dolne ---
O = [(0.8, 0.15), (8.0, -0.15), (16.0, -0.25), (22.6, -0.15), (24.7, 0.3),
     (25.9, 1.3), (27.3, 1.75), (28.6, 1.2), (29.5, -0.3),                                # wcięcie kręgowe górne (płytkie)
     (30.4, -3.0), (31.4, -5.4), (32.6, -6.9), (34.0, -7.3), (35.4, -6.4), (36.3, -4.2),   # wyrostek stawowy górny
     (37.3, -2.2), (39.4, -0.9), (41.8, 0.0), (43.6, 2.0),                                # (za wyrostkiem poprzecznym)
     (46.2, 8.6), (49.3, 17.2), (52.4, 26.2), (55.0, 33.8), (56.5, 38.2),                 # wyrostek kolczysty – brzeg górny
     (56.4, 41.2), (54.6, 42.7), (52.6, 41.8), (51.3, 38.6),                              # zgrubiały koniec
     (49.2, 33.2), (46.6, 27.6), (43.6, 22.4), (40.9, 18.6), (38.9, 16.9),                 # brzeg dolny
     (37.5, 18.4), (36.6, 21.4), (35.4, 24.4), (33.5, 25.7), (31.7, 24.9),                # wyrostek stawowy dolny
     (30.9, 21.8), (30.3, 17.8), (29.5, 14.4),
     (28.1, 12.2), (26.7, 12.4), (25.7, 14.1), (25.2, 16.7), (24.8, 18.9),               # wcięcie kręgowe dolne (głębokie)
     (23.2, 19.75), (16.0, 19.7), (8.0, 19.3), (1.0, 18.75),
     (0.15, 17.9), (0.8, 13.4), (1.25, 9.4), (0.75, 5.0), (0.05, 1.1)]
f.add(f'<path class="bone" d="{smooth(T(O))}"/>')

# listewka brzeżna (górna i dolna)
f.add(f'<path class="bonel" d="{smooth(T([(1.3, 1.5), (8.0, 1.3), (14.6, 1.25)]), closed=False)}"/>')
f.add(f'<path class="bonel" d="{smooth(T([(1.4, 17.5), (8.0, 17.9), (16.4, 18.2)]), closed=False)}"/>')
# grzebień wyrostka kolczystego (trójkątny przekrój) – delikatna linia wzdłuż
f.add(f'<path class="bonel" d="{smooth(T([(44.0, 8.4), (47.6, 18.4), (51.0, 28.0), (53.8, 35.6), (54.8, 39.0)]), closed=False)}"/>')

# dołki żebrowe na trzonie – na krawędzi górnej i dolnej, tuż u nasady łuku; górny większy
x1, y1 = P(17.7, -0.1); x2, y2 = P(25.5, 0.55)
f.add(f'<path class="facet" d="M{x1:.2f},{y1:.2f} C{P(17.9, 3.9)[0]:.2f},{P(17.9, 3.9)[1]:.2f} '
      f'{P(25.2, 4.6)[0]:.2f},{P(25.2, 4.6)[1]:.2f} {x2:.2f},{y2:.2f} '
      f'C{P(24.4, -0.05)[0]:.2f},{P(24.4, -0.05)[1]:.2f} {P(20.0, -0.2)[0]:.2f},{P(20.0, -0.2)[1]:.2f} {x1:.2f},{y1:.2f} Z"/>')
x1, y1 = P(19.8, 19.72); x2, y2 = P(24.9, 18.85)
f.add(f'<path class="facet" d="M{x1:.2f},{y1:.2f} C{P(19.9, 16.6)[0]:.2f},{P(19.9, 16.6)[1]:.2f} '
      f'{P(24.7, 16.0)[0]:.2f},{P(24.7, 16.0)[1]:.2f} {x2:.2f},{y2:.2f} '
      f'C{P(24.3, 19.5)[0]:.2f},{P(24.3, 19.5)[1]:.2f} {P(22.0, 19.75)[0]:.2f},{P(22.0, 19.75)[1]:.2f} {x1:.2f},{y1:.2f} Z"/>')

# powierzchnie stawowe wyrostków stawowych (płaszczyzna czołowa – widoczne z boku jako wąskie pasma):
# górny – zwrócona ku tyłowi, dolny – ku przodowi
f.add(f'<path class="facet" d="{smooth(T([(34.7, -7.05), (35.9, -5.5), (36.6, -3.4), (37.0, -1.4), (36.0, -1.6), (35.4, -3.6), (34.6, -5.6)]))}"/>')
f.add(f'<path class="facet" d="{smooth(T([(30.2, 16.2), (30.8, 19.8), (31.4, 22.8), (32.3, 25.3), (33.1, 24.7), (32.3, 21.8), (31.6, 18.6), (31.1, 15.6)]))}"/>')

# wyrostek poprzeczny – skierowany bocznie i ku tyłowi; widoczny od strony zgrubiałego końca
sh = T([(36.4, 6.8), (39.2, 9.4), (42.6, 9.6), (45.0, 7.4), (45.2, 4.0), (46.4, 6.6), (45.6, 10.2), (42.4, 11.6),
        (38.6, 11.0), (36.0, 8.6)])
f.add(f'<path class="shade" d="{smooth(sh)}"/>')
tp = T([(34.6, 3.0), (35.6, 0.6), (38.0, -0.6), (41.0, -0.4), (43.6, 1.2), (44.8, 4.0), (44.2, 7.0), (41.8, 9.0),
        (38.6, 9.2), (35.8, 7.6)])
f.add(f'<path class="bone" d="{smooth(tp)}"/>')
# dołek żebrowy wyrostka poprzecznego – na przedniej powierzchni końca wyrostka
x, y = P(37.0, 4.3)
f.add(f'<ellipse class="facet" cx="{x:.2f}" cy="{y:.2f}" rx="{1.85 * S:.2f}" ry="{3.0 * S:.2f}" transform="rotate(-8 {x:.2f} {y:.2f})"/>')

# --- podpisy ---
TL, TR = 36.0, 98.5
f.label(P(27.4, 1.5), 'wcięcie kręgowe górne', 'incisura vertebralis superior', (TL, 5.0), side='L')
f.label(P(20.5, 1.6), 'dołek żebrowy górny', 'fovea costalis superior', (TL, 14.5), side='L')
f.label(P(9.0, 9.5), 'trzon', 'corpus vertebrae', (TL, 24.5), side='L')
f.label(P(27.6, 6.8), 'nasada łuku kręgu', 'pediculus arcus vertebrae', (TL, 34.5), side='L')
f.label(P(27.4, 13.6), 'wcięcie kręgowe dolne', 'incisura vertebralis inferior', (TL, 44.8), side='L')
f.label(P(22.3, 18.4), 'dołek żebrowy dolny', 'fovea costalis inferior', (TL, 55.0), side='L')
f.label(P(33.4, -4.6), 'wyrostek stawowy górny', 'processus articularis superior', (TR, 7.5), side='R')
f.label(P(37.0, 4.3), 'dołek żebrowy wyrostka poprzecznego', 'fovea costalis processus transversi', (TR, 17.0), side='R')
f.label(P(41.8, 5.0), 'wyrostek poprzeczny', 'processus transversus', (TR, 26.5), side='R')
f.label(P(33.6, 21.0), 'wyrostek stawowy dolny', 'processus articularis inferior', (TR, 38.5), side='R')
f.label(P(53.0, 33.0), 'wyrostek kolczysty', 'processus spinosus', (TR, 50.5), side='R')
f.save()
