# STAWY MIĘDZYKRĘGOWE – dwa kręgi lędźwiowe (L3, L4) widziane od strony lewej (przód w lewo) + przekrój poziomy lewego stawu L3/L4.
# Schemat własny wg opisu Bochenka, t. I, s. 252 (stawy międzykręgowe, więzadła żółte) i s. 232 (ustawienie wyrostków stawowych
# kręgów lędźwiowych: powierzchnie prawie w płaszczyźnie strzałkowej; górne wklęsłe, zwrócone do tyłu i przyśrodkowo, dolne wypukłe,
# zwrócone do przodu i bocznie; górne obejmują dolne). Zarys kręgu lędźwiowego – jak w rysunku kr_l_bok. Nazwy z k_polaczenia.json.
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 150, 106
f = Fig('pol_staw_miedzykregowy', W, H,
        caption='stawy międzykręgowe · L3–L4 od strony lewej (przód w lewo) · przekrój poziomy lewego stawu L3/L4 (widok od góry)')


def poly(pts, closed=True):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + (' Z' if closed else '')


def cr(pts, closed=False, n=10, t=0.5):
    """punkty na krzywej rysowanej przez smooth() (Catmull-Rom)"""
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
    """przesunięcie łamanej o d wzdłuż normalnej (d>0 – w prawo od kierunku marszu, układ y w dół)"""
    out = []
    for i, p in enumerate(pl):
        a = pl[max(i - 1, 0)]; b = pl[min(i + 1, len(pl) - 1)]
        tx, ty = b[0] - a[0], b[1] - a[1]
        L = math.hypot(tx, ty) or 1
        out.append((p[0] - ty / L * d, p[1] + tx / L * d))
    return out


# ======================================================================= A. widok z boku L3–L4
SA = 0.70
XA, YA = 35.6, 14.0           # rysunek: x kości = 0 (przednia powierzchnia trzonu L3), y kości = 0 (górna powierzchnia trzonu L3)


def PA(x, y):
    return (XA + x * SA, YA + y * SA)


def TA(pts):
    return [PA(x, y) for x, y in pts]


# zarys kręgu lędźwiowego (jak kr_l_bok): x od przedniej powierzchni trzonu, y od górnej powierzchni trzonu
LV = [(0.9, 0.1), (8.0, -0.25), (17.0, -0.35), (26.0, -0.25), (32.6, 0.0), (34.0, 0.9), (34.4, 2.1),
      (36.2, 3.1), (38.4, 3.4), (40.2, 2.4),
      (41.0, -1.4), (41.8, -5.6), (42.8, -9.4), (44.6, -11.8), (47.0, -12.6), (49.2, -11.8), (50.4, -9.4), (50.9, -7.2),
      (52.9, -6.4), (54.9, -4.4), (55.2, -1.6), (54.0, 0.6),
      (53.6, 2.6), (56.0, 4.6), (62.0, 4.2), (70.0, 3.4), (78.0, 2.8), (83.6, 2.6),
      (86.6, 4.2), (87.7, 8.0), (87.8, 12.8), (87.2, 17.6), (85.4, 21.4), (82.2, 22.6),
      (76.6, 21.4), (70.4, 19.6), (64.8, 19.0), (61.0, 20.0),
      (59.0, 23.4), (58.2, 28.4), (57.4, 33.0), (56.0, 36.0), (53.8, 37.4), (51.4, 36.8),
      (49.6, 34.4), (48.6, 30.6), (48.0, 26.6), (47.2, 22.8),
      (45.8, 19.8), (43.4, 17.9), (40.4, 17.3), (37.6, 18.2), (35.6, 20.4),
      (34.5, 22.8), (34.3, 25.6), (33.6, 26.9), (26.0, 27.35), (17.0, 27.5), (8.0, 27.35), (1.1, 27.0),
      (0.1, 26.0), (0.7, 20.0), (1.35, 13.5), (0.7, 7.0), (0.05, 1.1)]
COSTAL = [(41.4, 4.6), (44.0, 2.4), (47.4, 2.2), (50.0, 4.0), (51.0, 7.4), (50.4, 11.0), (48.0, 13.6), (44.6, 14.0),
          (42.0, 12.2), (40.8, 8.6)]
ACC = [(49.4, 12.4), (52.2, 12.6), (54.0, 14.2), (53.6, 16.4), (51.2, 16.9), (49.4, 15.4)]
DSC = 11.0                    # wysokość krążka lędźwiowego (s. 250: 4–12 mm, w części lędźwiowej najwyższe)
VH = 27.5


class Fr:
    def __init__(self, ox, oy, deg):
        self.ox, self.oy, self.a = ox, oy, math.radians(deg)

    def g(self, x, y):
        c, s = math.cos(self.a), math.sin(self.a)
        return (self.ox + x * c - y * s, self.oy + x * s + y * c)

    def G(self, pts):
        return [self.g(x, y) for x, y in pts]


F3 = Fr(0.0, 0.0, 0.0)
F4 = Fr(-0.6, VH + DSC, -2.0)          # L4 lekko pochylony – krążek nieco wyższy z przodu (lordoza)
F2 = Fr(0.8, -(VH + DSC), 2.0)         # L2 (tylko dolna część, przycięta)
F5 = Fr(-1.6, 2 * (VH + DSC), -4.0)    # L5 (tylko górna część, przycięta)

YT, YB = -15.5, 2 * (VH + DSC) - 6.0   # linie cięcia u góry i u dołu (y kości)
ax0, ay0 = PA(-8, YT)
ax1, ay1 = PA(96, YB)
f.add(f'<defs><clipPath id="cp_smk_a"><rect x="{ax0:.2f}" y="{ay0:.2f}" width="{ax1 - ax0:.2f}" height="{ay1 - ay0:.2f}"/></clipPath></defs>')
f.add('<g clip-path="url(#cp_smk_a)">')


def disc(Fu, Fl):
    a, b = Fu.g(1.0, VH - 0.2), Fu.g(33.6, 26.9)
    c, d = Fl.g(34.0, 0.9), Fl.g(0.9, 0.1)
    mf = ((a[0] + d[0]) / 2 - 1.6, (a[1] + d[1]) / 2)
    mb = ((b[0] + c[0]) / 2 + 1.0, (b[1] + c[1]) / 2)
    return [a, b, mb, c, d, mf]


# otwory międzykręgowe (w głąb – cień), między wcięciem kręgowym dolnym wyższego a górnym niższego kręgu
for Fu, Fl in ((F2, F3), (F3, F4), (F4, F5)):
    fo = Fu.G([(34.0, 16.0), (37.6, 16.2), (43.4, 17.0), (46.6, 20.6), (47.4, 26.0)]) + Fl.G([(41.0, -2.0), (40.0, 2.8), (36.2, 3.6), (34.0, 2.0)])
    f.add(f'<path class="shade" d="{smooth(TA(fo))}"/>')

# kręgi: od dołu ku górze (wyrostek stawowy górny niższego kręgu leży bocznie – przykrywa wyrostek stawowy dolny wyższego)
for Fu, Fl in ((F2, F3), (F3, F4), (F4, F5)):
    f.add(f'<path class="annulus" d="{smooth(TA(disc(Fu, Fl)))}"/>')
# kolejność: L2, L3, L4, L5 – każdy następny przykrywa wyrostek dolny poprzedniego
for Fv in (F2, F3, F4, F5):
    f.add(f'<path class="bone" d="{smooth(TA(Fv.G(LV)))}"/>')
    # listewki brzeżne
    f.add(f'<path class="bonel" d="{smooth(TA(Fv.G([(1.2, 1.7), (12.0, 1.45), (24.0, 1.45), (32.9, 1.7)])), closed=False)}"/>')
    f.add(f'<path class="bonel" d="{smooth(TA(Fv.G([(1.3, 25.5), (12.0, 25.75), (24.0, 25.75), (33.0, 25.4)])), closed=False)}"/>')
    f.add(f'<path class="bonel" d="{smooth(TA(Fv.G([(84.0, 4.4), (84.8, 8.8), (84.9, 13.4), (84.3, 17.8), (82.9, 21.0)])), closed=False)}"/>')
    f.add(f'<path class="bone" d="{smooth(TA(Fv.G(COSTAL)))}"/>')
    f.add(f'<path class="bone" d="{smooth(TA(Fv.G(ACC)))}"/>')
f.add('</g>')

# torebka stawu L3/L4 (przyczepiona do brzegów powierzchni stawowych) – zarys przerywany
caps = F3.G([(48.6, 22.2), (52.6, 21.0), (57.6, 22.2), (60.4, 26.0), (60.6, 31.6), (59.0, 37.0), (56.2, 40.6), (52.4, 41.6),
             (49.6, 39.4), (48.4, 34.4), (47.8, 28.4)])
f.add(f'<path class="capsule" d="{smooth(TA(caps))}"/>')
f.text(*PA(15.0, 15.4), 'L3', cls='notec')
f.text(*PA(15.0, VH + DSC + 15.4), 'L4', cls='notec')

# ======================================================================= B. przekrój poziomy lewego stawu L3/L4 (od góry, przód ku górze)
SB = 1.5
U0, U1, V0, V1 = -27.0, 7.0, -13.0, 16.0          # okno wstawki (mm kości)
XB, YB0 = 96.4 - U0 * SB, 58.0 - V0 * SB          # x = 0 – płaszczyzna pośrodkowa, y = 0 – środek stawu


def PB(x, y):
    return (XB + x * SB, YB0 + y * SB)


def TB(pts):
    return [PB(x, y) for x, y in pts]


def mx(pts):
    return [(-x, y) for x, y in pts]


bx0, by0 = PB(U0, V0)
bx1, by1 = PB(U1, V1)
f.add(f'<defs><clipPath id="cp_smk_b"><rect x="{bx0:.2f}" y="{by0:.2f}" width="{bx1 - bx0:.2f}" height="{by1 - by0:.2f}" rx="2.2"/></clipPath></defs>')
f.add('<g clip-path="url(#cp_smk_b)">')

# powierzchnia stawowa wyrostka stawowego dolnego L3: wypukła, zwrócona do przodu i bocznie (prawie w płaszczyźnie strzałkowej)
iap_face = cr([(-10.9, -7.3), (-13.4, -5.4), (-14.9, -2.2), (-15.4, 1.6), (-15.0, 5.4), (-13.8, 8.6)], n=10)
GAP = 1.2
sap_face = offset(iap_face, GAP)       # powierzchnia wyrostka stawowego górnego L4: wklęsła, zwrócona do tyłu i przyśrodkowo
# przednia (kanałowa) powierzchnia blaszki L3 i jej tylna powierzchnia; wyrostek kolczysty w płaszczyźnie pośrodkowej
lam_front = [(-10.6, -6.9), (-10.0, -3.4), (-8.8, 0.4), (-6.6, 3.4), (-3.6, 5.8), (-1.0, 7.2), (0.0, 7.6)]
lam_back = [(-13.8, 8.6), (-12.2, 10.8), (-9.4, 12.2), (-6.0, 13.6), (-3.4, 15.4), (-2.3, 18.0), (-2.2, 24.0)]
iap = iap_face + cr(lam_back, n=6)[1:] + mx(cr(lam_back, n=6))[::-1] + mx(cr(lam_front, n=6)) + cr(lam_front, n=6)[::-1][1:]
# kanał kręgowy (w głębi) – przed więzadłami żółtymi
canal = [(-9.6, -16.0), (9.6, -16.0)] + mx(cr(lam_front, n=6)) + cr(lam_front, n=6)[::-1][1:] + [(-11.4, -8.6)]
f.add(f'<path class="shade" d="{poly(TB(canal))}"/>')
f.add(f'<path class="bone2" d="{poly(TB(iap))}"/>')
# wyrostek kolczysty – grzebień (linia pośrodkowa)
f.add(f'<path class="bonel" d="{poly(TB([(0.0, 12.0), (0.0, 17.0)]), closed=False)}"/>')

# wyrostek stawowy górny L4 (przekrój): obejmuje wyrostek dolny od przodu i bocznie; z tyłu wyrostek suteczkowaty
sap_out = cr([(-14.9, 9.8), (-17.2, 11.4), (-20.6, 12.0), (-23.4, 10.8), (-24.8, 8.0), (-24.2, 4.8), (-23.0, 2.6),
              (-22.8, -1.0), (-21.6, -5.2), (-19.2, -8.6), (-15.8, -10.6), (-12.4, -10.6), (-10.0, -9.2)], n=8)
f.add(f'<path class="cavity" d="{poly(TB(iap_face + sap_face[::-1]))}"/>')
f.add(f'<path class="bone2" d="{poly(TB(sap_face + sap_out))}"/>')
# chrząstka stawowa na obu powierzchniach; między nimi szczelinowata jama stawowa
c_i = offset(iap_face, 0.40)
c_s = offset(iap_face, GAP - 0.40)
f.add(f'<path class="facet" d="{poly(TB(iap_face + c_i[::-1]))}"/>')
f.add(f'<path class="facet" d="{poly(TB(sap_face + c_s[::-1]))}"/>')

# więzadła żółte: na przedniej powierzchni blaszek (od strony kanału), bocznie dochodzą do torebki stawowej
flv_in = cr(lam_front, n=6)
flv_out = offset(flv_in, 2.2)
flv_out[0] = (flv_out[0][0] + 0.4, flv_out[0][1] - 0.8)
f.add(f'<path class="lig" d="{poly(TB(flv_in + flv_out[::-1]))}"/>')
f.add(f'<path class="lig" d="{poly(TB(mx(flv_in) + mx(flv_out)[::-1]))}"/>')

# torebka stawowa: cienka, przyczepiona do brzegów powierzchni stawowych – z przodu (pod więzadłem żółtym) i z tyłu
fa, fb = iap_face[0], sap_face[0]
f.add(f'<path class="capsule" d="{smooth(TB([(fa[0] + 0.2, fa[1] + 0.4), (fa[0] - 0.2, fa[1] - 1.5), (fb[0] - 0.4, fb[1] - 2.0), (fb[0] - 1.6, fb[1] - 0.4)]), closed=False)}"/>')
la, lb = iap_face[-1], sap_face[-1]
f.add(f'<path class="capsule" d="{smooth(TB([(la[0] + 0.9, la[1] + 0.9), (la[0] + 0.3, la[1] + 2.6), (lb[0] - 1.0, lb[1] + 2.8), (lb[0] - 1.8, lb[1] + 1.0)]), closed=False)}"/>')
f.add('</g>')
f.add(f'<rect x="{bx0:.2f}" y="{by0:.2f}" width="{bx1 - bx0:.2f}" height="{by1 - by0:.2f}" rx="2.2" class="dim"/>')
f.text(*PB(-7.4, 11.2), 'L3', cls='notec')
f.text(*PB(-19.4, 2.2), 'L4', cls='notec')
f.text(*PB(2.0, -6.0), 'kanał', cls='notec')
f.text((bx0 + bx1) / 2, by0 - 1.4, 'przekrój poziomy (przód ku górze)', cls='notec')

# ======================================================================= podpisy
TL, TR = 33.0, 100.0
# A – lewa kolumna (struktury przednie)
f.label(PA(12.0, 8.0), 'trzon kręgu', 'corpus vertebrae', (TL, 13.0), side='L')
f.label(PA(37.6, 22.0), 'otwór międzykręgowy', 'foramen intervertebrale', (TL, 24.0), side='L')
f.label(PA(6.0, 33.0), 'krążek międzykręgowy', 'discus intervertebralis', (TL, 35.0), side='L')
# A – prawa kolumna (łuk i wyrostki)
f.label(PA(76.0, 12.0), 'wyrostek kolczysty', 'processus spinosus', (TR, 7.0), side='R')
f.label(PA(46.4, 31.0), 'wyrostek stawowy górny', 'processus articularis superior', (TR, 16.5), side='R')
f.label(PA(59.4, 27.0), 'torebka stawowa', 'capsula articularis', (TR, 26.0), side='R')
f.label(PA(57.6, 33.6), 'wyrostek stawowy dolny', 'processus articularis inferior', (TR, 35.5), side='R')
x, y = F4.g(66.0, 12.0)
f.label(PA(x, y), 'łuk kręgu', 'arcus vertebrae', (TR, 45.0), side='R')
# B – podpisy po lewej stronie wstawki
TB_L = bx0 - 3.0
f.label(PB(-15.6, -1.2), 'jama stawowa', 'cavitas articularis', (TB_L, 76.0), side='L')
f.label(PB(-13.4, 11.4), 'torebka stawowa', 'capsula articularis', (TB_L, 94.0), side='L')
f.label(PB(-11.0, -2.6), 'więzadło żółte', 'ligamentum flavum', (TB_L, 67.0), side='L')
f.save()
