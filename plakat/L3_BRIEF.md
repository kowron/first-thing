# Poziom ③ plakatu „Mięśnie szkieletu osiowego” – instrukcja dla wyciągania szczegółów z Bochenka

## Po co to jest
Student 1. roku medycyny (ŚUM) uczy się mięśni z: A. Bochenek, M. Reicher, *Anatomia człowieka*, t. I.
Zrobiliśmy wielki plakat A0 (PDF). Każdy mięsień ma kartę z poziomem ②: przyczepy (max 4 na stronę), czynność, części.
Teraz dobudowujemy **poziom ③ – szczegóły małym drukiem**, widoczne dopiero przy dużym przybliżeniu.
Zasada nadrzędna użytkownika: **wszystko w 100% z Bochenka. Jeśli coś w nauce jest inaczej niż w Bochenku – Bochenek ma rację.**
Użytkownik sprawdza fakty. Lepiej pominąć, niż napisać coś niepewnego.

## Źródła (tylko te)
- `/home/user/first-thing/all.txt` – OCR rozdziałów o mięśniach. Znacznik `=== BOOK PAGE n ===` otwiera tekst strony n książki.
  Numery linii (1-based) podajesz w polu `src`.
- Skan książki (do sprawdzania liczb i niejasnego OCR):
  `/tmp/claude-0/-home-user-first-thing/d41721b4-1413-50bf-8c94-691fa5e52b07/scratchpad/skan.pdf`
  W tym rozdziale strona PDF nr N to rozkładówka: lewa połowa = strona książki 2N+18, prawa = 2N+19
  (sprawdź numer w stopce). Renderowanie: `pdftoppm -r 150 -f N -l N -png "<skan>" /tmp/<nazwa>`,
  potem przytnij połówkę (PIL) i obejrzyj narzędziem Read. Zapisuj obrazki w /tmp, nie w /home/user/first-thing/plakat.
- `/home/user/first-thing/plakat/data.py` – co JUŻ jest na kartach (poziom ②): pola o (przyczep początkowy), i (końcowy), att,
  f (czynność), parts (części), sub (mięśnie składowe), note, extra, warn, omax. **Nie powtarzaj tego na poziomie ③.**
  (W polu `omax` jest np. „Bochenek podaje 7 przyczepów początkowych – tu wybrane 4” – brakujące przyczepy to dobry materiał na ③.)

**OCR psuje liczby** (np. „C,_;” zamiast zakresu segmentów, „Iniejszy”, „ż ebro”). **Każdą liczbę** (segmenty nerwów C/Th/L,
numery żeber i kręgów, procenty, wymiary) oraz każde niejasne słowo **sprawdź na skanie**. Nie zgaduj z wiedzy ogólnej.

## Co wchodzi na poziom ③ (przy każdym mięśniu, jeśli Bochenek to podaje)
Kategorie – pole `k` (dokładnie te napisy):
- `BUDOWA` – kształt, przebieg włókien, warstwy, ścięgna, z czego się składa (poza tym, co już jest w parts/sub)
- `POŁOŻENIE` – co go przykrywa, co on przykrywa, z czym graniczy, jakie tworzy trójkąty/szczeliny/brzegi
- `PRZYCZEPY – UZUPEŁNIENIE` – przyczepy pominięte na karcie (gdy było ich > 4) albo ważne szczegóły przyczepu
- `CZYNNOŚĆ – SZCZEGÓŁY` – tylko to, czego nie ma w polu f
- `UNERWIENIE` – dokładnie jak w Bochenku, z segmentami (sprawdzonymi na skanie)
- `ODMIANY` – najważniejsze odmiany / różnice osobnicze (max ~3 na mięsień, najczęstsze lub najbardziej znane)
- `UWAGI` – inne ważne rzeczy (np. znaczenie praktyczne, rozwój), jeśli Bochenek je podaje
- `!` – niezgodność w samym Bochenku (np. opis mięśnia vs streszczenie rozdziału) – podaj obie strony

Na mięsień zwykle 3–8 punktów. Nie dopisuj na siłę – jeśli Bochenek czegoś nie podaje, pomiń kategorię.

## Styl tekstu (ważne dla użytkownika)
- Po polsku, prostym językiem, styl notatki: krótkie równoważniki zdań, bez lania wody. Jeden punkt ≤ ~220 znaków.
- Tłumacz pozytywnie, czym coś jest. **Nie** używaj konstrukcji „to jest X, czyli NIE Y” i nie prostuj błędów, których nikt nie popełnił.
- Nie upychaj wielu nowych nazw w jednym zdaniu – lepiej dwa krótkie punkty.
- Łacińskie nazwy struktur/miejsc przyczepu, jeśli Bochenek je podaje, w podwójnych nawiasach kwadratowych:
  `wyrostek barkowy [[acromion]]` (render pokaże je małą czcionką w nawiasie).
- Zapis: m. / mm. / n. / nn. / ż. ; kręgi C1, Th12, L5 (bez indeksów dolnych); żebra cyframi rzymskimi (żebro XII);
  zakresy z półpauzą „–” (C3–C5, s. 653–654).
- Pole `pg` = strona(y) książki, z których pochodzi punkt (np. "653" albo "653–654").
- Pole `src` = zakres linii w all.txt (np. "202-205"), żeby dało się to szybko sprawdzić.

## Format wyniku – plik JSON (UTF-8), dokładnie taka struktura
```json
{
  "chapter": "<nazwa>",
  "muscles": {
    "<klucz mięśnia DOKŁADNIE jak w liście z zadania>": [
      {"k": "UNERWIENIE", "t": "…", "pg": "653", "src": "202-205"}
    ]
  },
  "groups": {
    "<tytuł grupy DOKŁADNIE jak w liście z zadania>": [
      {"k": "UNERWIENIE", "t": "…", "pg": "650", "src": "110-115"}
    ]
  },
  "panels": [
    {"id": "<id z zadania>", "title": "<tytuł>", "lat": "<łacina albo pusty>", "pg": "674–675",
     "items": [ {"k": "<krótki podtytuł WIELKIMI LITERAMI>", "t": "…", "pg": "674", "src": "1443-1450"} ]}
  ]
}
```
- `groups` – notatki o całej grupie (np. wspólne unerwienie, pochodzenie, wspólna czynność), tylko gdy Bochenek je podaje.
- `panels` – osobne tematy z rozdziału (lista w zadaniu); w panelu 6–14 punktów, podtytuły `k` dowolne, krótkie.
- Plik musi się wczytać przez `python3 -c "import json; json.load(open('<plik>'))"` – sprawdź to na końcu.
- Nie zmieniaj żadnych innych plików.

Na koniec odpowiedz krótko: ile punktów na mięsień/panel, jakie niezgodności w Bochenku znalazłeś, czego nie udało się odczytać.
