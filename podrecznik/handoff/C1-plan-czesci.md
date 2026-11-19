# Handoff C1 (wersja 2, oszczędna) – plan różnicowy podziału rozdziału na dwie części (Fable xhigh; 1 agent = 1 rozdział)

## Budżet – najważniejsze ograniczenie
Zleceniodawca: Fable ma zużywać **najwyżej ok. 25% kredytów projektu**. Poprzednie plany (Z02, Z03) miały po 120–150 KB i kosztowały tyle, co cała przebudowa rozdziału. Dlatego:
- **Czytasz tylko 3 pliki:** ten handoff, `STYL.md` (krótki) i **pakiet `pakiety/zNN.txt`** (rozpiska, mapa zakresu, fakty wcześniej ucięte, tekst rozdziału bez rycin, źródła przycięte do zakresu). Nie otwierasz pliku HTML rozdziału, wyciągu, innych plików ani skanów. Wyjątek: jedna konkretna wątpliwość, której nie da się rozstrzygnąć z tekstu – wtedy maks. 1–2 strony skanu (`/tmp/claude-0/-home-user-first-thing/600b873f-e07d-5766-b2f4-6a90b68ae091/scratchpad/dropbox/Drewa - Genetyka medyczna.pdf`, strona PDF = strona książki + 28; `pdftoppm -r 80`).
- **Pakiet czytaj w 2–4 dużych kawałkach** (Read z offset/limit ok. 800–1000 linii). Bez grepowania po innych plikach.
- **Plan ma najwyżej ok. 18 KB.** Zapisujesz **tylko różnice** względem obecnego tekstu – nie spisujesz tego, co już jest w rozdziale, nie cytujesz obecnego tekstu, nie proponujesz brzmień dla części 1. Brzmienia i odszukanie miejsc w pliku zrobi wykonawca (Opus).
- Łącznie najwyżej ok. 10–12 wywołań narzędzi. Plan zapisz jednym `Write` (ewentualnie jedna poprawka).

## Decyzja zleceniodawcy (co budujemy)
Podręcznik ma zawierać **wszystkie informacje z podanych źródeł** (w zakresie zagadnień z rozpiski). Każdy rozdział:
- **część 1 (ok. 70% informacji)** – wszystkie zagadnienia; najważniejsze w pełni, reszta tak, żeby ją rozumieć, bez szczegółów (to obecny rozdział po przesunięciu części szczegółów);
- **przejście** na końcu części 1;
- **część 2 – „na piątkę” (ok. 30%)** – rozszerzenie: szczegóły z części 1 i wszystko ze źródeł, czego w rozdziale brakuje. Bez nowych rycin, dobre tłumaczenie, funkcja użytkowa.
Ryciny się nie zmieniają.

## Zakres = „podane źródła”
- Sekcja E pakietu to źródła przycięte do zakresu z mapy (sekcja B). Wszystko w E, co dotyczy zagadnień z rozpiski, ma się znaleźć w rozdziale (część 1 albo 2). Fakty, które mapa kiedyś kazała ciąć (sekcja C pakietu i kolumna „Tniemy” w B), **wracają do części 2**. Nie wracają: pytania kontrolne źródła i odpowiedzi do nich, piśmiennictwo, odesłania do rycin bez treści, czyste powtórzenia.
- „Poza zakresem” z mapy – dalej poza (jeśli uważasz, że rozpiska jednak obejmuje temat – jedna linijka w „Decyzjach”).
- Informacje widoczne tylko na rycinach/tabelach źródła (opisane w tekście OCR) – też do kompletu: część 2, jako opis słowny lub tabela.
- Stary Jorde (ok. 2000) – tylko to, czego nie ma w Drewie do tych samych zajęć.
- Rozdziały 04 i 05 powstały kiedyś z opracowań (k4, k5), a nie wprost ze źródeł – porównujesz tekst rozdziału z **źródłami z sekcji E**, nie z opracowaniami.

## Format planu `plany/zNN-czesci.md` (dokładnie te punkty, zwięźle)
1. **Bilans** (3–5 linijek): ile mniej więcej informacji ze źródeł jest już w rozdziale; ile dochodzi; docelowy podział ≈ 70/30.
2. **Dopisać** – informacje ze źródeł, których w rozdziale brak, pogrupowane według sekcji części 2 (R1, R2, …). Jedna informacja = jedna linijka: `- s. X: treść` (pełna informacja: nazwy, liczby, warunki – ale bez ozdobników i bez wyjaśnień; wyjaśnia wykonawca). Jeśli coś z tej listy musi trafić do części 1 (bez tego nie da się zrozumieć zagadnienia) – oznacz `[P1]`.
3. **Przesunąć z części 1 do części 2** – lista: `- [id h2 albo tytuł h3] temat szczegółu → Rk` (np. „[c03-szlaki] pośrednicy szlaku ceramidowego (kroki 3–4) → R5”). Bez cytowania tekstu.
4. **Uprościć w części 1** (jeśli trzeba) – `- [miejsce] co ma zostać w części 1 (pół linijki)`.
5. **Sekcje części 2** – `Rk. Tytuł · łączy się z [id h2 części 1] · 1 linijka wskazówki (jaki problem rozwiązują te szczegóły / jak je powiązać / czy tabela pomoże)`.
6. **Przejście** – 2–3 zdania (dla kogo jest część 2, co rozszerza).
7. **Błędy i decyzje** – błędy A w obecnym tekście (fakt spoza źródeł, sprzeczność, wzmocnione twierdzenie) z poprawką w pół linijki; linie „Źródło: …” spoza zakresu; czerwona ramka „stare źródło” (tak/nie + 2 zdania, jeśli tak); kotwica ryciny z ChatGPT (z sekcji B/D – czy zostaje w części 1); decyzje do zatwierdzenia (najwyżej 5, po jednej linijce).

Nie zmieniaj żadnych plików poza planem. Nie commituj.
Raport (maks. 6 linijek): bilans, ile pozycji „Dopisać” i „Przesunąć”, błędy A, ramka, decyzje.
