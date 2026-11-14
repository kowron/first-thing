#!/usr/bin/env python3
"""Pomocnik builda (pypdf):
  pdftool.py dests IN.pdf                -> JSON {pages, dests: {id: [pageIndex, top]}}
  pdftool.py finalize IN.pdf OUT.pdf META.json -> metadane, zakładki, kontrola linków (JSON na stdout)
"""
import json
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
        out[norm(name)] = [idx, top]
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
        '/Creator': 'kolokwium6/build.mjs (Chromium)',
    })
    writer._root_object[NameObject('/Lang')] = TextStringObject('pl-PL')

    missing = []

    def add(item, parent=None):
        d = dests.get(item['id'])
        if not d:
            missing.append(item['id'])
            return None
        idx, top = d
        top = page_h if top is None else min(page_h, top + 18)
        return writer.add_outline_item(item['title'], idx, parent=parent, fit=Fit.xyz(left=0, top=top, zoom=None))

    for it in meta.get('outline', []):
        node = add(it)
        if node is not None:
            for ch in it.get('children', []) or []:
                add(ch, node)
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


if __name__ == '__main__':
    if len(sys.argv) >= 3 and sys.argv[1] == 'dests':
        cmd_dests(sys.argv[2])
    elif len(sys.argv) >= 5 and sys.argv[1] == 'finalize':
        cmd_finalize(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print(__doc__)
        sys.exit(2)
