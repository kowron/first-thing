# Podręcznik – instrukcja dla autorów rozdziałów (wersja dwukolumnowa)

Wzór każdego komponentu jest w działającym rozdziale `rozdzialy/z00-demo.html` (2 strony). Gdy coś jest
niejasne, podejrzyj, jak zrobiono to tam. Zasady treści: `ZASADY.md`.

## 1. Build

```bash
cd /home/user/first-thing/podrecznik
node build.mjs --only 05 --png        # podgląd TWOJEGO rozdziału (plik rozdzialy/z05-*.html)
```

* PDF: `<buildDir>/rozdzial-05.pdf`, PNG stron (96 dpi): `<buildDir>/rozdzial-05-png/p-1.png`, `p-2.png`, …
* `<buildDir>` = `/tmp/claude-0/-home-user-first-thing/600b873f-e07d-5766-b2f4-6a90b68ae091/scratchpad/build-podrecznik`
  (inny: `--out-dir DIR` albo zmienna `PODR_BUILD_DIR`). Wszystkie pliki robocze mają w nazwie numer rozdziału –
  kilku autorów może budować jednocześnie.
* Na końcu build wypisuje `BŁĄD` / `UWAGA` / `info`. Przed oddaniem: **zero `BŁĄD` i `UWAGA` dla Twojego pliku**.
  `info` to tylko informacja. Obejrzyj PNG swoich stron (Read).
* W podglądzie `--only` ryciny i strony są numerowane od 1, odsyłacze do innych rozdziałów pokazują „?” (normalne).
* Redaktor: `node build.mjs` – całość (bez demo) → `Biologia_molekularna_podrecznik.pdf` w katalogu projektu;
  `node build.mjs --demo` – całość z demo; `--keep` zostawia złożony HTML.

## 2. Plik rozdziału

* `rozdzialy/zNN-krotka-nazwa.html`, `NN` = numer zajęć (dwie cyfry), np. `rozdzialy/z05-pcr-diagnostyka.html`.
  **Genomika (rozdział „G”)**: `rozdzialy/z01-genomika.html`, `data-num="01"`, `data-label="G"` – build pokazuje
  wtedy „G” w otwarciu, spisie treści i paginie; podgląd: `node build.mjs --only 01`; id z prefiksem `c01-`.
* Fragment HTML: bez `<html>`, `<head>`, `<body>`, `<style>`, `<script>`, bez stylów inline (poza szerokością kolumn tabel).
* Dokładnie jedna sekcja; kolejność: `p.lead` → podrozdziały (`h2` + treść + linia `p.src`) → „W 60 sekund”.

```html
<section class="chapter" data-num="05" data-title="PCR, enzymy restrykcyjne, diagnostyka"
  data-short="PCR i diagnostyka" data-kicker="PCR · restryktazy · markery · diagnostyka">
  <p class="lead">Jedno–dwa zdania wprowadzenia (kursywa pod tytułem).</p>
  <h2 id="c05-pcr">Pierwszy podrozdział</h2>
  …
  <p class="src">Źródło: Ostrowska s. 54–56 · Drewa s. 703–705</p>
  …
  <div class="w60"><ul><li>…</li></ul></div>
</section>
```

`data-num`, `data-title` – obowiązkowe; `data-short` – krótszy tytuł do paginy (gdy tytuł > ok. 45 znaków);
`data-kicker` – nadtytuł (2–4 hasła); `data-label` – tylko dla „G”. Numeru, `<h1>`, etykiet ramek, numerów rycin
i stron nie piszesz – wstawia je build.

## 3. Id i odsyłacze

* Każde id w rozdziale zaczyna się od `cNN-` (np. `c05-fig-cykl`, `c05-pcr`); tylko litery, cyfry, `-`, `_`.
* Odsyłacze to puste `<a>` (tekst wstawia build): `<a class="figref" href="#c05-fig-cykl"></a>` → „ryc. 3”
  (`class="figref cap"` → „Ryc. 3”, `data-panel="B"` → „ryc. 3 B”); `<a class="pageref" href="#c05-pcr"></a>` → „s. 41”;
  `<a class="chapref" href="#c04"></a>` → „rozdz. 4 (s. 21)”.

## 4. Tekst

* `h2` – podrozdział (zielona kreska nad tytułem), `h3` – podtytuł (zielony), `h4` – mały nagłówek. Akapity są
  justowane, z dzieleniem wyrazów (robi je build – nie wstawiaj `&shy;`; błędne przeniesienie popraw w
  `lib/dzielenie-wyjatki.txt`).
* `<ul>` (zielone kropki), `<ol>` (kółka z cyfrą – etapy procesów). Termin przy pierwszym użyciu `<b>`, łacina i
  angielski `<i>`. Indeksy: `Mg<sup>2+</sup>`, `OD<sub>260</sub>`; sekwencje: `<span class="seq">5′-GAATTC-3′</span>`.
* Linia źródła na końcu każdego podrozdziału: `<p class="src">Źródło: Drewa s. 712–713 · Jóźwiak s. 90</p>`.
* Półpauza ze spacjami ` – `, cudzysłów „…”, zakresy `5–8`. Twarde spacje (w, z, i…, 100 pz, s., ryc.) wstawia build.

## 5. Komponenty (tylko te)

```html
<!-- POJĘCIE: mała ramka w kolumnie; bezpośrednio w <section>, przed akapitem, którego dotyczy (nie przed h2) -->
<aside class="note pojecie" data-term="Starter"><p>krótka definicja, maks. ok. 35 słów.</p></aside>

<!-- ZAPAMIĘTAJ: maks. 1 na podrozdział h2, 2–3 zdania -->
<div class="box zapamietaj"><p>…</p></div>

<!-- UWAGA DO ŹRÓDŁA: maks. 1–2 na rozdział, tylko gdy pewne -->
<div class="box uwaga"><p>W źródle (Drewa s. 713) … Poprawnie: …</p></div>

<!-- W 60 SEKUND: na końcu rozdziału, 4–6 punktów (na obie kolumny, punkty w dwóch kolumnach) -->
<div class="w60"><ul><li><b>Termin</b> – jedno zdanie.</li> …</ul></div>
```

Ramki i „Pojęcie” nie łamią się między kolumnami – trzymaj je krótkie. Innych typów (liceum, warto, poza,
przyklad, obraz, quiz) build nie przyjmuje (`UWAGA … bez typu`).

## 6. Ryciny

### Rycina z banku (najpierw sprawdź `bank-rycin/INDEX.md` i `bank-rycin/podglad-*.png`)

```html
<figure class="fig" id="c05-fig-cykl" data-bank="k5-ryc-04" data-title="Cykl PCR">
  <figcaption>Własny podpis, 1–2 wiersze (bez faktów spoza Twoich źródeł).</figcaption>
</figure>
```

Build wstawia `bank-rycin/k5-ryc-04.svg` (wektorowo, w oryginalnych kolorach) na obie kolumny, w skali ≈ 1:1;
wysokość w druku podaje INDEX. Zły id = `BŁĄD`. Etykietę „RYC. 3 Tytuł” tworzy build z `data-title`.

### Nowa rycina (inline SVG; tylko dla procesu kluczowego i w liczbie z handoffu)

```html
<figure class="fig" id="c02-fig-mitoza" data-title="Fazy mitozy">
  <div class="panel" data-badge="A" data-title="Profaza">   <!-- panel opcjonalny; obok siebie: <div class="panels cols-2"> -->
    <svg viewBox="0 0 640 260" role="img" aria-label="…">…</svg>
  </div>
  <figcaption>Podpis 1–2 wiersze.</figcaption>
</figure>
```

* Na obie kolumny: viewBox szerokości **640** (`panels cols-2` → 296 na panel, `cols-3` → 180).
  Wąska w jednej kolumnie: `<figure class="fig narrow">`, viewBox szerokości **280**.
* **Wysokość ≤ 1/3 strony**: przy szerokości 640 – viewBox wysokości ≤ 290 (suma paneli); przy 280 – ≤ 270.
* Tekst w SVG: `font-size` ≥ 10 (= ok. 7,5 pt; build mierzy i zgłasza mniejszy), standard 11. Bez `width`/`height`,
  nic poza viewBox. Własne id w SVG – z prefiksem `cNN-`. Nie definiuj własnych `<marker>`.
* Klasy (zamiast własnych kolorów) – **nazwy historyczne: `navy` = ciemna zieleń `#173d2b`, `teal` = zieleń akcentu
  `#2b7a4b`**; reszta palety: błękit `#4387b7`, fiolet `#7867a8`, ochra `#b77a20`, czerwień `#c84d42`, szary `#8a98a3`.
  * tekst: `t-xs`(10) `t-s`(11) `t-m`(12) `t-l`(14) `t-xl`(18), `b` `sb` `md`, `it`, `up`, `mono`, `mid` `end`, `muted` `faint`;
  * wypełnienie: `f-navy f-ink f-teal f-blue f-violet f-ochre f-red f-gold f-white f-gray f-tile f-none`,
    tła `f-teal-bg f-blue-bg f-violet-bg f-ochre-bg f-red-bg`; kontur: `s-navy s-teal s-blue s-violet s-ochre s-red s-gray s-rule s-white`
    + `sw1 sw15 sw2 sw3`;
  * gotowe: `tile`, `card`, `divider`, `gel`/`gel-uv`, `well`, `band` (+ kolor), `lane-label`, `size-label`, `membrane`, `spot`,
    `probe`, `dna` (+ kolor, `thin`), `rungs`, `arrow` (+ `teal navy red dashed both`), `step` (plakietka kroku:
    `<g class="step" transform="translate(x,y)"><circle r="9"/><text y="3.8">1</text></g>`), `step-title`, `axis`, `gridline`, `trace`, `guide`.
  * markery globalne: `url(#k6-arrow)`, `#k6-arrow-teal`, `#k6-arrow-navy`, `#k6-arrow-red`; wzór `#k6-hatch` (`lib/svg-defs.html`).

## 7. Tabele

```html
<table class="tbl">…</table>        <!-- w kolumnie, szerokość wg treści -->
<table class="tbl full">…</table>   <!-- na całą kolumnę -->
<table class="tbl wide">…</table>   <!-- na obie kolumny: ≥ 3 kolumny albo dłuższy tekst w komórkach -->
```
Zawsze `<thead>` (nagłówek powtarza się po złamaniu strony); pierwsza kolumna pogrubiona (wyłącz: `tbl plain-first`);
szerokości: `<th style="width:30%">`; liczby: `<td class="num">`. Wiersze się nie łamią.

## 8. Łamanie – czego się spodziewać

* Na obie kolumny idą: otwarcie, ryciny (bez `narrow`), `tbl wide`, „W 60 sekund”. Tekst przed takim elementem
  wyrównuje się w dwóch kolumnach, element staje pod nim, tekst biegnie dalej pod spodem.
* Rycina i ramka nie dzielą się – jeśli nie zmieszczą się na dole strony, przechodzą na następną i zostawiają
  miejsce. Dlatego: rycinę stawiaj zaraz po akapicie, który ją zapowiada (nie na końcu podrozdziału), ryciny z
  banku o wysokości ≥ 1/2 strony – najlepiej na początku podrozdziału. Build zgłasza strony zapełnione < 35 %.
* `UWAGA Element szerszy niż kolumna` → dodaj `wide` (tabela) albo zmniejsz rycinę/SVG; długą sekwencję podziel.
* Komunikat `info Kolumny: N × podział…` jest normalny (build wyrównuje kolumny po przejściu strony).

| komunikat | naprawa |
|---|---|
| `id="…" musi zaczynać się od „cNN-”` / `Zduplikowane id` | dodaj prefiks / zmień id (także w SVG) |
| `Odsyłacz do nieistniejącego id` | popraw `href="#cNN-…"` |
| `brak ryciny „…” w banku` | sprawdź id w `bank-rycin/INDEX.md` |
| `rycina bez tytułu` / `brak podpisu` | dodaj `data-title` / `<figcaption>` |
| `tekst w SVG ma po wydruku tylko … pt` | `font-size` ≥ 10 przy viewBox 640 (280 przy `narrow`) |
| `notatka bez typu` / `ramka bez typu` | tylko `note pojecie`, `box zapamietaj`, `box uwaga` |
| `„W 60 sekund” powinno mieć 3–6 punktów` | popraw liczbę `<li>` |
| `s. N: zapełniona tylko w X %` | przesuń rycinę/tabelę wcześniej, skróć ją albo ramkę |
| `data-num … nie zgadza się z numerem w nazwie pliku` | ujednolić (`z05-…` ↔ `data-num="05"`) |
