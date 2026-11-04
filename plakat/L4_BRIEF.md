# Treść do plakatów: KOŚCIEC OSIOWY oraz POŁĄCZENIA I MECHANIKA – instrukcja

## Po co
Student 1. roku medycyny (ŚUM) uczy się szkieletu osiowego z: A. Bochenek, M. Reicher, *Anatomia człowieka*, t. I.
Robimy wielkie plakaty A0 (PDF) z przybliżaniem:
- **poziom 1** (z daleka) – sam podział (drzewo grup),
- **poziom 2** (po przybliżeniu) – karty: cechy kości / budowa połączenia / opis zjawiska, z nazwami PL i łac.,
- **poziom 3** (duże przybliżenie) – szczegóły małym drukiem.
Przy kartach będą rysunki (robi je kto inny) – Ty podajesz, co na rysunku ma być podpisane.
Zasada nadrzędna użytkownika: **wszystko w 100% z Bochenka; jeśli gdzie indziej jest inaczej – Bochenek ma rację.**
Użytkownik sprawdza fakty. Lepiej pominąć niż napisać coś niepewnego.
Użytkownik **lubi podziały** – dzięki nim układa wiedzę „w szufladki”. Drzewo ma być przemyślane i zgodne z Bochenkiem.

## Źródła (tylko te)
- `/home/user/first-thing/bones.txt` – OCR rozdziałów o kościach i połączeniach. Znacznik `=== PDF N-0 ===` / `=== PDF N-1 ===` = lewa / prawa połowa
  strony PDF nr N. Numer strony książki stoi w stopce (osobna linia z liczbą 3-cyfrową) – na jej podstawie podawaj `pg`.
  Plik pomocniczy `/tmp/bonesp.tsv` (kolumny: znacznik PDF, nr linii, tekst) – nr linii jak w bones.txt.
- Skan: `/tmp/claude-0/-home-user-first-thing/d41721b4-1413-50bf-8c94-691fa5e52b07/scratchpad/skan.pdf`
  Render: `pdftoppm -r 150 -f N -l N -png "<skan>" /tmp/<twój_katalog>/x`, przytnij połówkę (PIL), obejrzyj narzędziem Read.
  Ryciny Bochenka możesz oglądać, żeby zrozumieć kształty i co podpisać – ale ich nie kopiujesz.
- OCR psuje łacinę i liczby (np. „azillae”, „0s sacrum”, „C,_;”). **Każdą liczbę i każdą wątpliwą nazwę łacińską sprawdź na skanie.**
  Nie zgaduj z wiedzy ogólnej.

## Zakres – co bierzesz (podane w zadaniu). Czego NIE bierzesz nigdy:
rozwój kręgosłupa, zmienność kręgosłupa, rozwój żeber i mostka, zmienność żeber i mostka, zmienność kształtu klatki piersiowej,
czynność kręgosłupa, ogólna charakterystyka/wymiary/powierzchnia/kanał kręgosłupa, połączenie kręgosłupa z czaszką, czaszka,
część ogólna o połączeniach kości. Osteologię kręgów, żeber i mostka bierzesz **całą i bardzo dokładnie** (także fragmenty małym drukiem w tych podrozdziałach).

## Format wyniku – plik JSON (UTF-8)
```json
{
  "chapter": "<nazwa z zadania>",
  "tree": [ <węzły> ]
}
```
Węzeł grupy (poziom 1 – podział):
```json
{"type": "group", "title": "Kręgi szyjne", "lat": "vertebrae cervicales", "pg": "222–228",
 "why": "krótko, czym ta grupa się wyróżnia (≤ 90 znaków)",
 "q": "opcjonalnie: pytanie-kryterium podziału dzieci, np. „który kręg?” (≤ 40 znaków)",
 "l3": [ <punkty poziomu 3 o całej grupie> ],
 "children": [ <węzły: grupy albo karty> ]}
```
Węzeł karty (poziom 2 + 3):
```json
{"type": "card", "title": "Kręg szyjny typowy (C3–C6)", "lat": "vertebra cervicalis", "pg": "222–224",
 "tag": "opcjonalnie: krótka etykieta, np. „STAW”, „CHRZĄSTKOZROST”, „WIĘZOZROST”, „KOŚCIOZROST”",
 "sections": [ {"k": "TRZON", "items": ["…", "…"]}, {"k": "ŁUK I WYROSTKI", "items": ["…"]} ],
 "l3": [ {"k": "KATEGORIA", "t": "…", "pg": "224", "src": "320-331"} ],
 "labels": ["guzek przedni {{tuberculum anterius}}", "…"],
 "fig": "jaki rysunek: np. „widok od góry” / „widok z boku” / „przekrój strzałkowy”; może być kilka, rozdzielone ' | '"}
```
- `sections` = poziom 2: najważniejsze cechy, które trzeba umieć (to, czego się uczy na zaliczenie). Krótkie punkty-notatki.
- `l3` = poziom 3: szczegóły, wymiary, uwagi, różnice, „!” dla niezgodności w samym Bochenku (np. opis vs streszczenie).
  Pole `k` w l3: krótka kategoria WIELKIMI LITERAMI (np. „SZCZEGÓŁY”, „WYMIARY”, „UWAGI”, „!”).
- `labels` = lista struktur do podpisania na rysunku (PL + łac.), 5–18 pozycji, tylko te, które da się pokazać na danym widoku.
- `fig` = jaki widok/rysunek najlepiej to pokaże.
- Strony `pg` przy karcie; w l3 przy każdym punkcie. Pole `src` = zakres linii w bones.txt.

## Styl tekstu
- Po polsku, prostym językiem, styl notatki (równoważniki zdań). Punkt ≤ ~220 znaków.
- **Nazwy struktur PL i łac. są równie ważne**: zapis `**guzek przedni** {{tuberculum anterius}}` – pogrubienie polskiej nazwy
  i łacina w podwójnych nawiasach klamrowych (pokaże się kursywą tej samej wielkości).
- Łacina „poboczna” (gdy tylko dopowiadasz) w podwójnych nawiasach kwadratowych: `[[processus spinosus]]` – małą czcionką w nawiasie.
- Tłumacz pozytywnie, czym coś jest. **Nie** używaj konstrukcji „to jest X, czyli NIE Y”. Nie upychaj wielu nowych nazw w jednym zdaniu.
- Bez rankingów siły. Zapis: m./mm./n./ż.; kręgi C1, Th12, L5, S1, Co1; żebra cyframi rzymskimi; zakresy z półpauzą „–”.
- Przy podziałach używaj kryteriów Bochenka (np. żebra prawdziwe/rzekome/wolne; kręgi prawdziwe/rzekome; połączenia ścisłe – więzozrosty,
  chrząstkozrosty, kościozrosty – i stawy), tak jak je podaje.

Plik musi się wczytać przez `python3 -c "import json; json.load(open('<plik>'))"`. Zapisuj go na bieżąco (po każdej większej części),
żeby przy przerwie nic nie przepadło. Pliki robocze trzymaj w /tmp/<twój_katalog>. Nie zmieniaj żadnych innych plików.

Na koniec odpowiedz krótko: struktura drzewa (tytuły), ile kart/punktów, niezgodności w Bochenku, czego nie dało się odczytać.
