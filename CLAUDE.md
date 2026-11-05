# Zasady pracy w tym repozytorium (od użytkownika, 4.11.2026)

Użytkownik nie zna się na programowaniu ani GitHubie – wszystko tłumaczyć prosto, po polsku, i robić za niego.

## Poziomy wysiłku (effort) i koszt
- **Nigdy nie używać poziomu „max”.** Sufit dla wszystkich modeli to **xhigh** (jest też wymuszony w `.claude/settings.json`).
- **Domyślnie medium** – dla większości zadań (Sonnet i Opus). Wysokie poziomy tylko wtedy, gdy zadanie tego naprawdę wymaga.
- Użytkownik wprost pozwolił dobierać poziom do zadania, także dla subagentów (parametr `effort` w narzędziu Agent):
  - **Sonnet:** low/medium – czytanie i przeglądanie źródeł, mało ważne odczyty, kod i skrypty rutynowe; high/xhigh – merytoryka, która trafi do plików wyjściowych (treść plakatów, weryfikacja faktów, terminologia).
  - **Opus:** medium – zadania trudniejsze, ale rutynowe (np. proste rysunki, weryfikacje); high – wymagające rysunki i złożona praca; xhigh – tylko najtrudniejsze rysunki/zadania wymagające najlepszej jakości.
  - Rysunki dzielić na zwykłe (medium/high) i najtrudniejsze (xhigh).
- **Aktualizacja 5.11.2026:** użytkownik chce, żeby więcej pracy szło na **Opusie xhigh** (rysunki, treść ★, weryfikacje z Bochenkiem), a mniej na Sonnecie. Sufit nadal xhigh – nigdy „max”.
- **Aktualizacja 5.11.2026 (2):** **NIE używać Sonneta do żadnych zadań** (także subagentów – zawsze `model: "opus"`), bo wykonywał polecenia niespójnie. Opus **medium** tylko do prostych zadań; do większości **high**, a do najważniejszych/najtrudniejszych **xhigh**. Domyślnie high. Nadal nigdy „max”. Poniższe zasady o Sonnecie są nieaktualne.
- Mało subagentów naraz (kilku, nie kilkunastu); nie uruchamiać zbędnych równoległych audytów. Jeśli praca jest duża, dzielić ją na etapy do zatwierdzenia przez użytkownika.

## Plakat A0 „Anatomia: szkielet osiowy”
Stan i instrukcje przebudowy: `plakat/HANDOFF.md` (sekcja „AKTUALIZACJA – sesja 2” na górze). Wszystko wg Bochenka t. I; terminologia dokładna co do słowa; łacina na rysunkach tylko taka, jaka jest u Bochenka.
