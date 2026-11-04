# Nakłada poprawki z verify_<ID>.json na plik drzewa k_*.json
# użycie: apply_verify2.py k_kregoslup verify_V1 [verify_V2 ...] [--skip ID:idx,...] [--dry]
import json, re, sys

args = [a for a in sys.argv[1:] if not a.startswith('--')]
opts = [a for a in sys.argv[1:] if a.startswith('--')]
dry = '--dry' in opts
skip = set()
for o in opts:
    if o.startswith('--skip='):
        skip |= set(o[7:].split(','))
P = f'/home/user/first-thing/plakat/{args[0]}.json'
d = json.load(open(P, encoding='utf-8'))


def walk(ns):
    for n in ns:
        yield n
        yield from walk(n.get('children', []))


def node(title):
    for n in walk(d['tree']):
        if n.get('title') == title:
            return n
    for n in walk(d['tree']):
        if n.get('title', '').strip().lower() == title.strip().lower():
            return n
    return None


dels = []   # (lista, indeks, opis)
for vf in args[1:]:
    vid = vf.split('_')[-1]
    v = json.load(open(f'/home/user/first-thing/plakat/{vf}.json', encoding='utf-8'))
    for k, iss in enumerate(v.get('issues', [])):
        tag = f'{vid}:{k}'
        if tag in skip:
            print('pominięte', tag); continue
        n = node(iss['card'])
        if n is None:
            print('?? brak węzła', tag, iss['card']); continue
        f, fix = iss['field'].strip(), iss.get('fix')
        try:
            if f in ('title', 'lat', 'pg', 'tag', 'why', 'q', 'fig'):
                if fix is None:
                    n.pop(f, None)
                else:
                    n[f] = fix
            elif m := re.fullmatch(r'sections/(\d+)/(\d+)', f):
                lst = n['sections'][int(m.group(1))]['items']
                j = int(m.group(2))
                if fix is None:
                    dels.append((lst, j, tag))
                else:
                    lst[j] = fix
            elif m := re.fullmatch(r'sections/(\d+)/k', f):
                n['sections'][int(m.group(1))]['k'] = fix
            elif m := re.fullmatch(r'l3/(\d+)/pg', f):
                n['l3'][int(m.group(1))]['pg'] = fix
            elif m := re.fullmatch(r'l3/(\d+)/k', f):
                n['l3'][int(m.group(1))]['k'] = fix
            elif m := re.fullmatch(r'l3/(\d+)', f):
                j = int(m.group(1))
                if fix is None:
                    dels.append((n['l3'], j, tag))
                else:
                    if isinstance(fix, dict):
                        n['l3'][j].update(fix)
                    else:
                        n['l3'][j]['t'] = fix
                    if iss.get('fix_pg'):
                        n['l3'][j]['pg'] = iss['fix_pg']
            elif m := re.fullmatch(r'labels/(\d+)', f):
                j = int(m.group(1))
                if fix is None:
                    dels.append((n['labels'], j, tag))
                else:
                    n['labels'][j] = fix
            else:
                print('?? nie rozumiem pola', tag, f); continue
            print('ok', tag, iss['card'][:30], f)
        except (IndexError, KeyError) as e:
            print('?? zły indeks', tag, iss['card'], f, e)
    for k, ms in enumerate(v.get('missing', [])):
        tag = f'{vid}:m{k}'
        if tag in skip:
            print('pominięte', tag); continue
        n = node(ms['card'])
        if n is None:
            print('?? brak węzła', tag, ms['card']); continue
        w = ms.get('where', 'l3').strip()
        if w.startswith('sections/'):
            i = int(w.split('/')[1])
            n['sections'][i]['items'].append(ms['text'] + (f' (s. {ms["pg"]})' if ms.get('pg') and False else ''))
        else:
            n.setdefault('l3', []).append({'k': ms.get('k') or 'SZCZEGÓŁY', 't': ms['text'], 'pg': ms.get('pg', '')})
        print('dodane', tag, ms['card'][:30], w)
# usuwanie od końca (żeby indeksy się nie przesunęły)
for lst, j, tag in sorted(dels, key=lambda x: (id(x[0]), -x[1])):
    print('usunięte', tag, '|', str(lst[j])[:90])
    del lst[j]
if not dry:
    json.dump(d, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('zapisane', P)
