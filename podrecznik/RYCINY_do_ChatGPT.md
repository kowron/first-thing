# 12 nowych rycin do zamówienia w ChatGPT – spis i gotowe prompty

Stan na 18.11.2026. Dokument dla zleceniodawcy: wklejasz najpierw **Wstęp (część 1)**, potem po jednej karcie ryciny na wiadomość.
Treść każdej ryciny pochodzi wyłącznie z tekstu podręcznika (pod każdą kartą: „Źródło treści”).

**Jak wybrano miejsca.** Po jednej rycinie na rozdział; rozdział 10 dostaje dwie (ma najmniej rycin na stronę tekstu, a dwa mechanizmy – XIST i premutacja FMR1 – są opisane tylko słowami). Pominięto wszystko, co ma już rycinę w rozdziale, oraz tematy, które mają gotową rycinę w `bank-rycin/` (np. telomery, interferencja RNA, topoizomerazy, startery do odwrotnej transkrypcji, krzywe Ct, mapa restrykcyjna) – tych nie trzeba zamawiać, wystarczy je wstawić z banku.

**Rozdziały w przebudowie (G, 4, 5).** Miejsca podano przez `id` podrozdziału h2 i nazwę h3 – te zostają po przepisaniu. Początek akapitu podano według wersji pliku z 18.11; jeśli akapit zmieni brzmienie, rycina staje po akapicie o tej samej treści (opisanej w karcie).

---

## 1. Wstęp dla ChatGPT – wspólny styl (wkleić raz, na początku rozmowy)

```text
Będziesz rysować serię 12 rycin do polskiego podręcznika akademickiego „Biologia molekularna” (studenci I roku kierunku lekarskiego). Każdą rycinę opiszę w osobnej wiadomości. Poniższe zasady obowiązują dla wszystkich rycin – trzymaj się ich bez przypominania.

STYL
- Płaska, czysta ilustracja naukowa o wyglądzie wektorowym (jak schemat w podręczniku akademickim). Białe tło (#ffffff).
- Bez cieni, bez gradientów, bez efektu 3D, bez faktur, bez dekoracji, bez ikon „dla ozdoby”, bez ramki wokół całej ryciny.
- Kształty proste: prostokąty z lekko zaokrąglonymi rogami, koła, owale, linie. Kontury jednej grubości (cienkie, równe).
- Strzałki proste lub łagodnie zagięte, z małym pełnym grotem. Każda strzałka znaczy tylko to, co podam w opisie.
- Dużo wolnego miejsca między elementami; nic się nie nakłada na napisy.

PALETA (używaj wyłącznie tych kolorów)
- ciemna zieleń #173d2b – główne kontury, tytuły paneli, plakietki A/B, najważniejsze elementy
- zieleń akcentu #2b7a4b – strzałki głównego biegu procesu, numery kroków (białe cyfry w zielonym kółku), wyróżnienia
- jasna zieleń #8fd3a6 i tło zielone #e7f2ea – wypełnienia elementów „prawidłowych / aktywnych”
- szary kafelek #f0f4f1, linia #dae5de, szara linia #9aa59f – tła paneli, elementy drugoplanowe, błony, linie pomocnicze
- tekst #222b26; tekst pomocniczy #5f6b64
- kolory pomocnicze do rozróżniania elementów: niebieski #4387b7 (tło #eef5fb), fiolet #7867a8 (tło #f1eef7), ochra #b77a20 (tło #fbf3e5), złoty #e3b23c
- czerwień #c84d42 (tło #fff0ec) – tylko dla: błędu, mutacji, hamowania, uszkodzenia, śmierci komórki
Żadnych innych barw (bez różu, turkusu, pomarańczu, czerni #000000).

NAPISY
- Wszystkie napisy po polsku, z poprawnymi polskimi znakami: ą, ę, ł, ó, ś, ź, ż, ć, ń (oraz wielkie: Ą, Ę, Ł, Ó, Ś, Ź, Ż, Ć, Ń).
- Krój bezszeryfowy, prosty (Inter, a jeśli niedostępny – podobny: Helvetica/Arial). Bez kursywy, chyba że ją wskażę.
- Na rycinie tylko etykiety, nazwy i numery kroków – żadnych zdań-akapitów, żadnych objaśnień od siebie.
- KAŻDĄ ETYKIETĘ NAPISZ DOKŁADNIE TAK, JAK PODAM W LIŚCIE (litera po literze, z wielkością liter, łącznikami, indeksami i znakami typu ′, →, ⁺). Nie tłumacz na angielski, nie skracaj, nie dodawaj własnych etykiet.
- Znak „prim” w zapisach 3′ i 5′ to ′ (nie apostrof ').
- Wysokość liter: etykiety ok. 40–45 px, nie mniej niż 36 px; tytuły paneli ok. 50 px, pogrubione.
- Bez tytułu ryciny i bez podpisu na obrazie (podpis jest w podręczniku). Bez znaków wodnych, logotypów, sygnatur.
- Panele oznaczaj plakietką: biała litera (A, B, C…) w kółku w kolorze #173d2b, w lewym górnym rogu panelu.

FORMAT
- Plik PNG, białe tło.
- Rycina „2 łamy” (cała szerokość strony, ok. 180 mm): szerokość 2400 px; wysokość według proporcji podanych przy rycinie.
- Rycina „1 łam” (ok. 85 mm): szerokość 1200 px; wysokość według proporcji podanych przy rycinie.
- Jeśli nie możesz wygenerować dokładnie podanych proporcji: wygeneruj obraz poziomy 3:2 (lub kwadrat dla rycin 1:1) i umieść całą treść w środkowym pasie o podanych proporcjach, zostawiając powyżej i poniżej czyste białe tło do przycięcia.
- Margines wewnętrzny: ok. 40 px białego pola z każdej strony; nic nie dotyka krawędzi.

ZASADA TREŚCI
- Rysuj tylko elementy, które wymienię. Niczego nie dodawaj „dla kompletności” (żadnych dodatkowych białek, organelli, liczb, strzałek).
- Jeśli czegoś nie da się narysować zgodnie z opisem – zapytaj, zamiast zgadywać.

Potwierdź krótko, że zasady są jasne, i czekaj na opis ryciny 1.
```

---

## 2. Tabela zbiorcza

| nr | rozdział | gdzie wstawić (id podrozdziału → miejsce) | tytuł ryciny (`data-title`) | szerokość | proporcje (px) |
|---|---|---|---|---|---|
| 1 | G – Genomika | `#c01-strategia` → przed tabelą strategii (zaślepka już stoi) | Panel, eksom, genom – co zostaje odczytane | 2 łamy | 20:9 (2400 × 1080) |
| 2 | 2 – Cykl komórkowy | `#c02-sg2`, h3 „Jak komórka kończy podział? Kompleks promujący anafazę” → po liście czterech zadań APC/C, przed akapitem „Ostatni punkt łączy się z jednym z pytań…” | Cztery zadania kompleksu APC/C | 2 łamy | 20:9 (2400 × 1080) |
| 3 | 3 – Apoptoza | `#c03-szlaki`, h3 „Szlak wewnętrzny: sygnał powstaje w komórce” → po akapicie zaczynającym się od „Porównaj oba szlaki.” | DISC i apoptosom – która domena łączy się z którą | 2 łamy | 20:9 (2400 × 1080) |
| 4 | 4 – Kwasy nukleinowe | `#c04-replikacja`, h3 „Jak replikacja unika błędów? Korekta” → po akapicie zaczynającym się od „Polimeraza na bieżąco sprawdza…” | Korekta: polimeraza cofa się i wycina błąd | 1 łam | 1:1 (1200 × 1200) |
| 5 | 5 – PCR | `#c05-rt` (h2 „Odwrotna transkrypcja i RT-PCR”) → na końcu podrozdziału, po akapicie o DNazie (dziś: „W bardzo czułych badaniach przeszkadzają…”) | RT-PCR: od RNA do produktu PCR | 2 łamy | 3:1 (2400 × 800) |
| 6 | 6 – Elektroforeza i hybrydyzacja | `#c06-hybrydyzacja`, h3 „Jak zobaczyć, gdzie usiadła sonda?” → po akapicie „4. Znakowanie enzymatyczne.”, przed tabelą | Cztery sposoby znakowania sondy | 2 łamy | 20:9 (2400 × 1080) |
| 7 | 7 – Komórki macierzyste | `#c07-typy`, h3 „Indukowane pluripotencjalne komórki macierzyste (iPSC) – cofnięcie różnicowania” → po liście pięciu kroków, przed akapitem „Zalety iPSC wynikają z ich pochodzenia.” | Jak powstają iPSC | 2 łamy | 8:3 (2400 × 900) |
| 8 | 8 – Dziedziczenie | `#c08-mito`, h3 „Dlaczego najciężej choruje układ nerwowy? Próg energetyczny” → po akapicie zaczynającym się od „Każda tkanka potrzebuje określonej ilości ATP.” | Heteroplazmia i próg energetyczny | 2 łamy | 20:9 (2400 × 1080) |
| 9 | 9 – Cytogenetyka | `#c09-aberracje`, h3 „Aberracje strukturalne: katalog zapisów” → po tabeli zapisów, przed akapitem „W kariotypie człowieka najczęściej stwierdza się izochromosom…” | Aberracje strukturalne – przed i po | 2 łamy | 20:9 (2400 × 1080) |
| 10 | 10 – Płeć | `#c10-lyon`, h3 „Jak komórka wyłącza cały chromosom? Mechanizm molekularny” → po akapicie zaczynającym się od „Co ją utrzymuje – metylacja DNA.” | Inaktywacja X: XIC, XIST, metylacja | 2 łamy | 8:3 (2400 × 900) |
| 11 | 10 – Płeć | `#c10-sprzezone`, h3 „Zespół kruchego chromosomu X – gdy proste reguły nie wystarczają” → po akapicie zaczynającym się od „Teraz paradoks znika.” | Paradoks Shermana: od premutacji do pełnej mutacji | 1 łam | 1:1 (1200 × 1200) |
| 12 | 11 – Biotechnologia | `#c11-kierunki`, h3 „Nowotwory – cztery różne pomysły” → po akapicie zaczynającym się od „Geny samobójcze – molekularna chemioterapia.” | Gen samobójczy i efekt sąsiedztwa | 2 łamy | 20:9 (2400 × 1080) |

Proporcje 20:9 (ok. 179 × 81 mm) i 1:1 (ok. 86 × 86 mm) mieszczą się w limicie podręcznika „rycina ≤ 1/3 strony”.

---

## 3. Karty rycin

### Rycina 1 · Rozdział G (Genomika)

- **Miejsce:** `#c01-strategia` – przed tabelą strategii (zaślepka `c01-fig-zakres` już stoi w rozdziale).
- **id:** `c01-fig-zakres` · **Tytuł:** Panel, eksom, genom – co zostaje odczytane · **2 łamy, 20:9**
- **Po co:** student ma zobaczyć na jednym odcinku DNA, że trzy strategie różnią się *zakresem*: panel czyta wybrane geny, WES – eksony wszystkich genów (ok. 1–2% genomu), WGS – także regiony niekodujące. Wniosek: wynik ujemny znaczy tyle, ile obejmował zakres.

**Prompt dla ChatGPT:**

```text
RYCINA 1. Format: 2 łamy, 2400 × 1080 px (20:9). Bez paneli A/B – jeden schemat z czterema poziomymi wierszami, czytany od góry do dołu.

UKŁAD
Z lewej wąska kolumna z nazwami wierszy (ok. 20% szerokości), z prawej (ok. 80%) w każdym wierszu ten sam odcinek DNA narysowany w identycznym położeniu, tak żeby elementy leżały dokładnie jeden pod drugim.

ODCINEK DNA (taki sam w każdym wierszu)
Pozioma cienka linia w kolorze #9aa59f. Na niej cztery geny rozmieszczone równo od lewej do prawej. Każdy gen to 3 prostokąty (eksony) połączone cienką linią (introny); eksony mają wysokość ok. 4× grubości linii. Między genami dłuższe odcinki samej linii (regiony niekodujące).

WIERSZ 1 (wzorzec, bez zaznaczeń): eksony z szarym wypełnieniem #f0f4f1 i konturem #173d2b. Nad genami podpisy: „gen 1”, „gen 2”, „gen 3”, „gen 4”. Trzy cienkie linie wskazujące (bez grotów) z etykietami: „ekson” (do jednego prostokąta), „intron” (do linii między eksonami tego samego genu), „regiony niekodujące” (do linii między genami).

WIERSZ 2 – nazwa z lewej: „Panel genów”. Zaznaczone na zielono (#2b7a4b, pełne wypełnienie) są tylko eksony genu 2 i genu 3; reszta bladoszara (#dae5de). Pod genami 2 i 3 mała klamra z etykietą „wybrane geny”.

WIERSZ 3 – nazwa z lewej: „WES”. Zielone (#2b7a4b) są eksony wszystkich czterech genów; introny i regiony między genami bladoszare (#dae5de). Z prawej strony wiersza etykieta: „eksom: ok. 1–2% genomu”.

WIERSZ 4 – nazwa z lewej: „WGS”. Zielony (#2b7a4b) jest cały odcinek: eksony, introny i regiony między genami (linia pogrubiona na zielono). W jednym miejscu między genem 3 a genem 4 krótka przerwa w zielonym kolorze (zostaje bladoszara linia) z etykietą „luka”. Z prawej strony wiersza etykieta: „także regiony niekodujące”.

Między wierszami cienkie poziome linie rozdzielające (#dae5de). W prawym dolnym rogu mała legenda: zielony kwadracik + „odczytane”, bladoszary kwadracik + „poza zakresem”.

PEŁNA LISTA ETYKIET (dokładnie tak):
gen 1 · gen 2 · gen 3 · gen 4 · ekson · intron · regiony niekodujące · Panel genów · wybrane geny · WES · eksom: ok. 1–2% genomu · WGS · także regiony niekodujące · luka · odczytane · poza zakresem

NIE RYSUJ: podwójnej helisy, chromosomów, sekwenatora, odczytów (krótkich kresek), liczb innych niż „ok. 1–2%”, strzałek, żadnych innych strategii (RNA-seq, badanie jednej zmiany).
```

- **Proponowany podpis:** Zacznij od górnego wiersza: ten sam odcinek DNA z czterema genami powtarza się w każdym wierszu. Porównaj, co jest zielone: w panelu – tylko wybrane geny, w WES – eksony wszystkich genów (ok. 1–2% genomu), w WGS – także introny i regiony niekodujące, choć i tu zostają luki. Wniosek: wynik ujemny mówi tylko o tym, co badanie objęło.
- **Źródło treści:** `#c01-ngs`, h3 „Panel, eksom, genom”: „Panel obejmuje wybrane geny lub regiony związane z problemem, WES – przede wszystkim regiony kodujące białka (eksom; sekwencje kodujące to ok. 1–2% genomu), WGS – genom znacznie szerzej, z regionami niekodującymi”; „większość intronów i elementów regulatorowych leży poza nim”; tabela strategii, wiersz WGS: „trudniejsza interpretacja; nadal są luki”.
- **Uwaga dla autora rozdziału:** tekst nie mówi wprost, czy panel czyta introny wybranych genów; na rycinie zaznaczono eksony (zgodnie z opisem panelu wirtualnego jako listy genów ocenianych w danych WES). Jeśli w nowej wersji G będzie inaczej – zmienić wiersz 2.

---

### Rycina 2 · Rozdział 2 (Cykl komórkowy)

- **Miejsce:** `#c02-sg2` (h2 „Regulacja faz S i G2”), h3 „Jak komórka kończy podział? Kompleks promujący anafazę” – po liście czterech zadań APC/C, przed akapitem zaczynającym się od „Ostatni punkt łączy się z jednym z pytań punktów kontrolnych”.
- **id:** `c02-fig-apc` · **Tytuł:** Cztery zadania kompleksu APC/C · **2 łamy, 20:9**
- **Po co:** student ma odczytać łańcuch „MPF → APC/C → cztery skutki” i zrozumieć, że jeden kompleks jednocześnie rozdziela chromatydy, wyłącza cdk1 i przygotowuje następny cykl.

**Prompt dla ChatGPT:**

```text
RYCINA 2. Format: 2 łamy, 2400 × 1080 px (20:9). Jeden schemat czytany od lewej do prawej, bez paneli A/B.

UKŁAD
U góry przez całą szerokość cienka pozioma oś czasu (#9aa59f) z dwoma napisami: z lewej „metafaza”, z prawej „anafaza”, między nimi grot strzałki w prawo.
Poniżej trzy kolumny:

KOLUMNA LEWA (ok. 20% szerokości): zaokrąglony prostokąt z wypełnieniem #eef5fb i konturem #4387b7, w środku dwa wiersze napisu: „MPF” (pogrubione) i pod spodem „cykliny B i A + cdk1”.

Od MPF w prawo gruba zielona strzałka (#2b7a4b) z napisem nad nią: „aktywuje”.

KOLUMNA ŚRODKOWA (ok. 20%): duży zaokrąglony prostokąt z wypełnieniem #173d2b i białym napisem: „APC/C” (pogrubione) i pod spodem mniejszym „cyklosom”.

KOLUMNA PRAWA (ok. 55%): cztery jednakowe poziome kafle jeden pod drugim (tło #f0f4f1, kontur #dae5de). Od APC/C do każdego kafla osobna zielona strzałka (#2b7a4b). Każdy kafel: z lewej zielone kółko z białym numerem (1–4), dalej mały piktogram, napis „co robi” (pogrubiony) i po cienkiej strzałce w prawo napis „skutek” (zwykły).

Kafel 1. Piktogram: chromosom w kształcie litery X złożony z dwóch chromatyd (#4387b7), spiętych w środku dwiema małymi czerwonymi klamrami (#c84d42); obok te same dwie chromatydy już rozdzielone, bez klamer. Napisy: „degradacja kohezyn” → „chromatydy siostrzane mogą się rozdzielić”.
Kafel 2. Piktogram: owal „cyklina B” (#b77a20, tło #fbf3e5) z trzema małymi kółkami doczepionymi w rzędzie (ubikwityna, fiolet #7867a8), strzałka do szarego walca. Napisy przy piktogramie: „cyklina B”, „ubikwityna”, „proteasom”. Napisy główne: „degradacja cykliny B” → „cdk1 traci partnera”.
Kafel 3. Piktogram: krótki odcinek DNA (pozioma linia) z prostokątem genu i zagiętą strzałką transkrypcji nad nim. Napisy: „nasila ekspresję genów cyklin fazy G1” → „potrzebne w następnym cyklu”.
Kafel 4. Piktogram: owal „geminina” (#7867a8, tło #f1eef7) przekreślony jedną czerwoną kreską (#c84d42). Napisy: „degradacja gemininy” → „DNA będzie można znowu skopiować w kolejnym cyklu”.

PEŁNA LISTA ETYKIET (dokładnie tak):
metafaza · anafaza · MPF · cykliny B i A + cdk1 · aktywuje · APC/C · cyklosom · 1 · 2 · 3 · 4 · degradacja kohezyn · chromatydy siostrzane mogą się rozdzielić · cyklina B · ubikwityna · proteasom · degradacja cykliny B · cdk1 traci partnera · nasila ekspresję genów cyklin fazy G1 · potrzebne w następnym cyklu · geminina · degradacja gemininy · DNA będzie można znowu skopiować w kolejnym cyklu

NIE RYSUJ: wrzeciona podziałowego, centrosomów, całej komórki, separazy, sekuryny, Cdc20 ani żadnych białek spoza listy; nie dodawaj koła cyklu komórkowego.
```

- **Proponowany podpis:** Zacznij od lewej: MPF (cykliny B i A z cdk1) aktywuje APC/C. Następnie porównaj cztery kafle – w każdym po lewej jest to, co APC/C robi, a po prawej skutek. Wniosek: ten sam kompleks rozdziela chromatydy (1), wyłącza kinazę cdk1 (2) i przygotowuje następny cykl (3, 4).
- **Źródło treści:** `#c02-sg2`: „Kompleks cyklin mitotycznych (cykliny B i A) z kinazą cdk1 to czynnik promujący fazę M (MPF).”; „W metafazie MPF aktywuje kompleks promujący anafazę (APC…), nazywany też cyklosomem i oznaczany skrótem APC/C.”; lista czterech zadań („Uruchamia enzymatyczną degradację kohezyn…”, „Obniża poziom cykliny B: przyłącza do niej ubikwitynę i kieruje ją do degradacji w proteasomie. Kinaza cdk1 traci partnera”, „Nasila ekspresję genów kodujących cykliny fazy G1…”, „Powoduje degradację gemininy…”) oraz akapit „Gdy APC/C ją rozkłada, ta ochrona znika – w kolejnym cyklu DNA będzie można znowu skopiować.”

---

### Rycina 3 · Rozdział 3 (Apoptoza)

- **Miejsce:** `#c03-szlaki` (h2 „Szlak zewnętrzny i wewnętrzny”), h3 „Szlak wewnętrzny: sygnał powstaje w komórce” – po akapicie zaczynającym się od „Porównaj oba szlaki. W każdym białko adaptorowe…”.
- **id:** `c03-fig-kompleksy` · **Tytuł:** DISC i apoptosom – która domena łączy się z którą · **2 łamy, 20:9**
- **Po co:** istniejąca rycina szlaków pokazuje kolejność białek, ale nie to, *czym* się łączą. Student ma zobaczyć regułę „domena z domeną tego samego typu” (DD–DD, DED–DED, CARD–CARD) i dwie różne końcówki białka adaptorowego.

**Prompt dla ChatGPT:**

```text
RYCINA 3. Format: 2 łamy, 2400 × 1080 px (20:9). Dwa panele obok siebie o równej szerokości: A z lewej, B z prawej, rozdzielone cienką pionową linią (#dae5de). Oba panele czyta się od góry do dołu i mają tę samą budowę: sygnał u góry → białko adaptorowe → prokaspaza → wynik na dole.

KONWENCJA RYSUNKU (ważna): każde białko to poziomy lub pionowy „pasek” złożony z prostokątnych segmentów-domen stykających się bokami. Ten sam typ domeny ma zawsze ten sam kolor:
- DD – niebieski #4387b7 (białe litery)
- DED – ochra #b77a20 (białe litery)
- CARD – fiolet #7867a8 (białe litery)
- WD-40 – ciemna zieleń #173d2b (białe litery)
- p20 i p10 – szare kafle #f0f4f1 z konturem #9aa59f (ciemne litery)
Tam, gdzie dwie domeny tego samego typu się łączą, narysuj je stykające się bokiem i zaznacz styk krótką podwójną kreską w kolorze #2b7a4b.

PANEL A – tytuł panelu: „DISC (szlak zewnętrzny)”
U góry pozioma błona komórkowa: dwa równoległe szare pasy (#9aa59f) przez całą szerokość panelu; z lewej strony podpis „błona komórkowa”.
1) Nad błoną: mały trójkąt (#c84d42) z etykietą „FasL”, osadzony w górnym końcu receptora.
2) Receptor „Fas”: pionowy pasek przechodzący przez błonę, z trzema częściami: nad błoną segment jasnoszary z etykietą obok „domena zewnątrzkomórkowa”, w błonie segment z etykietą „domena transbłonowa”, pod błoną segment zakończony niebieską domeną z napisem „DD” i etykietą obok „domena cytoplazmatyczna”.
3) Pod receptorem białko „FADD”: pasek z dwóch domen – górna niebieska „DD” styka się z DD receptora; dolna w kolorze ochry „DED”.
4) Pod FADD „prokaspaza 8 (lub 10)”: pasek z czterech segmentów w kolejności: „DED”, „DED”, „p20”, „p10”; pierwsza domena DED styka się z DED białka FADD.
5) Klamra obejmująca receptor, FADD i prokaspazę, z napisem „DISC”.
6) Zielona strzałka w dół do zaokrąglonego prostokąta (tło #e7f2ea, kontur #2b7a4b) z napisem „kaspaza 8 (lub 10)”.

PANEL B – tytuł panelu: „Apoptosom (szlak wewnętrzny)”
Bez błony. U góry z lewej mały fragment zarysu mitochondrium (owal ucięty krawędzią panelu, kontur #9aa59f) z podpisem „mitochondrium”; z niego wychodzi strzałka do małego czerwonego kółka z białą literą „c” i etykietą „cytochrom c”.
1) Białko „Apaf-1”: pasek z dwóch domen – górna ciemnozielona „WD-40”, dolna fioletowa „CARD”.
2) Do domeny WD-40 przylegają: kółko „c” (cytochrom c) oraz mały złoty sześciokąt (#e3b23c) z etykietą „dATP/ATP”.
3) Pod Apaf-1 „prokaspaza 9”: pasek z trzech segmentów: „CARD”, „p20”, „p10”; jej CARD styka się z CARD białka Apaf-1.
4) Klamra obejmująca cytochrom c, Apaf-1 i prokaspazę 9, z napisem „apoptosom”.
5) Zielona strzałka w dół do zaokrąglonego prostokąta (tło #e7f2ea, kontur #2b7a4b) z napisem „kaspaza 9”.

DÓŁ RYCINY (wspólny, pod oboma panelami, na środku): od „kaspaza 8 (lub 10)” i od „kaspaza 9” po jednej zielonej strzałce do wspólnego prostokąta (wypełnienie #173d2b, białe litery): „kaspazy wykonawcze 3, 6, 7”.

W prawym dolnym rogu mała legenda domen: cztery kolorowe kwadraciki z napisami „DD”, „DED”, „CARD”, „WD-40”.

PEŁNA LISTA ETYKIET (dokładnie tak):
DISC (szlak zewnętrzny) · błona komórkowa · FasL · Fas · domena zewnątrzkomórkowa · domena transbłonowa · domena cytoplazmatyczna · DD · FADD · DED · prokaspaza 8 (lub 10) · p20 · p10 · DISC · kaspaza 8 (lub 10) · Apoptosom (szlak wewnętrzny) · mitochondrium · cytochrom c · c · Apaf-1 · WD-40 · CARD · dATP/ATP · prokaspaza 9 · apoptosom · kaspaza 9 · kaspazy wykonawcze 3, 6, 7

NIE RYSUJ: trzech receptorów naraz (trimeru) – tylko jeden receptor, jedno FADD, jedna prokaspaza; nie rysuj apoptosomu jako siedmioramiennego koła – tylko jedno Apaf-1 z jedną prokaspazą 9; bez białek Bid, Bax, Bcl-2, bez jądra komórkowego, bez DAXX, bez Smac/DIABLO i AIF.
```

- **Proponowany podpis:** W każdym panelu czytaj z góry na dół: sygnał → białko adaptorowe → prokaspaza. Porównaj kolory stykających się domen: zawsze łączą się domeny tego samego typu – DD z DD i DED z DED w kompleksie DISC, CARD z CARD w apoptosomie. Wniosek: białko adaptorowe (FADD, Apaf-1) ma dwie różne końcówki – jedną odbiera sygnał, drugą chwyta prokaspazę inicjatorową.
- **Źródło treści:** `#c03-szlaki`, h3 „Szlak zewnętrzny…”: trzy domeny receptora („zewnątrzkomórkową – rozpoznaje ligand; transbłonową – tkwi w błonie; cytoplazmatyczną – z domeną śmierci DD”), kroki 1–5 („Domena DD receptora łączy się z domeną DD na C-końcu białka adaptorowego FADD.”; „Domena DED na N-końcu FADD łączy się z domeną DED prokaspazy 8 lub 10. Powstaje kompleks sygnałowy DISC…”), „DD z DD, DED z DED”. H3 „Szlak wewnętrzny…”, krok „Apoptosom”: „Na N-końcu jest domena CARD, która wiąże prokaspazę 9 (ta również ma domenę CARD). Na C-końcu jest domena powtórzeń WD-40, która wiąże cytochrom c oraz dATP/ATP.” Budowa prokaspaz (dwie DED w 8 i 10, CARD w 9, p20, p10): `#c03-kaspazy`, tabela „Inicjatorowe / Wykonawcze”.

---

### Rycina 4 · Rozdział 4 (Kwasy nukleinowe)

- **Miejsce:** `#c04-replikacja` (h2 „Replikacja: zasada i etapy”), h3 „Jak replikacja unika błędów? Korekta” – po akapicie zaczynającym się od „Polimeraza na bieżąco sprawdza, czy właśnie dołączony nukleotyd…”.
- **id:** `c04-fig-korekta` · **Tytuł:** Korekta: polimeraza cofa się i wycina błąd · **1 łam, 1:1** (w HTML: `class="fig narrow"`)
- **Po co:** student ma zobaczyć, dlaczego korekta biegnie w kierunku 3′→5′: błędny nukleotyd jest zawsze ostatni, na końcu 3′ rosnącej nici, więc polimeraza musi się cofnąć. (Tematy sąsiednie – widełki, nić opóźniona, telomery, topoizomerazy – mają ryciny w banku.)

**Prompt dla ChatGPT:**

```text
RYCINA 4. Format: 1 łam, 1200 × 1200 px (1:1). Trzy poziome pasy jeden pod drugim (kroki 1, 2, 3), rozdzielone cienkimi liniami (#dae5de). W każdym pasie ten sam fragment DNA w tym samym położeniu, żeby łatwo porównać.

ELEMENTY WSPÓLNE DLA KAŻDEGO PASA
- Dolna nić = matryca: poziomy rząd 7 jednakowych kwadratowych klocków (tło #f0f4f1, kontur #9aa59f), bez liter. Z lewej końca napis „3′”, z prawej „5′”.
- Górna nić = nowa nić: rząd klocków leżących dokładnie nad klockami matrycy (tło #8fd3a6, kontur #2b7a4b), bez liter; nowa nić zaczyna się z lewej i rośnie w prawo. Z lewej końca napis „5′”, na prawym (rosnącym) końcu napis „3′”.
- Między klockami obu nici krótkie pionowe kreski (pary zasad).
- Polimeraza: duży półprzezroczysty owal (tło #eef5fb, kontur #4387b7) obejmujący prawy koniec nowej nici.
- Etykiety „matryca” i „nowa nić” tylko w pasie 1 (z lewej strony nici).

PAS 1 – zielone kółko z białą cyfrą „1” i tytuł kroku: „zły nukleotyd na końcu 3′”.
Nowa nić ma 4 zielone klocki i piąty klocek CZERWONY (#c84d42), lekko przekrzywiony i odsunięty od matrycy, bez pionowej kreski parowania. Etykieta ze wskaźnikiem: „błędny nukleotyd”. Etykieta przy owalu: „polimeraza DNA”. Nad nową nicią cienka zielona strzałka w prawo z napisem „synteza 5′→3′”.

PAS 2 – cyfra „2” i tytuł kroku: „polimeraza cofa się i wycina”.
Owal polimerazy przesunięty o jeden klocek w lewo. Czerwony klocek odłączony, uniesiony nad nić i odlatujący w prawo-górę (krótka przerywana linia). Nowa nić ma 4 zielone klocki. Nad nicią czerwona strzałka skierowana W LEWO z napisem „egzonukleaza 3′→5′ (korekta)”.

PAS 3 – cyfra „3” i tytuł kroku: „synteza biegnie dalej”.
Nowa nić ma 5 zielonych klocków (piąty prawidłowy, z kreską parowania) i szósty zielony klocek właśnie dołączany. Owal polimerazy z powrotem na prawym końcu. Etykieta ze wskaźnikiem do piątego klocka: „prawidłowy nukleotyd”. Nad nicią zielona strzałka w prawo z napisem „synteza 5′→3′”.

PEŁNA LISTA ETYKIET (dokładnie tak):
1 · 2 · 3 · zły nukleotyd na końcu 3′ · polimeraza cofa się i wycina · synteza biegnie dalej · matryca · nowa nić · 5′ · 3′ · polimeraza DNA · błędny nukleotyd · prawidłowy nukleotyd · synteza 5′→3′ · egzonukleaza 3′→5′ (korekta)

NIE RYSUJ: liter zasad (A, T, G, C), podwójnej helisy skręconej w spiralę, widełek replikacyjnych, helikazy, starterów, fragmentów Okazaki, żadnych liczb poza numerami kroków.
```

- **Proponowany podpis:** Czytaj z góry na dół. W kroku 1 znajdź czerwony klocek – błędny nukleotyd leży na końcu 3′ nowej nici, bo został dołączony jako ostatni. Porównaj kierunek strzałek w krokach 1 i 2: synteza biegnie 5′→3′, a wycinanie – z powrotem, 3′→5′. Wniosek: polimeraza poprawia błąd, cofając się o jeden nukleotyd, i dopiero potem buduje dalej.
- **Źródło treści:** `#c04-replikacja`, h3 „Jak replikacja unika błędów? Korekta”: „Jeśli wstawiła zły nukleotyd, cofa się i go wycina – to aktywność egzonukleazy 3′→5′, czyli korekta (ang. proofreading). Kierunek się zgadza: nić rośnie 5′→3′, więc ostatni, błędny nukleotyd leży na końcu 3′ i polimeraza usuwa go, cofając się w stronę 5′.”
- **Uwaga:** krok 3 („synteza biegnie dalej”) jest dopowiedzeniem logicznym, nie osobnym zdaniem tekstu – jeśli autor rozdziału woli, można zamówić wersję z dwoma pasami (1–2).

---

### Rycina 5 · Rozdział 5 (PCR)

- **Miejsce:** `#c05-rt` (h2 „Odwrotna transkrypcja i RT-PCR”) – na końcu podrozdziału, po akapicie o usuwaniu genomowego DNA DNazą (w wersji z 18.11 zaczyna się od „W bardzo czułych badaniach przeszkadzają nawet niewielkie ilości genomowego DNA”). W planie v2 odpowiada to punktom „DNaza → jakościowo vs ilościowo”.
- **id:** `c05-fig-rt` · **Tytuł:** RT-PCR: od RNA do produktu PCR · **2 łamy, 3:1**
- **Po co:** student ma odczytać kolejność: RNA → (DNaza usuwa genomowe DNA) → odwrotna transkryptaza → cDNA → PCR, i zrozumieć, że PCR kopiuje już DNA, a nie RNA. (Rycina z trzema rodzajami starterów jest w banku: `k5-ryc-13` – ta jej nie dubluje.)

**Prompt dla ChatGPT:**

```text
RYCINA 5. Format: 2 łamy, 2400 × 800 px (3:1). Jeden poziomy ciąg czterech etapów czytany od lewej do prawej; etapy połączone grubymi zielonymi strzałkami (#2b7a4b). Nad etapami 2–4 dwie poziome klamry opisujące zakres.

KONWENCJA KOLORÓW: RNA – ochra #b77a20 (linia falista); DNA – niebieski #4387b7 (linia prosta); genomowe DNA – szary #9aa59f.

ETAP 1 (zielone kółko z „1”) – w kaflu (#f0f4f1): jedna falista linia w kolorze ochry z etykietą „mRNA” oraz obok krótki szary odcinek podwójnej linii z etykietą „genomowe DNA”. Tytuł pod kaflem: „RNA po izolacji”.

Strzałka 1→2; nad strzałką małe czerwone nożyczki lub czerwony znak „✕” na szarym odcinku i napis „DNaza”.

ETAP 2 (kółko „2”) – w kaflu: ta sama falista linia mRNA w kolorze ochry, już bez szarego DNA. Przy jej prawym końcu krótka niebieska kreska z etykietą „starter”, a przy starterze fioletowy owal (#7867a8, tło #f1eef7) z etykietą „odwrotna transkryptaza”; od startera wzdłuż mRNA biegnie w lewo dobudowywana prosta niebieska linia. Tytuł pod kaflem: „odwrotna transkrypcja (RT)”.

Strzałka 2→3.

ETAP 3 (kółko „3”) – w kaflu: prosta niebieska linia z etykietą „cDNA”. Tytuł pod kaflem: „DNA komplementarne do RNA”.

Strzałka 3→4.

ETAP 4 (kółko „4”) – w kaflu: wiele (ok. 8) krótkich jednakowych niebieskich podwójnych odcinków ułożonych w stos – produkt PCR. Tytuł pod kaflem: „PCR”. Z kafla dwie cienkie strzałki rozwidlające się w prawo do dwóch małych ramek jedna nad drugą:
- górna: „jakościowy PCR – wykrycie transkryptu”
- dolna: „PCR w czasie rzeczywistym – poziom ekspresji genu”

KLAMRY NAD CIĄGIEM: krótsza klamra nad etapami 2–3 z napisem „RT”; dłuższa klamra nad etapami 2–4 z napisem „RT-PCR”.

PEŁNA LISTA ETYKIET (dokładnie tak):
1 · 2 · 3 · 4 · mRNA · genomowe DNA · RNA po izolacji · DNaza · starter · odwrotna transkryptaza · odwrotna transkrypcja (RT) · cDNA · DNA komplementarne do RNA · PCR · jakościowy PCR – wykrycie transkryptu · PCR w czasie rzeczywistym – poziom ekspresji genu · RT · RT-PCR

NIE RYSUJ: probówek, termocyklera, wykresów, trzech rodzajów starterów (oligo(dT), heksamery, GSP), ogona poli(A), czapeczki, wirusów, temperatur ani liczby cykli.
```

- **Proponowany podpis:** Czytaj od lewej: po izolacji w próbce jest mRNA (ochra) i resztki genomowego DNA (szare), które usuwa DNaza. Porównaj kolory w krokach 2 i 3 – odwrotna transkryptaza buduje na RNA nić DNA (niebieską), czyli cDNA. Wniosek: PCR powiela dopiero cDNA, a cały ciąg od odwrotnej transkrypcji do PCR to RT-PCR.
- **Źródło treści:** `#c05-rt`: „Odwrotna transkrypcja (RT…) to przepisanie RNA na komplementarny do niego DNA, czyli cDNA. Wykonuje ją enzym odwrotna transkryptaza… Otrzymane cDNA jest matrycą do PCR, a połączenie obu etapów to RT-PCR.”; „Przepisywana jest sekwencja dojrzałego mRNA – złożona wyłącznie z eksonów.”; „…genomowego DNA; usuwa się je DNazą zaraz po izolacji RNA albo przed odwrotną transkrypcją. cDNA może posłużyć jako matryca w jakościowym PCR – żeby wykryć transkrypt badanego genu – albo w ilościowym PCR w czasie rzeczywistym, który ocenia… poziom ekspresji genu.”

---

### Rycina 6 · Rozdział 6 (Elektroforeza i hybrydyzacja)

- **Miejsce:** `#c06-hybrydyzacja` (h2 „Hybrydyzacja i sondy”), h3 „Jak zobaczyć, gdzie usiadła sonda?” – po akapicie zaczynającym się od „4. Znakowanie enzymatyczne.”, przed tabelą „Co doczepiamy do sondy / Jak widzimy sygnał”.
- **id:** `c06-fig-znakowanie` · **Tytuł:** Cztery sposoby znakowania sondy · **2 łamy, 20:9**
- **Po co:** student ma porównać, co w każdym sposobie jest doczepione do sondy i co ostatecznie widać – i zauważyć, że tylko w znakowaniu immunochemicznym między sondą a sygnałem stoi przeciwciało („kanapka”).

**Prompt dla ChatGPT:**

```text
RYCINA 6. Format: 2 łamy, 2400 × 1080 px (20:9). Cztery jednakowe pionowe kolumny (panele A, B, C, D) obok siebie, rozdzielone cienkimi liniami (#dae5de). Każdą kolumnę czyta się od dołu do góry, a wszystkie cztery porównuje się w poziomie – dlatego te same elementy muszą leżeć na tej samej wysokości we wszystkich kolumnach.

ELEMENTY WSPÓLNE W KAŻDEJ KOLUMNIE (od dołu):
- poziomy szary pas (#f0f4f1, kontur #9aa59f) – membrana; na nim pozioma niebieska linia (#4387b7) – badane DNA;
- nad nią krótsza zielona linia (#2b7a4b) sparowana z fragmentem niebieskiej (krótkie pionowe kreski między nimi) – sonda;
- nad sondą: znacznik (inny w każdej kolumnie);
- na samej górze kolumny, w zaokrąglonej ramce (tło #e7f2ea): napis „co widać”.
Etykiety „badane DNA” i „sonda” tylko w kolumnie A.

KOLUMNA A – tytuł: „radioaktywne”
Na sondzie mały złoty symbol (#e3b23c): kółko z trzema krótkimi promieniami. Etykieta: „nukleotyd z izotopem”. Od znacznika faliste linie w górę do ciemnoszarego prostokąta z czarną plamą. Ramka u góry: „klisza ciemnieje – autoradiografia”.

KOLUMNA B – tytuł: „fluorescencyjne”
Na sondzie gwiazdka (ochra #b77a20). Etykieta: „fluorochrom”. Od gwiazdki krótkie promienie. Ramka u góry: „świecenie w mikroskopie fluorescencyjnym”.

KOLUMNA C – tytuł: „immunochemiczne”
Na sondzie mały fioletowy trójkąt (#7867a8). Etykieta: „hapten”. Nad nim przeciwciało w kształcie odwróconej litery Y (kontur #173d2b): dwa ramiona skierowane w dół obejmują trójkąt haptenu, trzonek skierowany do góry. Etykieta: „przeciwciało”. Na górnym końcu trzonka czerwonawy sześciokąt (kontur #c84d42, tło #fff0ec). Etykieta: „enzym, barwnik fluorescencyjny lub koloidalne złoto”. Ramka u góry: „sygnał daje dopiero przeciwciało”.

KOLUMNA D – tytuł: „enzymatyczne”
Bezpośrednio na sondzie czerwonawy sześciokąt (taki sam jak w kolumnie C). Etykieta: „enzym”. Obok małe białe kółko z etykietą „substrat”, strzałka do pełnego fioletowego kółka z etykietą „barwny produkt”. Ramka u góry: „reakcja barwna w miejscu sondy”.

PEŁNA LISTA ETYKIET (dokładnie tak):
radioaktywne · fluorescencyjne · immunochemiczne · enzymatyczne · badane DNA · sonda · nukleotyd z izotopem · klisza ciemnieje – autoradiografia · fluorochrom · świecenie w mikroskopie fluorescencyjnym · hapten · przeciwciało · enzym, barwnik fluorescencyjny lub koloidalne złoto · sygnał daje dopiero przeciwciało · enzym · substrat · barwny produkt · reakcja barwna w miejscu sondy

NIE RYSUJ: mikroskopu, kasety, żelu, studzienek, drugiego przeciwciała, awidyny/streptawidyny, nazw konkretnych barwników i enzymów (rodamina, peroksydaza itp. – są w tekście, nie na rycinie), żadnych dodatkowych kroków.
```

- **Proponowany podpis:** W każdej kolumnie czytaj od dołu: badane DNA na membranie, sparowana z nim sonda, znacznik i – u góry – to, co widać. Porównaj kolumny C i D: w obu sygnał może dawać enzym, ale w C niesie go przeciwciało rozpoznające hapten, a w D enzym siedzi wprost na sondzie. Wniosek: znakowanie immunochemiczne jest dwustopniowe – sam hapten nie jest tym, co widzimy.
- **Źródło treści:** `#c06-hybrydyzacja`, h3 „Jak zobaczyć, gdzie usiadła sonda?”: punkty 1–4 („Do sondy wbudowuje się nukleotyd zawierający izotop promieniotwórczy… klisza ciemnieje. To autoradiografia.”; „Do sondy przyłącza się fluorochrom… Sygnał ogląda się w mikroskopie fluorescencyjnym.”; „…hapten… Dopiero przeciwciało niesie coś widocznego: enzym (fosfatazę alkaliczną lub peroksydazę), barwnik fluorescencyjny albo koloidalne złoto. Powstaje »kanapka«: badane DNA – sonda – hapten – przeciwciało – coś, co widać.”; „Enzym przyczepia się bezpośrednio do sondy… dodaje się substrat, a enzym zamienia go w barwny produkt.”) oraz tabela pod spodem.

---

### Rycina 7 · Rozdział 7 (Komórki macierzyste)

- **Miejsce:** `#c07-typy` (h2 „Cztery typy komórek macierzystych”), h3 „Indukowane pluripotencjalne komórki macierzyste (iPSC) – cofnięcie różnicowania” – po liście pięciu kroków, przed akapitem zaczynającym się od „Zalety iPSC wynikają z ich pochodzenia.”
- **id:** `c07-fig-ipsc` · **Tytuł:** Jak powstają iPSC · **2 łamy, 8:3**
- **Po co:** student ma odczytać pięć kroków w kolejności i zobaczyć dwa przeciwne kierunki: najpierw odróżnicowanie (krok 4), potem różnicowanie w wybranym kierunku (krok 5) – oraz to, że komórki wracają do tego samego pacjenta.

**Prompt dla ChatGPT:**

```text
RYCINA 7. Format: 2 łamy, 2400 × 900 px (8:3). Jeden poziomy ciąg pięciu kroków czytany od lewej do prawej, połączonych grubymi zielonymi strzałkami (#2b7a4b). Każdy krok: zielone kółko z białą cyfrą u góry, pod nim prosty piktogram, pod piktogramem tytuł kroku. Pod całym ciągiem jedna długa przerywana strzałka wracająca od prawej do lewej.

KROK 1 – piktogram: prosta sylwetka człowieka (popiersie, kontur #173d2b, bez rysów twarzy) i obok mały fragment tkanki (3–4 sklejone wielokątne komórki, tło #f0f4f1). Tytuł: „pobranie tkanki od pacjenta”.

KROK 2 – piktogram: płaska butelka hodowlana widziana z boku (kontur #173d2b) z kilkunastoma wydłużonymi komórkami na dnie (ochra #b77a20, tło #fbf3e5). Tytuł: „namnożenie komórek w butelce hodowlanej”.

KROK 3 – piktogram: jedna duża wydłużona komórka (ochra) z jądrem; do niej zbliża się mały sześciokąt (fiolet #7867a8) z etykietą „wirus”. Obok w ramce (tło #f1eef7, kontur #7867a8) cztery nazwy jedna pod drugą: „OCT4/3”, „SOX2”, „KLF4”, „c-MYC”. Tytuł: „transfekcja wirusem: nadekspresja czterech czynników transkrypcyjnych”.

KROK 4 – piktogram: zwarta grupa 6–7 małych okrągłych komórek (jasna zieleń #8fd3a6, kontur #2b7a4b) z dużymi jądrami. Etykieta przy grupie: „iPSC (pluripotencjalne)”. Tytuł: „odróżnicowanie”.

KROK 5 – z grupy iPSC trzy cienkie zielone strzałki rozchodzące się w prawo do trzech małych piktogramów ułożonych pionowo: (a) komórka z rozgałęzieniami i jednym długim wypustkiem – etykieta „neurony”; (b) dwa okrągłe krążki (czerwonawe, kontur #c84d42) – etykieta „komórki krwi”; (c) rząd trzech sześciennych komórek stojących obok siebie – etykieta „nabłonki”. Nad rozwidleniem napis „czynniki wzrostu”. Tytuł: „różnicowanie w wybranym kierunku”.

STRZAŁKA POWROTNA: pod ciągiem, od kroku 5 do sylwetki pacjenta w kroku 1, szara przerywana strzałka (#5f6b64) z napisem na środku: „komórki autogeniczne – dla tego samego pacjenta”.

PEŁNA LISTA ETYKIET (dokładnie tak):
1 · 2 · 3 · 4 · 5 · pobranie tkanki od pacjenta · namnożenie komórek w butelce hodowlanej · wirus · OCT4/3 · SOX2 · KLF4 · c-MYC · transfekcja wirusem: nadekspresja czterech czynników transkrypcyjnych · iPSC (pluripotencjalne) · odróżnicowanie · czynniki wzrostu · neurony · komórki krwi · nabłonki · różnicowanie w wybranym kierunku · komórki autogeniczne – dla tego samego pacjenta

NIE RYSUJ: zarodka ani blastocysty, strzykawek, skalpela, myszy, DNA, szczegółów anatomicznych twarzy, nazw konkretnych czynników wzrostu, żadnych dodatkowych typów komórek.
```

- **Proponowany podpis:** Czytaj od lewej, zgodnie z numerami 1–5. Porównaj kroki 4 i 5: najpierw komórka cofa się do stanu pluripotencjalnego (odróżnicowanie po nadekspresji OCT4/3, SOX2, KLF4 i c-MYC), a dopiero potem czynniki wzrostu kierują ją w wybrany typ komórek. Wniosek: iPSC powstają bez zarodka i wracają do tego samego pacjenta jako komórki autogeniczne.
- **Źródło treści:** `#c07-typy`, h3 o iPSC: „Klasycznie do wywołania pluripotencji trzeba zwiększyć ekspresję czterech czynników transkrypcyjnych: OCT4/3, SOX2, KLF4 i c-MYC.” + lista kroków 1–5 („Pobranie tkanki od pacjenta.” … „Różnicowanie w wybranym kierunku – odpowiednie czynniki wzrostu kierują je w konkretny typ tkanki, np. w neurony, komórki krwi albo nabłonki.”); h3 „Od kogo pochodzą komórki…”: „iPSC wytworzone z komórek samego pacjenta – autogenicznymi”.

---

### Rycina 8 · Rozdział 8 (Dziedziczenie)

- **Miejsce:** `#c08-mito` (h2 „Dziedziczenie mitochondrialne”), h3 „Dlaczego najciężej choruje układ nerwowy? Próg energetyczny” – po akapicie zaczynającym się od „Każda tkanka potrzebuje określonej ilości ATP.”
- **id:** `c08-fig-heteroplazmia` · **Tytuł:** Heteroplazmia i próg energetyczny · **2 łamy, 20:9**
- **Po co:** student ma połączyć dwa pojęcia, które tekst wyjaśnia osobno: (A) losowy rozdział cząsteczek mtDNA zmienia odsetek zmutowanych w komórkach potomnych, (B) ta sama komórka może być powyżej progu jednej tkanki i poniżej progu innej. Stąd zmienne objawy tej samej mutacji.

**Prompt dla ChatGPT:**

```text
RYCINA 8. Format: 2 łamy, 2400 × 1080 px (20:9). Dwa panele obok siebie: A z lewej (ok. 55% szerokości), B z prawej (ok. 45%), rozdzielone cienką pionową linią (#dae5de).

KONWENCJA: komórka = duży okrąg (kontur #173d2b, tło białe). Cząsteczka mtDNA = mały pierścień (pusty w środku okrąg o grubym konturze). Prawidłowe mtDNA – pierścień zielony #2b7a4b. Zmutowane mtDNA – pierścień czerwony #c84d42. Pierścienie rozrzucone luźno wewnątrz komórki, nie nakładają się. Nie rysuj jądra ani mitochondriów-fasolek.

PANEL A – tytuł: „Segregacja replikacyjna”
Czytany od góry do dołu, drzewko podziałów.
- U góry na środku jedna komórka wyjściowa: w środku 8 pierścieni – 4 zielone i 4 czerwone, wymieszane. Etykieta obok: „komórka z heteroplazmią”.
- Od niej dwie zielone strzałki w dół do dwóch komórek potomnych. Przy strzałkach napis: „podział – losowy przydział mtDNA”.
- Lewa komórka potomna: wyraźna przewaga zielonych (6 zielonych, 2 czerwone). Pod nią etykieta: „mało zmutowanych”.
- Prawa komórka potomna: wyraźna przewaga czerwonych (2 zielone, 6 czerwonych). Pod nią etykieta: „dużo zmutowanych”.
(Dokładna liczba pierścieni nie jest najważniejsza – ważne, żeby przewaga jednego koloru była widoczna od razu.)
- W lewym dolnym rogu panelu legenda: zielony pierścień + „prawidłowe mtDNA”, czerwony pierścień + „zmutowane mtDNA”.

PANEL B – tytuł: „Ta sama komórka, dwa progi”
Dwa jednakowe pionowe słupki obok siebie, stojące na wspólnej poziomej linii podstawy. Z lewej strony pionowa oś ze strzałką w górę i napisem „wytwarzanie ATP”. Oba słupki mają TĘ SAMĄ wysokość (ok. połowy wysokości panelu) i ten sam kolor (ochra #b77a20, tło #fbf3e5) – pokazują tę samą komórkę z tym samym odsetkiem zmutowanego mtDNA.
- Przez lewy słupek pozioma przerywana linia „próg” NISKO (na ok. 1/3 wysokości słupka) – słupek sięga ponad próg. Pod słupkiem: „tkanka o niższym progu”. Nad słupkiem w zielonej ramce (#e7f2ea): „bez objawów”.
- Przez prawy słupek pozioma przerywana czerwona linia „próg” WYSOKO (wyraźnie powyżej wierzchołka słupka) – słupek nie sięga progu. Pod słupkiem: „tkanka o wysokim progu, np. ośrodkowy układ nerwowy”. Nad linią progu w czerwonawej ramce (#fff0ec, kontur #c84d42): „komórki degenerują i obumierają”.
Przy każdej przerywanej linii napis „próg”.

PEŁNA LISTA ETYKIET (dokładnie tak):
Segregacja replikacyjna · komórka z heteroplazmią · podział – losowy przydział mtDNA · mało zmutowanych · dużo zmutowanych · prawidłowe mtDNA · zmutowane mtDNA · Ta sama komórka, dwa progi · wytwarzanie ATP · próg · tkanka o niższym progu · bez objawów · tkanka o wysokim progu, np. ośrodkowy układ nerwowy · komórki degenerują i obumierają

NIE RYSUJ: jądra komórkowego, mitochondriów w kształcie fasolki z grzebieniami, rodowodu, plemnika i komórki jajowej, liczb, procentów ani skali na osi, nazw chorób.
```

- **Proponowany podpis:** A – zacznij od komórki u góry: ma tyle samo prawidłowych (zielone) i zmutowanych (czerwone) cząsteczek mtDNA. Porównaj komórki potomne – po losowym rozdziale jedna ma mało, druga dużo zmutowanych. B – oba słupki to ta sama komórka; różni się tylko wysokość progu tkanki. Wniosek: ta sama mutacja może dać objawy w ośrodkowym układzie nerwowym, a w innej tkance – nie.
- **Źródło treści:** `#c08-mito`, h3 „Dlaczego objawy są tak różne? Heteroplazmia”: definicja („obecność w jednej komórce zarówno zmutowanych, jak i prawidłowych cząsteczek mtDNA; im większy odsetek zmutowanych cząsteczek, tym cięższa choroba”), „Zmienia się przez segregację replikacyjną podczas podziałów komórek i mitochondriów – losowo albo przez selekcję”, ramka „Obraz w głowie” (losowa garść kulek); h3 „Próg energetyczny”: „Gdy wytwarzanie ATP spadnie poniżej progu, komórki degenerują i obumierają. Najciężej chorują więc narządy o dużym zapotrzebowaniu na ATP i wysokim progu, np. ośrodkowy układ nerwowy. Ta sama mutacja może zatem dać objawy w jednym narządzie, a w innym – nie.”
- **Uwaga:** „tkanka o niższym progu” i „bez objawów” to dopełnienie ostatniego cytowanego zdania („w innym – nie”), nie osobny termin źródła.

---

### Rycina 9 · Rozdział 9 (Cytogenetyka)

- **Miejsce:** `#c09-aberracje` (h2 „Katalog aberracji i ich zapis”), h3 „Aberracje strukturalne: katalog zapisów” – po tabeli zapisów, przed akapitem zaczynającym się od „W kariotypie człowieka najczęściej stwierdza się izochromosom ramion długich chromosomu X”.
- **id:** `c09-fig-strukturalne` · **Tytuł:** Aberracje strukturalne – przed i po · **2 łamy, 20:9**
- **Po co:** tabela podaje zapisy, a istniejące ryciny pokazują tylko delecję interstycjalną i translokację wzajemną. Student ma zobaczyć, jak wygląda chromosom przed i po w sześciu pozostałych, najczęściej pytanych typach – zwłaszcza różnicę między inwersją para- i pericentryczną (czy odwrócony odcinek obejmuje centromer).

**Prompt dla ChatGPT:**

```text
RYCINA 9. Format: 2 łamy, 2400 × 1080 px (20:9). Sześć jednakowych paneli w siatce 3 kolumny × 2 rzędy (A, B, C w górnym rzędzie; D, E, F w dolnym), rozdzielonych cienkimi liniami (#dae5de). Każdy panel ma tę samą budowę: u góry tytuł (pogrubiony) i pod nim zapis kariotypu (krój o stałej szerokości znaków, mniejszy), niżej z lewej chromosom „przed”, zielona strzałka w prawo (#2b7a4b), z prawej chromosom „po”.

KONWENCJA CHROMOSOMU (ważna – identyczna we wszystkich panelach):
Chromosom to pionowy, wąski pasek o zaokrąglonych końcach (kontur #173d2b), z przewężeniem i małym ciemnym kółkiem (#173d2b) w miejscu centromeru. Ramię krótkie u góry (krótsze), ramię długie u dołu (dłuższe). Przy chromosomie „przed” w panelu A małe litery „p” (przy ramieniu górnym) i „q” (przy dolnym) oraz etykieta „centromer”. Pasek jest podzielony na kolorowe odcinki; odcinek, którego dotyczy zmiana, ma w środku białą strzałkę skierowaną w dół (pokazuje jego orientację). Miejsca pęknięć zaznacz krótkimi czerwonymi poprzecznymi kreskami (#c84d42) z etykietami prążków.
Kolory odcinków: tło chromosomu #f0f4f1; odcinek wyróżniony – ochra #b77a20; drugi chromosom w panelu F – niebieski #4387b7.

PANEL A – tytuł: „Inwersja paracentryczna”; zapis: „46,XX,inv(3)(q21q26)”
Przed: odcinek w ramieniu długim, między kreskami „q21” i „q26”, w kolorze ochry z białą strzałką w dół. Po: ten sam odcinek w tym samym miejscu, ale strzałka w GÓRĘ (odwrócony o 180°). Centromer poza odcinkiem. Pod panelem krótka etykieta: „bez centromeru”.

PANEL B – tytuł: „Inwersja pericentryczna”; zapis: „46,XX,inv(3)(p13q21)”
Przed: odcinek w kolorze ochry rozciąga się od kreski „p13” w ramieniu krótkim do kreski „q21” w ramieniu długim – obejmuje centromer; biała strzałka w dół. Po: ten sam odcinek odwrócony (strzałka w górę); ponieważ odcinek powyżej centromeru był krótszy niż poniżej, po odwróceniu centromer leży w innym miejscu odcinka (przesunięty ku dołowi). Pod panelem etykieta: „obejmuje centromer”.

PANEL C – tytuł: „Duplikacja”; zapis: „46,XX,dup(1)(q22q25)”
Przed: w ramieniu długim odcinek w kolorze ochry między kreskami „q22” i „q25”, strzałka w dół. Po: chromosom dłuższy – dwa takie same odcinki w kolorze ochry jeden pod drugim, oba ze strzałką w dół. Pod panelem etykieta: „odcinek podwojony”.

PANEL D – tytuł: „Izochromosom”; zapis: „46,X,i(X)(q10)”
Przed: chromosom X z ramieniem krótkim w kolorze szarym (#9aa59f) i ramieniem długim w kolorze ochry; przez centromer pozioma czerwona przerywana kreska z etykietą „q10”. Po: chromosom symetryczny – nad centromerem i pod centromerem takie samo ramię długie w kolorze ochry (lustrzane odbicie), brak ramienia szarego. Pod panelem etykieta: „dwa ramiona długie”.

PANEL E – tytuł: „Chromosom pierścieniowy”; zapis: „46,XX,r(7)(p22q36)”
Przed: kreski pęknięć blisko obu końców: „p22” u góry i „q36” u dołu; dwa małe końcowe odcinki poza kreskami w kolorze szarym (#9aa59f), środek w kolorze ochry. Po: zamknięty pierścień (obwarzanek) w kolorze ochry z centromerem (ciemne kółko) na obwodzie; obok dwa małe szare odcinki z etykietą „utracone”. Pod panelem etykieta: „końce połączone”.

PANEL F – tytuł: „Translokacja robertsonowska”; zapis: „45,XX,der(13;21)(q10;q10)”
Przed: dwa chromosomy akrocentryczne obok siebie (centromer bardzo blisko górnego końca, ramię krótkie bardzo małe): większy w kolorze ochry z podpisem „13” i mniejszy niebieski z podpisem „21”. Przy centromerze każdego czerwona kreska „q10”. Po: jeden chromosom pochodny – ramię długie chromosomu 13 (ochra) u góry i ramię długie chromosomu 21 (niebieskie) u dołu, połączone przy centromerze; obok dwa malutkie ramiona krótkie (ochra i niebieskie) z etykietą „utracone”. Podpis chromosomu pochodnego: „der(13;21)”. Pod panelem etykieta: „połączone ramiona długie”.

PEŁNA LISTA ETYKIET (dokładnie tak):
Inwersja paracentryczna · 46,XX,inv(3)(q21q26) · p · q · centromer · q21 · q26 · bez centromeru · Inwersja pericentryczna · 46,XX,inv(3)(p13q21) · p13 · obejmuje centromer · Duplikacja · 46,XX,dup(1)(q22q25) · q22 · q25 · odcinek podwojony · Izochromosom · 46,X,i(X)(q10) · q10 · dwa ramiona długie · Chromosom pierścieniowy · 46,XX,r(7)(p22q36) · p22 · q36 · utracone · końce połączone · Translokacja robertsonowska · 45,XX,der(13;21)(q10;q10) · 13 · 21 · der(13;21) · połączone ramiona długie

NIE RYSUJ: wzoru prążków G (poprzecznych pasków) na chromosomach, chromatyd siostrzanych (chromosomy jako pojedyncze paski, nie w kształcie X), delecji, translokacji wzajemnej, insercji, chromosomu dicentrycznego ani markerowego, jąder komórkowych, nazw zespołów chorobowych. Zapisy kariotypów przepisz znak po znaku – z przecinkami, nawiasami i średnikiem, bez spacji.
```

- **Proponowany podpis:** W każdym panelu porównaj chromosom po lewej (przed) z chromosomem po prawej (po); czerwone kreski to punkty pęknięć z zapisu nad rysunkiem, a biała strzałka pokazuje orientację odcinka. Zestaw panele A i B: w obu odcinek jest odwrócony o 180°, ale tylko w B obejmuje centromer. Wniosek: zapis podaje punkty pęknięć, a rodzaj aberracji mówi, co stało się z odcinkiem między nimi – odwrócenie, podwojenie, zamknięcie w pierścień albo połączenie ramion.
- **Źródło treści:** `#c09-aberracje`, tabela w h3 „Aberracje strukturalne: katalog zapisów” – wiersze: „Inwersja paracentryczna (inv) 46,XX,inv(3)(q21q26) – odwrócenie o 180° fragmentu między prążkami q21 i q26 – w obrębie ramienia długiego, bez centromeru”; „Inwersja pericentryczna 46,XX,inv(3)(p13q21) – … obejmuje centromer”; „Duplikacja (dup) 46,XX,dup(1)(q22q25) – bezpośrednie podwojenie fragmentu…”; „Izochromosom (i) 46,X,i(X)(q10) – chromosom złożony z dwóch identycznych ramion… (tu: długich X)”; „Chromosom pierścieniowy (r) 46,XX,r(7)(p22q36) – pęknięcia w p22 i q36 i połączenie złamanych końców; fragmenty dystalne od pęknięć ulegają delecji”; „Translokacja robertsonowska zrównoważona (der) 45,XX,der(13;21)(q10;q10) – … połączenie ich ramion długich i utrata ramion krótkich”.

---

### Rycina 10 · Rozdział 10 (Płeć) – pierwsza z dwóch

- **Miejsce:** `#c10-lyon` (h2 „Teoria Lyon – hipoteza powstawania chromatyny X”), h3 „Jak komórka wyłącza cały chromosom? Mechanizm molekularny” – po akapicie zaczynającym się od „Co ją utrzymuje – metylacja DNA.”
- **id:** `c10-fig-xist` · **Tytuł:** Inaktywacja X: XIC, XIST, metylacja · **2 łamy, 8:3**
- **Po co:** istniejąca rycina Lyon pokazuje skutek na poziomie komórek (mozaika, ciałka Barra). Tu student ma odczytać trzy kroki molekularne na jednym chromosomie – gdzie proces się zaczyna, co się rozprzestrzenia, co utrzymuje stan – i „paradoks”: XIST pracuje tylko na chromosomie wyłączonym.

**Prompt dla ChatGPT:**

```text
RYCINA 10. Format: 2 łamy, 2400 × 900 px (8:3). Cztery chromosomy X narysowane POZIOMO, jeden pod drugim lub w układzie: z lewej jeden (porównawczy), z prawej trzy w kolejnych krokach. Zalecany układ: lewa kolumna (ok. 25% szerokości) – „aktywny X”; prawa część (ok. 75%) – „nieaktywny X” w trzech krokach od lewej do prawej, połączonych zielonymi strzałkami (#2b7a4b). Między lewą kolumną a prawą częścią cienka pionowa linia (#dae5de).

KONWENCJA CHROMOSOMU: poziomy pasek o zaokrąglonych końcach (kontur #173d2b), z przewężeniem centromeru bliżej lewego końca. Na pasku 6 małych prostokątów – geny – rozmieszczonych równo wzdłuż chromosomu. W ramieniu długim, niedaleko centromeru, jeden wyróżniony prostokąt – gen XIST – w kolorze fioletowym (#7867a8). Gen aktywny: zielony (#2b7a4b) z małą zagiętą strzałką transkrypcji nad nim. Gen wyłączony: szary (#9aa59f), bez strzałki.

LEWA KOLUMNA – nagłówek: „aktywny X”
Jeden chromosom: wszystkie 6 genów zielonych ze strzałkami transkrypcji; gen XIST fioletowy, ale wyblakły (jasny fiolet #f1eef7 z konturem #7867a8), bez strzałki. Etykieta pod genem XIST: „XIST nie ulega transkrypcji”. Etykieta pod chromosomem: „geny pracują”.

PRAWA CZĘŚĆ – nagłówek: „nieaktywny X”
Krok 1 (zielone kółko z „1”) – tytuł: „gdzie się zaczyna”
Chromosom jak wyżej, geny jeszcze zielone. Wokół genu XIST fioletowa ramka-nawias z etykietą „XIC (Xq13) – centrum inaktywacji”. Nad genem XIST zagięta strzałka transkrypcji i krótka falista fioletowa linia z etykietą „RNA XIST”.

Krok 2 (kółko „2”) – tytuł: „co ją uruchamia”
Ten sam chromosom pokryty wieloma krótkimi falistymi fioletowymi liniami wzdłuż całej długości; od genu XIST dwie fioletowe strzałki w lewo i w prawo wzdłuż chromosomu. Geny szare, bez strzałek. Etykieta: „RNA XIST rozprzestrzenia się wzdłuż chromosomu”.

Krok 3 (kółko „3”) – tytuł: „co ją utrzymuje”
Ten sam chromosom, geny szare; nad każdym genem mały czerwony „lizak” (pionowa kreska zakończona pełnym kółkiem, #c84d42). Etykieta przy lizakach: „metylacja cytozyn (wyspy CpG)”. Etykieta pod chromosomem: „zahamowanie transkrypcji”. Gen XIST nadal intensywnie fioletowy ze strzałką transkrypcji, etykieta: „XIST ulega transkrypcji”.

PEŁNA LISTA ETYKIET (dokładnie tak):
aktywny X · XIST nie ulega transkrypcji · geny pracują · nieaktywny X · 1 · 2 · 3 · gdzie się zaczyna · XIC (Xq13) – centrum inaktywacji · RNA XIST · co ją uruchamia · RNA XIST rozprzestrzenia się wzdłuż chromosomu · co ją utrzymuje · metylacja cytozyn (wyspy CpG) · zahamowanie transkrypcji · XIST ulega transkrypcji

NIE RYSUJ: ciałka Barra, jądra komórkowego, komórek, histonów i nukleosomów, białek, chromosomu Y, genów TSIX ani żadnych nazw genów poza XIST, wzoru prążków, chromatyd siostrzanych (chromosom jako pojedynczy pasek).
```

- **Proponowany podpis:** Zacznij od prawej części i idź po numerach: w centrum inaktywacji XIC (Xq13) rusza transkrypcja genu XIST (1), jego RNA rozprzestrzenia się wzdłuż chromosomu i wyłącza geny (2), a metylacja cytozyn utrwala ten stan (3). Porównaj z aktywnym X po lewej: tam XIST milczy, a pozostałe geny pracują. Wniosek: XIST działa jak sygnał „wyłącz” dla tego chromosomu, na którym sam ulega transkrypcji.
- **Źródło treści:** `#c10-lyon`, h3 „Jak komórka wyłącza cały chromosom? Mechanizm molekularny”: „zlokalizowania w prążku Xq13 centrum inaktywacji – XIC, miejsca, w którym proces jest inicjowany”; „XIST nie koduje białka. Jego produktem jest RNA, który rozprzestrzenia się wzdłuż chromosomu i powoduje jego inaktywację.”; „XIST ulega transkrypcji w chromosomie nieaktywnym, a w aktywnym – nie.”; „zmiana wzoru metylacji cytozyn… skutkiem tego jest zahamowanie transkrypcji – gen po genie… zależy częściowo od metylacji tzw. wysp CpG… To metylacja odpowiada za utrzymanie chromosomu X w stanie nieaktywnym.” Tytuły kroków = śródtytuły akapitów („Gdzie się zaczyna”, „Co ją uruchamia”, „Co ją utrzymuje”).

---

### Rycina 11 · Rozdział 10 (Płeć) – druga z dwóch

- **Miejsce:** `#c10-sprzezone` (h2 „Dziedziczenie sprzężone z płcią”), h3 „Zespół kruchego chromosomu X – gdy proste reguły nie wystarczają” – po akapicie zaczynającym się od „Teraz paradoks znika.”
- **id:** `c10-fig-fmr1` · **Tytuł:** Paradoks Shermana: od premutacji do pełnej mutacji · **1 łam, 1:1** (w HTML: `class="fig narrow"`)
- **Po co:** student ma zobaczyć obok siebie rodowód i długość powtórzenia CGG w trzech pokoleniach – i odczytać, że powtórzenie powiększa się dopiero przy przekazaniu przez matkę. To wyjaśnia „zdrowego mężczyznę przekazującego chorobę”.

**Prompt dla ChatGPT:**

```text
RYCINA 11. Format: 1 łam, 1200 × 1200 px (1:1). Trzy poziome wiersze jeden pod drugim – trzy pokolenia rodziny. Z lewej strony każdego wiersza rzymska cyfra pokolenia (I, II, III), dalej symbol rodowodowy osoby z podpisem, a po prawej – schemat genu FMR1 tej osoby. Symbole trzech osób połączone pionową linią pochodzenia (jak w rodowodzie), biegnącą z góry na dół.

SYMBOLE RODOWODOWE (konwencja podręcznika): kwadrat – mężczyzna, koło – kobieta; symbol pusty z kropką w środku – nosiciel/nosicielka bez objawów; symbol całkowicie wypełniony (#173d2b) – osoba chora. Kontur #173d2b.

SCHEMAT GENU (po prawej, w każdym wierszu w tym samym położeniu): poziomy szary pasek (#f0f4f1, kontur #9aa59f) z podpisem „gen FMR1” (podpis tylko w wierszu I). Na lewym końcu paska kolorowy blok powtórzeń z napisem „CGG” w środku (lub obok, jeśli się nie mieści). Lewe krawędzie bloków we wszystkich wierszach wyrównane w pionie, żeby długości dało się porównać.

WIERSZ I: kwadrat pusty z kropką. Podpis: „dziadek – zdrowy”. Blok CGG średniej długości, w kolorze ochry (#b77a20). Etykieta nad blokiem: „premutacja”.

Między wierszem I a II, przy linii pochodzenia, mała etykieta ze strzałką w dół: „ojciec → córka: bez powiększenia”.

WIERSZ II: koło puste z kropką. Podpis: „córka – bez objawów”. Blok CGG tej samej długości co w wierszu I, ochra. Etykieta nad blokiem: „premutacja”.

Między wierszem II a III, przy linii pochodzenia, mała etykieta ze strzałką w dół: „matka → dziecko: powiększenie”.

WIERSZ III: kwadrat całkowicie wypełniony. Podpis: „wnuk – chory”. Blok CGG około 3 razy dłuższy niż w wierszach I i II, w kolorze czerwonym (#c84d42); nad blokiem rząd 5–6 małych „lizaków” (pionowa kreska z pełnym kółkiem, #173d2b). Etykieta nad blokiem: „pełna mutacja”. Etykieta przy lizakach: „silna metylacja”. Na prawym końcu paska genu przekreślona zagięta strzałka transkrypcji i etykieta: „brak mRNA FMR1”.

PEŁNA LISTA ETYKIET (dokładnie tak):
I · II · III · dziadek – zdrowy · córka – bez objawów · wnuk – chory · gen FMR1 · CGG · premutacja · pełna mutacja · ojciec → córka: bez powiększenia · matka → dziecko: powiększenie · silna metylacja · brak mRNA FMR1

NIE RYSUJ: liczb powtórzeń (żadnych wartości liczbowych), chromosomu X z „kruchym miejscem”, partnerów (babci, męża córki), rodzeństwa, twarzy ani sylwetek ludzi, sekwencji DNA literami innymi niż napis „CGG”.
```

- **Proponowany podpis:** Czytaj z góry na dół, pokolenie po pokoleniu, i porównuj długość bloku CGG po prawej. Między dziadkiem a córką blok się nie zmienia (premutacja, oboje bez objawów); wydłuża się dopiero, gdy gen przekazuje matka – u wnuka jest to pełna mutacja, zmetylowana i bez mRNA FMR1. Wniosek: o chorobie decyduje nie samo odziedziczenie genu, lecz to, przez którego rodzica przeszedł.
- **Źródło treści:** `#c10-sprzezone`, h3 „Zespół kruchego chromosomu X…”: „W jego nieulegającym translacji rejonie leży powtórzenie trójnukleotydu CGG”; „zdrowi męscy nosiciele i ich córki mają premutację – pośrednią liczbę powtórzeń”; „gdy córka przekazuje gen swoim dzieciom, premutacja często powiększa się do pełnej mutacji; przy przekazaniu z ojca na córkę takie powiększenie nie zachodzi”; „w pełnej mutacji powtórzenie CGG jest silnie zmetylowane, a w komórkach nie ma mRNA FMR1”; akapit „Teraz paradoks znika. Dziadek ma premutację i jest zdrowy. Córce przekazuje ją bez powiększenia… wnuk choruje.”
- **Uwaga:** tekst mówi „często powiększa się” – podpis i etykieta pokazują przypadek, w którym do powiększenia doszło; liczb powtórzeń w tekście nie ma, więc nie ma ich na rycinie.

---

### Rycina 12 · Rozdział 11 (Biotechnologia)

- **Miejsce:** `#c11-kierunki` (h2 „Kierunki terapii genowej”), h3 „Nowotwory – cztery różne pomysły” – po akapicie zaczynającym się od „Geny samobójcze – molekularna chemioterapia.”
- **id:** `c11-fig-samobojcze` · **Tytuł:** Gen samobójczy i efekt sąsiedztwa · **2 łamy, 20:9**
- **Po co:** student ma zobaczyć, dlaczego lek zabija tylko w guzie (prolek staje się toksyczny wyłącznie w komórce z transgenem) i dlaczego nie trzeba trafić transgenem do każdej komórki (toksyczne produkty przenikają do sąsiadek).

**Prompt dla ChatGPT:**

```text
RYCINA 12. Format: 2 łamy, 2400 × 1080 px (20:9). Dwa panele obok siebie: A z lewej (ok. 62% szerokości) – guz; B z prawej (ok. 38%) – prawidłowa tkanka. Rozdzielone cienką pionową linią (#dae5de). U góry przez oba panele biegnie poziomy pas naczynia krwionośnego.

GÓRNY PAS (wspólny): poziomy pas o jasnoczerwonym tle (#fff0ec) z konturem #c84d42, wysokości ok. 15% ryciny; z lewej etykieta „krwiobieg”. W pasie kilka małych pustych trójkątów (białe wypełnienie, kontur ochra #b77a20) – cząsteczki proleku; etykieta: „nietoksyczny prolek (np. gancyklowir)”. Z pasa w dół, do obu paneli, po kilka cienkich strzałek w kolorze ochry pokazujących, że prolek dociera do wszystkich komórek.

KONWENCJA KOMÓREK: komórka = zaokrąglony wielokąt z okrągłym jądrem. Komórka z transgenem ma w jądrze mały fioletowy prostokąt (#7867a8). Toksyczne metabolity = małe PEŁNE czerwone trójkąty (#c84d42). Komórka umierająca = kontur przerywany czerwony, tło #fff0ec.

PANEL A – tytuł: „Guz”
Rząd sześciu komórek guza stykających się bokami (tło #fbf3e5, kontur #b77a20). Dwie z nich (druga i piąta od lewej) mają w jądrze fioletowy prostokąt – transgen; etykieta ze wskaźnikiem do jednej: „transgen: gen HSV-tk”. Pozostałe cztery nie mają transgenu; etykieta ze wskaźnikiem do jednej: „komórka guza bez transgenu”.
Kroki ponumerowane zielonymi kółkami z białymi cyframi:
1 – przy strzałce z krwiobiegu do komórki z transgenem: „prolek wnika do komórek”.
2 – wewnątrz komórki z transgenem: pusty trójkąt → (krótka strzałka) → pełny czerwony trójkąt; etykieta: „prolek → toksyczne metabolity”.
3 – komórka z transgenem narysowana jako umierająca (przerywany czerwony kontur); etykieta: „apoptoza”.
4 – z komórek z transgenem do sąsiednich komórek bez transgenu poziome czerwone strzałki niosące pełne czerwone trójkąty; sąsiednie komórki także z przerywanym czerwonym konturem. Etykieta (pogrubiona) pod rzędem komórek: „efekt sąsiedztwa: toksyczne produkty przenikają do sąsiednich komórek”.

PANEL B – tytuł: „Prawidłowa tkanka”
Rząd czterech komórek stykających się bokami (tło #e7f2ea, kontur #2b7a4b), żadna nie ma fioletowego prostokąta. W komórkach kilka pustych trójkątów (prolek), brak czerwonych. Kontury ciągłe. Etykiety: „brak transgenu”, „prolek pozostaje nietoksyczny”.

PEŁNA LISTA ETYKIET (dokładnie tak):
krwiobieg · nietoksyczny prolek (np. gancyklowir) · Guz · transgen: gen HSV-tk · komórka guza bez transgenu · 1 · 2 · 3 · 4 · prolek wnika do komórek · prolek → toksyczne metabolity · apoptoza · efekt sąsiedztwa: toksyczne produkty przenikają do sąsiednich komórek · Prawidłowa tkanka · brak transgenu · prolek pozostaje nietoksyczny

NIE RYSUJ: wirusa ani wektora, strzykawki, sylwetki pacjenta, DNA, limfocytów, wzorów chemicznych, innych układów (deaminaza cytozynowa, CYP2B), nazw innych leków, połączeń szczelinowych między komórkami.
```

- **Proponowany podpis:** Zacznij od krwiobiegu u góry: nietoksyczny prolek dociera do wszystkich komórek. Porównaj panele – w guzie komórki z transgenem (fioletowy znacznik w jądrze) zamieniają prolek w toksyczne metabolity i giną przez apoptozę (kroki 1–3), w prawidłowej tkance prolek pozostaje nietoksyczny. Wniosek: toksyczne produkty przenikają też do sąsiednich komórek guza (krok 4, efekt sąsiedztwa), więc transgen nie musi trafić do każdej z nich.
- **Źródło treści:** `#c11-kierunki`, h3 „Nowotwory – cztery różne pomysły”, akapit „Geny samobójcze – molekularna chemioterapia.”: „Do komórek guza wprowadza się gen kodujący białko, które przekształca podany do krwiobiegu nietoksyczny prolek w toksyczne metabolity indukujące apoptozę. Chemioterapia działa więc tylko tam, gdzie jest transgen.”; „gen kinazy tymidynowej Herpes simplex (HSV-tk) – wywołuje podatność na acyklowir, gancyklowir i walacyklowir”; „toksyczne produkty powstające w zmodyfikowanych komórkach przenikają poza nie i niszczą sąsiednie, niezmodyfikowane komórki. To efekt sąsiedztwa (bystander effect) – dzięki niemu nie trzeba trafić transgenem do każdej komórki guza.”

---

## 4. Instrukcja dla zleceniodawcy

1. **Generowanie.** Otwórz nową rozmowę w ChatGPT, wklej cały „Wstęp” (część 1) i poczekaj na potwierdzenie. Potem **jedna rycina = jedna wiadomość**: wklej blok „Prompt dla ChatGPT” z karty. Po ok. 4–5 rycinach styl zaczyna się rozjeżdżać – wtedy zacznij nową rozmowę i wklej wstęp jeszcze raz. Poprawki zgłaszaj w tej samej rozmowie, wskazując konkretną etykietę lub element („w panelu B etykieta ma brzmieć…”); nie proś o „narysowanie od nowa”, jeśli błąd jest jeden.
2. **Sprawdzenie etykiet.** Połóż obok obrazu „Pełną listę etykiet” z karty i odhacz po kolei: każda etykieta z listy jest na obrazie, a żadnej nie ma ponad listę; polskie znaki i znak ′ w zapisach 3′/5′ są poprawne; skróty, nazwy białek i zapisy kariotypów zgadzają się znak po znaku z listą. Generatory obrazów najczęściej mylą się w długich etykietach i w zapisach z nawiasami – te czytaj litera po literze.
3. **Sprawdzenie rysunku.** Policz kroki i panele (mają być dokładnie te z promptu, w tej samej kolejności), sprawdź kierunek strzałek i kolory według opisu. Jeśli na obrazie jest element spoza promptu (dodatkowe białko, liczba, strzałka, tytuł, podpis) – poproś o usunięcie; nie przyjmuj ryciny „prawie dobrej”, bo treść musi zgadzać się z tekstem rozdziału.
4. **Wymiary.** Jeśli ChatGPT odda obraz w innych proporcjach niż zamówione, przytnij białe pasy do proporcji z tabeli zbiorczej; gdy szerokość jest mniejsza niż 2400 px (2 łamy) lub 1200 px (1 łam), poproś o wersję w większej rozdzielczości.
5. **Nazwy plików.** Zapisz każdy plik jako PNG pod nazwą równą `id` z karty: `c01-fig-zakres.png`, `c02-fig-apc.png`, `c03-fig-kompleksy.png`, `c04-fig-korekta.png`, `c05-fig-rt.png`, `c06-fig-znakowanie.png`, `c07-fig-ipsc.png`, `c08-fig-heteroplazmia.png`, `c09-fig-strukturalne.png`, `c10-fig-xist.png`, `c10-fig-fmr1.png`, `c11-fig-samobojcze.png`. Odeślij komplet razem z tym dokumentem – podpisy i miejsca wstawienia są w kartach.
