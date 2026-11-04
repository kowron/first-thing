# Kręg szczytowy (C1, atlas) – widok od góry (przód ku górze). Nazwy wg Bochenka (s. 224–225, ryc. 136).
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth, mirror

W, H = 150, 62
CX, OY, S = 75, 14.0, 0.85          # oś, przedni brzeg guzka przedniego, skala
def T(pts): return [(CX + x * S, OY + y * S) for x, y in pts]
def P(x, y): return (CX + x * S, OY + y * S)
def M(pts): return mirror(pts, CX)

f = Fig('kr_c1_gora', W, H, caption='kręg szczytowy (C1) · widok od góry (przód ku górze)')

# --- zarys: łuk przedni, części boczne z wyrostkami poprzecznymi, łuk tylny (lewa połowa, potem odbicie) ---
L = [(0, -0.2), (-1.9, 0.3), (-3.5, 1.4), (-6.5, 2.5), (-10.0, 4.1), (-13.0, 6.0), (-16.0, 7.5), (-19.5, 9.0), (-22.2, 10.9),
     (-25.0, 12.1), (-29.0, 12.5), (-33.0, 12.5), (-36.2, 13.5), (-37.6, 16.0), (-37.4, 19.0), (-35.6, 21.0), (-32.0, 21.6),
     (-28.5, 22.6), (-25.6, 24.0), (-23.2, 26.0), (-21.6, 29.0), (-19.0, 33.6), (-15.0, 38.6), (-10.0, 42.4), (-5.2, 44.6),
     (-2.6, 45.6), (-1.2, 46.8)]
Lt = T(L)
f.add(f'<path class="bone" d="{smooth(Lt + [P(0, 47.1)] + M(Lt))}"/>')

# otwór kręgowy: mała część przednia (dla zęba) i duża część tylna; części boczne wpuklają się do środka
F = T([(0, 7.0), (-4.0, 7.2), (-6.6, 8.0), (-8.7, 9.8), (-9.5, 12.0), (-9.1, 14.6), (-10.2, 17.6), (-12.4, 21.0), (-13.8, 25.0),
       (-13.9, 29.0), (-12.2, 33.4), (-8.6, 37.4), (-4.2, 39.9)])
f.add(f'<path class="hole" d="{smooth(F + [P(0, 40.6)] + M(F)[:-1])}"/>')

# dołek zębowy (powierzchnia stawowa na tylnej stronie łuku przedniego)
fd = T([(-4.7, 7.15), (-3.0, 6.05), (0, 5.65), (3.0, 6.05), (4.7, 7.15), (3.0, 7.25), (0, 7.05), (-3.0, 7.25)])
f.add(f'<path class="facet" d="{smooth(fd)}"/>')

for s in (-1, 1):
    # bruzda tętnicy kręgowej – na górnej powierzchni łuku tylnego, tuż za częścią boczną
    g = T([(s * 21.9, 27.8), (s * 20.4, 31.4), (s * 17.8, 35.0), (s * 15.7, 36.0), (s * 14.4, 34.6), (s * 15.0, 31.4), (s * 16.2, 28.0), (s * 18.6, 26.6)])
    f.add(f'<path class="bone2" d="{smooth(g)}"/>')
    # otwór wyrostka poprzecznego
    x, y = P(s * 28.0, 17.2)
    f.add(f'<circle class="hole" cx="{x:.2f}" cy="{y:.2f}" r="{3.0 * S:.2f}"/>')
    # dołek stawowy górny: owalny (nerkowaty), długie osie zbiegają się ku przodowi
    A, B = (s * 11.6, 8.6), (s * 19.6, 25.6)
    Lx = math.dist(A, B); ax = ((B[0] - A[0]) / Lx, (B[1] - A[1]) / Lx); n = (s * abs(ax[1]), -abs(ax[0]))
    uv = [(0, 0), (2, 3.4), (6, 5.0), (10, 5.3), (14, 4.8), (17.4, 3.2), (Lx, 0.3), (17.4, -2.6), (14, -3.2), (10, -2.2), (6, -2.9), (2, -2.6)]
    fov = T([(A[0] + u * ax[0] + v * n[0], A[1] + u * ax[1] + v * n[1]) for u, v in uv])
    f.add(f'<path class="facet" d="{smooth(fov)}"/>')


# --- podpisy ---
TL, TR = 40, 110
f.label(P(0, 0.4), 'guzek przedni', 'tuberculum anterius', (CX - 1.6, 5.5), side='L')
f.label(P(8.6, 3.7), 'łuk przedni', 'arcus anterior', (TR, 12.5), side='R')
f.label(P(2.6, 6.5), 'dołek zębowy', 'fovea dentis', (TR, 20.0), side='R')
f.label(P(28.0, 17.2), 'otwór wyrostka poprzecznego', 'foramen transversarium', (109.5, 29.5), side='R')
f.label(P(7.0, 31.0), 'otwór kręgowy', 'foramen vertebrale', (TR, 38.5), side='R')
f.label(P(-13.4, 38.6), 'łuk tylny', 'arcus posterior', (TL, 50.0), side='L')
f.label(P(0.9, 46.4), 'guzek tylny', 'tuberculum posterius', (TR, 48.0), side='R')
f.label(P(-21.0, 10.6), 'część boczna', 'massa lateralis', (TL, 14.0), side='L')
f.label(P(-16.2, 17.6), 'dołek stawowy górny', 'fovea articularis superior', (TL, 23.0), side='L')
f.label(P(-35.4, 18.0), 'wyrostek poprzeczny', 'processus transversus', (TL, 32.0), side='L')
f.label(P(-17.9, 31.0), 'bruzda tętnicy kręgowej', 'sulcus arteriae vertebralis', (TL, 41.0), side='L')
f.save()
