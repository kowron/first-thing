# Plan podziału na dwie części – rozdział G (01) Genomika
Plik `rozdzialy/z01-genomika.html` · id `c01-` · źródło: opracowanie „Genomika” (s. = strona opracowania) · linie źródła: „prezentacja LMZ 3, slajdy X–Y”.

## 1. Bilans
- W rozdziale jest ok. 80–85% informacji opracowania: wszystkie definicje, reguły interpretacji i tabele rozdz. 01–18; tekst wierny (3 drobne wzmocnienia – pkt 7).
- Dochodzi ok. 15–20%: fakty T z wyciągu i treść rycin spoza banku (ryc. 1, 3, 4, 8, 12, 13, 15, 18, 22, 23) – 89 pozycji.
- Do ≈ 70/30 z części 1 schodzi 13 grup szczegółów (≈ 10–12%): progi predyktorów, DALI/Rosetta, PDBbind, opisy baz z rozdz. 16, mechanika długich odczytów, szczegóły HGVS.

## 2. Dopisać (część 2)

### R1
- s. 4: zestaw haploidalny = jeden komplet chromosomów (plemnik, komórka jajowa); komórki somatyczne mają dwa – diploidalne `[P1]` (pół zdania; część 1 używa „locus diploidalny” bez definicji)
- s. 5: 5 dziedzin genomiki: strukturalna (sekwencja i organizacja genomu), funkcjonalna (jak działają geny i inne elementy), porównawcza (co łączy i różni genomy gatunków), różnic indywidualnych (różnice między osobami jednego gatunku), teoretyczna (modele organizacji i ewolucji)
- s. 5: neuron a miocyt: inne geny aktywne, inne ilości RNA, inny zestaw białek i ich modyfikacje
- s. 5–6: transkryptom = wszystkie RNA (kodujące i niekodujące) w określonych komórkach i warunkach; badanie może objąć część (np. mRNA); transkryptomika: które transkrypty, ile, jak złożone; wynik zależy od tkanki, czasu, bodźców, przygotowania próbki
- s. 6: proteom = białka w danym układzie i stanie; proteomika: ilość, formy, modyfikacje, oddziaływania; izoforma = wersja białka z tego samego genu; modyfikacje: fosforylacja, przycięcie, glikozylacja (różnorodność bez zmiany DNA)
- s. 6: pre-mRNA → wycięcie intronów, połączenie eksonów, czapeczka na początku, ogon poli-A; ekson = fragment zostający w dojrzałym transkrypcie (CDS albo UTR); alternatywny splicing → kilka mRNA → izoformy
- s. 6: białko musi się zwinąć, trafić na miejsce, często zostać zmodyfikowane → ilość mRNA i ilość działającego białka zmieniają się w różnym tempie
- s. 6: przewidywany gen + pasujący transkrypt + peptydy wspierają się nawzajem; z sekwencji aminokwasów nie odtworzy się DNA (degeneracja; leucyna – 6 kodonów)
- s. 6: aktywność genów zależy też od organizacji chromatyny i kontaktów DNA w przestrzeni jądra
- s. 6: przykład: wariant splicingowy – DNA pokazuje zmianę, RNA skutek (skład mRNA), białko efekt końcowy
- s. 8 (ryc. 1D): genomika – co zapisane; transkryptomika – jakie transkrypty obecne; proteomika – jakie produkty działają
- s. 11: RP-PCR: jeden starter wiąże się w wielu miejscach wewnątrz ciągu powtórzeń → „drabinka” produktów, ujawnia także bardzo długie ekspansje

### R2
- s. 15 (ryc. 3A): pytanie → gen (NCBI Gene, Ensembl) → transkrypt z wersją (RefSeq, Ensembl) → eksony i CDS (Ensembl, UniProt) → amplikon (Primer-BLAST)
- s. 15 (ryc. 3C): przykład: białko 380 aa, domena aa 120–210 → c.358–c.630 (aa 210 = c.628–630) → eksony 3 i 4 transkryptu NM_xxxxxx.2 → 2 amplikony; startery w intronach, by odczyt objął cały ekson i obie granice
- s. 16: starter stawia się dalej od badanej pozycji, by nie wypadła na słabo czytelnym początku chromatogramu
- s. 16: skład PCR: para starterów, polimeraza DNA, nukleotydy; amplikon obejmuje też startery
- s. 17 (ryc. 4A): cykl: denaturacja ok. 95 °C (ciepło rozrywa wiązania wodorowe) → przyłączanie starterów ok. 50–65 °C → wydłużanie ok. 72 °C
- s. 16–17 (ryc. 4B): idealnie ×2 na cykl (1→2→4→8); zwykle 25–35 cykli; realna wydajność niższa; na końcu plateau (brakuje składników)
- s. 17: Primer-BLAST projektuje startery i sprawdza, czy pasują wyłącznie do wybranej sekwencji
- s. 20 (ryc. 6B): dNTP ma 3 fosforany; przy wbudowaniu odchodzą 2, a 3′-OH końca nici łączy się z fosforanem nowego nukleotydu (wiązanie fosfodiestrowe)

### R3
- s. 25 (ryc. 8): wstawka zwykle kilkaset pz; adaptery na obu końcach; indeksy bywają na obu końcach; układ elementów zależy od zestawu; multipleks = połączenie bibliotek wielu próbek w jedną pulę
- s. 26 (ryc. 9): nowsze aparaty używają mniej niż 4 kanałów barwnych
- s. 28: Maxam–Gilbert: chemiczne cięcie DNA przy określonych zasadach; historyczna, 1977 (rok metody Sangera)
- s. 28: pirosekwencjonowanie: wbudowanie nukleotydu uwalnia pirofosforan → reakcje enzymatyczne → błysk światła
- s. 28: SOLiD: ligacja znakowanych krótkich oligonukleotydów z matrycą, odczyt fluorescencji
- s. 30 (ryc. 12A): PacBio HiFi: adaptery-pętle zamykają dwuniciową wstawkę w koło; wstawka kilkanaście tys. zasad; przejścia czytają obie nici; w konsensusie w każdej pozycji wygrywa większość
- s. 29–30 (ryc. 12B): nanopory (Oxford Nanopore): por = białko w błonie, płyną przez niego jony; poziom prądu zależy od kilku zasad naraz (np. GTAC) → bardziej złożony algorytm niż rozpoznanie barwy; RNA czytane bez cDNA
- s. 30: cDNA buduje odwrotna transkryptaza (DNA na matrycy RNA)
- s. 32 (ryc. 13A): do biblioteki RNA-seq często wybiera się mRNA z ogonem poli-A
- s. 32 (ryc. 13B): przykład: 48 odczytów na złączu 1–2, 45 na 2–3, 6 na 1–3 → większość transkryptów 1–2–3, część pomija ekson 2
- s. 32 (ryc. 13C): transkrypt fuzyjny np. A1–A2–B2–B3; zdradza go odczyt przez złącze A2|B2

### R4
- s. 38 (ryc. 15): przebieg: jednoniciowe sondy w polach (w każdym inna) → znakowana próbka → płukanie usuwa niezwiązane → skaner pobudza znaczniki i mierzy jasność pól (jaśniej = więcej pasującego materiału); budowa zależy od platformy
- s. 40: testy kojarzy się z tym, co mierzą; liczby genów, wersje i wskazania się zmieniają → dokumentacja konkretnej wersji
- s. 40: FoundationOne CDx – panel NGS, profil DNA nowotworu z tkanki; Oncomine Focus – panel NGS, zmiany DNA i RNA, w tym fuzje; CytoScan Dx – mikromacierz: liczba kopii i SNP; Infinium OmniExpress – macierz do genotypowania wielu SNP; MyPath Melanoma – profil ekspresji genów, qRT-PCR; MyRisk – odrębny test dziedzicznej predyspozycji do nowotworów
- s. 40: qRT-PCR = ilościowy PCR po odwrotnej transkrypcji (RNA → cDNA, pomiar szybkości przyrostu produktu); porównuje ilość wybranych transkryptów
- s. 40: uwaga do slajdu: Oncomine Focus stoi przy mikromacierzach, a to NGS (część DNA – zmiany sekwencji i liczby kopii; część RNA – fuzje i transkrypty)
- s. 40: uwaga do slajdu: „Myriad myPath 21+ Cancer Panel” łączy dwa testy – MyPath Melanoma (ekspresja; ocena zmian melanocytowych) i MyRisk (dziedziczne ryzyko); zdjęcie przypomina materiały MyRisk
- s. 41: panel nowotworowy – zmiany pomocne w doborze leczenia; macierz – zaburzenia liczby kopii; profil ekspresji – klasyfikacja tkanki

### R5
- s. 44 (ryc. 18A): rekord FASTQ = 4 linie: @nazwa; sekwencja; „+”; znaki jakości (jeden na zasadę)
- s. 44: Phred+33: Q = kod ASCII − 33; I (73) = Q40, ? (63) = Q30, 5 (53) = Q20, + (43) = Q10
- s. 44 (ryc. 18B): kolumny VCF: CHROM, POS, ID („.” = puste), REF, ALT, QUAL (jakość wywołania, skala Phreda), FILTER (PASS), INFO (np. DP=60), FORMAT (klucz GT:AD:DP), próbka (0/1:31,29:60)
- s. 44: odczyt przykładu chr1:1234567 G>A: GT 0/1 – heterozygota; AD 31,29 – 31 odczytów G, 29 A; DP 60; VAF = 29/60 ≈ 48%
- s. 44 (ryc. 18C): rekord BAM/CRAM = sekwencja + jakość + miejsce w genomie + jakość dopasowania
- s. 45: 10 narzędzi: BLAST (sekwencje podobne, lokalne podobieństwo); SAMtools (sortowanie, indeksowanie BAM); GATK (m.in. wykrywanie wariantów); IGV (przeglądarka odczytów, pokrycia, anotacji); UGENE (sekwencje, dopasowania, adnotacje); Sequencher (sekwencje, m.in. Sangera); VariantStudio (anotacja, filtrowanie, przegląd wariantów); Lasergene (pakiet do sekwencji i analiz molekularnych); R i Python (obliczenia, statystyka, automatyzacja); MATLAB (komercyjne środowisko obliczeniowe)
- s. 42 (ryc. 17): etapy: SAMtools, IGV – po dopasowaniu; GATK – wykrywanie wariantów; VariantStudio – anotacja i filtrowanie; BLAST – osobne zadanie
- s. 45: IGV i UGENE otwarte, MATLAB własnościowy; podział opisuje sposób udostępniania, a wiarygodność wynika z poprawnego użycia, walidacji i kontroli jakości; slajdy mylą część przypisań
- s. 47: 10 000 zasad o Q30 → średnio ok. 10 błędnych wywołań (przy dobrej kalibracji); nie wiadomo, które

### R6
- s. 55: elementy opisu wariantu: symbol genu; referencja i wersja; zmiana w DNA; transkrypt i skutek; zygotyczność lub VAF – każdy z pytaniem, na które odpowiada (tabela)
- s. 55: pozycje intronowe liczy się od granicy najbliższego eksonu; pełny opis zawiera identyfikator referencji; warianty złożone – dokładniejszy opis HGVS; numer aminokwasu zależy od izoformy
- s. 56: SIFT = Sorting Intolerant From Tolerant; odczyt: 0,01 – szkodliwy; 0,20 i 0,80 – tolerowane
- s. 57: przykład: w konserwowanej pozycji wszystkie homologi mają glicynę → zamiana na dużą resztę aromatyczną może dać niski SIFT
- s. 57: tabela SIFT / PolyPhen-2: idea (konserwacja homologów / sekwencja + struktura), kierunek skali, zastosowanie (podstawienia aminokwasów), rola (dowód pomocniczy)
- s. 59: fałd = kolejność i ułożenie helis α i harmonijek β; model 3D opisuje strukturę III-rzędową, czasem IV-rzędową
- s. 59–60 (ryc. 22A): SWISS-MODEL: 1) sekwencja aminokwasów lub ID białka → 2) wyszukanie wzorców (znane struktury) → 3) dopasowanie reszt celu do wzorca → 4) budowa modelu (rdzeń ze wzorca, pętle dobudowane) → 5) ocena jakości
- s. 60 (ryc. 22B): GMQE – cały model, 0–1 (bliżej 1 = dokładniej); QMEANDisCo – lokalnie, reszta po reszcie, 0–1; poniżej ok. 0,6 niska jakość
- s. 60: sprawdza się: pokrycie sekwencji wzorcem, jakość dopasowania, stan biologicznego kompleksu, oceny; mostek solny: Arg/Lys (+) z Asp/Glu (−)
- s. 61: wariant w pętli bez wzorca: różnica między modelami może być niepewnością obliczeń
- s. 61: DALI korzysta z odległości między elementami struktur; wspólny fałd nie wyklucza różnych centrów aktywnych i partnerów; dopasowanie strukturalne nie klasyfikuje wariantu
- s. 61: Rosetta = pakiet do modelowania, projektowania i analizy dużych cząsteczek; wynik zależy od modelu początkowego, próbkowania i funkcji oceny; w komórce białko otaczają woda, jony, partnerzy, błony, modyfikacje
- s. 61: porównanie referencja–wariant: ta sama izoforma, domena, stan kompleksu → jakość lokalna, kontakty, mechanizm; przy wiązaniu DNA liczy się powierzchnia kontaktu, nie ogólny kształt
- s. 62: pytania: SWISS-MODEL – jak zbudować model; DALI – jak podobne są struktury; Rosetta – konformacje, kompleksy, skutki energetyczne

### R7
- s. 63: miejsce wiązania ma kształt, rozkład ładunków, właściwości chemiczne; partner może się wiązać także dzięki zmienionej konformacji
- s. 63: PDBbind: do poznawania zależności budowa–siła wiązania oraz trenowania i sprawdzania modeli obliczeniowych; sprawdza się rodzaj pomiaru i warunki
- s. 63: Kd – stała dysocjacji; Ki – stała hamowania (inhibitor); IC50 – stężenie inhibitora zmniejszające aktywność o połowę w danym teście; nieporównywalne bez znajomości układu
- s. 64 (ryc. 23): θ = [L]/(Kd + [L]); przy [L] = 100 nM: referencja (Kd 10 nM) ≈ 91%, wariant (Kd 1 µM) ≈ 9%; krzywa wariantu przesunięta w prawo (100× wyższe stężenie do połowy wysycenia)
- s. 64 (ryc. 23): odczyt Kd: 50% na osi pionowej → do krzywej → stężenie na osi (skala logarytmiczna); tylko te same warunki pomiaru
- s. 64: skutek w komórce zależy jeszcze od rzeczywistych stężeń, funkcji białka, mechanizmu choroby
- s. 64, 76 (przykład 6): prawidłowa ilość białka (Western) przy spadku aktywności – wyniki zgodne: ilość i wielkość a funkcja; struktura pomaga wskazać mechanizm (np. centrum aktywne)

### R8
- s. 49: 1000 Genomes: faza 3 (2015) – 2504 osoby z 26 populacji (nazwa to zaokrąglenie); następca Human Genome Project
- s. 49: ExAC = Exome Aggregation Consortium; 2016 – 60 706 osób; agregacja i wspólna analiza istniejących danych
- s. 49: gnomAD = Genome Aggregation Database; v4.0 (2023) – 807 162 osoby
- s. 49: „niemal identyczne DNA” to przybliżenie: liczba różnic zależy od rodzaju wariantów i sposobu porównania; danych o bazie nie przenosi się na dwie osoby
- s. 50: AF z baz = częstości p i q z prawa Hardy’ego–Weinberga (p + q = 1), policzone na danych
- s. 66: OMIM = Online Mendelian Inheritance in Man; choroba monogenowa dziedziczy się mendlowsko (np. mukowiscydoza); HGMD = Human Gene Mutation Database, prowadzi do publikacji, dostęp zależy od wersji
- s. 67: ClinVar: różne oceny m.in. z innego zakresu danych albo aktualizacji
- s. 69: NCBI: Gene porządkuje geny, RefSeq – referencyjne sekwencje genomowe, transkryptów i białek; tok: gen i organizm → rekord → transkrypty → sekwencja; w Ensembl sprawdza się gatunek i wersję genomu
- s. 69: polimeraza RNA czyta matrycę 3′→5′, więc geny na różnych niciach biegną przeciwnie
- s. 70: przepływ: NCBI/Ensembl – ekson → UniProt – jaką część białka koduje → powrót do DNA i projekt amplifikacji
- s. 70: Human Protein Atlas: dane transkryptomiczne, obrazowanie z przeciwciałami, proteomika; także lokalizacja w komórce; część modułów obejmuje inne ssaki; barwienie ocenia się z metodą i jakością przeciwciała
- s. 70: GDC = NCI Genomic Data Commons: przeszukiwanie, analiza, zestawianie grup przypadków; dane molekularne, kliniczne, o materiale; zakres zależy od projektu i pliku; część danych otwarta, część z uprawnionym dostępem; porównania: typ materiału, sposób pomiaru, harmonizacja
- s. 70: zgodność DNA–RNA–białko zaburzają regulacja ekspresji, degradacja produktu, skład próbki
- s. 71: wariant w guzie w genie nieaktywnym w tej tkance: kontekst, ale nie powód do odrzucenia zmiany
- s. 73: test pewny dla SNV przy VAF 50% → dla VAF 2% i delecji eksonu skuteczność wykazuje się osobno

### R9
- s. 75 (przykład 1): znana zmiana rodzinna: referencja, wersja, zapis → region w NCBI/Ensembl → test celowany; startery obejmują miejsce i omijają pseudogen; po genotypie – aktualna klasyfikacja i dziedziczenie; wynik nieoczekiwany → jakość i allele dropout
- s. 75 (przykład 3): ekspansja HTT: oba allele, wiarygodność pomiaru, zakresy HTT
- s. 76 (przykład 4): podejrzenie utraty kopii eksonu → analiza liczby kopii + potwierdzenie (np. MLPA); brak wariantu punktowego nie wyklucza delecji; spadek pokrycia może wynikać z nieskutecznego wzbogacenia – sam nie rozpoznaje CNV
- s. 76: 6 pytań pełnej odpowiedzi: co zmierzono i jak; jakość i zakres; jaki wariant (referencja, zapis, skutek, zygotyczność/VAF); częstość, bazy, predykcje; funkcja i dziedziczenie; jaki wniosek naprawdę wynika
- s. 76: zdanie-wzorzec: „Oceniam najpierw wiarygodność wykrycia, następnie skutek biologiczny, a potem znaczenie kliniczne – w kontekście genu, dziedziczenia i fenotypu.”
- s. 78: pary nieobecne w „W 60 sekund”: ekson/CDS; genom/transkryptom; WES/WGS; ClinVar/gnomAD; OMIM/UniProt; PDBbind/predyktor; ilość/aktywność białka

## 3. Przesunąć z części 1 do części 2
- [c01-sanger · „Który fragment zbadać?”] reguła kodon n → c.(3n−2)–c.3n z aa 120; identyfikatory NM_ z wersją → R2
- [c01-sanger · „PCR…”] zakres 500–900 zasad i startery sekwencyjne dla fragmentów kilku tys. pz → R2
- [c01-ngs · „Sekwencjonowanie przez syntezę”] Ion Torrent (pH, jon wodorowy) → R3
- [c01-ngs · „Krótkie czy długie odczyty?”] mechanizm PacBio HiFi i nanoporów → R3
- [c01-bioinf · „Co robi komputer…”] akapit o doborze programów i IGV → R5
- [c01-skutek · „Jak zapisać wariant…”] r., p.(=), Ter, c.76+1G>A, uwaga GRCh37/GRCh38 → R6
- [c01-skutek · „Predyktory missense”] progi SIFT (0,05; ≤ 0,05), HumDiv/HumVar, progi Ensembl 0,446/0,908, kalibracja ClinGen → R6
- [c01-skutek · „Model struktury”] DALI i Rosetta → R6
- [c01-skutek · „Doświadczenie”] liczby Kd (10 i 1000 nM), PDBbind → R7
- [c01-skutek · „Doświadczenie”] nadekspresja, typ komórek, tabela „obserwacja → co wyjaśnić” → R7
- [c01-znaczenie · „Która baza…”] opisy HGMD i DISGENET; postaci sekwencji genomowa/cDNA/CDS; gen na nici odwrotnej → R8
- [c01-znaczenie · „Która baza…”] Swiss-Prot/TrEMBL; GDC; łączenie poziomów (amplifikacja–RNA–białko, korelacja z przeżyciem) → R8
- [c01-znaczenie · „Jak czytać ClinVar?”] tabela gwiazdek 0–4 → R8

## 4. Uprościć w części 1
- [c01-sanger · „Który fragment…”] zostaje: cel → gen, gatunek, wersja genomu, transkrypt (numer eksonu zależy od transkryptu); granice ekson–intron; hotspot
- [c01-ngs · długie odczyty] jedno zdanie: dają je m.in. PacBio HiFi i nanopory
- [c01-skutek · HGVS] zostaje: g./c./p., c.76A>T, p.(Gly12Asp) z sensem nawiasu, zależność od transkryptu
- [c01-skutek · predyktory] zostaje: idea SIFT i PolyPhen-2, odwrotne skale, brak wyniku = „nie wiadomo”, zgodność = jeden dowód
- [c01-skutek · model, doświadczenie] SWISS-MODEL i Kd po 1 zdaniu; co widać na modelu, jakość lokalna; test dobrany do mechanizmu; Western a ELISA z ramką „uwaga”
- [c01-znaczenie · bazy, ClinVar] tabela 7 baz, OMIM (gen ≠ wariant), UniProt i HPA po 1–2 zdania (RNA ≠ białko); gwiazdki = sposób przeglądu, nie kierunek
- [c01-klasy · przykład cz. 2] progi w nawiasach → „niski/wysoki – alarm” + odsyłacz do R6 (decyzja 4)

## 5. Sekcje części 2
- R1. Od DNA do działającej komórki · [c01-warianty] · dlaczego sama sekwencja nie wystarcza: gen → pre-mRNA → mRNA → białko; dziedziny jako tabela; RP-PCR jako dopowiedzenie do ekspansji
- R2. Od pytania do amplikonu: numeracja i cykl PCR · [c01-sanger] · jeden przykład do końca (domena 120–210 → eksony 3–4 → 2 amplikony); cykl PCR w tabeli 3 etapów
- R3. Technologie odczytu z bliska · [c01-ngs] · tabela „metoda → co jest sygnałem” (Maxam–Gilbert, pirosekwencjonowanie, SOLiD, Ion Torrent, HiFi, nanopory); złącza RNA-seq na liczbach 48/45/6
- R4. Mikromacierz krok po kroku i testy z prezentacji · [c01-macierze], [c01-strategia] · tabela 6 testów z kolumną „co mierzy”; obie uwagi do slajdów w jednej ramce
- R5. Pliki i programy · [c01-bioinf] · FASTQ i VCF pole po polu (tabele), z linii VCF wyprowadzić VAF 48%; tabela narzędzi z etapem drogi danych
- R6. Zapis, predykcja i model: szczegóły · [c01-skutek] · tabele: elementy opisu; SIFT/PolyPhen-2 z progami; SWISS-MODEL/DALI/Rosetta; kroki SWISS-MODEL z uzasadnieniem każdego
- R7. Siła wiązania i dobór doświadczenia · [c01-skutek] · przeliczyć θ dla 100 nM; pokazać, że prawidłowa ilość ≠ prawidłowa funkcja
- R8. Bazy i katalogi populacyjne z bliska · [c01-znaczenie] · tabela katalogów (rok/wydanie, liczba osób) z zastrzeżeniem o wersji; gwiazdki ClinVar; tok NCBI → Ensembl → UniProt; HPA i GDC – co naprawdę zmierzono
- R9. Od podejrzenia do wniosku · [c01-klasy] · przykłady 1, 3, 4 przeprowadzone przez 6 pytań (2 i 5 są w części 1, 6 – w R7); na końcu 7 par pojęć

## 6. Przejście
Część 1 wystarcza, żeby rozumieć całą drogę od wyboru badania do klasy wariantu i odpowiedzieć na trzy pytania. Część 2 jest dla osób, które chcą znać szczegóły z prezentacji: cykl PCR i budowę plików, pozostałe chemie sekwencjonowania, nazwy testów i programów, progi predyktorów, kroki modelowania struktury, liczby opisujące bazy. Każda sekcja rozszerza jeden podrozdział części 1.

## 7. Błędy i decyzje
**Błędy A (wzmocnione twierdzenia):**
- [c01-bioinf · Phred] „skala 0–1 opisuje prawdopodobieństwo” – źródło: „może opisywać” (s. 46) → złagodzić
- [c01-znaczenie · walidacja] „wariant potwierdza się metodą opartą na innej zasadzie” – źródło: „w wybranych sytuacjach” (s. 72) → dodać
- [c01-znaczenie · ClinVar] gwiazdki bez zastrzeżenia „w uproszczeniu, dla zbiorczych klasyfikacji wariantów germinalnych” (s. 67) → dopisać
- Dopowiedzenia bez pokrycia w źródle (niesprzeczne; zostawić jako rozumowanie albo złagodzić): [c01-sanger] „drugi pik niski, łatwo go przeoczyć”; [c01-sanger] uzasadnienie małej ilości ddNTP; [c01-strategia] „wariant obecny także we krwi przemawia za konstytucyjnym” (s. 36: „pomaga odróżnić”)
- Sprzeczności ze źródłem i faktów spoza opracowania nie znaleziono.

**Linie „Źródło”:** [c01-strategia] „slajdy 8–31” → 8–25 (rozdz. 06 opracowania); reszta zgodna. Część 2: R1 2–25 · R2 8–25, 80–89 · R3 8–25 · R4 23–31 · R5 64–67, 80–89 · R6 48–63, 80–89 · R7 48–63 · R8 32–63, 69–79 · R9 jak [c01-znaczenie] (rozdz. 18 to podsumowanie bez własnych slajdów).

**Ramka „stare źródło”:** nie. **Kotwica ryciny z ChatGPT:** nie dotyczy (8 rycin z banku `g`; w tekście ryc. 20 „NMD” zamiast ryc. 7 z listy mapy – bez wpływu na plan).

**Decyzje do zatwierdzenia:**
1. „Warto wiedzieć” (RP-PCR, Ki/IC50) i liczebności baz to uzupełnienia opracowania ze źródeł [n], nie ze slajdów – wracają do części 2 zgodnie ze zleceniem; liczebności z rokiem i wersją.
2. Z ramek „Z liceum” tylko fakty: leucyna – 6 kodonów, odwrotna transkryptaza, poziomy struktury białka, kierunek polimerazy RNA, p + q = 1.
3. Uwagi do slajdów w części 2 (Oncomine, Myriad, grupy programów) przekraczają limit mapy „maks. 2” – proponuję liczyć limit tylko dla części 1.
4. Progi SIFT/PolyPhen-2 schodzą do R6, a przykład końcowy części 1 ich używa – przykład bez progów (propozycja) albo progi zostają w części 1.
5. Z 18 par „Najważniejsze rozróżnienia” do R9 trafia 7 nieobecnych w „W 60 sekund”; słownik skrótów i mapa slajdów pominięte.

## Decyzje szefa (19.11) – obowiązują wykonawcę
- Decyzje 1, 2, 3, 5 – **TAK** (uzupełnienia opracowania wracają; z ramek „Z liceum” tylko 5 faktów; limit „maks. 2 uwagi do slajdów” dotyczy tylko części 1; z „Najważniejszych rozróżnień” 7 brakujących par do R9; mapa slajdów – pominąć; słownik skrótów – krótka tabela na końcu R9, jeśli nie dubluje części 1).
- **Decyzja 4 – progi SIFT/PolyPhen-2 zostają w części 1** (przykład końcowy z nich korzysta); do R6 tylko szczegóły ponad progi.
- Błędy A (3 wzmocnienia) – poprawić; linia źródła [c01-strategia] → slajdy 8–25.
