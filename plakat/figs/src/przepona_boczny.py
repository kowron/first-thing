# PRZEPONA – przekrój strzałkowy przez prawą połowę tułowia, na wysokości prawej kopuły przepony
# (schemat własny wg opisu Bochenka s. 690–695). Przód w lewo. Pasmo mięśniowe/ścięgniste – wydech,
# linia przerywana – głęboki wdech (kopuła prawa od górnego brzegu V chrząstki żebrowej do VII żebra, s. 695).
# Przyczep przedni – chrząstki żeber (część żebrowa), tylny – więzadło łukowate boczne nad m. czworobocznym
# lędźwi i XII żebro (część lędźwiowa / żebrowa, s. 691–692). Zachyłek żebrowo-przeponowy rozchyla się przy wdechu (s. 693).
import sys, math; sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth

W, H = 150, 100
K = 2.6                      # mm na cm
XA, YT = 47.0, 4.0           # x przedniej (wewnętrznej) powierzchni ściany przedniej (z=0); y górnego cięcia
YCUT = 29.6                  # dolne cięcie (cm)
f = Fig('przepona_boczny', W, H,
        caption='przepona · przekrój strzałkowy przez prawą kopułę (schemat) · przód w lewo')


def P(z, y):
    return (XA + K * z, YT + K * y)


# ---------- pomocnicze ----------
def cr(pts, closed=False, n=12, t=0.5):
    m = len(pts)
    PP = (pts[-1:] + pts + pts[:2]) if closed else ([pts[0]] + pts + [pts[-1]])
    out = []
    rng = range(1, m + 1) if closed else range(1, m)
    for i in rng:
        p0, p1, p2, p3 = PP[i - 1], PP[i], PP[i + 1], PP[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) * t / 3, p1[1] + (p2[1] - p0[1]) * t / 3)
        c2 = (p2[0] - (p3[0] - p1[0]) * t / 3, p2[1] - (p3[1] - p1[1]) * t / 3)
        for k in range(n):
            u = k / n
            a = (1 - u) ** 3; b = 3 * u * (1 - u) ** 2; c = 3 * u * u * (1 - u); d = u ** 3
            out.append((a * p1[0] + b * c1[0] + c * c2[0] + d * p2[0], a * p1[1] + b * c1[1] + c * c2[1] + d * p2[1]))
    if not closed:
        out.append(pts[-1])
    return out


def offset_var(pl, dfun):
    """przesunięcie łamanej wzdłuż normalnej o d = dfun(punkt) (d>0 – w dół przy marszu w prawo)."""
    out = []
    for i, p in enumerate(pl):
        a = pl[max(i - 1, 0)]; b = pl[min(i + 1, len(pl) - 1)]
        tx, ty = b[0] - a[0], b[1] - a[1]
        L = math.hypot(tx, ty) or 1
        d = dfun(p)
        out.append((p[0] - ty / L * d, p[1] + tx / L * d))
    return out


def poly(pts):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + ' Z'


def line(pts):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts)


def interp(prof, y):
    for (y0, v0), (y1, v1) in zip(prof, prof[1:]):
        if y0 <= y <= y1:
            return v0 + (v1 - v0) * (y - y0) / (y1 - y0)
    return prof[0][1] if y < prof[0][0] else prof[-1][1]


def y_at(pl, x, lo=None, hi=None):
    for (x0, y0), (x1, y1) in zip(pl, pl[1:]):
        if (x0 - x) * (x1 - x) <= 0 and x0 != x1:
            y = y0 + (y1 - y0) * (x - x0) / (x1 - x0)
            if (lo is None or y >= lo) and (hi is None or y <= hi):
                return y
    return None


def x_at(pl, y, lo=None, hi=None):
    for (x0, y0), (x1, y1) in zip(pl, pl[1:]):
        if (y0 - y) * (y1 - y) <= 0 and y0 != y1:
            x = x0 + (x1 - x0) * (y - y0) / (y1 - y0)
            if (lo is None or x >= lo) and (hi is None or x <= hi):
                return x
    return None


# ---------- ściany (profile z(y) w cm) ----------
A_IN = [(-2, 2.0), (4, 1.2), (8, 0.6), (12, 0.15), (15.6, 0.0), (21, 0.0), (26, 0.2), (32, 0.45)]
A_TH = [(-2, 1.75), (14.5, 1.75), (17.0, 1.45), (32, 1.45)]            # grubość ściany przedniej
P_IN = [(-2, 15.9), (4, 16.6), (10, 17.1), (16, 17.3), (18.7, 17.25), (19.5, 16.35), (24, 15.95), (32, 15.6)]
P_MID = [(-2, 17.7), (10, 18.75), (18, 18.95), (24, 18.35), (32, 18.0)]  # granica: żebra/m. czworoboczny – prostownik
P_OUT = [(-2, 21.4), (10, 22.4), (18, 22.6), (24, 22.3), (32, 21.9)]
ys = [-1.5 + 0.25 * k for k in range(int((YCUT + 2.5) / 0.25))]


def a_in(y): return interp(A_IN, y)
def a_out(y): return a_in(y) - interp(A_TH, y)
def p_in(y): return interp(P_IN, y)
def p_mid(y): return interp(P_MID, y)
def p_out(y): return interp(P_OUT, y)


# ---------- przepona (cm) ----------
EXP = [(0.15, 14.7), (0.55, 12.7), (1.3, 10.5), (2.5, 8.4), (4.1, 6.8), (6.0, 5.75), (7.9, 5.4), (9.8, 5.6),
       (11.8, 6.6), (13.6, 8.6), (15.0, 11.2), (15.95, 14.0), (16.45, 16.5), (16.6, 18.2), (16.35, 19.35)]
INS = [(0.15, 14.7), (1.3, 13.3), (2.9, 12.0), (4.9, 11.1), (7.0, 10.75), (9.3, 10.8), (11.6, 11.45),
       (13.6, 12.7), (14.95, 14.4), (15.7, 16.3), (16.15, 18.1), (16.35, 19.35)]
cE = [P(z, y) for z, y in cr(EXP, n=16)]
cI = [P(z, y) for z, y in cr(INS, n=16)]
TEN = (P(4.6, 0)[0], P(11.2, 0)[0])        # zasięg środka ścięgnistego (x, mm) – płatek prawy


def thick(p):
    x, y = p
    if TEN[0] < x < TEN[1]:
        return 1.25
    d = min(abs(x - TEN[0]), abs(x - TEN[1]))
    t = 1.25 + 0.65 * min(1.0, d / 3.0)
    return t


upE = offset_var(cE, lambda p: -thick(p) / 2)      # powierzchnia górna (piersiowa)
loE = offset_var(cE, lambda p: thick(p) / 2)       # powierzchnia dolna (brzuszna)
apex = min(upE, key=lambda p: p[1])
apexI = min(cI, key=lambda p: p[1])
print('szczyt kopuły (wydech)', [round(v, 2) for v in apex], ' wdech', [round(v, 2) for v in apexI])

# ---------- 1. ściana tylna: prostownik grzbietu, warstwa żeber, m. czworoboczny lędźwi ----------
erector = [P(p_mid(y), y) for y in ys] + [P(p_out(y), y) for y in ys][::-1]
f.add(f'<path class="muscle" d="{poly(erector)}"/>')
f.add(f'<path class="shade" d="{poly(erector)}"/>')
# włókna prostownika (pionowo)
for u in (0.3, 0.62):
    fib = [P(p_mid(y) + u * (p_out(y) - p_mid(y)), y) for y in ys]
    f.add(f'<path class="musclel" d="{line(fib)}"/>')
ys_th = [y for y in ys if y <= 18.9]
ribwall = [P(p_in(y), y) for y in ys_th] + [P(p_mid(y), y) for y in ys_th][::-1]
f.add(f'<path class="muscle" d="{poly(ribwall)}"/>')
ys_ql = [y for y in ys if y >= 18.6]
ql = [P(p_in(y), y) for y in ys_ql] + [P(p_mid(y), y) for y in ys_ql][::-1]
f.add(f'<path class="muscle" d="{poly(ql)}"/>')
for u in (0.33, 0.66):
    fib = [P(p_in(y) + u * (p_mid(y) - p_in(y)), y) for y in ys_ql if y >= 19.6]
    f.add(f'<path class="musclel" d="{line(fib)}"/>')
# żebra (tylne odcinki) w przekroju: V–XII
POST_RIBS = {'V': 0.6, 'VI': 3.2, 'VII': 5.8, 'VIII': 8.4, 'IX': 11.0, 'X': 13.6, 'XI': 16.1, 'XII': 18.2}
for nm, yc in POST_RIBS.items():
    zc = (p_in(yc) + p_mid(yc)) / 2
    c = P(zc, yc)
    rx, ry = (0.95, 1.75) if nm != 'XII' else (0.85, 1.35)
    f.add(f'<ellipse class="bone" cx="{c[0]:.2f}" cy="{c[1]:.2f}" rx="{rx}" ry="{ry}" transform="rotate(-28 {c[0]:.2f} {c[1]:.2f})"/>')

# ---------- 2. ściana przednia: mm. międzyżebrowe + chrząstki/żebra, niżej m. prosty brzucha ----------
front = [P(a_in(y), y) for y in ys] + [P(a_out(y), y) for y in ys][::-1]
f.add(f'<path class="muscle" d="{poly(front)}"/>')
f.add(f'<path class="shade" d="{poly(front)}"/>')
# pochewka / włókna m. prostego brzucha (od V chrząstki w dół – leży na chrząstkach V–VII)
for u in (0.28, 0.72):
    fib = [P(a_out(y) + u * (a_in(y) - a_out(y)), y) for y in ys if y >= 16.4]
    f.add(f'<path class="musclel" d="{line(fib)}"/>')
ANT_RIBS = {'III': 1.0, 'IV': 3.45, 'V': 5.9, 'VI': 8.3, 'VII': 10.7, 'VIII': 13.05, 'IX': 15.3}
ant_c = {}
for nm, yc in ANT_RIBS.items():
    zc = a_in(yc) - 0.62
    c = P(zc, yc)
    ant_c[nm] = c
    cls = 'bone' if nm in ('III', 'IV') else 'cart'
    rx, ry = (1.05, 1.5) if nm != 'IX' else (1.05, 1.25)
    f.add(f'<ellipse class="{cls}" cx="{c[0]:.2f}" cy="{c[1]:.2f}" rx="{rx}" ry="{ry}" transform="rotate(18 {c[0]:.2f} {c[1]:.2f})"/>')

# ---------- 3. płuco prawe ----------
GAP = 0.55
TIP_A, TIP_P = 10.3, 14.6          # dolne końce płuca w zachyłku (przedni, tylny) – cm
dia_up = offset_var(cE, lambda p: -thick(p) / 2 - GAP)
yA_mm, yP_mm = YT + K * TIP_A, YT + K * TIP_P
iA = next(i for i, p in enumerate(dia_up) if p[1] <= yA_mm)
iP = max(i for i, p in enumerate(dia_up) if p[1] <= yP_mm)
ant = [(P(a_in(y), y)[0] + GAP, P(0, y)[1]) for y in ys if y <= TIP_A - 1.6]
post = [(P(p_in(y), y)[0] - GAP, P(0, y)[1]) for y in ys if y <= TIP_P - 1.2][::-1]
tipA = ((ant[-1][0] + dia_up[iA][0]) / 2 - 0.15, yA_mm + 0.4)
tipP = ((post[0][0] + dia_up[iP][0]) / 2 + 0.1, yP_mm + 0.5)
lung = ant + [tipA] + dia_up[iA:iP + 1] + [tipP] + post
f.add(f'<path class="organ" d="{poly(lung)}"/>')

# ---------- 4. wątroba (płat prawy) ----------
liv_top = [p for p in loE if p[1] < YT + K * 16.6]
liv_top = [p for p in liv_top if p[0] > XA + K * 0.55]
liv_low = [P(15.2, 17.0), P(13.9, 17.5), P(12.6, 18.4), P(11.2, 19.6), P(8.8, 20.1), P(6.0, 19.4), P(3.2, 18.2),
           P(1.2, 17.2), P(0.5, 16.75)]
liver = liv_top + cr(liv_low, n=6)
f.add(f'<path class="organ" d="{poly(liver)}"/>')
f.add(f'<path class="shade" d="{poly(liver)}"/>')

# ---------- 5. nerka prawa (biegun górny przylega do przepony) ----------
kc = P(13.75, 23.6)
f.add(f'<ellipse class="organ" cx="{kc[0]:.2f}" cy="{kc[1]:.2f}" rx="{K * 1.85:.2f}" ry="{K * 5.2:.2f}" transform="rotate(-14 {kc[0]:.2f} {kc[1]:.2f})"/>')
f.add(f'<ellipse class="shade" cx="{kc[0]:.2f}" cy="{kc[1]:.2f}" rx="{K * 1.85:.2f}" ry="{K * 5.2:.2f}" transform="rotate(-14 {kc[0]:.2f} {kc[1]:.2f})"/>')

# ---------- 6. przepona (wydech): część mięśniowa – środek ścięgnisty – część mięśniowa ----------
iT0 = next(i for i, p in enumerate(cE) if p[0] >= TEN[0])
iT1 = next(i for i, p in enumerate(cE) if p[0] >= TEN[1])
for a, b, cls in ((0, iT0 + 1, 'muscle'), (iT1, len(cE), 'muscle'), (iT0, iT1 + 1, 'tendon')):
    seg = upE[a:b] + loE[a:b][::-1]
    f.add(f'<path class="{cls}" d="{poly(seg)}"/>')
for a, b in ((3, iT0 - 3), (iT1 + 3, len(cE) - 4)):
    f.add(f'<path class="musclel" d="{line(cE[a:b])}"/>')
# więzadło łukowate boczne (przekrój) – przyczep tylny, nad m. czworobocznym lędźwi
LIG = P(16.55, 19.55)
f.add(f'<ellipse class="lig" cx="{LIG[0]:.2f}" cy="{LIG[1]:.2f}" rx="1.25" ry=".75" transform="rotate(-20 {LIG[0]:.2f} {LIG[1]:.2f})"/>')

# ---------- 7. przepona – głęboki wdech (linia przerywana) ----------
f.add(f'<path class="capsule" d="{line(cI)}"/>')

# strzałki ruchu kopuły: wdech – w dół (niebieska), wydech – w górę (czerwona)
xa = apex[0] + 1.2
ya_lo = y_at(loE, xa - 1.25, apex[1] - 1, apex[1] + 4) + 0.8
yi = y_at(cI, xa - 1.25, apexI[1] - 1, apexI[1] + 3)
f.arrow(f'M{xa - 1.25:.2f},{ya_lo:.2f} L{xa - 1.25:.2f},{yi - 0.9:.2f}')
ya_lo2 = y_at(loE, xa + 1.25, apex[1] - 1, apex[1] + 4) + 0.8
yi2 = y_at(cI, xa + 1.25, apexI[1] - 1, apexI[1] + 3)
f.arrow(f'M{xa + 1.25:.2f},{yi2 - 0.7:.2f} L{xa + 1.25:.2f},{ya_lo2 + 0.2:.2f}', red=True)

# ---------- 8. poziomy kopuły (po stronie przedniej) ----------
XL = 41.4
y_exp = apex[1]
y_ins = apexI[1]
f.add(f'<path class="dim" d="M{XL:.2f},{y_exp:.2f} L{apex[0]:.2f},{y_exp:.2f}"/>')
f.add(f'<path class="dim" d="M{XL:.2f},{y_ins:.2f} L{apexI[0]:.2f},{y_ins:.2f}"/>')
f.text(XL - 0.6, y_exp - 0.55, 'kopuła prawa – wydech:', anchor='end')
f.text(XL - 0.6, y_exp + 2.05, 'górny brzeg V chrząstki żebrowej', anchor='end')
f.text(XL - 0.6, y_ins - 0.55, 'głęboki wdech: VII żebro', anchor='end')
f.text(XL - 0.6, y_ins + 2.05, '(do trzech żeber niżej)', anchor='end')
# numery żeber przy ścianie przedniej
for nm in ('V', 'VII'):
    c = ant_c[nm]
    f.text(c[0] - 2.2, c[1] + 0.75, nm, cls='note', anchor='end')

# jamy ciała
f.text(P(8.2, 1.6)[0], P(8.2, 1.6)[1], 'jama klatki piersiowej', cls='notec')
f.text(P(6.0, 24.5)[0], P(6.0, 24.5)[1], 'jama brzuszna', cls='notec')

# ---------- 9. podpisy ----------
# strona przednia (lewa)
f.label(P(4.0, 2.8), 'płuco prawe', 'pulmo dexter', (40.8, 10.0), side='L')
pc = min((p for p in cE if p[0] < TEN[0] - 4), key=lambda p: abs(p[1] - (YT + K * 9.3)))
f.label(pc, 'część żebrowa', 'pars costalis', (40.8, 41.0), side='L')
f.label(P(4.2, 15.6), 'wątroba', 'hepar', (40.8, 52.5), side='L')
cm = ant_c['IX']
f.label((cm[0] - 0.2, cm[1] + 0.4), 'łuk żebrowy', 'arcus costalis', (40.8, 62.0), side='L')
rp = P((a_in(25.0) + a_out(25.0)) / 2, 25.0)
f.label(rp, 'm. prosty brzucha', 'm. rectus abdominis', (40.8, 73.5), side='L')
# strona tylna (prawa)
pt = min((p for p in cE if TEN[0] + 3 < p[0] < TEN[1] - 2), key=lambda p: p[1])
f.label((pt[0] + 3.0, y_at(cE, pt[0] + 3.0, YT, YT + 30)), 'środek ścięgnisty', 'centrum tendineum', (109.4, 10.0), side='R')
pl_ = min((p for p in cE if p[0] > TEN[1] + 3), key=lambda p: abs(p[1] - (YT + K * 11.0)))
f.label(pl_, 'część lędźwiowa', 'pars lumbalis', (109.4, 24.0), side='R')
zr = P((p_in(16.6) + 16.75) / 2 + 0.05, 16.6)
f.label(zr, 'zachyłek żebrowo-przeponowy', 'recessus costodiaphragmaticus', (109.4, 38.0), side='R')
r12 = P((p_in(18.2) + p_mid(18.2)) / 2, 18.2)
f.label(r12, 'żebro XII', 'costa XII', (109.4, 49.0), side='R')
f.label((LIG[0] + 0.6, LIG[1] + 0.2), 'więzadło łukowate boczne', 'lig. arcuatum laterale', (109.4, 58.5), side='R')
f.label(P(13.3, 23.0), 'nerka prawa', 'ren dexter', (109.4, 68.0), side='R')
qp = P((p_in(26.0) + p_mid(26.0)) / 2, 26.0)
f.label(qp, 'm. czworoboczny lędźwi', 'm. quadratus lumborum', (109.4, 77.5), side='R')

# ---------- legenda ----------
LY = 92.6
lx = 22.0
f.add(f'<rect class="muscle" x="{lx:.2f}" y="{LY - 1.55:.2f}" width="5.2" height="1.9" rx=".4"/>')
f.text(lx + 6.4, LY + 0.3, 'położenie przy wydechu')
lx2 = lx + 34.0
f.add(f'<path class="capsule" d="M{lx2:.2f},{LY - 0.6:.2f} L{lx2 + 5.6:.2f},{LY - 0.6:.2f}"/>')
f.text(lx2 + 6.8, LY + 0.3, 'przy głębokim wdechu')
lx3 = lx2 + 32.5
f.arrow(f'M{lx3:.2f},{LY - 0.6:.2f} L{lx3 + 6.6:.2f},{LY - 0.6:.2f}')
f.text(lx3 + 8.0, LY + 0.3, 'wdech')
lx4 = lx3 + 18.5
f.arrow(f'M{lx4:.2f},{LY - 0.6:.2f} L{lx4 + 6.6:.2f},{LY - 0.6:.2f}', red=True)
f.text(lx4 + 8.0, LY + 0.3, 'wydech')

# przycięcie (górne i dolne cięcie przekroju)
body = ''.join(f.body[:-0] if False else f.body)
legend_start = next(i for i, s in enumerate(f.body) if 'rect class="muscle"' in s)
inside, legend = f.body[:legend_start], f.body[legend_start:]
f.body = [f'<defs><clipPath id="cp_przepona_boczny"><rect x="0" y="{YT:.2f}" width="{W}" height="{K * YCUT:.2f}"/>'
          f'</clipPath></defs><g clip-path="url(#cp_przepona_boczny)">{"".join(inside)}</g>'] + legend
f.save()
print('ok')
