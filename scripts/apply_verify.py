# Nakłada poprawki z verify_<ch>.json na l3_<ch>.json (fix_t=None -> usunięcie punktu)
import json, re, sys
ch = sys.argv[1]
L = f'/home/user/first-thing/plakat/l3_{ch}.json'
V = f'/home/user/first-thing/plakat/verify_{ch}.json'
d = json.load(open(L, encoding='utf-8'))
v = json.load(open(V, encoding='utf-8'))
dels = []
for iss in v['issues']:
    m = re.match(r'(muscles|groups|panels)/(.+?)\s*#(\d+)\s*$', iss['where'].strip())
    if not m:
        print('?? nie rozumiem:', iss['where']); continue
    sec, key, idx = m.group(1), m.group(2).strip(), int(m.group(3))
    if sec == 'panels':
        lst = next(p for p in d['panels'] if p['id'] == key)['items']
    else:
        lst = d[sec][key]
    if iss.get('fix_t') is None:
        dels.append((sec, key, idx, lst)); continue
    lst[idx]['t'] = iss['fix_t']
    if iss.get('fix_pg'):
        lst[idx]['pg'] = iss['fix_pg']
    print('poprawione:', iss['where'])
for sec, key, idx, lst in sorted(dels, key=lambda x: -x[2]):
    print('usunięte:', sec, key, idx, '|', lst[idx]['t'][:80])
    del lst[idx]
json.dump(d, open(L, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
