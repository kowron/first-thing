# Kolokwium 6 – instrukcja dla autorów rozdziałów

To jedyne źródło prawdy o formacie rozdziałów. Wzorzec każdego komponentu jest w działającym
rozdziale `chapters/00-demo.html`. Gdy coś jest niejasne, podejrzyj, jak zrobiono to tam.

---

## 1. Szybki start

```bash
cd /home/user/first-thing/kolokwium6
node build.mjs --only 03 --png      # podgląd TWOJEGO rozdziału (tu: 03)
```

* PDF: `<buildDir>/rozdzial-03.pdf`
* PNG stron (96 dpi): `<buildDir>/rozdzial-03-png/p-01.png`, `p-02.png`, …
* `<buildDir>` = `/tmp/claude-0/-home-user-first-thing/600b873f-e07d-5766-b2f4-6a90b68ae091/scratchpad/build`
  (zmienisz go przez `--out-dir DIR` albo zmienną `K6_BUILD_DIR`).
* Wszystkie pliki robocze i wynikowe mają w nazwie numer rozdziału, więc kilku autorów może budować
  jednocześnie i nikt nikomu nie nadpisze plików.
* Build wypisuje na końcu listę `BŁĄD` / `UWAGA` / `info`. **Przed oddaniem rozdziału nie może być
  żadnego `BŁĄD` ani `UWAGA` dotyczącego Twojego pliku.** Wpisy `info` są tylko informacją.
  Jeśli jest `BŁĄD`, skrypt kończy się z kodem 1.
* Obejrzyj PNG wszystkich swoich stron narzędziem Read.

Inne tryby (dla redaktora): `node build.mjs` – całość, wynik w katalogu projektu;
`node build.mjs --demo` – całość razem z rozdziałem 00-demo (→ `<buildDir>/demo.pdf`);
`--keep` zostawia złożony HTML (`<buildDir>/<nazwa>.tmp.html`).

W podglądzie `--only` ryciny są numerowane od 1, strony od 1, a odsyłacze do innych rozdziałów
pokazują „?” (to normalne – build zgłasza je jako `info`). W pełnym buildzie wszystko się wypełni.

---

## 2. Plik rozdziału

* Nazwa: `chapters/NN-krotka-nazwa.html`, np. `chapters/03-elektroforeza-bialek.html`
  (dwie cyfry, myślnik, małe litery bez polskich znaków). Plik `00-…` to demo – nie ruszaj go.
* Plik to **fragment HTML** – bez `<html>`, `<head>`, `<body>`, `<style>`, `<script>`, bez czcionek i CSS.
* Dokładnie jedna sekcja:

```html
<section class="chapter"
  data-num="03"
  data-title="Elektroforeza białek"
  data-short="Elektroforeza białek"
  data-kicker="SDS-PAGE · ogniskowanie izoelektryczne · 2D">

  <p class="lead">Jedno–trzy zdania wprowadzenia (kursywa, pod tytułem).</p>

  <h2 id="c03-sds">Pierwszy podrozdział</h2>
  …
</section>
```

| atrybut | obowiązkowy | do czego |
|---|---|---|
| `data-num` | tak | numer z nazwy pliku, dwie cyfry |
| `data-title` | tak | tytuł rozdziału (otwarcie, spis treści, zakładki PDF) |
| `data-short` | nie | krótsza wersja do żywej paginy u góry strony, gdy tytuł jest długi (> ok. 45 znaków) |
| `data-kicker` | nie (zalecany) | nadtytuł wersalikami, np. 2–4 hasła rozdzielone „ · ” |

**Nie** piszesz: numeru „03”, `<h1>`, linijki „W rozdziale: … · Ryciny: N”, id sekcji, numerów rycin,
numerów stron, etykiet ramek („ZAPAMIĘTAJ” itd.). Wszystko to generuje build.

Kolejność w pliku: `p.lead` → podrozdziały (`h2` + treść + linia `p.src`) → na końcu
**„W 60 sekund”** → **„Sprawdź się”**.

---

## 3. Id i odsyłacze

### Zasady id
* Każde id w rozdziale **musi zaczynać się od `cNN-`**, np. `c03-sds`, `c03-fig-western`, `c03-q-1`.
  Build zgłasza `BŁĄD` przy złym prefiksie i przy duplikatach (także id wewnątrz SVG!).
* Tylko litery, cyfry, `-` i `_`. Bez polskich znaków.
* Ryciny: `cNN-fig-…`. Pytania: `cNN-q-1`, `cNN-q-2`… Podrozdziały: `cNN-…` (id h2 jest opcjonalne –
  build nada je sam, ale jeśli chcesz się do h2 odwołać, nadaj własne).
* Id rozdziału nadaje build: `c03`. Nie ustawiaj go.
* Części końcowe mają prefiks `b-` (np. `b-sciaga`, `b-klucz`, `b-slownik`).

### Odsyłacze (puste `<a>` – tekst wstawia build, wszystkie są klikalne)

| zapis | wynik |
|---|---|
| `<a class="figref" href="#c03-fig-western"></a>` | ryc. 7 |
| `<a class="figref" href="#c03-fig-western" data-panel="B"></a>` | ryc. 7 B |
| `<a class="figref cap" href="#c03-fig-western"></a>` | Ryc. 7 (na początku zdania) |
| `<a class="pageref" href="#c03-sds"></a>` | s. 23 |
| `<a class="chapref" href="#c05"></a>` | rozdz. 5 (s. 41) |

Typowe użycie: `… wędrują do anody (<a class="figref" href="#c03-fig-zel"></a>).`
`pageref` może wskazywać dowolny element z id (h2, rycinę, tabelę, akapit). `chapref` – tylko rozdział (`#c05`).
Odsyłacz do nieistniejącego id = `UWAGA` + czerwony znacznik w PDF.

---

## 4. Tekst główny

```html
<h2 id="c03-sds">SDS-PAGE – rozdział według masy</h2>
<p>Zwykły akapit. <b>Termin</b> pogrubiony przy pierwszym użyciu, <i>łacina / angielski</i> kursywą.</p>

<h3>Podtytuł wewnątrz podrozdziału</h3>   <!-- teal, Inter -->
<h4>Mniejszy nagłówek</h4>                <!-- granatowy, mały -->

<ul>                                        <!-- teal kropki -->
  <li><b>pierwszy</b> – opis;</li>
  <li><b>drugi</b> – opis.</li>
</ul>

<ol>                                        <!-- granatowe kółka z cyfrą -->
  <li><b>Krok</b> – opis.</li>
</ol>

<p class="src">Źródło: Drewa s. 712–713</p>   <!-- na końcu KAŻDEGO podrozdziału -->
```

* **Linia źródła**: zawsze w formacie `Źródło: Klucz s. X–Y`, kilka źródeł rozdzielaj ` · `,
  np. `Źródło: Drewa s. 716–717 · Jorde s. 42`. Klucze: `Drewa`, `Jorde`, `Sylabus` (lista w `book.json`).
  Build zbiera te linie i scala zakresy stron na stronie „Źródła” – trzymaj się formatu.
* Pogrubienia `<b>`/`<strong>` są granatowe. Nie używaj kolorów ani stylów inline.
* Wzory chemiczne/indeksy: `Mg<sup>2+</sup>`, `OD<sub>260</sub>`. Sekwencje: `<span class="seq">5′-GAATTC-3′</span>`.
* Nie dziel wyrazów ręcznie, nie wstawiaj `&shy;`. Dzielenie i twarde spacje robi build:
  po jednoliterowych spójnikach/przyimkach (w, z, i, a, o, u), między liczbą a jednostką (100 pz, 5 V, 80 °C),
  po skrótach (s., ryc., np., ok.) i przed półpauzą „ – ”. Możesz pisać zwykłe spacje.
* Myślnik to półpauza ze spacjami: ` – `. Cudzysłów polski: „…”. Zakresy liczb: `5–8` (półpauza bez spacji).

---

## 5. Notatki marginesowe (prawa kolumna)

Notatka stoi na wysokości akapitu, który jest **bezpośrednio po niej**. Wstawiaj ją **przed** akapitem,
jako bezpośrednie dziecko `<section class="chapter">` – nigdy wewnątrz `<p>`, `<li>`, ramki ani tuż przed `<h2>`
(najpierw `h2`, potem notatka, potem akapit).

```html
<aside class="note liceum"><p><b>Nukleotyd</b> składa się z cukru, zasady azotowej i reszty fosforanowej.</p></aside>
<p>Akapit, którego dotyczy notatka…</p>

<aside class="note pojecie" data-term="Elektroforeza"><p>rozdział cząsteczek naładowanych w polu elektrycznym.</p></aside>
<aside class="note warto"><p>Szczegół lub ciekawostka.</p></aside>
<aside class="note poza"><p>Treść spoza Drewy (etykieta „POZA DREWĄ · UZUPEŁNIENIE”).</p></aside>
<aside class="note warto" data-label="Własna etykieta"><p>…</p></aside>
```

| klasa | wygląd | etykieta |
|---|---|---|
| `liceum` | błękitne tło, niebieska kreska | TO BYŁO W LICEUM (liczone na okładce) |
| `pojecie` | teal kreska; `data-term` = pogrubiony termin | POJĘCIE |
| `warto` | fioletowa kreska | WARTO WIEDZIEĆ |
| `poza` | szare tło, przerywana ramka | POZA DREWĄ · UZUPEŁNIENIE |

* **Długość: maks. ok. 45 słów (6–9 wierszy w wąskiej kolumnie).** Długie notatki nie mieszczą się
  obok akapitu i przeskakują na następną stronę – build zgłasza to jako `UWAGA … nie zmieściła się obok
  swojego akapitu`. Wtedy skróć notatkę albo przenieś ją przed wcześniejszy akapit.
* Kilka notatek pod rząd układa się jedna pod drugą; jeśli odjadą za daleko od akapitu, build da `info`.
  Nie stawiaj więcej niż 2 notatek obok krótkiego akapitu.
* Notatki nigdy nie nachodzą na ryciny ani szerokie tabele (te zawsze schodzą pod notatki), ale przez to
  notatka tuż przed ryciną może zostawić pustą przestrzeń nad ryciną – nie wstawiaj notatki bezpośrednio
  przed `<figure>` ani przed szeroką tabelą.

---

## 6. Ramki w tekście (kolumna tekstu)

```html
<div class="box zapamietaj"><p>Najważniejsze fakty z podrozdziału w 2–4 zdaniach.</p></div>
<div class="box przyklad"><p>Konkretny przypadek albo obliczenie krok po kroku.</p></div>
<div class="box obraz"><p>Porównanie / analogia, która pomaga zapamiętać mechanizm.</p></div>
<div class="box uwaga"><p>Błąd lub niejasność w źródle – z wyjaśnieniem.</p></div>
<div class="box poza"><p>Uzupełnienie spoza Drewy (szare tło, przerywana ramka).</p></div>

<!-- własny tytuł zamiast domyślnej etykiety (kolor zostaje z typu ramki): -->
<div class="box zapamietaj" data-title="Jak czytać nietypowy wzór prążków"><p>…</p></div>

<!-- ramka na pełną szerokość (rzadko): -->
<div class="box przyklad wide"><p>…</p></div>
```

| klasa | kolor | etykieta |
|---|---|---|
| `zapamietaj` | teal | ZAPAMIĘTAJ |
| `przyklad` | ochra | PRZYKŁAD |
| `obraz` | fiolet | OBRAZ W GŁOWIE |
| `uwaga` | czerwień | UWAGA DO ŹRÓDŁA |
| `poza` | szary, przerywana | POZA DREWĄ · UZUPEŁNIENIE |

W ramce mogą być `<p>`, `<ul>`, `<ol>`, `<b>`. Ramka nie łamie się między stronami – **maks. ok. 90 słów**.

---

## 7. „Liczby do zapamiętania”

```html
<div class="numbers">                         <!-- 3 kolumny w kolumnie tekstu -->
  <div class="n"><span class="v">5–8<small>V/cm</small></span><span class="d">napięcie rozdziału w żelu agarozowym</span></div>
  <div class="n"><span class="v">0,5–2<small>%</small></span><span class="d">typowe stężenie agarozy</span></div>
  <div class="n"><span class="v">1<small>nt</small></span><span class="d">rozdzielczość PAGE</span></div>
</div>
```
Warianty: `class="numbers wide"` (4 kolumny, pełna szerokość), `class="numbers cols-2"` (2 kolumny),
`data-title="…"` – inna etykieta. Wartość krótka (do ~7 znaków + jednostka w `<small>`), opis do ~8 słów.
Liczba pozycji: wielokrotność liczby kolumn (3, 6; przy `wide` 4, 8).

---

## 8. Ryciny

```html
<figure class="fig" id="c03-fig-western" data-title="Western blot – od żelu do prążka białka">
  <div class="panel" data-badge="A" data-title="Rozdział w żelu">
    <svg viewBox="0 0 640 220" role="img" aria-label="krótki opis dla czytników">
      …
    </svg>
  </div>
  <div class="panel" data-badge="B" data-title="Detekcja przeciwciałem">
    <svg viewBox="0 0 640 180">…</svg>
  </div>
  <figcaption>A – co pokazuje panel A. B – co pokazuje panel B. Zdania pełne, 2–4 wiersze.</figcaption>
  <p class="fig-src">Źródło: opracowanie własne na podstawie Drewa s. 731</p>
</figure>
```

* Etykietę „RYC. 7  Tytuł” wstawia build z `data-title`; numer jest globalny w całym dokumencie.
* `data-title` i `<figcaption>` są obowiązkowe (brak = `UWAGA`). `fig-src` zalecane.
* Panel bez plakietki/tytułu: `<div class="panel">` (bez atrybutów). Tylko tytuł: `data-title` bez `data-badge`.
* Panele obok siebie: owiń w `<div class="panels cols-2">…</div>` (lub `cols-3`).
* Rycina zawsze na **pełną szerokość** i nigdy nie łamie się między stronami. Jeśli nie zmieści się
  na dole strony, przechodzi na następną i zostawia białą przestrzeń – build zgłosi stronę zapełnioną
  < 35 %. Dlatego: **maks. wysokość ryciny ok. 1/2 strony** (suma viewBox-ów wysokości ≤ ~520 jedn.
  przy szerokości 640); stawiaj rycinę po akapicie, który ją zapowiada, a nie na samym końcu podrozdziału.
* `figure class="fig narrow"` – rycina tylko w kolumnie tekstu (rzadko; dla małych schematów).

### Wymiary SVG (zawsze `viewBox`, bez `width`/`height`)

| układ | szerokość viewBox | 1 jednostka ≈ |
|---|---|---|
| panel na pełną szerokość | **640** | 0,75 pt |
| `panels cols-2` (każdy panel) | **296** | 0,75 pt |
| `panels cols-3` (każdy panel) | **180** | 0,75 pt |
| `fig narrow` | **416** | 0,75 pt |

Wysokość dowolna. Przy tych szerokościach 1 jednostka SVG ≈ 1 px CSS, więc:
**tekst w SVG minimum `font-size` 10 (= 7,5 pt po wydruku)**, standard 11, wyróżnienia 12–14.
Build mierzy każdy tekst i zgłasza zbyt mały (< 7,3 pt) oraz tekst wychodzący poza viewBox.
Nie wychodź elementami poza viewBox (zostaną ucięte na krawędzi strony).

### Klasy do SVG (zdefiniowane w `css/style.css` – używaj ich zamiast własnych kolorów)

Tekst (domyślnie Inter 11, kolor `--ink`):
`t-xs` (10, minimum) `t-s` (11) `t-m` (12) `t-l` (14) `t-xl` (18) · `b` `sb` `md` (grubość) · `it` ·
`up` (wersaliki z rozstrzeleniem, 10) · `mono` · `mid` / `end` (wyrównanie) · `muted` `faint` (szarości).

Kolory wypełnienia: `f-navy f-ink f-teal f-blue f-violet f-ochre f-red f-gold f-white f-gray f-tile f-none`,
jasne tła: `f-teal-bg f-blue-bg f-violet-bg f-ochre-bg f-red-bg`.
Kontury: `s-navy s-teal s-blue s-violet s-ochre s-red s-gray s-rule s-white` + grubość `sw1 sw15 sw2 sw3`.

Gotowe elementy:

| klasa | element | uwagi |
|---|---|---|
| `tile` | `<rect rx="8">` | szary kafelek / tło grupy |
| `card` | `<rect rx="6">` | biała karta z obwódką |
| `divider` | `<line>` | przerywana linia podziału |
| `gel` / `gel-uv` | `<rect rx="6">` | ramka żelu (jasny / ciemny pod UV) |
| `well` | `<rect height="6" rx="1.5">` | studzienka (ciemna) |
| `band` (+ `ladder blue violet ochre red navy faint smear glow`) | `<rect height="4–5" rx="2">` | prążek; `ladder` = wzorzec (szary), `smear` = smuga |
| `lane-label` / `size-label` | `<text>` | podpis ścieżki (M, 1, 2…) / wielkości wzorca (wyr. do prawej) |
| `pole minus` / `pole plus` | `<text>` | znak – / + przy żelu |
| `membrane` | `<rect>` | membrana (nitroceluloza/nylon) |
| `spot` | `<circle>` | plamka (mikromacierz, dot-blot) |
| `probe` | `<path>` | sonda (czerwona gruba linia) |
| `dna` (+ `b`/`blue teal violet ochre red thin`) | `<path>` | nić DNA (gruba, zaokrąglona) |
| `rungs` | `<path>` | pary zasad między niciami |
| `arrow` (+ `teal navy red dashed both`) | `<path>`/`<line>` | strzałka z grotem (marker globalny) |
| `step` | `<g class="step" transform="translate(x,y)"><circle r="9"/><text y="3.8">1</text></g>` | plakietka kroku |
| `step-title` | `<text>` | tytuł kroku obok plakietki |
| `axis`, `gridline`, `trace` (+ kolor), `guide` | wykresy | oś, siatka, krzywa/elektroferogram, czerwona linia pomocnicza |

Markery strzałek są globalne: `marker-end="url(#k6-arrow)"`, `#k6-arrow-teal`, `#k6-arrow-navy`, `#k6-arrow-red`;
gradienty `#k6-grad-denat` (DGGE), `#k6-grad-band`; wzór `#k6-hatch` (patrz `lib/svg-defs.html`).
Nie definiuj własnych `<marker>` – jeśli musisz mieć własne `id` w SVG, nadaj mu prefiks `cNN-`.

Atrybuty `fill="…"`, `stroke="…"`, `font-size="…"` działają, ale **klasy mają pierwszeństwo**
(np. `class="band"` nadpisze `fill`). Kolory poza paletą tylko wyjątkowo – paleta:
granat `#153144`, tekst `#23323e`, teal `#007e83`, błękit `#4387b7`, fiolet `#7867a8`, ochra `#b77a20`,
czerwień `#c84d42`, szary `#8a98a3`, kafelek `#f2f5f7`.

Wzorce: żel z drabinką i krzywa wzorcowa – ryc. 2 w `00-demo.html`; schemat kroków z plakietkami – ryc. 4;
schemat aparatu + elektroferogram – ryc. 3; dwa panele obok siebie – ryc. 1.

---

## 9. Tabele

```html
<!-- wąska (w kolumnie tekstu, szerokość wg treści) -->
<table class="tbl">
  <thead><tr><th>Żel</th><th>Stężenie</th><th>Zakres</th></tr></thead>
  <tbody>
    <tr><td>agarozowy</td><td>0,5–2%</td><td>100 pz – 25 kpz</td></tr>
  </tbody>
</table>

<!-- na całą kolumnę tekstu -->      <table class="tbl full">…</table>
<!-- szeroka (obie kolumny) -->       <table class="tbl wide">…</table>
```

* Nagłówek granatowy wersalikami, pierwsza kolumna pogrubiona (wyłącz: `class="tbl plain-first"`),
  co drugi wiersz delikatnie podbarwiony. Szerokości kolumn: `<th style="width:30%">`.
* Zawsze `<thead>` – nagłówek powtarza się po złamaniu strony. Wiersze się nie łamią.
* Liczby wyrównane do prawej: `<td class="num">`. Tytuł tabeli (opcjonalnie): `<caption>Tytuł</caption>`.
* Tabela z ≥ 4 kolumnami albo długim tekstem w komórkach → `wide`. W tabelach nie ma dzielenia wyrazów.

---

## 10. „W 60 sekund” i „Sprawdź się” (koniec rozdziału)

```html
<div class="w60">
  <ul>
    <li>3–6 punktów, każdy 1–2 wiersze, z <b>pogrubionymi</b> kluczowymi terminami.</li>
    …
  </ul>
</div>

<div class="quiz">
  <ol>
    <li id="c03-q-1">Treść pytania?
      <div class="answer"><p>Odpowiedź z krótkim uzasadnieniem (1–3 zdania).</p></div></li>
    <li id="c03-q-2">Drugie pytanie?
      <div class="answer"><p>…</p></div></li>
  </ol>
</div>
```

* „W 60 sekund”: dokładnie 3–6 punktów (inaczej `UWAGA`).
* „Sprawdź się”: 5–8 pytań, jeden blok na rozdział. Każde `<li>` z id `cNN-q-N`, każda odpowiedź w
  `<div class="answer">` wewnątrz `<li>`. Odpowiedzi są ukryte w rozdziale – build przenosi je do części
  „Klucz odpowiedzi” (pogrupowane rozdziałami, z numerem strony pytania) i dopisuje pod pytaniami odsyłacz do klucza.
* W odpowiedzi możesz używać `<b>`, `figref`, `pageref`. Nie wstawiaj tam notatek, rycin ani tabel.
* Opcjonalnie `data-title="…"` na `.quiz` zmienia podtytuł („Pytania kontrolne”).

---

## 11. Części końcowe (`back/`) – dla autorów ściągi i słownika

* Pliki `back/NN-nazwa.html`, `NN` = kolejność. Build sam dokłada: Klucz odpowiedzi (20), Spis rycin (80),
  Źródła (90) – konfiguracja w `book.json`. Obecne: `10-sciaga.html`, `30-slownik.html` (zaślepki z poprawnym formatem).
* Format: `<section class="back" id="b-…" data-title="Tytuł">` (nagłówek „NA KONIEC / Tytuł” wstawia build).
  Id wewnątrz: prefiks `b-`.
* **Ściąga**: `<section class="back cheat" id="b-sciaga" data-title="Ściąga">`, w środku
  `<div class="cheat-cols">` z blokami `<div class="cheat-block"><h3><span class="n">03</span>Tytuł</h3>…</div>`.
  W blokach: `<p>`, `<ul>`, `<table class="tbl">`, `<div class="numbers">` (bez etykiety), `<div class="pair">` (dwie kolumny).
  Bloki nie łamią się – krótkie (6–12 wierszy). Cel: 1–2 strony.
* **Słownik**: `<dl class="glossary">` z pozycjami `<div><dt>SKRÓT</dt><dd>rozwinięcie <span class="en">(english)</span></dd></div>`, alfabetycznie.

---

## 12. Jak build to składa (żebyś wiedział, czego się spodziewać)

1. Składa jeden HTML: okładka (`front/cover.html`), „Jak korzystać” (`front/howto.html`), spis treści (auto),
   rozdziały w kolejności numerów, część końcowa.
2. W przeglądarce: numeruje ryciny, generuje otwarcia rozdziałów, etykiety ramek, spis treści, spis rycin,
   klucz odpowiedzi, źródła, statystyki okładki; wstawia twarde spacje i miękkie dzielenie wyrazów (polskie reguły sylabizacji).
3. Drukuje PDF (natywny druk Chromium), czyta z PDF numery stron każdego celu linku i drukuje ponownie z
   prawdziwymi numerami – aż numeracja się nie zmienia (zwykle 2 przebiegi). Potem zamienia miękkie łączniki
   na zwykłe dywizy tylko tam, gdzie wiersz faktycznie się łamie, i sprawdza, że łamanie się nie zmieniło.
4. Dokłada metadane, zakładki PDF (rozdziały + podrozdziały h2) i sprawdza linki.
5. Kontrole: id, odsyłacze, podpisy rycin, rozmiar tekstu w SVG, elementy szersze niż kolumna/pole zadruku,
   notatki, które odjechały od akapitu, strony zapełnione < 35 % (biała dziura), czcionki w PDF.

---

## 13. Typowe błędy (i jak je naprawić)

| objaw / komunikat | przyczyna | naprawa |
|---|---|---|
| `id="…" musi zaczynać się od „cNN-”` | brak prefiksu | dodaj `c03-` (także w id wewnątrz SVG) |
| `Zduplikowane id` | to samo id dwa razy (często skopiowany SVG z `<defs>`) | zmień jedno id |
| `Odsyłacz do nieistniejącego id` | literówka w `href` albo brak `#` | `href="#c03-fig-x"` |
| `rycina bez tytułu` / `brak podpisu` | brak `data-title` / `<figcaption>` | dodaj |
| `tekst w SVG ma po wydruku tylko 5,3 pt` | `font-size` < 10 albo viewBox szerszy niż 640 | zwiększ tekst / zmniejsz viewBox |
| `tekst … wychodzi poza viewBox` | etykieta przy krawędzi | przesuń, `class="end"`, powiększ viewBox |
| `Element wchodzi na kolumnę marginesową` | za szeroki obrazek, tabela, długie słowo/sekwencja | `class="wide"` / `tbl wide` / skróć |
| `notatka … przeszła na s. N` | za długa notatka, za dużo notatek obok siebie | skróć, przenieś wyżej |
| `notatka stoi tuż przed h2` / `musi być bezpośrednim dzieckiem` | zła pozycja `<aside>` | najpierw `h2`, potem `<aside>`, potem `<p>` |
| `s. N: zapełniona tylko w X %` | rycina/tabela/ramka nie zmieściła się | przenieś rycinę wcześniej (po akapicie zapowiadającym), skróć ją, podziel ramkę |
| `„W 60 sekund” powinno mieć 3–6 punktów` | za mało/za dużo `<li>` | popraw |
| `pytanie bez odpowiedzi` / `brak id` | brak `<div class="answer">` / `id` w `<li>` | dodaj |
| `data-num … nie zgadza się z numerem w nazwie pliku` | — | ujednolić |
| `plik rozdziału to fragment` | wklejony `<html>`/`<body>` | usuń, zostaw samą `<section>` |
| w PDF czerwone „s. ?” | odsyłacz do innego rozdziału w trybie `--only` | normalne w podglądzie |

Czego nie robić: stylów inline (`style="…"`) poza szerokościami kolumn tabel, własnego CSS, `<br>` do robienia
odstępów, pustych akapitów, obrazków rastrowych (tylko inline SVG), `<h1>`, ręcznego dzielenia wyrazów,
ręcznej numeracji rycin/stron/pytań.
