# Handoff G – Genomika: analiza genomu i genotypowanie (Opus xhigh, 1 agent)
Plan szczegółowy przygotował szef (Fable): **zakres, źródła, cięcia i lista rycin są ustalone poniżej – nie zmieniasz ich**. Twoja praca to dobry tekst i ryciny. Jeśli coś w planie nie zgadza się ze źródłem, zapisz to w `stan/g.md` i idź dalej według źródła.
Przeczytaj: `/home/user/first-thing/podrecznik/ZASADY.md`, `KOMPONENTY.md`, potem tylko wskazane fragmenty paczki.

- **Plik wynikowy:** `/home/user/first-thing/podrecznik/rozdzialy/z01-genomika.html` · **limit: 14 stron** (A4, dwie kolumny)
- **Paczka źródeł:** `/tmp/claude-0/-home-user-first-thing/600b873f-e07d-5766-b2f4-6a90b68ae091/scratchpad/zrodla/g/ (brak – źródłem jest samo opracowanie)` · **wyciąg:** `wyciagi/g.md` · **stan:** `stan/g.md` (jeśli istnieje – kontynuuj, nie czytaj źródeł od nowa)
- **Bank rycin:** `bank-rycin/INDEX.md`

**Ten rozdział powstaje przez skrócenie gotowego opracowania „Genomika” (84 s.) do 14 stron – nie piszesz od zera i nie rysujesz rycin.** Materiał: `material/genomika.txt` (s. 4–77). Źródłem opracowania była prezentacja LMZ 3; linie źródła podawaj jako „Źródło: prezentacja LMZ 3, slajdy X–Y” (zakres slajdów jest w nagłówku każdego rozdziału opracowania). Numer rozdziału w tomie jest roboczy (01) – nie wpisuj go na sztywno w tekście.

## Mapa: 18 rozdziałów opracowania → 7 podrozdziałów
| Podrozdział | Z rozdz. opracowania | Zostaje | Tniemy |
|---|---|---|---|
| 1. Co badamy i jakie są warianty | 01–02 | genom, gen, genotyp, allel/locus; rodzaje wariantów z definicjami i skutkiem (tabela) | droga od informacji do komórki – 2 zdania |
| 2. Od regionu do odczytu sekwencji | 03–04 | wybór regionu, amplifikacja w 3 zdaniach (odsyłacz do rozdz. o PCR), allele dropout, dNTP/ddNTP i odczyt metodą Sangera | szczegóły PCR |
| 3. Technologie sekwencjonowania i strategia badania | 05–06 | biblioteka NGS, sekwencjonowanie przez syntezę, odczyty sparowane, krótkie a długie odczyty, RNA-seq (co mówi), panel / eksom / genom, analiza trio | parametry aparatów, drugie technologie długich odczytów – 1 zdanie każda |
| 4. Mikromacierze | 07 | zasada, macierz SNP – co pokazują dwa wykresy | przykłady testów |
| 5. Od danych do wariantu: bioinformatyka i kontrola jakości | 08–09 | etapy drogi danych (lista), co to FASTQ i VCF w 1 zdaniu, miary jakości (pokrycie, jakość odczytu) i co robić przy słabej jakości | budowa plików |
| 6. Co wariant robi: populacja, położenie, predykcja, struktura, doświadczenie | 10–14 | częstość w populacji jako argument, położenie wariantu a skutek, przedwczesny STOP i NMD, cztery mechanizmy działania wariantu, do czego służą predyktory missense i ich ograniczenia, po co badania funkcjonalne | SWISS-MODEL krok po kroku, Kd i wykres – po 1 zdaniu |
| 7. Co wariant znaczy: geny, choroby, klasyfikacja | 15–18 | związek gen–choroba, sekwencja a ekspresja, trzy pytania (czy to prawdziwe / co robi / co znaczy), klasy wariantów i jakie dowody na nie się składają | rozdz. 18 „Łączenie materiału” i „Najważniejsze rozróżnienia” – wykorzystaj jako „W 60 sekund” |

**Usuń:** ramki „Z liceum”, „Przykład”, „Obraz w głowie”, „Uwaga do slajdu” (zostaw maks. 2 naprawdę potrzebne), słownik, mapę slajdów, źródła zewnętrzne [n] i odsyłacze do nich – w tekście nie może zostać nic, czego nie ma w prezentacji (jeśli opracowanie oznacza coś jako dopowiedzenie spoza slajdów – usuń).

## Ryciny – tylko z banku, 8 sztuk (nic nie rysujesz)
`g` ryc. 2 „Zmiany DNA i ich skutki” · ryc. 6 „dNTP i ddNTP” · ryc. 7 „Jak odczytuje się sekwencję?” · ryc. 9 „Sekwencjonowanie przez syntezę” · ryc. 11 „Krótkie i długie odczyty w trudnym regionie” · ryc. 16 „Macierz SNP” · ryc. 17 „Droga danych: od aparatu do raportu” · ryc. 21 „Cztery mechanizmy działania wariantu”.
