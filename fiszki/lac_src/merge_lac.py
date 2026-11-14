# Scala lac_1..6.json (wyciąg z Bochenka) w site/lac_data.js: bez powtórzeń łaciny, działy w kolejności książki.
import json, os, re, sys, collections
FZ = os.path.dirname(os.path.abspath(__file__)) + '/'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site', 'lac_data.js')
DROP = set(x.strip().lower() for x in open(FZ + 'lac_drop.txt').read().split('\n') if x.strip() and not x.startswith('#')) if os.path.exists(FZ + 'lac_drop.txt') else set()
def norm(s): return re.sub(r'[^a-z]+', ' ', s.lower()).strip()
seen = {}; groups = []; stats = collections.Counter(); dups = []
for n in range(1, 7):
    f = FZ + f'lac_{n}.json'
    if not os.path.exists(f): print('BRAK', f); continue
    for x in json.load(open(f)):
        la = re.sub(r'\s+', ' ', x['la'].replace('*', '')).strip(); pl = re.sub(r'\s+', ' ', x['pl']).strip()
        k = norm(la)
        if k in DROP: stats['pominięte (lista)'] += 1; continue
        if k in seen:
            if norm(seen[k]['p']) != norm(pl): dups.append((la, seen[k]['p'], pl))
            stats['powtórzenia'] += 1; continue
        it = {'p': pl, 'l': la, 's': x['s']}
        alt = [a.replace('*', '').strip() for a in (x.get('alt') or []) if a and norm(a) != k]
        if alt: it['a'] = alt
        if x.get('k'): it['k'] = 1
        seen[k] = it
        t = x['t'].strip()
        if not groups or groups[-1]['t'] != t: groups.append({'t': t, 'i': []})
        groups[-1]['i'].append(it); stats['nazwy'] += 1
# 14.11: usuń nazwy, które użytkownik w 1. rundzie dał do banku „umiem”; resztę w liczbie pojedynczej (szpilki).
# Każda fiszka zachowuje id = klucz ze starej łaciny, żeby postęp się nie zgubił.
REM = set(json.load(open(FZ + 'usuniete_umiem.json')))
SG = json.load(open(FZ + 'pojedyncza.json'))
def okey(la): return 'l:' + re.sub(r'[^a-z]+', '-', la.lower())
ng = []
for g in groups:
    its = []
    for it in g['i']:
        k = okey(it['l'])
        if k in REM: stats['usunięte (umiem)'] += 1; continue
        it['id'] = k
        for kk in (k, k + '#2'):
            if kk not in SG: continue
            v = SG[kk]; x = dict(it) if kk != k else it
            x['id'] = kk; x['p'], x['l'] = v[0], v[1]
            if len(v) > 2: x['a'] = v[2]
            elif 'a' in x and kk != k: del x['a']
            if 'a' in x and not x['a']: del x['a']
            if kk != k: its.append(x); stats['rozdzielone'] += 1
            else: stats['na pojedynczą'] += 1
        its.insert(len(its) - (1 if (k + '#2') in SG else 0), it)
    if its: ng.append({'t': g['t'], 'i': its})
groups = ng
seen = {norm(it['l']): it for g in groups for it in g['i']}
# druga nazwa nie może być główną nazwą innej fiszki (np. dawne „plicae umbilicales laterales”)
MAIN = set(seen)
for g in groups:
    for it in g['i']:
        if 'a' in it:
            bad = [a for a in it['a'] if norm(a) in MAIN]
            if bad: print('usuwam drugą nazwę', bad, 'przy', it['l']); it['a'] = [a for a in it['a'] if norm(a) not in MAIN]
            if not it['a']: del it['a']
# scal działy o tej samej nazwie, które wypadły obok siebie po usunięciu powtórzeń
out = []
for g in groups:
    if out and out[-1]['t'] == g['t']: out[-1]['i'] += g['i']
    elif g['i']: out.append(g)
open(OUT, 'w', encoding='utf-8').write('/* Wszystkie nazwy łacińskie z rozdziałów Bochenka (t. I) na zaliczenie: s. 219–298 i 649–733. Generowane: merge_lac.py */\nwindow.LAC=' + json.dumps({'groups': out}, ensure_ascii=False, separators=(',', ':')) + ';\n')
print(dict(stats), 'działów', len(out))
for g in out: print(f"  {len(g['i']):3}  {g['t']}")
if dups: print('ta sama łacina, różne polskie:'); [print('  ', d) for d in dups]
