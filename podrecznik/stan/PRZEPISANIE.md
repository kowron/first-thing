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
| 2 | Z04 kwasy nukleinowe | WZNOWIONY ~18:45 (plan + mapa k4/k5 w `stan/z04-v2.md`) |
| 2 | Z05 PCR | WZNOWIONY ~19:00 (użytkownik: 3 agenci naraz; plan + mapa k5 w `stan/z05-v2.md`) |
| 3 | Z11 biotechnologia | GOTOWE 18.11 (8 → 18 s., 2 nowe ryc.; przywrócone brakujące fakty Z); Drewa milczy o znakowaniu i wykrywaniu GMO |
| 3 | G (Genomika) | czeka – nie zaczęty |
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
