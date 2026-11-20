# Handoff R3-W – weryfikacja zgłoszeń recenzentów (Fable medium, 1 agent na cały podręcznik)

Sześciu recenzentów (Sonnet) zgłosiło wszystko, co podejrzane: `rewizja3/z01.md` … `z11.md`, `front.md` (razem ok. 580 pozycji, ok. 210 KB). Mieli zgłaszać z nadmiarem. Ty **potwierdzasz albo odrzucasz** każdą pozycję i wypisujesz potwierdzone błędy do jednego pliku. Plików rozdziałów NIE zmieniasz.

## Budżet
Pracuj rozdział po rozdziale: przeczytaj raport, a do pakietu `pakiety/zNN.txt` (D = aktualny tekst, E = źródła) zaglądaj punktowo (Grep/Read fragmentu), tylko gdy pozycji nie da się rozstrzygnąć z samego opisu. Nie czytaj pakietów w całości. Skan Drewy (`/tmp/claude-0/-home-user-first-thing/600b873f-e07d-5766-b2f4-6a90b68ae091/scratchpad/dropbox/Drewa - Genetyka medyczna.pdf`, przesunięcie stron +25…+28) tylko dla błędów merytorycznych, których nie rozstrzygniesz inaczej (maks. ok. 10 stron łącznie). Po każdym rozdziale dopisuj wynik do pliku (odporność na przerwanie).

## Ustalenia, które obowiązują (zgłoszenia sprzeczne z nimi – ODRZUĆ bez sprawdzania)
- Limity stron i liczby rycin z map (sekcja B) są nieaktualne; układ część 1 + część 2 i dodatkowe ryciny (w tym 12 rycin PNG z ChatGPT) – celowe.
- Fakty „Tniemy” / „poza planem mapy” wróciły celowo do części 2 (komplet źródeł), także opisy rycin i tabel źródła odczytane ze skanu (recenzenci widzieli tylko OCR – jeśli zarzut brzmi „nie da się zweryfikować w OCR / liczba inna niż w OCR”, a wykonawca odnotował odczyt ze skanu w `stan/zNN-v3.md` – odrzuć; sprawdź `grep` w tym pliku stanu).
- Z06: elektroforeza białek, przypomnienie ddNTP, wprowadzenie do STR i ojcostwa (s. 765–768, 779) – zostają na życzenie zleceniodawcy. Z02: „Zaburzenia mejozy” zostają. Z04/Z05: podstawy z materiału pomocniczego (PCR: temperatury, Mg²⁺ itd.) zostają; mechanizm ASA zostaje jako wyjaśnienie.
- Z08, Z10: zagadnienia Jordego pisane według Jordego (wyd. ok. 2000) – celowe. Z07: ramka Twymana – celowa. Wzmianki „wg rozpiski” (aksolotl, Bar, Chironomus, Giemsa) – zostają.
- Meta-komentarze w części 2 typu „źródło tego nie podaje” – dopuszczalne, jeśli krótkie; ramka „Sprawdź się” / pytania kontrolne – BŁĄD (zakaz quizów) → do usunięcia lub przeredagowania na ramkę „Przykład”.
- Nazwisk z błędną pisownią w źródle (Singer/Signer, Tijo/Tjio) nie podajemy.
- Definicje słów, objaśnienia logiczne i przykłady oznaczone jako przykładowe – dozwolone; fakt spoza źródeł podany jak fakt – błąd (usunąć lub złagodzić). Rozdz. 4: szczegóły z dawnych opracowań (k4), których nie ma w źródłach E – usuń lub sprowadź do źródła, chyba że to pół zdania potrzebne do odczytania istniejącej ryciny.

## Wynik: `rewizja3/POTWIERDZONE.md`
Dla każdego rozdziału (i front):
**A. TEKST – do wklejenia przez Sonneta** (on nie myśli – wkleja). Każda poprawka jako blok:
```
### zNN-k  (pozycja raportu nr …; M/Z/J)
PLIK: rozdzialy/zNN-….html
ZNAJDŹ: <dokładny, unikalny fragment obecnego tekstu – skopiowany z pliku HTML (sprawdź grep -c = 1), możliwie krótki>
ZAMIEŃ NA: <nowy fragment (HTML jak w pliku); „(USUŃ)” gdy fragment ma zniknąć>
```
Fragment ZNAJDŹ bierz z pliku `rozdzialy/…html` (nie z pakietu – pakiet nie ma znaczników HTML). Pisz w stylu podręcznika (STYL.md), niczego nie wzmacniaj.
**B. SKŁAD / RYCINY / UKŁAD – dla Opusa** (on umie myśleć – wystarczy 1 linijka na pozycję: miejsce + co nie tak). Tu także: błędy w stylu tabel (np. nagłówki zamieniane na wielkie litery psują „Dd”, „n”), strona „Jak korzystać” (nieaktualna zaślepka, brak opisu ramek „Przykład” i „Obraz w głowie”), brak wykazu źródeł (rozwinięcie skrótów Drewa, Jóźwiak, Jorde, Ostrowska, Alster–Korwek, Twyman – dane z rozpisek w pakietach, sekcja A), podtytuł okładki, błędy w rycinach SVG (np. liczba kroków na rycinie ≠ lista), rycina nieprzywołana w tekście.
**C. ODRZUCONE** – tylko liczba na rozdział i 3–5 słów o głównych powodach (nie wypisuj pozycji).
**D. DO DECYZJI ZLECENIODAWCY** – najwyżej 10 pozycji na cały podręcznik, po jednej linijce.

Nie commituj. Raport końcowy (maks. 10 linijek): liczby zgłoszeń / potwierdzonych (tekst, skład) / odrzuconych na rozdział, 5 najpoważniejszych potwierdzonych błędów.
