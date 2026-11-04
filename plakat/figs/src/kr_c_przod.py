# Kręg szyjny typowy (C3–C6) – widok od przodu. Nazwy i opis powierzchni trzonu wg Bochenka (s. 222–223).
import sys; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth, mirror

W, H = 150, 70
CX, OY, S = 75, 27.0, 1.4          # oś, górny brzeg trzonu (z przodu, pośrodku), skala
def T(pts): return [(CX + x * S, OY + y * S) for x, y in pts]
def P(x, y): return (CX + x * S, OY + y * S)
def M(pts): return mirror(pts, CX)

f = Fig('kr_c_przod', W, H, caption='kręg szyjny typowy (C3–C6) · widok od przodu')

for s in (-1, 1):
    def TS(pts): return T([(s * x, y) for x, y in pts])
    # słup stawowy w tle: wyrostek stawowy górny (u góry) i dolny (u dołu)
    col = TS([(13.4, -1.4), (14.4, -3.5), (16.8, -4.4), (19.0, -3.8), (19.9, -1.6), (19.8, 2.0), (19.6, 9.5), (19.8, 13.2),
              (18.9, 15.8), (16.6, 16.7), (14.3, 15.9), (13.3, 13.4), (13.0, 9.0), (13.0, 2.0)])
    f.add(f'<path class="bone2" d="{smooth(col)}"/>')
    x, y = P(s * 16.5, 14.9)
    f.add(f'<ellipse class="facet" cx="{x:.2f}" cy="{y:.2f}" rx="{2.5 * S:.2f}" ry="{1.25 * S:.2f}"/>')
    # listewka tylna z guzkiem tylnym (w tle, bocznie)
    pb = TS([(12.0, 1.9), (16.0, 2.0), (19.5, 2.4), (22.0, 2.9), (23.8, 2.7), (25.4, 3.6), (26.0, 5.4), (25.3, 7.2), (23.6, 7.9),
             (21.5, 8.2), (18.0, 8.7), (14.0, 8.9), (12.0, 8.8)])
    f.add(f'<path class="bone2" d="{smooth(pb)}"/>')
    # dno bruzdy nerwu rdzeniowego (widoczne między listewką przednią a tylną)
    sh = TS([(14.8, 3.1), (18.5, 2.9), (21.3, 3.3), (22.9, 4.2), (22.6, 5.3), (20.5, 5.0), (17.5, 4.5), (14.8, 4.2)])
    f.add(f'<path class="shade" d="{smooth(sh)}"/>')
    # listewka przednia z guzkiem przednim (odchodzi od trzonu)
    ab = TS([(8.8, 3.7), (12.0, 3.8), (15.0, 4.1), (17.4, 4.5), (19.2, 4.5), (21.0, 5.5), (21.8, 7.5), (21.2, 9.6), (19.4, 10.5),
             (17.6, 10.0), (15.6, 8.6), (12.5, 7.3), (8.8, 7.1)])
    f.add(f'<path class="bone" d="{smooth(ab)}"/>')
    # boczne, uniesione części powierzchni górnej trzonu (leżą z tyłu, nad brzegiem przednim)
    un = TS([(5.6, -0.4), (7.5, -2.3), (8.5, -3.75), (9.35, -4.0), (9.9, -3.2), (9.95, -0.6), (9.6, 0.8), (6.0, 0.8)])
    f.add(f'<path class="bone2" d="{smooth(un)}"/>')

# trzon (powierzchnia przednia); brzeg górny wklęsły, dolny słabo wypukły
B = T([(0, 0.0), (-4.5, -0.25), (-7.1, -0.85), (-8.7, -1.35), (-9.75, -0.7), (-9.95, 1.2), (-9.55, 4.0), (-9.3, 6.8), (-9.55, 9.7),
       (-9.9, 11.6), (-9.2, 12.7), (-6.5, 13.0), (-3.0, 13.35)])
f.add(f'<path class="bone" d="{smooth(B + [P(0, 13.5)] + M(B)[:-1])}"/>')
up = T([(0, 1.05), (-4.4, 0.8), (-7.0, 0.3), (-8.6, 0.15)])
lo = T([(-8.6, 11.6), (-6.4, 11.95), (-3.0, 12.25), (0, 12.4)])
f.add(f'<path class="bonel" d="{smooth(up + M(up)[1:], closed=False)}"/>')
f.add(f'<path class="bonel" d="{smooth(lo + M(lo)[1:], closed=False)}"/>')

# --- podpisy ---
f.label(P(-16.6, -3.3), 'wyrostek stawowy górny', 'processus articularis superior', (50.4, 9.5), side='L')
f.label(P(5.0, -0.25), 'powierzchnia górna trzonu', None, (85.0, 9.5), side='R')
f.text(85.7, 13.0, 'wklęsła w kierunku czołowym', cls='note')
f.label(P(-25.2, 4.2), 'guzek tylny', 'tuberculum posterius', (37, 25.5), side='L')
f.label(P(-20.6, 8.2), 'guzek przedni', 'tuberculum anterius', (37, 36.5), side='L')
f.label(P(21.8, 3.6), 'bruzda nerwu rdzeniowego', 'sulcus nervi spinalis', (113, 25.5), side='R')
f.label(P(13.0, 5.6), 'wyrostek poprzeczny', 'processus transversus', (113, 36.5), side='R')
f.label(P(-16.5, 15.4), 'wyrostek stawowy dolny', 'processus articularis inferior', (50.4, 57.5), side='L')
f.label(P(-3.0, 6.8), 'trzon kręgu', 'corpus vertebrae', (66.0, 57.5), side='R')
f.label(P(4.5, 13.25), 'powierzchnia dolna trzonu', None, (90.0, 57.5), side='R')
f.text(90.7, 61.0, 'słabo wypukła w kierunku czołowym', cls='note')
f.save()
