# Plan Z03 – Apoptoza i starzenie komórek: część 1 / część 2 (rozdział pilotażowy)

Plik rozdziału: `rozdzialy/z03-apoptoza.html` (stan z 18.11, 19 s., 58,9 tys. znaków tekstu). Handoff: `handoff/C1-plan-czesci.md`. Wykonawca: `handoff/C2-wykonanie-czesci.md`.
Przeczytane w całości: Drewa s. 165–174 (tekst + skan s. 165–173: tab. 8.1, 8.2, ryc. 8.2–8.6), Jóźwiak s. 126–127 (tekst + skan obu stron, w tym ryc. 11.8), Alster–Korwek s. 138–144 (tekst + skan ryc. 1–3), reszta r. 8 Drewy i r. 11 Jóźwiaka – tylko po to, żeby potwierdzić „Poza zakresem”.

**Oznaczenia.** Sekcje części 1: `apo` = `c03-apoptoza`, `kas` = `c03-kaspazy`, `bcl` = `c03-bcl2`, `szl` = `c03-szlaki`, `dod` = `c03-dodatkowe`, `fiz` = `c03-fizjologia`, `zab` = `c03-zaburzenia`, `sta` = `c03-starzenie`. Akapit wskazuję pierwszymi słowami w „…”. **O1–O36** = operacje na części 1 (pkt 3). **R1–R10** = sekcje części 2 (pkt 4). Kolumna **n** = liczba jednostek informacji w wierszu (do bilansu i kontroli). „(ryc.)” = informacja odczytana ze skanu ryciny lub tabeli, nie z tekstu biegłego.
Decyzje: **P1** – w części 1 w pełni · **P1u** – w części 1 w uproszczeniu, szczegół do części 2 · **P2** – tylko w części 2.

---

## 1. Bilans

- **Źródło w zakresie:** Drewa s. 165–174 (wstęp r. 8, 8.1–8.2.5; ok. 19 tys. znaków + 2 tabele + 4 schematy), Jóźwiak s. 126–127 (ok. 6,5 tys. znaków + tab. 11.4 + ryc. 11.8), Alster–Korwek s. 138–144 (ok. 33 tys. znaków + 3 ryciny). Razem ok. 59 tys. znaków; w inwentarzu **299 jednostek informacji** (Drewa 124, Jóźwiak 34, Alster 141).
- **W obecnym rozdziale** jest ok. 80% jednostek (ok. 86% objętości źródła): Drewa ok. 88%, Jóźwiak ok. 95%, Alster ok. 80%. Brakuje prawie wyłącznie tego, co mapa kazała ciąć: tab. 8.2 (nazwy, masy, chromosomy), szczegóły budowy kaspaz, reszta tab. 8.1 i układ domen z ryc. 8.3, historia i nazwiska, rozwinięcia skrótów, schemat ryc. 11.8, linie komórkowe i pojedyncze doświadczenia z artykułu o starzeniu.
- **Dochodzi: ok. 70 jednostek – wszystkie do części 2.** Do części 1 nie trzeba dopisać żadnego faktu (wszystkie jednostki P1 już są w tekście).
- **Przechodzi z części 1 do części 2: ok. 55 jednostek** (37 operacji: O1–O36 i O20a; pięć z nich to zarazem drobne poprawki wierności): metody oznaczania znaczników starzenia, liczby z pojedynczych doświadczeń, pośrednicy szlaku ceramidowego, droga DAXX, pełny skład megakanału, rzadziej wymieniane białka Bcl-2 i receptory, pięć leków, 5 wierszy tab. 11.4, wątek *C. elegans*.
- **Docelowo:** P1 = 186 jednostek (62%), P1u = 26 (9%), P2 = 87 (29%) → **część 1 ≈ 70%, część 2 ≈ 30% informacji** (objętościowo wg źródła ok. 72/28).
- **Objętość tekstu:** część 1 ok. 52 tys. znaków (z 58,9 tys.; ok. 16–17 s.), część 2 ok. 20–24 tys. znaków z tabelami (ok. 6–8 s.; 40–45% objętości części 1).
- Ryciny bez zmian (6 SVG) + zaślepka ryciny z ChatGPT w części 1 (pkt 8). Czerwona ramka „stare źródło”: **nie dotyczy** (pkt 6). Błędów klasy A w obecnym tekście: **brak** (pkt 7).

---

## 2. Inwentarz źródła
(POMINIĘTY w skrócie – inwentarz jest w pełnym pliku `plany/z03-czesci.md`; wszystkie fakty do napisania są w pkt 3 i 4, sprawdzaj kompletność względem pkt 4.)

## 3. Zmiany w części 1

Zasady dla wykonawcy:
1. **Nic nie dopisujemy do części 1** poza zdaniami łączącymi i krótkimi odsyłaczami do części 2. Wyjaśnienia, „Przykłady”, „Pojęcia”, „Zapamiętaj”, „W 60 sekund” – bez zmian (żaden nie zawiera szczegółu przenoszonego do części 2).
2. **Odsyłacz do części 2** tylko tam, gdzie lista lub tabela została skrócona – w nawiasie, z `pageref` do sekcji `c03-r-…` (np. „pełna lista – część 2, s. X”). Nie więcej niż jeden na akapit.
3. **Napis na rycinie = słowo w tekście części 1.** Każdy termin widoczny na rycinach części 1 musi zostać w części 1 przynajmniej nazwany (dlatego w O10, O11, O16, O27, O34 nazwy zostają, a przechodzi tylko rozwinięcie).
4. Po każdej operacji przeczytaj akapit w całości: czy nie został skok między zdaniami.

| Nr | Miejsce (id · pierwsze słowa) | Operacja |
|---|---|---|
| O1 | `apo` · „„Kontrolowana” znaczy tu, że komórka nie ginie biernie…” | **Przenieś do R1** ostatnie zdanie: „Genetyczne podstawy apoptozy poznano najpierw u nicienia *Caenorhabditis elegans* (Nagroda Nobla 2002).” |
| O2 | `apo` · „Apoptozę nazywa się też programowaną…” | **Przenieś do R1** zdanie „Pierwotnie „programowana śmierć” oznaczała tylko śmierć w procesach fizjologicznych – w okresie zarodkowym i później.” Następne zdanie **upraszczaj do:** „Słowem „apoptoza” opisuje się zmiany w umierającej komórce niezależnie od tego, czy zachodzą w trakcie rozwoju organizmu, czy wywołał je czynnik zewnętrzny.” |
| O3 | `apo` · „Równolegle zmienia się błona komórkowa.” | **Poprawka wierności (pkt 7, B1):** „Zmienia się też błona komórkowa. […] W apoptozie przemieszcza się do warstwy zewnętrznej i asymetria błony zostaje zaburzona.” |
| O4 | `kas` · „Zidentyfikowano 14 kaspaz. Pierwszą poznaną był…” | **Upraszczaj:** zostaje tylko liczba – dołącz do akapitu „Kaspazy to rodzina wysoko konserwatywnych proteaz cysteinowych…” jako zdanie „Zidentyfikowano 14 kaspaz.”; zdanie o ICE i *ced-3* **przenieś do R1**. |
| O5 | `kas` · lista trzech części prokaspazy („prodomena… p20… p10”) | Bez zmian treści. Po liście dopisz odsyłacz: „(masy części i dalsze szczegóły budowy – część 2, `pageref c03-r-kaspazy`)”. Rycina `c03-fig-kaspaza` pokazuje masy (3–24, 17–21, 10–13, 32–55 kDa), których tekst części 1 nie omawia – podpis się do nich nie odwołuje, **podpisu nie zmieniamy**. |
| O6 | `bcl` · „Antyapoptotyczne działanie Bcl-2 poznano dzięki podobieństwu…” | **Przenieś do R1** pierwsze zdanie (Ced-9). Akapit zaczyna się od „U człowieka zidentyfikowano 26 genów rodziny Bcl-2.” |
| O7 | `bcl` · tabela „Proapoptotyczne / Antyapoptotyczne”, wiersz 1 | **Upraszczaj do:** „Bax, Bak, Bad, Bid, Bim, Bcl-X<sub>S</sub> i inne” / „Bcl-2, Bcl-X<sub>L</sub>, Mcl-1, Bcl-W i inne”. Pod tabelą odsyłacz: „(wszystkie białka z tabeli źródła i układ domen każdego z nich – część 2, `pageref c03-r-bcl2`)”. Usunięte nazwy (Bok/Mtd, Bik, Hrk, PUMA, Noxa; Bfl-1/A1, Bcl-B/Boo/Diva) → R3. |
| O8 | `szl` · tabela „Receptor śmierci / Ligand” | **Upraszczaj do trzech wierszy:** „Fas / FasL”, „TNFR1 / TNFα”, „TRAIL-R1, TRAIL-R2 / TRAIL”. W zdaniu przed tabelą („Każdy receptor ma swój ligand:”) dopisz „(pozostałe nazwy i receptory – część 2)”. TNFR2 oraz nazwy CD95 i Apo1 → R4. |
| O9 | `szl` · „W niektórych typach komórek receptor Fas przekazuje sygnał przez inne białko adaptorowe – DAXX.” | **Upraszczaj do:** „W niektórych typach komórek receptor Fas przekazuje sygnał inną drogą – przez białko adaptorowe <b>DAXX</b> i <b>kinazę</b> JNK. Kinaza to enzym, który przyłącza do innych białek reszty fosforanowe (fosforyluje je) i w ten sposób zmienia ich działanie. Także ta droga kończy się uruchomieniem kaskady kaspaz (jej kolejne ogniwa – część 2).” Definicja kinazy **musi zostać** (korzysta z niej szlak ceramidowy). c-Jun, ERK, Rac-1 → R4. |
| O10 | `szl` · lista szlaku wewnętrznego, pkt 1 „Otwarcie megakanałów.” | **Upraszczaj do:** „<b>Otwarcie megakanałów.</b> Na styku obu błon mitochondrium otwierają się megakanały, czyli pory przepuszczalności <b>PTP</b> (ang. <i>permeability transition pore</i>). Ich budowę opisuje kilka hipotetycznych modeli. Za zasadniczy element najczęściej uznaje się translokator nukleotydów adeninowych <b>ANT</b> w błonie wewnętrznej, połączony z poryną <b>VDAC</b> w błonie zewnętrznej. Od strony cytoplazmy z kanałem łączą się białka Bcl-2 i Bax – to tu białka Bcl-2 pilnują bramy. (Pozostałe składniki kompleksu – część 2.)” BPR, kinaza kreatynowa, peroksydaza glutationowa → R4. |
| O11 | `szl` · tamże, pkt 3 „Uwolnienie białek.” | **Upraszczaj do:** „<b>Uwolnienie białek.</b> Z przestrzeni międzybłonowej do cytoplazmy wychodzi cytochrom c, a z nim m.in. czynnik indukcji apoptozy <b>AIF</b> (ang. <i>apoptosis-inducing factor</i>) i białko <b>Smac/DIABLO</b> (pełna lista – część 2).” Nazwa Apaf-2 i prokaspazy 2, 3, 9 → R4. |
| – | `szl` · „Porównaj oba szlaki. W każdym białko adaptorowe…” | **Bez zmian – akapit-kotwica ryciny z ChatGPT** (pkt 8). Bez zmian także: lista trzech domen receptora, kroki 1–6 szlaku Fas, akapit „Zauważ zasadę…”, pkt 4 „Apoptosom.”, cały h3 o Bid, Przykład. |
| O12 | `dod` · „Działa tu układ perforyna–granzym B (GrB, fragmentyna-2).” | Usuń „, fragmentyna-2” (→ R5). |
| O13 | `dod` · lista, pkt 1 „Wniknięcie granzymu B.” | **Upraszczaj do:** „<b>Wniknięcie granzymu B.</b> Początkowo uważano, że perforyna wbudowuje się w błonę komórki, która ma zginąć, i tworzy kanał dla granzymu B. Granzym B może jednak wnikać także bez udziału perforyny (dwie takie drogi – część 2).” Endocytoza i receptor mannozo-6-fosforanu → R5. |
| O14 | `dod` · „Szlak pseudoreceptorowy może przebiegać także z udziałem granzymu A (GrA, fragmentyna-1)…” | Usuń „, fragmentyna-1”; **przenieś do R5** ostatnie zdanie („Ścieżkę tę indukują wzrost stężenia ROS i zaburzenia potencjału błonowego mitochondrium.”). Reszta bez zmian. |
| O15 | `dod` · lista szlaku ceramidowego, pkt 2 „Sfingomielinaza.” | **Przenieś do R5** zdanie „Uwalnia się przy tym cholesterol i zmienia się przepuszczalność błony.” |
| O16 | `dod` · tamże, pkt 3 „Ceramid jako przekaźnik.” i pkt 4 „Dwie odnogi.” | **Zastąp obydwa:** „3. <b>Ceramid jako przekaźnik.</b> Ceramid aktywuje kinazy – CAPK (aktywowane przez ceramid), MAPK (aktywowane przez mitogeny) i kaskadę kinaz SAPK (związanych ze stresem)/JNK – oraz <b>fosfatazy</b> CAPP (aktywowane przez ceramid; fosfataza odłącza reszty fosforanowe, czyli działa odwrotnie niż kinaza). 4. <b>Kaspazy wykonawcze.</b> Kinazy SAPK/JNK uruchamiają kaskadę kaspaz wykonawczych. (Od czego zależy, które enzymy włączy ceramid – część 2.)” Reszta → R5. |
| O17 | `dod` · „Lipidy tego szlaku mogą też zwiększać przepuszczalność…” | Zostaje **tylko pierwsze zdanie**. Sfingozyna i sfingozyno-1-fosforan → R5. W tabeli `c03-tab-dodatkowe`, wiersz „Sfingomielinowo-ceramidowy”, kol. 3: „ceramid → kinazy (z kwaśnej sfingomielinazy prawdopodobnie SAPK/JNK)” → „ceramid → kinazy SAPK/JNK”. |
| O18 | `zab` · tabela `c03-tab-choroby` | **Upraszczaj do pięciu wierszy** (kolejność źródła): cukrzyca typu I / osteoporoza · zawał mięśnia serca / białaczka · choroba Alzheimera / chłoniak · choroba Parkinsona / raki (np. piersi, prostaty) · stwardnienie rozsiane / nadczynność tarczycy. W akapicie „Udział zaburzeń apoptozy udowodniono…” zmień „Tabela zestawia przykłady chorób w obu grupach.” na „Tabela zestawia po pięć przykładów z każdej grupy (cała tabela źródła – część 2, `pageref c03-r-zaburzenia`).” |
| O19 | `zab` · h3 „Leki działające na szlaki apoptozy” (nagłówek, akapit, lista pięciu leków) | **Usuń h3 z listą (→ R6).** Na końcu akapitu „Wiele leków przeciwnowotworowych działa właśnie przez to…” (h3 „Dlaczego nowotwór staje się oporny na leki?”) **dopisz:** „Z tego samego powodu opracowano wiele leków przeciwnowotworowych, które wpływają na szlaki związane z apoptozą i ją nasilają (pięć przykładów z mechanizmami – część 2).” |
| O20 | `sta` · h4 „Komórka duża i płaska” | **Poprawka wierności (pkt 7, B2):** usuń zdanie „Tę zmianę widać w mikroskopie.” (źródło nie podaje metody). |
| O20a | `sta` · „Przy każdym znaczniku szukaj odpowiedzi na trzy pytania…” | **Upraszczaj do:** „Przy każdym znaczniku szukaj odpowiedzi na dwa pytania: co się zmienia i dlaczego to świadczy o starzeniu (oraz kiedy może zmylić). Jak się poszczególne znaczniki oznacza – zebrano w części 2 (`pageref c03-r-metody`).” |
| O21 | `sta` · h4 SA-β-Gal, „<b>Jak się wykrywa.</b> W mikroskopie świetlnym…” | **Przenieś cały akapit do R7.** Na końcu akapitu „<b>Co to jest.</b>” dopisz jedno zdanie: „W barwieniu na aktywność tego enzymu w komórkach powstaje niebieski osad.” |
| O22 | `sta` · h4 „Wzrost ziarnistości”; h4 „Wzrost poziomu lipofuscyny” | **Przenieś do R7** zdania: „Ziarnistość ocenia się cytometrem przepływowym albo w mikroskopie.”; „Wykrywa się ją barwieniami histochemicznymi.” |
| O23 | `sta` · h4 „Zmiany cytoszkieletu” | **Przenieś:** zdanie „W badanych liniach fibroblastów komórki stare miały ponad dwukrotnie więcej wimentyny…” → R8; zdanie „Te białka wykrywa się immunocytochemicznie…” → R7. Zostaje: „…Jej poziom rośnie wraz z liczbą podziałów, a komórki stare mają mniej aktyny i tubuliny niż młode (liczby – część 2).” |
| O24 | `sta` · „Najpierw krótkie przypomnienie z rozdz. 2.” | **Upraszczaj:** zdanie „W każdej fazie dominuje inny kompleks cykliny z CDK: w fazie G1 – …, a w fazie G2 – cyklina A–CDK1.” → „W każdej fazie dominuje inny kompleks cykliny z CDK (które – rozdz. 2).” Lista kompleksów → R8. Lista dwóch klas inhibitorów i akapit o szlakach p53–p21 i p16–pRb – bez zmian. |
| O25 | `sta` · h4 „Zahamowanie proliferacji” | **Przenieś do R7:** zdanie „Wbudowanie BrdU lub EdU wykrywa się immunocytochemicznie, techniką ELISA albo cytometrem przepływowym.” oraz nawias „(wykrywanie immunocytochemiczne)” przy Ki67. |
| O26 | `sta` · „<b>Kiedy może zmylić.</b> W starzeniu komórek podczas rozwoju zarodkowego…” | **Upraszczaj:** „…w wielu nowotworach p16 brak – m.in. w glejaku wielopostaciowym, czerniaku i gruczolakoraku trzustki. Wnioskuje się z tego, że p16 hamuje rozwój nowotworu.” Pozostałe trzy nowotwory → R8. |
| O27 | `sta` · „<b>Inne inhibitory i cyklina D1.</b>” oraz „<b>Jak się wykrywa.</b> Poziom inhibitorów…” | **Zastąp oba akapity jednym:** „<b>Inne inhibitory i cyklina D1.</b> Istotną rolę w starzeniu odgrywają też pozostałe inhibitory obu klas – m.in. p15, p27 i p57. Znacznikiem starzenia nowotworowych komórek nabłonkowych jest cyklina D1. (Doświadczenia, które to pokazały – część 2, `pageref c03-r-cykl`.)” Szczegóły → R8, metoda → R7. |
| O28 | `sta` · h4 „Zatrzymanie w cyklu” | **Przenieś do R7** zdanie „Zatrzymanie w cyklu bada się cytometrem przepływowym.” |
| O29 | `sta` · h4 DNA-SCARS, „Skupiska białek DDR w jądrze starej komórki…” | **Przenieś do R7** ostatnie zdanie „Wykrywa się je immunocytochemicznie.” |
| O30 | `sta` · h4 SAHF: „SAHF powstają etapami:” + lista 4 kroków + „W komórkach pozbawionych kinaz ATM lub ATR…” | **Przenieś do R9** listę kroków i zdanie o ATM/ATR. **W części 1 zostaje:** „SAHF powstają etapami, z udziałem ciałek jądrowych PML (o nich niżej) i białek opiekuńczych histonów (kolejność etapów – część 2, `pageref c03-r-chromatyna`). Są znacznikiem i starzenia przyspieszonego wywołanego onkogenami, i replikacyjnego, ale ich pojawienie się zależy od typu komórek.” Pierwszy akapit h4 („Heterochromatyna to…”) bez zmian. |
| O31 | `sta` · h4 PML | **Przenieś do R7** zdanie „Białko PML wykrywa się immunocytochemicznie.” **Poprawka wierności (pkt 7, B4):** „W starzeniu liczba i wielkość PML-NB rosną, a w nowotworzeniu – maleją…” → „W starzeniu liczba i wielkość PML-NB rosną, a w nowotworzeniu ich liczba maleje, bo synteza PML jest obniżona.” |
| O32 | `sta` · h4 „Skracanie telomerów” | **Upraszczaj:** „Razem z kompleksem sześciu białek, zwanych <b>szelterynami</b>, pełnią funkcję ochronną.” (nazwy → R9); ostatnie zdanie: „Długość telomerów jest znacznikiem starzenia replikacyjnego.” (FISH, Southern → R7). |
| O33 | `sta` · h4 „Spadek poziomu laminy B1” | **Przenieś:** „…natomiast nie zależy od p38, ATM ani NF-κB.” → R9; „Laminę B1 wykrywa się immunocytochemicznie i techniką Western blotting.” → R7. Zostaje: „Spadek ten wymaga aktywności jednego z dwóch kluczowych szlaków starzenia, p16–pRb albo p53–p21.” |
| O34 | `sta` · h3 SASP, „SASP pojawia się przy trwałej aktywacji…” i „Jedną z pierwszych cytokin…” | **Upraszczaj akapit 2:** „…Przy przejściowej aktywacji komórki tych czynników nie wydzielają. Wydzielaniem sterują białka tego szlaku i czynniki transkrypcyjne, m.in. NF-κB (wszyscy regulatorzy – część 2, `pageref c03-r-chromatyna`).” ATM, NBS1, CHK2, C/EBP-β, p38MAPK, zdanie o p53 → R9. W akapicie 3 **przenieś do R7** ostatnie zdanie („SASP mierzy się cytometrem przepływowym i techniką ELISA.”); reszta (IL-1α → IL1R → NF-κB → IL-6, IL-8; skutki) bez zmian. |
| O35 | `sta` · tabela `c03-tab-wykrywanie` | **W części 1 zostają dwie pierwsze kolumny** („Znacznik” / „Co się zmienia w komórce starej”) jako tabela-podsumowanie; kolumna „Jak się go wykrywa” → R7 (tam pełna tabela metod, id `c03-r-tab-metody`). |
| O36 | `bcl` · „Rodzina Bcl-2 (ang. B-cell CLL/lymphoma 2)…” | **Poprawka (pkt 7, C1):** zdanie „Nazwa wskazuje na nowotwory z limfocytów B.” → „W nazwie są limfocyt B (<i>B-cell</i>) i chłoniak (<i>lymphoma</i>) – gen wykryto właśnie w chłoniakach.” |

**Ryciny części 1 – kontrola podpisów po zmianach** (żaden podpis nie staje się fałszywy):

| Rycina | Napisy dotyczące szczegółów z części 2 | Wniosek |
|---|---|---|
| `c03-fig-zmiany` | – | bez zmian |
| `c03-fig-kaspaza` | masy: 3–24, 17–21, 10–13, 32–55 kDa | podpis mas nie wymienia; R2 objaśnia je z `figref` do tej ryciny |
| `c03-fig-bcl2` | Bcl-2, Bcl-X<sub>L</sub>, Bcl-W, Mcl-1; Bax, Bak; Bad, Bid; Bim | wszystkie zostają w tabeli części 1 (O7) |
| `c03-fig-szlaki` | „uwalniane też: AIF, Smac/DIABLO”; „cięcie: laminy, aktyna, PARP, DNA-PK” | nazwy zostają w części 1 (O11; lista substratów bez zmian) |
| `c03-fig-dodatkowe` | A: „laminy, histon H1, SET”; B: „kinazy SAPK/JNK albo CAPK, MAPK i fosfatazy CAPP” | nazwy zostają (O14, O16) |
| `c03-fig-starzenie` | „IL-1α, IL-6, IL-8”; „też p15, p27, p57, cyklina D1”; „γH2AX, 53BP1”; „8-oksyGua, 8-oksydG” | nazwy zostają (O27, O34) |

---

## 4. Plan części 2

**Zasady dla całej części 2.**
- Każda sekcja zaczyna się od zdania-nawiązania z `pageref` do sekcji części 1 („W części 1 (s. X) wiesz już, że…”), potem problem, który rozwiązuje szczegół („czego jeszcze nie wiesz”), potem treść.
- **Nie dopowiadamy mechanizmów, których źródło nie podaje.** Przy każdej sekcji wypisałem „nie dopowiadać” – miejsca, w których łatwo dodać wiedzę spoza źródła.
- Informacje „(ryc.)” – odczytane z rycin – podawać jako opis schematu źródła („na schemacie Jóźwiaka…”), nie jako samodzielne twierdzenia (decyzja Z1).
- Rozwinięcia skrótów: raz, w tabeli R10; w tekście R1–R9 tylko tam, gdzie rozwinięcie coś tłumaczy (np. JNK, Apaf-2, ICE).
- Rycin w części 2 brak; wolno odsyłać `figref` do rycin części 1.
- Linie `p.src` – podane przy sekcjach.

### R1 · `c03-r-historia` · „Skąd to wiemy? Nazwa, odkrycia i nicień *C. elegans*”
- **Łączy się z:** `c03-apoptoza` (definicja i nazwy), pośrednio `c03-kaspazy`, `c03-bcl2`, `c03-dodatkowe`.
- **Treść:**
  1. *(nowe, D02)* Termin „apoptoza” wprowadzili w 1972 r. J.F. Kerr, A.H. Wyllie i A.R. Currie (s. 165).
  2. *(z cz. 1, O2; D08)* Starsze określenie „programowana śmierć komórki” stosowano pierwotnie tylko do śmierci zachodzącej w procesach fizjologicznych, które warunkują prawidłowe funkcjonowanie organizmu – na etapie embrionalnym i później; dziś oba terminy stosuje się często zamiennie (s. 165).
  3. *(z cz. 1, O1 + nowe; D05, D06)* Genetyczne podstawy apoptozy i udział ekspresji genów w jej regulacji poznano najpierw u nicienia *Caenorhabditis elegans*. Badania R. Horvitza, S. Brennera i J. Sulstona uhonorowano w 2002 r. Nagrodą Nobla (s. 165).
  4. *(z cz. 1, O4 + nowe; D35)* Pierwszego przedstawiciela kaspaz zidentyfikowano jako enzym, który przekształca pro-interleukinę 1β w aktywną interleukinę 1β – stąd nazwa ICE (*Interleukin Converting Enzyme*, enzym konwertujący interleukinę). Kluczową rolę ICE w apoptozie dowiedziono dzięki sklonowaniu genu *ced-3* *C. elegans*: jego produkt jest podobny do ICE (s. 167).
  5. *(nowe + z cz. 1, O6; D18, D20)* Gen *bcl-2* zidentyfikowano po raz pierwszy w 1986 r. – jako onkogen aktywowany przez translokację t(14;18). Antyapoptotyczne działanie białka Bcl-2 poznano dzięki temu, że budową i funkcją jest homologiczne (podobne) do białka Ced-9 *C. elegans* (s. 166).
  6. *(nowe, D88)* Najpóźniej opisano szlak indukowany stresem: wyniki badań, które go przedstawiły, opublikowano w 2000 r. (s. 174).
- **Wskazówka tłumaczenia.** Problem: w części 1 kaspazy i Bcl-2 pojawiają się „gotowe” – skąd wiadomo, że służą do apoptozy? Oś wyjaśnienia: dwa białka nicienia – dwie rodziny u człowieka: produkt *ced-3* ↔ kaspazy (ICE), Ced-9 ↔ Bcl-2. Powiązać ze słowem „wysoko konserwatywne” z części 1: skoro budowa niewiele zmieniła się w ewolucji, białko poznane u nicienia podpowiedziało funkcję białka człowieka. Daty ułożyć rosnąco (1972 → 1986 → 2000 → 2002) – krótka lista chronologiczna, nie tabela.
- **Nie dopowiadać:** innych genów *ced*, liczb komórek nicienia (to Drewa 8.3 – poza zakresem), nazwisk odkrywców Bcl-2, tego, kto i kiedy opisał poszczególne kaspazy.
- **Tabela:** nie. · **Źródło:** `Drewa s. 165–167, 174`.

### R2 · `c03-r-kaspazy` · „Kaspazy – szczegóły budowy i siedem kaspaz w tabeli”
- **Łączy się z:** `c03-kaspazy` (`figref c03-fig-kaspaza`, tabela `c03-tab-kaspazy`).
- **Treść:**
  1. *(nowe, D42)* Budowę kaspaz poznano dzięki krystalografii rentgenowskiej i sekwencjonowaniu białek. Kaspazy są syntetyzowane jako katalitycznie nieczynne, trzyczęściowe proenzymy o masie 32–55 kDa (s. 168).
  2. *(nowe, D43)* Masy części: prodomena 3–24 kDa, duża podjednostka p20 – 17–21 kDa, mała podjednostka p10 – 10–13 kDa. p20 zawiera centrum katalityczne; p10 źródło nazywa „małą podjednostką katalityczną”. Na schemacie źródła p20 to podjednostka α, p10 – podjednostka β (s. 168, ryc. 8.4).
  3. *(nowe, D48)* Katalityczna reszta cysteiny leży w dużej podjednostce, w obrębie konserwatywnego fragmentu sekwencji zapisywanego QACxG (ryc. 8.4, s. 169).
  4. *(nowe, D44, D49)* W większości prokaspaz p20 i p10 oddziela sekwencja łącznikowa. Schemat źródła pokazuje trzy miejsca cięcia, każde za resztą kwasu asparaginowego (zapis „asp-x”): jedno między prodomeną a p20 i dwa po obu stronach sekwencji łącznikowej (s. 168–169).
  5. *(nowe, D45)* Duża N-końcowa prodomena zawiera długi motyw (80–100 reszt aminokwasowych), który uczestniczy w przekazywaniu (transdukcji) sygnałów apoptozy (s. 168).
  6. *(nowe, D47)* Subdomeny DED i CARD są zbudowane z α-helis ułożonych nierównolegle, o charakterze amfipatycznym; z innymi białkami oddziałują przez interakcje elektrostatyczne lub hydrofobowe (s. 168).
  7. *(nowe, D38)* Tabela 8.2 w całości (s. 168):

  | Grupa | Kaspaza (inne nazwy) | Struktura | Masa (kDa) | Lokalizacja chromosomowa |
  |---|---|---|---|---|
  | inicjatorowe | kaspaza 2 (ICH-1) | 1 CARD + p20 + p10 | 48,8 | 7q34-q35 |
  | inicjatorowe | kaspaza 8 (MACH, FLICE, Mch5) | 2 DED + p20 + p10 | 55 | 2q33-q34 |
  | inicjatorowe | kaspaza 9 (ICE-LAP6, Mch6) | 1 CARD + p20 + p10 | 50 | 1p36.3-p36.1 |
  | inicjatorowe | kaspaza 10 (Mch-4) | 2 DED + p20 + p10 | 55 | 2q33-q34 |
  | wykonawcze | kaspaza 3 (CPP32, Apopain, Yama) | p20 + p10 | 32 | 4q34 |
  | wykonawcze | kaspaza 6 (Mch-2) | p20 + p10 | 34 | 4q25 |
  | wykonawcze | kaspaza 7 (Mch3, ICE-LAP-3, CMH-1) | p20 + p10 | 34 | 10q25 |

- **Wskazówka tłumaczenia.** Zacząć od ryciny `c03-fig-kaspaza` z części 1: „na rycinie widziałeś liczby w kDa – skąd się biorą i co mówią”. Trzy rzeczy do wyjaśnienia: (a) *rachunek mas*: trzy części składają się na całą prokaspazę o masie 32–55 kDa (nie sumować skrajnych wartości – zakresy obejmują różne kaspazy); w tabeli kaspazy inicjatorowe są cięższe (48,8–55 kDa) niż wykonawcze (32–34 kDa) – zgadza się to z tym, że w prodomenie mają CARD albo dwie DED (pisać „zgadza się z”, nie „dlatego”); (b) *po co łącznik i trzy cięcia*: cięcie przed p20 oddziela prodomenę, dwa cięcia przy łączniku rozdzielają p20 i p10 – stąd w części 1 „aktywny enzym to 2 × p20 + 2 × p10”; (c) *po co amfipatyczne helisy*: to nimi DED i CARD „chwytają” inne białka – to ta sama zasada „domena z domeną tego samego typu” (DD–DD, DED–DED, CARD–CARD) z części 1. „Amfipatyczny” objaśnić jednym zdaniem (cząsteczka z częścią hydrofilową i hydrofobową). W QACxG wystarczy powiedzieć, że to zapis jednoliterowy aminokwasów i że C oznacza cysteinę. Odczyt tabeli: kaspazy 8 i 10 mają tę samą budowę, masę i to samo miejsce w genomie (2q33-q34); zapis lokalizacji chromosomowej – odsyłacz do `chapref #c09`. Dopowiedzieć dwie rzeczy porządkujące: (1) zapis „p20 + p10” przy kaspazach wykonawczych nie znaczy, że nie mają prodomeny – w szlaku pseudoreceptorowym kaspaza 3 odcina prodomenę kaspazy 7 (s. 172; część 1, `pageref c03-dodatkowe`); (2) tabela obejmuje 7 z 14 kaspaz; kaspazy 12 (szlak stresowy) w niej nie ma.
- **Nie dopowiadać:** rozwinięć nazw alternatywnych (FLICE, CPP32 itd. – źródło ich nie rozwija), pozostałych kaspaz (1, 4, 5, 11… – to Jóźwiak poza zakresem), inhibitorów kaspaz (IAP), co oznaczają Q, A, G i x.
- **Tabela:** tak (jak wyżej, `tbl wide`). · **Źródło:** `Drewa s. 167–169, 172`.

### R3 · `c03-r-bcl2` · „Rodzina Bcl-2 – pełna lista i domeny każdego białka”
- **Łączy się z:** `c03-bcl2` (`figref c03-fig-bcl2`).
- **Treść:**
  1. *(z cz. 1, O7 + nowe; D24, D25)* Tabela 8.1 w całości (s. 166). **Proapoptotyczne (16):** Bax, Bak, Bok/Mtd, Bad, Bid, Bim, Bik, Hrk, Bcl-X<sub>S</sub>, APR/Noxa, PUMA, p193, Bcl-Gs, Bcl-rambo/Mil, Nip3, Nix/BNIP. **Antyapoptotyczne (6):** Bcl-2, Bcl-X<sub>L</sub>, Mcl-1, Bfl-1/A1, Bcl-W, Bcl-B/Boo/Diva. (Ukośnik łączy nazwy podane w tabeli razem. W tekście Drewa wymienia dziewięć pierwszych proapoptotycznych i wszystkie antyapoptotyczne. Tabela ma tytuł „Wybrane białka” – genów rodziny jest 26.)
  2. *(nowe, D27)* Układ domen według ryc. 8.3 (s. 167):

  | Białka | Domeny (kolejność jak na rycinie źródła) | Grupa |
  |---|---|---|
  | Bcl-2, Bcl-X<sub>L</sub>, Bcl-W, Bcl-B, Mcl-1 | BH4 – BH3 – BH1 – BH2 – TM | antyapoptotyczne |
  | Bfl-1 | BH1 – BH2 | antyapoptotyczne |
  | Bax, Bak, Bok | BH3 – BH1 – BH2 – TM | proapoptotyczne |
  | Bad, Bid | BH3 | proapoptotyczne |
  | Bim, Bik, Hrk, APR (Noxa) | BH3 – TM | proapoptotyczne |

- **Wskazówka tłumaczenia.** Problem: w części 1 padło „większość antyapoptotycznych ma BH1–BH4” i „proapoptotyczne mają BH1–BH3 albo tylko BH3” – kto jest wyjątkiem i które białka są „tylko BH3”? Tabela domen odpowiada wprost: (a) wyjątkiem od „większości” jest Bfl-1 – chroni komórkę, a ma tylko BH1 i BH2; (b) proapoptotyczne dzielą się na dwa typy: z trzema domenami (Bax, Bak, Bok) i z samą BH3 (Bad, Bid; z domeną TM: Bim, Bik, Hrk, APR); (c) Bid – łącznik szlaków z części 1 – należy do białek z samą BH3; (d) między pierwszym a trzecim wierszem jedyna różnica na schemacie to domena BH4. To są obserwacje z ryciny – podać je jako „co widać w tabeli”.
- **Nie dopowiadać:** funkcji poszczególnych domen (BH4 „chroni”, BH3 „zabija”), podziału na „aktywatory i uwrażliwiacze” (Jóźwiak, poza zakresem), lokalizacji pojedynczych białek wywiedzionej z obecności TM (źródło mówi tylko, że TM „prawdopodobnie odgrywa rolę w lokalizacji”), układu domen białek, których na ryc. 8.3 nie ma (PUMA, p193, Bcl-Gs, Bcl-rambo, Nip3, Nix, Bcl-X<sub>S</sub>).
- **Tabela:** tak – dwie (lista dwukolumnowa; układ domen). · **Źródło:** `Drewa s. 166–167`.

### R4 · `c03-r-szlaki` · „Szlak zewnętrzny i wewnętrzny – pozostałe receptory, droga przez DAXX, skład megakanału”
- **Łączy się z:** `c03-szlaki` (`figref c03-fig-szlaki`).
- **Treść:**
  1. *(z cz. 1, O8 + nowe; D54)* Receptory śmierci wymienione w źródle („do rodziny receptorów TNF zalicza się m.in.” – lista nie jest zamknięta; s. 169):

  | Receptor | Inne nazwy | Ligand |
  |---|---|---|
  | Fas | CD95, Apo1 | FasL (ligand Fas) |
  | TNFR1, TNFR2 | receptory czynnika martwicy nowotworów 1 i 2 (*Tumor Necrosis Factor Receptor 1, 2*) | TNFα |
  | TRAIL-R1, TRAIL-R2 | receptory liganda TRAIL (*TNF-Related Apoptosis-Inducing Ligand-R1, R2*) | TRAIL |

  2. *(z cz. 1, O9; D58, D59)* Droga przez DAXX (s. 169, 171): aktywacja receptora Fas może się odbywać także przez białko adaptorowe DAXX, które angażuje kinazę JNK (*Jun-N-terminal Kinase*). JNK fosforyluje N-końcowy odcinek czynnika transkrypcyjnego c-Jun oraz kinazę odpowiedzi zewnątrzkomórkowej ERK (*Extracellular Signal-regulated Kinase*) i w ten sposób uruchamia kaskadę kaspaz. Szlak z DAXX działa tylko w niektórych typach komórek i może być modyfikowany: DAXX bywa zastępowane układem sygnalizacyjnym związanym z małymi białkami G z rodziny Rho (Rac-1).
  3. *(z cz. 1, O10 + nowe; D65, D66)* Megakanał – wszystkie składniki z opisu i schematu źródła (s. 170–171):

  | Składnik | Gdzie (wg ryc. 8.5) | Co mówi źródło |
  |---|---|---|
  | ANT – translokator nukleotydów adeninowych | błona wewnętrzna | zasadniczy element kanału („najczęściej uznaje się”) |
  | VDAC – poryna | błona zewnętrzna | tworzy kompleks z ANT; do niej przyłącza się zmieniony Bax |
  | BPR – obwodowy receptor benzodiazepiny | błona zewnętrzna, obok VDAC | tworzy kompleks z ANT i VDAC |
  | kinaza kreatynowa (CK) | między błonami, przy styku ANT–VDAC | enzym, któremu przypisuje się funkcję regulatorową |
  | peroksydaza glutationowa (GPX) | przy ANT | enzym, któremu przypisuje się funkcję regulatorową |
  | Bcl-2, Bax | od strony cytoplazmy | łączą się z kanałem; na schemacie Bax „+”, Bcl-2 „–” przy wypływie cytochromu c |

  Źródło zastrzega, że istnieje kilka hipotetycznych modeli budowy i działania megakanałów; rycina pokazuje jeden „hipotetyczny model”.
  4. *(z cz. 1, O11 + nowe; D68)* Co wychodzi z przestrzeni międzybłonowej przy wzroście przepuszczalności PTP (s. 171): cytochrom c – zwany też Apaf-2 (*Apoptosis protease activating factor-2*); czynnik indukcji apoptozy AIF; prokaspazy 2, 3 i 9; białko Smac/DIABLO.
- **Wskazówka tłumaczenia.** (1) Tabela receptorów: jedno zdanie, że zasada jest ta sama co dla Fas – ligand na receptorze z domeną DD. (2) DAXX: zestawić z FADD z części 1 – tam adaptor własną domeną DED chwyta prokaspazę; tu adaptor włącza kinazę, a sygnał idzie dalej przez fosforylację (definicja kinazy jest w części 1). Nazwa JNK („kinaza N-końca Jun”) sama mówi, co enzym fosforyluje. Zaznaczyć, że tę samą kinazę JNK spotka się w szlaku ceramidowym (R5). (3) Megakanał: zacząć od zdania z części 1 („ANT + VDAC, od cytoplazmy Bcl-2 i Bax”) i dołożyć trzy brakujące elementy; podkreślić słowo „hipotetyczny”. Znaki „+” i „–” przy Bax i Bcl-2 to obrazowe powtórzenie tego, co część 1 mówi o bramie. (4) Lista białek: nazwa Apaf-2 tłumaczy się sama, gdy postawić ją obok Apaf-1 – apoptosom to Apaf-1 + Apaf-2 (cytochrom c) + prokaspaza 9; zauważyć, że prokaspaza 9 jest na liście białek wychodzących z mitochondrium, a w cytoplazmie wchodzi do apoptosomu.
- **Nie dopowiadać:** jak fosforylacja c-Jun i ERK włącza kaspazy (źródło tego nie podaje); co robią AIF i Smac/DIABLO po wyjściu z mitochondrium (źródło nie podaje; nie tłumaczyć „IAP”); funkcji kinazy kreatynowej, peroksydazy glutationowej i BPR; białka TRADD i innych receptorów (Jóźwiak poza zakresem).
- **Tabela:** tak – dwie (receptory; składniki megakanału). · **Źródło:** `Drewa s. 169–171`.

### R5 · `c03-r-dodatkowe` · „Szlak pseudoreceptorowy i ceramidowy – szczegóły”
- **Łączy się z:** `c03-dodatkowe` (`figref c03-fig-dodatkowe`, panele A i B).
- **Treść – szlak pseudoreceptorowy (s. 172–173):**
  1. *(z cz. 1, O12, O14; D78)* Inne nazwy: granzym B = GrB = fragmentyna-2; granzym A = GrA = fragmentyna-1.
  2. *(z cz. 1, O13 + nowe; D74)* Granzym B ma według źródła trzy drogi do wnętrza komórki docelowej: (a) przez kanał utworzony przez perforynę w jej błonie (tak uważano początkowo); (b) bez perforyn – na zasadzie endocytozy; (c) bez perforyn – przy udziale receptora mannozo-6-fosforanu. Na schemacie źródła (ryc. 8.6) drogi (b) i (c) opisano jako endocytozę i obie prowadzą przez endosom. Granzym A wnika przy udziale perforyny.
  3. *(z cz. 1, O14; D77)* Ścieżkę z granzymem A indukują wzrost stężenia reaktywnych form tlenu i zaburzenia potencjału błonowego mitochondrium.
- **Treść – szlak sfingomielinowo-ceramidowy (s. 172):**
  4. *(z cz. 1, O15; D81)* Hydrolizując sfingomielinę, sfingomielinaza uwalnia cholesterol i jednocześnie zmienia przepuszczalność błony.
  5. *(z cz. 1, O16; D83–D85)* To, co ceramid aktywuje, zależy od czynnika stymulującego sygnał, od typu komórki i od rodzaju sfingomielinazy:

  | Sfingomielinaza | Co aktywuje powstały ceramid | Dalej |
  |---|---|---|
  | obojętna | kinazy CAPK i MAPK, fosfatazy CAPP | (źródło nie podaje) |
  | kwaśna | prawdopodobnie kinazy SAPK/JNK | kaskada kaspaz wykonawczych |

  6. *(z cz. 1, O17; D87)* Produkty metabolizmu ceramidu też uczestniczą w apoptozie – z przeciwnym skutkiem: sfingozyna jest inhibitorem antyapoptotycznych białek Bcl-2 i Bcl-X<sub>L</sub>; jej ufosforylowana forma, sfingozyno-1-fosforan, hamuje apoptozę – blokuje wypływ cytochromu c i białka Smac/DIABLO z przestrzeni międzybłonowej mitochondrium.
- **Wskazówka tłumaczenia.** Pseudoreceptorowy: problem „jak enzym z zewnątrz dostaje się do cytoplazmy?” – trzy odpowiedzi; endocytozę objaśnić jednym zdaniem (wchłonięcie w pęcherzyku z błony – definicja była w części 1 i przechodzi tu razem z O13). Ceramidowy: problem z części 1 – „ceramid aktywuje kinazy i fosfatazy” – które i kiedy? Tabela dwóch odnóg; słowo „prawdopodobnie” musi zostać. Lipidy pokazać jako trzy cząsteczki o różnym skutku: ceramid (przekazuje sygnał do apoptozy), sfingozyna (hamuje białka, które chronią komórkę – wniosek logiczny „więc sprzyja apoptozie” można zostawić, jest w obecnym tekście), sfingozyno-1-fosforan (hamuje apoptozę). Powiązać z bramą mitochondrialną z części 1: Bcl-2 i Bcl-X<sub>L</sub> to białka, które nie wypuszczają cytochromu c; sfingozyno-1-fosforan działa w tę samą stronę co one. Przypomnieć, że JNK wystąpiła już przy DAXX (R4).
- **Nie dopowiadać:** co dalej robią CAPK, MAPK i CAPP; jak ROS „indukuje” ścieżkę granzymu A; enzymów przemiany ceramidu w sfingozynę; czym jest kompleks SET.
- **O szlaku indukowanym stresem** źródło nie podaje nic ponad część 1 (poza rokiem 2000 – R1); nie tworzyć pustego h3.
- **Tabela:** tak – jedna mała (dwie odnogi). · **Źródło:** `Drewa s. 172–173`.

### R6 · `c03-r-zaburzenia` · „Zaburzenia apoptozy – cała tabela chorób i leki nasilające apoptozę”
- **Łączy się z:** `c03-zaburzenia` (tabela `c03-tab-choroby`, h3 o oporności na leki); pkt 2 także z `c03-fizjologia`.
- **Treść:**
  1. *(z cz. 1, O18; J08)* Tabela 11.4 w całości (s. 127) – pozycje spoza części 1 wyróżnić (np. kursywą):

  | Nasilenie apoptozy | Zahamowanie apoptozy |
  |---|---|
  | cukrzyca typu I | osteoporoza |
  | zawał mięśnia serca | białaczka |
  | choroba Alzheimera | chłoniak |
  | choroba Parkinsona | raki (np. piersi, prostaty) |
  | stwardnienie rozsiane | nadczynność tarczycy |
  | *wrzodziejące zapalenie jelita grubego* | *zespół Smitha* |
  | *choroba Hashimoto* | *układowy toczeń rumieniowaty* |
  | *AIDS* | |

  2. *(nowe, J05)* Przykład z preparatu (podpis ryc. 11.7, s. 126): w raku gruczołowo-torbielowatym między komórkami nowotworowymi leżą pojedyncze komórki apoptotyczne – widać kondensację jądra, zmniejszenie komórek i ciałka apoptotyczne.
  3. *(z cz. 1, O19; J12)* Pięć leków nasilających apoptozę (podpis ryc. 11.8, s. 127):

  | Lek | Co hamuje | Dlaczego to nasila apoptozę (wg źródła) | Zastosowanie podane w źródle |
  |---|---|---|---|
  | cetuksymab | przeciwciało monoklonalne przeciw receptorowi nabłonkowego czynnika wzrostu (EGF) | EGF aktywuje szlaki chroniące przed apoptozą | rak jelita grubego, rak płaskonabłonkowy skóry |
  | erlotynib | inhibitor kinazy tyrozynowej związanej z receptorami EGF | źródło nie podaje osobno (ten sam receptor EGF co wyżej) | niedrobnokomórkowy rak płuca, rak trzustki |
  | imatynib | inhibitor kinazy tyrozynowej | źródło nie podaje (na schemacie: Bcr/Abl) | białaczki |
  | sorafenib | hamuje białko Raf | źródło nie podaje (na schemacie: ogniwo drogi od receptora) | rak nerki, wątroby i tarczycy |
  | bortezomib | inhibitor proteasomu | w proteasomie rozkładane są niektóre białka proapoptotyczne | szpiczak mnogi, chłoniaki |

  4. *(nowe, J13 – odczyt z ryciny, decyzja Z1)* Schemat ryc. 11.8 (s. 127). Od receptora w błonie komórkowej biegną dwie drogi: **Ras → Raf → Mek → Erk** oraz **PI3K → Akt**. Erk hamuje białko Bim; Akt hamuje Bim i Bax. Na dole schematu łańcuch: Bim → Bim-P (postać ufosforylowana) → Bim → Bax → apoptoza. Osobno narysowano Bcr/Abl ze strzałką do Raf. Punkty uchwytu leków na schemacie: cetuksymab – receptor od strony zewnątrzkomórkowej; erlotynib – receptor od strony cytoplazmy; imatynib – Bcr/Abl; sorafenib – Raf; **idelalizyb – PI3K** (lek jest tylko na rycinie, podpis go nie wymienia); bortezomib – przy ufosforylowanej postaci Bim (na rycinie „Bim-P”).
- **Wskazówka tłumaczenia.** Leki: w części 1 student wie, że nowotwór blokuje apoptozę i że leki mają ją przywracać – tu pytanie „w co konkretnie celują?”. Oś: Bim i Bax to proapoptotyczne białka rodziny Bcl-2 z części 1 (Bax tworzy pory dla cytochromu c). Sygnał od receptora czynnika wzrostu trzyma je „na hamulcu” (Erk i Akt hamują Bim i Bax) – stąd zdanie źródła „EGF aktywuje szlaki chroniące przed apoptozą”. Każdy lek z ryciny przerywa ten sygnał w innym miejscu: na receptorze (cetuksymab z zewnątrz, erlotynib od środka), niżej (sorafenib – Raf; idelalizyb – PI3K; imatynib – Bcr/Abl, które na schemacie pobudza Raf) – skutek ten sam: hamulec z Bim i Bax znika. Bortezomib działa inaczej: nie przerywa sygnału, tylko zatrzymuje rozkład białek proapoptotycznych w proteasomie (logika zdania z obecnego tekstu: „gdy proteasom nie działa, te białka nie są rozkładane”). Przejść to jako jeden ciąg „receptor → … → Bim, Bax → apoptoza”, zaznaczając, że to opis schematu źródła. Kinaza tyrozynowa, proteasom – po jednym zdaniu objaśnienia, jak w obecnym tekście (proteasom jest też w rozdz. 2). Tabela chorób: źródło podaje same nazwy – powiedzieć to wprost i odesłać do mechanizmów znanych z części 1 tylko dla nowotworów, choroby Alzheimera i Parkinsona.
- **Nie dopowiadać:** mechanizmów chorób z tabeli (cukrzyca, Hashimoto, AIDS, toczeń, zespół Smitha…) – to byłaby wiedza spoza źródła (częściowo Drewa 8.4, poza zakresem); że Erk fosforyluje Bim i że Bim-P trafia do proteasomu (rycina tego wprost nie mówi – wolno napisać tylko, gdzie na schemacie stoi bortezomib); czym są Bcr/Abl, Ras, Mek, PI3K, Akt ponad to, że są ogniwami drogi; wskazań idelalizybu.
- **Tabela:** tak – dwie (choroby; leki). · **Źródło:** `Jóźwiak s. 126–127`.

### R7 · `c03-r-metody` · „Jak oznacza się znaczniki starzenia”
- **Łączy się z:** `c03-starzenie` (tabela `c03-tab-wykrywanie` – w części 1 bez kolumny metod).
- **Treść** *(z cz. 1: O21–O23, O25, O27–O29, O31–O35; uzupełnione o brzmienie źródła)* – tabela `c03-r-tab-metody`:

  | Znacznik | Jak się go oznacza (wg źródła) | s. |
  |---|---|---|
  | SA-β-Gal | (a) mikroskop świetlny: komórki utrwala się, potem inkubuje w roztworze barwiącym z X-gal – substratem β-galaktozydazy; enzym tnie X-gal i powstaje barwny produkt, widoczny w komórkach jako niebieski osad (precypitat); (b) cytometr przepływowy: substrat, który pod wpływem β-galaktozydazy emituje zieloną fluorescencję – szybka ocena ilościowa komórek o podwyższonej aktywności | 139 |
  | ziarnistość | cytometr przepływowy lub obserwacja mikroskopowa | 139–140 |
  | lipofuscyna | barwienia histochemiczne | 140 |
  | wimentyna | barwienia immunocytochemiczne, Western blotting | 140 |
  | proliferacja: liczba komórek | zliczanie komórek (przy zahamowaniu liczba się nie zmienia) | 140 |
  | proliferacja: BrdU, EdU | immunocytochemicznie, techniką ELISA, cytometrem przepływowym | 140 |
  | Ki67 | immunocytochemicznie | 140 |
  | inhibitory cyklu (p16, p21 i inne), cyklina D1 | m.in. Western blotting | 141 |
  | zatrzymanie w cyklu | cytometr przepływowy | 141 |
  | DNA-SCARS | barwienia immunocytochemiczne | 142 |
  | SAHF | barwienie jądra DAPI; znakowanie na obecność histonu H3 zmetylowanego na lizynie 9, białka HP1, histonu makroH2A, białka HMGA | 142 |
  | PML | barwienia immunocytochemiczne | 142 |
  | długość telomerów | FISH, Southern blotting | 143 |
  | lamina B1 | barwienia immunocytochemiczne, Western blotting | 143 |
  | 8-oksydG, 8-oksyGua | oznaczane w jądrowym DNA narządów (gryzonie), w leukocytach i w moczu (ludzie); techniki źródło nie podaje | 143 |
  | metylacja DNA | poziom 5-metylocytozyny (5-mC); techniki źródło nie podaje | 143 |
  | SASP | cytometr przepływowy, ELISA | 144 |
  | zmiana morfologii; DEC1, DCR2 | źródło nie podaje metody | 138–139, 144 |

- **Wskazówka tłumaczenia.** Problem: w części 1 było „co się zmienia” – a jak to zobaczyć? Przed tabelą jeden akapit porządkujący: prawie wszystkie znaczniki obsługuje pięć narzędzi – barwienie i mikroskop (X-gal, barwienia histochemiczne, DAPI), przeciwciała w komórce (immunocytochemia – „barwienie przeciwciałami, które rozpoznają dane białko”, jak w obecnym tekście), Western blotting (`chapref #c06`), cytometr przepływowy (według źródła pozwala szybko ocenić ilościowo, ile komórek ma daną cechę), ELISA; do DNA: FISH (`chapref #c09`) i Southern blotting (`chapref #c06`). Rozwinąć SA-β-Gal jako jedyną opisaną krok po kroku procedurę: utrwalenie → inkubacja z substratem → enzym tnie substrat → barwny osad tam, gdzie jest enzym; zestawić z wersją cytometryczną (ten sam pomysł, produkt świeci zamiast się wytrącać, wynik w liczbach). Powiązać z wnioskiem części 1: skoro żaden znacznik nie jest swoisty, w praktyce łączy się metody (źródło: SA-β-Gal + zatrzymanie w cyklu).
- **Nie dopowiadać:** pH, stężeń, czasów inkubacji, nazw odczynników poza X-gal (artykuł ich nie podaje – także pH roztworu barwiącego nie ma w źródle), zasad działania ELISA i cytometru ponad jedno zdanie, metod dla znaczników, przy których źródło milczy.
- **Tabela:** tak (`tbl wide`). · **Źródło:** `Alster s. 139–144`.

### R8 · `c03-r-cykl` · „Znaczniki starzenia: morfologia, lizosomy i cykl – doświadczenia i liczby”
- **Łączy się z:** `c03-starzenie` (h3 „Struktura i morfologia komórki”, „Proliferacja i cykl komórkowy”).
- **Treść (h3 wg grup z części 1):**
  - **Kształt komórki.** 1. *(nowe, A08)* Powiększenie i spłaszczenie opisano w komórkach prawidłowych (ludzkie komórki mięśni gładkich, fibroblasty) oraz w liniach nowotworowych: ludzkie komórki raka okrężnicy HCT116, linie glejaka U343 MG-A, U87 MG i U343 MG, linia kostniakomięsaka U2OS, ludzkie komórki raka piersi MCF-7 (s. 139). 2. *(nowe, A09)* W melanocytach starzejących się wskutek nadekspresji onkogenu RAS stwierdza się intensywną wakuolizację; melanocyty starzejące się wskutek nadekspresji onkogenu BRAF mają wrzecionowate jądra (s. 139).
  - **SA-β-Gal.** 3. *(nowe, A11, A13)* Znacznik opisali Dimri i wsp.; był przydatny także w badaniu starzenia u gryzoni i naczelnych, stosuje się go też u starzejących się organizmów modelowych – np. Danio pręgowanego i *C. elegans* (s. 139). 4. *(nowe, A15, A16)* Dwa dowody, że SA-β-Gal nie jest niezbędna do starzenia: fibroblasty pacjentów z gangliozydozą GM1 ulegały starzeniu replikacyjnemu oraz przyspieszonemu – wywołanemu adriamycyną, związkiem indukującym uszkodzenia DNA – bez wzrostu aktywności SA-β-Gal; obniżenie poziomu β-galaktozydazy technikami siRNA lub shRNA w komórkach prawidłowych i nowotworowych nie hamuje indukcji starzenia (s. 139).
  - **Cytoszkielet.** 5. *(nowe, A26)* Wimentyna ma masę 58 kDa i wykazuje dużą homologię międzygatunkową (s. 140). 6. *(z cz. 1, O23 + nowe; A27)* Dane z linii fibroblastów: w embrionalnych fibroblastach linii TIG3 poziom wimentyny rósł wraz z liczbą podziałów; ludzkie fibroblasty skórne linii TIG101, które uległy starzeniu, miały ponad dwukrotnie więcej wimentyny niż komórki TIG3 na wczesnym pasażu; płodowe fibroblasty skórne linii TIG3S miały jej istotnie mniej niż TIG101. Komórki, które uległy starzeniu, miały czterokrotnie niższy poziom aktyny i dwukrotnie niższy poziom tubuliny niż komórki młode (s. 140).
  - **Cykl – tło.** 7. *(z cz. 1, O24 + nowe; A34)* Kompleksy dominujące w fazach: G1 – cyklina D–CDK4/CDK6 i cyklina E–CDK2; S – cyklina A–CDK2; G2 – cyklina A–CDK1 (s. 140); schemat artykułu (ryc. 2) pokazuje też fazę M – cyklina B–CDK1. Odsyłacz: `chapref #c02`. 8. *(nowe, A05)* Pełne symbole inhibitorów: klasa INK4/ARF – p15<sup>INK4B</sup>, p16<sup>INK4A</sup>, p18<sup>INK4C</sup>, p19<sup>INK4D</sup>; klasa CIP/KIP – p21<sup>CIP1</sup> (p21<sup>WAF1/CIP1</sup>), p27<sup>KIP1</sup>, p57<sup>KIP2</sup> (s. 138, 140).
  - **p16 – dopowiedzenia.** 9. *(z cz. 1, O26; A41)* Pełna lista nowotworów, w których brak p16: glejak wielopostaciowy, czerniak, gruczolakorak trzustki, niedrobnokomórkowy rak płuc, rak pęcherza, rak ustnej części gardła (s. 141). 10. *(nowe, A40)* Autorzy odnotowują też dane, według których sam wzrost poziomu p16 jest wystarczającym dowodem starzenia komórkowego (s. 141).
  - **Pozostałe inhibitory i cyklina D1** *(z cz. 1, O27 + nowe)* – tabela:

  | Białko (klasa) | Co zaobserwowano | W jakich komórkach / tkankach | s. |
  |---|---|---|---|
  | p15 (INK4/ARF) | starzeniu towarzyszy wzrost poziomu; wyższy poziom w zmianach łagodnych niż w nowotworach złośliwych; korelacja ze wzrostem aktywności SA-β-Gal i obecnością SAHF | skóra, płuca, trzustka | 141 |
  | p19<sup>Ink4d</sup> (INK4/ARF) | poziom rośnie z wiekiem, ale słabiej niż p16<sup>Ink4a</sup> | gryzonie | 141 |
  | p19<sup>Arf</sup> (u ludzi odpowiednik: p14<sup>ARF</sup>) | jego wzrost towarzyszy wzrostowi p16<sup>Ink4a</sup> | gryzonie | 141 |
  | p57 (CIP/KIP) | nadprodukcja → zatrzymanie w fazie G1, wzrost aktywności SA-β-Gal, komórki duże i płaskie | komórki raka prostaty linii PPC-1; to samo po wprowadzeniu p57 do trzech linii glejaka (U343 MG-A, U87 MG, U343 MG) | 141 |
  | p57 | poziom rośnie wraz z liczbą podziałów | linia HUC (*human uroepithelial cells*) | 141 |
  | p27 i p21 (CIP/KIP) | nadprodukcja indukuje starzenie | ludzkie komórki kostniakomięsaka linii U2OS | 141 |
  | cyklina D1 | znacznik starzenia; wzrost poziomu | nowotworowe komórki nabłonkowe (epitelialne); wzrost także w komórkach mięśni gładkich | 141 |

  11. *(nowe, A50)* Zatrzymanie w fazie G2 w starzeniu replikacyjnym opisano w pracy Mao i wsp. (s. 141).
- **Wskazówka tłumaczenia.** Problem: część 1 podaje uogólnienia („p57 odgrywa rolę w starzeniu”, „aktyny jest mniej”) – tu widać, z jakich doświadczeń pochodzą i jak wąskie bywają (jedna linia komórkowa, jeden gatunek). (a) Wyjaśnić na początku dwa słowa: *linia komórkowa* (komórki jednego pochodzenia utrzymywane w hodowli, oznaczane symbolem) i *nadprodukcja / wprowadzenie białka* jako typ doświadczenia: „dodajemy białko i patrzymy, czy pojawią się znaczniki” – w tabeli p57 pojawiają się dokładnie te znaczniki, które student zna z części 1 (kształt, SA-β-Gal, zatrzymanie w G1), i to jest dobry moment na krok samodzielnego rozumowania. (b) SA-β-Gal: zestawić dwa dowody (naturalny brak enzymu w GM1 i doświadczalne wyciszenie; siRNA – `chapref #c04`, jeśli termin jest tam objaśniony) z wnioskiem części 1: znacznik jest skutkiem (więcej lizosomów), nie przyczyną. (c) p15: ten sam układ „zmiany łagodne tak, złośliwe nie” co dla DEC1 i DCR2 w części 1 – zestawić. (d) Pkt 10 przedstawić uczciwie jako rozbieżność danych, której artykuł nie rozstrzyga: obok niego stoi fakt, że p16 rośnie też w gruczole mlekowym, i wniosek końcowy autorów (kilka znaczników). Nie rozstrzygać. (e) Cyklina D1: zaznaczyć, że to cyklina, a nie inhibitor („znacznikami są nie tylko inhibitory, ale i cykliny”) – bez wyjaśniania dlaczego.
- **Nie dopowiadać:** pochodzenia i charakterystyki linii komórkowych ponad to, co w nawiasach; mechanizmu, w jaki cyklina D1 rośnie w komórkach zatrzymanych; co to adriamycyna ponad „związek indukujący uszkodzenia DNA”; różnic RAS/BRAF.
- **Tabela:** tak (inhibitory). · **Źródło:** `Alster s. 138–141`.

### R9 · `c03-r-chromatyna` · „Znaczniki starzenia: DNA, chromatyna i SASP – szczegóły”
- **Łączy się z:** `c03-starzenie` (h3 „DNA i chromatyna”, „Fenotyp sekrecyjny (SASP)”).
- **Treść:**
  - **DNA-SCARS.** 1. *(nowe, A53)* Zmiana poglądu ma datę: do niedawna uważano, że starzenie przyspieszone mogą indukować uszkodzenia w telomerowym i nietelomerowym DNA; w 2012 r. kilka zespołów badawczych pokazało, że trwała aktywacja szlaku DDR jest wynikiem uszkodzeń w odcinkach telomerowych (s. 141).
  - **Jak powstają SAHF.** 2. *(nowe, A57)* SAHF opisali po raz pierwszy w 2003 r. Narita i wsp., w ludzkich fibroblastach (s. 142). 3. *(z cz. 1, O30; A59)* Kolejność zdarzeń według źródła: zanim SAHF powstaną, białka HIRA i HP1 przemieszczają się do ciałek PML-NB (w początkowym etapie biorą udział ASF1a, HIRA i PML). **Etap pierwszy** – kondensacja chromosomów; odpowiadają za nią dwa białka opiekuńcze histonów, HIRA i ASF1a; widać ją po barwieniu DAPI, zanim skupiska wzbogacą się w HP1, makroH2A i H3K9me. **Kolejny krok** – metylacja histonu H3 na lizynie 9. **Następnie** powstaje miejsce wiązania białka HP1 i wbudowuje się histon makroH2A (s. 142). 4. *(nowe, A61)* Doświadczenia: nadprodukcja HIRA lub ASF1a w komórkach pierwotnych przyspiesza tworzenie SAHF; wyciszenie ASF1a hamuje tworzenie SAHF w starzeniu indukowanym nadekspresją onkogenu RAS (s. 142). 5. *(z cz. 1, O30; A60)* W komórkach pozbawionych kinaz ATM lub ATR – kluczowych w szlaku odpowiedzi na uszkodzenia DNA – SAHF nie powstają (s. 142). 6. *(nowe, A58)* Rodziny składników: histon makroH2A – makroH2A1.1, 1.2 i 2; białka HP1 – HP1α, β i γ; białka HMGA – HMGA1 i 2 (s. 142). 7. *(nowe, A63)* Zależność od typu komórek: w starzeniu replikacyjnym ludzkich fibroblastów linii IMR90 i WI38 SAHF powstają, w linii BJ – nie; gdy jednak starzenie komórek BJ wywołano nadekspresją onkogenów, SAHF się pojawiały (s. 142). 8. *(nowe, A64)* Budowa SAHF: początkowo nie umiano rozróżnić modyfikacji H3K9me3, H3K9me2, H3K9me i H3K27me, bo wokół modyfikowanej lizyny leżą identyczne aminokwasy; pomogły bardziej specyficzne przeciwciała. SAHF mają budowę warstwową: rdzeń bogaty w H3K9me3 otacza pierścień, w którym dominuje H3K27me3. Podczas tworzenia SAHF rośnie poziom HP1, które wiąże się z H3K9me3, ale poziom samego H3K9me3 znacznie nie rośnie. Pozbawienie ludzkich fibroblastów H3K9me3 lub H3K27me3 nie uniemożliwia powstawania SAHF; nie uniemożliwia go też obniżenie poziomu białek HP1 (s. 142).
  - **Białko PML.** 9. *(nowe, A66)* PML opisano po raz pierwszy u osób z ostrą białaczką promielocytarną (stąd nazwa). Ciałka PML-NB nazywa się też ND10 i POD. Wśród ponad 50 białek PML-NB są także helikazy i topoizomerazy (s. 142). 10. *(nowe, A68)* Nadekspresja onkogenu RAS indukuje starzenie, któremu towarzyszy więcej PML-NB niż w komórkach kontrolnych; w tym starzeniu w obrębie PML-NB stwierdzono białka Rb i p53. W fibroblastach linii IMR90 starzeniu replikacyjnemu towarzyszył wzrost poziomu białka PML (s. 142).
  - **Telomery i lamina B1.** 11. *(z cz. 1, O32; A72)* Sześć szelteryn: TRF1, TRF2, POT1, TIN2, TPP1 i Rap1 (rozwinięcia – R10) (s. 142). 12. *(z cz. 1, O33 + nowe; A76, A77)* Spadek poziomu laminy B1 nie zależał od białek p38 i ATM ani od czynnika transkrypcyjnego NF-κB. Starzeniu może towarzyszyć wzrost poziomu reaktywnych form tlenu, ale obniżenie ich poziomu nie hamowało spadku laminy B1 (s. 143).
  - **Uszkodzenia oksydacyjne i metylacja.** 13. *(nowe, A80)* Wolnorodnikową teorię starzenia sformułował Denham Harman w 1956 r.; według niej wolne rodniki odgrywają krytyczną rolę w starzeniu organizmu (s. 143). 14. *(nowe, A81)* U ludzi poziom 8-oksydG był wyższy w dwóch grupach o średniej wieku 67 i 50 lat niż u osób w wieku ok. 31 lat; wykazano dodatnią korelację między poziomem 8-oksydG a wiekiem (badano leukocyty i mocz) (s. 143). 15. *(nowe, A84)* Transformacja komórek wirusem SV-40 powoduje, że poziom 5-metylocytozyny utrzymuje się na stałym poziomie – nie spada z kolejnymi pasażami (s. 143).
  - **SASP – co nim steruje.** 16. *(z cz. 1, O34; A87, A88)* Aktywność SASP regulują niektóre białka szlaku odpowiedzi na uszkodzenia DNA – ATM, NBS1 i CHK2 – oraz czynniki transkrypcyjne NF-κB i C/EBP-β. Istotną rolę pełni kinaza p38MAPK, która pojawia się pod wpływem nadekspresji onkogenu RAS i promieniowania X: indukuje SASP przez aktywację NF-κB. Inaktywacja białka p53 zwiększa wydzielanie niektórych elementów SASP (s. 143). 17. *(nowe, A89)* Zastosowanie inhibitora kinazy p38MAPK zmniejszało wydzielanie większości elementów SASP (s. 143).
- **Wskazówka tłumaczenia.** (a) SAHF: problem – część 1 mówi „powstają etapami”; tu etapy w kolejności źródła (uwaga: źródło nazywa kondensację „pierwszym etapem”, a przemieszczenie HIRA i HP1 do PML-NB umieszcza „przed powstaniem SAHF” – nie numerować przemieszczenia jako etapu 1, jak w obecnej liście). Każdemu białku przypisać czynność (HIRA i ASF1a kondensują; metylacja H3K9 tworzy miejsce dla HP1; makroH2A się wbudowuje). Doświadczenia z pkt 4 pokazać jako test „więcej białka → szybciej, brak białka → wcale”. Zapis H3K9me3 objaśnić raz: histon H3, lizyna (K) w pozycji 9, „me” = grupa metylowa (cyfra – liczba grup; to objaśnienie zapisu, nie nowy fakt). (b) Paradoks z pkt 8: po H3K9me i HP1 rozpoznaje się SAHF (część 1), a jednak ich usunięcie nie blokuje powstawania skupisk – zestawić z SA-β-Gal: znacznik nie musi być tym, co proces napędza. (c) Lamina B1: co mówi lista „nie zależy od”? Spadek wymaga jednego z dwóch głównych szlaków starzenia (część 1), a nie zależy od kinazy ATM (szlak DDR), od regulatorów SASP (p38, NF-κB – ten sam artykuł) ani od poziomu ROS. (d) SASP: wszystkie drogi schodzą się na NF-κB – białka DDR, p38MAPK → NF-κB, a w części 1: IL-1α → IL1R → NF-κB → IL-6, IL-8. Ułożyć jako krótką listę „co włącza NF-κB”. Zdanie o p53 podać jako fakt (zaskakujący, bo szlak p53–p21 prowadzi do starzenia) – bez wyjaśniania. (e) Pkt 1, 2, 13: daty wpleść w zdania, nie robić z nich osobnej listy.
- **Nie dopowiadać:** dlaczego SAHF leżą przy promotorach genów fazy S („wyciszają geny podziału” – źródło tego nie pisze); czym różnią się warianty makroH2A/HP1/HMGA; roli helikaz i topoizomeraz; dlaczego komórki po SV-40 utrzymują 5-mC („bo się nie starzeją” – nie ma w źródle); jak inaktywacja p53 zwiększa SASP.
- **Tabela:** nie (ewentualnie mała lista regulatorów SASP). · **Źródło:** `Alster s. 141–144`.

### R10 · `c03-r-skroty` · „Skróty z tego rozdziału – pełne nazwy”
- **Łączy się z:** cały rozdział (nawiązanie jednym zdaniem; bez `pageref` do konkretnej sekcji albo z odsyłaczem do `c03-szlaki` i `c03-starzenie`).
- **Treść** *(nowe: D62, D82, A72, A87 i rozwinięcia rozproszone po źródłach; skróty rozwinięte już w części 1 można pominąć)* – dwie tabele „Skrót / Pełna nazwa (ang.) / Czym jest”:

  **Apoptoza (Drewa s. 165–172):** PCD – *Programmed Cell Death* · Bcl-2 – *B-cell CLL/lymphoma 2* · BH – *Bcl-2 homology domain* · TM – *Transmembrane Domain* · Apaf-2 – *Apoptosis protease activating factor-2* (= cytochrom c) · ICE – *Interleukin Converting Enzyme* · ICAD – *Inhibitor of Caspase-Activated DNase* · DD – *Death Domain* · DED – *Death Effector Domain* · CARD – *Caspase Recruitment Domain* · TNF – *Tumor Necrosis Factor* · TNFR1, TNFR2 – *Tumor Necrosis Factor Receptor 1, 2* · TRAIL-R1, -R2 – *TNF-Related Apoptosis-Inducing Ligand-R1, R2* · FADD – *Fas-Associated Death Domain* · DISC – *Death Inducing Signaling Complex* · DAXX – *Death Adapter Protein/Death-Associated Protein* · JNK – *Jun-N-terminal Kinase* · ERK – *Extracellular Signal-regulated Kinase* · tBid – *truncated Bid* · VDAC – *Voltage Dependent Anion Channel* · ROS – *Reactive Oxygen Species* · PTP – *Permeability Transition Pore* · ANT – *Adenine Nucleotide Translocator* · BPR – *Peripheral Benzodiazepine Receptor* · AIF – *Apoptosis-Inducing Factor* · Smac/DIABLO – *Second mitochondrial activator of caspase/Direct IAP Binding protein with Low pI* · WD-40 – domena wielokrotnych powtórzeń WD (*WD-40 repeats*) · CAPK – *Ceramide-Activated Protein Kinases* · MAPK – *Mitogen-Activated Protein Kinases* · CAPP – *Ceramide-Activated Protein Phosphatase* · SAPK – *Stress Associated Protein Kinase* · GrB, GrA – granzym B (fragmentyna-2), granzym A (fragmentyna-1) · CK, GPX – kinaza kreatynowa, peroksydaza glutationowa (oznaczenia z ryc. 8.5).

  **Starzenie (Alster s. 138–144):** SA-β-Gal – *senescence associated β-galactosidase* · CDK – *cyclin-dependent kinases* · CKI – *cyclin-dependent kinase inhibitors* · INK4/ARF – *Inhibitor of kinase 4/alternative reading frame* · CIP/KIP – *CDK interacting protein/kinase inhibitory protein* · DDR – *DNA Damage Response* · DNA-SCARS – *DNA segments with chromatin alterations reinforcing senescence* · TIF – *telomere dysfunction-induced foci* · SAHF – *senescence associated heterochromatin foci* · HP1 – *heterochromatin protein-1* · HMGA – *High Mobility Group A* · PML – *promyelocytic leukemia protein* · PML-NB – *PML nuclear bodies* (inaczej ND10 – *nuclear bodies*, POD – *promyelocytic oncogenic domains*) · TRF1, TRF2 – *telomeric repeat binding factor 1, 2* · POT1 – *protection of telomeres 1* · TIN2 – *TRF1-interacting nuclear protein 2* · Rap1 – *repressor-activator protein 1* · FISH – *fluorescence in situ hybridization* · SASP – *senescence associated secretory phenotype* · SMS – *senescence-messaging secretome* · ATM – *Ataxia telangiectasia mutated* · NBS1 – *Nijmegen breakage syndrome protein-1* · CHK2 – *checkpoint kinase 2* · NF-κB – *nuclear factor kappa-light-chain-enhancer of activated B cells* · C/EBP-β – *CCAAT-enhancer-binding proteins* · DEC1 – *differentiated embryo-chondrocyte expressed-1* · DCR2 – *decoy death receptor-2* · HUC – *human uroepithelial cells*.
- **Wskazówka.** Tabela użytkowa; trzecia kolumna („czym jest”) – 2–5 słów wyłącznie z części 1 lub R1–R9 (np. FADD – „białko adaptorowe szlaku zewnętrznego”). Nie tłumaczyć nazw angielskich słowo po słowie, jeśli źródło nie podaje polskiego odpowiednika (polskie odpowiedniki ze źródła: ERK – kinaza odpowiedzi zewnątrzkomórkowej; BPR – obwodowy receptor benzodiazepiny; AIF – czynnik indukcji apoptozy; ANT – translokator nukleotydów adeninowych; CAPK/CAPP – aktywowane przez ceramid; MAPK – zależne od mitogenów; SAPK – związane ze stresem). TPP1 – źródło nie rozwija. Jeśli zabraknie miejsca: pominąć skróty rozwinięte w części 1.
- **Tabela:** tak – dwie. · **Źródło:** `Drewa s. 165–172 · Alster s. 138–144`.

---

## 5. Przejście (po „W 60 sekund”, przed częścią 2)

**Proponowany tekst:**
„Część 1 zawiera to, co trzeba rozumieć: czym jest apoptoza, kto ją przeprowadza, jakimi szlakami biegnie sygnał, co się dzieje, gdy jest jej za dużo albo za mało, i po czym poznać komórkę starą. Część 2 jest dla tych, którzy chcą znać źródła w całości – „na piątkę”. Nie wprowadza nowych tematów: dopowiada szczegóły do podrozdziałów, które już znasz – pełne listy białek, budowę kaspaz, pośredników szlaków, leki i sposoby oznaczania znaczników starzenia. Każda sekcja zaczyna się od odsyłacza do miejsca w części 1, które rozszerza.”

**Lista sekcji części 2** (z `pageref`):
1. Skąd to wiemy? Nazwa, odkrycia i nicień *C. elegans* (`c03-r-historia`)
2. Kaspazy – szczegóły budowy i siedem kaspaz w tabeli (`c03-r-kaspazy`)
3. Rodzina Bcl-2 – pełna lista i domeny każdego białka (`c03-r-bcl2`)
4. Szlak zewnętrzny i wewnętrzny – pozostałe receptory, droga przez DAXX, skład megakanału (`c03-r-szlaki`)
5. Szlak pseudoreceptorowy i ceramidowy – szczegóły (`c03-r-dodatkowe`)
6. Zaburzenia apoptozy – cała tabela chorób i leki nasilające apoptozę (`c03-r-zaburzenia`)
7. Jak oznacza się znaczniki starzenia (`c03-r-metody`)
8. Znaczniki starzenia: morfologia, lizosomy i cykl – doświadczenia i liczby (`c03-r-cykl`)
9. Znaczniki starzenia: DNA, chromatyna i SASP – szczegóły (`c03-r-chromatyna`)
10. Skróty z tego rozdziału – pełne nazwy (`c03-r-skroty`)

Do `c03-fizjologia` część 2 nie ma osobnej sekcji: fragment Jóźwiaka o fizjologii jest w części 1 w całości (jedyny dodatek – przykład z ryc. 11.7 – stoi w R6).

---

## 6. Czerwona ramka „stare źródło”

**Nie dotyczy.** Rozdział opiera się na: Drewa, Ferenc 2011 (r. 8), Jóźwiak 2020 (r. 11), Alster, Korwek 2014 (*Postępy Biochemii* 60: 138–146) – lata sprawdzone w nagłówkach plików paczki `zrodla/z03/`. Żadnego Jordego ani Twymana. Ramki nie wstawiać.

---

## 7. Wierność obecnego tekstu

**Błędy klasy A (fakt spoza źródeł, sprzeczność, wzmocnione twierdzenie): nie znalazłem.** Sprawdzone ponownie na źródle i skanach: wszystkie liczby (95%, 26 genów, 14 kaspaz, numery kaspaz i domeny z tab. 8.2, 100×, 30–50 SAHF, > 50 białek, 6 szelteryn, krotności dla wimentyny/aktyny/tubuliny), tab. 11.4 (nagłówki kolumn potwierdzone na skanie s. 127), kroki pięciu szlaków, etapy SAHF, lista leków.

**Drobne nieścisłości (B) – poprawić przy okazji:**
| Nr | Miejsce | Jest | Ma być | Źródło |
|---|---|---|---|---|
| B1 | `apo`, „Równolegle zmienia się błona…” | „Równolegle…”; „błona traci asymetrię” | „Zmienia się też…”; „asymetria błony zostaje zaburzona” (źródło nie podaje kolejności w czasie i mówi o „zaburzeniu”, nie o utracie) – O3 | Drewa s. 165 |
| B2 | `sta`, h4 „Komórka duża i płaska” | „Tę zmianę widać w mikroskopie.” | usunąć – artykuł nie podaje metody oceny morfologii – O20 | Alster s. 138–139 |
| B3 | `sta`, h4 „Zmiany cytoszkieletu” + tabela metod | metody („immunocytochemicznie albo Western blotting”) przypisane wimentynie, aktynie i tubulinie | źródło podaje je tylko dla wimentyny – w R7 wiersz „wimentyna” | Alster s. 140 |
| B4 | `sta`, h4 PML | „w nowotworzeniu – maleją” (liczba i wielkość) | „w nowotworzeniu ich liczba maleje” – O31 | Alster s. 142 |
| B5 | `sta`, h4 SAHF, lista etapów | przemieszczenie HIRA i HP1 do PML-NB jako „etap 1”, kondensacja jako „etap 2” | źródło: przemieszczenie „przed powstaniem SAHF”, kondensacja = „pierwszy etap” – uwzględnione w R9 | Alster s. 142 |

**Sformułowania autora (C) – dopuszczalne, ewentualnie złagodzić:**
- C1. `bcl`: „Nazwa wskazuje na nowotwory z limfocytów B.” – objaśnienie rozwinięcia skrótu; źródło nie rozwija „CLL”. Proponowane brzmienie w O36.
- C2. `apo`: „Przebieg apoptozy zależy przede wszystkim od dwóch grup białek.” – zdanie-pomost; źródło mówi o „roli” kaspaz i białek Bcl-2. Można zostawić albo: „W przebiegu apoptozy główne role odgrywają dwie grupy białek.”
- C3. `bcl`: „o losie komórki decyduje przewaga jednej z grup” – wniosek autora (w Drewie 8.1.1 nie ma „stosunku Bax/Bcl-2”); poprzedni recenzent uznał za dopuszczalny, podtrzymuję. Wspiera go ryc. 8.5 (Bax „+”, Bcl-2 „–”). Terminu „stosunek Bax/Bcl-2” nie wprowadzać także w części 2.
- C4. `sta`, PML: „Ten znacznik pomaga odróżnić starzenie od innych przyczyn zatrzymania cyklu.” – wniosek z faktu A69; zostaje (potrzebny do Przykładu).
- C5. `bcl`, „Kto wygrywa?”: p53 „nasila syntezę Bax i obniża poziom Bcl-2” – fakt z Drewy s. 148 (r. 7), czyli spoza paczki Z03, ale podany jako przypomnienie z rozdz. 2 (jest tam w `c02-p53`) z `chapref`. Dopuszczalne; linii „Źródło” nie uzupełniać.

**Wątpliwości autora (`stan/z03-v2.md`, `stan/z03.md`) – rozstrzygnięcia:**
- „Kaspazy wykonawcze nie mają domen CARD ani DED” (odczyt z tab. 8.2: struktura „p20 + p10”) – **zostaje**. Nie pisać natomiast, że nie mają prodomeny (kaspaza 7 ją ma – s. 172); wyjaśnione w R2.
- „Nazwa wskazuje na nowotwory z limfocytów B” – zob. C1.
- „Stosunek Bax/Bcl-2” – zob. C3. „Fragmentacja DNA” – w Drewie 8.1 jest tylko fragmentacja jądra; cięcie DNA jedynie pośrednio (ICAD/CAD, DNaza przy granzymie A) – **nie dopisywać** także w części 2 (drabinka DNA to Jóźwiak s. 123, poza zakresem). Inhibitory kaspaz – brak w źródle (IAP występuje tylko w nazwie Smac/DIABLO) – **nie dopisywać**.
- Tab. 11.4 – nagłówki kolumn potwierdzone na skanie po raz drugi.

**Linie „Źródło: …”** – wszystkie wskazują strony z mapy (Drewa 165–174, Jóźwiak 126–127, Alster 138–144); żadna nie wychodzi poza rozpiskę. `kas`: „Alster s. 143” dotyczy objaśnienia „laminy – składnik błony jądrowej” – poprawnie.

**Usterki samych źródeł** (bez ramki „Uwaga do źródła” – nic nie zmieniają merytorycznie): Drewa s. 165 „Horovitza” (pisać Horvitza); Drewa s. 172 „wpływ cytochromu c” (ma być „wypływ” – tak jest w tekście); Alster s. 139 „gangliozydazą GM1” (gangliozydoza – tak jest w tekście); Alster s. 142 „heterochromatyna uległa starzeniu w postaci 30–50 skupisk” (sens: tworzy skupiska); Alster s. 143 zapis „8-oxoGua” obok „8-oksyGua” (ta sama cząsteczka); Alster s. 144 „embro-chondrocyte”.

---

## 8. Miejsce ryciny z ChatGPT

Karta: `RYCINY_do_ChatGPT.md`, rycina 3 – `c03-fig-kompleksy`, „DISC i apoptosom – która domena łączy się z którą”, 2 łamy, 20:9.
**Akapit-kotwica zostaje w części 1 bez zmian:** `c03-szlaki`, h3 „Szlak wewnętrzny: sygnał powstaje w komórce”, akapit „Porównaj oba szlaki. W każdym białko adaptorowe…” – zaślepkę wstawić bezpośrednio po nim (przed h3 „Gdzie szlaki się łączą? Białko Bid”).
Wszystkie treści, z których rycina korzysta, też zostają w części 1 nietknięte: trzy domeny receptora, kroki 1–5 szlaku Fas, zasada „DD z DD, DED z DED”, krok „Apoptosom” (CARD i WD-40 białka Apaf-1, dATP/ATP), tabela kaspaz (dwie DED w kaspazach 8 i 10, CARD w kaspazie 9). Operacje O8–O11 ich nie dotykają. Proponowany podpis z karty pozostaje prawdziwy.

---

## 9. Decyzje do zatwierdzenia przez zleceniodawcę

- **Z1. Informacje odczytane wyłącznie z rycin źródeł.** Plan włącza je do części 2 jako opis schematu: (a) ryc. 11.8 Jóźwiaka – drogi Ras–Raf–Mek–Erk i PI3K–Akt, Bim, Bax oraz szósty lek, idelalizyb, którego nie ma ani w tekście, ani w podpisie (R6 pkt 4); (b) ryc. 8.5 Drewy – rozmieszczenie składników megakanału (R4 pkt 3, kolumna „Gdzie”); (c) ryc. 8.6 Drewy – endosom (R5 pkt 2); (d) ryc. 2 Alster–Korwek – cyklina B–CDK1 w fazie M (R8 pkt 7). Jeśli „komplet źródła” ma oznaczać tylko tekst i podpisy – usunąć te cztery pozycje (reszta planu się nie zmienia).
- **Z2. „Poza zakresem” – bez zmian, nic nie proponuję włączać.** Zagadnienia 1–4 rozpiski brzmią jak nagłówki Drewy 8.1–8.2.5, zagadnienia 5–6 jak nagłówki Jóźwiaka; Drewa 8.3–8.4 (fizjologia i patologia) oraz Jóźwiak: nekroza, „Szlaki apoptozy”, „Faza efektorowa”, „Immunologia” nie odpowiadają żadnemu sformułowaniu z rozpiski. Informacyjnie: w wyłączonych fragmentach są fakty bliskie zagadnieniu 1 (Jóźwiak s. 123–124: drabinka DNA, fosfatydyloseryna jako sygnał dla makrofagów; tab. 11.1 apoptoza–nekroza) – zostają poza podręcznikiem.
- **Z3. Sekcja R10 (tabele skrótów)** jest nowym elementem użytkowym, którego handoff wprost nie przewiduje; mieści rozwinięcia nazw obecne w źródłach. Można z niej zrezygnować – wtedy z „kompletu” wypadają angielskie rozwinięcia ok. 60 skrótów (w inwentarzu: D62 oraz części wierszy D54, D65, D68, D82, A72, A87, A92).

## Decyzje szefa (18.11, ok. 21:00) – obowiązują wykonawcę
- **Z1 – TAK:** informacje widoczne tylko na rycinach źródła (drogi sygnałowe i idelalizyb z ryc. 11.8 Jóźwiaka, rozmieszczenie składników megakanału, endosom, cyklina B–CDK1) wchodzą do części 2 jako opis słowny (bez rysowania rycin) – zleceniodawca chce kompletu informacji ze źródeł.
- **Z3 – TAK, krótko:** sekcja R10 (skróty) zostaje jako zwięzła tabela użytkowa na końcu części 2.
- Pozostałe pozycje planu bez zmian.
