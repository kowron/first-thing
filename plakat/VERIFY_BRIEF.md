# Weryfikacja treści plakatu z Bochenkiem – instrukcja

## Po co
Student medycyny uczy się z: A. Bochenek, M. Reicher, *Anatomia człowieka*, t. I. Zasada użytkownika: **wszystko w 100% z Bochenka;
jeśli gdzie indziej jest inaczej – Bochenek ma rację.** Ktoś inny przygotował treść plakatu (plik JSON). Ty jesteś niezależnym
sprawdzającym: porównujesz **każdy punkt** z książką i zgłaszasz błędy. Sam nic nie zmieniasz w plikach plakatu.

## Źródła
- `/home/user/first-thing/bones.txt` – OCR rozdziałów o kościach i połączeniach. Znacznik `=== PDF N-0 ===` / `=== PDF N-1 ===` = lewa / prawa
  połowa strony PDF nr N. Numer strony książki stoi w stopce (osobna linia z liczbą 3-cyfrową).
- `/home/user/first-thing/all.txt` – OCR rozdziałów o mięśniach (przepona, mechanika oddychania); znaczniki `=== BOOK PAGE N ===`.
- Skan: `/tmp/claude-0/-home-user-first-thing/d41721b4-1413-50bf-8c94-691fa5e52b07/scratchpad/skan.pdf`
  Render: `mkdir -p /tmp/<twój_katalog> && pdftoppm -r 150 -f N -l N -png "<skan>" /tmp/<twój_katalog>/x` (N = numer strony PDF;
  jedna strona PDF = dwie strony książki – przytnij połówkę przez PIL), obejrzyj narzędziem Read.
- OCR psuje łacinę i liczby. **Każdą liczbę i każdą łacińską nazwę, która w OCR wygląda inaczej niż w JSON, sprawdź na skanie.**
  Nie poprawiaj na podstawie wiedzy ogólnej – liczy się tylko tekst Bochenka.

## Co sprawdzasz (w przydzielonej części pliku)
Dla każdej karty i grupy: `title`, `lat`, `pg`, `tag`, `why`, `q`, każdy punkt `sections[i].items[j]`, każdy punkt `l3[i]` (tekst i `pg`),
każdą pozycję `labels[i]` (nazwy do podpisania na rysunku).
Zgłaszasz tylko **prawdziwe problemy**:
1. treść niezgodna z Bochenkiem (fakt, liczba, kierunek, położenie, przyczep, nazwa PL, nazwa łac., odmiana łaciny),
2. coś, czego u Bochenka nie ma (dopowiedziane z wiedzy ogólnej) – do usunięcia albo poprawy,
3. błędny numer strony `pg`,
4. pomylone struktury / przypisanie cechy do złego kręgu, żebra itp.,
5. treść spoza zakresu: rozwój i zmienność kręgosłupa, żeber, mostka; zmienność kształtu klatki; czynność kręgosłupa;
   połączenie kręgosłupa z czaszką; czaszka; część ogólna o połączeniach,
6. **ważne braki**: cecha opisana przez Bochenka w danym podrozdziale (także małym drukiem), której nigdzie w karcie nie ma.
Nie zgłaszasz: stylu, skrótów, kolejności, długości, sformułowań, które oddają sens Bochenka, ani znaczników formatowania
(`**…**`, `{{…}}`, `[[…]]` – zostaw je w poprawkach w tym samym stylu). Punkt z kategorią `!` = niezgodność wewnątrz Bochenka – sprawdź,
czy naprawdę jest.

## Wynik – plik JSON `/home/user/first-thing/plakat/verify_<ID>.json` (ID podane w zadaniu)
```json
{
  "issues": [
    {"card": "<dokładny tytuł karty lub grupy>", "field": "sections/1/2",
     "problem": "krótko: co jest źle",
     "fix": "pełny poprawiony tekst tego pola/punktu (w tym samym stylu, z **…** {{…}})  albo null = usunąć punkt",
     "evidence": "s. 224: krótki cytat z Bochenka (≤ 15 słów)"}
  ],
  "missing": [
    {"card": "<tytuł>", "where": "sections/1  albo  l3", "k": "kategoria dla l3", "text": "nowy punkt w stylu karty", "pg": "224"}
  ],
  "checked": 123,
  "notes": "co było nieczytelne / niepewne"
}
```
`field`: `title`, `lat`, `pg`, `tag`, `why`, `q`, `sections/<i>/<j>` (= `sections[i].items[j]`, liczone od 0), `l3/<i>` (= `l3[i]`),
`l3/<i>/pg`, `labels/<i>`. Indeksy liczysz w pliku tak, jak jest teraz zapisany.
Zapisuj wynik na bieżąco (po każdych kilku kartach), żeby przy przerwie nic nie przepadło. Plik musi się wczytać przez `json.load`.
Pliki robocze tylko w `/tmp/<twój_katalog>`. Nie zmieniaj żadnych innych plików.

Na koniec odpowiedz krótko: ile punktów sprawdzone, ile błędów (najważniejsze 3–5 w jednym zdaniu każdy), czego nie dało się sprawdzić.
