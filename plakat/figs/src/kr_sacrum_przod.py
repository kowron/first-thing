# Kość krzyżowa – widok od przodu (powierzchnia miedniczna). Prawa strona ciała po lewej stronie rysunku (kość symetryczna).
# Nazwy wg Bochenka, t. I, s. 232–235 (ryc. 145); listy podpisów z k_kregoslup.json (karty: Powierzchnia miedniczna,
# Kształt i położenie, Podstawa).
import sys; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth, mirror

W, H = 150, 79
CX, OY, S = 75.0, 13.0, 0.6          # oś, wzgórek (przedni brzeg powierzchni górnej S1), skala (mm rysunku / mm kości)
def P(x, y): return (CX + x * S, OY + y * S)
def T(pts): return [P(x, y) for x, y in pts]
def M(pts): return mirror(pts, CX)

f = Fig('kr_sacrum_przod', W, H, caption='kość krzyżowa · widok od przodu (powierzchnia miedniczna)')

# ---------- zarys (lewa połowa rysunku, w mm kości: od środka górnego brzegu do wierzchołka) ----------
TOP = [(0, -4.8), (-12, -4.45), (-19.5, -3.5), (-24.5, -2.4)]                 # tylny brzeg powierzchni górnej S1
ALA = [(-29.5, -3.0), (-34.6, -4.4), (-38.9, -5.3), (-42.7, -5.2), (-46.3, -3.8), (-49.8, -0.4), (-52.7, 4.5),
       (-54.6, 10.4), (-55.2, 16.4)]                                         # górny i boczny brzeg skrzydła
LAT = [(-55.0, 22.0), (-53.4, 27.6), (-50.8, 33.2), (-47.6, 39.0), (-44.6, 45.0), (-41.6, 51.6), (-38.5, 58.6),
       (-35.2, 65.6), (-31.8, 72.4), (-28.4, 78.6), (-25.6, 83.2), (-23.6, 85.9), (-21.6, 87.0), (-17.8, 87.7),
       (-14.2, 89.0), (-11.6, 91.6), (-9.9, 94.6), (-8.4, 97.2), (-4.0, 98.4)]          # … kąt boczny dolny → wierzchołek                # brzeg boczny → wierzchołek
half = T(TOP + ALA + LAT)
outline = half + [P(0, 98.5)] + M(half)[:-1]
f.add(f'<path class="bone" d="{smooth(outline)}"/>')

# delikatny cień wzdłuż brzegów bocznych (powierzchnie boczne uciekają ku tyłowi)
for s in (-1, 1):
    sh = T([(s * 54.6, 17), (s * 53.0, 27.5), (s * 50.2, 33.5), (s * 46.9, 39.6), (s * 43.9, 45.6), (s * 41.0, 52.2),
            (s * 38.0, 59.2), (s * 34.6, 66.1), (s * 30.8, 73.0), (s * 27.0, 78.6), (s * 24.3, 82.0),
            (s * 22.6, 81.2), (s * 25.4, 76.6), (s * 29.0, 70.6), (s * 32.6, 63.6), (s * 35.9, 56.4), (s * 38.8, 49.6),
            (s * 41.8, 43.4), (s * 45.0, 37.4), (s * 48.2, 31.6), (s * 50.6, 25.8), (s * 51.8, 19.5)])
    f.add(f'<path class="shade" d="{smooth(sh)}"/>')

# ---------- podstawa: powierzchnia górna trzonu S1 i górne powierzchnie skrzydeł (widziane skośnie z przodu i z góry) ----------
for s in (-1, 1):
    up = [(s * x, y) for x, y in [(-24.5, -2.4)] + ALA[:-1] + [(-54.9, 12.6)]]
    lo = [(s * x, y) for x, y in [(-51.6, 9.4), (-47.2, 6.0), (-42.0, 3.4), (-36.0, 1.2), (-30.0, -0.7)]]
    f.add(f'<path class="bone2" d="{smooth(T(up + lo))}"/>')
x, y = P(0, -2.4)
f.add(f'<ellipse class="bone2" cx="{x:.2f}" cy="{y:.2f}" rx="{24.5 * S:.2f}" ry="{2.4 * S:.2f}"/>')

def crescent(x, y, rx, ry, s, k=0.42, n=24):
    """półksiężyc wewnątrz elipsy po stronie bocznej (s=-1 lewa, +1 prawa strona rysunku)"""
    import math
    out = [(x + s * rx * math.cos(t), y + ry * math.sin(t)) for t in [math.pi * (i / n - 0.5) for i in range(n + 1)]]
    inn = [(x + s * rx * k * math.cos(t), y + ry * 0.97 * math.sin(t)) for t in [math.pi * (0.5 - i / n) for i in range(n + 1)]]
    return 'M' + ' L'.join(f'{a:.2f},{b:.2f}' for a, b in out + inn) + ' Z'


# ---------- otwory krzyżowe miedniczne (4 pary, ku dołowi coraz mniejsze) i kresy poprzeczne ----------
FOR = [(23.6, 22.0, 4.3, 5.0), (21.6, 41.0, 3.8, 4.4), (19.6, 58.5, 3.2, 3.7), (18.0, 73.6, 2.6, 3.0)]   # (|x|, y, rx, ry)
for cx, cy, rx, ry in FOR:
    for s in (-1, 1):
        # płytka bruzda biegnąca bocznie od otworu (gałąź przednia nerwu krzyżowego)
        g = T([(s * (cx + rx * 0.7), cy - ry * 0.35), (s * (cx + rx + 4.5), cy + 0.4), (s * (cx + rx + 8.5), cy + 2.2),
               (s * (cx + rx + 4.0), cy + ry * 0.75), (s * (cx + rx * 0.7), cy + ry * 0.5)])
        f.add(f'<path class="shade" d="{smooth(g)}"/>')
        x, y = P(s * cx, cy)
        rot = f'transform="rotate({-s * 12} {x:.2f} {y:.2f})"'
        f.add(f'<ellipse class="hole" cx="{x:.2f}" cy="{y:.2f}" rx="{rx * S:.2f}" ry="{ry * S:.2f}" {rot}/>')
        f.add(f'<path class="shade" d="{crescent(x, y, rx * S, ry * S, s)}" {rot}/>')
    # kresa poprzeczna (ślad zrostu trzonów) – od otworu do otworu, lekko wygięta ku dołowi
    a, b, c = P(-(cx - rx * 0.92), cy + 0.6), P(0, cy + 2.6), P(cx - rx * 0.92, cy + 0.6)
    f.add(f'<path class="bonel" d="M{a[0]:.2f},{a[1]:.2f} Q{b[0]:.2f},{b[1] + (b[1] - a[1]):.2f} {c[0]:.2f},{c[1]:.2f}"/>')

# wierzchołek – owalna powierzchnia do połączenia z kością guziczną
x, y = P(0, 96.5)
f.add(f'<ellipse class="bone2" cx="{x:.2f}" cy="{y:.2f}" rx="{7.9 * S:.2f}" ry="{2.0 * S:.2f}"/>')

# zrośnięte trzony S1–S5 (oznaczenie)
for t, yy in (('S1', 13.5), ('S2', 33.5), ('S3', 52.5), ('S4', 68.5), ('S5', 85.5)):
    f.text(CX, P(0, yy)[1], t, cls='notec')

# ---------- podpisy ----------
TL, TR = 39.5, 110.5
f.label(P(-9.0, -2.3), 'podstawa kości krzyżowej', 'basis ossis sacri', (TL, 5.0), side='L')
f.label(P(-37.0, -1.6), 'skrzydło kości krzyżowej', 'ala sacralis', (TL, 15.5), side='L')
f.label(P(-38.5, 31.0), 'części boczne', 'partes laterales', (TL, 30.0), side='L')
f.label(P(-6.0, 43.6), 'kresy poprzeczne', 'lineae transversae', (TL, 50.0), side='L')
f.label(P(1.0, 0.05), 'wzgórek', 'promontorium', (TR, 5.0), side='R')
f.label(P(7.0, 31.5), 'powierzchnia miedniczna', 'facies pelvina', (TR, 30.0), side='R')
f.label(P(21.6, 41.0), 'otwory krzyżowe miedniczne', 'foramina sacralia pelvina', (TR, 40.5), side='R')
f.label(P(2.5, 97.8), 'wierzchołek kości krzyżowej', 'apex ossis sacri', (TR, 66.0), side='R')
f.save()
