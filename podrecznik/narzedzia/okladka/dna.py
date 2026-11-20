#!/usr/bin/env python3
"""Model atomowy (ciężkie atomy) idealnej podwójnej helisy DNA w formie B – do grafiki okładki.

Zasady: standardowa geometria zasad w układzie odniesienia pary (Olson i in. 2001; współrzędne w Å,
oś x wskazuje bruzdę większą, oś z biegnie w kierunku 5'->3' nici I).
Szkielet cukrowo-fosforanowy: zbudowany z długości wiązań, kątów i kątów torsyjnych (cukier C2'-endo,
zasada anti); kąty dopasowane tak, żeby O3'(i) łączył się z P(i+1) przy 10 parach zasad na skręt
i odstępie 3,38 Å między parami (skok helisy 3,38 nm) – wynik dopasowania leży w szkielet.json
(python3 dna.py --dopasuj liczy go od nowa).
Nić I biegnie 5'->3' w kierunku +z; nić II powstaje przez obrót o 180° wokół osi x układu pary.
Helisa jest prawoskrętna: kolejna para jest obrócona o +36° i przesunięta o +3,38 Å.
"""
import itertools, json, math, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

BASES = {
    'A': {"C1'": (-2.479, 5.346, 0.000), 'N9': (-1.291, 4.498, 0.000), 'C8': (0.024, 4.897, 0.000),
          'N7': (0.877, 3.902, 0.000), 'C5': (0.071, 2.771, 0.000), 'C6': (0.369, 1.398, 0.000),
          'N6': (1.611, 0.909, 0.000), 'N1': (-0.668, 0.532, 0.000), 'C2': (-1.912, 1.023, 0.000),
          'N3': (-2.320, 2.290, 0.000), 'C4': (-1.267, 3.124, 0.000)},
    'G': {"C1'": (-2.477, 5.399, 0.000), 'N9': (-1.289, 4.551, 0.000), 'C8': (0.023, 4.962, 0.000),
          'N7': (0.870, 3.969, 0.000), 'C5': (0.071, 2.833, 0.000), 'C6': (0.424, 1.460, 0.000),
          'O6': (1.554, 0.955, 0.000), 'N1': (-0.700, 0.641, 0.000), 'C2': (-1.999, 1.087, 0.000),
          'N2': (-2.949, 0.139, -0.001), 'N3': (-2.342, 2.364, 0.001), 'C4': (-1.265, 3.177, 0.000)},
    'T': {"C1'": (-2.481, 5.354, 0.000), 'N1': (-1.284, 4.500, 0.000), 'C2': (-1.462, 3.135, 0.000),
          'O2': (-2.562, 2.608, 0.000), 'N3': (-0.298, 2.407, 0.000), 'C4': (0.994, 2.897, 0.000),
          'O4': (1.944, 2.119, 0.000), 'C5': (1.106, 4.338, 0.000), 'C7': (2.466, 4.961, 0.001),
          'C6': (-0.024, 5.057, 0.000)},
    'C': {"C1'": (-2.477, 5.402, 0.000), 'N1': (-1.285, 4.542, 0.000), 'C2': (-1.472, 3.158, 0.000),
          'O2': (-2.628, 2.709, 0.000), 'N3': (-0.391, 2.344, 0.000), 'C4': (0.837, 2.868, 0.000),
          'N4': (1.875, 2.027, 0.001), 'C5': (1.056, 4.275, 0.000), 'C6': (-0.023, 5.068, 0.000)},
}
COMP = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
SUGAR_ATOMS = ["O4'", "C2'", "C3'", "C4'", "C5'", "O3'", "O5'", 'P', 'OP1', 'OP2']

TWIST = 36.0      # stopni na parę zasad (10 par na skręt)
RISE = 3.38       # Å między parami (skok helisy 33,8 Å = ok. 3,4 nm)


# ------------------------------------------------------------------ geometria
def place(a, b, c, bond, angle, torsion):
    """Atom D: |CD| = bond, kąt BCD = angle, torsja ABCD = torsion (stopnie, konwencja IUPAC)."""
    a, b, c = (np.asarray(v, float) for v in (a, b, c))
    ang, tor = math.radians(angle), math.radians(torsion)
    bc = c - b; bc /= np.linalg.norm(bc)
    n = np.cross(b - a, bc); n /= np.linalg.norm(n)
    m = np.cross(n, bc)
    d2 = np.array([-bond * math.cos(ang), bond * math.sin(ang) * math.cos(tor), bond * math.sin(ang) * math.sin(tor)])
    return c + d2[0] * bc + d2[1] * m + d2[2] * n


def dihedral(a, b, c, d):
    b0 = a - b; b1 = c - b; b2 = d - c
    b1n = b1 / np.linalg.norm(b1)
    v = b0 - (b0 @ b1n) * b1n
    w = b2 - (b2 @ b1n) * b1n
    return math.degrees(math.atan2(np.cross(b1n, v) @ w, v @ w))


def angle(a, b, c):
    u, v = a - b, c - b
    return math.degrees(math.acos((u @ v) / np.linalg.norm(u) / np.linalg.norm(v)))


def rotz(p, deg, dz):
    """Obrót wokół osi helisy o deg stopni i przesunięcie o dz wzdłuż niej."""
    t = math.radians(deg)
    c, s = math.cos(t), math.sin(t)
    return np.array([c * p[0] - s * p[1], s * p[0] + c * p[1], p[2] + dz])


# ------------------------------------------------------------------ szkielet cukrowo-fosforanowy
def build_sugar(base, prm, stereo):
    """Atomy cukru i fosforanu nukleotydu nici I w układzie pary.
    prm: chi (wiązanie glikozydowe), P i tm (pofałdowanie cukru), gamma, beta, alpha (szkielet).
    stereo: trzy znaki ustalające konfigurację C1', C4' i C3' (naturalna: −1, −1, −1 – jedyna, przy której
    szkielet zamyka się przy kanonicznych kątach helisy B)."""
    B = {k: np.array(v) for k, v in BASES[base].items()}
    pur = base in 'AG'
    N = B['N9'] if pur else B['N1']
    Cref = B['C4'] if pur else B['C2']
    C1 = B["C1'"]
    s1, s2, s3 = stereo
    chi, P, tm = prm['chi'], prm['P'], prm['tm']
    nu = [tm * math.cos(math.radians(P + 144.0 * (j - 2))) for j in range(5)]
    at = {}
    at["O4'"] = place(Cref, N, C1, 1.420, 108.2, chi)
    at["C2'"] = place(Cref, N, C1, 1.525, 113.6, chi + s1 * 120.0)
    at["C3'"] = place(at["O4'"], C1, at["C2'"], 1.525, 102.6, nu[1])
    at["C4'"] = place(C1, at["C2'"], at["C3'"], 1.527, 102.8, nu[2])
    at["C5'"] = place(at["C2'"], at["C3'"], at["C4'"], 1.510, 115.0, nu[3] + s2 * 120.0)
    at["O3'"] = place(at["O4'"], at["C4'"], at["C3'"], 1.430, 110.0, nu[3] + s3 * 120.0)
    at["O5'"] = place(at["C3'"], at["C4'"], at["C5'"], 1.440, 110.5, prm['gamma'])
    at['P'] = place(at["C4'"], at["C5'"], at["O5'"], 1.593, 120.5, prm['beta'])
    # tlen O3' poprzedniego nukleotydu (do kontroli) i dwa tleny niemostkowe
    at['O3p'] = place(at["C5'"], at["O5'"], at['P'], 1.607, 104.0, prm['alpha'])
    at['OP1'] = place(at["C5'"], at["O5'"], at['P'], 1.485, 108.2, prm['alpha'] + 115.0)
    at['OP2'] = place(at["C5'"], at["O5'"], at['P'], 1.485, 108.2, prm['alpha'] - 115.0)
    at['_ringclose'] = np.linalg.norm(at["C4'"] - at["O4'"])
    return at


_FIT = None


def template(base):
    """Wszystkie ciężkie atomy nukleotydu nici I (zasada + cukier + fosforan) w układzie pary: {nazwa: xyz}."""
    global _FIT
    if _FIT is None:
        _FIT = json.load(open(os.path.join(HERE, 'szkielet.json'), encoding='utf-8'))
    f = _FIT[base]
    at = build_sugar(base, f['prm'], tuple(f['stereo']))
    atoms = {k: np.array(v, float) for k, v in BASES[base].items()}
    for k in SUGAR_ATOMS:
        atoms[k] = at[k]
    return atoms


# ------------------------------------------------------------------ dopasowanie kątów szkieletu
def closure(at, direction=+1):
    """Połączenie O3'(i) – P(i+1): odległość, dwa kąty i torsje epsilon, zeta, alfa."""
    Pn = rotz(at['P'], direction * TWIST, direction * RISE)
    O5n = rotz(at["O5'"], direction * TWIST, direction * RISE)
    C5n = rotz(at["C5'"], direction * TWIST, direction * RISE)
    d = np.linalg.norm(at["O3'"] - Pn)
    a1 = angle(at["C3'"], at["O3'"], Pn)
    a2 = angle(at["O3'"], Pn, O5n)
    eps = dihedral(at["C4'"], at["C3'"], at["O3'"], Pn)
    zeta = dihedral(at["C3'"], at["O3'"], Pn, O5n)
    alpha = dihedral(at["O3'"], Pn, O5n, C5n)
    return d, a1, a2, eps, zeta, alpha


def _wrap(a, lo):
    return (a - lo) % 360.0 + lo


def _flat(v, lo, hi, sig):
    return ((lo - v) / sig) ** 2 if v < lo else ((v - hi) / sig) ** 2 if v > hi else 0.0


def score(at, prm, direction=+1):
    """Kara: geometria połączenia + odstępstwa od kanonicznych kątów helisy B (BI) + położenie atomu P."""
    d, a1, a2, eps, zeta, alpha = closure(at, direction)
    delta = dihedral(at["C5'"], at["C4'"], at["C3'"], at["O3'"])
    geo = ((d - 1.607) / 0.015) ** 2 + ((a1 - 119.7) / 2.0) ** 2 + ((a2 - 104.0) / 2.0) ** 2 + ((at['_ringclose'] - 1.446) / 0.02) ** 2
    tor = (_flat(prm['chi'], -125, -95, 5) + _flat(prm['P'], 135, 180, 5) + _flat(prm['tm'], 33, 42, 2)
           + _flat(prm['gamma'], 40, 65, 5) + _flat(_wrap(prm['beta'], 0), 150, 200, 5)
           + _flat(_wrap(eps, 0), 165, 215, 5) + _flat(_wrap(zeta, 0), 240, 285, 5) + _flat(_wrap(alpha, 0), 280, 320, 5)
           + _flat(_wrap(delta, 0), 120, 150, 5))
    r, z = math.hypot(at['P'][0], at['P'][1]), at['P'][2]
    return geo + tor + _flat(r, 8.85, 9.15, 0.08) + _flat(z, -2.5, -1.6, 0.15)


def climb(base, stereo, direction, rng, starts=10, iters=2500):
    best = None
    keys = ['chi', 'P', 'tm', 'gamma', 'beta']
    for _ in range(starts):
        prm = dict(chi=rng.uniform(-125, -95), P=rng.uniform(135, 180), tm=rng.uniform(34, 41),
                   gamma=rng.uniform(40, 65), beta=rng.uniform(150, 200), alpha=-62.0)
        s = score(build_sugar(base, prm, stereo), prm, direction)
        step = 6.0
        for it in range(iters):
            q = dict(prm)
            for k in keys:
                q[k] = prm[k] + rng.normal(0, step)
            s2 = score(build_sugar(base, q, stereo), q, direction)
            if s2 < s:
                s, prm = s2, q
            if it % (iters // 5) == iters // 5 - 1:
                step *= 0.45
        if best is None or s < best[0]:
            best = (s, prm)
    return best


def fit(path):
    """Szuka konfiguracji i kątów; zapisuje wynik do pliku JSON (ok. 2 minut)."""
    rng = np.random.default_rng(7)
    res = []
    for stereo in itertools.product((1, -1), repeat=3):
        for direction in (1, -1):
            s, prm = climb('A', stereo, direction, rng, starts=4, iters=900)
            res.append((s, stereo, direction))
            print('konfiguracja', stereo, 'kierunek', direction, 'kara %.2f' % s, flush=True)
    res.sort(key=lambda t: t[0])
    _, stereo, direction = res[0]
    out = {}
    for b in 'AGTC':
        s, prm = climb(b, stereo, direction, rng)
        at = build_sugar(b, prm, stereo)
        d, a1, a2, eps, zeta, alpha = closure(at, direction)
        prm['alpha'] = alpha
        print(b, "kara %.3f  O3'-P %.3f Å  P: r %.2f Å, z %.2f Å" % (s, d, math.hypot(at['P'][0], at['P'][1]), at['P'][2]))
        out[b] = dict(stereo=list(stereo), direction=direction, prm=prm)
    json.dump(out, open(path, 'w', encoding='utf-8'), indent=1)


if __name__ == '__main__':
    if '--dopasuj' in sys.argv:
        fit(os.path.join(HERE, 'szkielet.json'))
    else:
        for b in 'AGTC':
            t = template(b)
            print(b, len(t), 'atomów; P: r = %.2f Å' % math.hypot(t['P'][0], t['P'][1]))
