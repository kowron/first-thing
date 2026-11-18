# Stan G v2 – przepisanie wg handoff/P-przepisanie.md (18.11.2026)

Przeczytano: P-przepisanie, STYL, PORADNIK s. 5–11, z06 (hybrydyzacja, Southern, STR, sekwencjonowanie, mikromacierze), ZASADY, KOMPONENTY, handoff G, wyciąg g, stan g, obecny z01, CAŁE material/genomika.txt (rozdz. 1–18 + rozróżnienia). Rewizji dla G brak.
Przed: 14 stron (build 4 z 16.11). Cel: 20–26 s. (maks. 28). Plik roboczy: `robocze/z01-genomika.html`.
Odsyłacze z innych rozdz. do #c01: z06 (ddNTP – „szerzej w rozdz. o genomice”), z10 (pseudogen, haploinsuficjencja) → te pojęcia muszą być zdefiniowane w G.

## Decyzje ogólne
- Kolejność h2 zmieniona wg zależności pojęciowych (zakres bez zmian): stary h2 3 rozdzielony na NGS (3) i Strategię (5), a Strategia stoi PO Mikromacierzach (4), bo wybór metody obejmuje macierz; częstość w populacji przeniesiona z „Co wariant robi” do „Co wariant znaczy” (źródło: rozdz. 10 należy do pytania 3 „Co to znaczy?”); rozróżnienie VAF/AF – w miejscu definicji AF (VAF jest już znany). Wynik: 8 h2.
- Ryciny: 7 z obecnej wersji (g-02, 06, 09, 11, 16, 17, 21) + powrót g-07 (jedyny obraz drabiny fragmentów → chromatogramu; z06 nie ma ryciny Sangera, a odsyła do #c01; panel D – dwa piki heterozygoty, potrzebny w przykładzie potwierdzenia) + 1 nowa z banku zamiast rysowania: g-20 (NMD – kluczowy mechanizm bez ryciny). Nic nie rysuję.
- Przykłady ze źródła (rozdz. 18 – w wyciągu T jako „przykłady”) używam jako ramki „Przykład” (rozumowanie, liczby oznaczone jako przykładowe); nie dodaję z nich nowych faktów – reguły są w wyciągu jako Z. Nazwy choroby Huntingtona nie używam (tylko w T-przykładach).
- T zostaje T: daty i liczebności baz, tabela 5 dziedzin genomiki, testy komercyjne, tabela 10 narzędzi, budowa FASTQ/VCF, kroki SWISS-MODEL (GMQE/QMEAN), Kd/Ki/IC50, ramki Z liceum, Primer-BLAST, RP-PCR „drabinka”.

## Plan h2
### 1. c01-warianty – Co badamy i jakie są warianty (sl. 2–25) – cel: ROZPOZNAĆ rodzaj wariantu (jedna cecha → nazwa → skutek)
- (b) problem: pacjent z podejrzeniem choroby genetycznej, 3 pytania (czy naprawdę / co robi / co znaczy) → genom (jądro + mtDNA, 3 mld pz, 2 zestawy, odcinki niekodujące) → gen (funkcjonalne RNA) → locus, allel, genotyp (A/G), homo/heterozygota → ile kopii (autosomy, mtDNA, X/Y u mężczyzny) → genetyka/genomika, mapowanie, genotypowanie, bioinformatyka → DNA to punkt wyjścia (neuron/miocyt; transkryptom/proteom – 2 zdania) → sekwencja referencyjna, wariant (2 kroki) → ramka odczytu → SNV (syn./missense/nonsense; syn. a splicing) → indel (÷3 / frameshift) → CNV, zmiany zrównoważone → ekspansja (HTT, progi, penetracja, przerwania, antycypacja) → konstytucyjny / de novo / somatyczny / mozaikowość → dlaczego jedna metoda nie wystarcza (krótkie odczyty, pseudogen, MLPA) → wynik ujemny.
- (c) –; (d) Przykład: rozpoznawanie wariantów na sekwencji z ryc. g-02 (pytania: ile nt? zmienia aminokwas? podzielne przez 3?).
### 2. c01-sanger – Od regionu do odczytu: PCR i metoda Sangera (sl. 8–25, 80–89) – cel: wyjaśnić mechanizm + odczytać chromatogram
- (b) region z pytania (gen, gatunek, wersja genomu, transkrypt; izoformy; NM_.wersja) → CDS/UTR → kodon n = c.(3n−2)…c.3n → splicing, mRNA/cDNA → hotspot, szerokość → PCR (przypomnienie + #c05), amplikon, PCR nie czyta → dobry starter, podobne sekwencje → allele dropout → amplikon vs odczyt (500–900), kontrole → Sanger: problem → ddNTP (ryc. g-06) → drabina → kapilara (#c06) (ryc. g-07) → PCR vs Sanger, orientacja forward/reverse → chromatogram, basecalling, dwa piki, IUPAC, SNV vs indel, tabela → przygotowanie odczytu, numeracja → kiedy Sanger, czułość.
- (d) Przykład: allele dropout w rodzinie (matka A/A, dziecko „G/G”) – liczby/litery przykładowe.
### 3. c01-ngs – Sekwencjonowanie następnej generacji (sl. 8–25) – cel: wyjaśnić mechanizm SBS i dobór długości odczytu
- (b) problem skali → NGS, odczyt, dopasowanie → biblioteka, adaptery, indeks, UMI → klastry, cykl z odwracalną blokadą (ryc. g-09) → porównanie z Sangerem, inne chemie (1 zdanie) → paired-end → krótkie vs długie, fazowanie (ryc. g-11), HiFi i nanopory po 1 zdaniu → RNA-seq → tabela pytanie→informacja.
- (d) Przykład: para odczytów 350 pz vs 460 pz → delecja (liczby z ryc. 10 źródła, przykładowe).
### 4. c01-macierze – Mikromacierze (sl. 23–31) – cel: zrozumieć model LRR/BAF i rozpoznać cztery sytuacje
- (b) hybrydyzacja (przypomnienie + #c06), sonda → macierz SNP, SNP, LRR, BAF (skąd 0,5 i 0,33/0,67) (ryc. g-16) → array-CGH, zrównoważona translokacja → macierz SNP+CN, ekspresyjna → tabela.
- (d) Przykład: wyprowadzenie BAF przy 1, 2, 3 kopiach + odczyt „LRR niżej, brak pasma 0,5”.
### 5. c01-strategia – Strategia badania (sl. 8–31) – cel: WYBÓR METODY (kryterium: oczekiwana klasa zmiany + liczba możliwych genów)
- (b) zakres ≠ technologia → panel / WES (eksom) / WGS, tabela → panel fizyczny/wirtualny → kryterium + dwa zestawione przypadki (ramka) → szerokość ≠ dokładność → trio → nowotwór (krew) → wynik ujemny, reinterpretacja.
- (d) Przykład: dwóch pacjentów – objawy pasujące do wielu genów (panel/WES) vs podejrzenie ekspansji CAG w HTT (test dla ekspansji; ujemne WES nic nie rozstrzyga); trio 0/0 + 0/0 → 0/1.
### 6. c01-bioinf – Od danych do wariantu (sl. 64–67, 80–89) – cel: wyjaśnić drogę danych + ocenić wiarygodność
- (b) lista etapów z „po co” (ryc. g-17) → FASTQ/BAM/VCF po 1 zdaniu → alignment, pseudogen → variant calling 0/0, 0/1, 1/1 → anotacja, filtrowanie → programy, IGV → Q (Phred, tabela, skala 0–1) → trzy niepewności → głębokość, pokrycie → VAF i przesunięcia → podejrzany wariant, UMI, błąd systematyczny.
- (d) Przykład: VAF 29/60 vs 80/1000 (liczby ze źródła, przykładowe) – co z nich wynika.
### 7. c01-skutek – Co wariant robi (sl. 48–63, 80–89) – cel: wyjaśnić mechanizm (położenie → RNA/białko → funkcja)
- (b) HGVS (c./p., nawias) → położenie (tabela) → missense → LoF → NMD (ryc. g-20) → GoF, DN, haploinsuficjencja (ryc. g-21) → mechanizm a choroba → SIFT, PolyPhen-2 (tabela) → zgodność = 1 dowód → model struktury, SWISS-MODEL, DALI, Rosetta po 1 zdaniu → ligand, PDBbind, Kd po 1 zdaniu → doświadczenie wg pytania, Western/ELISA (+ Uwaga do źródła), kontrole, tabela obserwacja→pytanie.
- (d) Przykład: dwa warianty nonsense w tym samym genie (ekson 2 vs ostatni ekson).
### 8. c01-znaczenie – Co wariant znaczy (sl. 32–63, 69–79) – cel: zrozumieć model AF + zastosować klasyfikację do nowego wariantu
- (b) katalogi populacyjne → AC, AN, AF, liczenie → częstość jako argument (dominująca / recesywna) → rzadkość ≠ dowód, efekt założyciela → VAF vs AF → bazy (tabela) OMIM, HGMD, DISGENET, NCBI, Ensembl (kierunek genu), UniProt, HPA, GDC, łączenie poziomów → ClinVar, gwiazdki, konflikt → 3 pytania, walidacja vs potwierdzenie, czułość/swoistość/granica → ACMG/AMP, 5 klas, VUS, cis/trans, segregacja.
- (d) Przykład (3 ramki): jeden wariant missense z panelu od odczytu do klasy (29/60, kontrola techniczna, potwierdzenie, HGVS, gnomAD, SIFT 0,01, PolyPhen-2 0,98, ClinVar, mechanizm, rodzina → VUS) + zmiana warunku (wariant częsty w populacji / nowe dowody).
- W 60 sekund: z rozdz. 18 i rozróżnień.

## Postęp
- h2 1 (warianty) – GOTOWE w robocze/ (3 pytania na wejściu; rozpoznawanie: tabela cecha→rodzaj→skutek; Przykład na sekwencji z ryc. g-02; Pojęcia: locus, sekwencja ref., ramka, penetracja, pseudogen). Dalej: marker <!-- @@DALEJ@@ --> w pliku.
- h2 2 (region, PCR, Sanger, chromatogram) – GOTOWE (Przykład: allele dropout w rodzinie; ryc. g-06 + powrót g-07 z nowymi podpisami; Pojęcia: CDS i UTR, hotspot, basecalling; chapref #c05, #c06).
- h2 3 (NGS) – GOTOWE (Przykład: para 350 vs 460 pz → delecja; ryc. g-09, g-11; Pojęcia: odczyt, fazowanie; pageref do h3 id c01-artefakty i c01-klasy – nadać te id w h2 6 i 8!).
- h2 4 (mikromacierze) – GOTOWE (Przykład: przewidywanie BAF/LRR dla 3 sytuacji; ryc. g-16; Pojęcie SNP; chapref #c06 x2).
- h2 5 (strategia) – GOTOWE (kryterium + Przykład: 2 pacjentów – wiele genów vs ekspansja HTT; trio; nowotwór; wynik ujemny; Pojęcie eksom; pageref c01-glebokosc – nadać id w h2 6).
- Kalibracja (build lustrzany w scratchpad/g2/mirror, nie liczę do 5): po h2 1–5 = 19 s., luki przed dużymi rycinami → g-07 USUNIĘTA ponownie (decyzja: miejsce; drabina opisana w tekście z przykładem 3′-TACGAT-5′). Reszta pisana oszczędniej.
- h2 6 (bioinf, QC) – GOTOWE (lista etapów z „po co”; Przykład VAF 29/60 vs 80/1000; h3 id c01-glebokosc, c01-artefakty; ryc. g-17).
- h2 7 (skutek) – GOTOWE (HGVS; tabela położenie; NMD + nowa z banku g-20; Przykład: 2 warianty nonsense; 4 mechanizmy + rachunek 1/16; SIFT/PolyPhen + tabela przywrócona; struktura; doświadczenie + Uwaga do źródła Western/ELISA).
