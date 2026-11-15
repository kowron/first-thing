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

## Krok 2 – bank rycin k4/k5/g GOTOWY
- 67 SVG w bank-rycin/ (k4 18, k5 26, g 23), ok. 11 MB; podglad-k4/k5/g.png (lib/bank_arkusz.mjs).
- Kontrola: arkusze obejrzane; automat (scratch/bank/check_edges.py) – brak atramentu przy krawędziach i 4 pt na zewnątrz ramek. Do pominięcia: brak.
- INDEX.md generuje lib/bank_index.py <scratch>/bank (podpisy g-01/02/07 streszczone ręcznie – ukryta warstwa tekstu w PDF).
- Uwaga: material/genomika.txt ma miejscami nałożony ukryty tekst (np. „Źródła: [1] [2]” w podpisach).
- Następny krok: szablon dwukolumnowy (CSS + build: data-bank, zNN, --only).

## Krok 3 – szablon (w toku)
- css/style.css: paleta zielona (nazwy --navy/--teal zostały: ciemna zieleń/zieleń akcentu), section.chapter {columns:2},
  column-span:all dla .opener/figure.fig/.wide/tbl.wide/.w60; „Pojęcie” = ramka w kolumnie; pismo 9,4/13 pt; usunięte quiz/klucz/liceum/poza.
- lib/browser.js: NOTE_KINDS=[pojecie], BOX_KINDS=[zapamietaj, uwaga], bez quizów i klucza; data-label (np. „G”) na otwarciu/spisie/paginie; kontrola szerokości kolumny.
- build.mjs: rozdzialy/zNN-*.html, --only NN, data-bank -> <img class="bank" src="bank-rycin/ID.svg">, PODR_BUILD_DIR; book.json buildDir = scratchpad/build-podrecznik.
- front/cover.html, front/howto.html – zaślepki zielone.
- Następny krok: rozdzialy/z00-demo.html (2 strony), build --only 00 --png, kontrola łamania, KOMPONENTY.md.

## Krok 4 – łamanie dwukolumnowe DZIAŁA
- Jeden kontener multicol na rozdział + column-span: Chromium nie wyrównywał kolumn po przejściu strony.
  Rozwiązanie: browser.js owija ciągi elementów między elementami „na obie kolumny” w <div class="cols">;
  po 1. przebiegu splitCols() dzieli .cols na czystych przejściach stron (pdftool dests ma teraz [strona, top, left]).
- Demo rozdzialy/z00-demo.html = 2 strony (rycina z banku k5-ryc-03 w środku s. 1, tabela wide w środku s. 2, tabela w kolumnie,
  Pojęcie, Zapamiętaj, Uwaga, W 60 sekund). Test 5-stronicowy (3× demo, 3 ryciny z banku) – bez białych dziur; plik testowy usunięty.
- Gęstość: s. 2 demo ≈ 3850 znaków przy ~22% strony zajętej tabelą -> ok. 5000 znaków na stronę samego tekstu (9,4/13 pt).
- Następny krok: sprawdzić, czy SVG z banku drukuje się wektorowo; --demo (okładka, spis); KOMPONENTY.md.

## Krok 5 – ZAKOŃCZONE (tura 1: szablon + bank k4/k5/g)
- KOMPONENTY.md (nowy, krótki). Genomika: rozdzialy/z01-genomika.html, data-num="01", data-label="G", build --only 01 (sprawdzone na pliku testowym, usuniętym).
- Rycina z banku drukuje się wektorowo (pdfimages: brak obrazów rastrowych); maski cairo zamienione na opacity (lib/bank_pdf.py).
- Polecenia: node build.mjs --only NN --png | --demo | (pełny). Build: scratchpad/build-podrecznik/rozdzial-NN.pdf.
- Tura 2 (do zrobienia): bank k6- (inline SVG z kolokwium6/chapters + git show c3e7824^:…), dopisać do INDEX.md
  (lib/bank_index.py obsługuje tylko k4/k5/g – dopisać sekcję k6 ręcznie albo rozszerzyć skrypt).
- Ograniczenia: ryciny z banku zawsze na obie kolumny w skali ≈ 1:1 (g-ryc-01/02/07 ≈ 9/10 strony); zostają w kolorach
  oryginału (granat/turkus); okładka i „Jak korzystać” to zaślepki do fazy 5.
