# Handoff R3 – rewizja podręcznika (Sonnet, recenzent)

Podręcznik „Biologia molekularna” (po polsku, studenci I roku lekarskiego, do egzaminu) jest w `/home/user/first-thing/podrecznik/`. Każdy rozdział ma część 1 (wszystkie zagadnienia) i część 2 „na piątkę” (szczegóły). Treść ma pochodzić WYŁĄCZNIE ze źródeł z rozpiski zajęć.

**Twoja rola: zgłaszaj wszystko, co podejrzane. Wszystko, co może być nie tak – zapisz.** Niczego nie poprawiasz i nie zmieniasz żadnych plików poza swoim raportem. Nie odsiewaj – wątpliwości rozstrzygnie szef. Lepiej zgłosić za dużo niż przeoczyć.

## Materiał dla rozdziału NN
- `pakiety/zNN.txt` – jeden plik: A rozpiska, B mapa zakresu, C fakty kiedyś ucięte, **D aktualny tekst rozdziału (bez rycin SVG; podpisy rycin są)**, **E źródła przycięte do zakresu**. Przeczytaj D i E w całości (kawałkami po ok. 800–1000 linii).
- Skład: `node build.mjs --only NN --png` (z katalogu `podrecznik/`) → strony PNG w `/tmp/claude-0/-home-user-first-thing/600b873f-e07d-5766-b2f4-6a90b68ae091/scratchpad/build-podrecznik/rozdzial-NN-png/`. Obejrzyj strony z rycinami i 4–6 innych (początek rozdziału, początek części 2, strony z tabelami). W buildzie jednego rozdziału odsyłacze do innych rozdziałów pokazują „?” – to normalne, nie zgłaszaj.
- Zasady: `ZASADY.md`, `STYL.md` (krótkie).

## Co sprawdzasz
1. **Merytoryka:** każdy fakt, liczba, nazwa, kolejność etapów, kierunek zależności w D – czy zgadza się ze źródłem w E; twierdzenia mocniejsze niż w źródle; fakty, których w E nie ma (uwaga: objaśnienia logiczne, definicje słów i przykłady oznaczone jako przykładowe są dozwolone – zgłaszaj tylko, gdy wyglądają na nowy fakt); sprzeczności między częścią 1 a częścią 2 i między miejscami w rozdziale; błędy w rachunkach i przykładach.
2. **Zrozumiałość:** pojęcie użyte przed wyjaśnieniem; skok w rozumowaniu; zdanie niezrozumiałe lub dwuznaczne; odsyłacz prowadzący do treści, której tam nie ma.
3. **Język:** literówki, błędy gramatyczne, zła odmiana, resztki po redakcji (urwane zdania, powtórzone akapity, znaczniki typu @@…@@), niespójna pisownia terminu.
4. **Ryciny i skład (z PNG):** rycina niezgodna z podpisem lub tekstem; nieczytelne lub nachodzące napisy; błędne etykiety; duże puste miejsca, pusta kolumna, tabela lub ramka ucięta/źle złamana, nagłówek sam na dole strony; rycina daleko od miejsca, które do niej odsyła.
5. Linie „Źródło: …” wskazujące strony spoza zakresu z sekcji A/B.

## Raport: `rewizja3/zNN.md`
Lista numerowana; każda pozycja w 1–3 linijkach:
`N. [M|Z|J|S] miejsce (id h2/h3 albo pierwsze słowa akapitu / nr strony PNG) → co jest → co podejrzane / jak jest w źródle (strona)`.
M = merytoryka, Z = zrozumiałość, J = język, S = skład/ryciny. Dodaj `(pewne)` albo `(do sprawdzenia)`.
Na końcu 2 zdania oceny ogólnej. Nie commituj. Odpowiedź końcowa: liczba pozycji M/Z/J/S i 3 najpoważniejsze.
