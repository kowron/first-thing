# AKTUALIZACJA – sesja 3 (ciąg dalszy): 7 stron A0, tematy ★ rozbudowane

**Budowanie:** `cd /home/user/first-thing/plakat && ./build_pages.py` (dla każdej strony szuka największego K mieszczącego się na stronie; `./build_pages.py m3` – wybrane strony; zmienne `KS`, `L3MIN`, `LIMIT`).
Strony (A0 1189×841): kregoslup, klatka (kości + połączenia żeber i mostka), m1 grzbiet, m2 mięśnie klatki, m3 brzuch (doki rozdzielone `DOCKSPLIT_brzuch`), polkreg, klodd (mechanika klatki + przepona + oddychanie).
Rozbudowy ★: `explain_*.json` (klucz = nazwa mięśnia / tytuł karty / id panelu) wstawiane jako sekcje kart (`oslib.expl_html`); zbędne stare wiersze usuwane przez `TRIM`, `_DROP_*` (build.py) i `CARD_TRIM` (oslib.py).
Agenci rysunkowi: instrukcja `plakat/STAR_BRIEF.md`. Nowe rysunki: mm_miedzyzebrowe, m_poprzeczny_klatki, m_piersiowy_wiekszy, m_najszerszy_grzbietu, m_prosty_brzucha, mm_brzucha_przyczepy, kanal_pachwinowy, przepona_wiezadla, klatka_wymiary, zebro_krzywizny.
Poprzedni opis „6 stron 1030×728” poniżej jest nieaktualny (build_pages.sh zastąpiono build_pages.py).

---

# AKTUALIZACJA – sesja 3 (5.11.2026): format 6 stron „A0,5” (1030×728 mm)

Plakat podzielono na **6 stron 1030×728 mm** (pole 0,75 m² – pomiędzy A0 i A1; PDF dowolnego rozmiaru, czytany w przeglądarce): 1 kręgosłup (kości), 2 klatka piersiowa (kości),
3 mięśnie grzbietu, 4 mięśnie klatki i brzucha, 5 połączenia i krzywizny kręgosłupa, 6 klatka (połączenia, mechanika) + przepona i oddychanie.
**Budowanie wszystkiego jednym poleceniem:** `cd /home/user/first-thing/plakat && ./build_pages.sh` (parametry stron – w skrypcie; `./build_pages.sh m1 klodd` – tylko wybrane strony).
Wynik: `/home/user/first-thing/Plakat_A0_5_szkielet_osiowy.pdf`. Limit wysokości `max_bottom` ≤ 717 mm. Poprzednia wersja 3×A0: `Plakat_A0_szkielet_osiowy.pdf`.
Nowe przełączniki: `build.py` – `REGIONS`, `PAGE=SZERxWYS`, `OUT`, `ROOT_TITLE/ROOT_SUB`, `DOCKCOLS_<rozdział>=2`; `build_os.py` – `PW/PH`, `LAYOUT`, `DATA`, `ONLY` (layout_kosciec.py: kregoslup|klatka; layout_mech.py: polkreg|klodd).
**Zmiany treści (od użytkownika):** mięśnie głębokie grzbietu – tylko nazwy (karty `namecard`, `NAMES_ONLY` w `build.py`); pełne opisy zostały przy m. krzyżowo-grzbietowym (prostownik grzbietu), mm. dźwigaczach żeber
i mięśniach powierzchownych. ★ = temat wskazany przez użytkownika jako ważny na zaliczeniu (`STAR_M`, `STAR_P` w `build.py`, `STAR_TITLES` w `gen_oddychanie.py`, pole `star` w kartach).
**Ustalenia z użytkownikiem (5.11):** faz kaszlu NIE robić. „Kiedy piersiowy większy pomaga w oddychaniu / pozycja, w której łatwiej oddychać” = ramiona ustalone, chwyt brzegu stołu lub krzesła → pomocniczy WDECHOWY (s. 680, 697). Przy m. poprzecznym klatki używać słowa „promienisty” (słowo prowadzącego). „Błona” z notatki = błony międzyżebrowe zewnętrzne (między chrząstkami żebrowymi). Rozwór aortowy zawsze na Th12. Tylko Opus (bez Sonneta).
(Bochenek s. 680: tylko pomocniczy wdechowy przy ustalonych ramionach).

---

# AKTUALIZACJA – sesja 2 (4.11.2026, wieczór) – czytaj to najpierw

**Środowisko (zmiana względem opisu poniżej):** projekt leży w `/home/user/first-thing/plakat/` (ścieżki w kodzie zamienione z `/home/claude`), skrypty w `/home/user/first-thing/scripts/`.
Czcionki: Inter + TeX Gyre Pagella (pobrane z CTAN do `/usr/local/share/fonts/texgyre`). Python playwright: `export PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`;
skrypty `launch` mają `executable_path=/opt/pw-browsers/chromium` i `--no-sandbox`. OCR książki (`all.txt`, `bones.txt`) NIE jest w repozytorium (`.gitignore`) – trzymać lokalnie.

**Przebudowa stron:**
```bash
cd /home/user/first-thing/plakat
python3 build.py && python3 ../scripts/pdf_poster2.py /home/user/first-thing/plakat/index.html p2.pdf          # strona 2 (cel max_bottom ≤ 830; teraz 829)
../scripts/meas.sh kosciec 0.8 0.75; K=0.8 FIGSCALE=0.75 PAGE=kosciec python3 build_os.py && python3 ../scripts/pdf_poster2.py /home/user/first-thing/plakat/page_kosciec.html test_k.pdf   # strona 1 (teraz 790)
../scripts/meas.sh mech 0.8 0.75;    K=0.8 FIGSCALE=0.75 PAGE=mech    python3 build_os.py && python3 ../scripts/pdf_poster2.py /home/user/first-thing/plakat/page_mech.html test_m.pdf       # strona 3 (teraz ~818)
```
`k_oddychanie.json` jest GENEROWANY (`python3 gen_oddychanie.py` z `data.py` + `l3_klatka.json`) – poprawki robić w generatorze/`data.py`, nie w JSON-ie.

**Stan:** strona 1 – gotowa (wszystkie rysunki); strona 2 – gotowa, dodany własny rysunek `pochewka_przekroje` (dok pod kolumną `bbocz`) i wiersz „Tłocznia – udział mięśni”;
strona 3 – układ przebudowany (`layout_mech.py`: kręgosłup 3 kolumny, klatka 2 bloki, oddychanie na podwójnej szerokości; parametry env `CWM`, `CWK`), `k_mech.json` napisany,
nowa karta „Tłocznia brzuszna” z rysunkiem `przepona_brzuch`. Weryfikacje V1–V7 i audyty terminologii T1/T3 nałożone (`verify_*.json`).
**Znane braki:** w skanie nie ma s. 288–289 i ryc. 194–195 (początek „Klatka piersiowa jako całość”) – użytkownik ma papierową książkę; dopisać z fotografii.
**Zasady wyciągnięte z tej sesji:** (1) nazwy łacińskie na rysunkach tylko takie, które są w t. I Bochenka (kontrola: skrypt porównujący `class="la"` z OCR; narządów typu hepar/ren/pulmo/cor/splen/gaster/pericardium u Bochenka nie ma – bez łaciny);
(2) numer strony PDF skanu brać ze znaczników `=== PDF N-0/1 ===` w `bones.txt` (stały wzór nie działa w całej książce);
(3) po zmianie rysunków/treści zawsze `meas.sh` → `build_os.py` → `pdf_poster2.py` i sprawdzić `max_bottom`, `over`, `overlap`.

---

# HANDOFF – plakat A0 „Anatomia: szkielet osiowy” (Piotr, ŚUM, 1. rok lekarski)

Stan na 4.11.2026, ok. 18:00. Dokument dla kolejnej sesji (Claude Code). Wszystko po polsku; kod ma twardo wpisane ścieżki `/home/user/first-thing/...`
– rozpakuj archiwum do `/home/user/first-thing/` (patrz „Uruchomienie”) albo zrób `sed -i 's#/home/user/first-thing#TWOJA_SCIEZKA#g'` na plikach `.py`, `.sh`, `.md`.

## 1. Cel (wymagania użytkownika)
Jeden PDF, **max 3 strony A0** (1189×841 mm, czytany w przeglądarce PDF z przybliżaniem), źródło: **A. Bochenek, M. Reicher, „Anatomia człowieka”, t. I**.
- **Strona 1 – Kościec osiowy:** kręgi (szyjny typowy, C1, C2, C6, C7, piersiowy typowy, Th1, Th10, Th11, Th12, lędźwiowy typowy, L5), kość krzyżowa, guziczna,
  żebra (I, II, typowe, XI–XII), mostek, klatka piersiowa jako całość (budowa ogólna). Osteologia bardzo dokładna i kompletna.
- **Strona 2 – plakat mięśni** (istniejący, bez zmian) – z jednym wyjątkiem: usunięta mechanika oddychania, karta przepony skrócona do tego, co trzeba umieć
  po łacinie: części + otwory, króciutkie opisy. Gotowe (`index.html` → `p2.pdf`).
- **Strona 3 – Połączenia i mechanika (dużo rysunków):** krzywizny kręgosłupa (bardzo szczegółowo + powstawanie krzywizn na osi czasu rozwoju dziecka) i skoliozy;
  mechanika klatki piersiowej (odporność, ruchomość – całość); **przepona w pełnym szczególe** (przed mechaniką oddychania); mechanika oddychania.
  Przepona i oddychanie = główny nacisk.
- **Połączenia (stawy, więzadła):** wszystkie z tułowia, z podziałem na rodzaje (chrząstkozrosty / więzozrosty / stawy); krzyżowo-guziczne i krzyżowo-biodrowe z więzadłami;
  żebra i mostek. **BEZ części ogólnej, BEZ połączeń czaszki z kręgosłupem** (to przy czaszce, nie teraz).
- Strony mają być **zrównoważone** (mniej więcej tyle samo treści); strona mięśni nie może się zmienić.
- **Poza zakresem (nie robić):** rozwój kręgosłupa, zmienność kręgosłupa, rozwój i zmienność żeber i mostka, zmienność kształtu klatki, czynność kręgosłupa,
  ogólna charakterystyka/wymiary/powierzchnia/kanał kręgosłupa, czaszka.
- **Wszystkie rysunki własne** (SVG rysowane kodem). Bez Nettera, bez rycin Bochenka; na plakatach nie wspominać Nettera. Użytkownik może później sam wkleić płyty w innym czacie.

## 2. Zasady twarde
1. **„Bochenek ma rację”** – wszystko w 100% z Bochenka. Lepiej pominąć niż napisać niepewne. Niezgodności wewnątrz Bochenka oznaczamy „!” w poziomie 3.
2. **Terminologia musi być dokładna co do słowa.** Profesor czepia się słówek: „żebro” zamiast „kość żebrowa” = oblany egzamin. Bochenek odróżnia **żebro** (całość) od
   **kości żebrowej** ({{os costale}}, część kostna) i **chrząstki żebrowej** ({{cartilago costalis}}). **Do zrobienia przed oddaniem: audyt całej treści
   (JSON + podpisy rysunków) pod kątem takich rozróżnień** – każde zdanie o części kostnej ma mówić „kość żebrowa”, o chrzęstnej „chrząstka żebrowa”; to samo dla
   „kręg/trzon kręgu”, „wyrostek/wyrostek stawowy”, „więzadło/więzozrost”, „staw/połączenie” itd. Nazwy PL i łacińskie dokładnie jak u Bochenka (łacina równie ważna jak PL).
3. Zapis: PL pogrubione + łacina kursywą (`**guzek przedni** {{tuberculum anterius}}`), łacina „poboczna” `[[...]]`. Styl notatek, bez „to jest X, czyli NIE Y”,
   bez upychania wielu nowych nazw w jednym zdaniu. Prosty język. Użytkownik lubi **podziały („szufladki”)** – drzewa z kryteriami podziału (kółka z pytaniami).
4. Trzy poziomy czytania: 1 = sam podział, 2 = karty z rysunkami, 3 = drobny druk w ramkach (ikonka „3”).

## 3. Struktura plików (`/home/user/first-thing/plakat/`)
| plik | rola |
|---|---|
| `build.py` | **strona 2** (mięśnie) → `index.html`; `l3_*.json` = poziom 3 mięśni; przepona skrócona (`przepona_short`), bez MECH. Kopia: `build_v2_backup.py` |
| `data.py` | dane mięśni (używane przez `build.py` i `gen_oddychanie.py`) |
| `build_os.py` | **strony 1 i 3**: `PAGE=kosciec` → `page_kosciec.html`, `PAGE=mech` → `page_mech.html`; env `K` (skala tekstu), `FIGSCALE` (skala rysunków), `L3S`, `MEASURE=1` |
| `oslib.py` | karty, rysunki inline, `FIGSCALE_FOR` (skala pojedynczych rysunków), `card_html`, `figs_html`, `est_height` |
| `layout_kosciec.py`, `layout_mech.py` | układ stron: `FIG` (karta→rysunki), `GFIG` (rysunek zbiorczy grupy), `MODE` (list/row/grid2/intro-row), `WIDTH`, `ROWSPEC`, `GRID2`, `MERGE`, `CH_WIDTHS` |
| `style.css`, `wires.js` | styl (wspólny z plakatem mięśni) i rysowanie łączników drzewa (JS) |
| `k_kregoslup.json`, `k_klatka.json`, `k_polaczenia.json`, `k_oddychanie.json` | **treść stron 1 i 3** (drzewa grup/kart; format w `L4_BRIEF.md`) |
| `k_mech.json` | **NIE ISTNIEJE** – krzywizny kręgosłupa + skoliozy + mechanika klatki (agent przerwany limitem) |
| `gen_oddychanie.py` | generuje `k_oddychanie.json` z `data.py` + `l3_klatka.json` |
| `figs/figlib.py`, `figs/preview.py`, `figs/FIG_BRIEF.md`, `figs/src/*.py` → `figs/out/*.svg` | biblioteka i źródła rysunków (1 jednostka = 1 mm; podpisy tylko przez `f.label`) |
| `L4_BRIEF.md`, `VERIFY_BRIEF.md` | instrukcje dla agentów: treść z OCR+skanu / weryfikacja |
| `verify_V1..V6.json` | wyniki weryfikacji (V5, V7 nieukończone – patrz §6) |
| `/home/user/first-thing/scripts/` | `pdf_poster2.py` (render PDF + metryki), `measure.py`, `meas.sh`, `apply_verify2.py`, `lines.py`, skrypty OCR |
| `/home/user/first-thing/bones.txt`, `all.txt` | OCR Bochenka (kości/połączenia; mięśnie/przepona/oddychanie). Znaczniki `=== PDF N-0/1 ===` i stopki = numery stron książki |

Skan książki (**nie dołączony – 132 MB**, użytkownik ma go u siebie): `/tmp/claude-0/-home-user-first-thing/d41721b4-1413-50bf-8c94-691fa5e52b07/scratchpad/skan.pdf`.
Jedna strona PDF = dwie strony książki (PDF 99-0 = s. 228, PDF 102-0 = s. 234…). Render: `pdftoppm -r 150 -f N -l N -png "<skan>" /tmp/x`.

## 4. Uruchomienie
```bash
# zależności: python3, playwright (+ chromium: `playwright install chromium`), pypdf, poppler-utils (pdftoppm), czcionki Inter i TeX Gyre Pagella
cd /home/user/first-thing/plakat
# strona 2 (gotowa):
python3 build.py && python3 /home/user/first-thing/scripts/pdf_poster2.py /home/user/first-thing/plakat/index.html p2.pdf
# strona 1:
/home/user/first-thing/scripts/meas.sh kosciec 0.8 0.75            # pomiar wysokości kart → measure_kosciec_0.8_0.75.json (używany do równoważenia kolumn)
K=0.8 FIGSCALE=0.75 PAGE=kosciec python3 build_os.py
python3 /home/user/first-thing/scripts/pdf_poster2.py /home/user/first-thing/plakat/page_kosciec.html test_k.pdf   # wypisuje max_bottom (cel ≤ 830), nakładanie, przepełnienia
# strona 3: to samo z PAGE=mech
# złożenie (kolejność: kościec, mięśnie, mechanika):
python3 -c "from pypdf import PdfWriter; w=PdfWriter(); [w.append(f) for f in ['test_k.pdf','p2.pdf','test_m.pdf']]; w.write('Plakat_A0_szkielet_osiowy.pdf')"
```
Podgląd rysunku: `cd figs && PXMM=4 python3 preview.py <nazwa>` → `figs/png/<nazwa>.png` (obejrzeć narzędziem Read).
Parametry układu strony 1: `CWS` (szerokość kolumny kręgosłupa, 112) i `CWT` (kolumna klatki, 104) – env.

## 5. Stan stron
| strona | stan |
|---|---|
| 2 mięśnie | **gotowa** (`p2.pdf`, max_bottom 824). Przepona skrócona (części + otwory + odsyłacz na stronę 3), mechaniki oddychania nie ma. |
| 1 kościec | zbudowana: `K=0.8 FIGSCALE=0.75`, 9 kolumn (kręgosłup 6 + klatka 4 szerokości), **max_bottom 794 ≤ 830 – mieści się**, bez nakładania. Brakujące rysunki = ramki-zaślepki. Do zrobienia: równowaga (kręgosłup ~794 vs klatka ~738), przegląd wizualny z bliska. |
| 3 mechanika | **przepełniona (max_bottom 1023)** i niekompletna: brak `k_mech.json` (krzywizny, skoliozy, mechanika klatki). Obecny układ = 3 szerokie kolumny w trybie `list` – trzeba go przebudować jak na stronie 1 (wiele wąskich kolumn, `grid2`, `ROWSPEC`, `MERGE`), K≈0.8, FIGSCALE≈0.75. Łącznie treść: połączenia (38 kart) + przepona (6) + mechanika oddychania (5) + do dodania krzywizny/skoliozy/mechanika klatki. |

## 6. Weryfikacja treści z Bochenkiem
Wyniki w `verify_V*.json`; nakładanie poprawek: `python3 /home/user/first-thing/scripts/apply_verify2.py k_kregoslup verify_V1 verify_V2 verify_V3 [--dry]` (skrypt napisany, **nieprzetestowany** – najpierw `--dry`; `--skip=V1:3,V1:4` pomija wskazane).
- **V1** (kręgi szyjne, `k_kregoslup.json`): 8 uwag + 2 braki. Najważniejsze: (a) punkty o rozwoju/zmienności (noworodek C2, żebro szyjne, pochodzenie listewki) = **poza zakresem → usunąć**;
  (b) „dawniej/dawna nazwa” – u Bochenka (przypisy s. 221, 225) jest tylko synonim → przeformułować; (c) l3/3 w „Kręg szyjny typowy” źle przypisana (ryc. 136 = C1, ryc. 139 = C7);
  (d) braki: podpis `foramen processus transversi` na ryc. 136 (C1) i 139 (C7).
- **V2** (piersiowe/lędźwiowe): 0 błędów; brak: Th1 – wyrostek kolczysty „jak od Th1 do Th8: spiczasty, silnie pochylony ku dołowi, w przekroju trójkątny” (s. 230).
- **V3** (kość krzyżowa/guziczna): 0 błędów; brak: nazwy `vertebrae verae` = `vertebrae presacrales` (kręgi ruchome) w opozycji do `vertebrae spuriae` (s. 220).
- **V4** (żebra): 2 uwagi – usunąć l3 „LICZBA” z „Żebra – cechy ogólne” (zmienność żeber, poza zakresem); w „Żebra prawdziwe” sections/0/1 zmienić na „z przodu łączą się obustronnie z mostkiem”.
- **V6** (połączenia kręgów przedkrzyżowych): 0 błędów, podział i etykiety zgodne z Bochenkiem.
- **V5 (mostek + klatka jako całość) i V7 (połączenia kości krzyżowej, połączenia żeber i mostka): NIE WYKONANE** (limit). V5 miał też sprawdzić, czy w skanie naprawdę brakuje s. 288–289
  (notatka w l3 grupy „Klatka piersiowa jako całość”).
- **Treść stron 3 (przepona, mechanika oddychania)** pochodzi z już zweryfikowanych danych (`data.py`, `l3_klatka.json`), ale karty „Mechanika oddychania” nie były osobno sprawdzone po przepisaniu – zweryfikować.
- Do wykonania na końcu: **osobny, niezależny audyt całości** (zwłaszcza terminologii – §2.2).

## 7. Rysunki (`figs/out`)
Gotowe (31 plików; część to **niedopracowane pierwsze wersje – agenci przerwali w trakcie poprawek, obejrzeć każdy**):
kr_c1_gora, kr_c2_bok, kr_c2_przod, kr_c7_gora, kr_c_gora, kr_c_przod, kr_l_bok, kr_l_gora, kr_sacrum_przod, kr_sacrum_tyl, kr_th_gora, kr_th_bok, kr_th_dolki, kr_th12_bok,
kregoslup_bok (cały kręgosłup, bok), krzywizny_dorosly, krzywizny_os_czasu, mostek_przod, mostek_bok, zebro_typowe, zebro_tyl, zebro_I, zebro_os_ruchu,
pol_przekroj_strzalkowy, pol_zebro_kreg_gora, pol_zebro_kreg_bok, pol_krazek_gora, przepona_dol, przepona_czolowy, oddychanie_wymiary (+ `wzor_th_gora` = wzór stylu).
**Brakujące (zaślepki w układzie):** kr_sacrum_bok, kr_coccyx, klatka_przod, zebro_II, zebra_XI_XII (zaślepki; `zebro_II`/`zebra_XI_XII` agent nie skończył), pol_karkowe, pol_staw_miedzykregowy,
pol_krzyzowo_biodrowy, pol_mostkowo_zebrowe, przepona_boczny, przepona_brzuch, typy_oddechowe, miesnie_oddechowe, zebra_ruchy_wymiary, klatka_odpornosc,
oraz nowe: skolioza (krzywizny w płaszczyźnie czołowej), rysunki do mechaniki chrząstki żebrowej. `kr_th_dolki` i `pol_przekroj_strzalkowy` – sprawdzić (kilka uwag agentów).
Rysunki powstają przez agentów (Opus) wg `figs/FIG_BRIEF.md`: własne, schematyczne, podpisy PL + łac. dokładnie jak u Bochenka, 6–14 podpisów, bez krzyżujących się linii.
Mapowanie rysunek→karta: `FIG`/`GFIG` w `layout_*.py`.

## 8. Plan dalszych prac (kolejność)
1. Napisać `k_mech.json` wg `L4_BRIEF.md` (agent Opus + skan): „Krzywizny w płaszczyźnie pośrodkowej”, „Powstawanie krzywizn” (oś czasu: noworodek → ok. 3 mies. → siedzenie → stanie/chodzenie → dorosły – wg Bochenka, s. ~263–265),
   „Krzywizny w płaszczyźnie czołowej” (skoliozy), „Odporność klatki piersiowej”, „Mechanika kości żebrowej” (osie ruchu, ruchy), „Mechanika chrząstki żebrowej”.
   Pomiń: czynność kręgosłupa, rozwój kręgosłupa (poza krzywiznami z osią czasu, o którą prosił użytkownik).
2. Dokończyć rysunki (lista w §7), obejrzeć wszystkie w podglądzie.
3. Zastosować poprawki z weryfikacji (§6), dokończyć V5 i V7, dopisać brakujące punkty.
4. Przebudować układ strony 3 (K≈0.8, FIGSCALE≈0.75), tak żeby max_bottom ≤ 830 i zawartość stron 1 i 3 była zbliżona (obie ~700–800 mm wysokości użytej).
5. Audyt terminologiczny (§2.2) całości, przegląd wizualny z przybliżeniem (poziomy 1/2/3 czytelne, łączniki, brak nakładania).
6. Złożyć 3 strony w jeden PDF (§4) i oddać.

## 9. Uwagi techniczne / pułapki
- `<style>` w SVG jest wycinany; style rysunków (figlib `STYLE`) dodawane raz do strony z prefiksem `.figsvg` (inaczej klasy `.pl`, `.note` kolidują z plakatem).
- `lookup()` w `build_os.py` – najpierw dokładny tytuł, potem najdłuższy pasujący przedrostek (klucze `FIG`/`MODE`/`WIDTH` mogą być początkiem tytułu).
- Wysokości kart do równoważenia kolumn bierze z `measure_<PAGE>_<K>_<FS>.json` (`meas.sh`); po zmianie treści/rysunków/K/FIGSCALE trzeba zmierzyć ponownie.
- `wires.js` rysuje łączniki po wyrenderowaniu (`data-wired="1"`); tryby: grid2 (pień pośrodku), row (szyna), list, `kstack` (boczne ścieżki).
- Playwright: viewport 7000×5200, `emulate_media('print')`; PDF wektorowy, `@page` 1189×841 mm.
- Limity API: sesje z agentami wyczerpywały tygodniowy limit; agentów odpalać po kilka, nie 9 naraz.
