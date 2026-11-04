# WZÓR STYLU: kręg piersiowy typowy – widok od góry (przód u góry rysunku)
import sys; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth, mirror

C = 70   # oś symetrii
f = Fig('wzor_th_gora', 140, 88, caption='kręg piersiowy typowy · widok od góry (przód ku górze)')

# łuk z wyrostkami (połowa lewa, potem odbicie)
L = [(60.5, 33), (56.8, 38.2), (50, 41.5), (45, 43.3), (42.6, 44.3), (41.2, 46.6), (42.2, 49.1), (44.8, 50),
     (49.2, 49.2), (54, 48.8), (58, 49.8), (63, 52.4), (67.2, 55), (68.3, 61), (69.1, 68), (69.6, 73.3)]
arch = L + [(C, 74.4)] + mirror(L, C)
f.add(f'<path class="bone" d="{smooth(arch)}"/>')
# otwór kręgowy
f.add(f'<ellipse class="hole" cx="{C}" cy="42.2" rx="7.1" ry="6.7"/>')
# wyrostki stawowe górne (garbki) z powierzchniami stawowymi skierowanymi ku tyłowi
for s in (-1, 1):
    x = C + s * 8.9
    f.add(f'<ellipse class="bone2" cx="{x:.2f}" cy="45.4" rx="3.4" ry="2.5"/>')
    f.add(f'<ellipse class="facet" cx="{x:.2f}" cy="46.5" rx="2.8" ry="1.15"/>')
    # dołek żebrowy wyrostka poprzecznego (na przedniej stronie końca wyrostka)
    tx = C + s * 25.6
    f.add(f'<ellipse class="facet" cx="{tx:.2f}" cy="45.0" rx="2.1" ry="1.15" transform="rotate({s * 22} {tx:.2f} {45.0})"/>')
# trzon (sercowaty) + obrączka brzeżna
body = [(59.2, 35.2), (55.6, 30.2), (55.8, 23), (61, 17.2), (C, 15.2), (79, 17.2), (84.2, 23), (84.4, 30.2), (80.8, 35.2), (C, 33.6)]
f.add(f'<path class="bone" d="{smooth(body)}"/>')
inner = [(60.6, 33.4), (57.8, 29.6), (58.1, 23.6), (62.4, 18.9), (C, 17.3), (77.6, 18.9), (81.9, 23.6), (82.2, 29.6), (79.4, 33.4), (C, 32)]
f.add(f'<path class="bonel" d="{smooth(inner)}"/>')
# dołki żebrowe górne na trzonie
for s in (-1, 1):
    x = C + s * 11.4
    f.add(f'<ellipse class="facet" cx="{x:.2f}" cy="33.6" rx="2.2" ry="1.3" transform="rotate({-s * 30} {x:.2f} 33.6)"/>')
# grzebień na wyrostku kolczystym (linia środkowa)
f.add(f'<path class="bonel" d="M{C},54 L{C},71.5"/>')

# podpisy (PL + łac.)
f.label((C - 3, 24), 'trzon kręgu', 'corpus vertebrae', (36, 18), side='L')
f.label((C - 11.6, 33.6), 'dołek żebrowy górny', 'fovea costalis superior', (36, 28), side='L')
f.label((C - 11.6, 38.5), 'nasada łuku', 'pediculus arcus vertebrae', (36, 37.5), side='L')
f.label((C - 25.8, 45.1), 'dołek żebrowy wyrostka poprzecznego', 'fovea costalis processus transversi', (4, 74), side='R')
f.label((C - 22, 47.6), 'wyrostek poprzeczny', 'processus transversus', (36, 49.5), side='L')
f.label((C + 3.5, 41), 'otwór kręgowy', 'foramen vertebrale', (104, 24), side='R')
f.label((C + 9.6, 46.4), 'wyrostek stawowy górny', 'processus articularis superior', (104, 33.5), side='R')
f.label((C + 6.5, 52.2), 'blaszka łuku', 'lamina arcus vertebrae', (104, 45), side='R')
f.label((C + 0.6, 66), 'wyrostek kolczysty', 'processus spinosus', (104, 64), side='R')
f.save()
