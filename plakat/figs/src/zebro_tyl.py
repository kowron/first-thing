# KONIEC TYLNY ŻEBRA TYPOWEGO (prawe żebro VII) w powiększeniu – widok od tyłu, nieco od strony przyśrodkowej
# (widać powierzchnię stawową głowy). Widok od tyłu: prawa strona ciała po prawej stronie rysunku,
# więc głowa (przyśrodkowo) po lewej, kąt żebra (bocznie) po prawej.
# Nazwy wg Bochenka, t. I, s. 274–275 (ryc. 184).
import sys; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
import math, os
from figlib import Fig, smooth

W, H = 150, 80
S = 1.1                       # mm rysunku / mm kości
OX, OY = 60.0, 21.0           # przyśrodkowy koniec głowy (x) / górny brzeg głowy (y)
f = Fig('zebro_tyl', W, H, caption='koniec tylny żebra typowego (prawe żebro VII) · widok od tyłu i nieco od strony przyśrodkowej')


def P(x, y):
    return (OX + x * S, OY + y * S)


def TT(pts):
    return [P(x, y) for x, y in pts]


def bez(pts, t=0.5, n=14):
    m = len(pts)
    Q = [pts[0]] + pts + [pts[-1]]
    out = [pts[0]]
    for i in range(1, m):
        p0, p1, p2, p3 = Q[i - 1], Q[i], Q[i + 1], Q[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) * t / 3, p1[1] + (p2[1] - p0[1]) * t / 3)
        c2 = (p2[0] - (p3[0] - p1[0]) * t / 3, p2[1] - (p3[1] - p1[1]) * t / 3)
        for k in range(1, n + 1):
            u = k / n
            a, b, c, d = (1 - u) ** 3, 3 * (1 - u) ** 2 * u, 3 * (1 - u) * u ** 2, u ** 3
            out.append((a * p1[0] + b * c1[0] + c * c2[0] + d * p2[0], a * p1[1] + b * c1[1] + c * c2[1] + d * p2[1]))
    return out


def poly(pts, close=True):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + (' Z' if close else '')


# ---------- zarys: głowa → górny brzeg szyjki (grzebień) → górny brzeg trzonu → kąt → (przerwanie) →
#            dolny brzeg trzonu → guzek → dolny brzeg szyjki → głowa ----------
UPPER = [(0.9, 4.2), (1.6, 1.9), (3.4, 0.35), (6.0, 0.0), (8.4, 0.8), (10.2, 2.4), (13.0, 3.0), (18.0, 2.9),
         (24.0, 2.6), (30.0, 2.6), (37.0, 3.4), (45.0, 5.2), (53.0, 7.9), (59.5, 10.9), (63.8, 14.0), (66.6, 18.0),
         (68.6, 23.0), (70.0, 28.6), (71.0, 33.0)]
LOWER = [(62.6, 35.6), (61.4, 31.0), (59.4, 26.8), (56.2, 23.0), (51.0, 20.0), (44.0, 17.6), (39.4, 16.8),
         (36.8, 17.6), (32.6, 18.2), (28.6, 17.0), (25.8, 13.8), (23.0, 10.5), (18.0, 9.6), (12.6, 9.8), (9.6, 10.9),
         (7.4, 12.3), (4.6, 12.7), (2.0, 11.3), (0.6, 8.6), (0.0, 6.1)]
BREAK = [(71.0, 33.0), (69.6, 33.3), (67.9, 34.6), (66.0, 34.2), (64.2, 35.0), (62.6, 35.6)]
up = bez(TT(UPPER), n=12)
lo = bez(TT(LOWER), n=12)
br = bez(TT(BREAK), n=6)
outline = up + br[1:-1] + lo
f.add(f'<path class="bone" d="{poly(outline)}"/>')
# przerwanie – powierzchnia złamu (inna płaszczyzna kości)
cut = TT([(71.0, 33.0), (69.6, 33.3), (67.9, 34.6), (66.0, 34.2), (64.2, 35.0), (62.6, 35.6),
          (63.6, 36.6), (65.6, 36.9), (67.6, 36.2), (69.6, 35.6), (71.0, 34.5)])
f.add(f'<path class="bone2" d="{smooth(cut)}"/>')

# ---------- głowa: powierzchnia stawowa (górna mniejsza, dolna większa) podzielona grzebieniem głowy ----------
HEAD_EDGE = [(3.0, 0.45), (1.6, 1.9), (0.8, 3.6), (0.05, 5.0), (0.0, 6.1), (0.55, 8.4), (1.8, 10.9), (3.6, 12.35)]
HEAD_IN = [(3.6, 12.35), (4.6, 10.6), (5.0, 8.2), (4.7, 6.0), (4.4, 4.0), (4.2, 1.9), (3.0, 0.45)]
CREST_Y = 4.9
up_f = TT([(3.0, 0.45), (1.6, 1.9), (0.8, 3.6), (0.15, CREST_Y), (4.55, CREST_Y + 0.15), (4.4, 3.4), (4.2, 1.9)])
lo_f = TT([(0.15, CREST_Y), (0.0, 6.1), (0.55, 8.4), (1.8, 10.9), (3.6, 12.35), (4.6, 10.6), (5.0, 8.2),
           (4.75, 6.2), (4.55, CREST_Y + 0.15)])
f.add(f'<path class="facet" d="{smooth(up_f)}"/>')
f.add(f'<path class="facet" d="{smooth(lo_f)}"/>')
# grzebień głowy – poziomy wał między powierzchniami
c1, c2 = P(-0.25, CREST_Y - 0.05), P(4.6, CREST_Y + 0.12)
f.add(f'<path class="bone2" d="M{P(-0.35, CREST_Y)[0]:.2f},{P(-0.35, CREST_Y)[1]:.2f} '
      f'Q{P(2.2, CREST_Y - 0.55)[0]:.2f},{P(2.2, CREST_Y - 0.55)[1]:.2f} {P(4.6, CREST_Y - 0.15)[0]:.2f},{P(4.6, CREST_Y - 0.15)[1]:.2f} '
      f'L{P(4.6, CREST_Y + 0.35)[0]:.2f},{P(4.6, CREST_Y + 0.35)[1]:.2f} '
      f'Q{P(2.2, CREST_Y + 0.45)[0]:.2f},{P(2.2, CREST_Y + 0.45)[1]:.2f} {P(-0.35, CREST_Y)[0]:.2f},{P(-0.35, CREST_Y)[1]:.2f} Z"/>')

# granica głowy i szyjki (delikatna)
f.add(f'<path class="bonel" d="{smooth(TT([(8.4, 1.0), (7.6, 4.0), (7.4, 7.5), (7.9, 11.6)]), closed=False)}"/>')

# ---------- szyjka: grzebień szyjki na górnym brzegu (ostry wał) ----------
f.add(f'<path class="bonel" d="{smooth(TT([(10.9, 3.75), (15.0, 3.85), (20.0, 3.7), (25.0, 3.45), (29.5, 3.45)]), closed=False)}"/>')

# ---------- guzek żebra: wyniosłość ku tyłowi i dołowi; powierzchnia stawowa w części przyśrodkowo-dolnej ----------
tub_top = TT([(25.6, 12.6), (27.4, 9.4), (30.6, 7.9), (34.4, 8.0), (37.4, 9.8), (38.9, 13.0), (38.6, 16.4)])
f.add(f'<path class="bonel" d="{smooth(tub_top, closed=False)}"/>')
f.add(f'<path class="shade" d="{smooth(TT([(34.6, 9.6), (37.6, 11.2), (38.7, 14.4), (37.2, 17.3), (33.8, 17.9), (35.4, 14.6)]))}"/>')
f.add(f'<path class="facet" d="{smooth(TT([(26.7, 12.4), (28.4, 10.2), (31.4, 10.0), (33.3, 12.2), (32.8, 15.2), (30.0, 16.5), (27.6, 15.3)]))}"/>')
# chropowata część boczna guzka (przyczep więzadła żebrowo-poprzecznego bocznego) – kreseczki
for x, y in [(35.0, 11.0), (36.4, 12.9), (35.2, 14.8)]:
    a_, b_ = P(x - 0.5, y + 0.2), P(x + 0.5, y - 0.2)
    f.add(f'<path class="bonel" d="M{a_[0]:.2f},{a_[1]:.2f} L{b_[0]:.2f},{b_[1]:.2f}"/>')

# ---------- kąt żebra: linia kąta na powierzchni zewnętrznej ----------
f.add(f'<path class="bonel" d="{smooth(TT([(62.6, 13.0), (60.2, 17.0), (58.0, 22.0)]), closed=False)}"/>')

# ---------- podpisy ----------
TL = 55.0
f.label(P(6.0, 2.6), 'głowa żebra', 'caput costae', (TL, 12.5), side='L')
f.label(P(2.3, 2.9), 'powierzchnia stawowa głowy żebra górna', 'facies articularis capitis costae superior', (TL, 21.0), side='L')
f.label(P(0.3, CREST_Y), 'grzebień głowy żebra', 'crista capitis costae', (TL, 29.5), side='L')
f.label(P(2.2, 8.6), 'powierzchnia stawowa głowy żebra dolna', 'facies articularis capitis costae inferior', (TL, 38.0), side='L')
f.label(P(14.5, 2.95), 'grzebień szyjki żebra', 'crista colli costae', (71.0, 8.5), side='R')
f.label(P(36.6, 10.4), 'guzek żebra', 'tuberculum costae', (100.5, 8.5), side='R')
f.label(P(64.0, 13.6), 'kąt żebra', 'angulus costae', (124.0, 8.5), side='R')
f.label(P(17.0, 6.3), 'szyjka żebra', 'collum costae', (74.5, 63.0), side='L')
f.label(P(30.0, 13.3), 'powierzchnia stawowa guzka żebra', 'facies articularis tuberculi costae', (91.0, 63.0), side='R')

if os.environ.get('PTS'):
    for nm, (x, y) in {'head_top': (3.0, 0.45), 'crest': (0.0, CREST_Y), 'upper_facet': (2.4, 2.8),
                       'lower_facet': (2.4, 8.4), 'head_body': (6.0, 6.0), 'neck_mid': (17.0, 6.0),
                       'neck_crest': (20.0, 1.6), 'tub_facet': (29.6, 11.6), 'tub': (34.5, 15.0),
                       'angle': (64.0, 13.6), 'body': (66.0, 28.0), 'break': (67.0, 35.0)}.items():
        print(nm, tuple(round(v, 1) for v in P(x, y)))

f.save()
