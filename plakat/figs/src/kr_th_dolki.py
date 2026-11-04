# Dołki żebrowe kręgów piersiowych – zestawienie: Th1, kręg typowy (Th2–Th9), Th10, Th11, Th12; widok z boku
# (od strony lewej; przód w lewo). Schemat własny. Wg Bochenka (s. 228–231, ryc. 143) – karty Th1, „Kręg piersiowy
# typowy”, Th10, Th11, Th12 w k_kregoslup.json:
#  Th1 – dołek żebrowy górny poniżej krawędzi górnej (sam, dla głowy żebra I), dołek dolny na krawędzi dolnej;
#  Th2–Th9 – dołek górny (większy) i dolny na krawędziach trzonu, tuż u nasady łuku;
#  Th10 – czasem tylko 1 dołek, przy górnym brzegu; dołek wyrostka poprzecznego niestały (linia przerywana);
#  Th11, Th12 – 1 dołek w środku powierzchni bocznej trzonu; wyrostek poprzeczny bez dołka, niezgrubiały.
# Dołki wyrostka poprzecznego: Th1–Th9 są (zgrubiały koniec wyrostka). Trzony rosną ku dołowi.
import sys; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 160, 70
S = 0.47                     # mm rysunku / mm kości (wszystkie kręgi w tej samej skali)
YB = 24.0                    # poziom górnej powierzchni trzonów

f = Fig('kr_th_dolki', W, H, caption='dołki żebrowe kręgów piersiowych · widok z boku (od strony lewej, przód w lewo)')

# ---------------- zarysy (mm kości; x=0 przednia powierzchnia trzonu, y=0 górna powierzchnia trzonu) ----------------
V = {}
V['Th1'] = dict(
    O=[(0.6, 0.1), (8.0, -0.15), (14.2, -0.1), (16.1, 0.4),
       (17.1, 1.3), (18.3, 1.7), (19.4, 1.1), (20.1, -0.4),
       (20.7, -2.6), (21.6, -4.5), (22.8, -5.5), (24.2, -5.3), (25.0, -3.8), (25.6, -1.9),
       (27.4, -0.8), (30.0, 0.3),
       (36.0, 2.6), (43.0, 5.4), (49.0, 8.0), (52.6, 9.6),
       (53.8, 11.2), (53.4, 13.2), (51.4, 13.8),
       (46.0, 12.6), (40.0, 11.4), (34.4, 10.8), (30.0, 11.2),
       (28.9, 13.0), (28.2, 15.8), (26.9, 18.0), (25.3, 17.9), (24.4, 15.6), (23.8, 12.8),
       (22.6, 10.3), (21.0, 9.3), (19.4, 9.9), (18.0, 11.3), (16.9, 12.9), (16.0, 13.9),
       (12.0, 14.05), (6.0, 13.95), (0.8, 13.6),
       (0.1, 12.8), (0.65, 9.6), (0.95, 6.8), (0.6, 3.6), (0.05, 0.9)],
    tp=[(21.4, 2.6), (22.2, 0.4), (24.2, -0.6), (26.6, -0.3), (28.6, 1.2), (29.4, 3.6), (28.6, 6.0), (26.4, 7.4),
        (23.8, 7.2), (21.8, 5.4)],
    tpf=('facet', 23.2, 3.4, 1.5, 2.6),                      # dołek żebrowy wyrostka poprzecznego
    fov=[('round', 12.3, 4.0, 2.45, 2.3),                    # dołek górny – cały, poniżej krawędzi górnej
         ('low', 11.4, 15.8, 13.95, 2.1)],                   # dołek dolny – na krawędzi dolnej
)
V['typ'] = dict(                                             # jak w kr_th_bok.py (kręg piersiowy typowy)
    O=[(0.8, 0.15), (8.0, -0.15), (16.0, -0.25), (22.6, -0.15), (24.7, 0.3),
       (25.9, 1.3), (27.3, 1.75), (28.6, 1.2), (29.5, -0.3),
       (30.4, -3.0), (31.4, -5.4), (32.6, -6.9), (34.0, -7.3), (35.4, -6.4), (36.3, -4.2),
       (37.3, -2.2), (39.4, -0.9), (41.8, 0.0), (43.6, 2.0),
       (46.2, 8.6), (49.3, 17.2), (52.4, 26.2), (55.0, 33.8), (56.5, 38.2),
       (56.4, 41.2), (54.6, 42.7), (52.6, 41.8), (51.3, 38.6),
       (49.2, 33.2), (46.6, 27.6), (43.6, 22.4), (40.9, 18.6), (38.9, 16.9),
       (37.5, 18.4), (36.6, 21.4), (35.4, 24.4), (33.5, 25.7), (31.7, 24.9),
       (30.9, 21.8), (30.3, 17.8), (29.5, 14.4),
       (28.1, 12.2), (26.7, 12.4), (25.7, 14.1), (25.2, 16.7), (24.8, 18.9),
       (23.2, 19.75), (16.0, 19.7), (8.0, 19.3), (1.0, 18.75),
       (0.15, 17.9), (0.8, 13.4), (1.25, 9.4), (0.75, 5.0), (0.05, 1.1)],
    tp=[(34.6, 3.0), (35.6, 0.6), (38.0, -0.6), (41.0, -0.4), (43.6, 1.2), (44.8, 4.0), (44.2, 7.0), (41.8, 9.0),
        (38.6, 9.2), (35.8, 7.6)],
    tpf=('facet', 37.0, 4.3, 1.85, 3.0),
    fov=[('up', 17.7, 25.5, -0.1, 4.4),                       # dołek górny – na krawędzi górnej (większy)
         ('low', 19.8, 24.9, 19.72, 3.2)],                   # dołek dolny – na krawędzi dolnej
)
V['Th10'] = dict(
    O=[(0.8, 0.15), (9.0, -0.2), (18.0, -0.3), (26.2, -0.2), (28.4, 0.4),
       (29.7, 1.5), (31.3, 2.0), (32.8, 1.4), (33.8, -0.3),
       (34.6, -3.0), (35.5, -5.6), (36.8, -7.2), (38.3, -7.6), (39.7, -6.8), (40.5, -4.8),
       (41.4, -2.6), (43.4, -1.0), (46.0, 0.2),
       (50.5, 2.8), (55.5, 6.2), (59.0, 9.0),
       (60.6, 10.6), (61.0, 13.6), (60.0, 16.6), (58.0, 17.8),
       (54.4, 16.4), (50.4, 15.0), (46.6, 15.2), (44.0, 16.6),
       (42.8, 19.0), (42.0, 22.6), (40.6, 25.4), (38.8, 25.8), (37.6, 23.8), (37.0, 20.4), (36.4, 17.2),
       (35.2, 14.4), (33.6, 13.4), (32.0, 14.0), (30.8, 16.0), (29.4, 18.8), (28.8, 21.4),
       (26.4, 22.0), (18.0, 22.1), (9.0, 21.8), (1.0, 21.2),
       (0.15, 20.3), (0.85, 15.0), (1.3, 10.8), (0.8, 5.6), (0.05, 1.2)],
    tp=[(38.6, 3.2), (39.6, 0.9), (41.8, -0.1), (44.4, 0.2), (46.6, 1.8), (47.4, 4.4), (46.6, 7.0), (44.2, 8.4),
        (41.4, 8.2), (39.4, 6.4)],
    tpf=('dim', 41.2, 4.2, 1.95, 3.0),                        # dołek wyrostka poprzecznego – niestały
    fov=[('round', 25.0, 3.3, 2.9, 2.7)],                    # czasem tylko 1 dołek – przy górnym brzegu
)
V['Th11'] = dict(
    O=[(0.8, 0.15), (9.0, -0.2), (19.0, -0.3), (27.2, -0.2), (29.4, 0.4),
       (30.7, 1.5), (32.4, 2.0), (33.9, 1.4), (34.9, -0.2),
       (35.7, -3.0), (36.6, -5.8), (37.9, -7.6), (39.4, -8.1), (40.9, -7.3), (41.7, -5.4),
       (42.4, -3.2), (44.2, -1.0), (46.5, 0.6),
       (52.0, 2.4), (57.5, 4.6), (61.4, 6.4),
       (63.2, 7.8), (63.8, 11.0), (63.0, 14.4), (60.8, 15.8),
       (56.6, 15.0), (52.0, 14.4), (48.0, 15.0), (45.2, 16.6),
       (44.0, 19.2), (43.2, 23.0), (41.8, 26.2), (39.9, 26.7), (38.7, 24.6), (38.1, 21.0), (37.4, 17.6),
       (36.2, 14.8), (34.6, 13.8), (33.0, 14.4), (31.8, 16.6), (30.4, 19.6), (29.8, 22.4),
       (27.4, 23.0), (19.0, 23.1), (9.0, 22.8), (1.0, 22.2),
       (0.15, 21.3), (0.85, 15.8), (1.3, 11.4), (0.8, 5.8), (0.05, 1.2)],
    tp=[(40.6, 4.4), (41.4, 2.4), (43.4, 1.6), (45.6, 2.2), (46.6, 4.4), (46.0, 6.8), (44.0, 8.0), (41.8, 7.4)],
    tpf=None,                                                # bez dołka
    fov=[('round', 19.4, 11.5, 2.9, 2.7)],                   # 1 dołek – w środku powierzchni bocznej
)
V['Th12'] = dict(                                            # jak w kr_th12_bok.py
    O=[(0.9, 0.15), (10.0, -0.2), (20.0, -0.3), (28.6, -0.2), (30.8, 0.4),
       (32.2, 1.6), (34.0, 2.1), (35.6, 1.5), (36.6, 0.0),
       (37.4, -3.2), (38.3, -6.0), (39.6, -8.0), (41.2, -8.7), (42.8, -8.1), (43.8, -6.3),
       (44.3, -4.4), (45.9, -3.7), (47.5, -2.1), (47.9, 0.3), (46.9, 2.0),
       (47.6, 3.3), (50.4, 3.7), (56.0, 3.6), (62.0, 3.5), (66.2, 3.3),
       (68.6, 4.3), (69.8, 7.4), (70.0, 11.6), (69.4, 15.4), (67.8, 18.0), (65.2, 18.7),
       (60.4, 17.7), (55.6, 16.8), (51.8, 17.0), (48.9, 18.3),
       (47.7, 21.0), (47.1, 25.6), (46.1, 29.6), (44.5, 31.6), (42.5, 31.5), (41.1, 29.2),
       (40.3, 25.0), (39.7, 21.0), (38.9, 17.6),
       (37.5, 15.0), (35.7, 14.0), (33.9, 14.8), (32.5, 17.4), (31.7, 20.6), (31.2, 23.5),
       (29.4, 24.55), (20.0, 24.7), (10.0, 24.4), (1.1, 23.8),
       (0.15, 22.8), (0.9, 17.0), (1.35, 12.0), (0.85, 6.4), (0.05, 1.2)],
    tp=[(39.8, 5.6), (40.8, 3.2), (43.0, 2.3), (45.4, 3.0), (46.5, 5.4), (46.0, 8.2), (43.8, 9.7), (41.4, 9.2)],
    tpf=None,
    fov=[('round', 21.0, 11.8, 3.2, 2.9)],
)

ORDER = ['Th1', 'typ', 'Th10', 'Th11', 'Th12']
NAME = {'Th1': 'Th1', 'typ': 'Th2–Th9', 'Th10': 'Th10', 'Th11': 'Th11', 'Th12': 'Th12'}
NOTES = {
    'Th1':  ['dołek górny – bez uzupełnienia,', 'poniżej krawędzi górnej', 'na wyrostku: jest'],
    'typ':  ['dołek górny i dolny', 'na krawędziach trzonu', 'na wyrostku: jest'],
    'Th10': ['czasem tylko 1 dołek', 'przy górnym brzegu', 'na wyrostku: niestały'],
    'Th11': ['1 dołek – w środku', 'powierzchni bocznej', 'na wyrostku: brak'],
    'Th12': ['1 dołek – w środku', 'powierzchni bocznej', 'na wyrostku: brak'],
}

# rozmieszczenie w poziomie: równe odstępy między zarysami
ext = {k: (min(x for x, y in V[k]['O']), max(x for x, y in V[k]['O'])) for k in ORDER}
tot = sum((b - a) * S for a, b in ext.values())
MARG = 2.6
GAP = (W - 2 * MARG - tot) / (len(ORDER) - 1)
X = {}
x = MARG
for k in ORDER:
    X[k] = x - ext[k][0] * S
    x += (ext[k][1] - ext[k][0]) * S + GAP

def P(k, bx, by): return (X[k] + bx * S, YB + by * S)
def T(k, pts): return [P(k, bx, by) for bx, by in pts]

for k in ORDER:
    v = V[k]
    f.add(f'<path class="bone" d="{smooth(T(k, v["O"]))}"/>')
    # dołki żebrowe na trzonie
    for fv in v['fov']:
        if fv[0] == 'round':
            _, cx, cy, rx, ry = fv
            x, y = P(k, cx, cy)
            f.add(f'<ellipse class="facet" cx="{x:.2f}" cy="{y:.2f}" rx="{rx * S:.2f}" ry="{ry * S:.2f}"/>')
        else:                                   # półowalny dołek na krawędzi trzonu
            kind, xa, xb, ye, hh = fv
            sg = 1 if kind == 'up' else -1
            a, b = P(k, xa, ye), P(k, xb, ye + (0.6 if kind == 'up' else -0.85))
            c1 = P(k, xa + 0.1, ye + sg * hh * 0.95); c2 = P(k, xb - 0.3, ye + sg * hh * 1.05)
            f.add(f'<path class="facet" d="M{a[0]:.2f},{a[1]:.2f} C{c1[0]:.2f},{c1[1]:.2f} {c2[0]:.2f},{c2[1]:.2f} '
                  f'{b[0]:.2f},{b[1]:.2f} Z"/>')
    # wyrostek poprzeczny (widoczny od strony końca) z cieniem
    tp = v['tp']
    sh = [(bx + 1.6, by + 1.9) for bx, by in tp]
    f.add(f'<path class="shade" d="{smooth(T(k, sh))}"/>')
    f.add(f'<path class="bone" d="{smooth(T(k, tp))}"/>')
    if v['tpf']:
        cls, cx, cy, rx, ry = v['tpf']
        x, y = P(k, cx, cy)
        f.add(f'<ellipse class="{cls}" cx="{x:.2f}" cy="{y:.2f}" rx="{rx * S:.2f}" ry="{ry * S:.2f}"/>')
    # nazwa i krótkie uwagi pod kręgiem (wyśrodkowane na zarysie)
    cxm = X[k] + (ext[k][0] + ext[k][1]) / 2 * S
    f.text(cxm, 50.6, NAME[k], cls='big', anchor='middle')
    for i, t in enumerate(NOTES[k]):
        f.text(cxm, 54.4 + i * 2.75, t, cls='notec', anchor='middle')

# ---------------- podpisy ----------------
f.label(P('typ', 21.4, 1.7), 'dołek żebrowy górny', 'fovea costalis superior', (38.6, 4.0), side='L')
f.label(P('typ', 22.4, 18.5), 'dołek żebrowy dolny', 'fovea costalis inferior', (30.0, 12.2), side='L')
f.label(P('typ', 37.0, 4.3), 'dołek żebrowy wyrostka poprzecznego', 'fovea costalis processus transversi', (52.0, 4.0), side='R')
f.label(P('Th10', 9.0, 11.0), 'trzon kręgu', 'corpus vertebrae', (67.6, 12.2), side='R')
f.label(P('Th11', 19.4, 11.5), 'dołek żebrowy', 'fovea costalis', (104.2, 4.0), side='R')
f.label(P('Th12', 43.2, 5.6), 'wyrostek poprzeczny', 'processus transversus', (142.0, 12.2), side='L')
f.save()
