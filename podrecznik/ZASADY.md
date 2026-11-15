# Zasady dla agentów piszących rozdziały (obowiązują wszystkich)

## Treść
1. **Tylko źródła z handoffu.** Każdy fakt, liczba, nazwa musi być w paczce źródeł rozdziału. Zero własnej wiedzy, zero „z liceum”, zero treści z innych rozdziałów podręcznika źródłowego.
2. **Zakres = zagadnienia z rozpiski** (lista w handoffie). Fragmenty źródła, które nie dotyczą żadnego zagadnienia – pomijamy w całości.
3. **Tniemy 10–30%** treści mieszczącej się w zagadnieniach. W pierwszej kolejności: daty, nazwiska, dygresje historyczne, długie wyliczanki przykładów (zostaw 2–3), szczegóły techniczne aparatury, powtórzenia, rzadkie wyjątki. Nie tniemy: definicji, etapów procesów, mechanizmów, klasyfikacji, liczb, o które łatwo zapytać, porównań.
4. **Tłumaczenie jest ważniejsze niż ozdobniki**: prosty język, krótkie zdania, najpierw „po co i co to jest”, potem mechanizm, potem szczegóły. Procesy – listy kroków; porównania – tabele. Objaśnienia logiczne są dozwolone, nowe fakty – nie.
5. Żadnych pytań, quizów, „sprawdź się”, „na kolokwium”.
6. Każdy podrozdział kończy linia źródła: `Źródło: Drewa s. X–Y` (albo Jóźwiak / Jorde / Ostrowska / Alster / Twyman / Materiał pomocniczy).
7. Błąd lub niejasność w źródle: krótka ramka „Uwaga do źródła” (maks. 1–2 na rozdział), tylko gdy pewne.
8. OCR bywa zniekształcony: nie zgaduj liczb; wątpliwe pomiń i zapisz w stanie.

## Forma
- Fragment HTML według `podrecznik/KOMPONENTY.md` (wersja dwukolumnowa – powstaje w fazie 0B). Jeden plik = jeden rozdział: `rozdzialy/zNN-nazwa.html`.
- Komponenty: akapit, h2, h3, listy, tabela, „Pojęcie” (krótka definicja w kolumnie), ramka „Zapamiętaj” (maks. 1 na podrozdział h2, 2–3 zdania), „W 60 sekund” na końcu rozdziału (4–6 punktów). Bez „Przykładów” z wymyślonymi danymi.
- **Ryciny**: najpierw sprawdź `bank-rycin/INDEX.md` – gotową rycinę wstawia się jednym znacznikiem, bez przerysowywania. Nową rysuj tylko dla procesu kluczowego w rozdziale i tylko w liczbie z handoffu. Nowa rycina: inline SVG, klasy z `KOMPONENTY.md`, wysokość ≤ 1/3 strony, podpis 1–2 wiersze.
- Limit stron z handoffu jest twardy.

## Tryb pracy (oszczędny)
Kroki – po każdym dopisz 3–6 linijek do `stan/zNN.md` (zrobione / pliki / następny krok / decyzje):
1. **Wyciąg** – przeczytaj paczkę źródeł RAZ i zapisz `wyciagi/zNN.md`: dla każdego zagadnienia lista faktów (1 linia = 1 fakt, ze stroną), przy każdym `Z` (zostaje) albo `T` (tniemy, z powodem w 2–3 słowach). Na końcu: proponowany układ podrozdziałów i lista rycin (z banku / nowe).
2. **Tekst** – pisz rozdział wyłącznie z wyciągu (do źródła wracaj tylko po dokładne brzmienie).
3. **Ryciny** – wstaw gotowe, narysuj nowe.
4. **Autokontrola** – build rozdziału (maks. 4–5 buildów), limit stron, każdy fakt `Z` z wyciągu jest w tekście, żaden fakt spoza wyciągu; obejrzyj strony raz.
Po przerwaniu: czytaj handoff + `stan/zNN.md` + `wyciagi/zNN.md`. Nie czytaj źródeł od nowa.

## Raport końcowy (maks. 12 linijek)
Plik, liczba stron, liczba rycin (bank / nowe), odsetek uciętych faktów, 5 najważniejszych cięć, wątpliwości do rewizji.
Nie commituj.
