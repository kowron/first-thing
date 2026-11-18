# Handoff P – przepisanie rozdziału w stylu „podręcznik, który uczy” (Opus, 1 agent = 1 rozdział)

## Dlaczego to robimy
Zleceniodawca ocenił rozdziały 2–11 jako „druga Drewa”: poprawne fakty, ale napisane tak, jakby czytelnik wszystko już wiedział – pojęcia używane przed wyjaśnieniem, kroki procedur bez „dlaczego”, metody bez „po co”. Przykład krytyki (dosłownie z jego uwag): *„Zanim pojawiły się STR, osoby identyfikowano analizą RFLP minisatelitów” – czytelnik nie wie, czym jest STR, co znaczy identyfikacja osoby, czym jest RFLP ani minisatelita, a zdanie już mówi, że minisatelita „miał dwie wersje”. I tak jest w co drugim akapicie.*
Rozdział 6 został przepisany i zaakceptowany („w miarę okej”) – to Twój **wzorzec**.

## Przeczytaj najpierw (w tej kolejności)
1. `/home/user/first-thing/podrecznik/STYL.md` – całe; to najważniejszy dokument.
2. `/home/user/first-thing/podrecznik/PORADNIK_jak_pisac.txt` – strony 5–11 (dobór początku akapitu, redakcja zdania, podpis ryciny, przebudowa źródła, kontrola).
3. Wzorzec: `rozdzialy/z06-elektroforeza-hybrydyzacja.html` – przeczytaj podrozdziały „Hybrydyzacja i sondy”, „Southern…” i „Identyfikacja genetyczna: układy STR” (to one były krytykowane i przepisane).
4. `ZASADY.md` (zasady źródłowe: tylko źródła z rozpiski, stary Jorde jako źródło pomocnicze, format) i `KOMPONENTY.md` (komponenty HTML; dostępne ramki: `box zapamietaj`, `box uwaga`, `box obraz`, `box przyklad`, notatka `aside.note pojecie`, `div.w60`).

## Materiały Twojego rozdziału
- **Obecny rozdział**: `rozdzialy/zNN-*.html` – źródło faktów, rycin (SVG) i tabel. Tekst piszesz od nowa; ryciny i tabele zostają (możesz poprawić podpisy według STYL.md).
- **Handoff rozdziału** `handoff/ZNN.md` – mapa zakresu (które podrozdziały źródła, co zostaje, co tniemy). Zakres i podział na zagadnienia nadal obowiązują.
- **Wyciąg** `wyciagi/zNN.md` – fakty ze stronami i decyzją Z (zostaje) / T (ucięte).
- **Rewizja** `rewizja/zNN.md` (jeśli istnieje) – poprawki recenzenta: A = błąd, B = fakt do przywrócenia, C = kosmetyka. Jeśli plik ma sekcję „Naniesiono” – są już w obecnym rozdziale; jeśli nie – **wpleć wszystkie A i B w nowy tekst** (C gdy sensowne).
- **Źródła** (do sprawdzania faktów, przywracania i rozumienia – czytaj tylko fragmenty z mapy): wskazane w części szczegółowej zlecenia.

## Jak pracujesz
1. **Plan (zapisz w `stan/zNN-v2.md`)**: dla każdego podrozdziału h2 – (a) co student ma umieć po lekturze (wyjaśnić mechanizm / wybrać metodę / zrozumieć model / rozpoznać), (b) jakie pojęcia są potrzebne, w jakiej kolejności je wprowadzisz, (c) które pojęcia pochodzą z innych rozdziałów (krótkie przypomnienie 1–3 zdaniami + `chapref`), (d) gdzie daś ramkę „Przykład” z rozumowaniem krok po kroku. Nowa kolejność podrozdziałów jest dozwolona, jeśli wynika z zależności pojęciowych.
2. **Pisanie**: podrozdział po podrozdziale; po każdym h2 dopisz linijkę do `stan/zNN-v2.md` (co gotowe). Piszesz do pliku roboczego `robocze/zNN-*.html` (ta sama nazwa co oryginał, inny katalog – build go nie czyta). Gdy cały tekst jest gotowy, podmieniasz oryginał (pkt 5). Plik w `rozdzialy/` z tym samym numerem może być tylko jeden, bo inaczej build zobaczy dwa rozdziały.
3. **Zasady treści** (bez wyjątków):
   - fakty, liczby, nazwy – tylko ze źródeł rozdziału i zgodne z nimi; objaśnienia logiczne („po co”, „dlaczego”) dozwolone, nowe fakty – nie; nie wzmacniaj twierdzeń źródła;
   - tniemy 10–30% **informacji** (handoff/wyciąg mówią co), **nigdy wyjaśnień**; fakty B z rewizji wracają;
   - **żadnych pytań kontrolnych** ani quizów;
   - ramki „Obraz w głowie” tylko z analogią, która ma nazwaną wspólną zależność; liczby przykładowe oznaczone;
   - objętość: bez sztywnego limitu; rozdział 6 urósł 1,7× – spodziewaj się podobnie; nie więcej niż 2× obecnej liczby stron.
4. **Ryciny**: zachowaj istniejące (to inline SVG – przenieś je bez zmian geometrii). Popraw podpisy: od czego zacząć oglądanie, co porównać, jaki wniosek. Nową rycinę (maks. 2 na rozdział) narysuj tylko tam, gdzie kluczowy mechanizm nie ma ryciny, a obraz pozwala odczytać zależność – w stylu i klasach istniejących rycin.
5. **Kontrola i podmiana**:
   - porównaj z wyciągiem: każdy fakt Z jest w tekście; każdy fakt B z rewizji jest w tekście; brak faktów spoza źródeł;
   - test najtrudniejszego akapitu (STYL.md) dla 2–3 akapitów; popraw kolejność, jeśli trzeba;
   - podmień: oryginał skopiuj do `/tmp/claude-0/-home-user-first-thing/600b873f-e07d-5766-b2f4-6a90b68ae091/scratchpad/archiwum-v1/`, a plik z `robocze/` przenieś w jego miejsce do `rozdzialy/`; `node build.mjs --only NN --png` – 0 BŁĄD/UWAGA; obejrzyj arkusz miniatur (montage) i 2–3 strony w pełnej rozdzielczości; maks. 5 buildów;
   - w `stan/zNN-v2.md` wpisz „GOTOWE” + liczba stron przed → po.
6. Po przerwaniu (limit): nowy agent czyta ten handoff, `stan/zNN-v2.md` i plik w `robocze/` – i kontynuuje od ostatniego gotowego podrozdziału. Nie zaczyna od nowa.

Nie commituj. Nie ruszaj innych rozdziałów, `css/`, `lib/`, `build.mjs`.

## Raport (maks. 12 linijek)
Strony przed → po; nowe ryciny; które poprawki z rewizji wplecione; 3 przykłady „było → jest” pokazujące największą zmianę w tłumaczeniu; wątpliwości źródłowe; czy coś zostało niedokończone.
