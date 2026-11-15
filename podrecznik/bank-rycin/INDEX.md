# Bank rycin – indeks

Gotowe ryciny wycięte wektorowo (SVG, tekst jako krzywe, kolory oryginału) z opracowań kolokwium 4, kolokwium 5 i „Genomiki”.
Wstawienie do rozdziału – jeden znacznik (szczegóły: `KOMPONENTY.md`, p. 6):

```html
<figure class="fig" id="c05-fig-cykl" data-bank="k5-ryc-04" data-title="Cykl PCR">
  <figcaption>Własny podpis, 1–2 wiersze.</figcaption>
</figure>
```

Podgląd miniatur: `podglad-k4.png`, `podglad-k5.png`, `podglad-g.png`. Ryciny `k6-` dojdą w następnej turze.
„Wymiary” = szerokość × wysokość w druku (build wstawia rycinę z banku na obie kolumny, 179 mm, skala ≈ 1:1);
w nawiasie – część wysokości pola zadruku (250 mm). Rycina wielopanelowa idzie w całości.

## k4- · Kwasy nukleinowe – kolokwium 4 (18 rycin; tekst opracowania: `material/k4.txt`)

| id | tytuł | źródło | wymiary | co pokazuje (z podpisu) |
|---|---|---|---|---|
| `k4-ryc-01` | Nukleotyd i nukleozyd | k4 s. 6 | 179 × 130 mm (≈ 1/2) | A – trzy części nukleotydu i numeracja węgli cukru. Zasada wisi na węglu 1′, fosforan na węglu 5′, a wolne 3′-OH czeka na kolejny nukleotyd. |
| `k4-ryc-02` | Nić DNA i para nici | k4 s. 7 | 179 × 94 mm (≈ 1/3) | A – jedna nić: szkielet cukrowo-fosforanowy, wiązania 3′→5′-fosfodiestrowe i dwa różne końce. B – dwie nici łączą się parami zasad (A z T, G z C) i biegną w przeciwnych kierunkach. |
| `k4-ryc-03` | Formy podwójnej helisy | k4 s. 9 | 179 × 160 mm (≈ 2/3) | A – trzy najważniejsze formy w tej samej skali: szeroka A, typowa B i wydłużona, zygzakowata Z. B – wszystkie sześć form; prawoskrętne to A, B, C, D i E, lewoskrętna jest tylko Z. |
| `k4-ryc-04` | Nukleosom i solenoid | k4 s. 12 | 179 × 143 mm (≈ 1/2) | A – nukleosom: oktamer histonów z owiniętym DNA i histonem H1 na zewnątrz. Po prawej: dodatnie histony przyciągają ujemne DNA. |
| `k4-ryc-05` | Poziomy upakowania DNA | k4 s. 13 | 179 × 90 mm (≈ 1/3) | Sześć kolejnych poziomów: od podwójnej helisy (2 nm) do chromosomu metafazowego (1400 nm). Na kolokwium pytano o nukleosomy (11 nm) i solenoid (30 nm). |
| `k4-ryc-06` | DNA a RNA | k4 s. 16 | 179 × 125 mm (≈ 1/2) | A – trzy różnice widoczne w budowie: grupa –OH przy 2′ w rybozie, grupa metylowa w tyminie, której brak w uracylu, oraz liczba nici. |
| `k4-ryc-07` | Rodzaje RNA i miejsca ich działania | k4 s. 18 | 179 × 141 mm (≈ 1/2) | A – podział RNA na kodujące i niekodujące wraz z jednym słowem o funkcji każdego rodzaju. B – gdzie w komórce działa każdy rodzaj: snoRNA w jąderku, snRNA w jądrze, mRNA, tRNA, rRNA oraz miRNA i siRNA w cytoplazmie. |
| `k4-ryc-08` | tRNA | k4 s. 20 | 179 × 113 mm (≈ 1/2) | A – „koniczyna”: ramię akceptorowe z aminokwasem na końcu 3′, pętle D i T oraz pętla antykodonowa. B – antykodon 3′-UAC-5′ paruje z kodonem 5′-AUG-3′, więc tRNA przynosi metioninę. |
| `k4-ryc-09` | snoRNA i RNA telomerazy | k4 s. 22 | 179 × 94 mm (≈ 1/3) | A – snoRNA paruje z rRNA i wskazuje enzymowi nukleotyd do zmiany. B – RNA telomerazy jest matrycą: paruje z końcem chromosomu, a telomeraza dobudowuje kolejne GGTTAG. |
| `k4-ryc-10` | Dojrzewanie mRNA i splicing | k4 s. 25 | 179 × 141 mm (≈ 1/2) | A – od pre-mRNA do dojrzałego mRNA: najpierw czapeczka i ogon poli(A), potem spliceosom wycina introny (w kształcie lassa) i łączy eksony. |
| `k4-ryc-11` | Interferencja RNA: miRNA i siRNA | k4 s. 26 | 179 × 135 mm (≈ 1/2) | Obie drogi zaczynają się od dłuższego RNA, które Dicer tnie na krótkie fragmenty. miRNA pasuje do mRNA częściowo i hamuje translację; siRNA pasuje w całości i prowadzi do zniszczenia mRNA. |
| `k4-ryc-12` | Replikacja semikonserwatywna | k4 s. 28 | 179 × 122 mm (≈ 1/2) | A – trzy hipotezy rozdzielenia nici; prawdziwa jest semikonserwatywna. B – doświadczenie Meselsona i Stahla: położenie prążków DNA po 0, 1 i 2 podziałach w ciężkim, a potem lekkim azocie. |
| `k4-ryc-13` | Trzy etapy replikacji | k4 s. 30 | 179 × 139 mm (≈ 1/2) | A – inicjacja: białka wiążą ori, DNA się rozplata, powstaje bańka z dwojgiem widełek. B – elongacja: w każdych widełkach jedna nić powstaje w sposób ciągły, druga we fragmentach Okazaki. |
| `k4-ryc-14` | Nić opóźniona krok po kroku | k4 s. 31 | 179 × 104 mm (≈ 1/3) | Pięć kroków, które zamieniają fragmenty Okazaki w ciągłą nić: starter od prymazy, wydłużenie przez polimerazę, usunięcie startera, wypełnienie luki, połączenie przez ligazę. |
| `k4-ryc-15` | Widełki replikacyjne | k4 s. 34 | 179 × 125 mm (≈ 1/2) | Wszystkie białka z tabeli w jednym miejscu. |
| `k4-ryc-16` | Topoizomerazy | k4 s. 36 | 179 × 125 mm (≈ 1/2) | A – DNA zrelaksowane i superskręcone; przed widełkami helikaza wytwarza napięcie, które usuwa topoizomeraza. B – topoizomeraza I tnie jedną nić. |
| `k4-ryc-17` | Telomery i telomeraza | k4 s. 37 | 179 × 126 mm (≈ 1/2) | A – problem końców: po usunięciu ostatniego startera nowa nić jest krótsza. B – telomeraza wydłuża koniec 3′ według matrycy z własnego RNA. |
| `k4-ryc-18` | Izolacja i ocena DNA | k4 s. 39 | 179 × 125 mm (≈ 1/2) | A – pięć kroków izolacji metodą kolumnową. B – spektrofotometr mierzy, ile światła UV pochłania próbka (kwasy nukleinowe przy 260 nm, białka przy 280 nm); elektroforeza w żelu rozdziela DNA według długości. |

## k5- · Analiza DNA i RNA – kolokwium 5 (26 rycin; tekst opracowania: `material/k5.txt`)

| id | tytuł | źródło | wymiary | co pokazuje (z podpisu) |
|---|---|---|---|---|
| `k5-ryc-01` | Materiał do badań DNA | k5 s. 5 | 179 × 126 mm (≈ 1/2) | A – źródła DNA do badań molekularnych, także w badaniach prenatalnych i preimplantacyjnych. |
| `k5-ryc-02` | Izolacja DNA i ocena preparatu | k5 s. 7 | 179 × 125 mm (≈ 1/2) | A – izolacja DNA metodą kolumnową, np. z wymazu z jamy ustnej: liza, wiązanie DNA ze złożem, płukanie i elucja. |
| `k5-ryc-03` | Składniki reakcji PCR | k5 s. 11 | 179 × 94 mm (≈ 1/3) | Co jest w probówce i do czego służy każdy składnik. Matryca dostarcza wzoru, startery wyznaczają początek i koniec kopiowanego fragmentu, a polimeraza buduje nowe nici z dNTP. |
| `k5-ryc-04` | Cykl PCR | k5 s. 13 | 179 × 143 mm (≈ 1/2) | A – profil temperatury w termocyklerze: denaturacja, przyłączanie starterów i wydłużanie powtarzają się ok. 36–40 razy. |
| `k5-ryc-05` | Ocena produktu PCR w żelu agarozowym | k5 s. 15 | 179 × 90 mm (≈ 1/3) | Ścieżka M – wzorzec wielkości. P1 – prążek oczekiwanej wielkości (350 pz): wynik dodatni. P2 – brak prążka. P3 – obok właściwego prążka dodatkowy produkt niespecyficzny. |
| `k5-ryc-06` | Enzymy restrykcyjne – pochodzenie i nazwy | k5 s. 17 | 179 × 67 mm (≈ 1/4) | A – system restrykcji i modyfikacji: metylaza znakuje własne DNA bakterii, a restryktaza tnie obce DNA faga, które takich znaczników nie ma. |
| `k5-ryc-07` | Jak często tną enzymy czwórkowe, szóstkowe i ósemkowe | k5 s. 18 | 179 × 45 mm (≈ 1/4) | Ten sam odcinek DNA o długości 8 tys. pz; czerwone kreski to miejsca cięcia. Enzym czwórkowy tnie średnio co 256 pz i daje bardzo małe fragmenty, szóstkowy – średnio co ok. 4096 pz, a ósemkowy tnie rzadko i daje duże fragmenty. |
| `k5-ryc-08` | Palindrom, cięcie i rodzaje końców | k5 s. 20 | 179 × 123 mm (≈ 1/2) | A – EcoRI rozpoznaje palindrom GAATTC i przecina obie nici między G i A. Oba fragmenty mają jednoniciowe końce 5′-AATT, czyli lepkie końce. |
| `k5-ryc-09` | Jak z wzorów restrykcyjnych powstaje mapa | k5 s. 22 | 179 × 96 mm (≈ 1/3) | Fragment DNA o długości 6 kb tnie się osobno enzymem EcoRI (E), osobno HindIII (H) i obydwoma naraz (E+H). EcoRI daje fragmenty 2 i 4 kb, HindIII – 5 i 1 kb, a oba enzymy – 2, 3 i 1 kb. |
| `k5-ryc-10` | Budowa wektora plazmidowego | k5 s. 26 | 179 × 60 mm (≈ 1/4) | Najważniejsze elementy wektora: ori – miejsce rozpoczęcia replikacji, od którego zależy liczba kopii; geny markerowe, np. oporności na ampicylinę (amp R ) i tetracyklinę (tet R ); miejsca cięcia MCS w obrębie genu markerowego – wstawka przerywa ten gen. |
| `k5-ryc-11` | Klonowanie krok po kroku | k5 s. 27 | 179 × 84 mm (≈ 1/3) | Cztery etapy klonowania: cięcie wektora i badanego DNA tym samym enzymem, łączenie lepkich końców ligazą, wprowadzenie zrekombinowanego plazmidu do komórek bakterii i selekcja na podłożu z antybiotykiem. |
| `k5-ryc-12` | Dlaczego RNA trzeba chronić | k5 s. 28 | 179 × 58 mm (≈ 1/4) | Rybonukleazy (RNazy) są w materiale biologicznym, na sprzęcie i w otoczeniu; są bardzo aktywne i trwałe, więc szybko rozkładają RNA. |
| `k5-ryc-13` | Trzy rodzaje starterów do odwrotnej transkrypcji | k5 s. 31 | 179 × 65 mm (≈ 1/4) | Oligo(dT) wiąże ogon poli(A) mRNA, losowe heksamery – wiele miejsc w różnych cząsteczkach RNA, a starter specyficzny (GSP) – tylko RNA badanego genu. |
| `k5-ryc-14` | Detekcja w PCR w czasie rzeczywistym | k5 s. 34 | 179 × 125 mm (≈ 1/2) | A – SYBR Green świeci przy każdym produkcie: właściwym, niespecyficznym i przy strukturze primer-dimer. B – sonda TaqMan: dopóki jest cała, wygaszacz (W) tłumi reporter (R). |
| `k5-ryc-15` | Krzywe amplifikacji i krzywa wzorcowa | k5 s. 35 | 179 × 94 mm (≈ 1/3) | A – krzywe trzech próbek o różnej liczbie kopii na starcie. Próbka z największą liczbą kopii najwcześniej przekracza linię odcięcia, więc ma najniższe Ct. |
| `k5-ryc-16` | Nested PCR i multipleks PCR | k5 s. 37 | 179 × 128 mm (≈ 1/2) | A – nested PCR: najpierw startery zewnętrzne, potem na produkcie pierwszej reakcji startery wewnętrzne. B – multipleks PCR: trzy pary starterów powielają w jednej probówce trzy fragmenty różnej długości. |
| `k5-ryc-17` | Amplifikacja allelo-specyficzna (ASA) | k5 s. 38 | 179 × 94 mm (≈ 1/3) | Starter N kończy się nukleotydem pasującym do allelu prawidłowego, a starter M – do allelu zmutowanego. Produkt powstaje tylko wtedy, gdy koniec 3′ startera pasuje do matrycy. |
| `k5-ryc-18` | Inne odmiany PCR | k5 s. 40 | 179 × 118 mm (≈ 1/2) | A – odwrócony PCR: startery pasują do znanego odcinka, ale powielają sąsiadujący, nieznany DNA. B – 3′ RACE: DNA z poli(T) wiąże się z ogonem poli(A) mRNA i jest starterem odwrotnej transkrypcji. |
| `k5-ryc-19` | SSCP – kształt pojedynczych nici | k5 s. 45 | 179 × 63 mm (≈ 1/4) | Produkt PCR denaturuje się formamidem, a pojedyncze nici fałdują się w kształt zależny od sekwencji. Nić z mutacją przyjmuje inny kształt, więc w niedenaturującym żelu poliakrylamidowym wędruje z inną szybkością niż nić prawidłowa. |
| `k5-ryc-20` | DGGE i TGGE – elektroforeza w gradiencie | k5 s. 46 | 179 × 58 mm (≈ 1/4) | W żelu z rosnącym stężeniem mocznika (DGGE) lub rosnącą temperaturą (TGGE) nici DNA zaczynają się rozdzielać. Fragment z mutacją ma inną temperaturę topnienia, więc daje prążek w innym miejscu niż fragment prawidłowy. |
| `k5-ryc-21` | PCR-RFLP – jak mutacja zmienia wzór restrykcyjny | k5 s. 47 | 179 × 107 mm (≈ 1/2) | Produkt PCR o długości 300 pz. 1 – allel prawidłowy z jednym miejscem cięcia daje fragmenty 100 i 200 pz. 2 – mutacja niszczy miejsce cięcia: zostaje jeden fragment 300 pz. 1+2 – heterozygota ma prążki obu alleli. 3 – mutacja tworzy nowe miejsce: trzy fragmenty. 4 – delecja 60 pz skraca jeden z fragmentów. |
| `k5-ryc-22` | OLA i LCR – metody oparte na ligacji | k5 s. 50 | 179 × 120 mm (≈ 1/2) | A – OLA: oligonukleotyd z biotyną (B) zostaje połączony z oligonukleotydem przyczepionym do płytki tylko wtedy, gdy oba pasują do matrycy. |
| `k5-ryc-23` | Markery STR i ustalanie ojcostwa | k5 s. 54 | 179 × 121 mm (≈ 1/2) | A – allele STR różnią się liczbą powtórzeń motywu CA, więc produkty PCR mają różną długość. Allele są kodominujące: heterozygota ma dwa prążki, homozygota – jeden. |
| `k5-ryc-24` | SNP i jego wykrywanie | k5 s. 55 | 179 × 92 mm (≈ 1/3) | A – dwa allele różniące się jednym nukleotydem w zaznaczonej pozycji. B – sonda w pełni komplementarna hybrydyzuje i daje sygnał; przy jednej niesparowanej pozycji hybrydyzacja nie zachodzi. |
| `k5-ryc-25` | RAPD i AFLP | k5 s. 57 | 179 × 125 mm (≈ 1/2) | A – RAPD: ten sam krótki starter przyłącza się w wielu miejscach, a produkt powstaje między dwoma miejscami zwróconymi ku sobie. |
| `k5-ryc-26` | Metody molekularne w diagnostyce zakażeń | k5 s. 63 | 179 × 128 mm (≈ 1/2) | A – materiał genetyczny wirusa wykrywa się metodą PCR już kilka dni po zakażeniu, zanim pojawią się przeciwciała (okienko serologiczne). |

## g- · Genomika – analiza genomu i genotypowanie (23 rycin; tekst opracowania: `material/genomika.txt`)

| id | tytuł | źródło | wymiary | co pokazuje (z podpisu) |
|---|---|---|---|---|
| `g-ryc-01` | Od genu do RNA i białka | g s. 8 | 179 × 224 mm (≈ 9/10) | A – budowa genu: promotor, eksony z częścią kodującą (CDS) i niekodującą (UTR), introny; B – z jednego pre-mRNA dwa różne mRNA (alternatywny splicing); C – z każdego mRNA inna izoforma białka; D – trzy poziomy opisu: genomika, transkryptomika, proteomika. |
| `g-ryc-02` | Zmiany DNA i ich skutki | g s. 13 | 179 × 224 mm (≈ 9/10) | A – rodzaje zmian sekwencji i ich skutek w białku (synonimiczna, zmiany sensu, nonsensowna, delecja 3 nt, insercja 1 nt); B – ekspansja powtórzeń CAG; C – większe zmiany: delecja, duplikacja i inwersja. |
| `g-ryc-03` | Od pytania do fragmentu, który zbadasz | g s. 15 | 179 × 178 mm (≈ 2/3) | Kolejne przybliżenia: od pytania, przez gen i transkrypt, do eksonów i ampliconu. Ten sam odcinek DNA może mieć różny numer eksonu w różnych transkryptach. |
| `g-ryc-04` | PCR krok po kroku | g s. 17 | 179 × 142 mm (≈ 1/2) | A – jeden cykl: denaturacja, przyłączenie starterów, wydłużanie. B – liczba kopii rośnie mniej więcej dwukrotnie w każdym cyklu, aż reakcja dochodzi do plateau. |
| `g-ryc-05` | Allele dropout: gdy namnaża się tylko jeden allel | g s. 18 | 179 × 99 mm (≈ 1/3) | Częsty wariant w miejscu wiązania startera blokuje namnażanie jednego allelu. Heterozygota wygląda wtedy w chromatogramie jak homozygota. |
| `g-ryc-06` | dNTP i ddNTP: o wszystkim decyduje grupa 3′-OH | g s. 20 | 179 × 162 mm (≈ 2/3) | dNTP i ddNTP różnią się jednym atomem przy węglu 3′. Wolna grupa 3′-OH pozwala dołączyć kolejny nukleotyd; jej brak kończy syntezę. |
| `g-ryc-07` | Jak odczytuje się sekwencję? | g s. 23 | 179 × 224 mm (≈ 9/10) | A – PCR: para starterów wyznacza amplikon; B – Sanger: jeden starter, wydłużanie zatrzymywane barwnym ddNTP; C – kapilara: krótsze fragmenty docierają do detektora wcześniej; D – chromatogram: sygnał zamieniony na litery, obok heterozygotyczny SNV. |
| `g-ryc-08` | Biblioteka NGS: przygotowanie fragmentów | g s. 25 | 179 × 169 mm (≈ 2/3) | DNA zostaje pocięte na krótkie fragmenty, które dostają adaptery, indeks próbki i opcjonalnie UMI. Indeks mówi, z której próbki pochodzi odczyt, a UMI – z której cząsteczki. |
| `g-ryc-09` | Sekwencjonowanie przez syntezę | g s. 26 | 179 × 173 mm (≈ 2/3) | Każdy klaster to tysiące kopii jednego fragmentu. W każdym cyklu aparat „fotografuje” barwę wszystkich klastrów naraz; seria zdjęć daje sekwencje. |
| `g-ryc-10` | Odczyty sparowane (paired-end) | g s. 27 | 179 × 173 mm (≈ 2/3) | Para odczytów z dwóch końców jednego fragmentu. Nieoczekiwana odległość albo położenie odczytów pary w genomie zdradza delecję lub rearanżację. |
| `g-ryc-11` | Krótkie i długie odczyty w trudnym regionie | g s. 29 | 179 × 162 mm (≈ 2/3) | Krótki odczyt z wnętrza powtórzenia pasuje do wielu miejsc. Długi odczyt sięga do unikatowych odcinków po obu stronach – i jednocześnie pokazuje, które warianty leżą na tej samej kopii chromosomu. |
| `g-ryc-12` | Dwie technologie długich odczytów | g s. 30 | 179 × 163 mm (≈ 2/3) | A – HiFi: wiele przejść po tej samej kolistej cząsteczce daje dokładny konsensus. B – nanopor: przechodząca nić zmienia prąd jonowy, a algorytm zamienia ten sygnał na litery. |
| `g-ryc-13` | RNA-seq: co mówią odczyty z RNA | g s. 32 | 179 × 198 mm (≈ 9/10) | Liczba odczytów na eksonach odzwierciedla ilość transkryptu, a odczyty rozpięte między eksonami pokazują, jak zostały połączone. |
| `g-ryc-14` | Analiza trio: co dają dane rodziców | g s. 36 | 179 × 93 mm (≈ 1/3) | Dane rodziców pokazują, czy wariant jest nowy (de novo) i czy dwa warianty dziecka pochodzą od różnych rodziców – a więc leżą na różnych kopiach genu. |
| `g-ryc-15` | Mikromacierz: rozpoznawanie przez komplementarność | g s. 38 | 179 × 144 mm (≈ 1/2) | Znakowane fragmenty próbki wiążą się tylko z pasującymi sondami. Skaner mierzy jasność każdego pola – im więcej pasującego materiału, tym silniejszy sygnał. |
| `g-ryc-16` | Macierz SNP: dwa wykresy, cztery sytuacje | g s. 39 | 179 × 111 mm (≈ 1/2) | Każda kropka to jedna badana pozycja. Górny wykres pokazuje ilość DNA, dolny – udział allelu B. Utrata, zysk kopii i region homozygotyczny dają charakterystyczne układy pasm. |
| `g-ryc-17` | Droga danych: od aparatu do raportu | g s. 42 | 179 × 124 mm (≈ 1/2) | Kolejne etapy analizy i pliki, które powstają po drodze. Fioletowe etykiety wskazują przykładowe programy używane na danym etapie. |
| `g-ryc-18` | Jak wyglądają pliki FASTQ i VCF | g s. 44 | 179 × 144 mm (≈ 1/2) | Rekord FASTQ to cztery linie: nazwa, sekwencja, separator i jakość zapisana znakami. Linia VCF opisuje jeden wariant – z genotypem i liczbą odczytów każdego allelu. |
| `g-ryc-19` | Gdzie leży wariant i co może zmienić | g s. 52 | 179 × 118 mm (≈ 1/2) | Położenie wariantu w genie wskazuje, jaki mechanizm warto sprawdzić: ilość RNA, skład transkryptu, sekwencję białka albo stabilność mRNA. |
| `g-ryc-20` | Przedwczesny STOP i degradacja mRNA (NMD) | g s. 53 | 179 × 132 mm (≈ 1/2) | Położenie przedwczesnego kodonu STOP decyduje, czy mRNA zostanie rozłożone (brak białka), czy przetłumaczone na skrócone białko. |
| `g-ryc-21` | Cztery mechanizmy działania wariantu | g s. 54 | 179 × 123 mm (≈ 1/2) | Utrata funkcji, haploinsuficjencja, nabycie funkcji i efekt dominująco negatywny. W kompleksie z czterech podjednostek jedna zmieniona wersja może zepsuć większość kompleksów. |
| `g-ryc-22` | SWISS-MODEL: jak powstaje model 3D | g s. 60 | 179 × 130 mm (≈ 1/2) | Od sekwencji przez wzorzec do modelu. Lokalna ocena jakości pokazuje, które fragmenty modelu są pewne, a które – jak pętla bez dobrego wzorca – tylko przybliżone. |
| `g-ryc-23` | Kd: siła wiązania na wykresie | g s. 64 | 179 × 93 mm (≈ 1/3) | Krzywa wariantu jest przesunięta w prawo: żeby związać połowę cząsteczek, potrzeba stukrotnie wyższego stężenia liganda. |

Razem: 67 rycin. Do pominięcia: brak (wszystkie sprawdzone na arkuszu podglądu i automatycznie – krawędzie bez uciętych elementów, bez tekstu spoza ryciny).
