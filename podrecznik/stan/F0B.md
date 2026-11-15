# Stan F0B (szablon + bank rycin k4/k5/g)

## Krok 0 – start (2026-11-15)
- Przeczytano handoff F0B, ZASADY.md, PLAN.md. Brak wcześniejszego stanu.
- Następny krok: kopia systemu składu z kolokwium6/ do podrecznik/.

## Krok 1 – kopia systemu + teksty + wycinanie rycin
- Skopiowano build.mjs, book.json, lib/, css/, fonts/, front/ z kolokwium6 do podrecznik/ (jeszcze bez zmian).
- material/k4.txt, k5.txt, genomika.txt (pdftotext -layout, znaczniki „[Strona N]”).
- lib/bank_pdf.py: wycinanie wektorowe (pypdf CropBox + pdftocairo -svg); ręczne ramki w bank-rycin/ramki.json.
  Uruchom: python3 lib/bank_pdf.py k5 <pdf> <scratch>/bank/k5  (dane do INDEX w <scratch>/bank/<prefiks>.json)
- Następny krok: arkusz podglądu (lib/bank_arkusz.mjs), kontrola wzrokowa, INDEX.md.
