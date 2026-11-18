# Handoff C1 – plan podziału rozdziału na dwie części (Fable xhigh: merytoryka i plan; 1 agent = 1 rozdział)

## Decyzja zleceniodawcy (18.11.2026, wieczór)
Podręcznik ma zawierać **wszystkie informacje z podanych źródeł** (w zakresie zagadnień z rozpiski zajęć – patrz niżej). Żeby dało się z niego uczyć, każdy rozdział dzieli się na dwie części:
- **Część 1 (ok. 70% materiału)** – wszystkie zagadnienia z rozpiski, ale: (1) najważniejsze rzeczy **w pełni**, (2) pozostałe **tak, żeby je rozumieć**, bez szczegółów. To jest obecny rozdział po przepisaniu (styl STYL.md) – po przesunięciu części szczegółów do części 2.
- Na końcu części 1 – **przejście** do części 2.
- **Część 2 (ok. 30% materiału) – „część na 5”**: rozszerzenie informacji z części 1 – wszystko, czego w części 1 nie ma lub jest tylko zarysowane, aż do kompletu źródła. Mało rycin (żadnych nowych), dużo dobrego tłumaczenia; funkcja użytkowa, nie wizualna. Czyta ją mniej osób.
- **Ryciny się nie zmieniają.**

Ty piszesz **plan i merytorykę** (co gdzie, z jakim brzmieniem faktu i stroną). Wykonawca (Opus) przebuduje plik HTML według Twojego planu i napisze tekst – **nie będzie czytał źródeł**, więc wszystko, czego potrzebuje, musi być w planie.

## Uniwersum informacji = „podane źródła”
- Zakres = fragmenty źródeł przypisane do zagadnień z rozpiski zajęć: mapa w `handoff/ZNN.md` (kolumny „Źródło”, „Zostaje”, „Tniemy”). **Wszystko, co było w kolumnie „Tniemy” i w wyciągu oznaczone T, teraz wraca – do części 2** (chyba że to oczywisty balast bez wartości informacyjnej: powtórzenie, odesłanie do ryciny, której nie mamy, piśmiennictwo, pytania kontrolne źródła).
- Sekcje opisane w mapie jako „Poza zakresem” (tematy, których nie ma w rozpisce zajęć) – **dalej poza podręcznikiem**. Jeśli uważasz, że któraś z nich jednak odpowiada zagadnieniu z rozpiski (`zrodla/zNN/ROZPISKA.txt`) – zapisz to jako decyzję do zatwierdzenia, nie włączaj.
- Stary Jorde (ok. 2000/2001) – jak dotąd: tylko to, czego nie ma w Drewie do tych samych zajęć (ZASADY pkt 9).

## Materiały
- Rozdział (już przepisany, styl do zachowania): `rozdzialy/zNN-*.html`
- Mapa zakresu: `handoff/ZNN.md` (G: `handoff/G.md`); wyciąg `wyciagi/zNN.md`; stan autora `stan/zNN-v2.md` (G: `stan/g-v2.md`) – sekcje wątpliwości; rewizje `rewizja/zNN.md` (i `zNN-v2.md`, jeśli są).
- Źródła: paczka `/tmp/claude-0/-home-user-first-thing/600b873f-e07d-5766-b2f4-6a90b68ae091/scratchpad/zrodla/zNN/` (`SPIS.md`, `ROZPISKA.txt`); Drewa OCR `/root/.claude/uploads/600b873f-e07d-5766-b2f4-6a90b68ae091/b95214fd-Drewa_Genetyka_medyczna_OCR.txt` (zakresy linii w mapie); skan Drewy `…/scratchpad/dropbox/Drewa - Genetyka medyczna.pdf` (strona PDF = strona książki + 28); Z04/Z05 – też `material/k4.txt`, `material/k5.txt` (opracowania, z których powstały); G – `material/genomika.txt` (jedyne źródło).
- Zasady: `STYL.md`, `ZASADY.md`. Spis rycin do zamówienia: `RYCINY_do_ChatGPT.md` (karta dla tego rozdziału – miejsce ryciny musi zostać w części 1).
- **Tym razem przeczytaj przypisane fragmenty źródeł w całości** – celem jest komplet informacji.

## Co oddajesz: `plany/zNN-czesci.md`
1. **Bilans** (5–10 linijek): objętość źródła w zakresie; co z niego jest w obecnym rozdziale (szacunek %); co dochodzi; docelowy podział informacji ≈ 70/30.
2. **Inwentarz źródła** – podrozdział po podrozdziale źródła, lista jednostek informacji (fakt, definicja, etap, liczba, przykład, klasyfikacja, wyliczenie). Przy każdej:
   - decyzja: **P1** (w części 1 w pełni) / **P1u** (w części 1 w uproszczeniu – napisz, co zostaje w części 1, a jaki szczegół idzie do części 2) / **P2** (tylko w części 2);
   - stan: **jest** (gdzie: id h2/h3 + pierwsze słowa akapitu) / **brak** (do dopisania – podaj pełną treść po polsku, wiernie wobec źródła, ze stroną);
   - strona źródła.
   Kryterium P1: definicje, mechanizmy, klasyfikacje, etapy, to, o co pytają sformułowania zagadnień w rozpisce, i wszystko, bez czego nie da się zrozumieć reszty. P2: szczegółowe wyliczenia, dodatkowe przykłady, liczby i masy, nazwy mniej ważnych białek/genów, wyjątki, warianty metod, szczegóły techniczne, historia (jeśli nie jest bezwartościowa).
3. **Zmiany w części 1** – lista konkretnych operacji na obecnym tekście: `id + pierwsze słowa` → **przenieś do części 2** (sekcja X) / **upraszczaj do:** „proponowane brzmienie” / **dopisz:** treść (gdy fakt P1 jest „brak”). Część 1 ma nadal czytać się płynnie: wyjaśnień nie wycinaj, tniesz szczegóły. Ryciny zostają, gdzie są (jeśli podpis ryciny w części 1 odwołuje się do szczegółu przeniesionego do części 2 – zaznacz to; podpisu nie zmieniamy, chyba że byłby fałszywy).
4. **Plan części 2** – sekcje `h2` w kolejności części 1 (tytuł w stylu „Cykliny – szczegóły” albo pytanie), dla każdej: z którą sekcją części 1 się łączy (id – wykonawca da odsyłacz `pageref`), lista informacji (przeniesione z części 1 / nowe ze źródła – pełna treść ze stroną), wskazówka tłumaczenia (jaki problem rozwiązuje ten szczegół, jak go powiązać z częścią 1), czy tabela pomoże. Rycin w części 2: zero nowych; istniejących nie przenosimy.
5. **Przejście** – propozycja tekstu (2–4 zdania: dla kogo jest część 2 i co rozszerza) + lista sekcji części 2.
6. **Czerwona ramka „stare źródło”** – jeśli rozdział opiera się (choćby częściowo) na starym wydaniu (Jorde ok. 2000/2001; Twyman – wyd. ang. 2001, w rozpisce tłumaczenie PWN 2003): proponowany tekst ramki (2–3 zdania: które części rozdziału, że wydanie jest stare, że tam, gdzie to samo jest w Drewie/Jóźwiaku, pierwszeństwo miało nowsze źródło). Sprawdź rok w pliku źródła.
7. **Wierność obecnego tekstu** (przy okazji czytania źródeł): błędy A (fakt spoza źródeł, sprzeczność, wzmocnione twierdzenie) z poprawką; rozstrzygnięcia wątpliwości autora ze `stan/zNN-v2.md`; linie „Źródło: …” wskazujące strony spoza rozpiski.
8. **Miejsce ryciny z ChatGPT** (z `RYCINY_do_ChatGPT.md`): potwierdź, że akapit-kotwica zostaje w części 1; jeśli przenosisz go do części 2 – wskaż nowe miejsce w części 1.

Plan pisz zwięźle (tabele, listy), ale treść faktów do dopisania – pełnymi zdaniami gotowymi do przeredagowania. Nie zmieniaj plików rozdziałów. Nie commituj.
Raport (maks. 8 linijek): bilans 70/30, ile informacji dochodzi, 3 najważniejsze decyzje, błędy A, ramka tak/nie.
