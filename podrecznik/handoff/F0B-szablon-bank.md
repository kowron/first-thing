# Handoff F0B – szablon dwukolumnowy i bank rycin (Opus, 1 agent)
Nie piszesz treści rozdziałów.

## A. Szablon
Baza: działający system składu w `/home/user/first-thing/kolokwium6/` (`build.mjs`, `lib/`, `css/style.css`, `fonts/`, `KOMPONENTY.md`; natywny druk Chromium przez Playwright – nic nie instaluj). Skopiuj go do `/home/user/first-thing/podrecznik/` i przerób:
- A4, **tekst rozdziału w dwóch kolumnach** (bez kolumny marginesowej); otwarcie rozdziału, ryciny, szerokie tabele i „W 60 sekund” na obie kolumny (`column-span: all`); mała rycina/tabela może stać w jednej kolumnie (`fig narrow`).
- **Kolor przewodni: zielony** (decyzja zleceniodawcy) zamiast granatu i turkusu: okładka ciemnozielona, akcenty (kreski, numery rozdziałów, h3, punktory, nagłówki tabel, plakietki) w odcieniach zieleni; dobierz spójną, czytelną paletę i zamień zmienne kolorów w CSS oraz klasy kolorów SVG tak, by ryciny z banku nie wymagały przerabiania (ryciny z gotowych PDF-ów zostają w swoich kolorach).
- Pismo mniejsze niż w kolokwium 6 (cel: ok. 5000 znaków tekstu na stronę), czytelne.
- „Pojęcie” jako mała ramka w kolumnie; ramka „Zapamiętaj”; „Uwaga do źródła”; bez quizów, klucza, notatek „liceum”, „Poza Drewą”.
- Rozdziały: `rozdzialy/zNN-*.html`, `data-num` = numer zajęć; żywa pagina, spis treści, numeracja rycin i odsyłacze jak dotąd; tryb `--only NN --png`.
- Gotowa rycina z banku: jeden znacznik, np. `<figure class="fig" data-bank="k5-ryc-04" data-title="…"><figcaption>…</figcaption></figure>` – build wstawia plik z banku.
- Zaktualizuj `KOMPONENTY.md` (krótko, tylko to, co potrzebne autorom) i zrób 2-stronicowe demo.
Sprawdź łamanie: rycina na obie kolumny w środku strony, tabela, przejście między stronami, brak dużych białych pól.

## B. Bank rycin (żeby nie rysować od nowa)
Źródła:
- `/root/.claude/uploads/600b873f-e07d-5766-b2f4-6a90b68ae091/ad413184-Kwasy_nukleinowe_kolokwium_4_1.pdf` (18 rycin) → prefiks `k4-`
- `/root/.claude/uploads/600b873f-e07d-5766-b2f4-6a90b68ae091/2dc495de-Analiza_DNA_i_RNA_kolokwium_5_dla_osob_ktore_chca_5.pdf` (26 rycin) → `k5-`
- `/root/.claude/uploads/600b873f-e07d-5766-b2f4-6a90b68ae091/af3be42c-Genomika_analiza_genomu_i_genotypowanie_1.pdf` (23 ryciny) → `g-`
- kolokwium 6: inline SVG w `/home/user/first-thing/kolokwium6/chapters/*.html` oraz w starych rozdziałach (`git show c3e7824^:kolokwium6/chapters/<plik>`; 41 rycin) → `k6-`
Z PDF-ów wycinaj ryciny wektorowo (np. `pdftocairo -svg` strony + przycięcie viewBox do ramki ryciny; położenie z `pdftotext -bbox-layout` po etykiecie „RYC. N”), bez podpisu i etykiety. Zapisz do `bank-rycin/<id>.svg`.
`bank-rycin/INDEX.md`: id · tytuł ryciny (z etykiety) · źródło i strona · wymiary · jedno zdanie, co pokazuje (z podpisu). Zrób też arkusz podglądu PNG (miniatury z id) do szybkiego wyboru.
Przy okazji zapisz tekst trzech opracowań jako `material/k4.txt`, `k5.txt`, `genomika.txt` (`pdftotext -layout`, ze znacznikami stron).

## Stan i raport
Stan po każdym kroku: `stan/F0B.md`. Raport ≤ 12 linijek. Nie commituj.

## Zakres tej tury
Bank rycin teraz tylko z trzech PDF-ów (`k4-`, `k5-`, `g-`); `k6-` w następnej turze. Rozdziały pierwszej tury: G, Z02, Z03, Z04, Z05.
