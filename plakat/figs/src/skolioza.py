# SKOLIOZY – krzywizny kręgosłupa w płaszczyźnie czołowej; kręgosłup widziany od tyłu (prawa strona ciała po prawej
# stronie rysunku). Schemat własny, krzywizny powiększone dla czytelności.
# Treść wyłącznie wg Bochenka (t. I, s. 266–268):
#  – skrzywienia boczne (skolioses) występują zwykle (68%); u noworodka i paroletnich dzieci brak krzywizn czołowych,
#    rozwijają się później (przeważnie 7–10 r.ż.);
#  – najczęściej (52%) skrzywienie boczne części piersiowej wypukłością na prawo, przeważnie na wysokości trzeciego –
#    szóstego kręgu piersiowego; lewostronna piersiowa tylko 16%;
#  – często łączy się ze skrzywieniem bocznym części lędźwiowej wypukłym w lewo (kompensacyjne, względy statyczne,
#    np. dłuższa kończyna dolna lewa); skolioza piersiowa może się też łączyć z kompensacyjną skoliozą drugostronną szyi
#    (względy ortooptyczne);
#  – s. 268: najsłabszym miejscem jest jakoby piąty kręg piersiowy – tu najczęściej boczne skrzywienia.
import sys, math, os
sys.path.insert(0, '/home/user/first-thing/plakat/figs')
from figlib import Fig, smooth, mirror

W, H = 146, 124
f = Fig('skolioza', W, H, caption='skrzywienia boczne kręgosłupa (skolioses) · płaszczyzna czołowa · widok od tyłu · krzywizny powiększone')


def poly(pts, close=True):
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + (' Z' if close else '')


# ---------------------------------------------------------------- kręgi (wymiary w mm kości)
# name, reg, h (wysokość trzonu), disc (krążek pod spodem), wb (szerokość trzonu), wt (rozpiętość wyrostków poprzecznych)
V = []


def add(name, reg, h, disc, wb, wt):
    V.append(dict(name=name, reg=reg, h=h, disc=disc, wb=wb, wt=wt))


add('C1', 'C1', 10, 4, 0, 76)
add('C2', 'C2', 24, 5, 20, 56)
for i, (wb, wt) in enumerate([(19, 48), (20, 49), (21, 50), (23, 52)]):
    add(f'C{i + 3}', 'C', 14, 5, wb, wt)
add('C7', 'C7', 15, 5, 25, 70)
TH = [(16, 4, 27, 76), (17, 4, 28, 72), (17.5, 4, 28, 68), (18, 4, 29, 66), (18.5, 5, 30, 64), (19, 5, 31, 63),
      (19.5, 5, 32, 62), (20, 5.5, 33, 61), (21, 5.5, 35, 58), (22, 6, 37, 54), (23, 6, 39, 48), (24, 8, 41, 42)]
for i, (h, d, wb, wt) in enumerate(TH):
    add(f'Th{i + 1}', 'T', h, d, wb, wt)
for i, (h, d, wb, wt) in enumerate([(26, 10, 43, 64), (27, 11, 45, 76), (27, 11, 47, 88), (27, 12, 49, 86), (27, 12, 51, 82)]):
    add(f'L{i + 1}', 'L', h, d, wb, wt)


def layout(S, Y0):
    """położenie kręgów (środki trzonów) w mm rysunku wzdłuż osi; zwraca poziom podstawy kości krzyżowej"""
    y = Y0
    for v in V:
        v['y0'] = y
        v['yc'] = y + v['h'] * S / 2
        y += (v['h'] + v['disc']) * S
    return y


# ---------------------------------------------------------------- przebieg krzywizn: przesunięcie boczne osi (mm rysunku)
# Zadana krzywizna osi x''(y) = suma trzech dzwonów (szyjna – wypukła w lewo, piersiowa – w prawo, lędźwiowa – w lewo);
# warunki: kość krzyżowa pionowa i w linii pośrodkowej, a kręg szczytowy znów nad nią (x = 0, x' = 0) – krzywizny
# wyrównują się wzajemnie (kompensacyjne). Między krzywiznami odcinki prawie proste, skośne.
APEX_T = 4.4                       # odchylenie wierzchołka krzywizny piersiowej (mm rysunku)


def solve(M, b):
    n = len(b)
    A = [row[:] + [b[i]] for i, row in enumerate(M)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(A[r][c]))
        A[c], A[p] = A[p], A[c]
        for r in range(n):
            if r != c:
                k = A[r][c] / A[c][c]
                A[r] = [x - k * y for x, y in zip(A[r], A[c])]
    return [A[i][n] / A[i][i] for i in range(n)]


def make_offset(byname, S):
    def lvl(n, fr=0.5):
        v = byname[n]
        return v['y0'] + fr * v['h'] * S
    yt = lvl('C1', 0.0) - 0.7
    yb = byname['L5']['y0'] + (byname['L5']['h'] + byname['L5']['disc']) * S
    # dzwony krzywizny: (środek, sigma) – połączenie szczytowo-obrotowe, szyjna, piersiowa, lędźwiowa, lędźwiowo-krzyżowa
    C = {'CC': (lvl('C2', 0.0), 1.6), 'C': (lvl('C4', 1.0), 2.6),
         'T': ((lvl('Th4', 0.5) + lvl('Th5', 0.5)) / 2, 3.3),          # wierzchołek Th4/Th5 – zgięcie głównie Th3–Th6
         'L': (lvl('L3', 0.0), 5.0), 'LS': (lvl('L5', 0.5), 1.3)}
    N = 1600
    ys = [yt + (yb - yt) * k / N for k in range(N + 1)]
    dy = ys[1] - ys[0]

    def g(y, c, s_):
        return math.exp(-0.5 * ((y - c) / s_) ** 2) / (s_ * math.sqrt(2 * math.pi))

    def prof(a):                                  # całkowanie od dołu (x = 0, x' = 0 u podstawy kości krzyżowej)
        X = [0.0] * (N + 1); D = [0.0] * (N + 1)
        for k in range(N - 1, -1, -1):
            kap = sum(a[n] * g(ys[k], *C[n]) for n in a)
            D[k] = D[k + 1] - kap * dy
            X[k] = X[k + 1] - D[k] * dy
        return X, D

    def at(X, y):
        return X[min(N, max(0, int(round((y - yt) / dy))))]
    P = {'top': yt, 'C': C['C'][0] - 1.0, 'T': C['T'][0], 'L': C['L'][0]}

    def feats(a):
        X, D = prof(a)
        r = {k: at(X, y) for k, y in P.items()}
        r['sl'] = D[0]
        return r, X
    # warunki: szczyt nad kością krzyżową i pionowo; lędźwiowa i szyjna – mniejsze, drugostronne (kompensacyjne)
    fs = [lambda r: r['top'], lambda r: r['sl'], lambda r: r['L'] + 0.64 * r['T'], lambda r: r['C'] + 0.30 * r['T']]
    base = {n: 0.0 for n in C}; base['T'] = -1.0
    r0, _ = feats(base)
    cols = []
    for n in ('CC', 'C', 'L', 'LS'):
        a = dict(base); a[n] = 1.0
        cols.append(feats(a)[0])
    sol = solve([[f_(c) - f_(r0) for c in cols] for f_ in fs], [-f_(r0) for f_ in fs])
    a = dict(base); a.update(zip(('CC', 'C', 'L', 'LS'), sol))
    r, X = feats(a)
    sc = APEX_T / r['T']
    X = [x * sc for x in X]

    def off(y):
        if y >= yb:
            return 0.0
        if y <= ys[0]:
            return X[0]
        k = min(N - 1, int((y - ys[0]) / dy)); t = (y - ys[k]) / dy
        return X[k] + (X[k + 1] - X[k]) * t
    return off


# ---------------------------------------------------------------- rysowanie kręgosłupa od tyłu
def draw_spine(CX, Y0, S, curved=True, detail=True):
    ybase = layout(S, Y0)
    byname = {v['name']: v for v in V}
    off = make_offset(byname, S) if curved else (lambda y: 0.0)

    def frame(y):
        dy = 0.2
        dx = (off(y + dy) - off(y - dy)) / (2 * dy)
        L = math.hypot(dx, 1)
        t = (dx / L, 1 / L)                      # wzdłuż osi (w dół)
        n = (t[1], -t[0])                        # w poprzek (w prawo)
        return (CX + off(y), y), t, n

    def T(v, pts):
        c, t, n = frame(v['yc'])
        return [(c[0] + (u * n[0] + w * t[0]) * S, c[1] + (u * n[1] + w * t[1]) * S) for u, w in pts]

    out = dict(frame=frame, off=off, byname=byname, ybase=ybase, T=T)

    # --- trzony i krążki (w głębi – widoczne między łukami)
    for i, v in enumerate(V):
        if v['reg'] == 'C1':
            continue
        h, wb = v['h'], v['wb']
        if i + 1 < len(V):
            w2 = V[i + 1]
            # krążek: od dolnej powierzchni v do górnej powierzchni w2 (w układzie v)
            gap = v['disc']
            disc = [(-wb / 2 + 1.2, h / 2 - 0.2), (wb / 2 - 1.2, h / 2 - 0.2), (w2['wb'] / 2 - 1.2, h / 2 + gap + 0.2),
                    (-w2['wb'] / 2 + 1.2, h / 2 + gap + 0.2)]
            f.add(f'<path class="annulus" d="{poly(T(v, disc))}"/>')
        r = 2.0
        body = [(-wb / 2 + r, -h / 2), (wb / 2 - r, -h / 2), (wb / 2, -h / 2 + r), (wb / 2 - 0.8, 0), (wb / 2, h / 2 - r),
                (wb / 2 - r, h / 2), (-wb / 2 + r, h / 2), (-wb / 2, h / 2 - r), (-wb / 2 + 0.8, 0), (-wb / 2, -h / 2 + r)]
        if v['reg'] == 'C2':
            body = [(-4, -h / 2 - 13), (4, -h / 2 - 13), (5, -h / 2 - 4)] + body[1:-1] + [(-5, -h / 2 - 4)]
        f.add(f'<path class="bone" d="{smooth(T(v, body), t=0.4)}"/>')

    # --- łuki z wyrostkami (od dołu ku górze: wyrostki kolczyste wyższych kręgów zachodzą dachówkowato)
    ARCH, SPIN = {}, {}
    for v in V[::-1]:
        h, wt, reg = v['h'], v['wt'], v['reg']
        a = wt / 2
        if reg == 'T':
            n_ = int(v['name'][2:])
            R = [(0, -h / 2 - 1.2), (6.5, -h / 2 - 2.6), (10.0, -h / 2 - 1.0), (a - 3.5, -h / 2 - 2.6), (a, -h / 2 - 1.8),
                 (a + 0.6, -h / 2 + 1.6), (a - 1.6, -h / 2 + 4.2), (a - 5.0, -h / 2 + 4.0), (11.0, -h / 2 + 6.5),
                 (10.0, h / 2 + 0.5), (6.5, h / 2 + 1.5), (0, h / 2 - 1.0)]
            L = h * (0.55 + 0.25 * (1 - abs(n_ - 7) / 6))
            sp = [(0, -h / 2 + 3.0), (2.8, -h / 2 + 4.0), (2.4, h / 2 + L * 0.5), (2.6, h / 2 + L - 1.8), (0, h / 2 + L)]
        elif reg == 'L':
            R = [(0, -h / 2 - 1.0), (6.0, -h / 2 - 2.0), (11.5, -h / 2 - 5.0), (14.5, -h / 2 - 1.5), (14.5, -3.4),
                 (a - 3.0, -3.6), (a, -2.4), (a + 0.3, 0.8), (a - 3.0, 2.0), (15.0, 3.0), (13.5, h / 2 + 2.0),
                 (9.0, h / 2 + 4.0), (5.0, h / 2 + 1.5), (0, h / 2 + 0.5)]
            sp = [(0, -h / 2 + 2.0), (4.6, -h / 2 + 4.0), (5.0, h / 2 + 2.0), (4.0, h / 2 + 5.2), (0, h / 2 + 5.8)]
        elif reg == 'C':
            R = [(0, -h / 2 - 0.3), (7.0, -h / 2 - 0.9), (15.0, -h / 2 - 0.7), (a - 1.0, -h / 2 + 1.2), (a + 0.2, -h / 2 + 4.2),
                 (a - 1.2, h / 2 - 1.2), (15.0, h / 2 + 0.8), (7.0, h / 2 + 1.0), (0, h / 2)]
            sp = [(0, -h / 2 + 3), (2.8, -h / 2 + 4.0), (3.4, h / 2 + 2.0), (3.6, h / 2 + 4.4), (0, h / 2 + 3.4)]
        elif reg == 'C7':
            R = [(0, -h / 2 - 0.3), (7.0, -h / 2 - 1.2), (15.0, -h / 2 - 0.8), (18.0, -h / 2 + 0.6), (a - 3.0, -h / 2 + 0.2),
                 (a, -h / 2 + 1.4), (a - 0.6, -h / 2 + 4.6), (a - 4.0, -h / 2 + 5.0), (18.0, -h / 2 + 7.0),
                 (17.0, h / 2 + 0.8), (7.0, h / 2 + 1.0), (0, h / 2)]
            sp = [(0, -h / 2 + 3), (3.2, -h / 2 + 4.0), (3.0, h / 2 + 6.0), (3.4, h / 2 + 10.0), (0, h / 2 + 12.0)]
        elif reg == 'C2':
            R = [(0, -h / 2 + 2.0), (8.0, -h / 2 + 1.0), (15.0, -h / 2 - 2.5), (a - 2.0, -h / 2 + 0.5),
                 (a, -h / 2 + 4.0), (a - 2.5, -h / 2 + 8.0), (19.5, h / 2 - 2.0), (14.0, h / 2 + 1.0), (7.0, h / 2), (0, h / 2 - 1.0)]
            sp = [(0, -h / 2 + 5), (5.6, -h / 2 + 7.0), (6.6, h / 2 + 1.0), (5.4, h / 2 + 4.4), (0, h / 2 + 3.0)]
        else:  # C1 – łuk tylny + części boczne + wyrostki poprzeczne
            R = [(0, -h / 2 + 1.0), (9.0, -h / 2 + 0.4), (16.0, -h / 2 - 2.5), (a - 4.0, -h / 2 - 1.5),
                 (a, -h / 2 + 2.0), (a - 2.0, h / 2 + 1.0), (21.0, h / 2 + 2.5), (15.0, h / 2 + 2.6),
                 (8.0, h / 2 + 1.0), (0, h / 2 + 1.4)]
            sp = None
        arch = R + mirror(R, 0)[1:-1]
        pts = T(v, arch)
        ARCH[v['name']] = pts
        f.add(f'<path class="bone" d="{smooth(pts, t=0.45)}"/>')
        if sp:
            sp_full = sp + mirror(sp, 0)[1:-1]
            sp_pts = T(v, sp_full)
            SPIN[v['name']] = sp_pts
            f.add(f'<path class="bone" d="{smooth(sp_pts, t=0.45)}"/>')
    out['ARCH'], out['SPIN'] = ARCH, SPIN

    # --- kość krzyżowa (od tyłu) i kość guziczna – oś pionowa
    def SP(u, w):                                   # mm kości od środka podstawy kości krzyżowej
        return (CX + u * S, ybase + w * S)
    half = [(0, -2.0), (6.0, -2.4), (9.0, -9.0), (14.0, -9.6), (16.0, -3.0), (30.0, -1.0), (46.0, 0.0), (53.0, 4.0),
            (54.0, 14.0), (50.0, 30.0), (43.0, 45.0), (34.0, 60.0), (24.0, 76.0), (16.0, 90.0), (11.0, 100.0), (0, 101.0)]
    sac = half + mirror(half, 0)[1:-1]
    sac_pts = [SP(u, w) for u, w in sac]
    f.add(f'<path class="bone" d="{smooth(sac_pts, t=0.45)}"/>')
    if detail:
        # powierzchnia uchowata (od tyłu – zarys części bocznych), grzebień pośrodkowy, otwory krzyżowe tylne, rozwór
        for s in (-1, 1):
            for k, (u, w) in enumerate([(19.0, 18.0), (17.0, 38.0), (15.0, 57.0), (13.0, 73.0)]):
                x, y = SP(s * u, w)
                r = (3.4 - 0.45 * k) * S
                f.add(f'<ellipse class="hole" cx="{x:.2f}" cy="{y:.2f}" rx="{r:.2f}" ry="{r * 0.8:.2f}"/>')
            crest = [SP(s * u, w) for u, w in [(33.0, 8.0), (31.0, 30.0), (27.0, 52.0), (21.0, 74.0)]]
            f.add(f'<path class="bonel" d="{smooth(crest, closed=False)}"/>')
        for w in (10.0, 30.0, 50.0, 68.0):
            x, y = SP(0, w)
            f.add(f'<ellipse class="bone2" cx="{x:.2f}" cy="{y:.2f}" rx="{3.2 * S:.2f}" ry="{4.6 * S:.2f}"/>')
        hia = [SP(u, w) for u, w in [(-6.5, 101.0), (-6.0, 89.0), (-3.0, 84.0), (3.0, 84.0), (6.0, 89.0), (6.5, 101.0)]]
        f.add(f'<path class="hole" d="{smooth(hia, closed=False)} Z"/>')
    cy = ybase + 102.5 * S
    for k, (hh, ww) in enumerate([(9.0, 22.0), (7.5, 16.0), (6.0, 11.0), (5.0, 7.0)]):
        pts = [(CX - ww / 2 * S, cy), (CX + ww / 2 * S, cy), (CX + ww * 0.4 * S, cy + hh * S), (CX - ww * 0.4 * S, cy + hh * S)]
        f.add(f'<path class="bone" d="{smooth(pts, t=0.6)}"/>')
        cy += (hh + 1.6) * S
    out['SP'] = SP
    out['coccyx_end'] = (CX, cy)
    return out


# ================================================================ kręgosłup dorosłego (skolioza)
CX, Y0, S = 74.0, 7.5, 0.14
A = draw_spine(CX, Y0, S)
by, off, frame = A['byname'], A['off'], A['frame']


def lvl(n, fr=0.5):
    v = by[n]
    return v['y0'] + fr * v['h'] * S


# płaszczyzna pośrodkowa (linia pionowa przez środek kości krzyżowej)
f.add(f'<path class="dim" d="M{CX:.2f},{Y0 - 4.0:.2f} L{CX:.2f},{A["coccyx_end"][1] + 2.0:.2f}"/>')


def axis_pt(y, d=0.0):
    """punkt na osi kręgosłupa na wysokości y, przesunięty o d (mm rysunku) w poprzek osi (+ w prawo)"""
    c, t, n = frame(y)
    return (c[0] + n[0] * d, c[1] + n[1] * d)


def bracket(y_a, y_b, d, tick):
    """klamra wzdłuż osi w odległości d; ząbki na końcach (tick – ku kręgosłupowi). Zwraca punkt środkowy."""
    pts = [axis_pt(y_a + (y_b - y_a) * k / 30, d) for k in range(31)]
    dd = 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts)
    for y in (y_a, y_b):
        p0, p1 = axis_pt(y, d), axis_pt(y, d - tick)
        dd += f' M{p0[0]:.2f},{p0[1]:.2f} L{p1[0]:.2f},{p1[1]:.2f}'
    f.add(f'<path class="lead" d="{dd}"/>')
    return axis_pt((y_a + y_b) / 2, d)


def top(n):
    return by[n]['y0']


def bot(n):
    return by[n]['y0'] + by[n]['h'] * S


mC = bracket(top('C2') + 0.6, bot('C7'), -5.9, -1.0)
mT = bracket(top('Th3') - 0.3, bot('Th6') + 0.3, 6.0, 1.0)
mL = bracket(top('L1'), bot('L5'), -7.6, -1.0)

# strony ciała (widok od tyłu: lewa strona ciała po lewej stronie rysunku)
f.text(CX - 7.4, Y0 + 1.6, 'strona lewa', cls='note', anchor='end')
f.text(CX + 7.4, Y0 + 1.6, 'strona prawa', cls='note', anchor='start')

TL, TR = 57.0, 91.0


def notes(x, y, lines, side):
    for k, t in enumerate(lines):
        f.text(x + (0.7 if side == 'R' else -0.7), y + 6.6 + 2.6 * k, t, cls='note', anchor='start' if side == 'R' else 'end')


# --- lewa kolumna
f.label(mC, 'skolioza drugostronna szyi', None, (TL, mC[1] - 2.0), side='L')
notes(TL, mC[1] - 2.0 - 3.0, ['kompensacyjna – względy ortooptyczne'], 'L')
v5 = by['Th5']
p5 = A['T'](v5, [(-v5['wt'] / 2 + 1.0, -v5['h'] / 2 + 1.2)])[0]
f.label(p5, 'piąty kręg piersiowy', None, (TL, 31.0), side='L')
notes(TL, 31.0 - 3.0, ['jakoby najsłabsze miejsce kręgosłupa –', 'tu najczęściej boczne skrzywienia'], 'L')
v12 = by['Th12']
p12 = A['T'](v12, [(0, v12['h'] / 2 + 5.0)])[0]
f.label(p12, 'wyrostek kolczysty', 'processus spinosus', (TL, 55.0), side='L')
f.label(mL, 'lewostronnie wypukła skolioza lędźwiowa', None, (TL, mL[1] - 2.0), side='L')
notes(TL, mL[1] - 2.0 - 3.0, ['kompensacyjna – względy statyczne', '(np. z powodu dłuższej kończyny dolnej lewej)'], 'L')

# --- prawa kolumna
f.label((CX, Y0 - 2.6), 'płaszczyzna pośrodkowa', None, (TR, Y0 - 2.6), side='R')
f.label(mT, 'prawostronnie wypukła skolioza piersiowa', None, (TR, mT[1] - 2.0), side='R')
notes(TR, mT[1] - 2.0 - 3.0, ['wypukłość na prawo, przeważnie na wysokości', 'trzeciego – szóstego kręgu piersiowego;',
                              'najczęstsza (52%), lewostronna tylko 16%'], 'R')
v10 = by['Th10']
p10 = A['T'](v10, [(v10['wt'] / 2 - 3.0, -v10['h'] / 2 + 1.0)])[0]
f.label(p10, 'wyrostek poprzeczny', 'processus transversus', (TR, 54.0), side='R')
vL = by['L3']
pL = A['T'](vL, [(11.0, 5.0)])[0]
f.label(pL, 'kręgi lędźwiowe', 'vertebrae lumbales', (TR, 78.0), side='R')
pS = A['SP'](30.0, 40.0)
f.label(pS, 'kość krzyżowa', 'os sacrum', (TR, 100.0), side='R')

if os.environ.get('PTS'):
    for v in V:
        print(v['name'], round(v['yc'], 1), round(off(v['yc']), 2))
    print('base', A['ybase'], 'coccyx', A['coccyx_end'])
f.save()
