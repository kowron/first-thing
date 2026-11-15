#!/usr/bin/env python3
"""Dokłada do podzbiorów Inter (fonts/Inter-*.woff2) glify, których nie ma w Inter
ani w Source Serif 4, kopiując je z DejaVu Sans (licencja Bitstream Vera / DejaVu
pozwala na modyfikację i osadzanie). Dzięki temu w PDF nie pojawia się czcionka
zastępcza (DejaVuSans) z innymi proporcjami.

Obecnie: U+221D ∝ (proporcjonalny do). Glif jest skalowany tak, by miał wysokość
i położenie Interowego ∞ (U+221E) z tego samego pliku, szerokość jak inne znaki
matematyczne Inter (=, +), a w odmianach pochyłych – pochylony jak Inter Italic.

  PYTHONPATH=<katalog z fontTools i brotli> python3 lib/fontpatch.py   # z katalogu projektu
Skrypt jest idempotentny (pomija pliki, które mają już dany znak).
"""
import os
import sys

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEJAVU = {'book': '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
          'bold': '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'}
TARGETS = {  # plik Inter -> (wariant DejaVu, pochylenie)
    'Inter-Regular.woff2': ('book', False), 'Inter-Italic.woff2': ('book', True),
    'Inter-Medium.woff2': ('book', False), 'Inter-MediumItalic.woff2': ('book', True),
    'Inter-SemiBold.woff2': ('bold', False), 'Inter-SemiBoldItalic.woff2': ('bold', True),
    'Inter-Bold.woff2': ('bold', False), 'Inter-BoldItalic.woff2': ('bold', True),
}
CHARS = [0x221D]
REF = 0x221E          # ∞ – wzorzec wysokości i linii osi
SLANT = 0.166         # tg kąta pochylenia Inter Italic (ok. 9,4°)


def bounds(font, cp):
    gs = font.getGlyphSet()
    bp = BoundsPen(gs)
    gs[font.getBestCmap()[cp]].draw(bp)
    return bp.bounds


def patch(path, src_path, italic):
    font = TTFont(path)
    cmap = font.getBestCmap()
    todo = [cp for cp in CHARS if cp not in cmap]
    if not todo:
        print(f'{os.path.basename(path)}: bez zmian')
        return
    src = TTFont(src_path)
    sgs = src.getGlyphSet()
    ib, sb = bounds(font, REF), bounds(src, REF)
    scale = (ib[3] - ib[1]) / (sb[3] - sb[1])
    ty = ib[1] - sb[1] * scale
    mid = (ib[1] + ib[3]) / 2
    ref_adv = font['hmtx'][cmap[ord('=')]][0]
    for cp in todo:
        gname = src.getBestCmap()[cp]
        b = BoundsPen(sgs)
        sgs[gname].draw(b)
        x0, _, x1, _ = b.bounds
        w = (x1 - x0) * scale
        adv = max(ref_adv, round(w + 2 * 140))
        tx = (adv - w) / 2 - x0 * scale
        # x' = s*x + k*s*y + (tx - k*mid) ; y' = s*y + ty  (pochylenie wokół osi znaku)
        k = SLANT if italic else 0.0
        tpen = TTGlyphPen(None)
        sgs[gname].draw(TransformPen(tpen, (scale, 0, k * scale, scale, tx + k * (ty - mid), ty)))
        glyph = tpen.glyph()
        name = f'uni{cp:04X}'
        order = font.getGlyphOrder()
        if name in order:
            name += '.k6'
        font['glyf'].glyphs[name] = glyph
        font.setGlyphOrder(order + [name])
        glyph.recalcBounds(font['glyf'])
        font['hmtx'].metrics[name] = (adv, glyph.xMin if hasattr(glyph, 'xMin') else 0)
        for t in font['cmap'].tables:
            if t.isUnicode():
                t.cmap[cp] = name
        print(f'{os.path.basename(path)}: + U+{cp:04X} z {os.path.basename(src_path)} (skala {scale:.3f}, szer. {adv})')
    font['maxp'].numGlyphs = len(font.getGlyphOrder())
    font.flavor = 'woff2'
    font.save(path)


if __name__ == '__main__':
    for fn, (variant, italic) in TARGETS.items():
        p = os.path.join(ROOT, 'fonts', fn)
        if not os.path.exists(p):
            print(f'brak {p}', file=sys.stderr)
            continue
        patch(p, DEJAVU[variant], italic)
