#!/usr/bin/env python3
"""Bank rycin: wektorowe wycinanie rycin z gotowych opracowań PDF (k4, k5, genomika).

  python3 lib/bank_pdf.py <prefiks> <plik.pdf> <tmp-dir>   -> bank-rycin/<prefiks>-ryc-NN.svg + <tmp-dir>/<prefiks>.json

Położenie ryciny: etykieta „RYC. N” (pdftotext -bbox-layout) -> od dołu etykiety do pierwszego wiersza
tekstu przy lewym marginesie (podpis); w tym pasie ramka = obszar „atramentu” (render 100 dpi) + 3 pt.
Ręczne poprawki ramek: bank-rycin/ramki.json  {"k5-ryc-04": [x0, y0, x1, y1]}  (pt, od lewego górnego rogu).
Wycinanie: strona -> jednostronicowy PDF z CropBox -> pdftocairo -svg -cropbox (tekst jako krzywe).
"""
import json, os, re, subprocess, sys, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANK = os.path.join(ROOT, 'bank-rycin')
DPI = 100
K = DPI / 72.0
MARGIN_X = 50.0       # tekst zaczynający się przy lewym marginesie (44 pt) = podpis / tekst główny
PAD = 3.0


def lines_by_page(pdf):
    out = subprocess.run(['pdftotext', '-bbox-layout', pdf, '-'], capture_output=True, text=True).stdout
    pages = []
    for pm in re.finditer(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', out, re.S):
        ls = []
        for bm in re.finditer(r'<block [^>]*>(.*?)</block>', pm.group(3), re.S):
            blk = []
            for m in re.finditer(r'<line xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</line>', bm.group(1), re.S):
                words = [html.unescape(w) for w in re.findall(r'>([^<]*)</word>', m.group(5))]
                blk.append(dict(x0=float(m.group(1)), y0=float(m.group(2)), x1=float(m.group(3)), y1=float(m.group(4)), t=' '.join(words)))
            for l in blk:
                l['blk'] = blk
            ls += blk
        pages.append(dict(w=float(pm.group(1)), h=float(pm.group(2)), lines=ls))
    return pages


def read_pgm(path):
    b = open(path, 'rb').read()
    parts = b.split(maxsplit=4)
    w, h = int(parts[1]), int(parts[2])
    return w, h, parts[4][-w * h:]


def render(pdf, pno, tmp):
    base = os.path.join(tmp, f'r{pno}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-gray', '-f', str(pno), '-l', str(pno), '-singlefile', pdf, base], check=True)
    return read_pgm(base + '.pgm')


def ink_box(img, y0, y1, x0=30.0, x1=565.0, thr=245):
    w, h, d = img
    Y0, Y1, X0, X1 = int(y0 * K), min(h, int(y1 * K)), int(x0 * K), min(w, int(x1 * K))
    rows = []
    for y in range(Y0, Y1):
        row = d[y * w + X0:y * w + X1]
        ink = [i for i, v in enumerate(row) if v < thr]
        rows.append((y, ink[0] + X0, ink[-1] + X0) if ink else None)
    # pomiń cienką kreskę pod etykietą (genomika): pierwsza grupa wierszy <= 3 px na prawie całą szerokość
    i = 0
    while i < len(rows) and rows[i] is None:
        i += 1
    j = i
    while j < len(rows) and rows[j] is not None:
        j += 1
    if i < len(rows) and j - i <= 3 and all(r and (r[2] - r[1]) > 0.7 * (X1 - X0) for r in rows[i:j]):
        rows = rows[j:]
    rr = [r for r in rows if r]
    if not rr:
        return None
    return (min(r[1] for r in rr) / K, rr[0][0] / K, (max(r[2] for r in rr) + 1) / K, (rr[-1][0] + 1) / K)


def main():
    prefix, pdf, tmp = sys.argv[1], sys.argv[2], sys.argv[3]
    os.makedirs(tmp, exist_ok=True)
    manual = {}
    mf = os.path.join(BANK, 'ramki.json')
    if os.path.exists(mf):
        manual = json.load(open(mf))
    pages = lines_by_page(pdf)
    figs = []
    for pi, pg in enumerate(pages):
        pno = pi + 1
        for l in pg['lines']:
            m = re.match(r'^RYC\s*\.\s*([\d ]+)$', l['t'].strip())
            if not m or l['x0'] > MARGIN_X:
                continue
            n = int(m.group(1).replace(' ', ''))
            fid = f'{prefix}-ryc-{n:02d}'
            # tytuł: wiersze na tej samej wysokości, na prawo od „RYC. N”, bez „RYCINA Z WERSJI…”
            same = [o for o in pg['lines'] if o is not l and o['y0'] < l['y1'] and o['y1'] > l['y0'] and o['x0'] > l['x1'] - 1 and o['x0'] < 400]
            title = ' '.join(o['t'] for o in sorted(same, key=lambda o: o['x0'])).strip()
            lab_bot = max([l['y1']] + [o['y1'] for o in same]) + 1.5
            below = sorted([o for o in pg['lines'] if o['y0'] > lab_bot + 4 and o['x0'] < MARGIN_X and len(o['t']) > 3], key=lambda o: o['y0'])
            cap = below[0] if below else None
            cap_top = (cap['y0'] - 1.5) if cap else pg['h'] - 60
            img = render(pdf, pno, tmp)
            box = ink_box(img, lab_bot, cap_top)
            if not box:
                print(f'{fid}: brak atramentu', file=sys.stderr)
                continue
            x0, y0, x1, y1 = box
            x0, y0, x1, y1 = max(0, x0 - PAD), max(lab_bot, y0 - PAD), min(pg['w'], x1 + PAD), min(cap_top, y1 + PAD)
            if fid in manual:
                x0, y0, x1, y1 = manual[fid]
            caption = ''
            if cap:
                # kolejne wiersze podpisu przy lewym marginesie, odstęp między wierszami < 6 pt
                rest = sorted([o for o in pg['lines'] if o['y0'] >= cap['y0'] - 1 and o['x0'] < MARGIN_X], key=lambda o: o['y0'])
                blk = [rest[0]]
                for o in rest[1:]:
                    if o['y0'] - blk[-1]['y1'] > 6:
                        break
                    blk.append(o)
                caption = re.sub(r'\s+', ' ', ' '.join(o['t'] for o in blk)).replace('‐ ', '').strip()
            figs.append(dict(id=fid, n=n, title=title, page=pno, box=[round(v, 1) for v in (x0, y0, x1, y1)],
                             w_mm=round((x1 - x0) / 72 * 25.4), h_mm=round((y1 - y0) / 72 * 25.4), caption=caption))
            cut(pdf, pno, (x0, y0, x1, y1), pg['h'], os.path.join(BANK, fid + '.svg'), tmp)
            print(f'{fid}  s.{pno}  {figs[-1]["w_mm"]}×{figs[-1]["h_mm"]} mm  {title}')
    json.dump(figs, open(os.path.join(tmp, prefix + '.json'), 'w'), ensure_ascii=False, indent=1)


def cut(pdf, pno, box, ph, out, tmp):
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import RectangleObject
    x0, y0, x1, y1 = box
    r = PdfReader(pdf)
    w = PdfWriter()
    p = w.add_page(r.pages[pno - 1])
    rect = RectangleObject([x0, ph - y1, x1, ph - y0])
    p.cropbox = rect
    p.mediabox = rect
    one = os.path.join(tmp, 'one.pdf')
    with open(one, 'wb') as f:
        w.write(f)
    subprocess.run(['pdftocairo', '-svg', one, out], check=True)
    s = open(out, encoding='utf-8').read()
    s = re.sub(r'(\d+\.\d\d)\d+', r'\1', s)                       # mniejszy plik: 0,01 pt wystarczy
    s = re.sub(r'<\?xml[^>]*>\s*', '', s)
    open(out, 'w', encoding='utf-8').write(s)


if __name__ == '__main__':
    main()
