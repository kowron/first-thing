# Rysunki do plakatów anatomicznych – instrukcja

## Po co
Student medycyny uczy się szkieletu osiowego z polskiego podręcznika Bochenka. Robimy plakaty A0 (PDF, wektorowe, z przybliżaniem).
Potrzebne są **własne, oryginalne, schematyczne rysunki** – czyste, ładne, czytelne, z podpisami PL + łac.
**Nie kopiujesz żadnych ilustracji** (Bochenek, Netter, internet). Ryciny Bochenka ze skanu możesz oglądać tylko po to,
żeby zrozumieć kształt i położenie struktur – rysujesz po swojemu, uproszczony schemat.

## Narzędzia (używaj tylko ich)
- `/home/user/first-thing/plakat/figs/figlib.py` – klasa `Fig` + funkcje `smooth()` (gładki kontur przez punkty), `mirror()` (odbicie połowy
  konturu względem osi – do kształtów symetrycznych), `shift()`. Przeczytaj nagłówek pliku: lista klas stylu (bone, facet, cart, lig,
  annulus, nucleus, capsule, cavity, muscle, tendon, nerve, artery, vein, organ, hole, shade, arrow, arrow2, axis, dim, note…).
  **Używaj wyłącznie tych klas** – kolory i grubości są wspólne dla wszystkich rysunków. Nie dodawaj własnych kolorów ani czcionek.
- Podpisy wyłącznie przez `f.label((x, y), 'nazwa polska', 'nomen latinum', (tx, ty), side='L'|'R')` – kropka na strukturze,
  linia z łamaniem, tekst PL (pogrubiony) i pod nim łacina (kursywa). Strzałki ruchu: `f.arrow('M… Q…')` (niebieska) lub `red=True`.
  Krótkie napisy w rysunku (np. „wdech”, „L3”): `f.text(x, y, 'tekst', cls='note'|'notec'|'big')`.
- Jednostka = 1 mm na plakacie (rysunek wstawiany w skali 1:1). Czcionki podpisów są stałe (≈ 7 pt) – nie zmieniaj ich.
- Wzór stylu: `/home/user/first-thing/plakat/figs/src/wzor_th_gora.py` → `figs/png/wzor_th_gora.png` (obejrzyj go najpierw).
- Każdy rysunek = osobny plik `figs/src/<nazwa>.py`, który zapisuje `figs/out/<nazwa>.svg` (f.save()).
- Podgląd: `cd /home/user/first-thing/plakat/figs && python3 preview.py <nazwa>` → `figs/png/<nazwa>.png` – **obejrzyj go narzędziem Read po
  każdej większej zmianie** i poprawiaj, aż będzie dobrze.

## Konwencje
- Widok od góry: przód (brzuszna strona) ku górze rysunku. Widok z boku: przód w lewo. Widok od przodu: prawa strona ciała po lewej stronie
  rysunku (jak u stojącego naprzeciw człowieka). Widok od tyłu: odwrotnie. Przekroje: podpisz, jaki to przekrój.
- `caption` w `Fig(...)`: krótki opis widoku, np. „kręg szczytowy (C1) · widok od góry”.
- Szerokość płótna zwykle 110–150 mm, wysokość według potrzeb (60–110 mm). Kształt w środku, podpisy po bokach (lewa kolumna tekstu
  wyrównana do prawej, prawa do lewej), w razie potrzeby także pod/nad rysunkiem. Zostaw ~2 mm marginesu – nic nie może wychodzić poza płótno.
- 6–14 podpisów na rysunek. Linie podpisów nie mogą się krzyżować ani przechodzić przez inne napisy; teksty nie mogą na siebie nachodzić.
- Kształty gładkie (`smooth`), proporcje możliwie wierne anatomii, symetria tam, gdzie jest w naturze (`mirror`). Delikatny cień (`shade`)
  wolno użyć dla głębi, bez przesady. Powierzchnie stawowe – klasa `facet`; chrząstka – `cart`; więzadła – `lig`.
- Nazwy PL i łac. **dokładnie jak w Bochenku** – sprawdzaj w OCR (`/home/user/first-thing/bones.txt` – kości i połączenia; `/home/user/first-thing/all.txt` – mięśnie,
  przepona, oddychanie) i na skanie, gdy łacina w OCR wygląda podejrzanie:
  `/tmp/claude-0/-home-user-first-thing/d41721b4-1413-50bf-8c94-691fa5e52b07/scratchpad/skan.pdf`
  (render: `pdftoppm -r 120 -f N -l N -png "<skan>" /tmp/<katalog>/x`; obrazki trzymaj w /tmp/<katalog>, nie w katalogu plakatu).
  Jeśli w `/home/user/first-thing/plakat/k_*.json` są już listy `labels` dla Twojej karty – użyj tych nazw.

## Jakość
To ma być „ładne graficznie” – jak dobre schematy w podręczniku: czysto, bez bałaganu, czytelne z bliska. Lepiej mniej podpisów, ale
porządnie rozłożonych. Każdy rysunek oglądnij w podglądzie przynajmniej 2 razy (po pierwszej wersji i po poprawkach).

Na koniec odpowiedz krótko: lista rysunków (nazwa pliku, co przedstawia, rozmiar w mm), co było trudne, czego nie jesteś pewien.

## Skan – numeracja stron (POPRAWIONE)
Skan: /tmp/claude-0/-home-user-first-thing/d41721b4-1413-50bf-8c94-691fa5e52b07/scratchpad/skan.pdf (458 stron PDF). Jedna strona PDF = dwie strony książki (lewa = parzysta, prawa = nieparzysta).
**Numer strony PDF dla danej strony książki bierz ze znaczników `=== PDF N-0 ===` / `=== PDF N-1 ===` w `bones.txt`** (N = numer strony PDF,
-0 = lewa, -1 = prawa połowa; np. s. 276–277 = PDF 123, s. 278–279 = PDF 124, s. 290–291 = PDF 129) – to jest pewne. W skanie brakuje s. 288–289, 6–55
i 646–647, więc stały wzór na numerację NIE działa w całej książce (działa tylko blisko s. 700–720: PDF 344 = s. 706–707). Zawsze sprawdź numer w stopce
wyrenderowanej strony.
Render: pdftoppm -r 110 -f N -l N -png "/tmp/claude-0/-home-user-first-thing/d41721b4-1413-50bf-8c94-691fa5e52b07/scratchpad/skan.pdf" <katalog_w_scratchpadzie>/x
