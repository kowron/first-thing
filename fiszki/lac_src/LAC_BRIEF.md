# Zadanie: wszystkie nazwy łacińskie z Bochenka (t. I) – jeden rozdział

Student 1. roku medycyny uczy się na zaliczenie „szkielet osiowy” według podręcznika Bochenek & Reicher, „Anatomia człowieka”, t. I.
Z tych nazw powstaną fiszki: student widzi nazwę polską i ma wpisać nazwę łacińską. Dlatego każda para musi być dokładnie taka, jak u Bochenka.

Strony książki są w plikach `pages/NNN.txt` (OCR jednej strony; katalog: /tmp/claude-0/-home-user-first-thing/d41721b4-1413-50bf-8c94-691fa5e52b07/scratchpad/fz).
OCR ma błędy literowe (np. „intimt” = intimi, „ałaria” = alaria, „łumborum” = lumborum, „C,—Th,” = zgubione cyfry, „|” i śmieci z rycin). Podpisy rycin to zwykle sama łacina bez polskiego – pomijaj je.

## Co wypisać
Przeczytaj KAŻDĄ stronę z Twojego zakresu, od początku do końca, i wypisz KAŻDĄ nazwę łacińską, którą Bochenek podaje w tekście razem z polską nazwą (zwykle „polska nazwa (latin name)”). Dotyczy to wszystkiego: kości, części, wyrostków, powierzchni, otworów, więzadeł, stawów, błon, mięśni i ich części, powięzi, kanałów, trójkątów, fałdów, naczyń i nerwów, jeśli Bochenek podaje je z łaciną, krzywizn (kyphosis, lordosis, scoliosis) itd.
- Polską nazwę podaj w MIANOWNIKU (np. „wyrostka kolczystego (processus spinosus)” → „wyrostek kolczysty”), w tej samej liczbie co łacina (łacina w liczbie mnogiej → polski w mnogiej). Bez „m.”/„mm.” na początku polskiej nazwy: pisz pełne „mięsień …”, „mięśnie …”, „więzadło …” jeśli tak jest w tekście; skróty łacińskie rozwiń: „m.” → „musculus”, „mm.” → „musculi”, „lig.” → „ligamentum”, „ligg.” → „ligamenta”, „a.”/„v.”/„n.” → arteria/vena/nervus, „proc.” → processus.
- Łacinę popraw tylko z błędów OCR (literówki). Nie zmieniaj formy, którą wybrał Bochenek (np. jeśli pisze „vertebrae thoracicae”, nie zmieniaj na inną). Gwiazdkę po łacinie (np. „angulus lumbosacralis*”) usuń.
- Jeśli Bochenek podaje drugą nazwę łacińską (np. w przypisie „! vertebrae thoracales” albo „lub …”), dodaj ją w polu `alt`.
- Każda łacina tylko raz w Twoim zakresie (pierwsze wystąpienie). Jeśli ta sama łacina ma w tekście dwie polskie nazwy, wybierz tę z opisu głównego, drugą dopisz w `uwaga`.
- Pomijaj: etymologie („splenion = opatrunek”, „amfi = dokoła”), nazwy zwierząt i grup zwierząt, nazwiska, łacińskie słowa ogólne niebędące nazwą struktury, nazwy z samych podpisów rycin bez polskiego odpowiednika w tekście, łacińskie opisy ruchów, jeśli nie są nazwą (np. „rotatio s. torsio” – TAK, to nazwa ruchu z polskim „ruchy obrotowe”; oceniaj rozsądnie).
- Nazwy kliniczne podane przez Bochenka z łaciną (np. „przepuklina pachwinowa”, „diastasis musculorum rectorum”) – dołącz, ale z `k: true`.

## Działy (pole `t`)
Każdej parze nadaj krótki dział – nagłówek z książki albo jego skrót, 2–5 słów, np. „Kręgi szyjne”, „Kręg szczytowy”, „Kość krzyżowa”, „Krążki międzykręgowe”, „Więzadła kręgosłupa”, „Mięśnie powierzchowne grzbietu”, „Mięśnie głębokie grzbietu”, „Przepona”, „Pochewka mięśnia prostego”, „Kanał pachwinowy”. Kolejność par = kolejność w książce, więc działy idą po kolei. Nie twórz działów na 1–2 nazwy: dołącz je do sąsiedniego.

## Wynik
Zapisz plik JSON (lista obiektów, kolejność książkowa):
`{"pl": "wyrostek kolczysty", "la": "processus spinosus", "alt": [], "s": 221, "t": "Budowa kręgu", "k": false, "uwaga": ""}`
Pole `s` = numer strony (liczba). Zapisz do pliku podanego w poleceniu. Nie zmieniaj żadnych innych plików.
Na koniec odpowiedz krótko: liczba par, lista działów (z liczbą par w każdym), wątpliwości (strona + jedno zdanie).
