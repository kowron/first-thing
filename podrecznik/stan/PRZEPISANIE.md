# Przepisanie rozdziałów w stylu STYL.md – stan (dla szefa / następnej sesji)

Polecenie użytkownika (18.11 wieczór; o ~17:40 zgoda na 7 agentów naraz przed resetem limitu tygodniowego): kontynuować podręcznik samodzielnie (bez ChatGPT, bez Fable), maks. 4 agenci naraz, limit może się skończyć. Rozdział 6 zaakceptowany „w miarę okej” – wzorzec. Poradnik z Dropboxa: `PORADNIK_jak_pisac.txt`, streszczony w `STYL.md`.
Handoff dla agentów: `handoff/P-przepisanie.md`.

| Tura | Rozdział | Stan |
|---|---|---|
| 1 | Z07 komórki macierzyste | GOTOWE 18.11 (10 → 17 s.), commit 73775b8 |
| 1 | Z08 dziedziczenie | GOTOWE 18.11 (22 → 30 s., 2 nowe ryc.) – do rewizji: własne wyliczenia 12:3:1 (dynia) i penetracja 0,6 → 30%, oznaczone |
| 1 | Z09 cytogenetyka | GOTOWE 18.11 (17 → 24 s., 2 nowe ryc.) – do rewizji: objaśnienie gwiazdek w tab. 18.3 (wniosek autora) |
| 1 | Z10 płeć | GOTOWE 18.11 (12 → 16 s.), commit 4d62c88 |
| 2 | Z02 cykl komórkowy | uruchomiony 18.11 |
| 2 | Z03 apoptoza (rewizja B do naniesienia) | uruchomiony 18.11 |
| 2 | Z04 kwasy nukleinowe (przywrócić wyjaśnienia z k4/k5) | uruchomiony 18.11 ~17:40 |
| 2 | Z05 PCR (przywrócić wyjaśnienia z k5) | uruchomiony 18.11 ~17:40 |
| 3 | Z11 biotechnologia | uruchomiony 18.11 ~17:40 |
| 3 | G (Genomika) | czeka – po 18:00 (Fable jako advisor wg użytkownika) |
| – | Z06 | gotowy (17.11) |

Po zakończeniu każdego agenta: commit + push na `ccr-aabe67ae-lcr511`. Na koniec pełny build i PDF dla użytkownika.
Jeśli agent przerwany limitem: wznowić go (SendMessage) albo uruchomić nowego z tym samym zleceniem – handoff każe kontynuować z `stan/zNN-v2.md`.
