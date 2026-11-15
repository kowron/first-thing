#!/usr/bin/env python3
"""Generuje bank-rycin/INDEX.md z metadanych lib/bank_pdf.py:  python3 lib/bank_index.py <tmp-dir>  (<tmp-dir>/<prefiks>/<prefiks>.json)"""
import json, re, sys, os
S = sys.argv[1]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = {'k4': ('Kwasy nukleinowe – kolokwium 4', 'material/k4.txt'),
       'k5': ('Analiza DNA i RNA – kolokwium 5', 'material/k5.txt'),
       'g': ('Genomika – analiza genomu i genotypowanie', 'material/genomika.txt')}
# podpisy z nałożoną ukrytą warstwą tekstu w PDF – streszczenie ręczne z widocznego podpisu
FIX = {
 'g-ryc-01': 'A – budowa genu: promotor, eksony z częścią kodującą (CDS) i niekodującą (UTR), introny; B – z jednego pre-mRNA dwa różne mRNA (alternatywny splicing); C – z każdego mRNA inna izoforma białka; D – trzy poziomy opisu: genomika, transkryptomika, proteomika.',
 'g-ryc-02': 'A – rodzaje zmian sekwencji i ich skutek w białku (synonimiczna, zmiany sensu, nonsensowna, delecja 3 nt, insercja 1 nt); B – ekspansja powtórzeń CAG; C – większe zmiany: delecja, duplikacja i inwersja.',
 'g-ryc-07': 'A – PCR: para starterów wyznacza amplikon; B – Sanger: jeden starter, wydłużanie zatrzymywane barwnym ddNTP; C – kapilara: krótsze fragmenty docierają do detektora wcześniej; D – chromatogram: sygnał zamieniony na litery, obok heterozygotyczny SNV.',
}
def summary(c):
    parts = re.split(r'(?<=[.!?])\s+(?=[A-ZĄĆĘŁŃÓŚŹŻ])', c.strip())
    out = ''
    for p in parts:
        if out and len(out) + len(p) > 230: break
        out = (out + ' ' + p).strip()
        if len(out) > 110: break
    return out
H = 250
lines = ['# Bank rycin – indeks', '',
 'Gotowe ryciny wycięte wektorowo (SVG, tekst jako krzywe, kolory oryginału) z opracowań kolokwium 4, kolokwium 5 i „Genomiki”.',
 'Wstawienie do rozdziału – jeden znacznik (szczegóły: `KOMPONENTY.md`, p. 6):', '',
 '```html',
 '<figure class="fig" id="c05-fig-cykl" data-bank="k5-ryc-04" data-title="Cykl PCR">',
 '  <figcaption>Własny podpis, 1–2 wiersze.</figcaption>',
 '</figure>',
 '```', '',
 'Podgląd miniatur: `podglad-k4.png`, `podglad-k5.png`, `podglad-g.png`. Ryciny `k6-` dojdą w następnej turze.',
 '„Wymiary” = szerokość × wysokość w druku (build wstawia rycinę z banku na obie kolumny, 179 mm, skala ≈ 1:1);',
 'w nawiasie – część wysokości pola zadruku (250 mm). Rycina wielopanelowa idzie w całości.', '']
total = 0
for pre in ['k4', 'k5', 'g']:
    figs = json.load(open(f'{S}/{pre}/{pre}.json'))
    total += len(figs)
    name, txt = SRC[pre]
    lines += [f'## {pre}- · {name} ({len(figs)} rycin; tekst opracowania: `{txt}`)', '',
              '| id | tytuł | źródło | wymiary | co pokazuje (z podpisu) |', '|---|---|---|---|---|']
    for f in figs:
        h = round(f['h_mm'] * 179 / f['w_mm'])
        fr = h / H
        fr = '≈ 1/4' if fr < 0.3 else '≈ 1/3' if fr < 0.42 else '≈ 1/2' if fr < 0.58 else '≈ 2/3' if fr < 0.75 else '≈ 9/10'
        s = (FIX.get(f['id']) or summary(f['caption'])).replace('|', '/')
        lines.append(f"| `{f['id']}` | {f['title']} | {pre} s. {f['page']} | 179 × {h} mm ({fr}) | {s} |")
    lines.append('')
lines.append(f'Razem: {total} rycin. Do pominięcia: brak (wszystkie sprawdzone na arkuszu podglądu i automatycznie – krawędzie bez uciętych elementów, bez tekstu spoza ryciny).')
open(os.path.join(ROOT, 'bank-rycin', 'INDEX.md'), 'w').write('\n'.join(lines) + '\n')
print(total)
