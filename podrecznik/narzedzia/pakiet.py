#!/usr/bin/env python3
"""Pakiet wejściowy dla planisty (Fable) – jeden plik tekstowy na rozdział, bez LLM.

Zawartość: zagadnienia z rozpiski, mapa zakresu (handoff/ZNN.md), lista faktów T z wyciągu,
tekst rozdziału bez SVG/HTML (z id h2/h3), źródła przycięte do zakresu z mapy.
Użycie:  python3 narzedzia/pakiet.py 04 [05 ...]   ->  pakiety/z04.txt
"""
import re, sys, pathlib
from bs4 import BeautifulSoup, NavigableString

ROOT = pathlib.Path(__file__).resolve().parent.parent
SP = pathlib.Path('/tmp/claude-0/-home-user-first-thing/600b873f-e07d-5766-b2f4-6a90b68ae091/scratchpad')
ZR = SP / 'zrodla'
SYL = SP / 'dropbox' / 'syl'
DREWA = pathlib.Path('/root/.claude/uploads/600b873f-e07d-5766-b2f4-6a90b68ae091/b95214fd-Drewa_Genetyka_medyczna_OCR.txt')

# Zakres źródeł: (plik, wybór). wybór: None = cały plik; ('s', [(od, do), ...]) = strony [Strona N];
# ('l', [(od, do), ...]) = linie pliku (1-indeksowane, włącznie).
JORDE = ZR / 'z08' / 'jorde_r05_STARE_WYDANIE.txt'
ZAKRES = {
    '02': [(ZR/'z02'/'drewa_r07.txt', ('s', [(143, 151), (155, 162)])), (ZR/'z02'/'jozwiak_r06.txt', None)],
    '03': [(ZR/'z03'/'drewa_r08.txt', ('s', [(165, 174)])), (ZR/'z03'/'jozwiak_r11.txt', None), (ZR/'z03'/'alster_korwek_2014.txt', None)],
    '04': [(ZR/'z04'/'drewa_r03.txt', None), (ZR/'z04'/'drewa_r18.txt', None),
           (ZR/'z04'/'drewa_r27.txt', None), (ZR/'z04'/'ostrowska_r06.txt', None)],
    '05': [(ZR/'z05'/'drewa_r27.txt', None), (ZR/'z05'/'ostrowska_r06.txt', None)],
    '06': [(ZR/'z06'/'drewa_r27.txt', None), (ZR/'z06'/'drewa_r29.txt', None)],
    '07': [(ZR/'z07'/'jozwiak_r09.txt', None), (ZR/'z07'/'jozwiak_r10_ryc10.7_10.8.txt', None),
           (ZR/'z07'/'drewa_r26.txt', ('s', [(694, 698)])), (ZR/'z07'/'twyman_M3.txt', None)],
    '08': [(ZR/'z08'/'drewa_r02.txt', ('s', [(10, 24)])), (ZR/'z08'/'drewa_r16.txt', ('s', [(373, 382)])),
           (ZR/'z08'/'drewa_r10.txt', ('s', [(198, 199), (212, 212)])),
           (ZR/'z08'/'drewa_r12.txt', ('s', [(269, 275), (281, 291)])),
           (ZR/'z08'/'drewa_r13.txt', ('s', [(295, 306)])),
           (JORDE, ('l', [(429, 584)])), (ZR/'z08'/'material_pomocniczy_zaj8.txt', None)],
    '10': [(JORDE, ('l', [(11, 428)]))],   # + linie Drewy z mapy (automatycznie)
    '01': [(ROOT/'material'/'genomika.txt', None)],
}
OCR_Z_MAPY = {'09', '10', '11'}   # zakresy „l. A–B” Drewy OCR odczytywane z handoff/ZNN.md


def tekst_rozdzialu(nn):
    f = next((ROOT/'rozdzialy').glob(f'z{nn}-*.html'))
    soup = BeautifulSoup(f.read_text(encoding='utf-8'), 'html.parser')
    for s in soup.find_all('svg'):
        s.decompose()
    out = []

    def txt(el):
        return re.sub(r'\s+', ' ', el.get_text(' ', strip=True))

    def walk(el):
        for ch in el.children:
            if isinstance(ch, NavigableString):
                continue
            n, cls = ch.name, ch.get('class') or []
            if n in ('h2', 'h3', 'h4'):
                out.append(f"\n{'#' * int(n[1])} {txt(ch)}  [{ch.get('id', '')}]")
            elif n == 'figure':
                cap = ch.find('figcaption')
                out.append(f"[RYCINA {ch.get('id', '')} „{ch.get('data-title', '')}”: {txt(cap) if cap else ''}]")
            elif n == 'table':
                out.append('[TABELA]')
                for tr in ch.find_all('tr'):
                    out.append(' | '.join(txt(c) for c in tr.find_all(['th', 'td'])))
                out.append('[/TABELA]')
            elif n == 'aside':
                out.append(f"[POJĘCIE {ch.get('data-term', '')}] {txt(ch)}")
            elif n == 'div' and ('box' in cls or 'w60' in cls or 'przejscie' in cls):
                kind = [c for c in cls if c != 'box']
                out.append(f"[RAMKA {' '.join(kind)}] {txt(ch)}")
            elif n in ('ul', 'ol'):
                for li in ch.find_all('li', recursive=False):
                    out.append(f"- {txt(li)}")
            elif n == 'p':
                pre = '[ŹRÓDŁO] ' if 'src' in cls else ('[LEAD] ' if 'lead' in cls else '')
                out.append(pre + txt(ch))
            elif n in ('section', 'div'):
                walk(ch)
            else:
                out.append(txt(ch))

    sec = soup.find('section')
    out.insert(0, f"(plik rozdzialy/{f.name}; data-title: {sec.get('data-title', '')})")
    walk(sec)
    return '\n'.join(x for x in out if x.strip())


def przytnij(path, wybor):
    lines = path.read_text(encoding='utf-8', errors='replace').splitlines()
    if wybor is None:
        return '\n'.join(lines), 'cały plik'
    kind, zakresy = wybor
    if kind == 'l':
        part = []
        for a, b in zakresy:
            part.append(f'[linie {a}–{b}]')
            part.extend(lines[a - 1:b])
        return '\n'.join(part), 'linie ' + ', '.join(f'{a}–{b}' for a, b in zakresy)
    # strony: [Strona N] otwiera stronę N
    keep, cur, part = False, None, []
    for ln in lines:
        m = re.match(r'\s*\[Strona (\d+)\]', ln)
        if m:
            cur = int(m.group(1))
            keep = any(a <= cur <= b for a, b in zakresy)
        if keep:
            part.append(ln)
    return '\n'.join(part), 's. ' + ', '.join(f'{a}–{b}' if a != b else f'{a}' for a, b in zakresy)


def drewa_z_mapy(nn):
    mapa = (ROOT/'handoff'/f'Z{nn}.md').read_text(encoding='utf-8')
    zak = sorted({(int(a), int(b)) for a, b in re.findall(r'l\.\s*(\d{4,})[–-](\d{4,})', mapa)})
    return [(DREWA, ('l', zak))] if zak else []


def lista_T(nn):
    p = ROOT/'wyciagi'/f'{"g" if nn == "01" else "z" + nn}.md'
    if not p.exists():
        return '(brak wyciągu)'
    out = []
    for ln in p.read_text(encoding='utf-8').splitlines():
        if ln.startswith('#'):
            out.append(ln)
        elif re.match(r'\s*-\s*T\b', ln):
            out.append(ln)
    return '\n'.join(out)


def rozpiska(nn):
    for p in (ZR/f'z{nn}'/'ROZPISKA.txt', SYL/f'z{nn}.txt'):
        if p.exists():
            return p.read_text(encoding='utf-8', errors='replace')
    return '(brak rozpiski – G: źródłem jest prezentacja LMZ 3 i opracowanie material/genomika.txt)'


def zbuduj(nn):
    mapa = ROOT/'handoff'/('G.md' if nn == '01' else f'Z{nn}.md')
    zr = list(ZAKRES.get(nn, []))
    if nn in OCR_Z_MAPY:
        zr = drewa_z_mapy(nn) + zr
    parts = [f'# PAKIET PLANISTY – rozdział {"G" if nn == "01" else nn}',
             'Jedyny plik do przeczytania (poza handoffem C1, STYL.md i ZASADY.md). Sekcje: A rozpiska, B mapa zakresu, '
             'C fakty uciętych wcześniej (T z wyciągu), D tekst rozdziału (bez rycin SVG), E źródła przycięte do zakresu.',
             '\n\n======== A. ROZPISKA ZAJĘĆ ========\n', rozpiska(nn),
             '\n\n======== B. MAPA ZAKRESU (handoff) ========\n', mapa.read_text(encoding='utf-8'),
             '\n\n======== C. FAKTY UCIĘTE WCZEŚNIEJ (T z wyciągu) ========\n', lista_T(nn),
             '\n\n======== D. TEKST ROZDZIAŁU ========\n', tekst_rozdzialu(nn),
             '\n\n======== E. ŹRÓDŁA (przycięte do zakresu z mapy) ========\n']
    for path, wybor in zr:
        body, opis = przytnij(path, wybor)
        parts.append(f'\n---------- {path.name} ({opis}) ----------\n{body}')
    out = ROOT/'pakiety'/f'z{nn}.txt'
    out.parent.mkdir(exist_ok=True)
    out.write_text('\n'.join(parts), encoding='utf-8')
    return out


if __name__ == '__main__':
    for nn in sys.argv[1:]:
        p = zbuduj(nn.zfill(2))
        t = p.read_text(encoding='utf-8')
        sec = {k: len(v) for k, v in zip('ABCDE', re.split(r'\n======== [A-E]\. .*? ========\n', t)[1:])}
        print(f'{p.name}: {len(t):,} znaków (~{len(t)//3.6/1000:.0f} tys. tokenów)  sekcje: {sec}')
