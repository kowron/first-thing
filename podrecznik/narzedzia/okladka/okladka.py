#!/usr/bin/env python3
"""Grafika okładki podręcznika: atomowy model podwójnej helisy DNA (forma B) w perspektywie,
z głębią ostrości, plus wypisy (skok helisy, bruzdy) – czysty, wektorowy SVG.

  python3 narzedzia/okladka/okladka.py            przelicza grafikę i podmienia <svg class="cv-art"> w front/cover.html
  python3 narzedzia/okladka/okladka.py --svg X    dodatkowo zapisuje samą grafikę do pliku X (samodzielny SVG)
  node narzedzia/okladka/podglad.mjs wynik.png    szybki podgląd okładki bez składania całej książki

Teksty okładki (tytuł, podtytuł, opis, podziałka rozdziałów, liczniki) są w front/cover.html i w bloku
„Okładka” w css/style.css – skrypt ich nie rusza, wymienia tylko element <svg class="cv-art">.

Jak to jest narysowane (i dlaczego tak):
- Model: wszystkie ciężkie atomy helisy B (dna.py), promienie van der Waalsa; nić I jasnozielona, nić II złota,
  zasady ciemnozielone. Helisa prawoskrętna, 10 par zasad na skręt, bruzda większa i mniejsza wynikają z geometrii.
- Każdy atom to <use> symbolu złożonego z zagnieżdżonych „kropek”. Kropka = bardzo krótka kreska z okrągłym
  zakończeniem (M x y h.01), czyli koło. Chromium zapisuje taką kreskę w PDF kilkunastoma bajtami, podczas gdy
  <circle> to ok. 30 krzywych, a każde użycie gradientu to kilka osobnych obiektów PDF (1000 kul z gradientem
  = kilka MB). Cała okładka waży w PDF ok. 0,3 MB i pozostaje wektorowa; filtrów (blur) nie ma, bo Chromium
  rasteryzuje je w 300 dpi.
- Symbole są uniwersalne: kolor cienia i światła podaje egzemplarz (<use color="…" stroke="…">), a światłocień
  powstaje z półprzezroczystych warstw. Mgła (dal), okluzja (bruzdy) i światło całej helisy zmieniają tylko te
  dwa kolory, więc przejścia są płynne, a symboli jest kilkadziesiąt.
- Głębia ostrości: kula poza płaszczyzną ostrości dostaje symbol z miękką krawędzią (warstwy o rosnącym kryciu).
- Kolejność rysowania: od najdalszych (algorytm malarza); kule całkowicie zasłonięte są pomijane.
Jednostka SVG = 1 mm strony A4 (210 × 297). Model w angstremach (1 nm = 10 Å).
"""
import argparse, math, os, re, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True      # bez katalogu __pycache__ w repozytorium
from dna import COMP, RISE, TWIST, rotz, template     # noqa: E402

W, H = 210.0, 297.0
PX = 0.2645833                      # 1 px CSS w mm (rozmiary pisma podajemy w px)
VDW = {'C': 1.70, 'N': 1.55, 'O': 1.52, 'P': 1.85}

# ------------------------------------------------------------------ ustawienia
# Kamera: patrzy z dołu wzdłuż helisy (elev < 0), więc dół strony jest bliżej (duży, nieostry), góra ginie w dali.
CAM = dict(target=(0, 0, 0), dist=80.0, elev=-34, azim=20, roll=-8, focal=262, center=(154, 172))

CFG = dict(
    i0=-45, i1=85,                               # zakres par zasad modelu
    znear=14.0, zfar=420.0,
    fog='#153b28', deep='#081a11', fog0=95.0, fog1=300.0, fogp=0.75, fogmax=0.93,     # mgła w dali
    aok=0.74, amb=0.43, macrop=1.15, aomix=0.55, darkmax=0.82,                        # okluzja i światło helisy
    rim=[0.05, 0.12, 0.21, 0.31], rimcol='#c9f0d6', rimdir=(0.80, -0.15, 0.58),       # światło kontrowe
    aperture=1.7, focus_shift=-7.0, sharp=0.07, farblur=0.3, farblurmax=0.2,          # głębia ostrości
    blur_levels=[0.10, 0.16, 0.25, 0.38, 0.56, 0.8, 1.15, 1.6],
    halo=0.85, minalpha=0.30,
    lod=[0.9, 2.2, 4.6],                         # progi promienia (mm) dla liczby warstw kuli
    glow=dict(op=0.075, size=3.2, stride=3),     # poświata pod helisą
)

# Materiały: c – kolor w świetle, sh – kolor w cieniu, ks – połysk. Klucz z cyfrą 1 = nić II.
MAT = {
    'P':   dict(c='#dcf3e4', sh='#36684f', ks=0.75),      # nić I: jasna zieleń (cukry = #8fd3a6 z palety książki)
    'OP':  dict(c='#c8ecd5', sh='#2f6048', ks=0.72),
    'OB':  dict(c='#b2e3c4', sh='#295741', ks=0.62),
    'SC':  dict(c='#8fd3a6', sh='#1f5139', ks=0.55),
    'SO':  dict(c='#a0dab4', sh='#235a40', ks=0.55),
    'P1':  dict(c='#f0c452', sh='#7a5310', ks=0.95),      # nić II: złoto
    'OP1': dict(c='#e9b84a', sh='#6f4b10', ks=0.85),
    'OB1': dict(c='#d9a941', sh='#5f4310', ks=0.75),
    'SC1': dict(c='#c99a35', sh='#4f370c', ks=0.7),
    'SO1': dict(c='#d4a53c', sh='#573d0e', ks=0.7),
    'BC':  dict(c='#1f6a46', sh='#07201a', ks=0.4),       # zasady: ciemna zieleń
    'BN':  dict(c='#2b8a5e', sh='#0a2a1c', ks=0.45),
    'BO':  dict(c='#4fae80', sh='#103526', ks=0.5),
}

# Tło strony
PAL = dict(top='#0e2a1c', mid='#143a27', bottom='#0d261a', glow0='#256645', glow1='#1b5038')
GLOW = (150, 176, 150)              # poświata tła: środek x, y i promień (mm)
TOPFADE = (128, 0.88)               # przyciemnienie pod tytułem: wysokość (mm) i siła

# Wypisy
ANN_X = 18.0                        # linia wymiarowa = lewy margines tekstu
ANN_Y = (112, 222)                  # zakres wysokości, w którym szukamy pełnego skrętu
MINT, WHITE = '#8fd3a6', '#ffffff'

# Sekwencja nici I (5'->3'): początek mRNA genu β-globiny (HBB) – odcinek 5'UTR i pierwsze kodony.
SEQ = ('ACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACC'
       'ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAG')
SEQ0 = 50                           # indeks A z kodonu ATG (para zasad nr 0 modelu)


# ------------------------------------------------------------------ drobne narzędzia
def hex2rgb(h):
    h = h.lstrip('#')
    if len(h) == 3:
        h = ''.join(ch * 2 for ch in h)
    return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], float)


def rgb2hex(c):
    c = np.clip(np.round(c), 0, 255).astype(int)
    s = '%02x%02x%02x' % (c[0], c[1], c[2])
    if s[0] == s[1] and s[2] == s[3] and s[4] == s[5]:
        s = s[0] + s[2] + s[4]
    return '#' + s


def mix(a, b, t):
    return a * (1 - t) + b * t


def smooth(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def num(v, nd=2):
    """Liczba do SVG: bez zbędnych zer."""
    s = ('%.' + str(nd) + 'f') % v
    if '.' in s:
        s = s.rstrip('0').rstrip('.')
    if s.startswith('0.'):
        s = s[1:]
    elif s.startswith('-0.'):
        s = '-' + s[2:]
    return s if s not in ('', '-', '-0') else '0'


def base36(n):
    d = '0123456789abcdefghijklmnopqrstuvwxyz'
    s = ''
    while True:
        s = d[n % 36] + s
        n //= 36
        if n == 0:
            return s


# ------------------------------------------------------------------ model
TEMPL = {b: template(b) for b in 'AGTC'}


def material(name):
    if name == 'P':
        return 'P'
    if name in ('OP1', 'OP2'):
        return 'OP'
    if name in ("O5'", "O3'"):
        return 'OB'
    if name == "O4'":
        return 'SO'
    if name.endswith("'"):
        return 'SC'
    return 'B' + name[0]            # BC, BN, BO


def matkey(a):
    """Klucz materiału: najpierw wariant dla nici (np. 'P1'), potem ogólny."""
    k = a['mat'] + str(a['st'])
    return k if k in MAT else a['mat']


def base_at(i, st=0):
    b = SEQ[(i + SEQ0) % len(SEQ)]
    return b if st == 0 else COMP[b]


def atom_pos(i, st, name, base):
    """Położenie atomu (Å) nukleotydu w parze i; st = 0 (nić I) lub 1 (nić II)."""
    p = TEMPL[base][name]
    if st == 1:
        p = np.array([p[0], -p[1], -p[2]])
    return rotz(p, i * TWIST, i * RISE)


def build_model(i0, i1):
    atoms = []
    for i in range(i0, i1):
        for st in (0, 1):
            b = base_at(i, st)
            for name in TEMPL[b]:
                atoms.append(dict(p=atom_pos(i, st, name, b), el=name[0], name=name, mat=material(name), i=i, st=st, base=b))
    return atoms


def ambient_occlusion(P, radius=6.5):
    """Prosta okluzja: ważona liczba sąsiadów w promieniu; 0 = atom odsłonięty, 1 = najgłębiej schowany."""
    n = len(P)
    ao = np.zeros(n)
    for a in range(0, n, 400):
        d = np.linalg.norm(P[a:a + 400, None, :] - P[None, :, :], axis=2)
        w = np.clip(1 - d / radius, 0, 1)
        ao[a:a + 400] = w.sum(axis=1) - 1.0
    lo, hi = np.percentile(ao, 4), np.percentile(ao, 97)
    return np.clip((ao - lo) / (hi - lo), 0, 1)


# ------------------------------------------------------------------ kamera
class Camera:
    """Rzut perspektywiczny. Układ prawoskrętny bez odbicia lustrzanego – skręt helisy na obrazie jest prawdziwy."""

    def __init__(self, target, dist, elev, azim, roll, focal, center):
        e, a = math.radians(elev), math.radians(azim)
        d = np.array([math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
        self.pos = np.array(target, float) + dist * d
        f = -d
        up = np.array([0, 0, 1.0])
        r = np.cross(f, up); r /= np.linalg.norm(r)
        u = np.cross(r, f)
        ro = math.radians(roll)
        self.r = math.cos(ro) * r + math.sin(ro) * u
        self.u = -math.sin(ro) * r + math.cos(ro) * u
        self.f, self.F = f, focal
        self.cx, self.cy = center
        self.dist = dist

    def project(self, P):
        """-> x, y na stronie (mm), głębia (Å), skala (mm/Å)."""
        V = np.asarray(P, float) - self.pos
        z = V @ self.f
        s = self.F / z
        return self.cx + s * (V @ self.r), self.cy - s * (V @ self.u), z, s


# ------------------------------------------------------------------ symbole kul
LIGHT = np.array([-0.50, -0.62, 0.60]); LIGHT /= np.linalg.norm(LIGHT)      # światło: z lewej z góry, od widza
NCAP = {3: (22, 9), 2: (14, 6), 1: (7, 3), 0: (3, 1)}       # liczba warstw: (światło rozproszone, połysk)
GLOSS = [0.0, 0.22, 0.45, 0.7, 0.95]
CDIF = 0.80                         # powyżej tej jasności zaczyna się połysk
LIMB_GAP = 0.015                    # kontur po stronie światła (ułamek promienia)


def t_dif(c):
    return smooth(c / CDIF) ** 0.9


def inv_t(t):
    lo, hi = 0.0, CDIF
    for _ in range(40):
        mid = (lo + hi) / 2
        if t_dif(mid) < t:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def cap_circle(c):
    """Okrąg przybliżający obszar o jasności >= c na kuli jednostkowej oświetlonej z kierunku LIGHT: (cx, cy, r)."""
    lx, ly, lz = LIGHT
    s = math.hypot(lx, ly)
    rho = math.sqrt(max(0.0, 1 - c * c))
    e_far = c * s - rho * lz
    e_near = min(1.0, c * s + rho * lz)
    if c <= s:
        # czasza sięga za brzeg tarczy po stronie światła: jasny obszar dochodzi (prawie) do brzegu kuli;
        # wąski ciemny margines zostaje jako delikatny kontur oddzielający sąsiednie kule
        e_near = 1.0 - LIMB_GAP
    r_axis = (e_near - e_far) / 2
    m = (e_near + e_far) / 2
    r = min(0.55 * r_axis + 0.45 * rho, 1.0 - m)
    return m * lx / s, m * ly / s, r


def blur_alpha(b):
    return min(1.0, max(CFG['minalpha'], 1.0 / (0.55 + b) ** 1.3))


class Symbols:
    """Symbole kul o promieniu 1: ostre (liczba warstw, połysk, światło kontrowe) i rozmyte (poziom rozmycia, połysk)."""

    def __init__(self):
        self.map = {}

    @staticmethod
    def dot(x, y, r, paint=None, op=None):
        s = '<path d="M%s %sh.01"' % (num(x - 0.005, 3), num(y, 3))
        if paint:
            s += ' stroke="%s"' % paint
        s += ' stroke-width="%s"' % num(2 * r, 3)
        if op is not None and op < 0.997:
            s += ' stroke-opacity="%s"' % num(op, 3)
        return s + '/>'

    def _add(self, key, out):
        sid = 'cv-' + base36(len(self.map) + 10)
        self.map[key] = (sid, '<g id="%s">%s</g>' % (sid, ''.join(out)))
        return sid

    def get(self, lod, blurq, glossq, rimq=0):
        key = (lod, blurq, glossq, rimq)
        if key in self.map:
            return self.map[key][0]
        gloss = GLOSS[glossq]
        out = []
        lx, ly, _ = LIGHT
        if blurq == 0:
            nd, ns = NCAP[lod]
            out.append(self.dot(0, 0, 1.0, 'currentColor'))             # podkład: kolor cienia
            if lod >= 1:
                # światło kontrowe: jasny sierp po stronie cienia (prawy dolny brzeg kuli)
                ra = CFG['rim'][rimq]
                wd = 0.05 + 0.02 * rimq
                out.append(self.dot(0, 0, 1.0, CFG['rimcol'], ra))
                if lod >= 2:
                    out.append(self.dot(lx * wd * 0.5, ly * wd * 0.5, 1 - wd * 0.5, CFG['rimcol'], ra * 0.6))
                out.append(self.dot(lx * wd, ly * wd, 1 - wd, 'currentColor'))
            # światło rozproszone: warstwy w kolorze światła (stroke egzemplarza) o rosnącym kryciu
            prev = 0.0
            for k in range(nd):
                c = inv_t(k / nd) if k else 0.0
                T = (k + 0.6) / nd if k < nd - 1 else 1.0
                a = 1 - (1 - T) / (1 - prev) if prev < 0.999 else 1.0
                prev = T
                x, y, r = cap_circle(c)
                out.append(self.dot(x, y, r, None, a))
            if gloss > 0:                                                # połysk: białe warstwy
                prev = 0.0
                for k in range(ns):
                    c = CDIF + (1 - CDIF) * math.sqrt(k / ns) if k else CDIF + (1 - CDIF) * 0.12
                    Wt = gloss * ((k + 0.7) / ns) ** 1.15
                    a = 1 - (1 - Wt) / (1 - prev)
                    prev = Wt
                    x, y, r = cap_circle(c)
                    out.append(self.dot(x, y, r, '#fffdf2', a))
        else:
            b = CFG['blur_levels'][blurq - 1]
            g = CFG['halo']
            A = blur_alpha(b)
            r_out, r_in = 1 + b * g, max(0.10, 1 - b * g)
            K = int(round(8 + 22 * min(1.0, b / 1.2)))
            prev = 0.0
            for k in range(K):                     # miękka krawędź w kolorze pośrednim (stroke egzemplarza)
                r = r_out + (r_in - r_out) * k / (K - 1)
                C = A * smooth((k + 1) / K)
                a = (C - prev) / (1 - prev)
                prev = C
                out.append(self.dot(0, 0, r, None, a))
            # światło: warstwy w kolorze światła (currentColor) przesunięte ku światłu
            soft = max(0.0, 1 - 0.6 * min(1.0, b))
            q = r_in ** 0.4
            for c in (0.08, 0.18, 0.28, 0.38, 0.47, 0.56, 0.64, 0.71, 0.77):
                x, y, r = cap_circle(c)
                if r * q < 0.04:
                    continue
                out.append(self.dot(x * q, y * q, r * q, 'currentColor', 0.24 * A))
            if gloss > 0:
                for c in (0.83, 0.88, 0.92, 0.95, 0.975):
                    x, y, r = cap_circle(c)
                    if r * q < 0.03:
                        continue
                    out.append(self.dot(x * q, y * q, r * q * (1 + 0.5 * b), '#fffdf2', (0.10 + 0.10 * soft) * gloss * A))
        return self._add(key, out)

    def glow(self):
        """Bardzo miękki krążek – poświata pod helisą."""
        if 'glow' in self.map:
            return self.map['glow'][0]
        out = []
        K = 22
        prev = 0.0
        for k in range(K):
            r = 1.0 - 0.94 * k / (K - 1)
            C = 0.92 * (smooth((k + 1) / K) ** 1.6)
            a = (C - prev) / (1 - prev)
            prev = C
            out.append(self.dot(0, 0, r, None, a))
        return self._add('glow', out)

    def defs(self):
        return '\n'.join(s for _, s in self.map.values())


# ------------------------------------------------------------------ render helisy
def shade_atoms(cam, atoms, P, Z):
    """Kolor cienia i światła każdego atomu (okluzja, światło całej helisy, mgła), połysk i siła światła kontrowego."""
    cfg = CFG
    fogc, deep = hex2rgb(cfg['fog']), hex2rgb(cfg['deep'])
    ao = ambient_occlusion(P)
    Lw = LIGHT[0] * cam.r - LIGHT[1] * cam.u - LIGHT[2] * cam.f
    rr = np.hypot(P[:, 0], P[:, 1]) + 1e-9
    ncyl = np.c_[P[:, 0] / rr, P[:, 1] / rr, np.zeros(len(P))]
    macro = np.clip(ncyl @ Lw, -1, 1) * np.clip(rr / 9.0, 0, 1)
    lit = cfg['amb'] + (1 - cfg['amb']) * np.clip(0.5 + 0.5 * macro, 0, 1) ** cfg['macrop']
    dark = np.clip((1 - (1 - ao * cfg['aomix']) * lit) / cfg['darkmax'], 0, 1)
    fog = np.clip((Z - cfg['fog0']) / (cfg['fog1'] - cfg['fog0']), 0, 1) ** cfg['fogp'] * cfg['fogmax']
    rimw = cfg['rimdir'][0] * cam.r + cfg['rimdir'][1] * cam.u + cfg['rimdir'][2] * cam.f
    rimw = rimw / np.linalg.norm(rimw)
    rimf = np.clip(ncyl @ rimw, 0, 1) ** 1.5 * np.clip(rr / 9.0, 0, 1) * (1 - fog) ** 1.2
    rimf = rimf * np.where(ncyl @ (-cam.f) < -0.15, 0.3, 1.0)       # tylna strona helisy: bez jasnych obrysów
    S = np.zeros((len(atoms), 3)); B = np.zeros((len(atoms), 3)); G = np.zeros(len(atoms))
    aok = cfg['aok']
    for j, a in enumerate(atoms):
        m = MAT[matkey(a)]
        b, s = hex2rgb(m['c']), hex2rgb(m['sh'])
        d = dark[j]
        b2 = mix(b, mix(s, deep, 0.35), d * aok)
        s2 = mix(s, deep, d * aok * 0.9)
        S[j] = mix(s2, fogc, fog[j]); B[j] = mix(b2, fogc, fog[j])
        G[j] = m.get('ks', 0.6) * (1 - 0.7 * d) * (1 - fog[j]) ** 1.5
    return S, B, G, fog, rimf


def render(cam):
    cfg = CFG
    zfocus = cam.dist + cfg['focus_shift']
    atoms = build_model(cfg['i0'], cfg['i1'])
    P = np.array([a['p'] for a in atoms])
    X, Y, Z, Sc = cam.project(P)
    R = np.array([VDW[a['el']] for a in atoms]) * Sc
    ok = (Z > cfg['znear']) & (X > -R * 2.6) & (X < W + R * 2.6) & (Y > -R * 2.6) & (Y < H + R * 2.6) & (Z < cfg['zfar'])
    # głębia ostrości: promień rozmycia rośnie z odległością od płaszczyzny ostrości (w dali słabiej)
    coc = cfg['aperture'] * cam.F * np.abs(1.0 / np.maximum(Z, 1e-6) - 1.0 / zfocus)
    coc = np.where(Z > zfocus, np.minimum(coc * cfg['farblur'], cfg['farblurmax'] * R), coc)
    b = coc / R
    levels = cfg['blur_levels']
    blurq = np.zeros(len(atoms), int)
    for k, lv in enumerate(levels):
        lo = cfg['sharp'] if k == 0 else math.sqrt(levels[k - 1] * lv)
        blurq[b >= lo] = k + 1
    S, B, G, fog, rimf = shade_atoms(cam, atoms, P, Z)
    # usuwanie kul całkowicie zasłoniętych przez bliższe nieprzezroczyste
    lvl = np.array([0.0] + levels)[blurq]
    core = np.where(blurq == 0, R * 0.985, 0.0)
    for k, lv in enumerate(levels):
        if blur_alpha(lv) >= 0.999:
            sel = blurq == k + 1
            core[sel] = R[sel] * max(0.10, 1 - lv * cfg['halo'])
    ext = R * (1 + lvl * cfg['halo'])
    idx = np.nonzero(ok)[0]
    order = idx[np.argsort(Z[idx])]            # od najbliższych
    ang = np.linspace(0, 2 * math.pi, 10, endpoint=False)
    samp = np.concatenate([[(0.0, 0.0)], np.c_[np.cos(ang), np.sin(ang)] * 0.97, np.c_[np.cos(ang + 0.3), np.sin(ang + 0.3)] * 0.55])
    keep, kx, ky, kr = [], [], [], []
    for j in order:
        if kx:
            ax, ay, ar = np.array(kx), np.array(ky), np.array(kr)
            near = (np.abs(ax - X[j]) < ar + ext[j]) & (np.abs(ay - Y[j]) < ar + ext[j])
            if near.any():
                ax, ay, ar = ax[near], ay[near], ar[near]
                px, py = X[j] + samp[:, 0] * ext[j], Y[j] + samp[:, 1] * ext[j]
                d2 = (px[:, None] - ax[None, :]) ** 2 + (py[:, None] - ay[None, :]) ** 2
                if (d2 < ar[None, :] ** 2).any(axis=1).all():
                    continue
        keep.append(j)
        if core[j] > 0:
            kx.append(X[j]); ky.append(Y[j]); kr.append(core[j])
    sym = Symbols()
    items = []
    stats = dict(atomy=len(idx), narysowane=len(keep), rozmyte=0)
    for j in keep:
        gq = int(np.argmin([abs(G[j] - g) for g in GLOSS]))
        if blurq[j] == 0:
            lod = 3 if R[j] > cfg['lod'][2] else 2 if R[j] > cfg['lod'][1] else 1 if R[j] > cfg['lod'][0] else 0
            if lod == 0:
                gq = min(gq, 1)
            rq = 0 if rimf[j] < 0.12 else 1 if rimf[j] < 0.4 else 2 if rimf[j] < 0.7 else 3
            if atoms[j]['mat'][0] == 'B':          # ciemne zasady: bez mocnego jasnego obrysu
                rq = min(rq, 1)
            sid = sym.get(lod, 0, gq, rq if lod >= 1 else 0)
            c1, c2 = rgb2hex(S[j]), rgb2hex(B[j])                       # color = cień, stroke = światło
        else:
            stats['rozmyte'] += 1
            sid = sym.get(0, int(blurq[j]), min(gq, 3) if gq else 0)
            c2, c1 = rgb2hex(mix(S[j], B[j], 0.42)), rgb2hex(B[j])     # stroke = kolor pośredni, color = światło
        items.append((Z[j], '<use href="#%s" color="%s" stroke="%s" transform="translate(%s %s)scale(%s)"/>' % (
            sid, c1, c2, num(X[j]), num(Y[j]), num(R[j], 3))))
    # poświata: miękkie krążki w kolorze światła pod helisą (co kilka atomów szkieletu)
    g = cfg['glow']
    fmax = 0.45
    sel = [j for j in keep if fog[j] < fmax and atoms[j]['mat'] in ('P', 'OP', 'SC', 'OB', 'SO')][::g['stride']]
    for j in sel:
        w = 1 - fog[j] / fmax
        items.append((1e9, '<use href="#%s" stroke="%s" opacity="%s" transform="translate(%s %s)scale(%s)"/>' % (
            sym.glow(), rgb2hex(mix(B[j], hex2rgb('#ffffff'), 0.15)), num(g['op'] * w, 3), num(X[j]), num(Y[j]), num(R[j] * g['size'], 2))))
    stats['poświata'] = len(sel)
    items.sort(key=lambda t: -t[0])            # od najdalszych
    stats['symbole'] = len(sym.map)
    return sym, [s for _, s in items], stats


# ------------------------------------------------------------------ tło i przyciemnienie
def background():
    gx, gy, gr = GLOW
    p = PAL
    defs = ('<radialGradient id="cv-bg1" gradientUnits="userSpaceOnUse" cx="%s" cy="%s" r="%s">'
            '<stop offset="0" stop-color="%s"/><stop offset=".4" stop-color="%s" stop-opacity=".9"/>'
            '<stop offset="1" stop-color="%s" stop-opacity="0"/></radialGradient>'
            '<linearGradient id="cv-bg2" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="297">'
            '<stop offset="0" stop-color="%s"/><stop offset=".5" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>'
            % (gx, gy, gr, p['glow0'], p['glow1'], p['mid'], p['top'], p['mid'], p['bottom']))
    body = ('<rect width="210" height="297" fill="url(#cv-bg2)"/>'
            '<rect width="210" height="297" fill="url(#cv-bg1)"/>')
    return defs, body


def overlay():
    """Przyciemnienie górnej strefy: dalsza część helisy ginie w mroku pod tytułem."""
    h, k = TOPFADE
    p = PAL
    defs = ('<linearGradient id="cv-top" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="%s">'
            '<stop offset="0" stop-color="%s" stop-opacity="%s"/><stop offset=".5" stop-color="%s" stop-opacity="%s"/>'
            '<stop offset=".8" stop-color="%s" stop-opacity="%s"/><stop offset="1" stop-color="%s" stop-opacity="0"/></linearGradient>'
            % (h, p['top'], num(.97 * k), p['top'], num(.84 * k), p['mid'], num(.4 * k), p['mid']))
    return defs, '<rect width="210" height="%s" fill="url(#cv-top)"/>' % h


# ------------------------------------------------------------------ wypisy
def T(x, y, s, size, fill=MINT, anchor='start', weight=500, family='Inter', ls=None, rot=0):
    """Tekst SVG: położenie w mm, rozmiar pisma w px CSS (skalowanie w transform)."""
    tr = 'translate(%s %s)' % (num(x), num(y)) + ('rotate(%s)' % num(rot, 1) if rot else '') + 'scale(%s)' % num(PX, 5)
    a = ' text-anchor="%s"' % anchor if anchor != 'start' else ''
    l = ' letter-spacing="%s"' % ls if ls else ''
    return '<text transform="%s" font-family="%s" font-size="%s" font-weight="%s" fill="%s"%s%s>%s</text>' % (
        tr, family, num(size, 2), weight, fill, a, l, s)


def L(pts, w=0.18, col=MINT, op=0.55):
    d = 'M' + 'L'.join('%s %s' % (num(x), num(y)) for x, y in pts)
    return '<path d="%s" stroke="%s" stroke-width="%s" stroke-opacity="%s" fill="none"/>' % (d, col, num(w, 3), num(op))


def marker(x, y, col=WHITE):
    return ('<circle cx="%s" cy="%s" r="1.25" fill="none" stroke="%s" stroke-width=".2" stroke-opacity=".85"/>'
            '<circle cx="%s" cy="%s" r=".42" fill="%s"/>') % (num(x), num(y), col, num(x), num(y), col)


def annotations(cam):
    """Wymiar „skok helisy” (ten sam atom nici I w dwóch kolejnych skrętach = 10 par zasad = 3,4 nm),
    wypisy bruzd (środek bruzdy zwrócony ku kamerze) i pasek sekwencji przy lewej krawędzi."""
    o = []
    info = {}
    az = math.degrees(math.atan2(cam.pos[1], cam.pos[0]))      # azymut kamery wokół osi helisy

    def P2(p):
        x, y, z, s = cam.project(np.array(p, float))
        return np.array([x, y]), z, s

    def groove(kind, k):
        # oś x układu pary wskazuje bruzdę większą; bruzda mniejsza leży po przeciwnej stronie
        th = az if kind == 'major' else az + 180.0
        zz = (th / TWIST + 10 * k) * RISE
        ang = math.radians(az)
        rad = 7.6 if kind == 'major' else 8.6
        return P2((rad * math.cos(ang), rad * math.sin(ang), zz))

    x0 = ANN_X
    xl = x0 + 5.2                          # początek wypisów
    lo, hi = ANN_Y

    # --- skok helisy: dwa kolejne skręty nici I na lewym obrysie (ten sam atom, 10 par dalej)
    best = None
    for widen in (0, 8, 16, 30, 60):
        for i in range(-30, 31):
            b = base_at(i, 0)
            for name in ('P', 'OP1', 'OP2'):
                pa, _, sa = P2(atom_pos(i, 0, name, b))
                pb, _, sb = P2(atom_pos(i + 10, 0, name, base_at(i + 10, 0)))
                ra, rb = VDW[name[0]] * sa, VDW[name[0]] * sb
                if not (lo - widen <= pb[1] and pa[1] <= hi + widen):
                    continue
                score = (pa[0] - ra) + (pb[0] - rb)        # oba punkty jak najdalej w lewo
                if best is None or score < best[0]:
                    best = (score, pa, ra, pb, rb, i, name)
        if best:
            break
    _, pa, ra, pb, rb, ip, nm = best
    ya, yb = pa[1], pb[1]                  # dół i góra
    for (p, r) in ((pa, ra), (pb, rb)):
        o.append(L([(x0, p[1]), (p[0] - r - 0.9, p[1])], op=0.42))
        o.append('<circle cx="%s" cy="%s" r=".45" fill="%s"/>' % (num(p[0] - r - 0.9), num(p[1]), WHITE))
    o.append(L([(x0, yb), (x0, ya)], op=0.8, w=0.2))
    for y in (ya, yb):                     # zakończenia wymiaru: ukośne kreski
        o.append(L([(x0 - 0.9, y + 0.9), (x0 + 0.9, y - 0.9)], op=0.95, w=0.25, col=WHITE))
    o.append(T(xl, yb - 1.9, 'PODWÓJNA HELISA DNA · FORMA B', 7.3, fill='#a9d9ba', weight=600, ls='.2em'))
    info['skok'] = (round(float(yb), 1), round(float(ya), 1), 'pary %d i %d' % (ip, ip + 10), nm)

    # --- wypisy bruzd: poziome linie do znacznika na helisie
    cands = []
    for kind, name in (('minor', 'Bruzda mniejsza'), ('major', 'Bruzda większa')):
        for k in range(-3, 4):
            pt, _, _ = groove(kind, k)
            cands.append((pt[1], name, pt))
    sel = sorted([c for c in cands if yb + 7 <= c[0] <= ya - 5], key=lambda c: c[0])
    for yy, name, pt in sel:
        o.append(L([(xl, pt[1]), (pt[0] - 1.25, pt[1])], op=0.42))
        o.append(marker(pt[0], pt[1]))
        o.append(T(xl, pt[1] - 1.9, name.upper(), 7.3, fill='#a9d9ba', weight=600, ls='.2em'))
    info['bruzdy'] = [(round(float(c[0]), 1), c[1]) for c in sel]

    # --- wartość wymiaru: w największej wolnej przerwie między liniami
    ys = [yb] + [c[0] for c in sel] + [ya]
    g, g0, g1 = sorted(((ys[k + 1] - ys[k], ys[k], ys[k + 1]) for k in range(len(ys) - 1)), reverse=True)[0]
    yv = (g0 + g1) / 2 + 3.6
    o.append(T(xl, yv - 9.2, 'SKOK HELISY', 7.3, fill='#a9d9ba', weight=600, ls='.2em'))
    o.append(T(xl - 0.35, yv, '3,4 nm', 26, fill=WHITE, weight=300, family="'Inter Display'", ls='-.01em'))
    o.append(T(xl, yv + 5.2, 'ok. 10 par zasad na skręt', 7.7, fill='#8fb49e', weight=400, ls='.02em'))

    # --- pasek sekwencji przy lewej krawędzi (nić I, 5'->3', pierwsze 30 kodonów)
    seq = SEQ[SEQ0:SEQ0 + 90]
    cod = ' '.join(seq[i:i + 3] for i in range(0, len(seq), 3))
    o.append(T(8.4, 281.8, '5′ – ' + cod + ' – 3′', 6.0, fill='#6a9a80', weight=400,
               family="'JetBrains Mono'", ls='.165em', rot=-90))
    return '\n'.join(o), info


# ------------------------------------------------------------------ całość
def art():
    cam = Camera(**CAM)
    sym, body, stats = render(cam)
    d1, b1 = background()
    d2, b2 = overlay()
    ann, info = annotations(cam)
    # jeden element w wierszu – czytelniejsze różnice w repozytorium po ponownym wygenerowaniu
    svg = '\n'.join(['<svg class="cv-art" viewBox="0 0 210 297" aria-hidden="true">',
                     '<defs>', d1, d2, sym.defs(), '</defs>', b1,
                     '<g fill="none" stroke-linecap="round">', '\n'.join(body), '</g>', b2,
                     '<g class="cv-ann">', ann, '</g>', '</svg>'])
    stats.update(info)
    return svg, stats


def main():
    ap = argparse.ArgumentParser(description='Grafika okładki: przelicza model helisy i podmienia <svg class="cv-art"> w front/cover.html')
    ap.add_argument('--svg', help='zapisz dodatkowo samą grafikę jako samodzielny plik SVG')
    ap.add_argument('--bez-zapisu', action='store_true', help='nie zmieniaj front/cover.html')
    a = ap.parse_args()
    svg, stats = art()
    print('grafika: %d KB' % (len(svg.encode('utf-8')) // 1024), stats)
    if a.svg:
        alone = svg.replace('<svg class="cv-art"', '<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" class="cv-art"', 1)
        open(a.svg, 'w', encoding='utf-8').write(alone)
        print('zapisano', a.svg)
    if not a.bez_zapisu:
        path = os.path.join(ROOT, 'front', 'cover.html')
        html = open(path, encoding='utf-8').read()
        # sam element (z atrybutem viewBox) – wzmianka o nim w komentarzu pliku nie może pasować do wzorca
        new, n = re.subn(r'<svg class="cv-art" viewBox=[\s\S]*?</svg>', lambda m: svg, html, count=1)
        if n != 1:
            sys.exit('front/cover.html: nie znaleziono elementu svg.cv-art – wstaw <svg class="cv-art" viewBox="0 0 210 297"></svg> '
                     'jako pierwsze dziecko <section class="cover">')
        if new != html:
            open(path, 'w', encoding='utf-8').write(new)
            print('podmieniono grafikę w', path)
        else:
            print('bez zmian:', path)


if __name__ == '__main__':
    main()
