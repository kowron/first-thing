# POŁĄCZENIA ŻEBRA Z KRĘGOSŁUPEM – widok od góry (przód ku górze; prawa strona ciała po prawej stronie rysunku).
# Kręg piersiowy (środkowy) z prawym żebrem: staw głowy żebra i staw żebrowo-poprzeczny z więzadłami.
# Po stronie lewej (bez żebra) widać dołki żebrowe, w które wchodzą głowa i guzek żebra.
# Schemat własny wg opisu Bochenka, t. I, s. 283–285 (nazwy z kart k_polaczenia.json).
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth, mirror

W, H = 150, 96
S = 1.12                 # mm rysunku / mm kości
CX, OY = 60.0, 14.0      # oś pośrodkowa; przedni brzeg trzonu
f = Fig('pol_zebro_kreg_gora', W, H, caption='kręg piersiowy z prawym żebrem · widok od góry (przód ku górze)')


def T(pts):
    return [(CX + x * S, OY + y * S) for x, y in pts]


def P(x, y):
    return (CX + x * S, OY + y * S)


def cr(pts, closed=True, n=12, t=0.5):
    """punkty na krzywej rysowanej przez smooth()"""
    m = len(pts)
    Q = (pts[-1:] + pts + pts[:2]) if closed else ([pts[0]] + pts + [pts[-1]])
    out = []
    for i in (range(1, m + 1) if closed else range(1, m)):
        p0, p1, p2, p3 = Q[i - 1], Q[i], Q[i + 1], Q[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) * t / 3, p1[1] + (p2[1] - p0[1]) * t / 3)
        c2 = (p2[0] - (p3[0] - p1[0]) * t / 3, p2[1] - (p3[1] - p1[1]) * t / 3)
        for k in range(n):
            u = k / n
            a, b, c, d = (1 - u) ** 3, 3 * u * (1 - u) ** 2, 3 * u * u * (1 - u), u ** 3
            out.append((a * p1[0] + b * c1[0] + c * c2[0] + d * p2[0], a * p1[1] + b * c1[1] + c * c2[1] + d * p2[1]))
    if not closed:
        out.append(pts[-1])
    return out


def offset(pl, d):
    """przesunięcie łamanej o d wzdłuż normalnej (d>0 – w prawo od kierunku marszu w układzie y w dół)"""
    out = []
    for i, p in enumerate(pl):
        a = pl[max(i - 1, 0)]; b = pl[min(i + 1, len(pl) - 1)]
        tx, ty = b[0] - a[0], b[1] - a[1]
        L = math.hypot(tx, ty) or 1
        out.append((p[0] - ty / L * d, p[1] + tx / L * d))
    return out


def poly(pts):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + ' Z'


def line(pts):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts)


# ---------------- łuk kręgu z wyrostkami (połowa prawa w mm kości, potem odbicie) ----------------
arch_R = [(0.0, 19.0), (7.5, 19.2), (11.0, 20.0), (12.5, 22.8), (17.0, 24.4), (21.5, 26.0), (25.0, 27.0), (27.6, 27.8),
          (29.6, 29.2), (30.4, 31.4), (29.8, 33.8), (27.6, 35.2), (23.5, 35.4), (19.5, 35.8), (15.8, 37.0), (12.0, 39.0),
          (8.0, 41.4), (4.6, 43.8), (2.8, 46.6), (2.2, 51.0), (2.1, 55.0), (2.6, 58.4), (1.7, 60.4), (0.0, 60.8)]
arch = arch_R + mirror(arch_R, 0)[1:-1]
f.add(f'<path class="bone" d="{smooth(T(arch))}"/>')
# otwór kręgowy
cx_, cy_ = P(0, 27.5)
f.add(f'<ellipse class="hole" cx="{cx_:.2f}" cy="{cy_:.2f}" rx="{7.3 * S:.2f}" ry="{7.0 * S:.2f}"/>')
# wyrostki stawowe górne (powierzchnie stawowe zwrócone ku tyłowi)
for s in (-1, 1):
    x, y = P(s * 9.2, 30.6)
    f.add(f'<ellipse class="bone2" cx="{x:.2f}" cy="{y:.2f}" rx="{3.2 * S:.2f}" ry="{2.4 * S:.2f}" transform="rotate({s * 12} {x:.2f} {y:.2f})"/>')
    f.add(f'<ellipse class="facet" cx="{x + s * 0.2:.2f}" cy="{y + 0.9:.2f}" rx="{2.6 * S:.2f}" ry="{1.05 * S:.2f}" transform="rotate({s * 12} {x:.2f} {y:.2f})"/>')
# grzebień wyrostka kolczystego
f.add(f'<path class="bonel" d="{line(T([(0, 45.5), (0, 58.6)]))}"/>')
# dołek żebrowy wyrostka poprzecznego – strona lewa (bez żebra)
x, y = P(-26.7, 28.0)
f.add(f'<ellipse class="facet" cx="{x:.2f}" cy="{y:.2f}" rx="{2.5 * S:.2f}" ry="{1.2 * S:.2f}" transform="rotate(-24 {x:.2f} {y:.2f})"/>')

# ---------------- trzon ----------------
body_R = [(0, 0), (5.2, 0.35), (9.6, 1.9), (12.7, 4.9), (14.1, 8.8), (14.2, 12.8), (13.5, 16.6), (11.9, 19.6), (8.6, 21.2), (4.2, 20.8)]
body = body_R + [(0, 20.1)] + mirror(body_R, 0)[:-1]
f.add(f'<path class="bone" d="{smooth(T(body))}"/>')
rim = [(x * 0.84, 1.6 + y * 0.84) for x, y in body]
f.add(f'<path class="bonel" d="{smooth(T(rim))}"/>')
# dołek żebrowy górny – strona lewa
x, y = P(-12.9, 18.0)
f.add(f'<ellipse class="facet" cx="{x:.2f}" cy="{y:.2f}" rx="{2.3 * S:.2f}" ry="{1.3 * S:.2f}" transform="rotate(62 {x:.2f} {y:.2f})"/>')

# ---------------- więzadło żebrowo-poprzeczne (między szyjką żebra a wyrostkiem poprzecznym) ----------------
lig_ct = [(25.2, 26.2), (22.6, 23.6), (19.8, 22.1), (17.2, 21.1), (15.4, 20.8), (13.6, 21.6), (12.9, 23.1), (17.0, 24.9),
          (21.5, 26.5), (24.9, 27.4)]
f.add(f'<path class="lig" d="{smooth(T(lig_ct))}"/>')
for a, b in [((16.8, 21.4), (14.6, 23.8)), ((19.4, 22.4), (17.6, 25.1)), ((21.9, 23.7), (20.6, 26.2)), ((23.9, 25.3), (23.2, 26.9))]:
    f.add(f'<path class="bonel" d="{line(T([a, b]))}"/>')

# ---------------- żebro prawe ----------------
rib = [(12.9, 15.6), (14.0, 14.1), (16.0, 13.7), (17.9, 14.6), (20.5, 16.4), (23.5, 18.2), (26.5, 19.7), (30.0, 20.9),
       (35.0, 22.2), (40.5, 23.3), (46.0, 24.0), (51.0, 24.4), (54.2, 24.5), (54.5, 30.6), (51.0, 30.8), (46.0, 30.7),
       (40.5, 30.4), (36.0, 30.2), (32.6, 30.0), (30.4, 29.2), (28.4, 28.0), (26.3, 27.0), (24.6, 25.8), (22.4, 23.8),
       (19.8, 22.4), (17.4, 21.4), (15.2, 20.9), (13.3, 19.8), (12.3, 17.8)]
f.add(f'<path class="bone" d="{smooth(T(rib))}"/>')
# powierzchnia przekroju na końcu bocznym
cut = [(53.2, 24.8), (54.3, 24.6), (54.6, 27.6), (54.5, 30.5), (53.4, 30.5), (53.1, 27.6)]
f.add(f'<path class="bone2" d="{smooth(T(cut))}"/>')
# brzeg górny / grzebień szyjki
f.add(f'<path class="bonel" d="{smooth(T([(18.4, 17.9), (22.8, 20.6), (27.6, 23.2), (33.5, 25.3), (42.0, 26.8), (52.0, 27.5)]), closed=False)}"/>')

# ---------------- powierzchnie stawowe w stawach (szpary stawowe widziane od góry) ----------------
body_curve = cr(body, closed=True, n=16)
seg = [p for p in body_curve if p[0] > 0 and 15.0 <= p[1] <= 19.4]
seg.sort(key=lambda p: p[1])
inner = offset(seg, 0.45)      # do środka trzonu (strona prawa, marsz w dół → normalna w prawo = do środka)
outer = offset(seg, -0.75)
f.add(f'<path class="facet" d="{poly(T(outer + inner[::-1]))}"/>')
arch_curve = cr(arch, closed=True, n=16)
seg2 = [p for p in arch_curve if p[0] > 0 and 24.6 <= p[0] <= 29.6 and p[1] < 29.8]
seg2.sort(key=lambda p: p[0])
inn2 = offset(seg2, 0.5)
out2 = offset(seg2, -0.55)
f.add(f'<path class="facet" d="{poly(T(out2 + inn2[::-1]))}"/>')

# ---------------- więzadło promieniste głowy żebra ----------------
rad = [(18.5, 15.3), (18.3, 12.0), (17.4, 8.6), (15.7, 5.3), (13.2, 2.6), (11.4, 3.2), (12.9, 6.0), (13.7, 9.0),
       (13.9, 12.0), (13.4, 14.4), (14.6, 15.6), (16.6, 16.0)]
f.add(f'<path class="lig" d="{smooth(T(rad))}"/>')
for q in [(12.7, 3.8), (14.4, 6.4), (15.8, 9.4), (16.8, 12.4)]:
    f.add(f'<path class="bonel" d="{line(T([(16.3, 15.2), q]))}"/>')

# ---------------- więzadło guzka żebra ----------------
lt = [(27.4, 34.8), (29.5, 34.0), (30.3, 32.2), (31.0, 30.0), (35.6, 30.1), (35.6, 31.9), (33.3, 33.9), (30.4, 35.5), (28.0, 35.9)]
f.add(f'<path class="lig" d="{smooth(T(lt))}"/>')
A0, A1 = (28.3, 35.6), (30.1, 32.6)       # przyczep na wierzchołku wyrostka poprzecznego
B0, B1 = (35.0, 31.6), (31.8, 30.3)       # przyczep na tylnej powierzchni guzka żebra
for u in (0.2, 0.5, 0.8):
    a = (A0[0] + (A1[0] - A0[0]) * u, A0[1] + (A1[1] - A0[1]) * u)
    b = (B0[0] + (B1[0] - B0[0]) * u, B0[1] + (B1[1] - B0[1]) * u)
    f.add(f'<path class="bonel" d="{line(T([a, b]))}"/>')

# ---------------- więzadło podłużne przednie (na przedniej powierzchni trzonu) ----------------
all_ = [(-9.6, 1.2), (-5.0, -0.9), (0, -1.5), (5.0, -0.9), (9.6, 1.2), (8.8, 2.2), (5.0, 0.9), (0, 0.6), (-5.0, 0.9), (-8.8, 2.2)]
f.add(f'<path class="lig" d="{smooth(T(all_))}"/>')

# ---------------- podpisy ----------------
TL = 34.0
f.label(P(-3.5, -0.6), 'więzadło podłużne przednie', 'ligamentum longitudinale anterius', (37.6, 5.0), side='L')
f.label(P(-6.0, 9.0), 'trzon kręgu', 'corpus vertebrae', (TL, 17.0), side='L')
f.label(P(-12.9, 18.0), 'dołek żebrowy górny', 'fovea costalis superior', (TL, 28.0), side='L')
f.label(P(-21.5, 31.6), 'wyrostek poprzeczny', 'processus transversus', (TL, 40.0), side='L')
f.label(P(-26.7, 28.0), 'dołek żebrowy wyrostka poprzecznego', 'fovea costalis processus transversi', (3.5, 82.0), side='R')

TR = 101.0
f.label(P(16.2, 9.6), 'więzadło promieniste głowy żebra', 'ligamentum capitis costae radiatum', (TR, 8.0), side='R')
f.label(P(16.0, 18.3), 'głowa żebra', 'caput costae', (TR, 18.5), side='R')
f.label(P(23.0, 20.9), 'szyjka żebra', 'collum costae', (TR, 28.5), side='R')
f.label(P(32.4, 32.4), 'więzadło guzka żebra', 'ligamentum tuberculi costae', (TR, 52.0), side='R')
f.label(P(28.6, 27.4), 'guzek żebra', 'tuberculum costae', (TR, 61.0), side='R')
f.label(P(18.4, 23.5), 'więzadło żebrowo-poprzeczne', 'ligamentum costotransversarium', (TR, 70.0), side='R')
f.label(P(1.0, 54.0), 'wyrostek kolczysty', 'processus spinosus', (TR, 80.0), side='R')
f.save()
