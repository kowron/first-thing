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

Kolumna „Stan”: **jest** (gdzie) / **brak** (treść do dopisania stoi w kolumnie „Jednostka” – pełnym zdaniem, wiernie wobec źródła) / **jest → O…** (przenieś lub uprość operacją z pkt 3). Dla P2 podaję sekcję docelową R….

### 2.1. Drewa – wstęp rozdziału 8 (s. 165)

| ID | Jednostka informacji | s. | n | Dec. | Stan |
|---|---|---|---|---|---|
| D01 | Termin „apoptoza” pochodzi od greckiego *apoptosis* – opadanie płatków kwiatowych lub liści z drzew. | 165 | 1 | P1 | jest: `apo`, „Ten proces to apoptoza.” |
| D02 | Termin wprowadzili w 1972 r. J.F. Kerr, A.H. Wyllie i A.R. Currie. | 165 | 1 | P2 | brak → R1 |
| D03 | Apoptoza to zespół zmian morfologicznych i biochemicznych prowadzących do kontrolowanej śmierci komórki z pominięciem procesu zapalnego. | 165 | 1 | P1 | jest: tamże + Pojęcie „Apoptoza” |
| D04 | Jest stanem fizjologicznym; wymaga ekspresji wielu genów oraz nakładu energii. | 165 | 2 | P1 | jest: `apo`, „„Kontrolowana” znaczy tu…” |
| D05 | Genetyczne podstawy apoptozy oraz udział ekspresji genów w jej regulacji poznano najpierw u nicienia *Caenorhabditis elegans*. | 165 | 1 | P2 | jest (tamże, ostatnie zdanie) → O1 → R1 |
| D06 | Badania R. Horvitza, S. Brennera i J. Sulstona uhonorowano w 2002 r. Nagrodą Nobla. (W źródle zapis „Horovitza” – literówka; pisać „Horvitza”.) | 165 | 1 | P2 | jest częśc. („Nagroda Nobla 2002”), nazwiska – brak → R1 |
| D07 | Apoptozę nazywa się też programowaną lub samobójczą śmiercią komórki (PCD – *Programmed Cell Death*); terminy często stosuje się zamiennie. | 165 | 1 | P1 | jest: `apo`, „Apoptozę nazywa się też…” |
| D08 | Pierwotnie określenie „programowana śmierć komórki” stosowano tylko do śmierci zachodzącej w procesach fizjologicznych, które warunkują prawidłowe funkcjonowanie organizmu – na etapie embrionalnym i w późniejszym okresie. | 165 | 1 | P2 | jest (tamże) → O2 → R1 |
| D09 | Obecnie „apoptoza” opisuje zmiany w umierającej komórce niezależnie od tego, czy śmierć zachodzi podczas rozwoju organizmu, czy jest indukowana przez czynniki zewnętrzne. | 165 | 1 | P1 | jest (tamże; po O2 zostaje) |

### 2.2. Drewa 8.1 Apoptoza (s. 165–166)

| ID | Jednostka informacji | s. | n | Dec. | Stan |
|---|---|---|---|---|---|
| D10 | Dotyczy przeważnie pojedynczych komórek; trwa od kilku do kilkunastu godzin. | 165 | 2 | P1 | jest: `apo`, „Apoptozę nazywa się też…” (koniec) |
| D11 | Komórka traci wodę i w konsekwencji się obkurcza. | 165 | 1 | P1 | jest: `apo`, „Zacznij od komórki prawidłowej…” |
| D12 | Fosfatydyloseryna przemieszcza się z wewnętrznej do zewnętrznej warstwy błony komórkowej → zaburzenie asymetrii błony. | 165 | 1 | P1 | jest: `apo`, „Równolegle zmienia się błona…” (poprawka O3) |
| D13 | Etapy: (1) pierwszy objaw morfologiczny – zmiany w jądrze; (2) kondensacja chromatyny i jej ułożenie pod otoczką jądrową (marginalizacja); (3) obkurczenie jądra i jego fragmentacja; (4) kondensacja cytoplazmy, na powierzchni charakterystyczne pęcherzyki; (5) rozpad komórki na fragmenty otoczone błoną – ciałka apoptotyczne (resztki chromatyny i cytoplazmy, niezmienione organella). | 165 | 5 | P1 | jest: `apo`, lista `ol` 1–3 |
| D14 | Ciałka apoptotyczne fagocytują sąsiadujące komórki lub makrofagi. | 165 | 1 | P1 | jest: `apo`, lista, pkt 4 |
| D15 | Ryc. 8.2 (ryc.): kolejność zmian; „ciągłość błony komórkowej” zachowana. | 166 | 1 | P1 | jest: ryc. `c03-fig-zmiany` + lista, pkt 3 |
| – | Ryc. 8.1 (elektronogram komórki w apoptozie). | 166 | – | balast | zdjęcie, którego nie mamy – pomijamy |

### 2.3. Drewa 8.1.1 Rodzina białek Bcl-2 (s. 166–167)

| ID | Jednostka informacji | s. | n | Dec. | Stan |
|---|---|---|---|---|---|
| D17 | Rodzina Bcl-2 (*B-cell CLL/lymphoma 2*) – duża, heterogenna grupa białek regulujących apoptozę. | 166 | 1 | P1 | jest: `bcl`, „Rodzina Bcl-2 (ang.…” |
| D18 | Gen *bcl-2* zidentyfikowano po raz pierwszy w 1986 r. – jako onkogen aktywowany przez translokację t(14;18). | 166 | 1 | P2 | rok – brak → R1 |
| D19 | Onkogen aktywowany przez t(14;18); translokacja obecna w 95% przypadków nieziarniczych chłoniaków grudkowych. | 166 | 2 | P1 | jest: tamże (potrzebne do Przykładu w `zab`) |
| D20 | Antyapoptotyczne działanie białka Bcl-2 poznano dzięki temu, że budową i funkcją jest homologiczne do białka Ced-9 *C. elegans*. | 166 | 1 | P2 | jest: `bcl`, „Antyapoptotyczne działanie Bcl-2 poznano…” → O6 → R1 |
| D21 | U ludzi zidentyfikowano 26 genów rodziny BCL-2; kilka z nich przez alternatywny splicing mRNA daje dwa lub więcej białek o przeciwstawnym działaniu (np. Bcl-X<sub>L</sub> i Bcl-X<sub>S</sub>). | 166 | 2 | P1 | jest: tamże (po O6 początek akapitu) |
| – | Adres bazy (apoptosis-db.org), z której pochodzi liczba 26. | 166 | – | balast | odesłanie; opcjonalnie pół zdania w R3 |
| D23 | Dwie grupy: proapoptotyczne – ich nadekspresja prowadzi do śmierci komórki; antyapoptotyczne – zwiększają prawdopodobieństwo przeżycia. | 166–167 | 2 | P1 | jest: `bcl`, „Białka rodziny dzieli się na dwie grupy…” + tabela |
| D24 | Przedstawiciele z tekstu. Pro: Bax, Bak, Bok/Mtd, Bad, Bid, Bim, Bik, Hrk, Bcl-X<sub>S</sub>. Anty: Bcl-2, Bcl-X<sub>L</sub>, Mcl-1, Bfl-1/A1, Bcl-W, Bcl-B/Boo/Diva. | 166–167 | 2 | P1u | jest (tabela, wiersz 1) → O7. **Cz. 1:** Bax, Bak, Bad, Bid, Bim, Bcl-X<sub>S</sub> / Bcl-2, Bcl-X<sub>L</sub>, Mcl-1, Bcl-W (te są na ryc. `c03-fig-bcl2`). **Cz. 2 (R3):** Bok/Mtd, Bik, Hrk / Bfl-1/A1, Bcl-B/Boo/Diva |
| D25 | Tab. 8.1 (ryc.) wymienia jeszcze siedem białek proapoptotycznych: APR/Noxa, PUMA, p193, Bcl-Gs, Bcl-rambo/Mil, Nip3, Nix/BNIP. | 166 | 1 | P2 | PUMA i Noxa – jest (tabela) → O7; pozostałe pięć – brak → R3 |
| D26 | Każde białko rodziny ma od jednej do czterech domen BH (*Bcl-2 homology domain*); większość antyapoptotycznych – BH1–BH4, proapoptotyczne – BH1–BH3 albo tylko BH3. | 167 | 2 | P1 | jest: `bcl`, „Mimo przeciwnego działania…” |
| D27 | Ryc. 8.3 (ryc.) – układ domen w łańcuchu (w kolejności jak na rycinie): Bcl-2, Bcl-X<sub>L</sub>, Bcl-W, Bcl-B, Mcl-1: BH4–BH3–BH1–BH2–TM; Bax, Bak, Bok: BH3–BH1–BH2–TM; Bfl-1: tylko BH1–BH2; Bad, Bid: tylko BH3; Bim, Bik, Hrk, APR: BH3 i TM. | 167 | 1 | P2 | brak (w cz. 1 tylko ogólnie + rycina) → R3 |
| D28 | Niektóre białka mają hydrofobową domenę transbłonową TM (*Transmembrane Domain*), która prawdopodobnie odgrywa rolę w lokalizacji tych białek. | 167 | 1 | P1 | jest: tamże |
| D29 | Antyapoptotyczne: głównie w zewnętrznej błonie mitochondrialnej; także w błonie siateczki śródplazmatycznej i w otoczce jądrowej. | 167 | 1 | P1 | jest: tabela + „Białka antyapoptotyczne (Bcl-2…” |
| D30 | Ich główna rola: stabilizacja błony mitochondrialnej, przeciwdziałanie stresowi oksydacyjnemu, zapobieganie uwalnianiu cytochromu c (który w konsekwencji nie wiąże się z Apaf-1 – czynnikiem aktywującym apoptozę). | 167 | 1 | P1 | jest: tamże (lista) |
| D31 | Proapoptotyczne: w cytozolu; po odpowiednim sygnale oddziałują z antyapoptotycznymi, powodując hamowanie lub rozpoczęcie śmierci komórki. | 167 | 1 | P1 | jest: `bcl`, „Białka proapoptotyczne (Bax, Bak…” |
| D32 | Białka Bcl-2 regulują też działanie kaspaz we wszystkich szlakach apoptozy oraz stężenie Ca<sup>2+</sup> w komórce. | 167 | 1 | P1 | jest: `bcl`, „Białka rodziny Bcl-2 regulują też…” |

### 2.4. Drewa 8.1.2 Kaspazy (s. 167–169)

| ID | Jednostka informacji | s. | n | Dec. | Stan |
|---|---|---|---|---|---|
| D33 | Rodzina wysoko konserwatywnych proteaz cysteinowych; reszta cysteinowa pełni funkcję katalitycznego nukleofila. | 167 | 2 | P1 | jest: `kas`, „Kaspazy to rodzina…” |
| D34 | Hydrolizują wiązania peptydowe w sąsiedztwie kwasu asparaginowego. | 167 | 1 | P1 | jest: `kas`, „Kaspazy hydrolizują…” |
| D35 | Pierwszego przedstawiciela kaspaz zidentyfikowano jako enzym, który przekształca pro-interleukinę 1β (pro-IL-1β) w aktywną interleukinę 1β – ICE (*Interleukin Converting Enzyme*). Kluczową rolę ICE w apoptozie dowiedziono dzięki sklonowaniu genu *ced-3* *C. elegans*: jego produkt jest podobny do ICE. | 167 | 2 | P2 | jest częśc.: `kas`, „Zidentyfikowano 14 kaspaz. Pierwszą…” → O4 → R1 (uzupełnić: „pro-IL-1β → IL-1β”, „dowiedziono dzięki sklonowaniu”) |
| D36 | Zidentyfikowano 14 kaspaz; dzieli się je na inicjatorowe (indukujące apoptozę) i efektorowe (wykonawcze). | 167 | 2 | P1 | jest: tamże + „Kto tnie prokaspazę?” |
| D37 | Tab. 8.2: inicjatorowe – 2, 8, 9, 10; wykonawcze – 3, 6, 7. Struktura: kaspazy 2 i 9 – 1 CARD + p20 + p10; kaspazy 8 i 10 – 2 DED + p20 + p10; wykonawcze – p20 + p10. | 168 | 2 | P1 | jest: `kas`, „W prodomenie kaspaz inicjatorowych…”, lista, tabela `c03-tab-kaspazy` |
| D38 | Tab. 8.2 (ryc.) – (a) inne nazwy, (b) masy, (c) lokalizacja chromosomowa każdej z siedmiu kaspaz – pełne dane w R2. | 168 | 3 | P2 | brak → R2 (tabela) |
| D39 | Inicjatorowe aktywują się przez autoproteolizę; wykonawcze – przez proteolizę dokonaną przez wcześniej aktywowane kaspazy inicjujące. | 167 | 1 | P1 | jest: `kas`, lista „Kaspazy inicjatorowe… / Kaspazy wykonawcze…” |
| D40 | Kaspazy wykonawcze tną liczne białka cytoplazmatyczne i jądrowe, m.in. białka cytoszkieletu (laminy, aktyna, fodryna), inhibitor CAD (ICAD, *Inhibitor of Caspase-Activated DNase*), polimerazę poli(ADP)-rybozy (PARP), białka Rb i MDM2 (+ s. 171: DNA-PK). | 167, 171 | 1 | P1 | jest: `kas`, lista substratów (cała zostaje – część nazw jest na ryc. `c03-fig-szlaki`) |
| D41 | Wszystkie kaspazy występują w komórce jako nieaktywne proformy – zymogeny. | 167–168 | 1 | P1 | jest: `kas`, „Pomyśl, co by było…” |
| D42 | Budowę poznano dzięki krystalografii rentgenowskiej i sekwencjonowaniu białek: kaspazy są syntetyzowane jako katalitycznie nieczynne, trzyczęściowe proenzymy o masie 32–55 kDa. | 168 | 1 | P1u | „trzy części” – jest; **cz. 2 (R2):** metody badań i masa 32–55 kDa – brak w tekście (masa jest tylko na ryc. `c03-fig-kaspaza`) |
| D43 | Trzy domeny: duża wewnętrzna p20 (17–21 kDa) z podjednostką katalityczną (centrum katalityczne); mała C-końcowa p10 (10–13 kDa), zwana małą podjednostką katalityczną; N-końcowa prodomena (3–24 kDa), zwana domeną śmierci DD (*Death Domain*). | 168 | 1 | P1u | nazwy i położenie – jest (`kas`, lista trzech części); **cz. 2 (R2):** masy części i określenie „mała podjednostka katalityczna” – brak w tekście |
| D44 | W większości prokaspaz podjednostki p20 i p10 oddziela sekwencja łącznikowa. | 168 | 1 | P2 | brak → R2 |
| D45 | Duża N-końcowa prodomena zawiera długi motyw (80–100 reszt), zaangażowany w transdukcję (przekazywanie) sygnałów apoptozy. | 168 | 1 | P2 | brak → R2 |
| D46 | Domena DD ma dwie subdomeny: wykonawczą domenę śmierci DED (*Death Effector Domain*) i domenę aktywacji i rekrutacji kaspaz CARD (*Caspase Recruitment Domain*). | 168 | 1 | P1 | jest: `kas`, „W prodomenie kaspaz inicjatorowych…” |
| D47 | DED i CARD składają się z ułożonych nierównolegle α-helis o charakterze amfipatycznym; z innymi białkami oddziałują przez interakcje elektrostatyczne lub hydrofobowe. | 168 | 1 | P2 | brak → R2 |
| D48 | Ryc. 8.4 (ryc.): katalityczna reszta cysteinowa leży w dużej podjednostce, w obrębie konserwatywnego fragmentu QACxG. | 169 | 1 | P2 | brak → R2 |
| D49 | Ryc. 8.4 (ryc.): trzy miejsca cięcia „asp-x” (za resztą Asp): jedno między prodomeną a p20, dwa – po obu stronach sekwencji łącznikowej; p20 opisano jako podjednostkę α, p10 jako podjednostkę β. | 169 | 1 | P1u | „cięcie za Asp, między prodomeną a p20 i między p20 a p10” – jest (`kas`, „Aktywacja polega na cięciu.”); **cz. 2 (R2):** trzy miejsca, łącznik, nazwy α/β – brak |
| D50 | Aktywna kaspaza: dwie podjednostki p20 i dwie p10 (ryc. 8.4). | 169 | 1 | P1 | jest: tamże + ryc. `c03-fig-kaspaza` |

### 2.5. Drewa 8.2 i 8.2.1 Szlak zewnętrzny (s. 168–171)

| ID | Jednostka informacji | s. | n | Dec. | Stan |
|---|---|---|---|---|---|
| D51 | Apoptoza przebiega różnymi szlakami zależnie od rodzaju komórki i czynnika indukującego; najlepiej poznane: zewnętrzny (błona komórkowa), wewnętrzny (mitochondrialny), pseudoreceptorowy (perforyny, granzym B); także sfingomielinowo-ceramidowy i indukowany stresem. | 168 | 2 | P1 | jest: `szl`, „Wiesz już, kto tnie…” |
| D52 | Szlak zewnętrzny = receptorowy, poznany najwcześniej i najlepiej; uczestniczą receptory śmierci i ich ligandy; receptory to białka transbłonowe z nadrodziny receptorów TNF (*Tumor Necrosis Factor*). | 168–169 | 2 | P1 | jest: `szl`, „Szlak zewnętrzny, zwany też receptorowym…” |
| D53 | Trzy domeny receptora: zewnątrzkomórkowa (rozpoznaje ligand), transbłonowa, cytoplazmatyczna z domeną śmierci DD. | 169 | 1 | P1 | jest: tamże, lista (źródło ryciny z ChatGPT – nie ruszać) |
| D54 | Do rodziny receptorów TNF zalicza się m.in.: TNFR1 i TNFR2 (*Tumor Necrosis Factor Receptor 1, 2*), Fas/CD95/Apo1, TRAIL-R1 i TRAIL-R2 (*TNF-Related Apoptosis-Inducing Ligand-R1, R2*). Ligandy: TNFα (dla TNFR1 i TNFR2), FasL (dla Fas), TRAIL (dla TRAIL-R1 lub -R2). | 169 | 1 | P1u | jest (tabela „Receptor śmierci / Ligand”) → O8. **Cz. 1:** Fas–FasL, TNFR1–TNFα, TRAIL-R1/-R2–TRAIL. **Cz. 2 (R4):** TNFR2, nazwy CD95 i Apo1 (jest), angielskie rozwinięcia (brak) |
| D55 | Najlepiej poznana i najczęściej opisywana jest ścieżka z receptorem Fas. | 169 | 1 | P1 | jest: `szl`, „Najlepiej poznana jest ścieżka…” |
| D56 | FasL + Fas → białko adaptorowe FADD: jego C-końcowa domena DD łączy się z DD receptora; N-końcowa DED – z DED prokaspazy 8 lub 10; powstaje kompleks DISC (*Death Inducing Signaling Complex*), w którym prokaspaza 8/10 staje się czynną kaspazą. | 169 | 3 | P1 | jest: `szl`, lista `ol` 1–4 (źródło ryciny z ChatGPT – nie ruszać) |
| D57 | Kaspazy 8/10 inicjują kaspazy wykonawcze 3, 6, 7 → proteoliza m.in. lamin i białek cytoszkieletu → nieuchronnie śmierć komórki. | 169 | 1 | P1 | jest: lista, pkt 5–6 |
| D58 | Aktywacja receptora Fas może się odbywać także przez białko adaptorowe DAXX, angażujące kinazę JNK; szlak ten działa tylko w niektórych typach komórek. | 169, 171 | 1 | P1u | jest: `szl`, „W niektórych typach komórek receptor Fas…” → O9 (w cz. 1 zostaje DAXX + JNK + „uruchamia kaskadę kaspaz”) |
| D59 | JNK fosforyluje N-końcowy odcinek czynnika transkrypcyjnego c-Jun oraz kinazę odpowiedzi zewnątrzkomórkowej ERK i tak uruchamia kaskadę kaspaz. Szlak może być modyfikowany: białko DAXX bywa zastępowane układem sygnalizacyjnym związanym z małymi białkami G z rodziny Rho (Rac-1). | 171 | 2 | P2 | jest (tamże) → O9 → R4 |
| D60 | W niektórych przypadkach szlak receptorowy łączy się z wewnętrznym przez Bid: kaspaza 8 tnie Bid do tBid (*truncated Bid*); tBid wiąże Bax i zmienia jego konformację; Bax przyłącza się do poryny VDAC i współtworzy przepuszczalne pory; wypływa cytochrom c. | 171 | 2 | P1 | jest: `szl`, „W niektórych przypadkach szlak receptorowy…” + lista |
| D61 | Z mitochondrium wypływa wtedy 100-krotnie więcej cytochromu c niż w typowej ścieżce wewnętrznej. | 171 | 1 | P1 | jest: `szl`, „Sygnał z receptora śmierci może więc…” |
| D62 | Rozwinięcia nazw: FADD – *Fas-Associated Death Domain*; DAXX – *Death Adapter Protein/Death-Associated Protein*; JNK – *Jun-N-terminal Kinase*; ERK – *Extracellular Signal-regulated Kinase*; VDAC – *Voltage Dependent Anion Channel*. | 169, 171 | 1 | P2 | brak → R10 |

### 2.6. Drewa 8.2.2 Szlak wewnętrzny (s. 171, ryc. 8.5 s. 170)

| ID | Jednostka informacji | s. | n | Dec. | Stan |
|---|---|---|---|---|---|
| D63 | Kluczową rolę odgrywają mitochondria (centra energetyczne). Początek szlaku = zwiększenie przepuszczalności błony mitochondrialnej; wyzwalacze: wzrost ROS, wzrost Ca<sup>2+</sup> w cytoplazmie, szok termiczny, zaburzenia transportu elektronów, uszkodzenia DNA. | 171 | 2 | P1 | jest: `szl`, „W szlaku wewnętrznym kluczową rolę…” |
| D64 | Otwierają się megakanały mitochondrialne = pory przepuszczalności PTP (*Permeability Transition Pore*), na styku obu błon; ich budowę i działanie opisuje kilka hipotetycznych modeli. | 171 | 2 | P1 | jest: lista `ol`, pkt 1 |
| D65 | Za zasadniczy element najczęściej uznaje się translokator nukleotydów adeninowych ANT (*Adenine Nucleotide Translocator*) w błonie wewnętrznej. Tworzy kompleksy z poryną VDAC błony zewnętrznej i z obwodowym receptorem benzodiazepiny BPR (*Peripheral Benzodiazepine Receptor*). W kompleksie jest też wiele enzymów, którym przypisuje się funkcje regulatorowe – m.in. kinaza kreatynowa i peroksydaza glutationowa – oraz białka rodziny Bcl-2 (Bcl-2, Bax), łączące się z kanałem od strony cytoplazmatycznej. | 171 | 1 | P1u | jest (pkt 1) → O10. **Cz. 1:** ANT + VDAC + Bcl-2/Bax od strony cytoplazmy. **Cz. 2 (R4):** BPR, kinaza kreatynowa, peroksydaza glutationowa (jest), angielskie nazwy (brak) |
| D66 | Ryc. 8.5 (ryc.), „hipotetyczny model megakanału”: ANT w błonie wewnętrznej, przy nim peroksydaza glutationowa (GPX); VDAC w błonie zewnętrznej, obok BPR; kinaza kreatynowa (CK) między błonami, przy styku ANT–VDAC; Bax i Bcl-2 po stronie cytoplazmy. Przy mitochondrium: Bax „+”, Bcl-2 „–” (wypływ cytochromu c). W podpisie ANT nazwano „translokazą”. | 170 | 1 | P2 | brak → R4 (odczyt z ryciny – zob. decyzja Z1) |
| D67 | Otwarcie megakanałów (niezależnie od teorii budowy): obniża potencjał transbłonowy, hamuje syntezę ATP, podnosi stężenie Ca<sup>2+</sup> w macierzy. | 171 | 1 | P1 | jest: lista, pkt 2 |
| D68 | Wzrostowi przepuszczalności PTP towarzyszy uwolnienie z przestrzeni międzybłonowej do cytoplazmy: cytochromu c, zwanego Apaf-2 (*Apoptosis protease activating factor-2*), czynnika indukcji apoptozy AIF (*Apoptosis-Inducing Factor*), prokaspaz 2, 3 i 9 oraz białka Smac/DIABLO (*Second mitochondrial activator of caspase/Direct IAP Binding protein with Low pI*). | 171 | 1 | P1u | jest (pkt 3) → O11. **Cz. 1:** cytochrom c, AIF, Smac/DIABLO (te są na ryc. `c03-fig-szlaki`). **Cz. 2 (R4):** nazwa Apaf-2, prokaspazy 2, 3, 9 (jest), rozwinięcia (brak) |
| D69 | W cytoplazmie, z udziałem ATP, powstaje apoptosom: cytochrom c + białko adaptorowe Apaf-1 + prokaspaza 9. Apaf-1: na N-końcu domena CARD (łączy prokaspazę 9), na C-końcu domena wielokrotnych powtórzeń WD (*WD-40 repeats*), która wiąże cytochrom c oraz dATP/ATP. | 171 | 2 | P1 | jest: lista, pkt 4 + Pojęcie „Apoptosom” (źródło ryciny z ChatGPT – nie ruszać) |
| D70 | Prokaspaza 9 ulega w apoptosomie katalitycznej aktywacji i uruchamia kaskadę kaspaz wykonawczych; tną one białka istotne dla przeżycia: laminy, aktynę, PARP, DNA-PK. | 171 | 1 | P1 | jest: lista, pkt 5–6 |

### 2.7. Drewa 8.2.3 Szlak pseudoreceptorowy (s. 172, ryc. 8.6 s. 173)

| ID | Jednostka informacji | s. | n | Dec. | Stan |
|---|---|---|---|---|---|
| D71 | Szlak zewnątrzpochodny, indukowany przez komórki układu odpornościowego: cytotoksyczne limfocyty T (CTL) i komórki NK. Uczestniczy układ perforyna–granzym B; CTL i NK produkują perforynę i proteazę serynową – granzym B, uwalniane przez egzocytozę. | 172 | 2 | P1 | jest: `dod`, „Tak jak w szlaku receptorowym…”, „Działa tu układ…” |
| D72 | Początkowo uważano, że perforyna wbudowuje się w błonę komórki, która ma ulec apoptozie, i tworzy kanał dla granzymu B. | 172 | 1 | P1 | jest: lista `ol`, pkt 1 |
| D73 | W cytoplazmie granzym B, podobnie jak kaspazy, hydrolizuje różne substraty i aktywuje kaspazę 3; ta odcina prodomenę kaspazy 7, aktywuje ją i uruchamia kaskadę kaspaz wykonawczych. | 172 | 1 | P1 | jest: lista, pkt 2 |
| D74 | Granzym B może też wnikać bez udziału perforyn: na zasadzie endocytozy albo przy udziale receptora mannozo-6-fosforanu. Ryc. 8.6 (ryc.): obie te drogi oznaczono „endocytoza” i obie prowadzą przez endosom. | 172–173 | 1 | P1u | jest (pkt 1) → O13. **Cz. 1:** „może wnikać także bez perforyny”. **Cz. 2 (R5):** endocytoza, receptor mannozo-6-fosforanu (jest), endosom (brak, odczyt z ryciny) |
| D75 | Granzym B hydrolizuje Bid do tBid; tBid łączy się z Bax i uruchamia ścieżkę z udziałem mitochondrium. | 172 | 1 | P1 | jest: lista, pkt 3 |
| D76 | Wariant z granzymem A (wydzielają go też CTL i NK; wnika przy udziale perforyny): mechanizm nie do końca wyjaśniony; apoptoza niezależna od kaspaz, angażuje jądro; granzym A przechodzi do jądra i hydrolizuje laminy, histon H1 i kompleks SET; na pociętą chromatynę działa uaktywniona DNaza → apoptotyczne zmiany w jądrze. | 172 | 3 | P1 | jest: `dod`, „Szlak pseudoreceptorowy może przebiegać także…” (substraty są na ryc. `c03-fig-dodatkowe`) |
| D77 | Ścieżkę z granzymem A indukuje wzrost stężenia reaktywnych form tlenu oraz zaburzenia potencjału błonowego mitochondrium. | 172 | 1 | P2 | jest (tamże, ostatnie zdanie) → O14 → R5 |
| D78 | Inne nazwy: granzym B = GrB = fragmentyna-2; granzym A = GrA = fragmentyna-1. | 172 | 1 | P2 | jest (w nawiasach) → O12, O14 → R5 (skróty GrB, GrA zostają w cz. 1) |

### 2.8. Drewa 8.2.4 Szlak sfingomielinowo-ceramidowy (s. 172, ryc. 8.6)

| ID | Jednostka informacji | s. | n | Dec. | Stan |
|---|---|---|---|---|---|
| D79 | Ceramid pełni rolę wtórnego przekaźnika. Szlak aktywują: promieniowanie jonizujące, infekcje wirusowe, brak czynników wzrostu. | 172 | 2 | P1 | jest: `dod`, „Ten szlak zaczyna się tak jak zewnętrzny…” |
| D80 | Po połączeniu FasL z Fas aktywuje się kwaśna lub obojętna sfingomielinaza; hydrolizuje błonową sfingomielinę do ceramidu i fosfocholiny (fosforanu choliny). | 172 | 2 | P1 | jest: lista `ol`, pkt 1–2 |
| D81 | Przy tej hydrolizie uwalnia się cholesterol i zmienia się przepuszczalność błony. | 172 | 1 | P2 | jest (pkt 2, drugie zdanie) → O15 → R5 |
| D82 | Ceramid aktywuje: kinazy CAPK (*Ceramide-Activated Protein Kinases*), zależne od mitogenów kinazy MAPK (*Mitogen-Activated Protein Kinases*), fosfatazy CAPP (*Ceramide-Activated Protein Phosphatase*) oraz kaskady kinaz SAPK (*Stress Associated Protein Kinase*)/JNK. | 172 | 1 | P1u | jest (pkt 3) → O16. **Cz. 1:** nazwy czterech grup enzymów (są na ryc. `c03-fig-dodatkowe`). **Cz. 2 (R10):** angielskie rozwinięcia (brak) |
| D83 | To, co ceramid aktywuje, zależy od czynnika stymulującego sygnał, typu komórki i rodzaju sfingomielinazy. | 172 | 1 | P2 | jest (pkt 3, koniec) → O16 → R5 |
| D84 | Ceramid powstały z udziałem sfingomielinazy obojętnej aktywuje kinazy CAPK, MAPK oraz CAPP. | 172 | 1 | P2 | jest (pkt 4) → O16 → R5 |
| D85 | Działanie sfingomielinazy kwaśnej prawdopodobnie prowadzi do powstania ceramidu, który indukuje aktywację kinaz SAPK/JNK; te uruchamiają kaskadę kaspaz wykonawczych. | 172 | 1 | P1u | jest (pkt 4) → O16. **Cz. 1:** „kinazy SAPK/JNK uruchamiają kaskadę kaspaz wykonawczych”. **Cz. 2 (R5):** przypisanie do sfingomielinazy kwaśnej, „prawdopodobnie” |
| D86 | Lipidy te mogą też wpływać na ścieżkę wewnętrzną – zwiększają przepuszczalność błony mitochondrialnej. | 172 | 1 | P1 | jest: `dod`, „Lipidy tego szlaku mogą też…” (pierwsze zdanie) |
| D87 | W apoptozie uczestniczą produkty metabolizmu ceramidu: sfingozyna – inhibitor antyapoptotycznych białek Bcl-2 i Bcl-X<sub>L</sub>; sfingozyno-1-fosforan (ufosforylowana forma sfingozyny) – hamuje apoptozę, blokując wypływ cytochromu c i białka Smac/DIABLO z przestrzeni międzybłonowej mitochondrium. (W źródle literówka „wpływ”.) | 172 | 2 | P2 | jest (tamże, dalsze zdania) → O17 → R5 |

### 2.9. Drewa 8.2.5 Szlak indukowany stresem (s. 174)

| ID | Jednostka informacji | s. | n | Dec. | Stan |
|---|---|---|---|---|---|
| D88 | Wyniki badań przedstawiające ten szlak opublikowano w 2000 r. | 174 | 1 | P2 | brak → R1 |
| D89 | Szlak niezależny od receptorów błony komórkowej i od mitochondrium; kluczowa siateczka śródplazmatyczna. Indukcja: zaburzenia homeostazy Ca<sup>2+</sup> lub nadmierne gromadzenie w siateczce białek niewłaściwie zmodyfikowanych lub błędnie pofałdowanych. | 174 | 2 | P1 | jest: `dod`, „Ten szlak jest niezależny…” + lista, pkt 1 |
| D90 | Czynniki te aktywują prokaspazę 12 z błony siateczki; kaspaza 12 uruchamia kaskadę kaspaz wykonawczych. Kaspaza 12 nie jest konieczna w innych ścieżkach – uznano ją za enzym inicjujący tylko ten szlak. | 174 | 2 | P1 | jest: lista, pkt 2–3 + „Kaspaza 12 nie jest potrzebna…” |
| D91 | Szlak odpowiada za apoptozę neuronów w chorobie Alzheimera; może przebiegać także z udziałem Apaf-1 i ścieżki mitochondrialnej. | 174 | 2 | P1 | jest: tamże + `zab`, „W chorobie Alzheimera…” |

### 2.10. Jóźwiak – Znaczenie apoptozy w fizjologii (s. 126)

| ID | Jednostka informacji | s. | n | Dec. | Stan |
|---|---|---|---|---|---|
| J01 | Kilka typów procesów w dużym stopniu zależy od apoptozy; eliminowane są komórki nadmiarowe, niefunkcjonalne lub niebezpieczne dla organizmu. | 126 | 1 | P1 | jest: `fiz`, „Apoptoza usuwa komórki…” |
| J02 | Rozwój embrionalny: eliminacja komórek, które spełniły rolę; formowanie i kształtowanie niektórych narządów; rozdzielanie palców (apoptoza komórek między połączonymi zawiązkami); zahamowanie → syndaktylia. | 126 | 3 | P1 | jest: `fiz`, h4 „1. Rozwój embrionalny” |
| J03 | Modelowanie układu odpornościowego: przez całe życie w grasicy rozwijają się limfocyty T rozpoznające różne antygeny, także własne; limfocyt skierowany przeciw antygenom własnym → apoptoza (selekcja negatywna) – ochrona przed chorobą autoimmunizacyjną. | 126 | 2 | P1 | jest: h4 „2. Modelowanie…” |
| J04 | Eliminacja uszkodzonych komórek: zakażone wirusem lub po toksynach, nie do uratowania – apoptoza, najczęściej na drodze stresu oksydacyjnego; tak samo komórki uszkodzone przez zbyt niski poziom tlenu lub substancji odżywczych (np. nowotwory rosnące szybciej niż ich naczynia). | 126 | 2 | P1 | jest: h4 „3. Eliminacja uszkodzonych komórek” |
| J05 | Ryc. 11.7 (podpis zdjęcia): w raku gruczołowo-torbielowatym między komórkami nowotworowymi układają się pojedyncze komórki apoptotyczne; widać kondensację jądra, zmniejszenie komórek i ciałka apoptotyczne. | 126 | 1 | P2 | brak → R6 (jedno zdanie-przykład; zdjęcia nie mamy) |
| J06 | Komórki z uszkodzonym DNA: np. promieniowanie jonizujące → uszkodzenie DNA → aktywacja p53; p53 najpierw zatrzymuje cykl na przejściu G1→S (czas na naprawę); gdy naprawa niemożliwa, zwiększa ekspresję Bax → kanały w błonie mitochondrium → wypływ cytochromu c → faza efektorowa. Mechanizm wykorzystuje radioterapia (apoptoza jest jednym z kilku mechanizmów eliminacji komórek). | 126 | 4 | P1 | jest: h4 „4. Eliminacja komórek z uszkodzonym DNA” |

### 2.11. Jóźwiak – Zaburzenia apoptozy, Nowotwory, Choroby neurodegeneracyjne (s. 126–127)

| ID | Jednostka informacji | s. | n | Dec. | Stan |
|---|---|---|---|---|---|
| J07 | Zaburzenia = nasilenie lub zablokowanie apoptozy; prowadzą lub przyczyniają się do wielu procesów patologicznych. Udział udowodniono m.in. w: nowotworach, nadczynności tarczycy, osteoporozie, stwardnieniu rozsianym, chorobie Parkinsona, chorobie Alzheimera. | 126 | 2 | P1 | jest: `zab`, „Skoro apoptoza jest tak ważna…”, „Udział zaburzeń apoptozy…” |
| J08 | Tab. 11.4. Nasilenie apoptozy: cukrzyca typu I, zawał mięśnia serca, choroba Alzheimera, choroba Parkinsona, stwardnienie rozsiane, wrzodziejące zapalenie jelita grubego, choroba Hashimoto, AIDS. Zahamowanie apoptozy: osteoporoza, białaczka, chłoniak, raki (np. piersi, prostaty), nadczynność tarczycy, zespół Smitha, układowy toczeń rumieniowaty. | 127 | 1 | P1u | jest (tabela `c03-tab-choroby`, 8 + 7) → O18. **Cz. 1:** po pięć pierwszych z każdej kolumny. **Cz. 2 (R6):** pełna tabela |
| J09 | Nowotwory: skoro p53 nasila apoptozę po wykryciu uszkodzenia DNA, apoptoza musi zostać zablokowana, aby w długim rozwoju komórki nowotworowej mogły się niekontrolowanie gromadzić mutacje. Zaburzenia apoptozy często odpowiadają za oporność na leki przeciwnowotworowe (leki te często wywołują apoptozę). | 126–127 | 2 | P1 | jest: `zab`, h3 „Dlaczego nowotwór musi…”, „Dlaczego nowotwór staje się oporny…” |
| J10 | Opracowano całą gamę leków przeciwnowotworowych, które wpływają na szlaki związane z apoptozą. | 127 | 1 | P1 | jest: `zab`, h3 „Leki działające…” → po O19 jedno zdanie zostaje w cz. 1 |
| J11 | Najczęstsze zaburzenia w komórkach nowotworowych: nadekspresja antyapoptotycznych białek Bcl-2 (chłoniaki, rak sutka, rak płuc); inaktywacja apoptosomu (czerniak, białaczki, rak szyjki macicy); obniżenie ekspresji Fas (rak wątrobowokomórkowy, rak przełyku, rak jelita grubego); obniżenie aktywności kaspaz. | 127 | 4 | P1 | jest: `zab`, tabela „Gdzie szlak bywa przerwany?” |
| J12 | Ryc. 11.8 (podpis) – pięć leków nasilających apoptozę: cetuksymab, erlotynib, imatynib, sorafenib, bortezomib (mechanizmy i wskazania – pełne brzmienie w R6). | 127 | 5 | P2 | jest: `zab`, h3 „Leki działające na szlaki apoptozy” (lista) → O19 → R6 |
| J13 | Ryc. 11.8 (ryc., schemat): drogi sygnałowe od receptora do Bim i Bax oraz punkty uchwytu sześciu leków, w tym idelalizybu, którego nie ma w podpisie (pełny opis w R6). | 127 | 1 | P2 | brak → R6 (odczyt z ryciny – decyzja Z1) |
| J14 | Choroba Alzheimera: amyloid β (Aβ) odkłada się w przestrzeni międzykomórkowej, białko tau – wewnątrz komórek; Aβ aktywuje kaspazę 3 i nasila apoptozę neuronów; tau jest substratem kaspazy 3, a jego przecięcie prowadzi do gromadzenia agregatów tau w neuronie. | 127 | 3 | P1 | jest: `zab`, „W chorobie Alzheimera…” |
| J15 | Choroba Parkinsona: utrata neuronów dopaminergicznych w układzie nigrostriatalnym; aktywacja kaspazy 3, blokowanie Bcl-2, zwiększenie ekspresji receptora Fas. Zmiany nasilające apoptozę prawdopodobnie przyczyniają się do utraty neuronów w OUN. | 127 | 2 | P1 | jest: `zab`, „W chorobie Parkinsona…” |

### 2.12. Alster–Korwek – wprowadzenie i grupa „struktura i morfologia” (s. 138–140)

| ID | Jednostka informacji | s. | n | Dec. | Stan |
|---|---|---|---|---|---|
| A01 | Starzenie komórkowe – złożony, wieloetapowy proces związany z nieodwracalnym zatrzymaniem komórek w cyklu. | 138 | 1 | P1 | jest: `sta`, „Starzenie komórkowe to złożony…” |
| A02 | Replikacyjne: zależne od skracania telomerów; w hodowli skończona liczba podziałów; po kilku tygodniach lub miesiącach. Przyspieszone: niezależne od skracania telomerów; po kilku dniach od zadziałania czynnika. | 138 | 2 | P1 | jest: tamże, lista |
| A03 | Nie ma jednego znacznika typowego wyłącznie dla starzenia; pewność daje dopiero współwystępowanie kilku. Znaczniki dzielą się na uniwersalne i komórkowo specyficzne. | 138 | 2 | P1 | jest: `sta`, „Znacznik starzenia to cecha…” + Pojęcie |
| A04 | Grupy: struktura i morfologia; regulacja cyklu; DNA i heterochromatyna; fenotyp wydzielniczy; osobno – starzenie indukowane onkogenami (ryc. 1). | 138 | 1 | P1 | jest: tamże, lista + ryc. `c03-fig-starzenie` |
| A05 | Pełne symbole inhibitorów: p16<sup>INK4a</sup>, p21<sup>WAF1/CIP1</sup> (p21<sup>CIP1</sup>), p15<sup>INK4B</sup>, p18<sup>INK4C</sup>, p19<sup>INK4D</sup>, p27<sup>KIP1</sup>, p57<sup>KIP2</sup>. | 138, 140 | 1 | P2 | brak → R8 |
| – | Afiliacje, daty, przypisy odsyłające do innych artykułów zeszytu, piśmiennictwo (73 poz.). | – | – | balast | pomijamy |
| A07 | Komórki w starzeniu replikacyjnym i przyspieszonym powiększają się i stają się płaskie; dotyczy komórek prawidłowych (np. ludzkie komórki mięśni gładkich, fibroblasty) i nowotworowych. | 138–139 | 2 | P1 | jest: `sta`, h4 „Komórka duża i płaska” (poprawka O20) |
| A08 | Zmianę tę opisano m.in. w liniach nowotworowych: ludzkie komórki raka okrężnicy HCT116, linie glejaka U343 MG-A, U87 MG i U343 MG, linia kostniakomięsaka U2OS, ludzkie komórki raka piersi MCF-7. | 139 | 1 | P2 | brak → R8 |
| A09 | W melanocytach starzejących się wskutek nadekspresji onkogenu RAS stwierdza się intensywną wakuolizację. Melanocyty starzejące się wskutek nadekspresji onkogenu BRAF mają wrzecionowate jądra. | 139 | 2 | P2 | brak → R8 |
| A10 | Podstawowy marker: wzrost aktywności i poziomu enzymu lizosomalnego SA-β-Gal; najbardziej znany i najpowszechniej używany in vitro i in vivo; opisany w starzeniu replikacyjnym i przyspieszonym. | 139 | 3 | P1 | jest: `sta`, h4 SA-β-Gal, „Co to jest.” |
| A11 | Znacznik opisali Dimri i wsp. | 139 | 1 | P2 | brak → R8 |
| A12 | Obecny w komórkach, które uległy starzeniu, ale nie w spoczynkowych fibroblastach ani zróżnicowanych keratynocytach; aktywność rośnie z wiekiem dawcy (fibroblasty skóry, keratynocyty naskórka). | 139 | 2 | P1 | jest: „Dlaczego świadczy o starzeniu.” |
| A13 | Znacznik był przydatny także w badaniu starzenia u gryzoni i naczelnych; stosuje się go u starzejących się organizmów modelowych, np. Danio pręgowanego i *C. elegans*. | 139 | 1 | P2 | brak → R8 |
| A14 | Wzrost aktywności także bez starzenia: nieprawidłowe warunki hodowli, przegęszczenie hodowli, światło cebulek włosowych, przewody ekrynowe i łojowe. Wzrost aktywności koreluje ze wzrostem masy lizosomów w komórkach starych. | 139 | 2 | P1 | jest: „Kiedy może zmylić.”, „Dlaczego świadczy…” |
| A15 | SA-β-Gal nie jest niezbędna do starzenia: fibroblasty pacjentów z gangliozydozą GM1 (choroba spichrzeniowa, brak β-galaktozydazy) ulegały starzeniu replikacyjnemu i przyspieszonemu – to drugie pod wpływem adriamycyny, związku indukującego uszkodzenia DNA – bez wzrostu aktywności SA-β-Gal (znacznik zależy od lizosomalnej β-galaktozydazy). | 139 | 1 | P1u | GM1 – jest („Kiedy może zmylić.”); **cz. 2 (R8):** adriamycyna – brak |
| A16 | Obniżenie poziomu β-galaktozydazy technikami siRNA lub shRNA w komórkach prawidłowych i nowotworowych nie hamuje indukcji starzenia. | 139 | 1 | P2 | brak → R8 |
| A17 | Żeby uniknąć wyników fałszywie dodatnich, SA-β-Gal bada się z innym znacznikiem, np. zatrzymaniem w cyklu; jednoczesne zatrzymanie w cyklu i wzrost aktywności świadczą, że wzrost wiąże się ze starzeniem. | 139 | 1 | P1 | jest: „Kiedy może zmylić.” |
| A18 | Mikroskop świetlny: komórki utrwala się, potem inkubuje w roztworze barwiącym z X-gal – substratem β-galaktozydazy; enzym tnie X-gal i powstaje barwny produkt, widoczny w komórkach jako niebieski precypitat. | 139 | 1 | P1u | jest („Jak się wykrywa.”) → O21. **Cz. 1:** jedno zdanie o niebieskim osadzie. **Cz. 2 (R7):** procedura |
| A19 | Cytometr przepływowy: substrat, który pod wpływem β-galaktozydazy emituje zieloną fluorescencję; metoda pozwala na szybką ocenę ilościową komórek o podwyższonej aktywności SA-β-Gal. | 139 | 1 | P2 | jest (tamże) → O21 → R7 |
| A20 | Funkcja SA-β-Gal w starzeniu nie jest poznana; przypuszcza się, że wzrost aktywności wynika jedynie ze wzrostu liczby lizosomów, a nie ze związku przyczynowo-skutkowego ze starzeniem. | 139 | 1 | P1 | jest: „Dlaczego świadczy o starzeniu.” (koniec) |
| A21 | Wzrost ziarnistości komórek – prawdopodobnie przez wzrost masy lizosomów. | 139 | 1 | P1 | jest: h4 „Wzrost ziarnistości” |
| A22 | Ziarnistość określa się cytometrem przepływowym lub obserwacją mikroskopową. | 139–140 | 1 | P2 | jest → O22 → R7 |
| A23 | Lipofuscyna – brązowożółty barwnik powstający podczas utleniania lipoprotein w lizosomach; jej ilość rośnie w komórkach starych organizmów. | 140 | 2 | P1 | jest: h4 „Wzrost poziomu lipofuscyny” |
| A24 | Lipofuscynę ocenia się barwieniami histochemicznymi. | 140 | 1 | P2 | jest → O22 → R7 |
| A25 | Zmienia się poziom białek cytoszkieletu: wimentyny, β-aktyny i tubuliny. | 140 | 1 | P1 | jest: h4 „Zmiany cytoszkieletu” |
| A26 | Wimentyna: białko o masie 58 kDa, III grupa filamentów pośrednich, obecne w komórkach pochodzenia mezenchymalnego; wykazuje dużą homologię międzygatunkową. | 140 | 1 | P1u | grupa III i komórki mezenchymalne – jest; **cz. 2 (R8):** 58 kDa i homologia – brak |
| A27 | W embrionalnych fibroblastach linii TIG3 poziom wimentyny rósł wraz z liczbą podziałów. Ludzkie fibroblasty skórne linii TIG101, które uległy starzeniu, miały ponad dwukrotnie więcej wimentyny niż komórki TIG3 na wczesnym pasażu; płodowe fibroblasty skórne linii TIG3S miały istotnie mniej wimentyny niż TIG101. Komórki, które uległy starzeniu, miały czterokrotnie niższy poziom aktyny i dwukrotnie niższy poziom tubuliny niż komórki młode. | 140 | 1 | P1u | kierunek zmian – jest; liczby – jest → O23. **Cz. 1:** wimentyna rośnie z liczbą podziałów, aktyny i tubuliny mniej. **Cz. 2 (R8):** liczby (jest) i nazwy linii (brak) |
| A28 | Poziom wimentyny ocenia się barwieniami immunocytochemicznymi i techniką Western blotting. | 140 | 1 | P2 | jest (uogólnione na „te białka”) → O23 → R7 (tylko wimentyna – zob. pkt 7) |

### 2.13. Alster–Korwek – proliferacja i cykl (s. 140–141)

| ID | Jednostka informacji | s. | n | Dec. | Stan |
|---|---|---|---|---|---|
| A29 | Podstawowy znacznik: liczba komórek – po zahamowaniu proliferacji się nie zmienia. | 140 | 1 | P1 | jest: `sta`, h4 „Zahamowanie proliferacji” |
| A30 | Wbudowywanie BrdU lub EdU do DNA: brak komórek wbudowujących = zahamowanie syntezy DNA, a więc proliferacji = zatrzymanie w cyklu. | 140 | 1 | P1 | jest: tamże |
| A31 | Białko Ki67 – powszechnie stosowany znacznik proliferacji; brak jego skupisk świadczy o zatrzymaniu proliferacji. | 140 | 1 | P1 | jest: tamże |
| A32 | Wbudowanie BrdU/EdU wykrywa się immunocytochemicznie, techniką ELISA i cytometrem przepływowym; Ki67 – immunocytochemicznie. | 140 | 2 | P2 | jest → O25 → R7 |
| A33 | Cykl regulują cykliny, kinazy zależne od cyklin (CDK) i inhibitory tych kinaz (CKI). | 140 | 1 | P1 | jest: `sta`, „Najpierw krótkie przypomnienie…” |
| A34 | Cztery fazy: G1, S, G2, M; w każdej dominuje inny kompleks cykliny z CDK: G1 – cyklina D–CDK6–CDK4 i cyklina E–CDK2; S – cyklina A–CDK2; G2 – cyklina A–CDK1. Ryc. 2 (ryc.): w fazie M – cyklina B–CDK1; zaznaczono też wyjście do G0. | 140 | 1 | P1u | jest (lista kompleksów) → O24. **Cz. 1:** „w każdej fazie inny kompleks”. **Cz. 2 (R8):** lista (jest) + cyklina B–CDK1 (brak, odczyt z ryciny) |
| A35 | Klasa INK4/ARF (p15, p16, p18, p19): wiążą CDK4 i CDK6 → allosteryczna zmiana uniemożliwia oddziaływanie z cyklinami D. Klasa CIP/KIP (p21, p27, p57): hamują kompleks cyklina–CDK, wiążąc się z jego szczeliną katalityczną. | 140 | 2 | P1 | jest: tamże, lista |
| A36 | Kluczowe szlaki starzenia: p53–p21 (głównie starzenie indukowane uszkodzeniami DNA i replikacyjne) i p16–pRb (indukowane nadekspresją onkogenów); część białek wspólna. | 140–141 | 1 | P1 | jest: „W starzeniu kluczową rolę odgrywają…” |
| A37 | Zwiększona synteza p21 i p16 towarzyszy starzeniu replikacyjnemu i przyspieszonemu; poziom p16 rośnie z wiekiem u ludzi (wykazano w skórze i limfocytach T) i myszy. | 141 | 2 | P1 | jest: h4 „Wzrost poziomu inhibitorów cyklu”, „Co i dlaczego.” |
| A38 | Wzrost p16 koreluje ze zmniejszoną liczbą komórek progenitorowych, obserwowaną z wiekiem w wielu tkankach. | 141 | 1 | P1 | jest: tamże (zostaje) |
| A39 | Starzenie w rozwoju embrionalnym: rośnie p21, nie p16. Wzrost p16 także poza starzeniem – w komórkach gruczołu mlekowego. | 141 | 2 | P1 | jest: „Kiedy może zmylić.” |
| A40 | Są też dane pokazujące, że wzrost poziomu p16 jest wystarczającym dowodem starzenia komórkowego. | 141 | 1 | P2 | brak → R8 |
| A41 | Białka p16 brak w wielu typach nowotworów: glejaku wielopostaciowym, czerniaku, gruczolakoraku trzustki, niedrobnokomórkowym raku płuc, raku pęcherza, raku ustnogardłowym → wniosek: obecność p16 hamuje rozwój nowotworu. | 141 | 1 | P1u | jest (6 nowotworów) → O26. **Cz. 1:** trzy pierwsze + wniosek. **Cz. 2 (R8):** pełna lista |
| A42 | Istotną rolę w starzeniu odgrywają też inne inhibitory obu klas (p15, p19, p27, p57); znacznikami są również cykliny (cyklina D1). | 141 | 1 | P1u | jest (rozwinięte) → O27. **Cz. 1:** jedno–dwa zdania (nazwy są na ryc. `c03-fig-starzenie`) |
| A43 | p15: starzeniu towarzyszy wzrost jego poziomu; wyższy poziom w zmianach łagodnych skóry, płuc i trzustki, ale nie w nowotworach złośliwych tych tkanek. Podwyższony poziom korelował z innymi znacznikami: wzrostem aktywności SA-β-Gal i obecnością SAHF. | 141 | 2 | P2 | pierwsze zdanie – jest → O27; korelacja – brak → R8 |
| A44 | U gryzoni poziom p19<sup>Ink4d</sup> rośnie z wiekiem, ale nie w takim stopniu jak p16<sup>Ink4a</sup>. U gryzoni wzrostowi p16<sup>Ink4a</sup> towarzyszy wzrost p19<sup>Arf</sup> (u ludzi jego odpowiednikiem jest p14<sup>ARF</sup>). | 141 | 2 | P2 | brak → R8 |
| A45 | p57: (a) nadprodukcja w komórkach raka prostaty linii PPC-1 → zatrzymanie w fazie G1, wzrost aktywności SA-β-Gal, komórki duże i płaskie; (b) w linii HUC (*human uroepithelial cells*) poziom p57 rośnie wraz z liczbą podziałów; (c) wprowadzenie p57 do trzech linii glejaka (U343 MG-A, U87 MG, U343 MG) → komórki duże i płaskie, zatrzymanie w G1, wzrost aktywności SA-β-Gal. | 141 | 3 | P2 | (a), (b) – jest bez nazw linii → O27; (c) i nazwy linii – brak → R8 |
| A46 | p27: nie tylko nadprodukcja p21, ale i p27 w ludzkich komórkach kostniakomięsaka linii U2OS prowadziła do indukcji starzenia. | 141 | 1 | P2 | jest bez nazwy linii → O27 → R8 |
| A47 | Cyklina D1 jest znacznikiem starzenia nowotworowych komórek epitelialnych (nabłonkowych); wzrost jej poziomu obserwowano też w komórkach mięśni gładkich. | 141 | 1 | P2 | pierwsza część – jest (zostaje też w cz. 1 jako wzmianka); mięśnie gładkie – brak → R8 |
| A48 | Poziom inhibitorów cyklu i cykliny D1 ocenia się m.in. techniką Western blotting. | 141 | 1 | P2 | jest → O27 → R7 |
| A49 | Zatrzymanie w cyklu uważa się za nieodwracalne – nie są znane czynniki fizjologiczne, które by je odwróciły. Zależnie od typu komórek i czynnika: G1 albo G2; replikacyjne – zwykle G1 (może też G2), przyspieszone – G2. | 141 | 3 | P1 | jest: h4 „Zatrzymanie w cyklu” |
| A50 | Zatrzymanie bada się cytometrem przepływowym. (Zatrzymanie w G2 w starzeniu replikacyjnym opisano w pracy Mao i wsp.) | 141 | 1 | P2 | metoda – jest → O28 → R7; nazwisko – brak → R8 |

### 2.14. Alster–Korwek – DNA i chromatyna (s. 141–143)

| ID | Jednostka informacji | s. | n | Dec. | Stan |
|---|---|---|---|---|---|
| A51 | Uszkodzenia DNA powodujące trwałą aktywację szlaku DDR prowadzą do przyspieszonego starzenia; trwałą aktywację (w odróżnieniu od przejściowej) cechują długo utrzymujące się skupiska białek DDR, np. γH2AX i 53BP1. | 141 | 2 | P1 | jest: `sta`, h4 DNA-SCARS, „Na uszkodzenia DNA…” |
| A52 | Trwała aktywacja DDR wynika z uszkodzeń w odcinkach telomerowych; kilka takich uszkodzeń wystarcza do indukcji starzenia. | 141 | 2 | P1 | jest: „Skupiska białek DDR w jądrze…” |
| A53 | Do niedawna uważano, że starzenie przyspieszone indukują uszkodzenia w telomerowym i nietelomerowym DNA; w 2012 r. kilka zespołów badawczych pokazało, że trwała aktywacja DDR jest wynikiem uszkodzeń w odcinkach telomerowych. | 141 | 1 | P2 | „wcześniej uważano / nowsze badania” – jest (zostaje w cz. 1); rok i „kilka zespołów” – brak → R9 |
| A54 | DNA-SCARS – skupiska białek DDR w jądrze (m.in. ATM, γH2AX, 53BP1); wśród nich TIF – skupiska przy uszkodzonych lub zbyt krótkich telomerach; DNA-SCARS często współwystępują z PML. | 141–142 | 3 | P1 | jest: tamże |
| A55 | DNA-SCARS bada się barwieniami immunocytochemicznymi. | 142 | 1 | P2 | jest → O29 → R7 |
| A56 | SAHF: w ludzkich fibroblastach 30–50 skupisk heterochromatyny widocznych po barwieniu DAPI; powstają w obszarach promotorowych genów białek regulujących fazę S; wykrywa się je przez znakowanie na obecność histonu H3 zmetylowanego na lizynie 9, białka HP1, histonu makroH2A i białka HMGA. | 142 | 3 | P1 | jest: h4 SAHF, „Heterochromatyna to…” |
| A57 | SAHF opisali po raz pierwszy w 2003 r. Narita i wsp., w ludzkich fibroblastach. | 142 | 1 | P2 | brak → R9 |
| A58 | Rodziny składników: histon makroH2A – makroH2A1.1, 1.2 i 2; białka HP1 – HP1α, β i γ; białka HMGA – HMGA1 i 2. | 142 | 1 | P2 | brak → R9 |
| A59 | Powstawanie SAHF: w początkowym etapie biorą udział ASF1a, HIRA i PML; przed powstaniem SAHF białka HIRA i HP1 ulegają translokacji do PML-NB. Pierwszy etap – kondensacja chromosomów (odpowiadają za nią białka opiekuńcze histonów HIRA i ASF1a), widoczna po barwieniu DAPI, zanim SAHF wzbogacą się w HP1, makroH2A i H3K9me. Kolejny krok – metylacja histonu H3 na lizynie 9. Następnie powstaje miejsce wiązania HP1 i wbudowuje się histon makroH2A. | 142 | 1 | P1u | jest (lista 4 kroków) → O30. **Cz. 1:** jedno zdanie („etapami, z udziałem ciałek PML i białek opiekuńczych histonów”). **Cz. 2 (R9):** etapy |
| A60 | W komórkach pozbawionych kinaz ATM lub ATR (kluczowych w szlaku DDR) SAHF nie powstają. | 142 | 1 | P2 | jest → O30 → R9 |
| A61 | Nadprodukcja HIRA lub ASF1a w komórkach pierwotnych przyspiesza tworzenie SAHF. Wyciszenie ASF1a hamuje tworzenie SAHF w starzeniu indukowanym nadekspresją onkogenu RAS. | 142 | 2 | P2 | brak → R9 |
| A62 | SAHF są markerem starzenia przyspieszonego indukowanego onkogenami i replikacyjnego, ale zależy to od typu komórek. | 142 | 1 | P1 | jest: „…SAHF są znacznikiem i starzenia…” |
| A63 | W starzeniu replikacyjnym ludzkich fibroblastów linii IMR90 i WI38 SAHF powstają, w linii BJ – nie; gdy starzenie komórek BJ indukowano nadekspresją onkogenów, SAHF się pojawiały. | 142 | 1 | P2 | brak → R9 |
| A64 | (a) Początkowo nie umiano rozróżnić modyfikacji H3K9me3, H3K9me2, H3K9me i H3K27me – wokół modyfikowanej lizyny są identyczne aminokwasy; pomogły bardziej specyficzne przeciwciała. (b) SAHF mają budowę warstwową: rdzeń bogaty w H3K9me3 otacza pierścień, w którym dominuje H3K27me3. (c) Podczas tworzenia SAHF rośnie poziom HP1, które wiąże się z H3K9me3, ale poziom H3K9me3 znacznie nie rośnie. (d) Pozbawienie ludzkich fibroblastów H3K9me3 lub H3K27me3 nie uniemożliwia powstawania SAHF; nie uniemożliwia go też obniżenie poziomu białek HP1. | 142 | 4 | P2 | brak → R9 |
| A65 | Białko PML jest głównym składnikiem ciałek PML-NB; jest w nich ponad 50 białek, m.in. Rb, p53, ATM, ATR i białka naprawy uszkodzeń DNA. | 142 | 2 | P1 | jest: h4 PML, „Białko PML (ang.…” |
| A66 | (a) PML opisano po raz pierwszy u osób z ostrą białaczką promielocytarną. (b) PML-NB (*PML nuclear bodies*) nazywa się też ND10 (*nuclear bodies*) i POD (*promyelocytic oncogenic domains*). (c) Wśród białek PML-NB są też helikazy i topoizomerazy. | 142 | 3 | P2 | brak → R9 |
| A67 | Synteza (nadprodukcja) PML w komórkach prawidłowych prowadzi do nieodwracalnego zatrzymania w cyklu i starzenia; w starzeniu rośnie liczba i wielkość PML-NB, nowotworzeniu towarzyszy zmniejszenie ich liczby (obniżona synteza PML); brak PML uniemożliwia starzenie wywołane nadprodukcją RAS. | 142 | 3 | P1 | jest: tamże (poprawka O31) |
| A68 | Nadekspresja RAS indukuje starzenie, któremu towarzyszy więcej PML-NB niż w komórkach kontrolnych; w starzeniu indukowanym RAS w obrębie PML-NB stwierdzono białka Rb i p53. W fibroblastach linii IMR90 starzeniu replikacyjnemu towarzyszył wzrost poziomu PML. | 142 | 2 | P2 | brak → R9 |
| A69 | W komórkach zatrzymanych z braku surowicy, z powodu konfluencji lub nadprodukcji p53 nie przybywa PML-NB. PML-NB biorą udział w powstawaniu SAHF. | 142 | 2 | P1 | jest: „Ten znacznik pomaga odróżnić…” (potrzebne do Przykładu) |
| A70 | PML wykrywa się barwieniami immunocytochemicznymi. | 142 | 1 | P2 | jest → O31 → R7 |
| A71 | Telomery – fragmenty DNA na końcach chromosomów; u ssaków powtórzenia sześciu nukleotydów TTAGGG; z każdym podziałem się skracają; maksymalna liczba podziałów = limit Hayflicka, a starzenie spowodowane skracaniem telomerów = replikacyjne. | 142–143 | 3 | P1 | jest: h4 „Skracanie telomerów” |
| A72 | Telomery wraz z kompleksem białek pełnią funkcję ochronną; sześć białek związanych z telomerami – szelteryny: TRF1 (*telomeric repeat binding factor 1*), TRF2 (*telomeric repeat binding factor 2*), POT1 (*protection of telomeres 1*), TIN2 (*TRF1-interacting nuclear protein 2*), TPP1, Rap1 (*repressor-activator protein 1*). | 142 | 1 | P1u | jest (z nazwami) → O32. **Cz. 1:** „sześć białek – szelteryn”. **Cz. 2 (R9):** nazwy (jest) i rozwinięcia (brak) |
| A73 | Telomery odbudowuje telomeraza; poziom enzymu i liczba komórek z jego aktywnością różnią się między gatunkami: u myszy aktywna w komórkach somatycznych, u ludzi rzadko. | 143 | 2 | P1 | jest: tamże |
| A74 | Długość telomerów to znacznik starzenia replikacyjnego; oznacza się ją technikami FISH (*Fluorescence in situ hybridization*) i Southern blotting. | 143 | 1 | P1u | jest → O32. **Cz. 1:** znacznik. **Cz. 2 (R7):** metody |
| A75 | Spadek poziomu laminy B1 (in vitro i in vivo); laminy – filamenty pośrednie typu V, składnik błony jądrowej; spadek w starzeniu replikacyjnym, indukowanym nadekspresją onkogenów i uszkodzeniami DNA. | 143 | 3 | P1 | jest: h4 „Spadek poziomu laminy B1” |
| A76 | Spadek laminy B1 nie zależy od białek p38, ATM ani czynnika transkrypcyjnego NF-κB, wymaga natomiast aktywności jednego z kluczowych szlaków starzenia: p16–pRb albo p53–p21. | 143 | 1 | P1u | jest → O33. **Cz. 1:** wymaga szlaku. **Cz. 2 (R9):** niezależność od p38, ATM, NF-κB |
| A77 | Starzeniu może towarzyszyć wzrost poziomu reaktywnych form tlenu; obniżenie ich poziomu nie hamowało spadku laminy B1. | 143 | 1 | P2 | brak → R9 |
| A78 | Laminę B1 bada się barwieniami immunocytochemicznymi i techniką Western blotting. | 143 | 1 | P2 | jest → O33 → R7 |
| A79 | Znacznik: poziom utlenionych pochodnych zasad azotowych i nukleozydów, np. 8-oksyguaniny (8-oksyGua) i 8-oksy-2′-deoksyguanozyny (8-oksydG). Wolnorodnikowa teoria starzenia: wolne rodniki uszkadzają makrocząsteczki – DNA, lipidy, białka. | 143 | 2 | P1 | jest: h4 „Oksydacyjne modyfikacje zasad azotowych” |
| A80 | Wolnorodnikową teorię starzenia sformułował Denham Harman w 1956 r.; zakłada ona, że wolne rodniki odgrywają krytyczną rolę w starzeniu organizmu. | 143 | 1 | P2 | brak → R9 |
| A81 | Poziom 8-oksydG rośnie z wiekiem: u gryzoni wyższy w jądrowym DNA z różnych narządów starszych zwierząt; u ludzi wyższy w dwóch grupach o średniej wieku 67 i 50 lat niż u osób w wieku ok. 31 lat, z dodatnią korelacją między poziomem 8-oksydG a wiekiem (badano leukocyty i mocz). | 143 | 1 | P1u | trend, gryzonie, leukocyty i mocz – jest; **cz. 2 (R9):** grupy wiekowe i korelacja – brak |
| A82 | W moczu z wiekiem rośnie też 8-oksyGua, uważana za najczulszy znacznik wpływu stresu oksydacyjnego na DNA. | 143 | 1 | P1 | jest: tamże |
| A83 | Globalna demetylacja w wielu typach komórek i tkanek (poziom 5-metylocytozyny spada in vitro z liczbą pasaży); demetylacja konkretnych genów (np. *MYC*, β-aktyna); w starzeniu replikacyjnym fibroblastów – hipometylacja i skupiskowa hipermetylacja konkretnych genów, profil podobny do nowotworowego. | 143 | 3 | P1 | jest: h4 „Zmiany metylacji DNA” |
| A84 | Transformacja komórek wirusem SV-40 powoduje, że 5-mC utrzymuje się na stałym poziomie. | 143 | 1 | P2 | brak → R9 |

### 2.15. Alster–Korwek – SASP, onkogeny, podsumowanie (s. 143–144)

| ID | Jednostka informacji | s. | n | Dec. | Stan |
|---|---|---|---|---|---|
| A85 | Komórki stare mają fenotyp wydzielniczy SASP (inaczej SMS): cytokiny, proteazy, czynniki wzrostu i inne związki działające autokrynnie lub parakrynnie; zależy od bodźca indukującego starzenie i typu komórek. | 143 | 3 | P1 | jest: `sta`, h3 SASP, „Stare komórki nie tylko…” |
| A86 | SASP pojawia się przy trwałej aktywacji DDR; przy przejściowej czynniki nie są wydzielane. | 143 | 1 | P1 | jest: „SASP pojawia się przy trwałej…” |
| A87 | Aktywność SASP regulują niektóre białka szlaku DDR: ATM (*Ataxia telangiectasia mutated*), NBS1 (*Nijmegen breakage syndrome protein-1*) i CHK2 (*checkpoint kinase 2*) oraz czynniki transkrypcyjne NF-κB (*nuclear factor kappa-light-chain-enhancer of activated B cells*) i C/EBP-β (*CCAAT-enhancer-binding proteins*). | 143 | 1 | P1u | jest (bez rozwinięć) → O34. **Cz. 1:** „białka szlaku DDR i czynniki transkrypcyjne, m.in. NF-κB”. **Cz. 2 (R9):** lista (jest) i rozwinięcia (brak) |
| A88 | Inaktywacja białka p53 zwiększa wydzielanie niektórych elementów SASP. Kinaza p38MAPK, która pojawia się pod wpływem nadekspresji onkogenu RAS i promieniowania X, indukuje SASP przez aktywację NF-κB. | 143 | 2 | P2 | jest → O34 → R9 |
| A89 | Zastosowanie inhibitora kinazy p38MAPK zmniejszało wydzielanie większości elementów SASP. | 143 | 1 | P2 | brak → R9 |
| A90 | Jedną z pierwszych wydzielanych cytokin jest IL-1α: wiąże się z receptorem IL1R, który aktywuje kaskadę sygnałów prowadzącą do aktywacji NF-κB; ten indukuje transkrypcję genów prozapalnych cytokin IL-6 i IL-8. Czynniki SASP działają pozytywnie i negatywnie: indukują angiogenezę, proliferację i różnicowanie komórek, naprawę (regenerację) tkanek, transformację epitelialno-mezenchymalną, oporność na chemioterapię, aktywują układ odpornościowy (ryc. 3). | 143–144 | 2 | P1 | jest: „Jedną z pierwszych cytokin…” |
| A91 | SASP mierzy się cytometrem przepływowym i techniką ELISA. | 144 | 1 | P2 | jest → O34 → R7 |
| A92 | Starzenie indukowane onkogenami: podwyższony poziom białek DEC1 (*differentiated embryo-chondrocyte expressed-1*) i DCR2 (*decoy death receptor-2*), aktywowanych przez p53; wyższy w zmianach łagodnych skóry, płuc i trzustki niż w nowotworach złośliwych; koreluje ze wzrostem aktywności SA-β-Gal i obecnością SAHF. | 144 | 2 | P1 | jest: h3 „Znaczniki starzenia wywołanego onkogenami” (rozwinięcie DEC1 → R10) |
| A93 | Wniosek autorów: trzeba zbadać przynajmniej kilka znaczników; dopiero ich współwystępowanie daje pewność, że komórki uległy starzeniu. | 144 | 1 | P1 | jest: h3 „Jeden znacznik to za mało…” |

**Suma:** P1 = 186 (Drewa 83, Jóźwiak 26, Alster 77) · P1u = 26 (12, 1, 13) · P2 = 87 (29, 7, 51).

---

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
