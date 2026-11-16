# Stan F0A – przygotowanie źródeł

## Tura 1 (z02–z05, bez OCR) – 2026-11-15
Paczki w scratchpadzie: `zrodla/z02` … `zrodla/z05` + `zrodla/INDEX.md` (teksty nie są commitowane). Skrypty: `scratchpad/scripts/build.py`, `joz_cols.py`, `gen_spis.py`.
- Drewa (gotowy OCR txt): r. 7 i r. 8 w całości; r. 3 s. 28–34, 37–45, 48–55; r. 18 s. 431–432; r. 27 s. 710–712 (z04) oraz 703–705, 725, 732–735 (z05) – OK.
- Jóźwiak (warstwa OCR PDF): tekst złożony łamami ze współrzędnych słów (pdftotext -bbox), podpisy rycin/tabele wyjęte na koniec strony; numeracja książki odtworzona (PDF−11 do s. 117, PDF−10 od s. 119). Zakres wg koordynatora: r. 6 s. 68–75 („Punkty kontrolne…” → przed „Leki przeciwnowotworowe”), r. 11 s. 126–127 („Znaczenie apoptozy…” → przed „Podsumowaniem”); reszta rozdziałów w `*_reszta.txt` – OK.
- Alster–Korwek (pdftotext, s. 138–146) – OK.
- Ostrowska r. 6 (PDF 1–12 = s. 53–64) – BRAK s. 56 i 59 (strony odwrócone w skanie, OCR = szum) → do OCR w turze 2.
- Pozostaje (tura 2): OCR Drewa r. 2, 10, 12, 13, 16, Jorde r. 5, Twyman M3, Ostrowska s. 56/59; paczki z06–z11.

## Tura 2 (OCR + z06–z08) – 2026-11-16
- tesseract 5.3.4 + pol + eng zainstalowany przez apt (działa; po restarcie kontenera trzeba zainstalować ponownie).
