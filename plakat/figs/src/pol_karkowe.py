# WIĘZADŁO KARKOWE – odcinek szyjny kręgosłupa z fragmentem kości potylicznej, widok od strony lewej (przód w lewo).
# Schemat własny wg opisu Bochenka, t. I, s. 254 (więzadło karkowe, więzadła międzykolcowe i nadkolcowe); nazwy z k_polaczenia.json.
# Pokazane: nieparzysta, trójkątna błona w płaszczyźnie pośrodkowej – u góry na grzebieniu potylicznym zewnętrznym, od przodu na guzku
# tylnym kręgu szczytowego i wierzchołkach wyrostków kolczystych C2–C7; brzeg tylny wolny; od C7 w dół – więzadło nadkolcowe;
# w obrębie szyi łączą się z nim więzadła międzykolcowe. Połączeń czaszki z kręgosłupem nie rysujemy (z kości potylicznej – tylko
# fragment łuski z grzebieniem potylicznym zewnętrznym).
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 140, 104
S = 0.47                       # mm rysunku / mm kości
X0, Y0 = 50.0, 32.0            # położenie guzka przedniego kręgu szczytowego na rysunku
f = Fig('pol_karkowe', W, H,
        caption='więzadło karkowe · kręgi szyjne i fragment kości potylicznej · widok od strony lewej (przód w lewo)')


def P(x, y):
    return (X0 + x * S, Y0 + y * S)


def T(pts):
    return [P(x, y) for x, y in pts]


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


class Frame:
    """lokalny układ kręgu: p – ku tyłowi, q – ku dołowi; O – punkt (0,0) w mm kości, th – kąt osi (stopnie, >0: oś biegnie w dół i do tyłu)"""
    def __init__(self, O, th):
        self.O, self.th = O, math.radians(th)

    def g(self, p, q):
        c, s = math.cos(self.th), math.sin(self.th)
        return (self.O[0] + p * c + q * s, self.O[1] - p * s + q * c)

    def G(self, pts):
        return [self.g(p, q) for p, q in pts]


# ============================================================ geometria (mm kości; x ku tyłowi, y ku dołowi)
# --- kręg szczytowy (C1): łuk przedni, część boczna z wyrostkiem poprzecznym (od końca), łuk tylny z guzkiem tylnym
ATLAS = [(-0.4, 0.0), (0.3, -4.2), (2.4, -5.8), (5.4, -5.4), (8.0, -6.9), (11.5, -8.1), (16.0, -7.0), (20.6, -7.6), (23.8, -6.6),
         (25.8, -4.4), (28.2, -3.4), (31.0, -3.9), (35.5, -4.5), (40.2, -5.1), (43.8, -4.6), (46.2, -2.2), (46.6, 1.2), (45.2, 4.4),
         (41.8, 5.4), (37.2, 4.4), (32.4, 3.7), (28.4, 4.0), (25.6, 5.9), (22.8, 8.0), (17.8, 8.5), (12.2, 7.8), (8.6, 6.2),
         (5.2, 5.6), (2.2, 5.8), (0.3, 4.2)]
ATLAS_TP = [(12.4, -2.6), (14.6, -5.0), (17.8, -5.4), (20.2, -3.0), (20.8, 0.8), (19.0, 4.0), (15.6, 4.8), (13.0, 2.8)]
TUB_POST = (46.5, 0.2)                       # guzek tylny kręgu szczytowego

# --- kręg obrotowy (C2): zarys jak w rysunku kr_c2_bok (u – ku tyłowi, v – w dół od wierzchołka zęba)
C2_O = [(8.0, 0.0), (5.2, 0.8), (3.6, 2.8), (3.0, 5.5), (2.9, 8.5), (3.3, 11.2), (4.0, 13.0), (3.6, 14.3), (2.2, 15.0), (0.8, 15.6),
        (0.0, 16.8), (-0.2, 19.5), (0.2, 24.0), (0.3, 28.5), (-0.1, 33.0), (-0.6, 36.5), (0.0, 38.6), (1.4, 39.2), (5.0, 38.4),
        (9.0, 37.2), (12.4, 36.1), (14.3, 35.1), (15.1, 33.3), (15.5, 31.0), (16.5, 29.3), (18.2, 28.7), (19.8, 29.2), (20.9, 30.8),
        (21.4, 33.0), (21.7, 35.2), (22.3, 37.2), (23.3, 38.8), (24.6, 39.6), (26.0, 39.0), (26.8, 37.0), (27.2, 34.6), (28.0, 32.7),
        (29.8, 31.6), (32.5, 31.1), (35.5, 31.4), (39.0, 32.2), (42.0, 32.2), (44.8, 31.0), (46.2, 28.8), (46.0, 26.0), (44.6, 24.1),
        (41.5, 23.2), (37.5, 22.4), (33.0, 21.8), (28.5, 21.0), (25.0, 20.4), (22.4, 19.4), (20.6, 18.0), (19.2, 16.4), (17.4, 15.2),
        (15.0, 14.4), (13.2, 13.9), (12.6, 12.6), (12.8, 10.0), (13.0, 7.0), (12.6, 4.0), (11.4, 1.6), (9.8, 0.3)]
C2_TP = [(12.6, 20.9), (16.8, 20.7), (19.8, 22.1), (20.2, 24.8), (18.6, 27.0), (15.8, 27.6), (13.4, 25.8), (12.4, 23.0)]
C2_TIP = (46.2, 27.4)
# ząb przylega powierzchnią przednią (u≈3.5, v≈7.3) do łuku przedniego C1; kręg lekko pochylony (lordoza)
TH2 = -5.0
_c, _s = math.cos(math.radians(TH2)), math.sin(math.radians(TH2))
_ax, _ay = 3.5 * _c + 7.3 * _s, -3.5 * _s + 7.3 * _c
F2 = Frame((6.3 - _ax, -0.3 - _ay), TH2)

# --- kręgi C3–C7 i Th1–Th2: (nazwa, wysokość trzonu h, głębokość D, kąt osi th, długość wyrostka kolczystego, jego nachylenie γ)
SPEC = [('C3', 14.0, 15.5, -9.0, 15.0, 20), ('C4', 14.0, 16.0, -3.0, 15.0, 21), ('C5', 14.0, 16.5, 3.0, 16.5, 22),
        ('C6', 14.0, 17.0, 9.0, 22.0, 24), ('C7', 15.0, 17.0, 14.0, 33.0, 27), ('Th1', 16.0, 18.0, 18.0, 34.0, 36),
        ('Th2', 17.0, 18.5, 20.0, 34.0, 42)]
DISC = 5.0


def body_pts(h, D):
    return [(0.5, 0.0), (D * 0.5, -0.2), (D - 0.8, 0.0), (D + 0.1, 0.9), (D + 0.3, h * 0.5), (D + 0.1, h - 0.8), (D - 0.8, h),
            (D * 0.5, h + 0.15), (1.4, h + 0.55), (-0.2, h + 0.1), (-0.5, h - 1.6), (0.2, h * 0.5), (-0.3, 1.4)]


def post_pts(h, D, Ls, alpha, kind='C'):
    """nasada, filar stawowy (wyrostek stawowy górny i dolny; powierzchnie stawowe skośne, ok. 45°) i wyrostek kolczysty"""
    a = math.radians(alpha)
    u = (math.cos(a), math.sin(a))
    n = (-math.sin(a), math.cos(a))                         # normalna – ku dołowi od osi wyrostka
    rU, rL = (D + 12.6, 4.4), (D + 12.0, 13.2)              # nasada wyrostka kolczystego: brzeg górny i dolny
    base = (D + 12.6, 4.4)
    wt = 3.6 if kind == 'C' else 4.0                        # grubość wyrostka przy końcu
    tU = (base[0] + Ls * u[0], base[1] + Ls * u[1])
    tL = (tU[0] + wt * n[0] + 0.6 * u[0], tU[1] + wt * n[1] + 0.6 * u[1])
    # koniec: guzkowaty (C3–C6 – rozdwojony, z boku widać zgrubienie), C7 i Th – zaokrąglony guzek
    knob = 0.9 if kind == 'C' else 0.6
    tip = [(tU[0] - 0.6 * n[0], tU[1] - 0.6 * n[1] * knob),
           (tU[0] + 1.5 * u[0] + 0.4 * n[0], tU[1] + 1.5 * u[1] + 0.4 * n[1]),
           (tU[0] + 2.1 * u[0] + 0.5 * wt * n[0], tU[1] + 2.1 * u[1] + 0.5 * wt * n[1]),
           (tL[0] + 1.3 * u[0], tL[1] + 1.3 * u[1]),
           (tL[0] - 0.6 * u[0] + 0.5 * n[0] * knob, tL[1] - 0.6 * u[1] + 0.5 * n[1] * knob)]
    mU = (base[0] + 0.45 * Ls * u[0] - 0.3 * n[0], base[1] + 0.45 * Ls * u[1] - 0.3 * n[1])
    mL = (rL[0] + 0.5 * (tL[0] - rL[0]) + 0.5 * n[0], rL[1] + 0.5 * (tL[1] - rL[1]) + 0.5 * n[1])
    hd = h + DISC
    pts = [(D - 0.6, 2.6), (D + 2.4, 2.4), (D + 3.8, 1.2),            # nasada (brzeg górny)
           (D + 4.2, -1.6), (D + 4.9, -3.2), (D + 6.0, -3.4),          # wierzchołek wyrostka stawowego górnego
           (D + 9.4, -0.2), (D + 12.3, 2.6),                           # powierzchnia stawowa górna (ku górze i do tyłu)
           mU, tip[0]] + tip[1:] + [mL, rL,
           (D + 12.7, hd - 1.0), (D + 12.6, hd + 1.4), (D + 11.6, hd + 1.9),    # koniec wyrostka stawowego dolnego
           (D + 8.6, hd - 1.0), (D + 5.4, hd - 4.2),                   # powierzchnia stawowa dolna (ku dołowi i do przodu)
           (D + 4.3, hd - 6.4), (D + 3.6, h - 3.4), (D + 2.0, h - 4.6), (D - 0.6, h - 4.4)]    # wcięcie kręgowe dolne
    return pts, tU


def facets(D, h):
    """paski chrząstki stawowej na powierzchni górnej i dolnej filaru"""
    hd = h + DISC
    up = [(D + 4.9, -3.0), (D + 6.0, -3.0), (D + 9.4, 0.2), (D + 12.1, 2.8), (D + 11.6, 3.3), (D + 9.0, 0.9), (D + 5.8, -2.0)]
    lo = [(D + 5.6, hd - 4.5), (D + 8.6, hd - 1.4), (D + 11.5, hd + 1.5), (D + 11.0, hd + 1.9), (D + 8.2, hd - 0.7), (D + 5.4, hd - 3.6)]
    return up, lo


# rozmieszczenie kręgów (marsz w dół wzdłuż osi)
c2_low_front = F2.g(1.4, 39.2)
V = []
prev = None
for name, h, D, th, Ls, gam in SPEC:
    if prev is None:
        lf, thp = c2_low_front, TH2
    else:
        Fp, hp, thp = prev
        lf = Fp.g(0.0, hp)
    dn = (math.sin(math.radians((thp + th) / 2)), math.cos(math.radians((thp + th) / 2)))
    O = (lf[0] + DISC * dn[0], lf[1] + DISC * dn[1])
    Fr = Frame(O, th)
    kind = 'C' if name in ('C3', 'C4', 'C5', 'C6') else 'T'
    pp, tip = post_pts(h, D, Ls, gam + th, kind)
    V.append(dict(name=name, h=h, D=D, th=th, F=Fr, post=Fr.G(pp), tip=Fr.g(*tip), body=Fr.G(body_pts(h, D)),
                  fac=[Fr.G(x) for x in facets(D, h)]))
    prev = (Fr, h, th)
vs = {v['name']: v for v in V}

TIP = {'C1': TUB_POST, 'C2': F2.g(*C2_TIP)}
for v in V:
    TIP[v['name']] = v['tip']

# --- kość potyliczna: fragment łuski; profil pośrodkowy (dolny tylny brzeg) = grzebień potyliczny zewnętrzny
INION = (73.0, -40.0)          # guzowatość potyliczna zewnętrzna – wierzchołek trójkąta więzadła
OPIST = (36.6, -13.4)          # tylny brzeg otworu wielkiego
CREST = [(73.0, -39.6), (67.4, -34.6), (59.6, -28.6), (51.6, -22.6), (44.4, -17.6), (39.4, -14.6), OPIST]
OCC = [(66.4, -62.4), (70.6, -57.0), (73.6, -50.6), (74.8, -44.6), (74.4, -41.6)] + CREST[1:] + [(35.0, -15.2)]
OCC_CUT = [(35.0, -15.2), (66.4, -62.4), (67.6, -61.0), (36.9, -14.6)]       # powierzchnia przecięcia (linia cięcia)

# ============================================================ rysowanie
YCUT_TOP, YCUT_BOT = -66.0, 128.0
cx0, cy0 = P(-30, YCUT_TOP)
cx1, cy1 = P(140, YCUT_BOT)
f.add(f'<defs><clipPath id="cp_karkowe"><rect x="{cx0:.2f}" y="{cy0:.2f}" width="{cx1 - cx0:.2f}" height="{cy1 - cy0:.2f}"/></clipPath></defs>')
f.add('<g clip-path="url(#cp_karkowe)">')

# 0. kanał kręgowy w głębi (widoczny przez otwory międzykręgowe)
canal = []
for v in [None] + V:
    if v is None:
        canal += [F2.g(12.4, 12.0), F2.g(14.6, 36.4)]
    else:
        canal += [v['F'].g(v['D'] - 0.2, 0.0), v['F'].g(v['D'] - 0.2, v['h'])]
back = []
for v in [None] + V:
    if v is None:
        back += [F2.g(20.0, 12.0), F2.g(21.0, 36.4)]
    else:
        back += [v['F'].g(v['D'] + 4.6, 0.0), v['F'].g(v['D'] + 4.6, v['h'])]
f.add(f'<path class="shade" d="{poly(T(canal + back[::-1]))}"/>')

# 1. więzadło karkowe (płaszczyzna pośrodkowa, za wyrostkami kolczystymi)
front = cr(CREST, n=8)
front += [(TIP['C1'][0] - 0.2, TIP['C1'][1] - 1.6)]
for k in ('C2', 'C3', 'C4', 'C5', 'C6', 'C7'):
    x, y = TIP[k]
    front.append((x + 0.4, y + 0.6))
c7 = TIP['C7']
free = cr([(c7[0] + 2.6, c7[1] - 2.4), (65.4, 80.0), (67.0, 40.0), (69.4, 0.0), (71.6, -26.0), INION], n=10)
nuchae = front + free[:-1]
f.add(f'<path class="lig" d="{poly(T(nuchae))}"/>')
# włókna – pasma biegnące od grzebienia ku wierzchołkom wyrostków kolczystych
for a, b, c in [((68.0, -33.6), (65.6, 20.0), (c7[0] + 1.6, c7[1] - 10.0)),
                ((60.0, -28.0), (58.0, 16.0), (TIP['C6'][0] + 4.0, TIP['C6'][1] - 2.0)),
                ((51.6, -21.8), (51.0, 8.0), (TIP['C4'][0] + 5.0, TIP['C4'][1] + 2.0))]:
    f.add(f'<path class="bonel" d="{smooth(T([a, b, c]), closed=False)}"/>')

# więzadło nadkolcowe: wąskie pasmo łączące wierzchołki wyrostków kolczystych od C7 w dół
sup = [TIP['C7'], TIP['Th1'], TIP['Th2'], (TIP['Th2'][0] + 6.0, TIP['Th2'][1] + 20.0)]
a_side = [(x - 0.1, y + 1.0) for x, y in sup]
b_side = [(x + 3.0, y - 0.6) for x, y in sup]
b_side[0] = (c7[0] + 2.6, c7[1] - 2.4)
f.add(f'<path class="lig" d="{poly(T(cr(a_side, n=8) + cr(b_side, n=8)[::-1]))}"/>')


# 2. więzadła międzykolcowe (między sąsiednimi wyrostkami kolczystymi; w szyi łączą się z więzadłem karkowym)
def isp(upper, lower):
    Fu, Fl = upper['F'], lower['F']
    return [Fu.g(upper['D'] + 11.0, 14.0), (upper['tip'][0] + 0.2, upper['tip'][1] + 2.4),
            (lower['tip'][0] + 0.2, lower['tip'][1] + 0.2), Fl.g(lower['D'] + 12.0, 2.6)]


pairs = [('C3', 'C4'), ('C4', 'C5'), ('C5', 'C6'), ('C6', 'C7'), ('C7', 'Th1'), ('Th1', 'Th2')]
f.add(f'<path class="lig" d="{poly(T([F2.g(29.0, 31.6), (TIP["C2"][0] - 1.0, TIP["C2"][1] + 3.2), (TIP["C3"][0] + 0.2, TIP["C3"][1] + 0.2), vs["C3"]["F"].g(vs["C3"]["D"] + 12.0, 2.6)]))}"/>')
for u_, l_ in pairs:
    f.add(f'<path class="lig" d="{poly(T(isp(vs[u_], vs[l_])))}"/>')
f.add(f'<path class="lig" d="{poly(T([(30.0, 3.6), (44.6, 4.6), (TIP["C2"][0] - 1.0, TIP["C2"][1] - 3.6), F2.g(30.0, 21.4)]))}"/>')

# 3. kręgi: łuki (filary stawowe, wyrostki kolczyste), krążki, trzony
f.add(f'<path class="bone" d="{smooth(T(F2.G(C2_O)))}"/>')
for v in V:
    f.add(f'<path class="bone" d="{smooth(T(v["post"]))}"/>')
    for fc in v['fac']:
        f.add(f'<path class="facet" d="{smooth(T(fc))}"/>')


def disc_poly(Fu, hu, Du, Fl, Dl, front_off=1.0):
    a, b = Fu.g(front_off, hu + 0.3), Fu.g(Du - 0.6, hu)
    c, d = Fl.g(Dl - 0.6, 0.0), Fl.g(0.6, 0.0)
    mf = ((a[0] + d[0]) / 2 - 1.0, (a[1] + d[1]) / 2)
    mb = ((b[0] + c[0]) / 2 + 0.6, (b[1] + c[1]) / 2)
    return [a, b, mb, c, d, mf]


f.add(f'<path class="annulus" d="{smooth(T(disc_poly(F2, 38.4, 13.0, vs["C3"]["F"], vs["C3"]["D"], 1.6)))}"/>')
for u_, l_ in pairs:
    U, L_ = vs[u_], vs[l_]
    f.add(f'<path class="annulus" d="{smooth(T(disc_poly(U["F"], U["h"], U["D"], L_["F"], L_["D"])))}"/>')
for v in V:
    f.add(f'<path class="bone" d="{smooth(T(v["body"]))}"/>')
f.add(f'<path class="bone" d="{smooth(T(F2.G(C2_TP)))}"/>')
# kręg szczytowy (na zębie C2)
f.add(f'<path class="bone" d="{smooth(T(ATLAS))}"/>')
f.add(f'<path class="bone" d="{smooth(T(ATLAS_TP))}"/>')

# 4. kość potyliczna – fragment łuski; z przodu linia cięcia (powierzchnia przecięcia ciemniejsza)
f.add(f'<path class="bone" d="{smooth(T(OCC))}"/>')
f.add(f'<path class="bone2" d="{poly(T(OCC_CUT))}"/>')
f.add(f'<path class="shade" d="{smooth(T([(38.6, -14.6), (44.4, -17.6), (51.6, -22.6), (59.6, -28.6), (67.4, -34.6), (72.6, -39.4), (69.0, -39.6), (60.0, -33.6), (51.0, -27.4), (43.6, -21.8), (39.0, -17.2)]))}"/>')
# kresa karkowa górna (od guzowatości potylicznej zewnętrznej ku przodowi i bocznie)
f.add(f'<path class="bonel" d="{smooth(T([(73.8, -43.2), (67.0, -45.6), (58.0, -45.0), (49.0, -41.4)]), closed=False)}"/>')
f.add('</g>')

# oznaczenia kręgów
f.text(*P(35.0, 2.6), 'C1', cls='notec')
x, y = F2.g(7.0, 30.6); f.text(*P(x, y), 'C2', cls='notec')
for v in V:
    x, y = v['F'].g(v['D'] * 0.5, v['h'] * 0.5 + 1.6)
    if y < YCUT_BOT - 4:
        f.text(*P(x, y), v['name'], cls='notec')

# ============================================================ podpisy
TL, TR = 40.0, 92.0
f.label(P(62.0, -48.0), 'kość potyliczna', 'os occipitale', (TR, 5.0), side='R')
f.label(P(62.4, -30.6), 'grzebień potyliczny zewnętrzny', 'crista occipitalis externa', (TR, 14.0), side='R')
f.label(P(71.0, 4.0), 'więzadło karkowe', 'ligamentum nuchae', (TR, 31.0), side='R')
f.label(P(45.4, 0.4), 'guzek tylny', 'tuberculum posterius', (TR, 40.5), side='R')
xx, yy = TIP['C4']
f.label(P(xx - 5.0, yy + 1.6), 'wyrostek kolczysty', 'processus spinosus', (TR, 52.0), side='R')
a = isp(vs['C5'], vs['C6'])
f.label(P((a[0][0] + a[2][0]) / 2 + 3.0, (a[0][1] + a[2][1]) / 2 + 0.6), 'więzadło międzykolcowe', 'ligamentum interspinale', (TR, 62.0), side='R')
xx, yy = TIP['C7'][0] * 0.45 + TIP['Th1'][0] * 0.55, TIP['C7'][1] * 0.45 + TIP['Th1'][1] * 0.55
f.label(P(xx + 1.6, yy - 0.6), 'więzadło nadkolcowe', 'ligamentum supraspinale', (TR, 84.0), side='R')

f.label(P(1.2, -2.6), 'kręg szczytowy', 'atlas', (TL, 25.0), side='L')
x, y = F2.g(4.0, 26.0)
f.label(P(x, y), 'kręg obrotowy', 'axis', (TL, 39.0), side='L')
x, y = vs['C7']['F'].g(4.5, 10.5)
f.label(P(x, y), 'kręg wystający', 'vertebra prominens', (TL, 82.0), side='L')
f.save()
