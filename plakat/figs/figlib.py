# -*- coding: utf-8 -*-
"""Wspólna biblioteka rysunków do plakatów (styl jednolity).
Jednostki: 1 jednostka = 1 mm na plakacie (rysunek wstawiany w skali 1:1).

Użycie:
    from figlib import Fig
    f = Fig('kr_th_typ_gora', 90, 70, caption='kręg piersiowy typowy – widok od góry')
    f.add('<path class="bone" d="..."/>')              # kształty (klasy stylu poniżej)
    f.label((x, y), 'trzon kręgu', 'corpus vertebrae', (tx, ty))   # podpis z linią
    f.save()                                             # → figs/out/<nazwa>.svg

Klasy stylu (używaj tylko tych):
  bone      – kość (wypełnienie kremowe, kontur brązowy)
  bone2     – powierzchnia przekroju / inna płaszczyzna kości (ciemniejszy krem)
  bonel     – cienka linia szczegółu na kości (brzeg, grzebień, bruzda) – bez wypełnienia
  facet     – powierzchnia stawowa (jasnoniebieska, chrząstka stawowa)
  cart      – chrząstka (żebrowa, krążek itp.)
  annulus   – pierścień włóknisty krążka
  nucleus   – jądro miażdżyste
  lig       – więzadło (ochra)
  capsule   – torebka stawowa (przerywana linia)
  cavity    – jama stawowa / szpara (białe wypełnienie)
  muscle    – mięsień
  tendon    – ścięgno / środek ścięgnisty
  nerve, artery, vein, organ – nerw, tętnica, żyła, narząd (np. płuco, serce)
  hole      – otwór (białe wypełnienie, kontur kości)
  shade     – delikatny cień (półprzezroczysty)
  arrow     – strzałka ruchu (niebieska, z grotem)   – użyj f.arrow(...)
  arrow2    – strzałka przeciwna / druga faza (czerwona)
  axis      – oś obrotu (kreska-kropka, czerwona)
  dim       – linia wymiarowa / pomocnicza (szara, cienka)
  note      – tekst pomocniczy w rysunku (szary, mały) – użyj f.text(...)
"""
import os, html

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')
os.makedirs(OUT, exist_ok=True)

STYLE = """
.bone{fill:#f3e7d0;stroke:#6b5640;stroke-width:.35;stroke-linejoin:round}
.bone2{fill:#e2cfab;stroke:#6b5640;stroke-width:.3;stroke-linejoin:round}
.bonel{fill:none;stroke:#8a7356;stroke-width:.22;stroke-linecap:round;stroke-linejoin:round}
.facet{fill:#cfe3f1;stroke:#4f7fa3;stroke-width:.28}
.cart{fill:#d7eaf5;stroke:#5c8db0;stroke-width:.3}
.annulus{fill:#e3edf7;stroke:#6f92b5;stroke-width:.28}
.nucleus{fill:#a9cbe8;stroke:#4f7fa3;stroke-width:.28}
.lig{fill:#efd28a;stroke:#a7822a;stroke-width:.28}
.ligl{fill:none;stroke:#b8902e;stroke-width:.55;stroke-linecap:round}
.capsule{fill:none;stroke:#7a6a55;stroke-width:.3;stroke-dasharray:1 .6}
.cavity{fill:#ffffff;stroke:#7a6a55;stroke-width:.22}
.muscle{fill:#eaa595;stroke:#b4553f;stroke-width:.3}
.musclel{fill:none;stroke:#c9705b;stroke-width:.2}
.tendon{fill:#f4ead6;stroke:#a89268;stroke-width:.3}
.nerve{fill:#f6d55c;stroke:#b8961c;stroke-width:.25}
.artery{fill:#e05a5a;stroke:#a82f2f;stroke-width:.25}
.vein{fill:#5b82c9;stroke:#33589b;stroke-width:.25}
.organ{fill:#f0d9e6;stroke:#a5708c;stroke-width:.28}
.hole{fill:#ffffff;stroke:#6b5640;stroke-width:.3}
.shade{fill:#6b5640;opacity:.10;stroke:none}
.arrow{fill:none;stroke:#1f6fd1;stroke-width:.7;stroke-linecap:round;marker-end:url(#ah)}
.arrow2{fill:none;stroke:#d23c3c;stroke-width:.7;stroke-linecap:round;marker-end:url(#ah2)}
.axis{fill:none;stroke:#d23c3c;stroke-width:.4;stroke-dasharray:2.2 .8 .4 .8}
.dim{fill:none;stroke:#8d939a;stroke-width:.22;stroke-dasharray:.8 .5}
.lead{fill:none;stroke:#3a3d42;stroke-width:.18;stroke-linejoin:round}
.dot{fill:#3a3d42}
.pl{font-family:Inter,sans-serif;font-weight:600;font-size:2.55px;fill:#1f2328}
.la{font-family:'TeX Gyre Pagella',serif;font-style:italic;font-size:2.45px;fill:#6b5a3c}
.note{font-family:Inter,sans-serif;font-size:2.1px;fill:#6c737c}
.notec{font-family:Inter,sans-serif;font-size:2.1px;fill:#6c737c;text-anchor:middle}
.big{font-family:Inter,sans-serif;font-weight:800;font-size:3.2px;fill:#1f2328}
.cap{font-family:Inter,sans-serif;font-size:2.2px;fill:#7b828a;letter-spacing:.08px;text-anchor:middle;font-weight:600}
"""

DEFS = """<defs>
<marker id="ah" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4.2" markerHeight="4.2" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#1f6fd1"/></marker>
<marker id="ah2" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4.2" markerHeight="4.2" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d23c3c"/></marker>
</defs>"""


def esc(t):
    return html.escape(t, quote=False)


class Fig:
    def __init__(self, name, w, h, caption=None):
        self.name, self.w, self.h, self.caption = name, w, h, caption
        self.body, self.labels_svg = [], []

    def add(self, svg):
        self.body.append(svg)

    def text(self, x, y, t, cls='note', anchor='start'):
        self.body.append(f'<text x="{x:.2f}" y="{y:.2f}" class="{cls}" text-anchor="{anchor}">{esc(t)}</text>')

    def arrow(self, d, red=False):
        self.body.append(f'<path class="{"arrow2" if red else "arrow"}" d="{d}"/>')

    def label(self, at, pl, lat=None, to=None, side=None, elbow=True, one_line=False):
        """at=(x,y) punkt na strukturze; to=(tx,ty) miejsce tekstu (początek linii tekstu).
        side='R' – tekst na prawo od 'to' (wyrównany do lewej), 'L' – na lewo (wyrównany do prawej).
        Domyślnie side wynika z położenia: to[0] >= at[0] → 'R'."""
        ax, ay = at
        tx, ty = to
        if side is None:
            side = 'R' if tx >= ax else 'L'
        # linia: od punktu do (tx, ty) z krótkim poziomym odcinkiem przy tekście
        if elbow:
            kx = tx - 1.6 if side == 'R' else tx + 1.6
            pts = f'{ax:.2f},{ay:.2f} {kx:.2f},{ty:.2f} {tx:.2f},{ty:.2f}'
        else:
            pts = f'{ax:.2f},{ay:.2f} {tx:.2f},{ty:.2f}'
        self.labels_svg.append(f'<polyline class="lead" points="{pts}"/><circle class="dot" cx="{ax:.2f}" cy="{ay:.2f}" r=".38"/>')
        anchor = 'start' if side == 'R' else 'end'
        x = tx + 0.7 if side == 'R' else tx - 0.7
        if lat and one_line:
            self.labels_svg.append(f'<text x="{x:.2f}" y="{ty + 0.9:.2f}" text-anchor="{anchor}"><tspan class="pl">{esc(pl)}</tspan>'
                                   f'<tspan class="la" dx="1">{esc(lat)}</tspan></text>')
        else:
            self.labels_svg.append(f'<text x="{x:.2f}" y="{ty + 0.9:.2f}" class="pl" text-anchor="{anchor}">{esc(pl)}</text>')
            if lat:
                self.labels_svg.append(f'<text x="{x:.2f}" y="{ty + 3.6:.2f}" class="la" text-anchor="{anchor}">{esc(lat)}</text>')

    def svg(self):
        cap = ''
        if self.caption:
            cap = f'<text x="{self.w / 2:.2f}" y="{self.h - 1.2:.2f}" class="cap">{esc(self.caption)}</text>'
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}mm" height="{self.h}mm">'
                f'<style>{STYLE}</style>{DEFS}<g>{"".join(self.body)}</g><g>{"".join(self.labels_svg)}</g>{cap}</svg>')

    def save(self):
        p = os.path.join(OUT, self.name + '.svg')
        open(p, 'w', encoding='utf-8').write(self.svg())
        return p


def smooth(pts, closed=True, t=0.5):
    """Gładka ścieżka przez punkty (Catmull-Rom → Bézier). pts = [(x,y), ...]"""
    n = len(pts)
    if n < 3:
        return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts)
    P = (pts[-1:] + pts + pts[:2]) if closed else ([pts[0]] + pts + [pts[-1]])
    d = f'M{P[1][0]:.2f},{P[1][1]:.2f}'
    rng = range(1, n + 1) if closed else range(1, n)
    for i in rng:
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) * t / 3, p1[1] + (p2[1] - p0[1]) * t / 3)
        c2 = (p2[0] - (p3[0] - p1[0]) * t / 3, p2[1] - (p3[1] - p1[1]) * t / 3)
        d += f' C{c1[0]:.2f},{c1[1]:.2f} {c2[0]:.2f},{c2[1]:.2f} {p2[0]:.2f},{p2[1]:.2f}'
    return d + (' Z' if closed else '')


def mirror(pts, cx):
    """Odbicie listy punktów względem pionowej osi x=cx (kolejność odwrócona – do domykania konturu)."""
    return [(2 * cx - x, y) for x, y in reversed(pts)]


def shift(pts, dx=0, dy=0, s=1.0, ox=0, oy=0):
    return [((x - ox) * s + ox + dx, (y - oy) * s + oy + dy) for x, y in pts]
