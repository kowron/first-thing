# Kręg wystający (C7, vertebra prominens) – widok od góry (przód ku górze).
# Nazwy i cechy wg Bochenka (s. 226–227, ryc. 139) – karta „Kręg wystający (C7)” w k_kregoslup.json
# (nazwy ogólne – otwór kręgowy, wyrostek stawowy górny, blaszka łuku kręgu – z karty „Budowa ogólna kręgu”).
import sys; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth, mirror

W, H = 150, 77
CX, OY, S = 75, 9.0, 0.95          # oś symetrii, przedni brzeg trzonu, skala
def T(pts): return [(CX + x * S, OY + y * S) for x, y in pts]
def P(x, y): return (CX + x * S, OY + y * S)
def M(pts): return mirror(pts, CX)

f = Fig('kr_c7_gora', W, H, caption='kręg wystający (C7) · widok od góry (przód ku górze)')

# --- łuk z wyrostkami (lewa połowa, potem odbicie) ---
L = [(0, 4.0), (-9.0, 4.0), (-11.2, 4.6), (-13.5, 5.0), (-16.5, 5.2), (-19.2, 5.0),           # listewka przednia (cienka)
     (-21.0, 4.4), (-22.5, 4.8), (-23.0, 6.0),                                                   # guzek przedni (mały)
     (-25.0, 6.6), (-28.0, 6.6), (-31.0, 6.8), (-33.3, 7.6), (-34.8, 9.3), (-35.0, 11.6),       # koniec wyrostka poprzecznego
     (-34.0, 13.8), (-31.8, 15.0), (-28.5, 15.3), (-25.2, 15.1), (-22.8, 15.4), (-21.6, 16.6),  # listewka tylna (duża)
     (-22.0, 18.4), (-22.1, 21.2), (-21.4, 24.0), (-19.8, 26.0),                                 # słup stawowy
     (-17.0, 27.3), (-13.8, 28.6), (-10.6, 30.6), (-7.8, 33.4), (-5.6, 36.6),                    # blaszka łuku
     (-4.4, 40.0), (-4.0, 44.5), (-3.9, 49.0), (-4.1, 52.5), (-4.9, 55.0), (-5.0, 57.6),        # wyrostek kolczysty
     (-3.8, 59.6), (-1.6, 60.3)]
Lt = T(L)
f.add(f'<path class="bone" d="{smooth(Lt + [P(0, 60.4)] + M(Lt))}"/>')

# otwór kręgowy (zaokrąglony trójkąt; przedni brzeg schowany pod trzonem)
F = T([(0, 14.6), (-7.6, 14.7), (-11.2, 15.6), (-12.8, 17.8), (-12.4, 20.8), (-9.8, 24.4), (-6.0, 27.3), (-2.4, 29.2)])
f.add(f'<path class="hole" d="{smooth(F + [P(0, 29.8)] + M(F)[:-1])}"/>')

for s in (-1, 1):
    # bruzda nerwu rdzeniowego – na górnej powierzchni wyrostka poprzecznego, bocznie od otworu
    g = T([(s * 18.4, 7.9), (s * 21.5, 7.3), (s * 25.5, 7.6), (s * 29.2, 8.1), (s * 30.6, 9.4), (s * 29.2, 10.9),
           (s * 25.2, 11.1), (s * 21.2, 11.2), (s * 18.7, 10.6)])
    f.add(f'<path class="bone2" d="{smooth(g)}"/>')
    # otwór wyrostka poprzecznego – zwykle mniejszy niż w innych kręgach szyjnych
    x, y = P(s * 15.8, 9.7)
    f.add(f'<circle class="hole" cx="{x:.2f}" cy="{y:.2f}" r="{1.9 * S:.2f}"/>')
    # wyrostek stawowy górny: powierzchnia stawowa zwrócona ku górze i do tyłu
    x, y = P(s * 17.4, 20.6)
    f.add(f'<ellipse class="bone2" cx="{x:.2f}" cy="{y:.2f}" rx="{4.1 * S:.2f}" ry="{3.6 * S:.2f}" transform="rotate({s * 12} {x:.2f} {y:.2f})"/>')
    f.add(f'<ellipse class="facet" cx="{x:.2f}" cy="{y + 0.4:.2f}" rx="{3.5 * S:.2f}" ry="{2.9 * S:.2f}" transform="rotate({s * 12} {x:.2f} {y:.2f})"/>')

# --- trzon: większy niż w pozostałych kręgach szyjnych ---
B = T([(0, -0.3), (-5.5, -0.15), (-8.8, 0.6), (-10.6, 2.6), (-11.0, 7.0), (-10.7, 11.6), (-9.6, 14.2), (-6.0, 15.2)])
f.add(f'<path class="bone" d="{smooth(B + [P(0, 15.1)] + M(B)[:-1])}"/>')
Bi = T([(0, 1.3), (-5.2, 1.4), (-7.6, 2.1), (-8.9, 3.9), (-9.2, 7.2), (-9.0, 10.8), (-8.0, 12.8), (-4.6, 13.5)])
f.add(f'<path class="bonel" d="{smooth(Bi + [P(0, 13.5)] + M(Bi)[:-1])}"/>')
for s in (-1, 1):   # uniesione boczne brzegi powierzchni górnej
    u = T([(s * 10.95, 5.5), (s * 10.85, 9.5), (s * 10.4, 12.6), (s * 9.4, 14.3), (s * 8.6, 13.6), (s * 9.2, 11.0), (s * 10.0, 7.6)])
    f.add(f'<path class="bone2" d="{smooth(u)}"/>')

def note(tx, ty, t, side):
    f.text(tx + 0.7 if side == 'R' else tx - 0.7, ty, t, cls='note', anchor='start' if side == 'R' else 'end')

# --- podpisy ---
TL, TR = 40.0, 110.0
f.label(P(-22.0, 5.3), 'guzek przedni', 'tuberculum anterius', (TL, 7.0), side='L');  note(TL, 13.9, 'słabo rozwinięty', 'L')
f.label(P(-33.0, 11.4), 'wyrostek poprzeczny', 'processus transversus', (TL, 19.5), side='L')
f.label(P(-24.5, 13.3), 'listewka tylna', None, (TL, 29.5), side='L');  note(TL, 33.6, 'duża', 'L')
f.label(P(-17.8, 21.2), 'wyrostek stawowy górny', 'processus articularis superior', (TL, 39.0), side='L')
f.label(P(-10.4, 27.6), 'blaszka łuku kręgu', 'lamina arcus vertebrae', (TL, 49.0), side='L')
f.label(P(4.0, 6.0), 'trzon kręgu', 'corpus vertebrae', (TR, 6.5), side='R')
f.label(P(16.6, 6.1), 'listewka przednia', None, (TR, 16.5), side='R');  note(TR, 20.6, 'mała, słabo zaznaczona', 'R')
f.label(P(15.8, 9.7), 'otwór wyrostka poprzecznego', 'foramen transversarium', (TR, 26.0), side='R');  note(TR, 32.9, 'zwykle mniejszy', 'R')
f.label(P(5.0, 22.0), 'otwór kręgowy', 'foramen vertebrale', (TR, 39.0), side='R')
f.label(P(1.4, 49.0), 'wyrostek kolczysty', 'processus spinosus', (TR, 55.0), side='R');  note(TR, 61.9, 'niepodzielony i długi', 'R')
f.save()
