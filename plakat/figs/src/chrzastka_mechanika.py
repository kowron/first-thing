# MECHANIKA CHRZĄSTKI ŻEBROWEJ – model pierścieni żebrowych I i VII od przodu, w położeniu wydechu i wdechu
# (schemat własny; idea modelu jak ryc. 200/1–2 u Bochenka, t. I, s. 295–296).
# Podczas podnoszenia się kości żebrowej i bocznego przesunięcia jej końca mostkowego:
#   1) powiększa się kąt chrząstki (α) – na żebrach I–V między kością a chrząstką, na dalszych w obrębie samej chrząstki,
#   2) obrót w stawie mostkowo-żebrowym – powiększa się kąt między chrząstką żebrową a mostkiem (β),
#   3) chrząstka skręca się dokoła osi czołowej biegnącej wzdłuż niej; brzeg górny obraca się nieco do wewnątrz.
# Pierścień I łączy się z rękojeścią chrząstkozrostem (bez stawu), pierścień VII – stawem mostkowo-żebrowym.
# Tylne odcinki żeber (za płaszczyzną mostka) lekko przyciemnione.
import sys, math
sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth, mirror

W, H = 150, 106
f = Fig('chrzastka_mechanika', W, H,
        caption='model pierścieni żebrowych I i VII · widok od przodu (prawa strona ciała po lewej)')


# ---------------------------------------------------------------- narzędzia
def cr(pts, n=14, t=0.5):
    """punkty na otwartej krzywej Catmull-Rom (ta sama krzywa co smooth(closed=False))"""
    m = len(pts)
    Q = [pts[0]] + pts + [pts[-1]]
    out = []
    for i in range(1, m):
        p0, p1, p2, p3 = Q[i - 1], Q[i], Q[i + 1], Q[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) * t / 3, p1[1] + (p2[1] - p0[1]) * t / 3)
        c2 = (p2[0] - (p3[0] - p1[0]) * t / 3, p2[1] - (p3[1] - p1[1]) * t / 3)
        for k in range(n):
            u = k / n
            a, b, c, d = (1 - u) ** 3, 3 * u * (1 - u) ** 2, 3 * u * u * (1 - u), u ** 3
            out.append((a * p1[0] + b * c1[0] + c * c2[0] + d * p2[0], a * p1[1] + b * c1[1] + c * c2[1] + d * p2[1]))
    out.append(pts[-1])
    return out


def poly(pts, close=True):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + (' Z' if close else '')


def unit(v):
    L = math.hypot(*v) or 1.0
    return (v[0] / L, v[1] / L)


def add(a, b, k=1.0):
    return (a[0] + b[0] * k, a[1] + b[1] * k)


def band(c, w0, w1=None, cap0=False, cap1=False):
    """pasmo wzdłuż gęstej łamanej c, szerokość w0→w1 (zamknięty wielokąt)"""
    w1 = w0 if w1 is None else w1
    L = [0.0]
    for i in range(1, len(c)):
        L.append(L[-1] + math.dist(c[i - 1], c[i]))
    tot = L[-1] or 1
    A, B = [], []
    for i, p in enumerate(c):
        a = c[max(i - 1, 0)]; b = c[min(i + 1, len(c) - 1)]
        tx, ty = unit((b[0] - a[0], b[1] - a[1]))
        w = (w0 + (w1 - w0) * L[i] / tot) / 2
        A.append((p[0] - ty * w, p[1] + tx * w))
        B.append((p[0] + ty * w, p[1] - tx * w))

    def cap(i, w, sgn):
        a = c[max(i - 1, 0)]; b = c[min(i + 1, len(c) - 1)]
        tx, ty = unit((b[0] - a[0], b[1] - a[1]))
        nx, ny = -ty, tx
        out = []
        for k in range(1, 12):
            ph = math.pi * k / 12
            out.append((c[i][0] + w * (nx * math.cos(ph) + sgn * tx * math.sin(ph)),
                        c[i][1] + w * (ny * math.cos(ph) + sgn * ty * math.sin(ph))))
        return out
    out = list(A)
    if cap1:
        out += cap(len(c) - 1, w1 / 2, 1)
    out += B[::-1]
    if cap0:
        out += cap(0, w0 / 2, -1)[::-1]
    return out


def fillet(p0, b, p2, r, n=8):
    """łamana p0-b-p2 z zaokrągleniem narożnika b (promień r)"""
    d1 = unit((p0[0] - b[0], p0[1] - b[1]))
    d2 = unit((p2[0] - b[0], p2[1] - b[1]))
    cosang = max(-1, min(1, d1[0] * d2[0] + d1[1] * d2[1]))
    ang = math.acos(cosang)
    t = r / math.tan(ang / 2)
    a1, a2 = add(b, d1, t), add(b, d2, t)
    bis = unit((d1[0] + d2[0], d1[1] + d2[1]))
    cc = add(b, bis, r / math.sin(ang / 2))
    s0 = math.atan2(a1[1] - cc[1], a1[0] - cc[0])
    s1 = math.atan2(a2[1] - cc[1], a2[0] - cc[0])
    ds = s1 - s0
    while ds > math.pi: ds -= 2 * math.pi
    while ds < -math.pi: ds += 2 * math.pi
    return [(cc[0] + r * math.cos(s0 + ds * k / n), cc[1] + r * math.sin(s0 + ds * k / n)) for k in range(n + 1)]


def resample(pts, step=0.2):
    out = [pts[0]]
    for p in pts[1:]:
        q = out[-1]
        d = math.dist(p, q)
        if d < 1e-6:
            continue
        k = max(1, int(d / step))
        for j in range(1, k + 1):
            out.append((q[0] + (p[0] - q[0]) * j / k, q[1] + (p[1] - q[1]) * j / k))
    return out


def ang_deg(v):
    return math.degrees(math.atan2(v[1], v[0]))


def sector(v, d1, d2, r, n=20):
    """punkty łuku kąta między kierunkami d1 i d2 (krótszy łuk)"""
    a0, a1 = ang_deg(d1), ang_deg(d2)
    da = a1 - a0
    while da > 180: da -= 360
    while da < -180: da += 360
    return [(v[0] + r * math.cos(math.radians(a0 + da * k / n)), v[1] + r * math.sin(math.radians(a0 + da * k / n))) for k in range(n + 1)]


def angle_between(d1, d2):
    return math.degrees(math.acos(max(-1, min(1, d1[0] * d2[0] + d1[1] * d2[1]))))


# ---------------------------------------------------------------- model (współrzędne lokalne panelu: x – bocznie (+), y – w dół od górnego brzegu Th1)
SX = 0.93          # skala pozioma modelu
# kręgosłup: trzony Th1–Th12 (front)
VERT = [(k * 4.0, k * 4.0 + 3.1, 2.15 + 0.07 * k) for k in range(12)]

# mostek – połowa obrysu (x>0), położenie wydechu
STERN_HALF = [(0, 8.1), (1.2, 7.75), (2.3, 7.35), (3.5, 7.55), (4.15, 8.8), (4.35, 10.6), (4.1, 12.6), (3.4, 14.6),
              (2.85, 16.3), (2.75, 17.1), (2.85, 19.5), (3.0, 23.5), (3.1, 27.5), (2.9, 30.8), (2.45, 33.0),
              (2.2, 33.9), (1.65, 34.6), (1.35, 36.6), (0.95, 38.6), (0.4, 40.3)]
Y_MS, Y_XS = 16.9, 33.9          # chrząstkozrost górny / dolny

STATES = {
    # położenie wydechu
    'E': dict(
        dy=0.0,
        R1=[(2.0, 1.6), (5.4, 0.95), (8.5, 2.0), (10.4, 4.3), (10.8, 6.5), (10.3, 8.7), (9.4, 10.4), (8.7, 11.5)],
        S1=(3.7, 11.9),
        R7=[(2.3, 25.6), (7.0, 25.2), (11.5, 26.2), (15.3, 28.7), (17.8, 32.2), (18.8, 36.3), (18.4, 40.4),
            (16.8, 44.3), (14.6, 47.6), (12.7, 49.6)],
        S7=(1.7, 33.55), mid7=(0.35, 0.25),
    ),
    # położenie wdechu: żebra uniesione, końce mostkowe kości żebrowych przesunięte bocznie, mostek wyżej
    'I': dict(
        dy=-2.4,
        R1=[(2.0, 1.6), (5.5, 0.85), (8.9, 1.6), (10.9, 3.5), (11.3, 5.1), (10.9, 6.6), (9.9, 7.8), (8.45, 8.75)],
        S1=(3.7, 9.5),
        R7=[(2.3, 25.6), (7.2, 25.0), (12.0, 25.5), (16.3, 27.2), (19.3, 29.9), (20.8, 33.1), (20.8, 36.2),
            (19.8, 39.1), (18.0, 41.4), (15.9, 42.9)],
        S7=(1.7, 31.15), mid7=(0.45, 0.2),
    ),
}


def build(state):
    """zwraca słownik z liniami środkowymi (lokalne, x>0)"""
    s = STATES[state]
    out = {}
    # pierścień I: kość → kąt chrząstki na granicy kości i chrząstki → chrząstka do rękojeści (chrząstkozrost)
    r1 = cr([(x * SX, y) for x, y in s['R1']], n=16)
    out['r1'] = resample(r1, 0.15)
    J1 = out['r1'][-1]
    S1 = (s['S1'][0] * SX, s['S1'][1])
    out['c1'] = resample([J1, S1], 0.15)
    out['J1'] = J1
    out['t1'] = unit((J1[0] - out['r1'][-4][0], J1[1] - out['r1'][-4][1]))     # kierunek kości przy końcu
    out['S1'] = S1
    # pierścień VII: kość → krótki odcinek chrząstki w przedłużeniu kości → załamanie (kąt chrząstki) → mostek
    r7 = cr([(x * SX, y) for x, y in s['R7']], n=16)
    out['r7'] = resample(r7, 0.15)
    J7 = out['r7'][-1]
    t7 = unit((J7[0] - out['r7'][-4][0], J7[1] - out['r7'][-4][1]))
    B7 = add(J7, t7, 1.9)
    S7 = (s['S7'][0] * SX, s['S7'][1])
    d = (S7[0] - B7[0], S7[1] - B7[1])
    nrm = unit((d[1], -d[0]))
    M7 = add(((B7[0] + S7[0]) / 2, (B7[1] + S7[1]) / 2), nrm, s['mid7'][0])
    fil = fillet(J7, B7, M7, 0.9)
    tail = cr([fil[-1], M7, S7], n=20)
    out['c7'] = resample([J7] + fil + tail[1:], 0.15)
    out.update(J7=J7, B7=B7, S7=S7, t7=t7, M7=M7)
    out['lat7'] = max(range(len(out['r7'])), key=lambda i: out['r7'][i][0])
    out['lat1'] = max(range(len(out['r1'])), key=lambda i: out['r1'][i][0])
    out['dy'] = s['dy']
    return out


def draw_panel(CX, OY, state, marks=(-1, 1)):
    g = build(state)
    dy = g['dy']

    def T(p, side):
        return (CX + side * p[0], OY + p[1])

    def TL(pts, side):
        return [T(p, side) for p in pts]

    # --- kręgosłup (za mostkiem)
    for i, (y0, y1, hw) in enumerate(VERT):
        if i < len(VERT) - 1:
            yb = VERT[i + 1][0]
            f.add(f'<rect class="annulus" x="{CX - hw + 0.25:.2f}" y="{OY + y1 - 0.1:.2f}" width="{2 * hw - 0.5:.2f}" height="{yb - y1 + 0.2:.2f}"/>')
        f.add(f'<rect class="bone" x="{CX - hw:.2f}" y="{OY + y0:.2f}" width="{2 * hw:.2f}" height="{y1 - y0:.2f}" rx=".55"/>')
    # --- kości żebrowe (cały pierścień kostny jednym pasmem), tylne odcinki przyciemnione
    for side in (-1, 1):
        for key, w0, w1, lat in (('r1', 1.9, 1.75, 'lat1'), ('r7', 1.45, 1.4, 'lat7')):
            c = TL(g[key], side)
            f.add(f'<path class="bone" d="{poly(band(c, w0, w1, cap0=True))}"/>')
            k = g[lat]
            for frac in (1.0, 0.75, 0.5):
                kk = max(3, int(k * frac))
                f.add(f'<path class="shade" d="{poly(band(c[:kk], w0 - 0.1, w0 - 0.1, cap0=True))}"/>')
    # --- chrząstki żebrowe
    for side in (-1, 1):
        # VII
        c7 = TL(g['c7'], side)
        f.add(f'<path class="cart" d="{poly(band(c7, 1.3, 1.2))}"/>')
        # I – pod kątem do kości: klin wypełniający zewnętrzną stronę narożnika
        c1 = TL(g['c1'], side)
        J = T(g['J1'], side)
        tb = (side * g['t1'][0], g['t1'][1])
        tc = unit((c1[-1][0] - c1[0][0], c1[-1][1] - c1[0][1]))
        hb, hc = 1.75 / 2, 1.7 / 2
        nb, nc = (-tb[1], tb[0]), (-tc[1], tc[0])
        f.add(f'<path class="cart" d="{poly(band(c1, 1.7, 1.75))}"/>')
        f.add(f'<path class="cart" style="stroke:none" d="{poly([J, add(J, nb, hb * 1.02), add(J, nc, hc * 1.02)])}"/>')
        f.add(f'<path class="cart" style="stroke:none" d="{poly([J, add(J, nb, -hb * 1.02), add(J, nc, -hc * 1.02)])}"/>')
    # --- mostek
    half = [(x, y + dy) for x, y in STERN_HALF]
    outline = [(CX + x, OY + y) for x, y in half] + [(CX, OY + 40.75 + dy)] + [(CX - x, OY + y) for x, y in reversed(half[1:])]
    f.add(f'<path class="bone" d="{smooth(outline, closed=True, t=0.35)}"/>')
    # chrząstkozrosty mostkowe (cienkie pasma chrząstki)
    for yy, hw in ((Y_MS, 2.72), (Y_XS, 2.05)):
        f.add(f'<rect class="cart" x="{CX - hw:.2f}" y="{OY + yy + dy - 0.28:.2f}" width="{2 * hw:.2f}" height=".56"/>')
    # stawy mostkowo-żebrowe VII (szpara stawowa na brzegu mostka)
    for side in (-1, 1):
        S = T(g['S7'], side)
        tv = unit((g['M7'][0] - g['S7'][0], g['M7'][1] - g['S7'][1]))
        e = add(S, (side * tv[0], tv[1]), 0.55)
        rotd = ang_deg((side * tv[0], tv[1])) + 90
        f.add(f'<ellipse class="facet" cx="{e[0]:.2f}" cy="{e[1]:.2f}" rx=".95" ry=".38" transform="rotate({rotd:.1f} {e[0]:.2f} {e[1]:.2f})"/>')

    # --- kąty α (chrząstki) i β (chrząstka–mostek)
    res = {'g': g, 'T': T}
    for side in marks:
        # α pierścienia VII – w obrębie chrząstki
        V = T(g['B7'], side)
        d1 = (-side * g['t7'][0], -g['t7'][1])
        sv = (g['M7'][0] - g['B7'][0], g['M7'][1] - g['B7'][1])
        d2 = unit((side * sv[0], sv[1]))
        arc = sector(V, d1, d2, 3.1)
        f.add(f'<path class="shade" d="{poly([V] + arc)}"/>')
        f.add(f'<path class="dim" style="stroke-dasharray:none" d="{poly(arc, close=False)}"/>')
        bis = unit((d1[0] + d2[0], d1[1] + d2[1]))
        p = add(V, bis, 4.6)
        f.text(p[0], p[1] + 0.9, 'α', cls='pl', anchor='middle')
        res[('a7', side)] = arc[int(len(arc) * 0.22)]
        res[('a7v', side)] = V
        res['alpha7'] = angle_between(d1, d2)
        # β – między chrząstką VII a mostkiem (oś mostka ku dołowi)
        Sv = (CX + side * 2.25, OY + g['S7'][1])
        dc = unit((V[0] - Sv[0], V[1] - Sv[1]))
        dd = (0.0, 1.0)
        bdeg = angle_between(dd, dc)
        f.add(f'<path class="dim" d="M{Sv[0]:.2f},{Sv[1]:.2f} L{Sv[0]:.2f},{Sv[1] + (8.8 if bdeg < 32 else 6.4):.2f}"/>')
        arcb = sector(Sv, dd, dc, 3.6)
        f.add(f'<path class="shade" d="{poly([Sv] + arcb)}"/>')
        f.add(f'<path class="dim" style="stroke-dasharray:none" d="{poly(arcb, close=False)}"/>')
        bisb = unit((dd[0] + dc[0], dd[1] + dc[1]))
        ab = math.radians(ang_deg(dd) + (ang_deg(dc) - ang_deg(dd)) * (0.5 if bdeg < 32 else 0.4))
        pb = add(Sv, (math.cos(ab), math.sin(ab)), 7.6 if bdeg < 32 else 6.0)
        f.text(pb[0], pb[1] + 0.9, 'β', cls='pl', anchor='middle')
        res[('b', side)] = add(Sv, bisb, 3.6)
        res['beta'] = angle_between(dd, dc)
        # α pierścienia I – między kością a chrząstką
        V1 = T(g['J1'], side)
        e1 = (-side * g['t1'][0], -g['t1'][1])
        sc = (g['S1'][0] - g['J1'][0], g['S1'][1] - g['J1'][1])
        e2 = unit((side * sc[0], sc[1]))
        arc1 = sector(V1, e1, e2, 2.2)
        f.add(f'<path class="shade" d="{poly([V1] + arc1)}"/>')
        f.add(f'<path class="dim" style="stroke-dasharray:none" d="{poly(arc1, close=False)}"/>')
        bis1 = unit((e1[0] + e2[0], e1[1] + e2[1]))
        p1 = add(V1, bis1, 3.4)
        f.text(p1[0], p1[1] + 0.9, 'α', cls='pl', anchor='middle')
        res[('a1', side)] = arc1[int(len(arc1) * 0.25)]
        res['alpha1'] = angle_between(e1, e2)
    return res


# ================================================================ panele
OY = 12.0
CA, CB = 49.5, 90.8
A = draw_panel(CA, OY, 'E')
B = draw_panel(CB, OY, 'I')
print('wydech: α VII %.0f°, β %.0f°, α I %.0f°' % (A['alpha7'], A['beta'], A['alpha1']))
print('wdech:  α VII %.0f°, β %.0f°, α I %.0f°' % (B['alpha7'], B['beta'], B['alpha1']))

# numery pierścieni (wewnątrz pętli, po prawej stronie rysunku)
for P in (A, B):
    g = P['g']
    p7 = P['T'](g['r7'][g['lat7']], 1)
    f.text(p7[0] - 2.0, p7[1] + 0.8, 'VII', cls='note', anchor='end')
    p1 = P['T'](g['r1'][g['lat1']], 1)
    f.text(p1[0] + 1.7, p1[1] + 0.8, 'I', cls='note')

# strzałka (wdech): kość żebrowa unosi się, jej koniec mostkowy przesuwa się bocznie
gB = B['g']
JB = B['T'](gB['J7'], 1)
ar0, ar1 = (JB[0] + 1.0, JB[1] + 5.2), (JB[0] + 3.9, JB[1] + 1.3)
f.arrow(f'M{ar0[0]:.2f},{ar0[1]:.2f} L{ar1[0]:.2f},{ar1[1]:.2f}')

# tytuły paneli
f.text(CA, 5.3, 'położenie wydechu', cls='big', anchor='middle')
f.text(CA, 8.6, 'kąty α i β małe', cls='notec')
f.text(CB, 5.3, 'położenie wdechu', cls='big', anchor='middle')
f.text(CB, 8.6, 'kąty α i β powiększone', cls='notec')

# ================================================================ skręcenie chrząstki (powiększony fragment + przekrój)
P0, P1, P2 = (40.0, 93.4), (48.0, 91.2), (75.6, 82.0)
u = unit((P2[0] - P1[0], P2[1] - P1[1]))
nup = (u[1], -u[0])                    # normalna ku górze (u biegnie w prawo i ku górze)
Cm = add(P1, (P2[0] - P1[0], P2[1] - P1[1]), 0.56)
ea, eb = 4.1, 1.55


def ell(t):
    t = math.radians(t)
    return (Cm[0] + ea * math.cos(t) * nup[0] + eb * math.sin(t) * u[0], Cm[1] + ea * math.cos(t) * nup[1] + eb * math.sin(t) * u[1])


# tylna połowa pierścienia obrotu (za chrząstką)
f.add(f'<path class="arrow" style="marker-end:none" d="{poly([ell(-t) for t in range(0, 181, 6)], close=False)}"/>')
# kość żebrowa (kikut) + przekrój
seg_b = resample([P0, P1], 0.2)
f.add(f'<path class="bone" d="{poly(band(seg_b, 4.5, 4.4))}"/>')
f.add(f'<ellipse class="bone2" cx="{P0[0] + 0.15:.2f}" cy="{P0[1]:.2f}" rx=".75" ry="2.2" transform="rotate({ang_deg(u):.1f} {P0[0]:.2f} {P0[1]:.2f})"/>')
# chrząstka
seg_c = resample([P1, add(P2, u, 1.2)], 0.2)
f.add(f'<path class="cart" d="{poly(band(seg_c, 4.1, 3.9))}"/>')
# mostek (fragment)
f.add(f'<path class="bone" d="M75.3,73.6 L81.6,73.6 L81.9,96.4 L75.6,96.4 Z"/>')
f.add(f'<ellipse class="facet" cx="75.55" cy="82.0" rx=".55" ry="2.15"/>')
f.text(78.7, 99.6, 'mostek', cls='notec')
f.text(42.5, 99.6, 'kość żebrowa', cls='notec')
# oś czołowa wzdłuż chrząstki
a0, a1 = add(P1, u, -9.5), add(P2, u, 4.0)
f.add(f'<path class="axis" d="M{a0[0]:.2f},{a0[1]:.2f} L{a1[0]:.2f},{a1[1]:.2f}"/>')
# przednia połowa pierścienia obrotu: przód chrząstki idzie ku górze → brzeg górny ku tyłowi (do wewnątrz)
f.arrow(poly([ell(180 - t) for t in range(0, 171, 6)], close=False))

# przekrój chrząstki: wydech (pełny) i wdech (przerywany); przód w lewo
Q = (94.5, 82.6)
KS = 1.6
SEC = [(0.0, -3.25), (-1.0, -2.75), (-1.55, -1.3), (-1.62, 0.4), (-1.35, 2.0), (-0.7, 3.05), (0.15, 3.25), (0.85, 2.75),
       (1.15, 1.4), (1.0, -0.2), (1.05, -1.75), (0.8, -2.85)]


def secpts(tilt):
    a = math.radians(tilt)
    return [(Q[0] + KS * (x * math.cos(a) - y * math.sin(a)), Q[1] + KS * (x * math.sin(a) + y * math.cos(a))) for x, y in SEC]


TE, TI = 8.0, 38.0
f.add(f'<path class="cart" d="{smooth(secpts(TE), closed=True)}"/>')
f.add(f'<path class="capsule" d="{smooth(secpts(TI), closed=True)}"/>')
f.add(f'<circle class="axis" style="stroke-dasharray:none" cx="{Q[0]:.2f}" cy="{Q[1]:.2f}" r=".6"/>')
f.add(f'<circle class="dot" style="fill:#d23c3c" cx="{Q[0]:.2f}" cy="{Q[1]:.2f}" r=".22"/>')
topE, topI = secpts(TE)[0], secpts(TI)[0]
arcp = [(Q[0] + 7.9 * math.cos(math.radians(a)), Q[1] + 7.9 * math.sin(math.radians(a))) for a in range(-104, -65, 3)]
f.arrow(poly(arcp, close=False))
f.text(Q[0], 92.4, 'przekrój chrząstki', cls='notec')
f.text(Q[0] - 4.2, Q[1] + 0.8, 'przód', cls='note', anchor='end')
f.text(Q[0] + 4.3, Q[1] + 0.8, 'do wewnątrz', cls='note')
# legenda przekroju
LY = 96.8
f.add(f'<rect class="cart" x="{Q[0] - 8.6:.2f}" y="{LY - 1.5:.2f}" width="3.4" height="2.0" rx=".5"/>')
f.text(Q[0] - 4.6, LY + 0.25, 'wydech', cls='note')
f.add(f'<path class="capsule" d="M{Q[0] + 4.6:.2f},{LY - 0.5:.2f} L{Q[0] + 8.2:.2f},{LY - 0.5:.2f}"/>')
f.text(Q[0] + 9.0, LY + 0.25, 'wdech', cls='note')
f.text(58.0, 73.4, 'skręcenie chrząstki', cls='big', anchor='middle')

# ================================================================ podpisy
TL, TR = 30.0, 112.5
# panel A (wydech) – lewa kolumna
f.label(A[('a1', -1)], 'kąt chrząstki α', None, (TL, 15.5), side='L')
f.text(TL - 0.7, 19.6, 'żebra I–V: między kością', cls='note', anchor='end')
f.text(TL - 0.7, 22.3, 'a chrząstką', cls='note', anchor='end')
gA = A['g']
pr = A['T'](gA['r7'][int(len(gA['r7']) * 0.22)], -1)
f.label(pr, 'pierścień żebrowy', None, (TL, 29.0), side='L')
f.text(TL - 0.7, 33.1, 'para żeber + mostek', cls='note', anchor='end')
kb = A['T'](gA['r7'][int(len(gA['r7']) * 0.60)], -1)
f.label(kb, 'kość żebrowa', 'os costale', (TL, 46.0), side='L')
kc = A['T'](gA['c7'][int(len(gA['c7']) * 0.36)], -1)
f.label(kc, 'chrząstka żebrowa', 'cartilago costalis', (TL, 55.5), side='L')
f.label(A[('a7', -1)], 'kąt chrząstki α', None, (TL, 64.5), side='L')
f.text(TL - 0.7, 68.6, 'żebra dalsze: w obrębie', cls='note', anchor='end')
f.text(TL - 0.7, 71.3, 'samej chrząstki', cls='note', anchor='end')
# panel B (wdech) – prawa kolumna
f.label((CB + 1.6, OY + 22.0 + gB['dy']), 'mostek', 'sternum', (TR, 19.5), side='R')
sj = B['T'](gB['S7'], 1)
f.label((sj[0] + 0.85, sj[1] + 0.2), 'staw mostkowo-żebrowy', 'articulatio sternocostalis', (TR, 29.5), side='R')
f.label(B[('b', 1)], 'kąt β', None, (TR, 39.5), side='R')
f.text(TR + 0.7, 43.6, 'między chrząstką żebrową', cls='note')
f.text(TR + 0.7, 46.3, 'a mostkiem', cls='note')
am = ((ar0[0] + ar1[0]) / 2 + 0.3, (ar0[1] + ar1[1]) / 2 - 0.2)
f.label(am, 'kość żebrowa unosi się', None, (TR, 56.5), side='R')
f.text(TR + 0.7, 60.6, 'jej koniec mostkowy', cls='note')
f.text(TR + 0.7, 63.3, 'przesuwa się bocznie', cls='note')
# skręcenie – podpisy
f.label(add(P1, u, 3.2), 'oś czołowa wzdłuż chrząstki', None, (39.0, 80.5), side='L')
f.text(38.3, 84.6, 'podłużne skręcenie chrząstki', cls='note', anchor='end')
f.text(38.3, 87.3, 'przenosi się na kość żebrową', cls='note', anchor='end')
f.label(topE, 'brzeg górny chrząstki', None, (TR, 77.6), side='R')
f.text(TR + 0.7, 81.7, 'przy unoszeniu żebra', cls='note')
f.text(TR + 0.7, 84.4, 'obraca się nieco do wewnątrz', cls='note')

f.save()
