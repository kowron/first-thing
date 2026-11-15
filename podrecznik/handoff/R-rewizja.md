# Handoff R – rewizja (Fable, medium)

## Część A – rewizja merytoryczna rozdziałów (3 agentów równolegle)
Podział: R1 = Z02, Z03, Z07 · R2 = Z08, Z09, Z10 · R3 = Z04, Z05, Z06, Z11, G.
Dla każdego rozdziału czytasz: rozdział (`rozdzialy/zNN-*.html`), wyciąg (`wyciagi/zNN.md`), `stan/zNN.md`; ze źródeł (`/tmp/claude-0/-home-user-first-thing/600b873f-e07d-5766-b2f4-6a90b68ae091/scratchpad/zrodla/zNN/`) tylko fragmenty potrzebne do sprawdzenia.
Sprawdzasz, w tej kolejności:
1. **Zgodność ze źródłem** – każda liczba, nazwa, kolejność etapów, kierunek zależności; treści spoza źródeł (mają zniknąć).
1a. **Stary Jorde** (Z08, Z10): sprawdź, że z Jordego wzięto tylko to, czego nie ma w Drewie do tych samych zajęć, i że nie przeniesiono danych przestarzałych.
2. **Cięcia** – lista `T` w wyciągu: czy nie ucięto rzeczy podstawowej (definicja, etap, klasyfikacja, typowe pytanie egzaminacyjne) i czy nie zostawiono balastu. Cel 10–30% cięć, zależnie od wagi tematu.
3. **Tłumaczenie** – miejsca niezrozumiałe, przeskoki, zbyt gęste akapity.
4. **Ryciny** – zgodność z tekstem i źródłem; zbędne lub brakujące.
Nie poprawiasz plików. Wynik: `rewizja/zNN.md` – lista poprawek (miejsce → co jest → co ma być → strona źródła), z priorytetem A (błąd) / B (ważne) / C (kosmetyka). Maks. 40 pozycji na rozdział.

## Część B – redakcja całości (1 agent, po naniesieniu poprawek z części A)
Czytasz wszystkie rozdziały (bez źródeł). Sprawdzasz: jednolitą terminologię i pisownię, powtórzenia między rozdziałami (np. elektroforeza w Z04 i Z06, PCR w Z05 i Z06, chromosom w Z04 i Z09, dziedziczenie w Z08 i Z10) – zostaje pełny opis w jednym miejscu i odsyłacz w drugim; proporcje (czy któryś rozdział jest za gęsty/za rzadki względem wagi); spójność rycin. Wynik: `rewizja/calosc.md` – lista poprawek jak wyżej.
