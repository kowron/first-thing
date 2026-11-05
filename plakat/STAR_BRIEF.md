# Wspólna instrukcja – tematy „★ na zaliczenie” (rysunki + wyjaśnienia)

Plakat A0,5 „Anatomia: szkielet osiowy” (student 1. roku lekarskiego, źródło: A. Bochenek, M. Reicher, „Anatomia człowieka”, t. I). Użytkownik wskazał tematy ★,
które MUSZĄ być wzorowo opracowane: duża, czytelna czcionka, własne rysunki i **lepsze tłumaczenie** (proste, krok po kroku, ale w 100% wg Bochenka).

## Zasady twarde
1. „Bochenek ma rację” – tylko fakty z Bochenka t. I; lepiej pominąć niż napisać niepewne. Niezgodności w samym Bochenku oznacz „!” w polu `warn`.
2. Terminologia dokładna co do słowa (żebro / kość żebrowa / chrząstka żebrowa; blaszka / warstwa; więzadło / więzozrost; staw / połączenie itd.). Łacina tylko taka, jaka jest w Bochenku
   (narządów, których Bochenek nie podaje po łacinie, nie tłumacz na łacinę). Nie wspominaj Nettera.
3. Prosty język, styl notatek, krótkie zdania, jedna nowa nazwa na zdanie. Podziały („szufladki”) mile widziane. Żadnych „to jest X, czyli NIE Y”.
4. Źródła: OCR `/home/user/first-thing/all.txt` (mięśnie, przepona, oddychanie; znaczniki `=== BOOK PAGE N ===`) i `/home/user/first-thing/bones.txt` (kości, połączenia; też znaczniki `=== PDF N-0/1 ===`).
   Gdy OCR wygląda podejrzanie (łacina, liczby) – skan: `/tmp/claude-0/-home-user-first-thing/d41721b4-1413-50bf-8c94-691fa5e52b07/scratchpad/skan.pdf` (numer strony PDF dla strony książki bierz ze znaczników `=== PDF N-0/1 ===` w bones.txt; w all.txt strony 650–733 to ok. PDF 322–365,
   np. s. 706–707 = PDF 344, s. 718–719 = PDF 350; zawsze sprawdź numer w stopce). Render: `pdftoppm -r 110 -f N -l N -png /tmp/claude-0/-home-user-first-thing/d41721b4-1413-50bf-8c94-691fa5e52b07/scratchpad/skan.pdf <katalog_w_scratchpadzie>/x`, potem Read.
   Skan służy do zrozumienia układu – NIE kopiujesz rycin.

## Rysunki (własne, schematyczne, SVG kodem)
Instrukcja: `/home/user/first-thing/plakat/figs/FIG_BRIEF.md` (obowiązuje w całości; biblioteka `figs/figlib.py`, wzory `figs/src/*.py`, podgląd: `cd /home/user/first-thing/plakat/figs && PXMM=8 python3 preview.py <nazwa>`
→ `figs/png/<nazwa>.png`, obejrzyj Read min. 2 razy, także fragmenty w powiększeniu). Środowisko: `export PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`.
Kontrola nakładania/krzyżowania linii podpisów: `python3 /tmp/claude-0/-home-user-first-thing/d41721b4-1413-50bf-8c94-691fa5e52b07/scratchpad/zebra_agent/tools/check.py figs/out/<nazwa>.svg` (ma dać 0 problemów).
Rysunki mają być WIĘKSZE niż dotąd: płótno szerokości **120–160 mm**, wysokość do ~120 mm, 8–16 podpisów (PL + łacina jak u Bochenka), teksty nie nachodzą, linie się nie krzyżują.
Pliki: `figs/src/<nazwa>.py` → `figs/out/<nazwa>.svg`. NIE modyfikuj innych plików poza własnymi (src/out/png, plik wyjaśnień, scratchpad).

## Wyjaśnienia „★ W SKRÓCIE” (plik JSON)
Zapisz `/home/user/first-thing/plakat/explain_<twoja_nazwa>.json` w formacie:
```json
{ "<klucz>": { "title": "krótki tytuł (np. Jak przebiegają włókna?)", "points": ["krótki punkt 1 (s. 686)", "punkt 2 (s. 686–687)"],
               "steps": ["opcjonalnie: kroki 1., 2., 3. – gdy opisujesz mechanizm lub przebieg"], "warn": ["opcjonalnie: ! niezgodność Bochenka"],
               "fig": ["nazwa_rysunku_z_figs/out"] } }
```
**Klucz** = dokładna nazwa mięśnia z `/home/user/first-thing/plakat/data.py` (pole `pl`, np. `mm. międzyżebrowe zewnętrzne`), albo dokładny tytuł karty z `k_*.json` (np. `Otwory`),
albo id panelu z `l3_*.json` (np. `kanal`). 3–8 punktów na klucz, każdy z numerem strony Bochenka. Pisz tak, żeby student po przeczytaniu umiał to opowiedzieć na egzaminie
(przyczepy początkowe → końcowe, przebieg włókien, czynność, unerwienie tylko jeśli Bochenek podaje i jest istotne). Wyjaśnienia nie mogą powtarzać słowo w słowo istniejących kart – mają **tłumaczyć** (porządek, kolejność, „po co”).

## Na koniec odpowiedz krótko
Lista rysunków (nazwa, co przedstawia, rozmiar mm), klucze wyjaśnień, 5 najważniejszych wątpliwości / niezgodności Bochenka, czego nie dało się potwierdzić.
