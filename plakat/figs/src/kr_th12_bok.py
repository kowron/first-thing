# Dwunasty kręg piersiowy (Th12) – widok z boku (od strony lewej; przód w lewo). Schemat własny.
# Cechy i nazwy wg Bochenka (s. 228–231, ryc. 143) – karta „Dwunasty kręg piersiowy (Th12)” w k_kregoslup.json:
# trzon szeroki, zbliżony do lędźwiowych; 1 dołek żebrowy w środku powierzchni bocznej trzonu; wyrostek poprzeczny
# bez dołka żebrowego, niezgrubiały; wyrostek stawowy górny – powierzchnia prawie w płaszczyźnie czołowej (zwrócona
# ku tyłowi, z boku widoczna jako wąskie pasmo), dolny – prawie w płaszczyźnie strzałkowej (z boku widoczna en face);
# na stronie bocznej wyrostka stawowego górnego guzki: wyrostek suteczkowaty i dodatkowy; wyrostek kolczysty krótszy,
# bardziej poziomy, spłaszczony i zgrubiały na końcu.
import sys; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 150, 64
X0, Y0, S = 40.0, 15.6, 0.95         # x=0: przednia powierzchnia trzonu, y=0: górna powierzchnia trzonu
def T(pts): return [(X0 + x * S, Y0 + y * S) for x, y in pts]
def P(x, y): return (X0 + x * S, Y0 + y * S)

f = Fig('kr_th12_bok', W, H, caption='dwunasty kręg piersiowy (Th12) · widok z boku (od strony lewej, przód w lewo)')

O = [(0.9, 0.15), (10.0, -0.2), (20.0, -0.3), (28.6, -0.2), (30.8, 0.4),
     (32.2, 1.6), (34.0, 2.1), (35.6, 1.5), (36.6, 0.0),                                  # wcięcie kręgowe górne
     (37.4, -3.2), (38.3, -6.0), (39.6, -8.0), (41.2, -8.7), (42.8, -8.1), (43.8, -6.3),   # wyrostek stawowy górny
     (44.3, -4.4), (45.9, -3.7), (47.5, -2.1), (47.9, 0.3), (46.9, 2.0),                  # wyrostek suteczkowaty
     (47.6, 3.3), (50.4, 3.7), (56.0, 3.6), (62.0, 3.5), (66.2, 3.3),                     # wyrostek kolczysty – brzeg górny
     (68.6, 4.3), (69.8, 7.4), (70.0, 11.6), (69.4, 15.4), (67.8, 18.0), (65.2, 18.7),    # koniec spłaszczony, zgrubiały
     (60.4, 17.7), (55.6, 16.8), (51.8, 17.0), (48.9, 18.3),                              # brzeg dolny
     (47.7, 21.0), (47.1, 25.6), (46.1, 29.6), (44.5, 31.6), (42.5, 31.5), (41.1, 29.2),  # wyrostek stawowy dolny
     (40.3, 25.0), (39.7, 21.0), (38.9, 17.6),
     (37.5, 15.0), (35.7, 14.0), (33.9, 14.8), (32.5, 17.4), (31.7, 20.6), (31.2, 23.5),  # wcięcie kręgowe dolne
     (29.4, 24.55), (20.0, 24.7), (10.0, 24.4), (1.1, 23.8),
     (0.15, 22.8), (0.9, 17.0), (1.35, 12.0), (0.85, 6.4), (0.05, 1.2)]
f.add(f'<path class="bone" d="{smooth(T(O))}"/>')

# listewka brzeżna
f.add(f'<path class="bonel" d="{smooth(T([(1.4, 1.6), (9.0, 1.4), (17.0, 1.35)]), closed=False)}"/>')
f.add(f'<path class="bonel" d="{smooth(T([(1.5, 22.5), (9.0, 22.95), (17.0, 23.15)]), closed=False)}"/>')
# zgrubiały koniec wyrostka kolczystego
f.add(f'<path class="bonel" d="{smooth(T([(66.6, 5.0), (67.4, 8.6), (67.5, 12.4), (66.8, 15.8), (65.4, 17.6)]), closed=False)}"/>')
# zarys guzka suteczkowatego na tle wyrostka stawowego górnego
f.add(f'<path class="bonel" d="{smooth(T([(44.6, -3.9), (44.4, -1.6), (45.6, 0.9), (46.9, 1.9)]), closed=False)}"/>')

# dołek żebrowy – tylko 1, w środku powierzchni bocznej trzonu (dla głowy żebra XII)
x, y = P(21.0, 11.8)
f.add(f'<ellipse class="facet" cx="{x:.2f}" cy="{y:.2f}" rx="{3.4 * S:.2f}" ry="{3.0 * S:.2f}" transform="rotate(-10 {x:.2f} {y:.2f})"/>')

# wyrostek stawowy górny – powierzchnia w płaszczyźnie czołowej, zwrócona ku tyłowi (wąskie pasmo)
f.add(f'<path class="facet" d="{smooth(T([(42.4, -8.4), (43.5, -6.9), (44.0, -5.2), (44.1, -3.9), (43.3, -4.3), (42.9, -6.0), (42.1, -7.6)]))}"/>')
# wyrostek stawowy dolny – powierzchnia prawie w płaszczyźnie strzałkowej, zwrócona bocznie (widoczna en face)
fi = T([(40.6, 21.4), (41.0, 25.2), (41.9, 28.6), (43.2, 30.5), (44.6, 30.1), (45.1, 27.2), (44.9, 23.6), (44.1, 20.6),
        (42.3, 19.6)])
f.add(f'<path class="facet" d="{smooth(fi)}"/>')

# wyrostek poprzeczny – krótki, niezgrubiały, bez dołka żebrowego (widoczny od strony końca)
sh = T([(41.0, 8.6), (43.4, 10.6), (46.0, 10.4), (47.6, 8.4), (47.4, 5.6), (48.6, 7.6), (48.0, 10.8), (45.4, 12.4),
        (42.4, 12.0), (40.6, 10.2)])
f.add(f'<path class="shade" d="{smooth(sh)}"/>')
tp = T([(39.8, 5.6), (40.8, 3.2), (43.0, 2.3), (45.4, 3.0), (46.5, 5.4), (46.0, 8.2), (43.8, 9.7), (41.4, 9.2)])
f.add(f'<path class="bone" d="{smooth(tp)}"/>')
# wyrostek dodatkowy – mały guzek ku tyłowi i ku dołowi od wyrostka poprzecznego
ac = T([(46.2, 9.6), (48.2, 9.1), (49.7, 10.4), (49.4, 12.5), (47.4, 13.0), (45.9, 11.6)])
f.add(f'<path class="bone" d="{smooth(ac)}"/>')

# --- podpisy ---
TL, TR = 36.0, 110.0
f.label(P(21.0, 11.8), 'dołek żebrowy', 'fovea costalis', (TL, 12.0), side='L')
f.label(P(8.0, 16.0), 'trzon', 'corpus vertebrae', (TL, 24.0), side='L')
f.label(P(42.8, 26.2), 'wyrostek stawowy dolny', 'processus articularis inferior', (TL, 44.0), side='L')
f.label(P(41.0, -6.0), 'wyrostek stawowy górny', 'processus articularis superior', (TR, 5.5), side='R')
f.label(P(46.6, -1.0), 'wyrostek suteczkowaty', 'processus mamillaris', (TR, 14.5), side='R')
f.label(P(60.0, 8.5), 'wyrostek kolczysty', 'processus spinosus', (TR, 23.5), side='R')
f.label(P(43.0, 6.0), 'wyrostek poprzeczny', 'processus transversus', (TR, 33.0), side='R')
f.label(P(47.7, 11.0), 'wyrostek dodatkowy', 'processus accessorius', (TR, 42.5), side='R')
f.save()
