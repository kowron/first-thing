#!/usr/bin/env python3
"""Buduje strony plakatu: dla każdej strony szuka NAJWIĘKSZEJ skali tekstu K, przy której treść mieści się na stronie (A0 1189x841 mm),
i składa jeden PDF.  Użycie: ./build_pages.py [strona ...]   (kregoslup klatka m1 m2 m3 polkreg klodd)
Zmienne: LIMIT (maks. dół treści, domyślnie 826), KS (lista skal), L3MIN (min. rozmiar opisów poziomu 3 w pt, domyślnie 5.3)."""
import os, re, subprocess, sys, json
from pypdf import PdfWriter
ROOT = '/home/user/first-thing/plakat'
OUT = os.environ.get('OUT', '/tmp/claude-0/-home-user-first-thing/d41721b4-1413-50bf-8c94-691fa5e52b07/scratchpad/pages')
os.makedirs(OUT, exist_ok=True)
PW, PH = 1189, 841
LIMIT = float(os.environ.get('LIMIT', 826))
KS = [float(x) for x in os.environ.get('KS', '1.05,1.0,0.95,0.9,0.85,0.8,0.75').split(',')]
L3MIN = float(os.environ.get('L3MIN', 5.8))
ENV0 = dict(os.environ, PLAYWRIGHT_BROWSERS_PATH='/opt/pw-browsers', EXFIG=os.environ.get('EXFIG', '0.75'))

# strony: (rodzaj, parametry). 'os' = build_os.py (nazwa, layout, only, env szerokości, FS),  'mus' = build.py (rozdziały, env)
PAGES = {
 'kregoslup': ('os', dict(layout='kosciec', only='kregoslup', env=dict(CWS=160, CWT=104), fs=0.85)),
 'klatka':    ('os', dict(layout='kosciec', only='klatka', env=dict(CWS=112, CWT=165, CWPOL=450), fs=0.8)),
 'm1':        ('mus', dict(regions='grzbiet', env=dict(ROOT_TITLE='Grzbiet', ROOT_SUB='mięśnie grzbietu – powierzchowne i głębokie', W_pow=300, W_band=240, W_krot=150, W_podp=150))),
 'm2':        ('mus', dict(regions='klatka', env=dict(ROOT_TITLE='Klatka piersiowa', ROOT_SUB='mięśnie klatki piersiowej', W_kpow=280, W_kgleb=300, W_kprz=400, DOCKCOLS_klatka=2))),
 'm3':        ('mus', dict(regions='brzuch', env=dict(ROOT_TITLE='Brzuch', ROOT_SUB='mięśnie brzucha · pochewka · kanał pachwinowy', W_bbocz=380, W_bprzed=330, W_btyl=330, DOCKSPLIT_brzuch='btyl:6,bprzed:2,bbocz:9', DOCKCOLS_brzuch=1))),
 'polkreg':   ('os', dict(layout='mech', only='polkreg', env=dict(CWM=270), fs=0.85)),
 'klodd':     ('os', dict(layout='mech', only='klodd', env=dict(CWM=120, CWK6=300, CWO=848), fs=0.75)),
}
ORDER = ['kregoslup', 'klatka', 'm1', 'm2', 'm3', 'polkreg', 'klodd']

def run(cmd, env):
    return subprocess.run(cmd, env=env, cwd=ROOT, capture_output=True, text=True).stdout

def measure(html, name, env):
    out = run(['python3', '../scripts/pdf_poster2.py', f'{ROOT}/{html}', f'{OUT}/{name}.pdf'], env)
    b = re.search(r'max_bottom (\d+)', out); r = re.search(r'max_right (\d+)', out)
    over = len(re.findall(r'^over \|', out, flags=re.M)); ov = len(re.findall(r'^overlap \|', out, flags=re.M))
    return (int(b.group(1)) if b else 9999), (int(r.group(1)) if r else 0), over, ov

def build(name, K):
    kind, p = PAGES[name]
    env = dict(ENV0, L3S=str(round(max(1.2, L3MIN / (3.9 * K)), 2)), **{k: str(v) for k, v in p['env'].items()})
    if kind == 'os':
        env.update(PAGE=name, LAYOUT=p['layout'], DATA='kosciec' if p['layout'] == 'kosciec' else 'mech', ONLY=p['only'], PW=str(PW), PH=str(PH), K=str(K), FIGSCALE=str(p['fs']))
        run(['../scripts/meas.sh', name, str(K), str(p['fs'])], env)
        run(['python3', 'build_os.py'], env)
        return measure(f'page_{name}.html', name, env)
    env.update(PAGE=f'{PW}x{PH}', K=str(K), REGIONS=p['regions'], OUT=f'page_{name}.html')
    run(['python3', 'build.py'], env)
    return measure(f'page_{name}.html', name, env)

todo = sys.argv[1:] or ORDER
res = {}
def ok(name, K):
    b, r, over, ov = build(name, K)
    print(f'  {name:10s} K={K:<6} dół={b:4d} prawo={r:4d} over={over} overlap={ov}', flush=True)
    return b <= LIMIT and over == 0 and ov == 0
LO, HI, STEP = float(os.environ.get('KLO', 0.75)), float(os.environ.get('KHI', 1.5)), float(os.environ.get('KSTEP', 0.02))
for name in todo:
    # wyszukiwanie binarne największego K, które się mieści (zakładamy: mniejsze K = niższa strona)
    # punkt startowy: pierwsze K (od góry), które się mieści – przy bardzo małym K drobny druk (L3MIN) rośnie, więc K=LO nie zawsze jest „najbezpieczniejsze”
    hi = HI; lo = next((k for k in (1.0, 0.95, 0.9, 0.85, 0.8, LO) if k >= LO and ok(name, k)), None)
    if lo is None:
        res[name] = None; print(f'== {name}: nie mieści się nawet przy K={LO}', flush=True); continue
    while hi - lo > STEP:
        mid = round((lo + hi) / 2, 3)
        if ok(name, mid): lo = mid
        else: hi = mid
    lo = round(lo, 3); ok(name, lo)          # końcowe zbudowanie wybranej wersji
    res[name] = lo
    print(f'== {name}: wybrane K = {lo}', flush=True)
w = PdfWriter()
for n in ORDER:
    f = f'{OUT}/{n}.pdf'
    if os.path.exists(f):
        w.append(f)
w.add_metadata({'/Title': 'Plakat „Anatomia: szkielet osiowy” (wg Bochenka, t. I)'})
w.write('/home/user/first-thing/Plakat_A0_5_szkielet_osiowy.pdf')
print('PDF złożony, stron:', len(w.pages), res)
