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

---

## Z02 – Cykl komórkowy, mitoza i mejoza (64 zgłoszenia)

### A. TEKST

### z02-1  (pozycja raportu nr 2; Z – samo związanie cykliny nie włącza kinazy, por. kroki 2–3 niżej)
PLIK: rozdzialy/z02-cykl-komorkowy.html
ZNAJDŹ: Zmienia się to, gdy przyłączy się do niej <b>cyklina</b>
ZAMIEŃ NA: Pierwszym warunkiem jej włączenia jest przyłączenie <b>cykliny</b>

### z02-2  (pozycja raportu nr 5; Z)
PLIK: rozdzialy/z02-cykl-komorkowy.html
ZNAJDŹ: zaangażowane w replikację DNA i podwojenie centrosomu. Skutek:
ZAMIEŃ NA: zaangażowane w replikację DNA i podwojenie centrosomu (struktury z mikrotubulami, która w mitozie się rozdziela). Skutek:

### z02-3  (pozycja raportu nr 6; M – część 2 podawała inny moment niż krok 4, do którego odsyła)
PLIK: rozdzialy/z02-cykl-komorkowy.html
ZNAJDŹ: mniej więcej w połowie fazy S wraca do zera – w fazie S cyklinę E rozkłada proteasom (krok 4);
ZAMIEŃ NA: na wykresie wraca do zera mniej więcej w połowie fazy S; według tekstu proteasom rozkłada cyklinę E pod koniec fazy S (krok 4);

### z02-4  (pozycja raportu nr 10; Z)
PLIK: rozdzialy/z02-cykl-komorkowy.html
ZNAJDŹ: białko receptorowe dla TNF.</li>
ZAMIEŃ NA: białko receptorowe dla TNF (czynnika martwicy nowotworów).</li>

### z02-5  (pozycja raportu nr 12; M – źródło: „wydaje się”)
PLIK: rozdzialy/z02-cykl-komorkowy.html
ZNAJDŹ: ale udział p57 jest dużo bardziej istotny
ZAMIEŃ NA: ale udział p57 wydaje się dużo bardziej istotny

### z02-6  (pozycja raportu nr 14; M – źródła nie utożsamiają obu punktów)
PLIK: rozdzialy/z02-cykl-komorkowy.html
ZNAJDŹ: Odpowiada on punktowi kontrolnemu G2/M (
ZAMIEŃ NA: Leży w tym samym miejscu cyklu co punkt kontrolny G2/M (

### z02-7  (pozycja raportu nr 15; M)
PLIK: rozdzialy/z02-cykl-komorkowy.html
ZNAJDŹ: Mają trzy zadania, w ustalonej kolejności:</p>
ZAMIEŃ NA: Mają trzy zadania:</p>

### z02-8  (pozycja raportu nr 18; Z – część 2 pisze, że część 1 mówi „ostrożnie” o sekwencji homologicznej)
PLIK: rozdzialy/z02-cykl-komorkowy.html
ZNAJDŹ: mogą zostać skopiowane z chromatydy siostrzanej, a ciągłość
ZAMIEŃ NA: mogą zostać skopiowane z nieuszkodzonej sekwencji homologicznej, a ciągłość

### z02-9  (pozycja raportu nr 19; M – w tym rozdziale otoczka znika w prometafazie)
PLIK: rozdzialy/z02-cykl-komorkowy.html
ZNAJDŹ: w profazie chromosomy się kondensowały, a otoczka znikała – teraz jest odwrotnie.
ZAMIEŃ NA: w profazie chromosomy się kondensowały – teraz się rozluźniają.

### z02-10  (pozycja raportu nr 23; J)
PLIK: rozdzialy/z02-cykl-komorkowy.html
ZNAJDŹ: To one zapewniają prawidłowy podział materiału genetycznego.
ZAMIEŃ NA: Ta precyzja zapewnia prawidłowy podział materiału genetycznego.

### z02-11  (pozycja raportu nr 27; Z)
PLIK: rozdzialy/z02-cykl-komorkowy.html
ZNAJDŹ: Każda kolejna para homologów podwaja liczbę możliwości.
ZAMIEŃ NA: Każda kolejna para homologów podwaja liczbę możliwych zestawów (2 pary – 4 zestawy, 3 pary – 8).

### z02-12  (pozycja raportu nr 31; J)
PLIK: rozdzialy/z02-cykl-komorkowy.html
ZNAJDŹ: (wszystkie przykłady z tabeli źródła – część 2,
ZAMIEŃ NA: (pozostałe przykłady z tabeli źródła – część 2,

### z02-13  (pozycja raportu nr 34; M – tabela Jóźwiaka różni się też w G0 i G2)
PLIK: rozdzialy/z02-cykl-komorkowy.html
ZNAJDŹ: Różnica dotyczy fazy M: u Jóźwiaka
ZAMIEŃ NA: Najważniejsza różnica dotyczy fazy M: u Jóźwiaka

### z02-14  (pozycja raportu nr 38; Z – sekcja ma cztery podrozdziały)
PLIK: rozdzialy/z02-cykl-komorkowy.html
ZNAJDŹ: Zostały trzy pytania: jak antagonista czynnika wzrostu może wywołać apoptozę, czy wyrok p53 jest ostateczny i gdzie jeszcze p53 hamuje cykl.
ZAMIEŃ NA: Zostały cztery pytania: jak antagonista czynnika wzrostu może wywołać apoptozę, czy wyrok p53 jest ostateczny, jaką rolę gra przy p53 białko p300 i gdzie jeszcze p53 hamuje cykl.

### z02-15  (pozycja raportu nr 47; M – domysł o błędzie źródła podany jak ustalenie)
PLIK: rozdzialy/z02-cykl-komorkowy.html
ZNAJDŹ: Zapewne miało być „skracające się”: tekst mówi o skracaniu się włókien wrzeciona.
ZAMIEŃ NA: Tekst źródła mówi w tym miejscu o skracaniu się włókien wrzeciona.

### z02-16  (pozycja raportu nr 52; J – źródło rozwija TPA w nazwie TRE)
PLIK: rozdzialy/z02-cykl-komorkowy.html
ZNAJDŹ: PDGF, FGF, TPA, DMSO,
ZAMIEŃ NA: PDGF, FGF, DMSO,

### z02-17  (pozycja raportu nr 53; J)
PLIK: rozdzialy/z02-cykl-komorkowy.html
ZNAJDŹ: To etapy z <a class="figref" href="#c02-fig-cdk"></a> z jedną nowością:
ZAMIEŃ NA: To te same etapy co na <a class="figref" href="#c02-fig-cdk"></a>, z jedną nowością:

### B. SKŁAD / RYCINY / UKŁAD (Opus)
- z02-B1 (poz. 56) puste miejsca przed rycinami na całą szerokość: s. 1 (ok. 40 mm, ryc. 1 na s. 2), s. 3 (prawy łam ok. 80 mm, ryc. 2 na s. 4), s. 7 (65/40 mm, ryc. 4 na s. 8), s. 16 (ok. 65 mm, ryc. 7 na s. 17). Numery stron = build `--only 02`.
- z02-B2 (poz. 57) s. 19: ramka „Zapamiętaj” w lewym łamie, prawy łam pusty aż do „W 60 sekund”.
- z02-B3 (poz. 58, 59) tabele: „Pięć liczb o BRCA” – ostatni wiersz sam na s. 27; tabela „Błąd / Gamety / Zygoty” na początku s. 28, zdanie wprowadzające na dole s. 27; „Mitoza a mejoza” 4+4 i tabela skrótów 6+3 – do oceny.
- z02-B4 (poz. 61, 62) tabela zbiorcza „Kompleks / Kiedy / Co robi” (s. 12) stoi pod h3 „Punkt restrykcyjny fazy G2”, choć podsumowuje cały cykl – dać jej własny nagłówek lub przesunąć; s. 23: nagłówek „Kto włącza który hamulec?” + 1 zdanie oderwane od tabeli na s. 24.
- z02-B5 (poz. 63) odsyłacze `pageref` do h2 zamiast do h3: MPF i APC/C → `#c02-sg2` (s. 10), a opis jest na s. 11 (jest id `c02-apc`); punkt kontrolny M → `#c02-cykl` (s. 1), opis na s. 2–3.
- z02-B6 (poz. 64) żywa pagina „Cykl komórkowy, mitoza i mejoza” ≠ tytuł rozdziału „Mitoza, mejoza i regulacja cyklu komórkowego” (`data-short` vs `data-title`) – do ujednolicenia lub zostawić świadomie.
- z02-B7 (poz. 29) tabela „Mitoza a mejoza”, wiersz „Ilość DNA: 2n → 2n / 2n → 1n”: sprawdzić, czy styl nagłówków/komórek nie zmienia wielkości liter w „n” (uwaga ogólna o tabelach).

### C. ODRZUCONE: 38
Limit stron i liczba rycin (nieaktualne), „Zaburzenia mejozy” i strony 143/162 (zostają – decyzje Z1, Z2, Z4), opisy rycin i tabel źródeł odczytane ze skanu (plan `plany/z02-czesci.md`: ryc. 6.6–6.10, 7.1, 7.5–7.12, tab. 7.1), różnice między Drewą a Jóźwiakiem oddane wiernie (centrosomy, APC/C, pRb), przypomnienia z rozdz. 3 i objaśnienia logiczne.

---

## Z03 – Apoptoza i starzenie komórek (42 zgłoszenia)

### A. TEKST

### z03-1  (pozycja raportu nr 1; J – szyk dwuznaczny: czyta się „ciałka pochłaniają komórki”)
PLIK: rozdzialy/z03-apoptoza.html
ZNAJDŹ: a jej szczątki, zamknięte w błonie, pochłaniają inne komórki.
ZAMIEŃ NA: a jej szczątki, zamknięte w błonie, są pochłaniane przez inne komórki.

### z03-2  (pozycja raportu nr 1; J)
PLIK: rozdzialy/z03-apoptoza.html
ZNAJDŹ: ciałka apoptotyczne, które pochłaniają sąsiednie komórki lub makrofagi.
ZAMIEŃ NA: ciałka apoptotyczne, pochłaniane przez sąsiednie komórki lub makrofagi.

### z03-3  (pozycja raportu nr 1; J)
PLIK: rozdzialy/z03-apoptoza.html
ZNAJDŹ: Ciałka apoptotyczne pochłaniają (fagocytują) sąsiednie komórki albo <b>makrofagi</b>
ZAMIEŃ NA: Ciałka apoptotyczne są pochłaniane (fagocytowane) przez sąsiednie komórki albo przez <b>makrofagi</b>

### z03-4  (pozycja raportu nr 2; M – źródło nie mówi o „ustalonej kolejności”)
PLIK: rozdzialy/z03-apoptoza.html
ZNAJDŹ: Zmiany widoczne w jej budowie następują w ustalonej kolejności – numery
ZAMIEŃ NA: Zmiany widoczne w jej budowie opisujemy po kolei – numery

### z03-5  (pozycja raportu nr 4; Z – DD raz oznaczało prodomenę kaspazy, raz domenę receptora; źródło: DED i CARD to subdomeny DD)
PLIK: rozdzialy/z03-apoptoza.html
ZNAJDŹ: zwana domeną śmierci <b>DD</b> (ang. <i>death domain</i>);
ZAMIEŃ NA: zwana domeną śmierci <b>DD</b> (ang. <i>death domain</i>); domena DD ma dwie subdomeny – DED i CARD – i to nimi prokaspazy łączą się z innymi białkami (o tym przy szlakach);

### z03-6  (pozycja raportu nr 14; M – TNFR1 i TNFR2 mają wspólny ligand)
PLIK: rozdzialy/z03-apoptoza.html
ZNAJDŹ: Każdy receptor ma swój ligand (
ZAMIEŃ NA: Receptory mają swoje ligandy (

### z03-7  (pozycja raportu nr 15; Z)
PLIK: rozdzialy/z03-apoptoza.html
ZNAJDŹ: uniemożliwia im oddziaływanie z cyklinami D
ZAMIEŃ NA: uniemożliwia kinazom oddziaływanie z cyklinami D

### z03-8  (pozycja raportu nr 17; Z)
PLIK: rozdzialy/z03-apoptoza.html
ZNAJDŹ: liczbą komórek progenitorowych w wielu tkankach
ZAMIEŃ NA: liczbą komórek progenitorowych (komórek, z których powstają dojrzałe komórki tkanki) w wielu tkankach

### z03-9  (pozycja raportu nr 17; Z)
PLIK: rozdzialy/z03-apoptoza.html
ZNAJDŹ: transformację epitelialno-mezenchymalną i oporność
ZAMIEŃ NA: transformację epitelialno-mezenchymalną (przemianę komórek nabłonkowych w komórki o cechach mezenchymalnych) i oporność

### z03-10  (pozycja raportu nr 18; M – źródło podaje to tylko dla ciałek PML)
PLIK: rozdzialy/z03-apoptoza.html
ZNAJDŹ: (3) Pomogą znaczniki, które przy tamtych przyczynach się nie zmieniają: przy zatrzymaniu
ZAMIEŃ NA: (3) Pomoże znacznik, który przy tamtych przyczynach się nie zmienia: przy zatrzymaniu

### z03-11  (pozycja raportu nr 20; M – w źródle zalecenie, nie reguła)
PLIK: rozdzialy/z03-apoptoza.html
ZNAJDŹ: bada się ją razem z innym znacznikiem, np. zatrzymaniem w cyklu
ZAMIEŃ NA: dobrze jest badać ją razem z innymi znacznikami, np. z zatrzymaniem w cyklu

### z03-12  (pozycja raportu nr 22; M – szyk odwracał sens: to pierścień otacza rdzeń)
PLIK: rozdzialy/z03-apoptoza.html
ZNAJDŹ: rdzeń bogaty w H3K9me3 otacza pierścień, w którym dominuje H3K27me3
ZAMIEŃ NA: rdzeń bogaty w H3K9me3 jest otoczony pierścieniem, w którym dominuje H3K27me3

### z03-13  (pozycja raportu nr 33; Z – numer strony prowadził do początku podrozdziału, nie do ryciny)
PLIK: rozdzialy/z03-apoptoza.html
ZNAJDŹ: (<a class="figref" href="#c03-fig-kaspaza"></a>, <a class="pageref" href="#c03-kaspazy"></a>) przy każdej części
ZAMIEŃ NA: (<a class="figref" href="#c03-fig-kaspaza"></a>) przy każdej części

### B. SKŁAD / RYCINY / UKŁAD (Opus)
- z03-B1 (poz. 39) s. 6: tabela porównawcza szlaków złamana między łamami – nagłówek + 1 wiersz w lewym, 4 wiersze w prawym bez nagłówka → `break-inside: avoid` albo `tbl full`.
- z03-B2 (poz. 40) s. 20: tabela receptorów śmierci – ostatni wiersz (TRAIL-R1, TRAIL-R2) sam na górze prawego łamu.
- z03-B3 (poz. 37) s. 7: dolne ok. 65–75 mm obu łamów puste (ryc. 5 na s. 8); s. 8: lewy łam pusty ok. 65 mm przed ryc. 6.
- z03-B4 (poz. 41) s. 2→3: zdanie „Prokaspaza składa się z trzech części (ryc. 2):” oderwane od listy i ryciny; s. 19→20: wstęp „Co widać w tabeli?” oderwany od listy – drobne.

### C. ODRZUCONE: 27
Limit stron i liczba rycin (nieaktualne), opisy rycin i tabel źródeł odczytane ze skanu (plan `plany/z03-czesci.md`: tab. 8.1, 8.2, 11.4 – nagłówki potwierdzone, ryc. 8.2–8.6, 11.8, Alster ryc. 1–3), przypomnienia z rozdz. 2, definicje słów i objaśnienia logiczne, oczywiste poprawki OCR (IL-1β, „wypływ”), powtórzenie Pojęcie/akapit (zamierzone), pusta strona przed częścią 2.

---

## Z04 – Kwasy nukleinowe, replikacja, izolacja DNA i RNA (51 zgłoszeń)

Uwaga dla wklejającego: bloki z04-6a…6d dotyczą jednego fragmentu (topoizomerazy) – wklej wszystkie cztery.

### A. TEKST

### z04-1a  (pozycja raportu nr 1; M – DnaA nie ma w źródle)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: <li><b>białka inicjatorowe</b> (u <i>E. coli</i> – DnaA) przyłączają
ZAMIEŃ NA: <li><b>białka inicjatorowe</b> przyłączają

### z04-1b  (pozycja raportu nr 1; M)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: zaczynają rozplatać DNA (u <i>E. coli</i>: DnaA)</td>
ZAMIEŃ NA: zaczynają rozplatać DNA</td>

### z04-2  (pozycja raportu nr 2; M – CCA zostaje tylko w podpisie ryciny, która je pokazuje)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: <li><b>koniec 3′</b>, zakończony sekwencją CCA – tu przyłączony
ZAMIEŃ NA: <li><b>koniec 3′</b> – tu przyłączony

### z04-4a  (pozycja raportu nr 4; M – źródło: snRNA „biorą udział w składaniu pre-mRNA”, bez spliceosomu i parowania z granicami intronu)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: , a te razem tworzą <b>spliceosom</b> – „maszynę”, która wycina z pre-mRNA wstawki zwane intronami i łączy pozostałe odcinki, eksony. Granice intronu snRNA rozpoznaje na zasadzie komplementarności – paruje z nimi. Cały proces, splicing, opisuje następny podrozdział.
ZAMIEŃ NA:  (małe jądrowe rybonukleoproteiny) i biorą udział w składaniu (splicingu) pre-mRNA – wycinaniu wstawek zwanych intronami i łączeniu pozostałych odcinków, eksonów. Ten proces opisuje następny podrozdział.

### z04-4b  (pozycja raportu nr 4; M)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: <td>wycina introny (spliceosom)</td><td>z granicami intronu w pre-mRNA</td>
ZAMIEŃ NA: <td>bierze udział w wycinaniu intronów (splicing)</td><td>źródło tego nie podaje</td>

### z04-4c  (pozycja raportu nr 4; M – zostaje półzdanie o rycinie)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ:  Najpierw musi on „wiedzieć”, gdzie kończy się ekson, a zaczyna intron. Pomaga w tym komplementarność: snRNA paruje z sekwencjami na granicach intronu.
ZAMIEŃ NA: (USUŃ)

### z04-6a  (pozycje raportu nr 6 i 34; M – źródło, s. 34, 37, 53: przecięcie jednej lub obu nici; topo I usuwa superskręt, topo II go dodaje; gyraza)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: Działają w trzech krokach: przecinają jedną nić albo obie, pozwalają DNA obrócić się lub przejść przez przerwę, a potem z powrotem łączą przecięte końce. Sekwencja DNA się nie zmienia – zmienia się tylko jego skręcenie.
ZAMIEŃ NA: Superskręcone DNA można uwolnić ze stanu skrętu tylko przez przerwanie jednej albo obu nici – i to właśnie robią topoizomerazy. Dwa typy dają przeciwne skutki:

### z04-6b  (pozycja raportu nr 6; M)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: <li><b>Topoizomeraza I</b> przecina <b>jedną</b> nić. Przecięta nić obraca się wokół drugiej, napięcie maleje, a potem przerwa zostaje zamknięta. Nie potrzebuje ATP.</li>
ZAMIEŃ NA: <li><b>Topoizomeraza I</b> usuwa superskręt – zmniejsza (relaksuje) napięcie skrętne DNA.</li>

### z04-6c  (pozycje raportu nr 6 i 34; M)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: <li><b>Topoizomeraza II</b> przecina <b>obie</b> nici, przeprowadza przez przerwę inny odcinek helisy, a potem łączy nici. Zużywa ATP. U bakterii jej odmianą jest <b>gyraza</b>, która wprowadza ujemne superskręty.</li>
ZAMIEŃ NA: <li><b>Topoizomeraza II</b> dodaje superskręt – zwiększa napięcie skrętne DNA.</li>
    <li><b>Gyraza</b> – topoizomeraza bakterii – pracuje tuż przed widełkami: najpierw zamienia DNA skręcone dodatnio w rozluźnione (ten krok wymaga ATP), a potem w skręcone ujemnie (szczegóły – <a class="pageref" href="#c04-r-enzymy"></a>).</li>

### z04-6d  (pozycja raportu nr 7; M – źródło nie mówi o antybiotykach blokujących gyrazę ani o zatrzymaniu podziałów)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: enzymy te są dobrym celem leków. Lek, który zablokuje topoizomerazę, zaburza kopiowanie DNA w komórce bakterii albo w komórce nowotworowej. Tak działają niektóre antybiotyki (blokują gyrazę bakterii) i leki przeciwnowotworowe (zatrzymują podziały komórek raka).
ZAMIEŃ NA: enzymy te są głównym celem leków przeciw chorobom bakteryjnym i nowotworowym. Przewiduje się, że lek działający na topoizomerazę zaburza replikację i transkrypcję w komórce bakterii albo w komórce nowotworowej, co prowadzi do śmierci tej komórki.

### z04-8  (pozycja raportu nr 8; M – „DNA w komórce jest ujemnie superskręcone” spoza źródła)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ:  W komórkach DNA jest zwykle lekko ujemnie superskręcone. Ma to sens: niedokręcone nici łatwiej rozdzielić, a rozdzielać je trzeba przy replikacji i transkrypcji. Dodatnie superskręty powstają natomiast przed przesuwającymi się widełkami replikacyjnymi.
ZAMIEŃ NA:  DNA skręcone dodatnio pojawia się przed przesuwającymi się widełkami replikacyjnymi.

### z04-11  (pozycja raportu nr 11; M – źródło i część 2: najczęstsze formy alternatywne to A, C i Z; rzadkie są tylko D i E)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: <td>rzadsze; ich warunki – w części 2 (
ZAMIEŃ NA: <td>C – częsta forma alternatywna (obok A i Z), D i E – rzadkie; ich warunki – w części 2 (

### z04-13  (pozycja raportu nr 13; M – wniosek o „warunkach komórkowych” i „w przyrodzie” spoza źródła)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: Skoro forma zależy od warunków, w komórce przeważa ta, która odpowiada warunkom komórkowym: wysokiej wilgotności i niskiemu stężeniu soli. To prawoskrętna <b>B-DNA</b> – helisa opisana przez Watsona i Cricka. Jest najczęstszą formą DNA w przyrodzie.
ZAMIEŃ NA: W komórkach najczęściej występuje prawoskrętna <b>B-DNA</b> – helisa opisana przez Watsona i Cricka. Powstaje przy wysokiej wilgotności i niskim stężeniu soli.

### z04-14a  (pozycja raportu nr 14; M – źródło: H1 „na zewnątrz nukleosomu”, wiąże DNA łącznikowe)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: Na zewnątrz rdzenia, w miejscu, gdzie DNA wchodzi na nukleosom i z niego schodzi, leży <b>histon H1</b>
ZAMIEŃ NA: Na zewnątrz nukleosomu leży <b>histon H1</b>

### z04-14b  (pozycja raportu nr 14; M – mikroskop elektronowy i „koraliki” spoza źródła)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: <p>Pod mikroskopem elektronowym rozluźniona chromatyna wygląda jak <b>koraliki nawleczone na nitkę</b>: koraliki to nukleosomy, a nitka – DNA łącznikowe. To włókno ma grubość ok. 11 nm.</p>
ZAMIEŃ NA: <p>Rozluźniona chromatyna interfazowa ma strukturę nukleosomów połączonych DNA łącznikowym. Ten poziom upakowania ma szerokość ok. 11 nm.</p>

### z04-14c  (pozycja raportu nr 14; M)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: a klips, który przytrzymuje nić na wejściu i wyjściu, to histon H1
ZAMIEŃ NA: a klips na zewnątrz szpulki to histon H1

### z04-14d  (pozycja raportu nr 14; M)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: <p>Włókno „koralików na nitce” zwija się dalej tak
ZAMIEŃ NA: <p>Łańcuch nukleosomów zwija się dalej tak

### z04-14e  (pozycja raportu nr 14; M)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: ma postać nukleosomów i włókien – dzięki czemu enzymy mają dostęp do genów.</p>
ZAMIEŃ NA: ma postać nukleosomów i włókien.</p>

### z04-18a  (pozycja raportu nr 18; M – „zapas” spoza źródła)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: Telomery są zapasem, który może się przy kolejnych replikacjach skracać bez utraty genów. Chronią też chromosomy
ZAMIEŃ NA: Ich obecność zapobiega utracie DNA z końców chromosomów i zapewnia niezmienną długość genomu. Telomery chronią też chromosomy

### z04-18b  (pozycja raportu nr 18; M)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: Jej RNA paruje z końcem 3′ chromosomu i służy za matrycę
ZAMIEŃ NA: Jej RNA paruje z końcowym fragmentem DNA chromosomu i służy za matrycę

### z04-18c  (pozycja raportu nr 18; M – źródło: drugą nić dobudowuje się „w sposób semikonserwatywny”)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: Drugą nić uzupełnia potem zwykła replikacja (starter i polimeraza).
ZAMIEŃ NA: Drugą nić dobudowuje się potem do niej w sposób semikonserwatywny.

### z04-18d  (pozycja raportu nr 18; M – źródło: skrócenie „przy każdym podziale mitotycznym”)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: więc ich telomery z wiekiem się skracają, co wiąże się
ZAMIEŃ NA: więc ich chromosomy skracają się przy każdym podziale, co wiąże się

### z04-18e  (pozycja raportu nr 18; M)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: <td>matryca dla powtórzeń telomeru</td><td>z końcem 3′ chromosomu</td>
ZAMIEŃ NA: <td>matryca dla powtórzeń telomeru</td><td>z końcowym fragmentem DNA chromosomu</td>

### z04-19  (pozycja raportu nr 19; M – źródło: „zwykle”)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: i zarazem najliczniejszym rodzajem RNA w komórce
ZAMIEŃ NA: i zarazem zwykle najliczniejszym rodzajem RNA w komórce

### z04-20  (pozycja raportu nr 20; M – źródło: „snoRNA stanowi część telomerazy u ssaków”)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: <p>U ssaków RNA telomerazy należy do rodziny snoRNA. Stąd jego inna funkcja: ta sama grupa RNA w jąderku kieruje modyfikacjami rRNA.</p>
ZAMIEŃ NA: <p>Według źródła u ssaków częścią telomerazy jest snoRNA – ten sam rodzaj RNA, który w jąderku kieruje modyfikacjami rRNA.</p>

### z04-21a  (pozycja raportu nr 21; M – „spinka” i „własne geny” spoza źródła)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: Gen miRNA daje w jądrze cząsteczkę w kształcie spinki – <b>pre-miRNA</b> (ok. 75 nukleotydów).
ZAMIEŃ NA: miRNA powstaje w jądrze jako dłuższa cząsteczka – <b>pre-miRNA</b> (75 nukleotydów).

### z04-21b  (pozycja raportu nr 21; M)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ:  miRNA reguluje w ten sposób własne geny komórki.</p>
ZAMIEŃ NA: </p>

### z04-21c  (pozycja raportu nr 21; M)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: <td>z pre-miRNA – spinki przepisanej z genu komórki</td>
ZAMIEŃ NA: <td>z pre-miRNA (75 nt), które powstaje w jądrze</td>

### z04-21d  (pozycja raportu nr 21; M)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: <li>dłuższe RNA w kształcie spinki (pre-miRNA) albo
ZAMIEŃ NA: <li>dłuższe RNA (pre-miRNA) albo

### z04-22a  (pozycja raportu nr 22; M)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: Dwuniciowe DNA ma zawsze kształt podwójnej helisy.
ZAMIEŃ NA: Dwuniciowe DNA ma kształt podwójnej helisy.

### z04-22b  (pozycje raportu nr 22 i 43; M/J – źródło: „większe zróżnicowanie strukturalne i funkcjonalne”)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: Dlatego rodzajów RNA jest dużo więcej niż rodzajów DNA (następny podrozdział).
ZAMIEŃ NA: Stąd większe zróżnicowanie RNA – strukturalne i funkcjonalne (rodzaje RNA opisuje następny podrozdział).

### z04-23  (pozycja raportu nr 23; M – źródło: „Uważa się, że…”)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: – ta technika daje DNA o najwyższej czystości;
ZAMIEŃ NA: – uważa się, że ta technika daje DNA o najwyższej czystości;

### z04-24  (pozycja raportu nr 24; M – „prosta w wykonaniu” źródło mówi o kolumnowej izolacji RNA, nie DNA)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: <p>Prosta w wykonaniu jest <b>metoda kolumnowa</b> – to trzeci sposób z listy.
ZAMIEŃ NA: <p><b>Metoda kolumnowa</b> to trzeci sposób z listy.

### z04-29  (pozycja raportu nr 29; M – 146 + 60 = 206)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: przypada więc ok. 200 par zasad (146 + 60)
ZAMIEŃ NA: przypada więc nieco ponad 200 par zasad (146 + 60 = 206)

### z04-36  (pozycja raportu nr 36; Z)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: przyłącza się do węgla 1′ wiązaniem <b>N-glikozydowym</b>, a fosforan
ZAMIEŃ NA: przyłącza się do węgla 1′ wiązaniem <b>N-glikozydowym</b> (łączy ono cukier z atomem azotu zasady), a fosforan

### z04-37  (pozycja raportu nr 37; Z)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: to aktywność <b>egzonukleazy 3′→5′</b>, czyli korekta
ZAMIEŃ NA: to aktywność <b>egzonukleazy 3′→5′</b> (egzonukleaza odcina nukleotydy od końca nici), czyli korekta

### z04-41  (pozycja raportu nr 41; J)
PLIK: rozdzialy/z04-kwasy-nukleinowe.html
ZNAJDŹ: Zestaw to z bakteriami: tam
ZAMIEŃ NA: Porównaj to z bakteriami: tam

### B. SKŁAD / RYCINY / UKŁAD (Opus)
- z04-B1 (poz. 3, 5, 10, 40) ryciny z banku k4 mają etykiety spoza źródeł E: ryc. 3 A (formy helisy) – A-DNA „ok. 11 par na skręt, krótsza i szersza” (sprzeczne z tabelą części 2, gdzie dla A-DNA „–”); ryc. 8 (tRNA) – „…CCA”, „ramię akceptorowe”, „pętla D”, „pętla T”, „pętla zmienna”; ryc. 9 (splicing) – „5′UTR”, „3′UTR”, „AUG … STOP”, „GU/AG”, „spliceosom”. Tekst ograniczono do półzdań potrzebnych do odczytania rycin. Do zrobienia na pewno: usunąć z ryc. 3 A liczbę „ok. 11 par” i z ryc. 9 etykiety UTR/AUG/STOP (niewyjaśnione nigdzie w tekście). Reszta – zob. D-4.
- z04-B2 (poz. 44) s. 21: strona zapełniona w 19% – sama ramka „Dalej: część 2” (pod „W 60 sekund” na s. 20 zabrakło ok. 15–20 px; stan/z04-v3 podpowiada skrócenie komórki „Tkanka/DNA” w tabeli DNA–RNA).
- z04-B3 (poz. 45, 46) tabele z samotnym wierszem: „Forma / Skręt / Najważniejsze cechy” – wiersz Z-DNA sam na s. 5; tabela grup funkcyjnych zasad (s. 22) – wiersz „guanina” sam w drugim łamie.
- z04-B4 (poz. 47, 48) tabela „Białko / enzym” 7 + 3 wiersze (s. 9→10), ryc. 7 dopiero pod nią; tabela „Polimerazy DNA – która do czego?” rozcięta między łamy (2 + 3 wiersze).
- z04-B5 (poz. 49) s. 5 (prawy łam), s. 8 (lewy), s. 18 (prawy) – łamy kończą się 15–20% przed dołem strony.
- z04-B6 (poz. 51) tabele części 2 (s. 24–26): kolumny liczbowe do prawej obok „–” do lewej; kolumna „Białka” (s. 26) oderwana od reszty wiersza – ujednolicić wyrównanie.
- z04-B7 (poz. 39) `pageref` do h2 zamiast do miejsca treści: „dodatnie superskręty” → `#c04-helisa` (s. 3; treść na s. 5 – dodać id do h3 „Superskręcenie”); „fragmenty Okazaki” (s. 3) → s. 6 zamiast s. 8; „RNA telomerazy” → `#c04-rna` (s. 12; treść na s. 14).
- z04-B8 po poprawkach z04-6a…6d i z04-14b sprawdzić, czy ryc. „Widełki replikacyjne” i ryc. „Poziomy upakowania” nie mają etykiet sprzecznych z nowym tekstem (np. „koraliki”, „topo I/II”).

### C. ODRZUCONE: 17
Limit stron (nieaktualny), liczby potwierdzone na skanie (10⁹–10¹⁰ przy korekcie – stan/z04-v3; „>10⁹” wiązań – Drewa s. 33; „3–6 µg” i „1–2 × 10⁷ komórek” – Ostrowska s. 56, sprawdzone teraz), uproszczenia części 1 rozwijane w części 2 (starter RNA, polimerazy), wierne oddanie niespójnego źródła (modele replikacji, potrójna helisa), przypomnienia z rozdz. 6 i 9, przykład RNAi oznaczony jako rozumowanie, linie „Źródło” (po poprawkach zgodne).

---

## Z05 – PCR, enzymy restrykcyjne, przesiew, markery, diagnostyka (70 zgłoszeń)

### A. TEKST

### z05-1  (pozycja raportu nr 17; M – Drewa nie mówi, „niż co”; to wniosek z kontekstu)
PLIK: rozdzialy/z05-pcr.html
ZNAJDŹ: łączące PCR z ligacją, jak OLA, są znacznie czulsze niż ASA i hybrydyzacja ASO.
ZAMIEŃ NA: łączące PCR z ligacją, jak OLA, mają znacznie większą czułość (z kontekstu: w porównaniu z opisanymi tuż przedtem ASA i hybrydyzacją ASO).

### z05-2  (pozycja raportu nr 19; M – fakt spoza źródła)
PLIK: rozdzialy/z05-pcr.html
ZNAJDŹ: Metycylina sama jest antybiotykiem β-laktamowym, a MRS są w praktyce
ZAMIEŃ NA: MRS są w praktyce

### z05-3  (pozycja raportu nr 20; M – kierunki transportu LDL/HDL spoza źródła)
PLIK: rozdzialy/z05-pcr.html
ZNAJDŹ: przypomnij sobie dwie frakcje cholesterolu. LDL przenosi cholesterol z wątroby do tkanek, a jego nadmiar sprzyja odkładaniu się blaszek miażdżycowych w tętnicach („zły cholesterol”). HDL zabiera nadmiar cholesterolu z tkanek do wątroby („dobry cholesterol”). Wariant związany z większym stężeniem LDL wiąże się więc z większym ryzykiem, a wariant związany z dużym stężeniem HDL – z mniejszym.
ZAMIEŃ NA: wystarczy wiedzieć, że LDL i HDL to dwie frakcje cholesterolu we krwi; źródło łączy większe stężenie cholesterolu LDL z większym ryzykiem choroby niedokrwiennej serca.

### z05-4a  (pozycja raportu nr 26; M – „dziś”, „najnowsze” = stan z 2011 r.)
PLIK: rozdzialy/z05-pcr.html
ZNAJDŹ: <p>Najnowszym osiągnięciem jest wprowadzenie mikromacierzy. Głównym przedmiotem zainteresowania są dziś testy wysokowydajne, a zaawansowana automatyzacja i postęp w mikro- i nanotechnologii pozwalają ulepszać wprowadzane techniki.</p>
ZAMIEŃ NA: <p>Za najnowsze osiągnięcie źródło (2011) uznaje wprowadzenie mikromacierzy. Głównym przedmiotem zainteresowania były wtedy testy wysokowydajne, a zaawansowana automatyzacja i postęp w mikro- i nanotechnologii pozwalały ulepszać wprowadzane techniki.</p>

### z05-4b  (pozycja raportu nr 26; M)
PLIK: rozdzialy/z05-pcr.html
ZNAJDŹ: <p>Do niedawna DNA sekwencjonowano prawie wyłącznie metodą Sangera
ZAMIEŃ NA: <p>Źródło (2011) podaje, że do niedawna DNA sekwencjonowano prawie wyłącznie metodą Sangera

### z05-4c  (pozycja raportu nr 26; M)
PLIK: rozdzialy/z05-pcr.html
ZNAJDŹ: Od kilku lat istnieje alternatywa – <b>pirosekwencjonowanie</b>.
ZAMIEŃ NA: Jako nowszą alternatywę wymienia <b>pirosekwencjonowanie</b>.

### z05-5  (pozycje raportu nr 30 i 50; J – wyliczenie z myślnikami o dwóch funkcjach)
PLIK: rozdzialy/z05-pcr.html
ZNAJDŹ: <p>Stąd szerokie zastosowania PCR: wykrywanie drobnoustrojów (powielony fragment genomu bakterii, wirusa, grzyba czy pierwotniaka potwierdza zakażenie lub inwazję), namnażanie wybranych fragmentów DNA i RNA (RNA najpierw przepisuje się na cDNA), alternatywa dla klonowania – PCR powieli nawet bardzo rzadką sekwencję z mieszaniny, o ile znamy sekwencje, które ją otaczają – badanie bardzo starego i skąpego materiału, np. plamy zaschniętej krwi (dlatego PCR jest ważną metodą kryminalistyki), oraz diagnostyka chorób genetycznych i nowotworów.</p>
ZAMIEŃ NA: <p>Stąd szerokie zastosowania PCR:</p>
  <ul>
    <li>wykrywanie drobnoustrojów – powielony fragment genomu bakterii, wirusa, grzyba czy pierwotniaka potwierdza zakażenie lub inwazję;</li>
    <li>namnażanie wybranych fragmentów DNA i RNA (RNA najpierw przepisuje się na cDNA);</li>
    <li>alternatywa dla klonowania – PCR powieli nawet bardzo rzadką sekwencję z mieszaniny, o ile znamy sekwencje, które ją otaczają;</li>
    <li>badanie bardzo starego i skąpego materiału, np. plamy zaschniętej krwi (dlatego PCR jest ważną metodą kryminalistyki);</li>
    <li>diagnostyka chorób genetycznych i nowotworów.</li>
  </ul>

### z05-6  (pozycja raportu nr 31; Z – skrót użyty przed wyjaśnieniem)
PLIK: rozdzialy/z05-pcr.html
ZNAJDŹ: <td>4. dNTP – dATP, dGTP, dTTP i dCTP</td>
ZAMIEŃ NA: <td>4. dNTP (trifosforany deoksyrybonukleotydów) – dATP, dGTP, dTTP i dCTP</td>

### z05-7  (pozycja raportu nr 32; Z)
PLIK: rozdzialy/z05-pcr.html
ZNAJDŹ: wchodzi w fazę logarytmicznego przyrostu ilości produktu.</p>
ZAMIEŃ NA: wchodzi w fazę logarytmicznego przyrostu ilości produktu – czyli gdy krzywa zaczyna szybko rosnąć.</p>

### z05-8  (pozycja raportu nr 34; Z – wiszący liczebnik przepisany ze źródła)
PLIK: rozdzialy/z05-pcr.html
ZNAJDŹ: <p>Trzecim typem sekwencji spełniających kryteria markera DNA są
ZAMIEŃ NA: <p>Kolejnym typem sekwencji spełniających kryteria markera DNA są

### z05-9  (pozycja raportu nr 51; J)
PLIK: rozdzialy/z05-pcr.html
ZNAJDŹ: Grupy różnią się tym, czym wychwytuje się zmienność: sondą, samym PCR – z dowolnie dobranym (arbitralnym) starterem albo ze starterami pasującymi do znanej sekwencji – PCR połączonym z trawieniem restrykcyjnym albo badaniem pojedynczej nici DNA (jak w SSCP,
ZAMIEŃ NA: Grupy różnią się tym, czym wychwytuje się zmienność. Może to być sonda. Może to być sam PCR – ze starterem dobranym dowolnie (arbitralnym) albo ze starterami pasującymi do znanej sekwencji. Może to być PCR połączony z trawieniem restrykcyjnym. Wreszcie – badanie pojedynczej nici DNA (jak w SSCP,

### z05-10  (pozycja raportu nr 48; J – pisownia jak w rozpisce i w reszcie rozdziału: „allelospecyficzna”)
PLIK: rozdzialy/z05-pcr.html
ZNAJDŹ (WSZYSTKIE 4 wystąpienia w pliku – 3 w tekście, 1 w atrybucie data-title ryciny c05-fig-asa): allelo-specyficzn
ZAMIEŃ NA: allelospecyficzn

### B. SKŁAD / RYCINY / UKŁAD (Opus)
- z05-B1 (poz. 54) ryc. 1 (cykl PCR), panel A: etykieta „denaturacja ~95 °C” nachodzi na oś i krawędź pola, „przyłączanie” leży na linii profilu, podpis „cykl powtarza się ok. 36–40 razy” na dolnej krawędzi ramki.
- z05-B2 (poz. 21, 66) ryc. 2 (RT-PCR, PNG c05-fig-rt): etykieta „mRNA (tylko eksony)” – fakt usunięty z tekstu decyzją szefa (stan/z05-v3: zmienić na „mRNA”); etykiety „odwrotna transkryptaza” i „starter” ok. 6 pt na kolorowych nitkach – nieczytelne.
- z05-B3 (poz. 65) ryc. 6 (mapa restrykcyjna): ścieżka „M” na żelu nieopisana w podpisie (dodać „M – wzorzec wielkości”).
- z05-B4 (poz. 40) ryc. 7 (SSCP): schemat pokazuje jedną nić na wariant, żel – po dwa prążki na ścieżkę; podpis nie wyjaśnia, że dwa prążki to dwie nici.
- z05-B5 (poz. 60) ryc. 11 (ASA): podtytuł styka się z etykietami ścieżek „N M N M N M”; po poprawce z05-10 sprawdzić tytuł ryciny („allelospecyficzna”) i ewentualną etykietę w SVG.
- z05-B6 (poz. 56, 57, 59) puste dolne ćwiartki stron: s. 8 (ryc. 4 dopiero na s. 9), s. 11 (ryc. 6 na s. 12), s. 16 (ramka „Przykład” przeniesiona na s. 17). Numery = build `--only 05`.
- z05-B7 (poz. 55, 61, 62, 63) tabele: „Co musi być w probówce?” – nagłówek + 1 wiersz na dole s. 1; VNTR/STR (s. 21) – ostatni wiersz sam w prawym łamie; tabela 4 genów – wiersz PON sam na s. 27, obok pusta prawa kolumna; sześć enzymów 4 + 2 (s. 29–30).
- z05-B8 (poz. 58, 69) osierocone nagłówki: h3 „Cztery etapy – po co każdy?” + 1 zdanie na dole s. 15; h2 „Cztery dalsze odmiany PCR” + 3 linie na dole s. 31.
- z05-B9 (poz. 64) odsyłacze do ryc. 13 A/B stoją na s. 22–23, rycina dopiero na s. 24.
- z05-B10 (poz. 68) linia „Źródło” poprzedniej sekcji ląduje na górze następnej strony/łamu tuż nad nowym h2 (s. 3, s. 30) – trzymać ją z ostatnim akapitem sekcji (`break-before: avoid`).
- z05-B11 (poz. 45) `pageref` do h2 zamiast do tabeli: „liczby powtórzeń – część 2” → s. 32 (tabela na s. 33); „sześć genów – część 2” → s. 34 (tabela na s. 35).

### C. ODRZUCONE: 41
Liczby i nazwy potwierdzone na skanie (stan/z05-v3: 5%, 95%, 5 kb, C516T, Ser474Ter, VV405, DMD, biotyna 5′; teraz dodatkowo Ostrowska s. 54: „dDTP” i „10ⁿ-krotne” – ramki „Uwaga do źródła” są słuszne), podstawy PCR i mechanizm ASA z materiału pomocniczego (zostają – decyzje D1, D2), mechanizm metylazy (jest w materiale pomocniczym k5), przypomnienia z rozdz. 4 i 6, krótkie meta-komentarze w części 2, limit stron, rodzaj żeński „gniazdowa PCR” (tak w źródle), terminologia źródeł (kb/kpz, STRP/STR).

---

## Z06 – Elektroforeza, hybrydyzacja, sekwencjonowanie, identyfikacja genetyczna (43 zgłoszenia)

Uwaga: ten rozdział zweryfikowano w trybie lekkim (zmiana zlecenia w trakcie pracy) – pozycje „do sprawdzenia” rozstrzygane z opisu i z jednego odczytu tekstu, bez sięgania do skanu.

### A. TEKST

### z06-1  (pozycja raportu nr 7; M – źródło: można amplifikować, ale to trudne i wymaga DNA wysokiej jakości)
PLIK: rozdzialy/z06-elektroforeza-hybrydyzacja.html
ZNAJDŹ: <p>Ale PCR słabo radzi sobie z <b>długimi</b> odcinkami.
ZAMIEŃ NA: <p>Ale namnażanie <b>długich</b> odcinków jest dla PCR trudne.

### z06-2  (pozycja raportu nr 9; M – zdanie przeczyło RFLP opisanemu dalej)
PLIK: rozdzialy/z06-elektroforeza-hybrydyzacja.html
ZNAJDŹ: Dzięki temu u każdego człowieka ten sam odcinek genu trafia zawsze do fragmentu o tej samej długości – i właśnie tę długość będziemy oglądać.
ZAMIEŃ NA: Dzięki temu w każdej kopii tego samego DNA cięcie wypada w tych samych miejscach, więc szukany odcinek trafia do fragmentu o określonej długości – i właśnie tę długość będziemy oglądać.

### z06-3  (pozycja raportu nr 11; M – dopisane ponad źródło)
PLIK: rozdzialy/z06-elektroforeza-hybrydyzacja.html
ZNAJDŹ:  Artefakt pojawia się zwykle w jednej.
ZAMIEŃ NA: (USUŃ)

### z06-4  (pozycja raportu nr 15; M – „używanego przy śladach” dopisane)
PLIK: rozdzialy/z06-elektroforeza-hybrydyzacja.html
ZNAJDŹ: wskaźnika <b>LR</b> używanego przy śladach:
ZAMIEŃ NA: wskaźnika <b>LR</b>:

### z06-5  (pozycja raportu nr 16; M – „wtedy” łączyło przyczynowo dwa osobne stwierdzenia źródła)
PLIK: rozdzialy/z06-elektroforeza-hybrydyzacja.html
ZNAJDŹ: prawdopodobieństwo ojcostwa wynosi wtedy zwykle 99,9999%
ZAMIEŃ NA: prawdopodobieństwo ojcostwa wynosi zwykle 99,9999%

### z06-6  (pozycja raportu nr 27; Z – lista ma trzy punkty, różnice są w dwóch pierwszych)
PLIK: rozdzialy/z06-elektroforeza-hybrydyzacja.html
ZNAJDŹ: z dwiema różnicami wynikającymi z natury RNA:</p>
ZAMIEŃ NA: z dwiema różnicami wynikającymi z natury RNA (kroki 1 i 2):</p>

### z06-7  (pozycja raportu nr 32; Z)
PLIK: rozdzialy/z06-elektroforeza-hybrydyzacja.html
ZNAJDŹ: (miniSTR) albo bada mtDNA.
ZAMIEŃ NA: (miniSTR) albo bada mtDNA (DNA mitochondrialne).

### z06-8a  (pozycja raportu nr 34; Z – notatka robocza w tekście dla studenta)
PLIK: rozdzialy/z06-elektroforeza-hybrydyzacja.html
ZNAJDŹ: którego stron nie mieliśmy. Drewa wspomina o białkach tylko pobocznie, więc podstawy (ładunek białka, SDS-PAGE, HbA i HbS) podano skrótowo – trzeba je uzupełnić z Jordego.
ZAMIEŃ NA: z którego ten podrozdział nie korzysta. Drewa wspomina o białkach tylko pobocznie, więc podstawy (ładunek białka, SDS-PAGE, HbA i HbS) podano tu skrótowo – warto je porównać z Jordem.

### z06-8b  (pozycja raportu nr 34; Z)
PLIK: rozdzialy/z06-elektroforeza-hybrydyzacja.html
ZNAJDŹ: Źródło: Drewa s. 715, 717, 732 · Jorde s. 42–43 (brak dostępu)</p>
ZAMIEŃ NA: Źródło: Drewa s. 715, 717, 732</p>

### z06-9  (pozycja raportu nr 36; J)
PLIK: rozdzialy/z06-elektroforeza-hybrydyzacja.html
ZNAJDŹ: zasada jest podobna jak w klasycznej CGH
ZAMIEŃ NA: zasada jest podobna do tej z klasycznej CGH

### B. SKŁAD / RYCINY / UKŁAD (Opus)
- z06-B1 (poz. 37) s. 11: ok. 22% pustego miejsca na dole obu łamów; ryc. 7 (pirosekwencjonowanie) dopiero na s. 12.
- z06-B2 (poz. 38) s. 9: osierocony nagłówek „Szukanie delecji i duplikacji…” + sama ramka „Pojęcie” na dole prawego łamu, treść na s. 10.
- z06-B3 (poz. 39) ryc. 2 (transfer): tekst mówi „membranę kładzie się na żelu”, na rycinie w panelach 1 i 3 membrana leży pod żelem – uzgodnić (do obejrzenia).
- z06-B4 (poz. 40, 41) numeracja rycina ↔ tekst: ryc. 7 ma numery 1–3, lista w tekście 4 punkty (apyraza bez numeru); ryc. 4 (Southern) ma 5 paneli, tekst 6 kroków.
- z06-B5 (poz. 42) s. 5: ramka „Pojęcie: Hapten” przerywa listę numerowaną między pkt 2 i 3; ramka „Przykład 2 × 4 = 8” stoi przy pkt 3 zamiast przy pkt 2.
- z06-B6 (poz. 33) `pageref` do h2 zamiast do miejsca treści: s. 14 → „s. 22” (treść na s. 23), s. 9 → „s. 18” (kolonie na s. 19).
- z06-B7 (poz. 23) ryc. 4: etykiety „obciążnik”, „podsiąka przez bibułę” – nie ma ich w źródle (Drewa: „warstwa higroskopijna”); do decyzji przy przeglądzie rycin.

### C. ODRZUCONE: 27 (tryb lekki)
Elektroforeza białek, przypomnienie ddNTP, wstęp do STR i ojcostwa ze s. 765–768 i 779 (zostają na życzenie zleceniodawcy), limit stron i liczba rycin, wartości z ryc. 29.4 i tab. 29.2 odczytane ze skanu (stan/z06-v3), domysły oznaczone w tekście jako domysły, objaśnienia logiczne, powtórzenie Pojęcie/akapit. Nierozstrzygnięte w trybie lekkim i zostawione bez zmian: poz. 13 („RT-PCR” = PCR w czasie rzeczywistym), 14 (brzmienie hipotez PI w części 1), 18 (liczby dla MLP), 28 (skąd „4” we wzorze PI), 30 (AATG a TCAT).

---

## Z07–Z11 – NIEZWERYFIKOWANE
Weryfikacja przerwana po rozdziale 06 na polecenie zleceniodawcy (rozdziały od z07 przejmuje inny agent). Raporty `rewizja3/z07.md` … `z11.md` nie były czytane.

---

## D. DO DECYZJI ZLECENIODAWCY (stan po front + z01–z06)
- D-1 (front poz. 1) podtytuł okładki „Od cyklu komórkowego do analizy genomu” nie odpowiada spisowi; propozycja: „Od genomu i cyklu komórkowego do biotechnologii”.
- D-2 (front poz. 8) pierwszy rozdział ma etykietę „G” zamiast „01” – zostawić (i dopisać zdanie wyjaśnienia na s. „Jak korzystać”) czy przenumerować na 01?
- D-3 (front poz. 9) spis treści nie pokazuje sekcji części 2 (tylko jedna pozycja „Część 2” na rozdział) – dodać je do spisu?
- D-4 (z04 poz. 3, 5, 40) ryciny z banku k4 (tRNA, splicing) mają etykiety spoza źródeł (CCA, pętle D/T, GU/AG, spliceosom, lasso): zostawić z półzdaniem w podpisie (stan obecny) czy oczyścić ryciny?
- D-5 (z02 poz. 49, z03 poz. 29) nazwiska zapisane w źródle błędnie („Fleming”, „Horovitz”), w tekście poprawnie („W. Flemming”, „R. Horvitz” – decyzja Z6 z 18.11): zostają, czy – jak Singer/Tjio – usuwamy nazwiska?
- D-6 (z06 poz. 28) wzór PI = 1 / (4 × p) podany bez wyjaśnienia, skąd czwórka (źródło też nie wyjaśnia) – dopisać wyprowadzenie jako „Przykład” czy zostawić?
