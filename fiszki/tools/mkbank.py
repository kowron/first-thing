#!/usr/bin/env python3
"""Kompiluje bank pytań (pliki tekstowe) do bank.js."""
import sys, re, json, glob, html, unicodedata
src=sorted(glob.glob(sys.argv[1]+'/*.txt')); out=sys.argv[2]
blocks=[]; L=None; U=None; grp=None; errs=[]; seen_la={}; ids=set(); CUR_S=None
PTAG=re.compile(r'\s*\{(s\.[^{}]*|z zajęć[^{}]*|brak[^{}]*)\}\s*$')
def ptag(t):
    """oddziela końcowy znacznik stron {s. 718–719} -> (tekst, strony)"""
    m=PTAG.search(t)
    return (t[:m.start()],m.group(1).strip()) if m else (t,None)
def nla(s): return re.sub(r'\s+',' ',s.strip().lower())
def low1(s): return s[:1].lower()+s[1:]
def conv(s, lesson, collect=True):
    """[pl|la|baza] -> pl (<i>la</i>), _x_ -> <i>x</i>; zbiera słówka."""
    def rep(m):
        parts=[x.strip() for x in m.group(1).split('|')]
        if len(parts)<2: errs.append('zły znacznik: '+m.group(0)); return m.group(0)
        disp,la=parts[0],parts[1]; base=parts[2] if len(parts)>2 else low1(disp)
        k=nla(la)
        if collect:
            if k in seen_la:
                if seen_la[k][0]!=base: errs.append(f'łacina "{la}" ma dwie polskie nazwy: {seen_la[k][0]} / {base}')
            else:
                seen_la[k]=(base,lesson['id']); w={'pl':base,'la':la}
                if CUR_S: w['s']=CUR_S
                lesson['words'].append(w)
        return f'{html.escape(disp)} (<i>{html.escape(la)}</i>)'
    s2=re.sub(r'\[([^\[\]]+)\]',rep,s)
    s2=re.sub(r'(?<![\w])_([^_]+)_(?![\w])',lambda m:'<i>'+m.group(1)+'</i>',s2)
    return s2
for f in src:
    for ln,raw in enumerate(open(f,encoding='utf-8'),1):
        line=raw.rstrip('\n'); s=line.strip()
        if not s: continue
        where=f'{f.split("/")[-1]}:{ln}'
        if s.startswith('@B '):
            blocks.append({'t':s[3:].strip(),'lessons':[]}); L=U=None
        elif s.startswith('@L '):
            p=[x.strip() for x in s[3:].split('|')]
            if len(p)!=4: errs.append(where+' @L: 4 pola'); continue
            L={'id':p[0],'tis':p[1],'t':p[2],'d':p[3],'units':[],'words':[]}
            if L['id'] in ids: errs.append(where+' powtórzone id '+L['id'])
            ids.add(L['id']); blocks[-1]['lessons'].append(L); U=None
        elif s.startswith('@U '):
            p=[x.strip() for x in s[3:].split('|')]
            if len(p)!=3: errs.append(where+' @U: 3 pola'); continue
            U={'id':p[0],'pri':int(p[1]),'src':p[2],'q':'','pts':[],'fu':[]}
            if 'u:'+U['id'] in ids: errs.append(where+' powtórzone id '+U['id'])
            ids.add('u:'+U['id']); L['units'].append(U); grp=None
        elif s.startswith('Q: '): U['q']=s[3:].strip()
        elif s.startswith('H: '): grp=s[3:].strip()
        elif s.startswith('X: '): U['x']=conv(s[3:].strip(),L,False)
        elif s.startswith('F: '):
            if '=>' not in s: errs.append(where+' F bez =>'); continue
            q,a=s[3:].split('=>',1); a,pg=ptag(a.strip()); f_={'q':q.strip(),'a':conv(a.strip(),L,False)}
            if pg: f_['s']=pg
            U['fu'].append(f_)
        elif s.startswith('- '):
            if ' ?? ' not in s: errs.append(where+' punkt bez pytania'); continue
            a,c=s[2:].split(' ?? ',1); c,pg=ptag(c.strip()); c=c.strip()
            if not c.endswith(('?','.')): errs.append(where+' pytanie bez znaku: '+c)
            CUR_S=pg; pt={'a':conv(a.strip(),L),'c':c}; CUR_S=None
            if pg: pt['s']=pg
            if grp: pt['g']=grp; grp=None
            U['pts'].append(pt)
        else: errs.append(where+' nieznana linia: '+s[:60])
# kontrole
nu=npt=nf=nw=0; nopg=[]
for b in blocks:
    for l in b['lessons']:
        nw+=len(l['words'])
        for u in l['units']:
            nu+=1; npt+=len(u['pts']); nf+=len(u['fu'])
            nos=[i for i,p in enumerate(u['pts']) if 's' not in p]+[('F',i) for i,f in enumerate(u['fu']) if 's' not in f]
            if nos: nopg.append((u['id'],nos))
            if not u['q']: errs.append('brak Q w '+u['id'])
            if len(u['pts'])<3: errs.append('mało punktów w '+u['id'])
            cs=[p['c'] for p in u['pts']]
            if len(set(cs))!=len(cs): errs.append('powtórzone pytanie fiszki w '+u['id'])
allc={}
for b in blocks:
    for l in b['lessons']:
        for u in l['units']:
            for p in u['pts']:
                if p['c'] in allc: errs.append('to samo pytanie fiszki w '+u['id']+' i '+allc[p['c']])
                allc[p['c']]=u['id']
if errs:
    print('BŁĘDY:'); [print(' ',e) for e in errs]; sys.exit(1)
js='window.BANK='+json.dumps({'blocks':blocks},ensure_ascii=False,separators=(',',':'))+';\n'
open(out,'w',encoding='utf-8').write(js)
if nopg: print('UWAGA – bez stron Bochenka:', sum(len(x[1]) for x in nopg), 'pozycji w', len(nopg), 'pytaniach')
print(f'bloki {len(blocks)}, lekcje {sum(len(b["lessons"]) for b in blocks)}, pytania {nu}, punkty {npt}, dopytania {nf}, słówka {nw}, {len(js)//1024} KB')
for b in blocks:
    for l in b['lessons']:
        print(f'  {l["id"]:24} pytań {len(l["units"]):2}  punktów {sum(len(u["pts"]) for u in l["units"]):3}  dopytań {sum(len(u["fu"]) for u in l["units"]):2}  słówek {len(l["words"]):2}')
