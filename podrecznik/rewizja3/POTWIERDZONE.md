# R3-W – potwierdzone zgłoszenia recenzentów (weryfikacja: Fable)

Układ: dla każdego rozdziału A (tekst – bloki ZNAJDŹ/ZAMIEŃ dla Sonneta), B (skład/ryciny/układ – dla Opusa), C (odrzucone – liczba). Sekcja D (do decyzji zleceniodawcy) – na końcu pliku.
Każdy fragment ZNAJDŹ sprawdzony w pliku HTML: `grep -c` = 1 (chyba że zaznaczono inaczej).

---

## FRONT (okładka, „Jak korzystać”, spis treści) – 14 zgłoszeń

### A. TEKST
(brak – wszystkie potwierdzone pozycje frontu wymagają przebudowy strony, więc są w B)

### B. SKŁAD / UKŁAD (Opus)
- front-B1 (poz. 2) `front/howto.html`: usunąć zaślepkę `<div class="ph">Miejsce na rycinę (w przygotowaniu)</div>` i podpis „Rycina w przygotowaniu – podpis pod polem już obowiązuje” – w książce nie ma ani jednego takiego pola.
- front-B2 (poz. 3) `front/howto.html`: w legendzie brak dwóch najczęstszych ramek – „Przykład” (ok. 109 ×) i „Obraz w głowie” (19 ×) – oraz linii „Źródło: …”; dodać po jednym wzorze z jednozdaniowym opisem (Przykład: „Rozumowanie przeprowadzone krok po kroku na jednym przypadku – bez nowych faktów.”; Obraz w głowie: „Porównanie, które ułatwia zapamiętanie – nie jest nowym faktem.”; Źródło: „Pod każdym podrozdziałem: skąd pochodzi treść (skróty – zob. wykaz źródeł).”). W wolne miejsce po zaślepce.
- front-B3 (poz. 4) brak wykazu źródeł: `book.json` ma `sources: []`; skróty z linii „Źródło:” nie są nigdzie rozwinięte. Dodać wykaz (na s. „Jak korzystać” albo osobna strona po spisie) – dane z rozpisek:
  - **Drewa** – Drewa G., Ferenc T.: Genetyka medyczna. Podręcznik dla studentów. Edra Urban & Partner, Wrocław 2011.
  - **Jóźwiak** – Jóźwiak J.: Biologia komórki dla studentów uczelni medycznych. Edra Urban & Partner, Wrocław 2020.
  - **Jorde** – Jorde L.B., Carey J.C., Bamshad M.J.: Genetyka medyczna. Edra Urban & Partner, Wrocław (rozpiska: wyd. 2021; rozdziały 8 i 10 korzystają z wydania ok. 2000 r. – zaznaczone ramką na początku rozdziału).
  - **Ostrowska** – Ostrowska Z., Mazur B.: Diagnostyka laboratoryjna dla studentów medycyny. Skrypt dla studentów III roku kierunku lekarskiego. Wydawnictwo ŚUM, Katowice 2011.
  - **Alster** – Alster O., Korwek Z.: Znaczniki starzenia komórkowego. Postępy Biochemii 2014; 60: 138–146.
  - **Twyman** – Twyman R.M.: Biologia rozwoju. Krótkie wykłady. Wydawnictwo Naukowe PWN, Warszawa 2003.
  - **prezentacja LMZ** (rozdz. G) i **Materiał pomocniczy do zajęć** – materiały prowadzących (bez danych bibliograficznych).
- front-B4 (poz. 5) `front/howto.html`, 1. zdanie: „treść pochodzi wyłącznie ze źródeł tam wskazanych – są podane pod każdym podrozdziałem” → niejednoznaczne „tam” / „są podane”; przy dodawaniu wykazu źródeł przeredagować na: „…a treść pochodzi wyłącznie ze źródeł wskazanych w rozpisce. Pod każdym podrozdziałem jest linia „Źródło” ze stronami; skróty rozwija wykaz źródeł.”
- front-B5 (poz. 1) `front/cover.html`, podtytuł „Od cyklu komórkowego do analizy genomu” nie odpowiada spisowi (książka zaczyna się od genomiki, kończy na biotechnologii i eugenice) – propozycja w D-1.
- front-B6 (poz. 10, 11) spis treści: rozdz. 04 – nagłówek z jedną pozycją osierocony na dole lewej kolumny s. 3; rozdz. 06 rozdarty między s. 3 i 4 bez nagłówka kontynuacji (s. 4 ma ok. 25% wolnego) → `break-inside: avoid` na bloku rozdziału w spisie.
- front-B7 (poz. 12) spis, rozdz. 10: tytuł „Chromosomy płci, chromatyna płciowa…” dochodzi niemal do numeru strony (brak odstępu/kropek) – drobne.
- front-B8 (poz. 13) metadane PDF: `Creator: kolokwium6/build.mjs` (nazwa starego projektu); `keywords` w `book.json` obejmują tylko rozdz. 1–6 – dopisać cytogenetykę, komórki macierzyste, dziedziczenie, biotechnologię.
- front-B9 (poz. 8) rozdział pierwszy ma w spisie i nagłówku etykietę „G”, pozostałe 02…11 – nigdzie niewyjaśnione; zob. D-2.

### C. ODRZUCONE: 4
Powtórzenia zdania „Jeden rozdział to jedne zajęcia” i kontrast okładki (kosmetyka), puste miejsce na s. 2 i okładce (wypełni je legenda/wykaz), brak sekcji części 2 w spisie (układ celowy – do D-3), pozycja informacyjna.

---

## Z01 – Genomika (45 zgłoszeń)

### A. TEKST

### z01-1  (pozycja raportu nr 10; M)
PLIK: rozdzialy/z01-genomika.html
ZNAJDŹ:  i od miejsca zmiany chromatogram staje się nieczytelny.</p>
ZAMIEŃ NA: .</p>

### z01-2  (pozycja raportu nr 11; M)
PLIK: rozdzialy/z01-genomika.html
ZNAJDŹ: Wariant 1 tworzy STOP w eksonie 2, wariant 2
ZAMIEŃ NA: Wariant 1 tworzy STOP w eksonie 2, daleko (znacznie ponad 55 nukleotydów) przed ostatnim złączem eksonów, wariant 2

### z01-3  (pozycja raportu nr 14; M)
PLIK: rozdzialy/z01-genomika.html
ZNAJDŹ: , a których nie zestawia „W 60 sekund”
ZAMIEŃ NA: (USUŃ)

### z01-4  (pozycja raportu nr 18; Z)
PLIK: rozdzialy/z01-genomika.html
ZNAJDŹ: i od uzyskanego pokrycia
ZAMIEŃ NA: i od uzyskanego pokrycia, czyli od tego, jaka część regionu została odczytana wystarczająco wiele razy (<a class="pageref" href="#c01-glebokosc"></a>)

### z01-5  (pozycja raportu nr 20; Z)
PLIK: rozdzialy/z01-genomika.html
ZNAJDŹ: <b>pseudogeny</b> i część rearanżacji
ZAMIEŃ NA: <b>pseudogeny</b> i część rearanżacji (zmian położenia lub orientacji odcinków DNA, np. translokacji i inwersji)

### z01-6  (pozycja raportu nr 19; Z)
PLIK: rozdzialy/z01-genomika.html
ZNAJDŹ: metodą <b>RP-PCR</b> (<i>repeat-primed PCR</i>)
ZAMIEŃ NA: metodą <b>RP-PCR</b> (<i>repeat-primed PCR</i>; zasada – <a class="pageref" href="#c01-r-komorka"></a>)

### z01-7  (pozycja raportu nr 21; Z)
PLIK: rozdzialy/z01-genomika.html
ZNAJDŹ: czy pozycja jest konserwowana,
ZAMIEŃ NA: czy pozycja jest konserwowana (czyli ma ten sam aminokwas w podobnych sekwencjach – tak ocenia ją SIFT, opisany niżej),

### z01-8  (pozycja raportu nr 25; Z)
PLIK: rozdzialy/z01-genomika.html
ZNAJDŹ: gdyby badany mężczyzna nie był ojcem biologicznym
ZAMIEŃ NA: gdyby mężczyzna zbadany jako ojciec nie był ojcem biologicznym dziecka

### z01-9  (pozycja raportu nr 26; Z)
PLIK: rozdzialy/z01-genomika.html
ZNAJDŹ: <tr><td>kilka nukleotydów, liczba niepodzielna przez 3</td>
ZAMIEŃ NA: <tr><td>jeden lub kilka nukleotydów, liczba niepodzielna przez 3</td>

### z01-10  (pozycja raportu nr 27; Z – lista ma 8 kroków, rycina 9: krok 1 ryciny to „sygnał z aparatu”)
PLIK: rozdzialy/z01-genomika.html
ZNAJDŹ: <li><b>basecalling</b> – sygnał zamienia się
ZAMIEŃ NA: <li><b>sygnał z aparatu</b> – obrazy fluorescencji albo przebieg prądu, jeszcze bez liter;</li>
    <li><b>basecalling</b> – sygnał zamienia się

### z01-11  (pozycja raportu nr 28; Z)
PLIK: rozdzialy/z01-genomika.html
ZNAJDŹ: nazwa projektu to zaokrąglenie
ZAMIEŃ NA: „1000” w nazwie projektu to zaokrąglenie (zbadano 2504 osoby)

### z01-12  (pozycja raportu nr 30; J)
PLIK: rozdzialy/z01-genomika.html
ZNAJDŹ: kompleksów czteropodjednostkowych (ramka)
ZAMIEŃ NA: kompleksów czteropodjednostkowych (kompleks obwiedziony ramką)

### z01-13  (pozycja raportu nr 32; J)
PLIK: rozdzialy/z01-genomika.html
ZNAJDŹ: (litera; Q30 – 1 błąd na 1000)
ZAMIEŃ NA: – jakość pojedynczej litery; Q30 to 1 błąd na 1000

### z01-14  (pozycja raportu nr 23; Z – tekst odsyła do wykresu, którego w rozdziale nie ma)
PLIK: rozdzialy/z01-genomika.html
ZNAJDŹ: na wykresie krzywa wariantu jest przesunięta w prawo
ZAMIEŃ NA: na wykresie wiązania (stężenie liganda na osi poziomej, część związanego białka na pionowej) krzywa wariantu byłaby przesunięta w prawo

### z01-15  (pozycja raportu nr 23; Z)
PLIK: rozdzialy/z01-genomika.html
ZNAJDŹ: dzięki temu obie krzywe z przykładu mieszczą się na jednym wykresie
ZAMIEŃ NA: dzięki temu krzywe o tak różnych K<sub>d</sub> jak w przykładzie zmieściłyby się na jednym wykresie

### z01-16  (pozycja raportu nr 24; Z – akapit o walidacji nie należy do tematu sekcji o bazach; sygnalizujemy to czytelnikowi)
PLIK: rozdzialy/z01-genomika.html
ZNAJDŹ: <p>Na koniec przykład do walidacji z części 1 (
ZAMIEŃ NA: <p>Ostatni przykład nie dotyczy już baz danych, tylko walidacji metody z części 1 (

### B. SKŁAD / RYCINY / UKŁAD (Opus)
- z01-B1 (poz. 35–40) tabele łamane między stronami z samotnymi wierszami: s. 11→12 („Pytanie | Szczególnie przydatna informacja”, 2+2), s. 22→23 (nagłówek + 1 wiersz na dole), s. 29→30 (testy komercyjne – 1 wiersz MyRisk na nowej stronie), s. 30→31 (linia VCF – samotny wiersz „próbka”), s. 31→32 („Element opisu” – ostatni wiersz sam), s. 34→35 (katalogi – nagłówek + 1 wiersz). Numery stron = build `--only 01`.
- z01-B2 (poz. 42) s. 30: przykładowa linia VCF (mono) łamana na dwa wiersze i justowana – wyłączyć justowanie / zmniejszyć czcionkę.
- z01-B3 (poz. 43) s. 22: wzór „AF = AC / AN” rozcięty między łamami – `break-inside: avoid`/nowrap.
- z01-B4 (poz. 44, 45) s. 13: linia „Źródło” ląduje w prawym łamie obok ramki Zapamiętaj; s. 9: ryc. SBS stoi przed nagłówkiem „Sekwencjonowanie przez syntezę”, tekst o niej dopiero na s. 10; s. 12: nagłówek „Macierz SNP…” osierocony na dole łamu.
- z01-B5 (poz. 33) ryc. 1 (rodzaje wariantów), panel A: linia skutku dla białka stoi bliżej następnego wiersza sekwencji niż własnego – zwiększyć odstęp między parami wierszy (do obejrzenia).
- z01-B6 (poz. 34) ryc. „Droga danych”: etykiety programów SAMtools/IGV stoją między kafelkami zamiast pod etapem „dopasowanie” (do obejrzenia). Po poprawce z01-10 lista w tekście ma 9 kroków jak rycina – sprawdzić zgodność nazw kroków 1–9.

### C. ODRZUCONE: 22
Limit stron/liczba rycin/ramki z mapy B (nieaktualne), fakty „T” i „Z liceum” wróciły celowo (są w opracowaniu E), objaśnienia logiczne bez nowych faktów (RP-PCR, podział metod, orientacja odczytów), powtórzenie Pojęcie/akapit (zamierzone), pusta strona przed częścią 2 (celowa), EJC (źródło nie rozwija skrótu).

