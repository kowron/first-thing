# Szkielet osiowy w 4 dni

Strona do nauki na zaliczenie nr 2 (szkielet osiowy): pytania prowadzącego, odpowiedzi według Bochenka (t. I).

## Układ
- `site/` – gotowa strona (to jest opublikowane jako artefakt)
  - `index.html` – szkielet strony i cały CSS
  - `app.js` – cała logika (widoki, sesja nauki, powtórki, egzamin, zapis postępu)
  - `wym.js` – listy do wymienianki (nazwy polskie i łacińskie wg Bochenka, strony)
  - `wymatch.js` – dopasowanie mowy/tekstu do nazw (klucz fonetyczny, tolerancja błędów; testowalne w node)
  - `gra.js` – wymienianka na czas: tryby polska/łacińska/mieszana, czas, punkty, medale, rekordy (`S.g`)
  - `lac.js` + `lac_data.js` – tryb Łacina: wszystkie nazwy łacińskie z Bochenka (s. 219–298, 649–733); runda 1 przegląd (umiem / nie jestem pewny / nie umiem), od rundy 2 pisanie tylko niepewnych, błędne wracają; stan w `S.lt`
  - `bank.js` – bank pytań, GENEROWANY z `bank/*.txt` (nie edytować ręcznie)
  - `fonts.css` – czcionki Literata i Instrument Sans jako data URI
- `bank/` – źródło treści: pytania, punkty odpowiedzi, dopytania, łacina
- `tools/mkbank.py` – kompilator banku

## Zmiana treści
Edytuj `bank/*.txt`, potem:

    python3 tools/mkbank.py bank site/bank.js

Format pliku banku:
- `@B tytuł bloku`
- `@L id | tkanka (muscle/bone/joint) | tytuł lekcji | opis`
- `@U id | priorytet 1–3 | strony Bochenka`
- `Q: pytanie prowadzącego`
- `H: nagłówek grupy punktów`
- `- punkt odpowiedzi ?? pytanie fiszki do tego punktu {s. 718–719}`
- `F: dopytanie => odpowiedź {s. 719}`
- `{s. …}` na końcu linii = strony Bochenka do przeczytania przed fiszką (sprawdzone z tekstem książki); `{z zajęć}` = treść spoza Bochenka.
  Strona pokazuje: zakres stron całej lekcji, stron pytania (`@U`), strony przy każdym punkcie odpowiedzi, na fiszce i przy słówku łacińskim.
- `X: uwaga do źródeł`
- `[tekst|nomen latinum|mianownik]` – pokazuje łacinę i dodaje słówko do wpisywania; `_tekst_` – kursywa bez słówka

## Podgląd lokalny
    cd site && python3 -m http.server 8000

Lokalnie postęp zapisuje się w localStorage (klucz `so5_v1`). Podpowiedź AI, dyktowanie i zapis na koncie
działają tylko w artefakcie na claude.ai (`window.claude.use('sample' | 'dictation' | 'db' | 'user')`);
poza nim strona po prostu ich nie używa.

## Mechanika (app.js)
Stan każdego pytania/słówka: `n` (ile podejść), `t` (czas), `d` (1 = utrwalone), `m` (brakujące punkty), `f` (nieudane dopytania).
Pierwszy raz: czytanie → odpowiedź z pamięci → porównanie → fiszki braków i dopytań do skutku.
Następnego dnia (granica doby 4:00) pełna powtórka; dobra odpowiedź utrwala, braki wracają kolejnego dnia już same.
Łacina: wpisywana, błędne wracają w rundach do skutku.

## Zasady treści
Źródłem jest Bochenek. Cecha struktury = to, co ją odróżnia od reszty grupy; przymiotniki zawsze z punktem odniesienia.
Każda informacja w jednym pytaniu.

## Łacina (`lac_src/`)
`lac_1..6.json` – nazwy wypisane z tekstu Bochenka (po jednym rozdziale), `lac_drop.txt` – pominięte, `merge_lac.py` – scala je do `site/lac_data.js` (bez powtórzeń, działy w kolejności książki). Lekcje z pytaniami nie mają już wpisywania łaciny.
