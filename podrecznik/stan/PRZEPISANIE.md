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
| 3 | G (Genomika) | uruchomiony ~19:15 (przywrócić wyjaśnienia z material/genomika.txt; cel 20–26 s.; stan w `stan/g-v2.md`) |
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
| G – dokończenie przepisania | wznowiony 19:35 |
| C1 plan Z03 (pilot) | uruchomiony 19:40 |
| I – infrastruktura | po G |
| C2 wykonanie Z03 (pilot) | po C1 Z03 i I |
| C1/C2 pozostałe: Z02, Z04, Z05, Z06, Z07, Z08, Z09, Z10, Z11, G | kolejno, po 2 agentów |
