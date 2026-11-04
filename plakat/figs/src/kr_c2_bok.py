# Kręg obrotowy (C2, axis) – widok z boku (od strony lewej; przód w lewo). Nazwy wg Bochenka (s. 225–226, ryc. 137).
import sys; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 150, 68
X0, Y0, S = 46.5, 9.0, 1.25          # x=0: przednia powierzchnia trzonu, y=0: wierzchołek zęba
def T(pts): return [(X0 + x * S, Y0 + y * S) for x, y in pts]
def P(x, y): return (X0 + x * S, Y0 + y * S)

f = Fig('kr_c2_bok', W, H, caption='kręg obrotowy (C2) · widok z boku (od strony lewej, przód w lewo)')

# zarys: ząb, trzon (z wargą przednio-dolną), wcięcie kręgowe dolne, wyrostek stawowy dolny, wyrostek kolczysty, łuk
O = [(8.0, 0.0), (5.2, 0.8), (3.6, 2.8), (3.0, 5.5), (2.9, 8.5), (3.3, 11.2), (4.0, 13.0), (3.6, 14.3), (2.2, 15.0), (0.8, 15.6),
     (0.0, 16.8), (-0.2, 19.5), (0.2, 24.0), (0.3, 28.5), (-0.1, 33.0), (-0.6, 36.5), (0.0, 38.6), (1.4, 39.2), (5.0, 38.4),
     (9.0, 37.2), (12.4, 36.1), (14.3, 35.1), (15.1, 33.3), (15.5, 31.0), (16.5, 29.3), (18.2, 28.7), (19.8, 29.2), (20.9, 30.8),
     (21.4, 33.0), (21.7, 35.2), (22.3, 37.2), (23.3, 38.8), (24.6, 39.6), (26.0, 39.0), (26.8, 37.0), (27.2, 34.6), (28.0, 32.7),
     (29.8, 31.6), (32.5, 31.1), (35.5, 31.4), (39.0, 32.2), (42.0, 32.2), (44.8, 31.0), (46.2, 28.8), (46.0, 26.0), (44.6, 24.1),
     (41.5, 23.2), (37.5, 22.4), (33.0, 21.8), (28.5, 21.0), (25.0, 20.4), (22.4, 19.4), (20.6, 18.0), (19.2, 16.4), (17.4, 15.2),
     (15.0, 14.4), (13.2, 13.9), (12.6, 12.6), (12.8, 10.0), (13.0, 7.0), (12.6, 4.0), (11.4, 1.6), (9.8, 0.3)]
f.add(f'<path class="bone" d="{smooth(T(O))}"/>')
# linia boczna łuku i wyrostka kolczystego
f.add(f'<path class="bonel" d="{smooth(T([(23.6, 22.4), (28.5, 23.6), (34.0, 24.6), (39.5, 25.6), (43.6, 27.0)]), closed=False)}"/>')
f.add(f'<path class="bonel" d="{smooth(T([(15.7, 27.4), (16.2, 28.4), (16.9, 29.0)]), closed=False)}"/>')

# delikatny cień pod nawisem części dźwigającej powierzchnię stawową górną
sd = T([(0.3, 19.0), (6.0, 20.0), (12.0, 20.0), (17.4, 19.0), (19.6, 17.6), (19.9, 19.2), (17.8, 21.0), (12.0, 22.0), (6.0, 22.0), (0.25, 21.0)])
f.add(f'<path class="shade" d="{smooth(sd)}"/>')
# powierzchnia stawowa przednia zęba (do łuku przedniego C1) i tylna
fa = T([(3.45, 3.3), (3.05, 5.6), (2.95, 8.5), (3.3, 11.3), (4.3, 10.8), (4.0, 8.2), (4.1, 5.6), (4.4, 3.9)])
f.add(f'<path class="facet" d="{smooth(fa)}"/>')
fp = T([(12.95, 6.6), (12.85, 9.6), (12.65, 12.4), (11.75, 12.0), (11.85, 9.6), (12.0, 7.2)])
f.add(f'<path class="facet" d="{smooth(fp)}"/>')
# powierzchnia stawowa górna (na bocznej części trzonu, obok zęba; skierowana skośnie ku dołowi i bocznie)
fs = T([(0.8, 15.6), (4.0, 14.5), (9.0, 14.0), (14.5, 14.4), (18.6, 15.9), (19.4, 17.3), (17.2, 18.9), (12.0, 19.8), (6.0, 19.8),
        (2.0, 19.0), (0.35, 17.3)])
f.add(f'<path class="facet" d="{smooth(fs)}"/>')
# wyrostek stawowy dolny – powierzchnia stawowa zwrócona ku dołowi i do przodu
fi = T([(21.55, 34.3), (21.95, 36.2), (22.6, 37.7), (23.6, 39.0), (24.7, 39.55), (25.4, 38.6), (24.2, 37.5), (23.3, 36.0), (22.8, 34.2)])
f.add(f'<path class="facet" d="{smooth(fi)}"/>')
# wyrostek poprzeczny z otworem (bez guzków i bez bruzdy nerwu rdzeniowego)
tp = T([(12.6, 20.9), (16.8, 20.7), (19.8, 22.1), (20.2, 24.8), (18.6, 27.0), (15.8, 27.6), (13.4, 25.8), (12.4, 23.0)])
f.add(f'<path class="bone" d="{smooth(tp)}"/>')
x, y = P(16.6, 23.1); f.add(f'<ellipse class="hole" cx="{x:.2f}" cy="{y:.2f}" rx="{1.8 * S:.2f}" ry="{1.3 * S:.2f}"/>')

# --- podpisy ---
TL, TR = 43.0, 107.5
f.label(P(7.4, 0.35), 'wierzchołek zęba', 'apex dentis', (TL, 6.0), side='L')
f.label(P(3.6, 7.4), 'powierzchnia stawowa przednia', 'facies articularis anterior', (TL, 15.0), side='L')
f.label(P(5.0, 17.6), 'powierzchnia stawowa górna', 'facies articularis superior', (TL, 25.0), side='L')
f.label(P(14.4, 25.6), 'wyrostek poprzeczny', 'processus transversus', (TL, 35.0), side='L')
f.label(P(6.5, 29.5), 'trzon kręgu', 'corpus vertebrae', (TL, 45.0), side='L')
f.label(P(8.4, 5.6), 'ząb', 'dens', (TR, 8.0), side='R')
f.label(P(12.35, 9.8), 'powierzchnia stawowa tylna', 'facies articularis posterior', (TR, 17.0), side='R')
f.label(P(16.6, 23.1), 'otwór wyrostka poprzecznego', 'foramen transversarium', (TR, 26.0), side='R')
f.label(P(38.0, 27.6), 'wyrostek kolczysty', 'processus spinosus', (TR, 35.5), side='R')
f.label(P(18.2, 28.75), 'wcięcie kręgowe dolne', 'incisura vertebralis inferior', (TR, 46.0), side='R')
f.label(P(25.6, 35.6), 'wyrostek stawowy dolny', 'processus articularis inferior', (TR, 55.0), side='R')
f.save()
