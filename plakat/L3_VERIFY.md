# Kontrola poziomu ③ – instrukcja dla sprawdzającego

Masz sprawdzić punkty w pliku JSON z poziomem ③ plakatu (szczegóły z: A. Bochenek, M. Reicher, *Anatomia człowieka*, t. I).
Użytkownik (student medycyny) sprawdza fakty i wymaga, żeby **wszystko zgadzało się z Bochenkiem**. Ty tych punktów nie pisałeś – oceniaj je świeżym okiem.

## Źródła
- `/home/user/first-thing/all.txt` – OCR książki; znacznik `=== BOOK PAGE n ===` otwiera stronę n. Każdy punkt ma pole `src` (zakres linii) i `pg` (strona).
- Skan: `/tmp/claude-0/-home-user-first-thing/d41721b4-1413-50bf-8c94-691fa5e52b07/scratchpad/skan.pdf`
  Strona PDF N = rozkładówka: lewa połowa = strona książki 2N+18, prawa = 2N+19. Render: `pdftoppm -r 150 -f N -l N -png "<skan>" /tmp/v_<nazwa>`,
  przytnij połówkę (PIL), obejrzyj narzędziem Read. OCR często psuje liczby i indeksy (np. „C,_;”).

## Co sprawdzasz w każdym punkcie
1. Czy treść wynika z tekstu Bochenka we wskazanych liniach (`src`) / na stronie `pg`? Nic dopisanego z wiedzy ogólnej.
2. **Liczby i oznaczenia** (segmenty nerwów C/Th/L, numery żeber/kręgów, procenty, wymiary) – zawsze porównaj ze skanem.
3. Czy strona `pg` jest właściwa.
4. Nazwy łacińskie w `[[...]]` – czy tak są w Bochenku (bez literówek z OCR).
5. Czy sens nie został odwrócony/przekręcony (np. „przyśrodkowo” ↔ „bocznie”, „górny” ↔ „dolny”).
Styl i długość zostaw – oceniasz tylko poprawność.

## Wynik
Zapisz plik JSON pod wskazaną ścieżką:
```json
{"checked": <liczba sprawdzonych punktów>,
 "issues": [
   {"where": "muscles/<klucz> #<indeks od 0>"  albo "groups/<tytuł> #i"  albo "panels/<id> #i",
    "problem": "co jest źle (krótko)",
    "fix_t": "poprawiony tekst punktu (cały) albo null, jeśli punkt należy usunąć",
    "fix_pg": "poprawna strona albo null, jeśli bez zmian",
    "evidence": "co jest w Bochenku – krótki cytat ze skanu/OCR + strona"}
 ]}
```
Zgłaszaj tylko realne błędy. Na koniec odpowiedz krótko: ile punktów sprawdzonych, ile błędów, jakie najpoważniejsze.
