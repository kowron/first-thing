# Handoff C2 – przebudowa rozdziału na część 1 i część 2 według planu (Opus xhigh: wykonawca; 1 agent = 1 rozdział)

## Co robisz
Zleceniodawca postanowił, że podręcznik ma zawierać **wszystkie informacje z podanych źródeł**, podzielone w każdym rozdziale na:
- **część 1** (ok. 70% materiału) – wszystkie zagadnienia, najważniejsze w pełni, reszta tak, żeby ją rozumieć, bez szczegółów;
- **przejście** na końcu części 1;
- **część 2 – „na piątkę”** (ok. 30%) – rozszerzenie: szczegóły i informacje, których w części 1 nie ma. Mało rycin (żadnych nowych), dobre tłumaczenie, funkcja użytkowa.
Plan merytoryczny przygotował Fable: `plany/zNN-czesci.md` – **co gdzie idzie, z pełną treścią faktów do dopisania i stronami źródła**. Ty przebudowujesz plik i piszesz tekst. Źródeł nie czytasz (wyjątek: gdy plan jest niejasny albo fakt wygląda podejrzanie – wtedy sprawdź jedno miejsce i zanotuj).

**Skany Drewy:** przesunięcie stron w skanie nie jest stałe (+25 … +28 – sprawdź numer wydrukowany na wyrenderowanej stronie, zanim wyciągniesz wniosek).

## Przeczytaj
1. `STYL.md` – całe (tak samo piszesz część 2: definicja przed użyciem, po co → co → jak, każdy krok wynika z poprzedniego, nic nie wzmacniasz).
2. `KOMPONENTY.md` – zwłaszcza sekcję o części 2, przejściu, ramce „stare źródło” i zaślepce ryciny.
3. Plan: dla Z02 i Z03 – **`plany/zNN-czesci-skrot.md`** (skrót pełnego planu bez inwentarza; pełny plik tylko do sprawdzenia pojedynczej pozycji); dla pozostałych rozdziałów – `plany/zNN-czesci.md` (plan różnicowy: „Dopisać”, „Przesunąć”, „Uprościć”, „Sekcje części 2”, „Przejście”, „Błędy i decyzje”). Plan różnicowy nie wskazuje dokładnych akapitów ani brzmień – odszukanie miejsc w pliku i redakcja to Twoje zadanie. Jeśli fakt z „Dopisać” wydaje Ci się niejasny, sprawdź go w pakiecie `pakiety/zNN.txt` (sekcja E – źródła przycięte do zakresu), nie w pełnych źródłach.
4. Obecny rozdział `rozdzialy/zNN-*.html`.
5. Karta tego rozdziału w `RYCINY_do_ChatGPT.md` (miejsce, id, tytuł, proporcje, proponowany podpis zaślepki).

## Jak pracujesz
1. Skopiuj rozdział do `robocze/zNN-*.html` (ta sama nazwa) i tam pracuj; stan zapisuj w `stan/zNN-v3.md` (po każdej sekcji: co gotowe).
2. **Część 1:** wykonaj operacje z planu (pkt 3 planu: przenieś / uprość / dopisz). Nie ruszaj rycin (SVG, `data-bank`) ani ich podpisów (wyjątek: plan mówi, że podpis stałby się fałszywy). Wyjaśnienia zostają – tniesz szczegóły. Po uproszczeniu akapit ma nadal czytać się płynnie (sprawdź skoki między zdaniami). Popraw błędy A z planu (pkt 7). Wstaw zaślepkę ryciny z ChatGPT w miejscu z karty / planu (pkt 8): `figure.fig.placeholder` z id, `data-title`, proporcjami, szerokością i proponowanym podpisem. Ramka „stare źródło” (jeśli plan ją przewiduje) – na początku rozdziału, po `p.lead`.
3. **„W 60 sekund”** zostaje na końcu części 1 (zaktualizuj, jeśli coś z niego przeszło do części 2). Po nim **przejście** (tekst z planu, pkt 5).
4. **Część 2:** sekcje według planu (pkt 4). Każda sekcja zaczyna się od krótkiego nawiązania do części 1 z odsyłaczem `<a class="pageref" href="#cNN-…"></a>` (czytelnik wie, co już umie), potem szczegóły – z wyjaśnieniem, po co ten szczegół i jak się łączy z tym, co w części 1. Nie wyliczanka: jeśli jest lista, poprzedź ją zdaniem, co łączy jej elementy. Tabele dozwolone (gdy porządkują porównanie); ramki „Przykład” tylko, gdy naprawdę pomagają; rycin brak. Linie `p.src` na końcu sekcji, jak w części 1. Id w części 2 z prefiksem `cNN-r-…`.
5. **Kontrola:** każda pozycja „Dopisać” / „Plan części 2” jest w tekście, każde „Przesunąć” wykonane – sprawdź skryptem po słowach kluczowych/liczbach i ręcznie; nic spoza planu i obecnego tekstu; brak faktów spoza źródeł.
6. **Podmiana i build:** oryginał skopiuj do `/tmp/claude-0/-home-user-first-thing/600b873f-e07d-5766-b2f4-6a90b68ae091/scratchpad/archiwum-v2/`, plik z `robocze/` przenieś do `rozdzialy/`; `node build.mjs --only NN --png` – 0 BŁĄD/UWAGA; obejrzyj arkusz miniatur i 2–3 strony (w tym początek części 2). Maks. 6 buildów. W `stan/zNN-v3.md`: „GOTOWE”, strony przed → po (część 1 / część 2).

Proporcje: część 1 po przesunięciach zwykle trochę krótsza niż obecny rozdział; część 2 – tyle, ile potrzeba na komplet informacji z dobrym tłumaczeniem (orientacyjnie 30–50% objętości części 1).
Po przerwaniu limitem: nowy agent czyta ten handoff, `stan/zNN-v3.md` i plik w `robocze/` – i kontynuuje.
Nie commituj. Nie ruszaj innych rozdziałów, `css/`, `lib/`, `build.mjs`.

## Raport (maks. 10 linijek)
Strony przed → po (cz. 1 / cz. 2); ile informacji przeniesiono, ile dopisano; czy wszystko z inwentarza jest; wątpliwości; czy coś niedokończone.
