# Handoff R2 – kontrola wierności po przepisaniu (Fable, 1 agent = 1 rozdział)

## Po co
Rozdziały zostały przepisane według `STYL.md` (tłumaczenie: „po co → co → jak”, definicje przed użyciem, przykłady, analogie). Autorzy mieli dopisywać **wyjaśnienia**, ale nie **nowe fakty**. Przy takim przepisywaniu łatwo o trzy błędy: (1) fakt spoza źródeł podany jako wyjaśnienie, (2) wzmocnione twierdzenie („towarzyszy” → „powoduje”, „może” → „zawsze”), (3) zgubiony fakt, który był w poprzedniej wersji. Twoje zadanie: znaleźć je i naprawić. Nie oceniasz stylu, chyba że zdanie jest niezrozumiałe lub błędne.

## Materiały
- Nowy rozdział: `rozdzialy/zNN-*.html` (Genomika: `z01-genomika.html`).
- Stara wersja (sprzed przepisania): `git show HEAD~0:podrecznik/…` nie pomoże – użyj archiwum `/tmp/claude-0/-home-user-first-thing/600b873f-e07d-5766-b2f4-6a90b68ae091/scratchpad/archiwum-v1/zNN-*.html`; jeśli go brak – `git log --oneline -- podrecznik/rozdzialy/zNN-*.html` i `git show <commit sprzed „Rewrite chapter ZNN”>:podrecznik/rozdzialy/zNN-….html`.
- Stan autora: `stan/zNN-v2.md` – **przeczytaj sekcje z wątpliwościami i „do decyzji”** – to pierwsze miejsca do rozstrzygnięcia.
- Wyciąg `wyciagi/zNN.md` (fakty ze stronami), rewizja `rewizja/zNN.md` (jeśli jest), mapa `handoff/ZNN.md`.
- Źródła: paczka `/tmp/claude-0/-home-user-first-thing/600b873f-e07d-5766-b2f4-6a90b68ae091/scratchpad/zrodla/zNN/` (`SPIS.md`); dla Z09–Z11 Drewa OCR `/root/.claude/uploads/600b873f-e07d-5766-b2f4-6a90b68ae091/b95214fd-Drewa_Genetyka_medyczna_OCR.txt` (zakresy linii w `handoff/ZNN.md`); dla Z04/Z05 też `material/k4.txt`, `material/k5.txt`; dla G – `material/genomika.txt`. Skan Drewy (strona PDF = strona książki + 28): `…/scratchpad/dropbox/Drewa - Genetyka medyczna.pdf`.
- Zasady: `ZASADY.md` (tylko źródła z rozpiski zajęć; stary Jorde – tylko gdy brak w Drewie), `STYL.md` (co wolno dopisać: objaśnienia logiczne, definicje, przykłady z liczbami oznaczonymi jako przykładowe).

## Jak sprawdzasz (oszczędnie – czytaj źródła tylko tam, gdzie jest wątpliwość)
1. Przeczytaj nowy rozdział w całości. Przy każdym zdaniu, które podaje **fakt** (liczba, nazwa, mechanizm, kolejność, związek przyczynowy, przykład kliniczny), a nie jest oczywistym objaśnieniem logicznym – zapytaj: czy to jest w wyciągu / starej wersji / źródle? Jeśli nie wiesz – sprawdź w źródle.
2. Porównaj automatycznie stary i nowy tekst: liczby, nazwy własne, symbole genów/białek obecne w starej wersji, a nieobecne w nowej (skrypt: wyciągnij tokeny z cyframi i słowa z wielkiej litery/symbole, różnica zbiorów). Każdy brak: celowe cięcie (T w wyciągu) czy zguba?
3. Linie „Źródło: …” – czy wskazują strony z rozpiski zajęć (zakres w `zrodla/zNN/SPIS.md` lub `handoff/ZNN.md`). Strona spoza rozpiski = sprawdź, czy fakty stoją też na stronie z rozpiski; jeśli nie – fakt usuń.
4. Ryciny i podpisy: czy podpis nie twierdzi czegoś, czego rycina/tekst nie pokazuje.

## Co robisz z wynikami
- **A (błąd: fakt spoza źródeł, sprzeczność ze źródłem, wzmocnione twierdzenie, zgubiony fakt Z)** – **poprawiasz od razu w pliku rozdziału**, minimalną zmianą tekstu (usuń/złagodź zdanie, przywróć fakt w odpowiednim miejscu). Nie przestawiaj rycin, nie przebudowuj akapitów.
- **Wątpliwości autora** ze `stan/zNN-v2.md` – rozstrzygnij (zostaje / zmienić / usunąć) i wykonaj.
- **B/C** (niejasność, drobna nieścisłość, kosmetyka) – tylko zapisz.
- Po poprawkach: `cd /home/user/first-thing/podrecznik && node build.mjs --only NN --png` – 0 BŁĄD; jeśli pojawi się UWAGA o pustej stronie, a wynika z Twojej zmiany – popraw drobnym skróceniem/wydłużeniem w tym samym miejscu (maks. 3 buildy). Odsyłacze do innych rozdziałów pokazują w buildzie jednego rozdziału „rozdz. ?” – to normalne.
- Wynik zapisz w `rewizja/zNN-v2.md`: sekcja „Naniesiono (A)” – lista: miejsce → było → jest → źródło; sekcja „Wątpliwości autora – rozstrzygnięcia”; sekcja „B/C – do decyzji” (maks. 15 pozycji); ocena 2–3 zdania.

Nie commituj. Nie ruszaj innych rozdziałów, `css/`, `lib/`, `build.mjs`.
Raport (maks. 8 linijek): ile poprawek A, 3 najważniejsze, rozstrzygnięcia wątpliwości, czy build czysty.
