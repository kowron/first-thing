# Przepisanie rozdziałów w stylu STYL.md – stan (dla szefa / następnej sesji)

Polecenie użytkownika (18.11 wieczór; o ~17:40 zgoda na 7 agentów naraz przed resetem limitu tygodniowego): kontynuować podręcznik samodzielnie (bez ChatGPT, bez Fable), maks. 4 agenci naraz, limit może się skończyć. Rozdział 6 zaakceptowany „w miarę okej” – wzorzec. Poradnik z Dropboxa: `PORADNIK_jak_pisac.txt`, streszczony w `STYL.md`.
Handoff dla agentów: `handoff/P-przepisanie.md`.

| Tura | Rozdział | Stan |
|---|---|---|
| 1 | Z07 komórki macierzyste | GOTOWE 18.11 (10 → 17 s.), commit 73775b8 |
| 1 | Z08 dziedziczenie | GOTOWE 18.11 (22 → 30 s., 2 nowe ryc.) – do rewizji: własne wyliczenia 12:3:1 (dynia) i penetracja 0,6 → 30%, oznaczone |
| 1 | Z09 cytogenetyka | GOTOWE 18.11 (17 → 24 s., 2 nowe ryc.) – do rewizji: objaśnienie gwiazdek w tab. 18.3 (wniosek autora) |
| 1 | Z10 płeć | GOTOWE 18.11 (12 → 16 s.), commit 4d62c88 |
| 2 | Z02 cykl komórkowy | GOTOWE 18.11 (13 → 19 s., 2 nowe ryc.) |
| 2 | Z03 apoptoza | GOTOWE 18.11 (13 → 19 s., 1 nowa ryc.); rewizja B1–B13, C14–C24 wplecione |
| 2 | Z04 kwasy nukleinowe | GOTOWE 18.11 (14 → 23 s.; wyjaśnienia z k4/k5 przywrócone; +1 ryc. z banku) |
| 2 | Z05 PCR | GOTOWE 18.11 (18 → 30 s.; wyjaśnienia z k5; +2 ryc. z banku) |
| 3 | Z11 biotechnologia | GOTOWE 18.11 (8 → 18 s., 2 nowe ryc.; przywrócone brakujące fakty Z); Drewa milczy o znakowaniu i wykrywaniu GMO |
| 3 | G (Genomika) | GOTOWE 18.11 (14 → 26 s.; +1 ryc. z banku g-20) |
| – | Z06 | gotowy (17.11) |

Po zakończeniu każdego agenta: commit + push na `ccr-aabe67ae-lcr511`. Na koniec pełny build i PDF dla użytkownika.
Jeśli agent przerwany limitem: wznowić go (SendMessage) albo uruchomić nowego z tym samym zleceniem – handoff każe kontynuować z `stan/zNN-v2.md`.

## Wznowienie po pauzie (18.11, ~18:00; użytkownik: wznowienie za ok. 4 h)
Agenci Z02, Z03, Z04, Z05, Z11 zatrzymani na czysto: każdy zapisał w `stan/zNN-v2.md` sekcję „## WZNOWIENIE” (następny krok, linie źródeł, co już przeczytane, decyzje). Pliki w `robocze/` są w repo.
Wznawiać: SendMessage do starego agenta (pełny kontekst) albo nowy agent z poleceniem: „Kontynuuj handoff `handoff/P-przepisanie.md` dla rozdziału ZNN od sekcji WZNOWIENIE w `stan/zNN-v2.md`; nie czytaj ponownie tego, co ta sekcja oznacza jako przeczytane”. Nowy agent musi i tak przeczytać STYL.md (krótki) – wzorca z06 tylko fragmenty wskazane w notatce.
Kolejność: najpierw Z03 i Z11 (najbliżej końca), potem Z02, Z04, Z05; G na końcu.

## 18.11, 18:09 – nowa decyzja użytkownika
Maks. **2 agenci naraz**; gdy jeden skończy, wchodzi następny (bez przerywania w losowym momencie). Praca ciągła do resetu limitu 5 h o 20:19. Fable = advisor.
Kolejka: Z03 + Z11 (wznowione 18:09, SendMessage do starych agentów) → Z02 → Z04 → Z05 → G.

## Do zrobienia po zakończeniu przepisywania
- Błąd składu `splitCols` (lib/browser.js): podział bloku dwukolumnowego wg pozycji z pierwszego przebiegu → kaskadowe prawie puste strony przed h3/rycinami (zgłaszali autorzy Z02, Z04). Naprawić w lib PO zakończeniu wszystkich agentów (nie w trakcie – ich układ jest dostrojony do obecnego zachowania).
- Okładka i „Jak korzystać z podręcznika” – nadal szkice.
- Ryciny z ChatGPT wg `RYCINY_do_ChatGPT.md` (Fable) – wkleić po otrzymaniu od użytkownika.

## Kontrola wierności po przepisaniu (Fable, medium) – handoff `handoff/R2-wiernosc.md`
Wynik: `rewizja/zNN-v2.md`; błędy A recenzent poprawia od razu w rozdziale. Maks. 3 agenci naraz łącznie z autorem G.
| Rozdział | Stan |
|---|---|
| Z05 | PRZERWANY limitem 18.11 – nie wznawiać; kontrolę wierności przejmuje plan C1 (pkt 7) |
| Z08 | PRZERWANY limitem 18.11 – nie wznawiać; przejmuje plan C1 (pkt 7) |
| Z09 | czeka (gwiazdki w tab. 18.3) |
| Z03, Z02, Z04, Z07, Z10, Z11 | czekają |
| G | po zakończeniu przepisania |

## 18.11, 20:30 – NOWA DECYZJA UŻYTKOWNIKA: dwie części w każdym rozdziale
- Podręcznik ma zawierać WSZYSTKIE informacje z podanych źródeł (zakres zagadnień z rozpiski). Rozdział = część 1 (~70%, najważniejsze w pełni, reszta do zrozumienia) + przejście + część 2 „na piątkę” (~30%, rozszerzenie, mało rycin, dobre tłumaczenie). Ryciny bez zmian.
- Czerwona ramka przed rozdziałami opartymi na starym podręczniku (Jorde ok. 2000/2001 → Z08, Z10; Twyman 2001 → Z07 – do potwierdzenia przez użytkownika).
- Tło stron: leciutko zielone, przejście biały → zielony.
- Ryciny z ChatGPT jutro – teraz zaślepki w miejscach z `RYCINY_do_ChatGPT.md`.
- Role: Fable xhigh = plan i merytoryka (`handoff/C1-plan-czesci.md` → `plany/zNN-czesci.md`); Opus xhigh = wykonanie (`handoff/C2-wykonanie-czesci.md`); infrastruktura – Opus (`handoff/I-infrastruktura.md`).
- Maks. 2 agenci naraz („pracuj spokojnie”). Kontrole wierności R2 (Z05, Z08) przerwane limitem – nie wznawiane; ich zadania przejmuje pkt 7 planu C1.

| Krok | Stan |
|---|---|
| G – dokończenie przepisania | GOTOWE (14 → 26 s.) |
| C1 plan Z03 (pilot) | GOTOWE 21:00 (`plany/z03-czesci.md`; 299 jednostek: P1 62%, P1u 9%, P2 29%; decyzje Z1, Z3 = tak) |
| C1 plan Z02 | GOTOWE 21:50 (`plany/z02-czesci.md`; 75/25; decyzje szefa dopisane) |
| I – infrastruktura | GOTOWE 21:45 (komponenty w KOMPONENTY.md pkt 9; tło #ffffff→#ecf6ef; naprawa wyrównania kolumn: dziury 33 → 5; pełny build 234 s.) |
| C2 wykonanie Z03 (pilot) | po C1 Z03 i I |
| C1/C2 pozostałe: Z02, Z04, Z05, Z06, Z07, Z08, Z09, Z10, Z11, G | kolejno, po 2 agentów |

## Na jutro (19.11) – od czego zacząć
Użytkownik 18.11 ok. 21:30: „po tych agentach zakończ, kontynuujesz jutro na spokojnie”. Maks. 2 agenci naraz.
1. **C2 wykonanie Z03 (pilot)** – Opus xhigh, `handoff/C2-wykonanie-czesci.md` + `plany/z03-czesci.md`. Potem pokazać użytkownikowi rozdział 3 (PDF `--only 03`) do oceny układu część 1 / część 2.
2. Równolegle: **C2 wykonanie Z02** (plan gotowy) albo **C1 plan** kolejnego rozdziału (kolejność: Z04, Z05, Z06, Z07, Z08, Z09, Z10, Z11, G).
3. Czerwona ramka (`box stare`): Z08, Z10 (Jorde ok. 2000) – pewne; Z07 (Twyman 2001) – czeka na odpowiedź użytkownika.
4. Ryciny z ChatGPT (użytkownik przyśle 19.11): wstawić jako `ryciny/cNN-fig-….png` w miejsce zaślepek (KOMPONENTY.md pkt 9); zaślepki wstawiają wykonawcy C2.
5. Pozostałe UWAGI składu po naprawie kolumn: G s. 8, Z05 s. 99 i 106, Z08 s. 155, Z09 s. 195 – wykonawcy C2 poprawią przy przebudowie.

## 18.11, 22:00 – UŻYTKOWNIK: Fable zużywa ~50% kredytów, ma ~25%. Naprawić PRZED kolejnymi agentami (nie uruchamiać nic wg starego C1).
Diagnoza (plany Z02, Z03): plan 127–155 KB (większy niż sam rozdział, 70–80 KB tekstu) – Fable spisał inwentarz WSZYSTKICH 300–430 jednostek, także tych, które już są w rozdziale, z cytatami i gotowymi brzmieniami; czytał rozdział z SVG, całe pliki źródeł (też poza zakresem) i skany (obrazy); 52–91 wywołań narzędzi; ok. 480–550 tys. tokenów na plan ≈ tyle co cały agent Opus.
Naprawa (do wdrożenia 19.11, przed pierwszym agentem):
1. Szef (skrypt, bez LLM) robi pakiet `pakiety/zNN.txt`: zagadnienia z rozpiski + wiersze mapy + lista T z wyciągu + tekst rozdziału bez SVG/HTML (z id h2/h3) + źródło przycięte do zakresu z mapy. Fable czyta 1 plik, maks. ok. 10 wywołań, skany tylko wyjątkowo (maks. 2 strony).
2. Nowy C1 („plan różnicowy”): Fable zapisuje TYLKO różnice – (a) fakty do dopisania (brak w rozdziale): „s. X: fakt”, pogrupowane wg sekcji części 2; (b) co przesunąć z części 1 do 2: id h2/h3 + temat (bez cytowania, bez gotowych brzmień); (c) szkic sekcji części 2 (tytuł + 1 linijka wskazówki); (d) błędy A, decyzje, ramka, rycina. Limit planu ok. 15–20 KB. Brzmienia i lokalizację w tekście robi Opus.
3. Gotowe plany Z02 i Z03 – nie przerabiać; wykonawcy dostają skrót wycięty skryptem (tylko pozycje „brak”, operacje O…, sekcje R…, decyzje), nie cały plik.
4. Liczyć zużycie: po każdym agencie zapisywać tokeny Fable i Opus (tabela niżej); jeśli udział Fable > 30% – zaproponować użytkownikowi Fable „high” zamiast „xhigh”.
| agent | model | tokeny |
|---|---|---|
| plan Z03 | Fable | 482 tys. |
| plan Z02 | Fable | 553 tys. |
| spis rycin | Fable | 257 tys. |
| infrastruktura | Opus | 476 tys. |
| plan Z04 (C1 v2, oszczędny) | Fable | 293 tys. (13 wywołań, plan 19 KB) |
| wykonanie Z03 (C2, pilot) | Opus | 405 tys. (92 wywołania) |
| plan Z05 (C1 v2, xhigh) | Fable | 244 tys. (10 wywołań, plan 20 KB) |
| plan Z06 (C1 v2, high) | Fable | 201 tys. (12 wywołań, plan 19 KB) |
| plan Z07 (C1 v2, high) | Fable | 177 tys. (9 wywołań, plan 19 KB) |
| plan Z08 (C1 v2, high) | Fable | 278 tys. (13 wywołań, plan 20 KB; pakiet 79 tys. tok.) |
| plan Z09 (C1 v2, high) | Fable | 190 tys. (9 wywołań, plan 17 KB) |
| plan Z10 (C1 v2, high) | Fable | 203 tys. (11 wywołań, plan 18 KB) |
| plan Z11 (C1 v2, high) | Fable | 184 tys. (8 wywołań, plan 13 KB) |
| plan G (C1 v2, high) | Fable | 268 tys. (12 wywołań, plan 22 KB; pakiet 85 tys. tok.) |

## 19.11 rano – wdrożona naprawa kosztów planowania
- `narzedzia/pakiet.py` → `pakiety/zNN.txt` (04–11, 01): 40–85 tys. tokenów na pakiet (rozpiska, mapa, T z wyciągu, tekst rozdziału bez SVG, źródła przycięte do zakresu).
- `handoff/C1-plan-czesci.md` v2: plan różnicowy, ≤18 KB, ≤12 wywołań, tylko pakiet + STYL.md.
- Skróty planów Z02/Z03: `plany/z02-czesci-skrot.md` (81 KB), `plany/z03-czesci-skrot.md` (67 KB) – bez inwentarza.
- Uruchomione (2 agentów): C2 wykonanie Z03 (Opus, pilot) + C1 v2 plan Z04 (Fable).
- Kolejka: C2 Z02 → C1 Z05, Z06, Z07, Z08, Z09, Z10, Z11, G (po każdym planie – C2 tego rozdziału).

- 19.11: C1 v2 Z04 gotowy (293 tys. tokenów vs 480–550 tys. wcześniej). Uruchomiony C1 v2 Z05 (Fable).

- 19.11: UŻYTKOWNIK ZGODA – Fable (plany C1) na wysiłku **high** zamiast xhigh, od kolejnego planu (Z05 już uruchomiony na xhigh – dokończy).
- 19.11: C2 Z03 (pilot) GOTOWE – 19 → 27 s. (cz. 1: 17 s., cz. 2: 10 s.); PDF dla użytkownika `Rozdzial_03_pilotaz_dwie_czesci.pdf`. CZEKAMY na ocenę pilotażu przed kolejnymi C2. Plany C1 idą dalej (Z05 xhigh, Z06 high).
- 19.11: czerwona ramka „stare źródło” – decyzja szefa: Z07 (Twyman 2001), Z08, Z10 (Jorde ok. 2000).
- 19.11: ZLECENIODAWCA – pilotaż Z03 zaakceptowany („wszystko dobrze, robisz tak wszystkie rozdziały”). Zagadnienia Jordego piszemy wg Jordego 2000 (nie Drewy) + ramka (ZASADY pkt 9 nowa wersja). Fable – medium i minimalnie (plany gotowe). Użytkownik da sygnał końca (chce zużyć ok. 60% limitu) – wtedy dokończyć bieżących agentów i stop.
- 19.11: WSZYSTKIE PLANY GOTOWE (Z02–Z11, G). Czekamy na ocenę pilotażu Z03 przez użytkownika; potem C2 (Opus xhigh) po 2 naraz: Z02, Z04, Z05, Z06, Z07, Z08, Z09, Z10, Z11, G.
- 19.11: C2 Z02 GOTOWE – 19 → 29 s. (cz. 1: 19 s., cz. 2: 10 s.). Uruchomiony C2 Z05.
- 19.11: C2 Z04 GOTOWE – 23 → 33 s. (cz. 1: 21 s., cz. 2: 12 s.); 9 błędów A poprawionych, skany sprawdzone. Uruchomiony C2 Z06.
- 19.11: C2 Z05 GOTOWE – 30 → 35 s. (cz. 1: 27 s., cz. 2: 8 s.); fakty spoza rozpiski usunięte; 8 miejsc na skanie zgodnych. Karta ryciny 5: „mRNA (tylko eksony)” → „mRNA”. Uruchomiony C2 Z07.
- 19.11: C2 Z06 GOTOWE – 20 → 24 s. (cz. 1: 17 s., cz. 2: 7 s.); tab. 29.2 ze skanu; skany: przesunięcie +25 w tej części Drewy. Uruchomiony C2 Z08.
- 19.11: C2 Z07 GOTOWE – 17 → 22 s. (cz. 1: 14 s., cz. 2: 8 s.); ramka Twyman; skany 6/7 zgodne. Aksolotl – pół zdania wg rozpiski (jak Bar/Chironomus w Z08).
- 19.11: UŻYTKOWNIK: po zakończeniu bieżących prac (Z07, Z08) – STOP. Następna sesja: C2 Z09, Z10, Z11, G (plany gotowe), potem pełny build, ryciny z ChatGPT.
- 19.11: C2 Z08 GOTOWE – 29 → 41 s. (cz. 1: 27 s., cz. 2: 14 s.); mitochondria wg Jordego; ramka; skany sprawdzone (przesunięcie +28 w r. 2, 13, 16). STOP na polecenie użytkownika.

## Następna sesja – od czego zacząć
1. C2 (Opus xhigh, po 2 naraz): Z09 (`plany/z09-czesci.md`), Z10 (`plany/z10-czesci.md` – Jorde wg wyd. 2000, ramka), Z11 (`plany/z11-czesci.md`), G (`plany/z01-czesci.md`). Prompt jak dla Z04–Z08 (karta ryciny: Z09 → 9, Z10 → 10 i 11, Z11 → 12, G → 1).
2. Pełny build `node build.mjs`, PDF dla użytkownika.
3. Ryciny z ChatGPT → `ryciny/cNN-fig-….png` w miejsce zaślepek (KOMPONENTY pkt 9).
4. Do decyzji użytkownika: nazwiska z błędami w Drewie (Singer/Signer, Tijo/Tjio – pominięte w Z04), aksolotl w Z07 (z rozpiski).
- 19.11 wieczór: C2 Z11 GOTOWE – 18 → 27 s. (cz. 1: 18 s., cz. 2: 9 s.). Z09, Z10 w toku; po nich STOP (G czeka na znak użytkownika).
- 19.11 wieczór: C2 Z10 GOTOWE – 16 → 24 s. (cz. 1: 16 s., cz. 2: 8 s.); Jorde wg wyd. 2000 + ramka; skan s. 459: liczby Y sprzeczne w druku – ramka „uwaga” zostaje łagodna.
- 19.11 wieczór: C2 Z09 GOTOWE – 24 → 31 s. (cz. 1: 21 s., cz. 2: 10 s.). STOP – został tylko G (C2 wg `plany/z01-czesci.md`, karta ryciny 1), potem pełny build i ryciny z ChatGPT. Czekamy na znak użytkownika.
- 19.11 wieczór: C2 G GOTOWE – 26 → 37 s. (cz. 1: 25 s., cz. 2: 12 s.). PEŁNY BUILD: 335 s., 0 błędów, 0 uwag, 94 ryciny (12 zaślepek). PDF wysłany użytkownikowi. ZOSTAJE: (1) ryciny z ChatGPT → `ryciny/cNN-fig-….png` w miejsce 12 zaślepek; (2) rewizja/sprawdzenie błędów nowego tekstu (części 2) i redakcja całości – DOPIERO na znak użytkownika.
- 20.11: 12 rycin z ChatGPT wstawionych (`ryciny/`), pełny build 335 s., 0/0. Użytkownik: nazwisk z błędami (Singer, Tijo) NIE podawać. Zostaje: rewizja – na znak użytkownika; aksolotl w Z07 – bez decyzji.

## 20.11 – REWIZJA (test łańcuszka zleconego przez użytkownika)
Łańcuszek: 6× Sonnet xhigh (zgłaszają wszystko podejrzane → `rewizja3/zNN.md`, handoff `handoff/R3-rewizja-sonnet.md`) → 1× Fable medium (weryfikuje, potwierdza/odrzuca, wypisuje błędy do `rewizja3/POTWIERDZONE.md`: tekst – gotowe brzmienia zamiany; skład/ryciny – lista) → 1× Sonnet (wkleja poprawki tekstu w całym podręczniku) + 1× Opus (skład, układ, ryciny w całym podręczniku). Na koniec raport tokenów: Fable / Sonnet / Opus i na co poszło najwięcej.
Podział Sonnetów: G+Z11 · Z02+Z03 · Z04+Z06 · Z05+Z07 · Z08+Z10 · Z09+strony wstępne. Uruchomieni 20.11.
| agent | model | tokeny |
|---|---|---|
| wstawienie 12 rycin | Opus | 138 tys. |
| rewizja G+Z11 | Sonnet | 603 tys. |
| rewizja Z02+Z03 | Sonnet | 520 tys. |
| rewizja Z04+Z06 | Sonnet | 551 tys. |
| rewizja Z05+Z07 | Sonnet | 522 tys. |
| rewizja Z08+Z10 | Sonnet | 661 tys. |
| rewizja Z09+front | Sonnet | 527 tys. |
- 20.11: 6 raportów Sonneta gotowych (`rewizja3/`, ok. 580 pozycji). Uruchomiony Fable medium – weryfikacja (`handoff/R3-weryfikacja-fable.md` → `rewizja3/POTWIERDZONE.md`). Potem: 1 Sonnet (sekcje A – wklejanie) i 1 Opus (sekcje B – skład/ryciny), pełny build, raport tokenów.
- 20.11: WERYFIKACJA GOTOWA – `rewizja3/POTWIERDZONE.md` (front + z01–z11): 127 bloków ZNAJDŹ/ZAMIEŃ (sekcje A), ok. 95 pozycji składu (sekcje B), sekcja D (10 pozycji); decyzje użytkownika: `rewizja3/DECYZJE-ZLECENIODAWCY.md` (D-1…D-6; D-7…D-10 bez decyzji – zostawić bez zmian). STOP na polecenie użytkownika.
- WIECZOREM (na znak użytkownika): 1× Sonnet – wkleić wszystkie bloki A z POTWIERDZONE.md (mechanicznie); 1× Opus – wszystkie sekcje B + D-2, D-3, D-6 z DECYZJE; potem pełny build, PDF, raport tokenów (Fable / Sonnet / Opus). Okładka – osobno, od nowa, później.
| weryfikacja front+z01–z06 | Fable medium | 343 tys. |
- 20.11 wieczór: REWIZJA ZAKOŃCZONA – 128 zamian tekstu (Sonnet), skład/ryciny/spis/„Jak korzystać”/wykaz źródeł/wyprowadzenie PI (Opus), nowa okładka (Fable max; `narzedzia/okladka/`). Pełny build: 339 s., 0/0. PDF: `Biologia_molekularna_podrecznik_2026-11-20_po_rewizji.pdf`.
- Zostało drobne: ramka „Dalej: część 2” sama na stronie w z07, z10, z11; kilka luk 5–6 cm przed rycinami; czcionka PNG ryc. genu samobójczego (z11) – tylko nowym plikiem z ChatGPT.
| poprawki tekstu (128 zamian) | Sonnet | 72 tys. |
| weryfikacja z07–z11 | Fable low | 180 tys. |
| skład, ryciny, spis, PI | Opus | 460 tys. |
| okładka | Fable max | 634 tys. |
