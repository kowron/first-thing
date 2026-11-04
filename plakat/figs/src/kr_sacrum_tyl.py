# Kość krzyżowa – widok od tyłu (powierzchnia grzbietowa). Prawa strona ciała po prawej stronie rysunku (kość symetryczna).
# Nazwy wg Bochenka, t. I, s. 233–236 (ryc. 146); lista podpisów z k_kregoslup.json (karta: Powierzchnia grzbietowa).
import sys; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
import math
from figlib import Fig, smooth, mirror

W, H = 150, 83
CX, OY, S = 75.0, 16.8, 0.6          # oś, poziom wzgórka (jak w widoku od przodu), skala
def P(x, y): return (CX + x * S, OY + y * S)
def T(pts): return [P(x, y) for x, y in pts]
def M(pts): return mirror(pts, CX)
def LR(pts, s): return [(s * x, y) for x, y in pts]

f = Fig('kr_sacrum_tyl', W, H, caption='kość krzyżowa · widok od tyłu (powierzchnia grzbietowa)')

# ---------- zarys (lewa połowa rysunku; mm kości) ----------
TOP = [(0, -7.0), (-6.0, -6.9), (-10.8, -6.4)]                                          # przedni brzeg pow. górnej S1 (w głębi)
SAP = [(-12.0, -7.4), (-13.0, -9.4), (-15.2, -10.6), (-17.8, -10.6), (-20.0, -9.2), (-21.3, -6.4), (-21.9, -2.6),
       (-22.8, 0.8)]
NOTCH = [(-24.8, 2.0), (-27.8, 1.2)]
LATT = [(-31.2, -1.8), (-35.2, -5.8), (-39.2, -8.4), (-43.4, -8.0), (-47.4, -5.2), (-50.8, -0.8), (-53.3, 4.6),
        (-54.8, 10.5), (-55.3, 16.5)]
LAT = [(-55.0, 22.0), (-53.4, 27.6), (-50.8, 33.2), (-47.6, 39.0), (-44.6, 45.0), (-41.6, 51.6), (-38.5, 58.6),
       (-35.2, 65.6), (-31.8, 72.4), (-28.4, 78.6), (-25.6, 83.2), (-23.6, 85.9), (-21.6, 87.0), (-17.8, 87.7),
       (-14.2, 89.0), (-11.6, 91.6), (-9.9, 94.6), (-8.4, 97.2), (-4.0, 98.4)]
half = T(TOP + SAP + NOTCH + LATT + LAT)
f.add(f'<path class="bone" d="{smooth(half + [P(0, 98.5)] + M(half)[:-1])}"/>')

# cień przy brzegach bocznych (powierzchnie boczne uciekają ku przodowi)
for s in (-1, 1):
    sh = LR([(54.6, 17), (53.0, 27.5), (50.2, 33.5), (46.9, 39.6), (43.9, 45.6), (41.0, 52.2), (38.0, 59.2), (34.6, 66.1),
             (30.8, 73.0), (27.0, 78.6), (24.3, 82.0), (22.6, 81.2), (25.4, 76.6), (29.0, 70.6), (32.6, 63.6), (35.9, 56.4),
             (38.8, 49.6), (41.8, 43.4), (45.0, 37.4), (48.2, 31.6), (50.6, 25.8), (51.8, 19.5)], s)
    f.add(f'<path class="shade" d="{smooth(T(sh))}"/>')

# ---------- guzowatość krzyżowa (chropowate pole w górnym rogu części bocznej) ----------
TUB = [(30.6, 1.0), (34.6, -4.0), (39.2, -6.6), (44.0, -6.0), (48.4, -2.8), (51.2, 2.6), (52.2, 9.0), (51.4, 15.6),
       (48.4, 20.4), (43.6, 21.0), (39.4, 17.4), (35.6, 11.6), (32.4, 6.0)]
STROKES = [(36.0, -1.6, 30), (40.6, -3.8, -20), (45.2, -2.6, 50), (49.0, 2.4, -35), (38.0, 3.4, -50), (42.8, 1.4, 15),
           (47.0, 6.8, 70), (50.0, 9.8, -10), (40.4, 8.2, 40), (44.8, 11.0, -60), (49.0, 14.6, 25), (37.6, 9.2, 0),
           (42.2, 15.0, 55), (46.4, 17.8, -25), (34.4, 3.4, 60), (44.2, 6.0, -5)]
for s in (-1, 1):
    f.add(f'<path class="shade" d="{smooth(T(LR(TUB, s)))}"/>')
    for (a, b, r) in STROKES:
        x, y = P(s * a, b)
        dx, dy = 0.42 * math.cos(math.radians(r * s)), 0.42 * math.sin(math.radians(r * s))
        f.add(f'<path class="bonel" d="M{x - dx:.2f},{y - dy:.2f} L{x + dx:.2f},{y + dy:.2f}"/>')

# ---------- podstawa widziana od tyłu: powierzchnia górna S1 (w głębi) i wejście do kanału krzyżowego ----------
top_s1 = T([(-10.8, -6.4), (-6.0, -6.9), (0, -7.0), (6.0, -6.9), (10.8, -6.4), (11.8, -3.6), (11.6, -0.4), (6.0, 0.0),
            (0, 0.1), (-6.0, 0.0), (-11.6, -0.4), (-11.8, -3.6)])
f.add(f'<path class="bone2" d="{smooth(top_s1)}"/>')
canal = T([(-11.6, -0.2), (-6.0, 0.3), (0, 0.4), (6.0, 0.3), (11.6, -0.2), (11.4, 3.6), (9.4, 7.0), (5.0, 9.4), (0, 10.0),
           (-5.0, 9.4), (-9.4, 7.0), (-11.4, 3.6)])
f.add(f'<path class="hole" d="{smooth(canal)}"/>')
f.add(f'<path class="shade" d="{smooth(T([(-11.2, 0.2), (0, 0.8), (11.2, 0.2), (9.8, 3.6), (0, 5.4), (-9.8, 3.6)]))}"/>')

# ---------- wyrostki stawowe górne (powierzchnie stawowe zwrócone ku tyłowi i przyśrodkowo) ----------
for s in (-1, 1):
    sap = LR([(12.0, -7.4), (13.0, -9.4), (15.2, -10.6), (17.8, -10.6), (20.0, -9.2), (21.3, -6.4), (21.9, -2.6),
              (22.0, 1.5), (20.8, 5.5), (18.4, 8.4), (15.4, 9.4), (13.0, 7.6), (12.0, 4.0), (11.6, -0.5), (11.6, -4.5)], s)
    f.add(f'<path class="bone" d="{smooth(T(sap))}"/>')
    x, y = P(s * 15.1, -3.4)
    f.add(f'<ellipse class="facet" cx="{x:.2f}" cy="{y:.2f}" rx="{2.6 * S:.2f}" ry="{5.0 * S:.2f}" '
          f'transform="rotate({s * 8} {x:.2f} {y:.2f})"/>')

# ---------- otwory krzyżowe grzbietowe (mniejsze, ostrzej zarysowane niż miedniczne) ----------
DOR = [(21.5, 23.0, 3.0, 3.9), (19.6, 42.0, 2.8, 3.5), (18.2, 59.5, 2.5, 3.0), (17.0, 74.5, 2.2, 2.6)]
for cx, cy, rx, ry in DOR:
    for s in (-1, 1):
        x, y = P(s * cx, cy)
        f.add(f'<ellipse class="hole" cx="{x:.2f}" cy="{y:.2f}" rx="{rx * S:.2f}" ry="{ry * S:.2f}" '
              f'transform="rotate({-s * 8} {x:.2f} {y:.2f})"/>')


def ridge(pts, s, w=None):
    """grzebień: linia szczytu; w – szerokość wąskiego cienia po prawej stronie (światło z lewej, jak przy grzebieniu pośrodkowym)"""
    if w:
        q = [(x + s * w, y) for x, y in pts]
        f.add(f'<path class="shade" d="{smooth(T(LR(pts, s)) + T(LR(q, s))[::-1])}"/>')
    f.add(f'<path class="bonel" d="{smooth(T(LR(pts, s)), closed=False)}"/>')


# grzebień krzyżowy boczny – guzki bocznie od otworów grzbietowych (szczątkowe wyrostki poprzeczne)
LCR = [(29.6, 12.0), (31.2, 17.4), (33.0, 23.0), (30.8, 29.4), (28.6, 35.0), (30.8, 42.0), (28.0, 48.6), (26.6, 53.4),
       (28.6, 59.5), (25.8, 66.0), (24.6, 70.2), (26.2, 74.5), (23.8, 79.6), (22.6, 83.4)]
# grzebień krzyżowy pośredni – rząd niskich guzków przyśrodkowo od otworów (zrośnięte wyrostki stawowe) → rożki krzyżowe
ICR = [(15.2, 9.6), (15.4, 16.0), (14.8, 23.0), (15.1, 30.6), (14.2, 36.0), (13.8, 42.0), (14.0, 49.0), (13.1, 54.0),
       (12.6, 59.5), (12.7, 65.6), (11.8, 70.0), (11.0, 74.6), (10.5, 79.0), (10.0, 81.6)]
for s in (-1, 1):
    ridge(LCR, s, w=2.2)
    ridge(ICR, s)

# ---------- rozwór krzyżowy (dolny otwór kanału, silnie wydłużony ku górze) i rożki krzyżowe ----------
HIA = [(-6.4, 98.0), (-6.2, 92.0), (-5.6, 85.0), (-4.8, 78.6), (-3.4, 74.0), (0, 72.2), (3.4, 74.0), (4.8, 78.6), (5.6, 85.0),
       (6.2, 92.0), (6.4, 98.0)]
hia = T(HIA)
q = P(0, 99.3)
f.add(f'<path class="bone2" d="{smooth(hia, closed=False)} Q{q[0]:.2f},{q[1]:.2f} {hia[0][0]:.2f},{hia[0][1]:.2f} Z"/>')
wall = [(-6.2, 92.0), (-5.6, 85.0), (-4.8, 78.6), (-3.4, 74.0), (0, 72.2), (3.4, 74.0), (4.8, 78.6), (5.6, 85.0), (6.2, 92.0)]
inner = [(4.4, 92.0), (3.6, 85.6), (2.6, 80.4), (1.4, 77.6), (0, 77.0), (-1.4, 77.6), (-2.6, 80.4), (-3.6, 85.6), (-4.4, 92.0)]
f.add(f'<path class="shade" d="{smooth(T(wall + inner))}"/>')
for s in (-1, 1):
    corn = T(LR([(5.8, 81.0), (8.4, 80.0), (11.0, 81.6), (12.0, 85.4), (11.4, 89.6), (10.0, 93.4), (8.2, 94.6), (6.6, 93.0),
                 (5.8, 89.0), (5.6, 85.0)], s))
    f.add(f'<path class="bone" d="{smooth(corn)}"/>')

# ---------- grzebień krzyżowy pośrodkowy – zwykle 4 podłużne guzki (zrośnięte wyrostki kolczyste S1–S4) ----------
f.add(f'<path class="bonel" d="M{P(0, 10.2)[0]:.2f},{P(0, 10.2)[1]:.2f} L{P(0, 71.6)[0]:.2f},{P(0, 71.6)[1]:.2f}"/>')
for yc, h in ((16.0, 6.2), (31.6, 6.6), (47.4, 6.4), (62.4, 5.6)):
    # podłużny guzek – wrzecionowaty, z cieniem po prawej stronie
    tb = [(0, yc - h), (-1.2, yc - h * 0.7), (-2.3, yc - h * 0.25), (-2.4, yc + h * 0.15), (-1.7, yc + h * 0.6)]
    tb = tb + [(0, yc + h)] + [(-x, y) for x, y in reversed(tb[1:])]
    sh = [(0.4, yc - h * 0.8), (2.6, yc - h * 0.35), (3.5, yc + h * 0.1), (2.6, yc + h * 0.65), (0.4, yc + h * 1.05)]
    f.add(f'<path class="shade" d="{smooth(T(sh))}"/>')
    f.add(f'<path class="bone" d="{smooth(T(tb))}"/>')

# ---------- podpisy ----------
TL, TR = 39.5, 108.5
f.label(P(-1.8, 6.0), 'kanał krzyżowy', 'canalis sacralis', (72.0, 4.2), side='L')
f.label(P(-42.4, 4.0), 'guzowatość krzyżowa', 'tuberositas sacralis', (TL, 16.0), side='L')
f.label(P(-30.4, 42.0), 'grzebień krzyżowy boczny', 'crista sacralis lateralis', (TL, 30.0), side='L')
f.label(P(-18.2, 59.5), 'otwory krzyżowe grzbietowe', 'foramina sacralia dorsalia', (TL, 46.0), side='L')
f.label(P(-9.2, 89.0), 'rożki krzyżowe', 'cornua sacralia', (TL, 62.5), side='L')
f.label(P(15.1, -3.4), 'wyrostki stawowe górne', 'processus articulares superiores', (TR, 4.2), side='R')
f.label(P(14.2, 36.0), 'grzebień krzyżowy pośredni', 'crista sacralis intermedia', (TR, 33.0), side='R')
f.label(P(2.6, 47.2), 'grzebień krzyżowy pośrodkowy', 'crista sacralis mediana', (TR, 45.0), side='R')
f.label(P(1.0, 81.0), 'rozwór krzyżowy', 'hiatus sacralis', (TR, 64.0), side='R')
f.save()
