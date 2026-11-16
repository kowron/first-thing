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

## Krok 6 – naprawa splitCols (prawie puste strony z 1–3 osieroconymi wierszami) – 2026-11-16
- Zgłoszenie: autorzy Z02, Z03, Z04 (stan/z02.md, z03.md, z04.md). Diagnoza potwierdzona: Chromium zapisuje cele PDF (dests)
  względem POLA ZADRUKU – lewy górny róg pola = [841,9; 0] (lewa kolumna left = 0, prawa 262,5), a próg w splitCols był w układzie
  strony (TOP = 841,89 − 22 mm = 779,5). Za „czyste przejście strony” uchodził każdy element startujący ≤ 65 pt (5 wierszy) pod górą
  lewej kolumny -> .cols-page (break-before: page) -> końcówka poprzedniego akapitu sama na stronie (UWAGA „zapełniona w 3%”).
  Pomiar (przebieg 1): prawdziwe przejścia mają dy = 0 (Chromium obcina margines na przejściu), fałszywe dy ≥ 1 wiersz.
- Poprawka: lib/browser.js, splitCols – punkt odniesienia = cel samego rozdziału (section.chapter zaczyna stronę, więc to lewy górny
  róg pola zadruku; niezależne od marginesów @page i od tego, czy Chromium kiedyś zmieni układ); podział tylko gdy
  dy ≤ margin-top elementu + 3 pt i dx ≤ 20 pt. lib/pdftool.py – tylko opis formatu dests ([strona, top, left], układ pola zadruku).
- build.mjs, inkCheck: kontrola już była (strona w środku sekcji zapełniona < 35% -> UWAGA; na wariantach z błędem zgłaszała każdą
  osieroconą stronę). Dodane tylko trafniejsze wyjaśnienie dla < 20%: „prawie pusta strona w środku rozdziału – zwykle 1–3 wiersze
  osierocone przez łamanie…” (początek komunikatu „zapełniona tylko w N%” bez zmian – skrypty autorów dalej go znajdą).
- Wyniki (--only NN --png): Z00 2 s., Z02 12 s., Z03 11 s., Z04 14 s. – bez zmian; PDF/PNG identyczne co do piksela z wersją sprzed
  poprawki (autorzy obeszli błąd w tekście, wszystkie obecne podziały to prawdziwe przejścia, dy = 0). 0 BŁĄD, 0 UWAGA, numeracja
  stabilna; --demo 42 s. identyczne (2 UWAGI = odsyłacze do jeszcze nienapisanych c05/c06). Arkusze miniatur obejrzane: brak dziur.
  Zmian w plikach rozdziałów nie było potrzeby.
- Test regresji (scratchpad/f0b-fix: stara vs nowa lib w kopii z dowiązaniami; warianty z przeszukiwania Z04 i stara wersja Z02):
  Z04 v01 15->14 s., v02 15->14, v04 17->15, v12 15->14, v15 15->15, v19 16->15, v59 17->15, v00 16->15; Z02 (szkic) 14->13;
  wszystkie strony 2–6% zniknęły, 0 UWAG (poza v00: s. 11 30% – rycina, nie splitCols). Strony v01 s. 4–6 i Z02 s. 8–10 obejrzane w 96 dpi.
- Zostaje (bez związku z poprawką, znane z z02.md): blok .cols przed ryciną, która nie mieści się na stronie, wypełnia kolumny po kolei
  (prawa kolumna krótsza) – inkCheck tego nie łapie (mierzy najniższy atrament). Cele w zakładkach/linkach PDF też są w układzie pola
  zadruku (widok skacze ok. 62 pt wyżej) – nieszkodliwe, nie ruszane.
- Do autorów: obejścia „żaden element nie może startować 1–5 wierszy pod górą strony” nie są już potrzebne.
