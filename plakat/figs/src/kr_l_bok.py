# Kręg lędźwiowy typowy – widok z boku (od strony lewej; przód w lewo). Nazwy wg Bochenka (s. 220–222, 231–232).
import sys; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 150, 68
X0, Y0, S = 40.0, 20.0, 0.8          # x=0: przednia powierzchnia trzonu, y=0: górna powierzchnia trzonu
def T(pts): return [(X0 + x * S, Y0 + y * S) for x, y in pts]
def P(x, y): return (X0 + x * S, Y0 + y * S)

f = Fig('kr_l_bok', W, H, caption='kręg lędźwiowy typowy · widok z boku (od strony lewej, przód w lewo)')

# zarys: trzon, wcięcie kręgowe górne, wyrostek stawowy górny z wyrostkiem suteczkowatym, wyrostek kolczysty,
# wyrostek stawowy dolny, wcięcie kręgowe dolne
O = [(0.9, 0.1), (8.0, -0.25), (17.0, -0.35), (26.0, -0.25), (32.6, 0.0), (34.0, 0.9), (34.4, 2.1),
     (36.2, 3.1), (38.4, 3.4), (40.2, 2.4),                                   # wcięcie kręgowe górne (płytkie)
     (41.0, -1.4), (41.8, -5.6), (42.8, -9.4), (44.6, -11.8), (47.0, -12.6), (49.2, -11.8), (50.4, -9.4), (50.9, -7.2),
     (52.9, -6.4), (54.9, -4.4), (55.2, -1.6), (54.0, 0.6),                   # wyrostek suteczkowaty
     (53.6, 2.6), (56.0, 4.6), (62.0, 4.2), (70.0, 3.4), (78.0, 2.8), (83.6, 2.6),
     (86.6, 4.2), (87.7, 8.0), (87.8, 12.8), (87.2, 17.6), (85.4, 21.4), (82.2, 22.6),
     (76.6, 21.4), (70.4, 19.6), (64.8, 19.0), (61.0, 20.0),
     (59.0, 23.4), (58.2, 28.4), (57.4, 33.0), (56.0, 36.0), (53.8, 37.4), (51.4, 36.8),   # wyrostek stawowy dolny
     (49.6, 34.4), (48.6, 30.6), (48.0, 26.6), (47.2, 22.8),
     (45.8, 19.8), (43.4, 17.9), (40.4, 17.3), (37.6, 18.2), (35.6, 20.4),   # wcięcie kręgowe dolne (głębokie)
     (34.5, 22.8), (34.3, 25.6), (33.6, 26.9), (26.0, 27.35), (17.0, 27.5), (8.0, 27.35), (1.1, 27.0),
     (0.1, 26.0), (0.7, 20.0), (1.35, 13.5), (0.7, 7.0), (0.05, 1.1)]
f.add(f'<path class="bone" d="{smooth(T(O))}"/>')

# listewka brzeżna (górna i dolna) – lekko wystający brzeg powierzchni trzonu
f.add(f'<path class="bonel" d="{smooth(T([(1.2, 1.7), (12.0, 1.45), (24.0, 1.45), (32.9, 1.7)]), closed=False)}"/>')
f.add(f'<path class="bonel" d="{smooth(T([(1.3, 25.5), (12.0, 25.75), (24.0, 25.75), (33.0, 25.4)]), closed=False)}"/>')
# zgrubiały koniec wyrostka kolczystego
f.add(f'<path class="bonel" d="{smooth(T([(84.0, 4.4), (84.8, 8.8), (84.9, 13.4), (84.3, 17.8), (82.9, 21.0)]), closed=False)}"/>')
# powierzchnia stawowa wyrostka stawowego dolnego – wypukła, zwrócona do przodu i bocznie
fi = T([(47.9, 24.6), (48.4, 29.4), (49.4, 33.4), (51.0, 36.3), (52.9, 37.2), (52.2, 34.4), (51.3, 30.8), (50.6, 27.0),
        (49.9, 23.8)])
f.add(f'<path class="facet" d="{smooth(fi)}"/>')

# wyrostek żebrowy – skierowany bocznie (ku patrzącemu) i nieco ku tyłowi; widoczny od strony końca
sh = T([(41.6, 11.6), (44.6, 15.0), (48.6, 15.6), (51.4, 13.0), (51.8, 9.0), (53.0, 11.8), (52.2, 15.6), (48.6, 17.6),
        (44.0, 17.0), (41.2, 14.2)])
f.add(f'<path class="shade" d="{smooth(sh)}"/>')
cp = T([(41.4, 4.6), (44.0, 2.4), (47.4, 2.2), (50.0, 4.0), (51.0, 7.4), (50.4, 11.0), (48.0, 13.6), (44.6, 14.0),
        (42.0, 12.2), (40.8, 8.6)])
f.add(f'<path class="bone" d="{smooth(cp)}"/>')
# wyrostek dodatkowy – mały guzek z tyłu u nasady wyrostka żebrowego
ac = T([(49.4, 12.4), (52.2, 12.6), (54.0, 14.2), (53.6, 16.4), (51.2, 16.9), (49.4, 15.4)])
f.add(f'<path class="bone" d="{smooth(ac)}"/>')

# --- podpisy ---
TL, TR = 37.0, 113.0
f.label(P(38.4, 3.6), 'wcięcie kręgowe górne', 'incisura vertebralis superior', (TL, 9.0), side='L')
f.label(P(12.0, 7.0), 'trzon kręgu', 'corpus vertebrae', (TL, 19.0), side='L')
f.label(P(37.0, 10.6), 'nasada łuku kręgu', 'pediculus arcus vertebrae', (TL, 29.0), side='L')
f.label(P(41.0, 17.6), 'wcięcie kręgowe dolne', 'incisura vertebralis inferior', (TL, 39.0), side='L')
f.label(P(49.6, 30.0), 'wyrostek stawowy dolny', 'processus articularis inferior', (TL, 50.0), side='L')
f.label(P(46.4, -8.0), 'wyrostek stawowy górny', 'processus articularis superior', (TR, 7.0), side='R')
f.label(P(54.0, -3.0), 'wyrostek suteczkowaty', 'processus mamillaris', (TR, 17.0), side='R')
f.label(P(46.4, 7.6), 'wyrostek żebrowy', 'processus costalis', (TR, 27.0), side='R')
f.label(P(76.0, 15.0), 'wyrostek kolczysty', 'processus spinosus', (TR, 37.0), side='R')
f.label(P(52.4, 15.0), 'wyrostek dodatkowy', 'processus accessorius', (TR, 47.0), side='R')
f.save()
