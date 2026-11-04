# Kręg obrotowy (C2, axis) – widok od przodu (prawa strona ciała po lewej stronie rysunku). Bez więzadeł.
# Nazwy wg Bochenka (s. 225–226) – karta „Kręg obrotowy (C2)” w k_kregoslup.json.
import sys; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth, mirror

W, H = 150, 63
CX, OY, S = 75, 8.0, 1.2          # oś symetrii, wierzchołek zęba, skala (mm rysunku / mm kości)
def T(pts): return [(CX + x * S, OY + y * S) for x, y in pts]
def P(x, y): return (CX + x * S, OY + y * S)
def M(pts): return mirror(pts, CX)

f = Fig('kr_c2_przod', W, H, caption='kręg obrotowy (C2) · widok od przodu')

# --- w tle: wyrostki stawowe dolne (za trzonem, pod wyrostkami poprzecznymi) ---
for s in (-1, 1):
    iap = T([(s * 11.4, 29.0), (s * 11.9, 32.4), (s * 12.9, 35.0), (s * 14.7, 36.4), (s * 17.0, 36.3), (s * 18.5, 34.6),
             (s * 18.9, 31.6), (s * 18.6, 28.6), (s * 15.2, 27.8)])
    f.add(f'<path class="bone2" d="{smooth(iap)}"/>')
    # powierzchnia stawowa dolna – zwrócona ku dołowi i do przodu
    fi = T([(s * 13.1, 34.4), (s * 14.7, 33.8), (s * 16.5, 33.7), (s * 18.2, 34.2), (s * 17.1, 35.6), (s * 15.0, 35.8)])
    f.add(f'<path class="facet" d="{smooth(fi)}"/>')

# --- zarys: ząb, części boczne trzonu z powierzchniami stawowymi górnymi, wyrostki poprzeczne, trzon ---
L = [(-2.0, 0.3), (-3.6, 1.15), (-4.6, 2.7), (-4.95, 5.0), (-4.85, 8.8), (-4.55, 11.2), (-4.3, 12.6), (-4.8, 13.7),
     (-5.9, 14.25), (-8.6, 14.35), (-12.0, 14.9), (-15.5, 15.9), (-18.8, 17.3), (-21.3, 18.8), (-22.6, 20.2),
     (-22.8, 21.6), (-23.8, 23.0), (-25.5, 24.6), (-26.6, 26.4), (-26.6, 28.0), (-25.6, 29.0), (-23.9, 28.8),
     (-22.3, 27.8), (-19.8, 27.5), (-16.4, 28.2), (-13.4, 29.4), (-10.9, 30.8), (-9.9, 32.6),
     (-9.7, 34.8), (-9.2, 36.6), (-7.1, 37.3), (-4.2, 37.9), (-1.9, 38.6)]
Lt = T(L)
f.add(f'<path class="bone" d="{smooth([P(0, 0)] + Lt + [P(0, 38.9)] + M(Lt))}"/>')

for s in (-1, 1):
    # delikatny cień pod nawisem części dźwigającej powierzchnię stawową górną
    sd = T([(s * 6.4, 17.6), (s * 10.0, 18.6), (s * 14.0, 19.8), (s * 18.0, 21.2), (s * 21.0, 22.4), (s * 18.0, 23.2),
            (s * 13.8, 22.0), (s * 9.8, 20.9), (s * 6.6, 19.9)])
    f.add(f'<path class="shade" d="{smooth(sd)}"/>')
    # powierzchnia stawowa górna – po bokach zęba, na części bocznej trzonu, opada skośnie ku dołowi i bocznie
    fs = T([(s * 6.1, 14.5), (s * 8.6, 14.62), (s * 12.0, 15.17), (s * 15.5, 16.17), (s * 18.8, 17.57), (s * 21.2, 19.0),
            (s * 22.3, 20.25), (s * 21.5, 21.3), (s * 18.8, 20.7), (s * 15.4, 19.6), (s * 11.8, 18.5), (s * 8.4, 17.7),
            (s * 6.1, 17.0), (s * 5.3, 15.6)])
    f.add(f'<path class="facet" d="{smooth(fs)}"/>')

# powierzchnia stawowa przednia zęba (owalna, do łuku przedniego C1)
fa = T([(0, 2.4), (-2.2, 3.0), (-3.0, 5.4), (-3.0, 8.4), (-2.2, 10.7), (0, 11.3), (2.2, 10.7), (3.0, 8.4), (3.0, 5.4), (2.2, 3.0)])
f.add(f'<path class="facet" d="{smooth(fa)}"/>')
# brzeg dolny trzonu (warga przednio-dolna)
lo = T([(-8.6, 35.6), (-6.5, 36.1), (-3.6, 36.6), (-1.6, 37.1), (0, 37.3)])
f.add(f'<path class="bonel" d="{smooth(lo + M(lo)[1:], closed=False)}"/>')

# --- podpisy ---
f.label(P(-0.6, 0.35), 'wierzchołek zęba', 'apex dentis', (58.0, 5.0), side='L')
f.label(P(3.95, 8.4), 'ząb', 'dens', (93.0, 21.0), side='R')
f.label(P(1.0, 6.4), 'powierzchnia stawowa przednia', 'facies articularis anterior', (93.0, 11.0), side='R')
f.label(P(-13.0, 16.2), 'powierzchnia stawowa górna', 'facies articularis superior', (41.0, 20.0), side='L')
f.label(P(-25.6, 27.4), 'wyrostek poprzeczny', 'processus transversus', (38.5, 34.0), side='L')
f.label(P(-15.8, 34.8), 'wyrostek stawowy dolny', 'processus articularis inferior', (41.0, 49.5), side='L')
f.label(P(4.0, 30.0), 'trzon kręgu', 'corpus vertebrae', (112.0, 44.0), side='R')
f.save()
