# Handoff F0A – przygotowanie źródeł (Opus, 1 agent)
Cel: każdy agent rozdziału dostaje małą paczkę czystego tekstu tylko ze swoich źródeł. Nie piszesz treści podręcznika.

## Wejście
- Folder z Dropboxa rozpakowany w `/tmp/claude-0/-home-user-first-thing/600b873f-e07d-5766-b2f4-6a90b68ae091/scratchpad/dropbox/` (jeśli katalogu nie ma – poproś zleceniodawcę o link i pobierz: `curl -L "<link>&dl=1" -o folder.zip`, rozpakuj bez pliku „Anatomia…”).
- Drewa – gotowy OCR wybranych rozdziałów: `/root/.claude/uploads/600b873f-e07d-5766-b2f4-6a90b68ae091/b95214fd-Drewa_Genetyka_medyczna_OCR.txt` (strony `[Strona N]`; początki rozdziałów: r3 l.36, r7 l.8075, r8 l.9744, r18 l.14381, r20 l.17599, r26 l.29034, r27 l.29527, r28 l.32311, r29 l.33696, r30 l.36567, r35 l.42727).
- Rozpiski zajęć jako tekst: `/tmp/claude-0/-home-user-first-thing/600b873f-e07d-5766-b2f4-6a90b68ae091/scratchpad/dropbox/syl/zNN.txt`.

## Zadania
1. **OCR** (zainstaluj tesseract z językiem polskim i angielskim: `apt-get install -y tesseract-ocr tesseract-ocr-pol`; jeśli instalacja jest zablokowana – zgłoś i przerwij, nie czytaj skanów „oczami”):
   - „Drewa – Genetyka medyczna.pdf” (963 s., skan): tylko rozdziały 2, 10, 12, 13, 16. Znajdź ich strony PDF w spisie treści (OCR kilku pierwszych stron), wytnij strony `pdftoppm -r 200`, OCR, wstaw znaczniki `[Strona N]` z numeracją książki.
   - „pdf24_przekonwertowany (2).pdf” – Jorde, rozdz. 5 (24 zrzuty ekranu tabletu: przytnij do obszaru strony książki, podwójne strony rozdziel).
   - „pdf24_przekonwertowany.pdf” – Twyman, sekcja M3 (7 zrzutów, angielski).
   Sprawdź jakość na 3 losowych stronach z każdego źródła (porównaj z obrazem); słabe strony powtórz w wyższej rozdzielczości.
2. **Paczki** – utwórz `/tmp/claude-0/-home-user-first-thing/600b873f-e07d-5766-b2f4-6a90b68ae091/scratchpad/zrodla/zNN/` z plikami txt zawierającymi wyłącznie zakres danego rozdziału (zachowaj znaczniki stron):
   - z02: Drewa r.7; Jóźwiak r.6
   - z03: Drewa r.8; Jóźwiak r.11; Alster–Korwek (`o2592 (1).pdf`, pdftotext)
   - z04: Drewa r.3 s.28–34, 37–45, 48–55; r.18 s.431–432; r.27 s.710–712; Ostrowska s.53–54, 56
   - z05: Ostrowska s.54–64; Drewa r.27 s.703–705, 725, 732–735
   - z06: Drewa r.27 s.712–718, 730–732; r.29 s.769–774, 780–782
   - z07: Jóźwiak r.9 + podpisy ryc. 10.7 i 10.8 z r.10; Drewa r.26; Twyman M3
   - z08: Drewa r.2, 10, 12, 13, 16; Jorde r.5 (część o dziedziczeniu mitochondrialnym); Materiał pomocniczy do zajęć 8
   - z09: Drewa r.18
   - z10: Drewa r.18 (podrozdziały o chromosomach płci i chromatynie płciowej), r.20 (podrozdziały o determinacji płci/gonady); Jorde r.5 (dziedziczenie sprzężone z płcią, cechy ograniczone i związane z płcią)
   - z11: Drewa r.28, 30, 35
   Jóźwiak ma warstwę tekstu (`pdftotext`), tnij po nagłówkach rozdziałów; Ostrowska też.
   W każdej paczce dodaj `ROZPISKA.txt` (zagadnienia z rozpiski) i `SPIS.md`: pliki, zakres stron, liczba znaków, przy każdym zagadnieniu – w którym pliku i na których stronach jest omówione (na podstawie nagłówków podrozdziałów; nie czytaj całej treści).
   W `SPIS.md` paczek z08 i z10 oznacz plik Jordego: „STARE WYDANIE (ok. 2000) – źródło pomocnicze, pierwszeństwo ma Drewa” i wypisz, które zagadnienia są omówione także w Drewie.
3. Zapisz `/tmp/claude-0/-home-user-first-thing/600b873f-e07d-5766-b2f4-6a90b68ae091/scratchpad/zrodla/INDEX.md` (paczka → pliki → rozmiar) i wpisz braki źródeł.

## Wynik i stan
Stan po każdym źródle dopisuj do `/home/user/first-thing/podrecznik/stan/F0A.md`. Raport ≤ 12 linijek: co zrobione, jakość OCR, braki. Tekstów źródłowych nie commituj (prawa autorskie) – zostają w scratchpadzie.
