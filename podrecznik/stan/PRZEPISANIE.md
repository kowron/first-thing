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
- 19.11: WSZYSTKIE PLANY GOTOWE (Z02–Z11, G). Czekamy na ocenę pilotażu Z03 przez użytkownika; potem C2 (Opus xhigh) po 2 naraz: Z02, Z04, Z05, Z06, Z07, Z08, Z09, Z10, Z11, G.
