# Stan G – Genomika: analiza genomu i genotypowanie

## Krok 0 – start (2026-11-16)
- Brak wcześniejszego stanu; przeczytane: handoff G, ZASADY, KOMPONENTY, bank-rycin/INDEX.md + podglad-g.png, wzór rozdz. z05 + stan/z05.md, sekcja sekwencjonowania i mikromacierzy w z06 (odsyłacze #c05, #c06).
- Plik wynikowy: rozdzialy/z01-genomika.html (data-num="01", data-label="G", id c01-), limit 14 s.; wyciąg: wyciagi/g.md.
- Ryciny z handoffu (bank): g-02 (224 mm, 9/10), g-06 (162), g-07 (224, 9/10), g-09 (173), g-11 (162), g-16 (111), g-17 (124), g-21 (123) = 1303 mm ≈ 5,2 s. z 14 → zostaje ok. 8,8 s. tekstu.
- Ryzyko: g-02 i g-07 po 9/10 strony. Kandydat do zamiany: g-07 → g-05 (allele dropout, 99 mm) albo pominięcie (Sanger jest w z06); decyzja po 1. buildzie.
- Linie źródła: „Źródło: prezentacja LMZ 3, slajdy X–Y” (zakres z nagłówka rozdziału opracowania).
- Następny krok: 1 – wyciąg z material/genomika.txt (s. 4–77).
- Krok 1 w toku: wyciąg rozdz. 01–04 zapisany w wyciagi/g.md (dalej: 05–18, od linii 1369 materiału).
- Wyciąg rozdz. 05–07 dopisany (dalej: 08–18, od linii 2368).
- Wyciąg rozdz. 08–09 dopisany (dalej: 10–18, od linii 2764).
- Wyciąg rozdz. 10–11 dopisany (dalej: 12–18, od linii 3189).
- Wyciąg rozdz. 12–14 dopisany (dalej: 15–18 + „Najważniejsze rozróżnienia”, od linii 3734).

## Krok 1 – wyciąg (zrobione)
- Plik: wyciagi/g.md – fakty Z/T dla 18 rozdz. opracowania (s. 4–79), układ 7 podrozdziałów, 8 rycin.
- Decyzje: daty/liczby baz populacyjnych (2504/26, 60 706, 807 162) – T; testy komercyjne (FoundationOne itd.) – T; narzędzia (tabela 10 programów) – T; ryciny spoza listy – T, fakty z nich (ryc. 10, 14, 19, 20) krótko w tekście.
- Rozbieżność planu: HGVS (s. 55) nie ma w kolumnie „Zostaje” ani „Tniemy” → 2–3 zdania (w razie wątpliwości zostaje).
- „Uwaga do źródła”: Western/ELISA (slajd: „Western do płynnych, ELISA do stałych”) – 1 ramka; ew. 2.: skala jakości 0–1 vs Phred.
- Następny krok: 2+3 – tekst rozdz. rozdzialy/z01-genomika.html z rycinami z banku.

## Krok 2+3 – tekst i ryciny (zrobione, przed buildem)
- Plik: rozdzialy/z01-genomika.html – 7 h2 wg handoffu, linie źródła „prezentacja LMZ 3, slajdy …”, 13 Pojęć, 6 Zapamiętaj, 1 Uwaga do źródła (Western/ELISA), W60 (6 pkt).
- Ryciny z banku (8): g-ryc-02, 06, 07, 09, 11, 16, 17, 21. Nowych 0. Odsyłacze: chapref #c05 (PCR), #c06 (kapilara, mikromacierze).
- Tabele: rodzaje wariantów, HTT, chromatogram, strategie, macierze, Q, położenie→skutek, SIFT vs PolyPhen, bazy, gwiazdki ClinVar, 5 klas.
- Następny krok: 4 – build `node build.mjs --only 01 --png`, limit 14 s.

## Krok 4 – autokontrola (w toku)
- Build 1: 20 s. (limit 14), 0 BŁĄD, 1 UWAGA (s. 13 – 32%, dziura przed ryciną). Kopia: scratchpad/g-work/z01-b1.html (60,9 KB).
- Decyzja: g-ryc-07 (9/10 s.) pominięta – dubluje g-06 i opis Sangera/kapilary z z06, a bez niej limit jest osiągalny (zgoda zleceniodawcy na pominięcie). Zostaje 7 rycin z banku.
- Plan: tekst −35% (cel ok. 40 KB): Pojęcia → definicje w tekście, skrócone opisy narzędzi (HiFi/nanopor, IGV, SWISS-MODEL/DALI/Rosetta, NCBI/Ensembl/HPA/GDC), bez powtórzeń tabel w prozie; definicje, mechanizmy, reguły interpretacji zostają.
- Build 2: tekst skrócony do 40 KB (bez Pojęć – definicje w tekście) → **14 s., 0 BŁĄD, 0 UWAGA**. Kopia: scratchpad/g-work/z01-b2.html.
- Luki: s. 1 (~20% przed g-02), s. 5 (~33% przed g-09), s. 8 (~27% przed g-16), s. 11 (kolumna 2 pusta – h3 „Położenie i mechanizm” tuż przed tabelą wide psuje wyrównanie). Ostatnia strona ~90%.
- Build 3 (plan): w lukach przywrócić ucięte fakty (tylko po stronie, która ma lukę; nic przed g-06), dodać zdanie wstępne po h3 „Położenie i mechanizm”.
- Build 3: przywrócone fakty w lukach (s. 1, 5, 8), zdanie po h3 „Położenie i mechanizm” → wyrównanie s. 11 naprawione; **14 s., 0/0**. Kopia: scratchpad/g-work/z01-b3.html. Ostatnia strona pełna do krawędzi (brak zapasu na dłuższe odsyłacze w pełnym buildzie); luki: s. 5 ~24%, s. 8 ~27%, s. 1 ~14%.
- Build 4 (plan): zapas na s. 14 – usunięta tabela SIFT vs PolyPhen-2 (treść w akapicie i W60), krótsza uwaga o skali 0–1; w lukach s. 5 i 8 – zdanie o metodach ze slajdu 21 (Maxam–Gilbert, pirosekwencjonowanie, SOLiD), jakość WES, trio, pochodzenie wariantu w guzie.
