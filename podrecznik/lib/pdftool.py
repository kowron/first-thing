#!/usr/bin/env python3
"""Pomocnik builda (pypdf):
  pdftool.py dests IN.pdf                -> JSON {pages, dests: {id: [pageIndex, top, left]}}
                                            top/left (pt) jak w PDF Chromium: względem pola zadruku,
                                            nie strony – lewy górny róg pola = [wysokość strony, 0]
  pdftool.py finalize IN.pdf OUT.pdf META.json -> metadane, zakładki, kontrola linków (JSON na stdout)
  pdftool.py linediff A.pdf B.pdf        -> JSON {pages, diffs: [{page, a: [fragmenty], b: [fragmenty]}]}
                                            porównanie wierszy (pdftotext -layout) po usunięciu U+00AD,
                                            z dywizami U+2010/U+002D traktowanymi jednakowo
  pdftool.py fontchars IN.pdf WZORZEC     -> JSON [{font, char, pages}] – znaki złożone czcionką,
                                            której nazwa zawiera WZORZEC (np. DejaVu); wymaga pdfminer.six
"""
import difflib
import json
import re
import subprocess
import sys

from pypdf import PdfReader, PdfWriter
from pypdf.generic import Fit, NameObject, TextStringObject


def norm(name):
    name = str(name)
    return name[1:] if name.startswith('/') else name


def read_dests(reader):
    out = {}
    for name, d in reader.named_destinations.items():
        try:
            idx = reader.get_destination_page_number(d)
        except Exception:
            continue
        top = d.get('/Top')
        try:
            top = float(top) if top is not None else None
        except Exception:
            top = None
        try:
            left = float(d.get('/Left')) if d.get('/Left') is not None else None
        except Exception:
            left = None
        out[norm(name)] = [idx, top, left]
    return out


def cmd_dests(path):
    r = PdfReader(path)
    print(json.dumps({'pages': len(r.pages), 'dests': read_dests(r)}))


def cmd_finalize(src, dst, meta_path):
    with open(meta_path, encoding='utf-8') as fh:
        meta = json.load(fh)
    reader = PdfReader(src)
    dests = read_dests(reader)
    writer = PdfWriter(clone_from=reader)
    page_h = float(reader.pages[0].mediabox.height) if reader.pages else 842.0

    writer.add_metadata({
        '/Title': meta.get('title', ''),
        '/Author': meta.get('author', ''),
        '/Subject': meta.get('subject', ''),
        '/Keywords': meta.get('keywords', ''),
        '/Creator': 'podrecznik/build.mjs (Chromium)',
    })
    writer._root_object[NameObject('/Lang')] = TextStringObject('pl-PL')

    missing = []

    def add(item, parent=None):
        d = dests.get(item['id'])
        if not d:
            missing.append(item['id'])
            return None
        idx, top = d[0], d[1]
        top = page_h if top is None else min(page_h, top + 18)
        return writer.add_outline_item(item['title'], idx, parent=parent, fit=Fit.xyz(left=0, top=top, zoom=None))

    def add_tree(item, parent=None):
        # rozdział -> podrozdziały -> (część 2 ->) podrozdziały części 2
        node = add(item, parent)
        if node is not None:
            for ch in item.get('children', []) or []:
                add_tree(ch, node)

    for it in meta.get('outline', []):
        add_tree(it)
    if meta.get('outline'):
        writer.page_mode = '/UseOutlines'

    links_total, broken = 0, []
    for pi, page in enumerate(writer.pages):
        for a in page.get('/Annots') or []:
            a = a.get_object()
            if a.get('/Subtype') != '/Link':
                continue
            links_total += 1
            dest = a.get('/Dest')
            if dest is None and a.get('/A') is not None:
                act = a['/A'].get_object()
                if act.get('/S') == '/URI':
                    continue
                dest = act.get('/D')
            if dest is None:
                continue
            if isinstance(dest, (list, tuple)):
                continue
            if norm(dest) not in dests:
                broken.append({'page': pi + 1, 'dest': norm(dest)})

    with open(dst, 'wb') as fh:
        writer.write(fh)
    print(json.dumps({'links': links_total, 'broken': broken, 'outline_missing': missing, 'pages': len(reader.pages)}))


def _layout_pages(path):
    out = subprocess.run(['pdftotext', '-layout', path, '-'], capture_output=True, text=True, check=True).stdout
    pages = out.split('\f')
    if pages and not pages[-1].strip():
        pages.pop()
    return pages


def _norm_line(line):
    line = line.replace('\u00ad', '').replace('\u2010', '-')
    return line


def cmd_linediff(a_path, b_path):
    a, b = _layout_pages(a_path), _layout_pages(b_path)
    diffs = []
    for i in range(max(len(a), len(b))):
        la = [_norm_line(l) for l in (a[i] if i < len(a) else '').split('\n') if l.strip()]
        lb = [_norm_line(l) for l in (b[i] if i < len(b) else '').split('\n') if l.strip()]
        # bez odstępów: pdftotext różnie rozstawia spacje w tekście ze spacjowaniem liter
        ka = [re.sub(r'\s+', '', l) for l in la]
        kb = [re.sub(r'\s+', '', l) for l in lb]
        if ka == kb:
            continue
        sm = difflib.SequenceMatcher(a=ka, b=kb, autojunk=False)
        da, db = [], []
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal':
                continue
            da += la[i1:i2]
            db += lb[j1:j2]
        seg = lambda ls: [re.sub(r'\s+', ' ', s).strip() for l in ls for s in re.split(r'\s{3,}', l.strip()) if s.strip()]
        diffs.append({'page': i + 1, 'a': seg(da), 'b': seg(db)})
    print(json.dumps({'pages': [len(a), len(b)], 'diffs': diffs}, ensure_ascii=False))


def cmd_fontchars(path, pattern):
    from pdfminer.high_level import extract_pages
    from pdfminer.layout import LTChar
    found = {}

    def walk(o, pno):
        if isinstance(o, LTChar):
            if pattern in o.fontname:
                key = (o.fontname.split('+')[-1], o.get_text())
                found.setdefault(key, set()).add(pno)
            return
        if hasattr(o, '__iter__'):
            for c in o:
                walk(c, pno)

    from pypdf import PdfReader
    n = len(PdfReader(path).pages)
    # najpierw szybko: na których stronach w ogóle jest ta czcionka
    pages = [p for p in range(1, n + 1)
             if pattern in subprocess.run(['pdffonts', '-f', str(p), '-l', str(p), path], capture_output=True, text=True).stdout]
    for pno in pages:
        for page in extract_pages(path, page_numbers=[pno - 1]):
            walk(page, pno)
    print(json.dumps([{'font': f, 'char': c, 'pages': sorted(p)} for (f, c), p in sorted(found.items())], ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) >= 3 and sys.argv[1] == 'dests':
        cmd_dests(sys.argv[2])
    elif len(sys.argv) >= 5 and sys.argv[1] == 'finalize':
        cmd_finalize(sys.argv[2], sys.argv[3], sys.argv[4])
    elif len(sys.argv) >= 4 and sys.argv[1] == 'linediff':
        cmd_linediff(sys.argv[2], sys.argv[3])
    elif len(sys.argv) >= 4 and sys.argv[1] == 'fontchars':
        cmd_fontchars(sys.argv[2], sys.argv[3])
    else:
        print(__doc__)
        sys.exit(2)
