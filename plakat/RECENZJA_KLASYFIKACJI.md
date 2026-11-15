# Recenzja klasyfikacji mięśni na plakacie – wg Bochenka t. I

Zakres: przeczytane w całości strony OCR 648–733 (grzbiet 649–677, klatka 677–702, brzuch 702–733, razem ze streszczeniami 675–677, 700–702, 730–733). Porównane z `plakat_m1.txt`, `plakat_m2.txt`, `plakat_m3.txt` oraz z `plakat/data.py` i `plakat/build.py` (sekcje I–III). Żaden plik plakatu nie został zmieniony.

Oznaczenia: **BŁĄD** = sprzeczne z Bochenkiem; **BRAK** = u Bochenka jest, na plakacie nie ma; **NIEJASNE** = zgodne, ale mylące albo sformułowane inaczej niż u Bochenka.

---

## 0. Najważniejsze wnioski

1. **Grzbiet, mięśnie głębokie – pasma.** Plakat pokazuje „pasmo boczne / pasmo przyśrodkowe” tylko jako podział mięśni długich. U Bochenka (s. 659) oba pasma obejmują całą właściwą mięśniówkę grzbietu: mięśnie krótkie i podpotyliczne też należą „czy to do pasma przyśrodkowego, czy też do bocznego”. Na plakacie mm. międzykolcowe, mm. międzypoprzeczne i mięśnie podpotyliczne nie mają żadnego przypisania do pasma (G1, G4, G5).
2. **Brak „układów”** (poprzeczno-kolcowy, międzykolcowy, międzypoprzeczny, przebieg kolcowo-poprzeczny), z których Bochenek buduje pasma. Bez nich nie widać, że m. kolcowy i mm. międzykolcowe to jeden układ, a m. krzyżowo-grzbietowy i mm. międzypoprzeczne – drugi (G3).
3. **Mm. skręcające.** Na s. 659 Bochenek wylicza je wśród mięśni krótkich, na s. 669 opisuje wśród długich. Plakat pokazuje tylko połowę tej niezgodności (ostrzeżenie jest w `data.py`, ale karta „bare” go nie wyświetla). „Pięć mięśni długich” to: mm. płatowate, m. krzyżowo-grzbietowy, m. kolcowy, m. półkolcowy, m. wielodzielny (G6).
4. **Błędne poziomy drzewa.** M. półkolcowy nie istnieje na plakacie jako mięsień – są dwie osobne karty jego części (G7). To samo w klatce: brak poziomu „mm. międzyżebrowe”, przez co skład 3-elementowy Bochenka wygląda jak 4 równorzędne mięśnie (K1).
5. **Krótkie mięśnie grzbietu** – brak podziału ze s. 669 na właściwe mięśnie grzbietu (gałęzie tylne) i mięśnie pochodzenia wentralnego (gałęzie przednie); cztery rodzaje mm. międzypoprzecznych nie są rozróżnione (G4).
6. Drobniejsze: odmiana wpisana jako „część” m. równoległobocznego (G11); m. najszerszy grzbietu bez wiersza części (G12); „do łopatki i k. ramiennej” (G13); dźwigacz jądra jako czwarta karta pod nagłówkiem „3 warstwy” (B1); pytania przy rozgałęzieniach nie oddają kryteriów Bochenka (G2, G9, K2).

Brzuch jest zgodny z Bochenkiem co do grup i kolejności; uwagi dotyczą tylko jasności.

---

## 1. Proponowane drzewa klasyfikacji (dokładnie wg Bochenka)

### 1.1 MIĘŚNIE GRZBIETU (s. 649–677)

```
MIĘŚNIE GRZBIETU – „dwie wielkie grupy, położone jedna na drugiej, różniące się budową i pochodzeniem” (s. 649)
│
├─ POWIERZCHOWNE MIĘŚNIE GRZBIETU (s. 650) – mięśnie szerokie; należą głównie do kończyny górnej; z mięśniówki
│  │   brzusznej, przewędrowały na grzbiet; gałęzie brzuszne nn. rdzeniowych – 2 podgrupy, razem 3 warstwy
│  │
│  ├─ Mięśnie kolcowo-ramienne (mm. spinohumerales*) – zdążają do kończyny górnej; 2 warstwy (s. 650)
│  │   ├─ [warstwa pierwsza]
│  │   │   ├─ m. czworoboczny (m. trapezius)
│  │   │   │     • część górna – zstępująca (pars descendens)
│  │   │   │     • część środkowa – poprzeczna (pars transversa)
│  │   │   │     • część dolna – wstępująca (pars ascendens)
│  │   │   └─ m. najszerszy grzbietu (m. latissimus dorsi)
│  │   │         • pars vertebralis • pars iliaca • pars costalis • pars scapularis   (tylko łacina, s. 652)
│  │   └─ [warstwa druga, głębsza – s. 657]
│  │       ├─ m. równoległoboczny (m. rhomboideus)
│  │       │     • część górna (szyjna) – m. równoległoboczny mniejszy (m. rhomboideus minor)
│  │       │     • część dolna (grzbietowa) – m. równoległoboczny większy (m. rhomboideus major)
│  │       └─ dźwigacz łopatki (m. levator scapulae)
│  │
│  └─ Mięśnie kolcowo-żebrowe (mm. spinocostales*) – „trzecia z kolei warstwa mięśni powierzchownych” (s. 650)
│      └─ mm. zębate tylne (mm. serrati posteriores)
│            ├─ m. zębaty tylny górny (m. serratus posterior superior)
│            └─ m. zębaty tylny dolny (m. serratus posterior inferior)
│
└─ GŁĘBOKIE MIĘŚNIE GRZBIETU (s. 658–673) – „przeważnie, choć nie wyłącznie, właściwe mięśnie grzbietu”;
   │   gałęzie tylne nn. rdzeniowych; cała mięśniówka = prostownik grzbietu (erector spinae) – s. 659
   │   Podział opisowy (nagłówki + streszczenie): 1) długie, 2) krótkie, 3) podpotyliczne.
   │   Podział morfologiczny (s. 659), przecinający wszystkie trzy grupy: PASMO BOCZNE / PASMO PRZYŚRODKOWE.
   │
   ├─ DŁUGIE MIĘŚNIE GRZBIETU (s. 659–669) – pięć mięśni długich + mm. skręcające
   │   │
   │   ├─ pasmo boczne
   │   │   ├─ Mięśnie kolcowo-poprzeczne (m. spinotransversalis) – jedyne o przebiegu kolcowo-poprzecznym
   │   │   │   └─ (1) mm. płatowate (mm. splenii)
   │   │   │         • m. płatowaty głowy (m. splenius capitis) – część większa, górna
   │   │   │         • m. płatowaty szyi (m. splenius cervicis) – część mniejsza, dolna
   │   │   └─ Mięsień krzyżowo-grzbietowy – układ międzypoprzeczny (razem z mm. międzypoprzecznymi)
   │   │       └─ (2) m. krzyżowo-grzbietowy (m. sacrospinalis*) – wspólna masa; ku górze dwa pasma:
   │   │             ├─ m. biodrowo-żebrowy (m. iliocostalis) – część boczna m. krzyżowo-grzbietowego
   │   │             │     • m. biodrowo-żebrowy lędźwi (m. iliocostalis lumborum)
   │   │             │     • m. biodrowo-żebrowy klatki piersiowej (m. iliocostalis thoracis)
   │   │             │     • m. biodrowo-żebrowy szyi (m. iliocostalis cervicis)
   │   │             └─ m. najdłuższy (m. longissimus) – pasmo przyśrodkowe m. krzyżowo-grzbietowego
   │   │                   • m. najdłuższy klatki piersiowej (m. longissimus thoracis)
   │   │                   • m. najdłuższy szyi (m. longissimus cervicis)
   │   │                   • m. najdłuższy głowy (m. longissimus capitis)
   │   │
   │   └─ pasmo przyśrodkowe
   │       ├─ Mięsień kolcowy – część główna układu międzykolcowego (razem z mm. międzykolcowymi)
   │       │   └─ (3) m. kolcowy (m. spinalis)
   │       │         • m. kolcowy klatki piersiowej (m. spinalis thoracis)
   │       │         • m. kolcowy szyi (m. spinalis cervicis)
   │       │         • m. kolcowy głowy (m. spinalis capitis) – występuje jako odmiana
   │       └─ Mięśnie poprzeczno-kolcowe (mm. transversospinales) – układ poprzeczno-kolcowy; 3 warstwy (s. 667)
   │           ├─ warstwa powierzchowna: (4) m. półkolcowy (m. semispinalis)
   │           │     • m. półkolcowy klatki piersiowej i szyi (m. semispinalis thoracis et cervicis)
   │           │     • m. półkolcowy głowy (m. semispinalis capitis)
   │           │           – część przyśrodkowa: m. dwubrzuścowy głowy (m. biventer capitis*)
   │           │           – część boczna: m. spleciony większy (m. complexus major*)
   │           ├─ warstwa środkowa: (5) m. wielodzielny (m. multifidus)
   │           └─ warstwa głęboka: mm. skręcające (mm. rotatores)   ! s. 659: krótkie; s. 669: opisane tutaj
   │                 • długie (rotatores longi*) – mijają jeden kręg
   │                 • krótkie (rotatores breves*) – do sąsiedniego, wyżej leżącego kręgu
   │                 • wg okolic: mm. rotatores thoracis, mm. rotatores cervicis, mm. rotatores lumborum
   │
   ├─ KRÓTKIE MIĘŚNIE GRZBIETU (s. 669–671) – między dwoma sąsiednimi kręgami; budowa metameryczna
   │   │
   │   ├─ właściwe mięśnie grzbietu (gałęzie tylne nn. rdzeniowych) – s. 669
   │   │   ├─ mm. międzykolcowe (mm. interspinales) – PASMO PRZYŚRODKOWE (układ międzykolcowy)
   │   │   │     • mm. interspinales cervicis (parzyste) • mm. interspinales lumborum (nieparzyste)
   │   │   │     • mm. interspinales thoracis (przeważnie zanikły)
   │   │   │   └─ m. krzyżowo-guziczny tylny (m. sacrococcygeus dorsalis) – pozostałość mm. międzykolcowych
   │   │   └─ mm. międzypoprzeczne (mm. intertransversarii) – PASMO BOCZNE (układ międzypoprzeczny); z nich właściwe to:
   │   │         • mm. międzypoprzeczne tylne szyi (mm. intertransversarii posteriores cervicis)
   │   │         • mm. międzypoprzeczne przyśrodkowe lędźwi (mm. intertransversarii mediales lumborum)
   │   │
   │   └─ mięśnie pochodzenia wentralnego (gałęzie przednie nn. rdzeniowych) – s. 669
   │       ├─ mm. międzypoprzeczne przednie szyi (mm. intertransversarii anteriores cervicis)
   │       ├─ mm. międzypoprzeczne boczne lędźwi (mm. intertransversarii laterales lumborum) → także tylne mięśnie brzucha (s. 712)
   │       │   └─ m. krzyżowo-guziczny przedni (m. sacrococcygeus ventralis) – „ta sama grupa co mm. międzypoprzeczne boczne”
   │       └─ mm. dźwigacze żeber (mm. levatores costarum)
   │             • mm. levatores costarum breves • mm. levatores costarum longi
   │
   └─ MIĘŚNIE PODPOTYLICZNE (mm. suboccipitales) – 5 mięśni (s. 671–673)
       ├─ m. skośny górny głowy (m. obliquus capitis superior) – PASMO BOCZNE (najwyższy tylny m. międzypoprzeczny szyi)
       ├─ m. prosty tylny mniejszy głowy (m. rectus capitis posterior minor) – PASMO PRZYŚRODKOWE (najwyższy m. międzykolcowy szyi)
       ├─ m. prosty tylny większy głowy (m. rectus capitis posterior major) – PASMO PRZYŚRODKOWE (z drugiego m. międzykolcowego szyi)
       ├─ m. skośny dolny głowy (m. obliquus capitis inferior) – PASMO PRZYŚRODKOWE (przypuszczalnie z m. międzykolcowego)
       └─ m. prosty boczny głowy (m. rectus capitis lateralis) – pochodzenia wentralnego (najwyższy m. międzypoprzeczny przedni szyi)
```

Kolejność mm. międzypoprzecznych w tekście Bochenka (s. 670) i w streszczeniu jest inna niż w drzewie powyżej: przednie szyi → tylne szyi → boczne lędźwi → przyśrodkowe lędźwi, jako jedna pozycja „mm. międzypoprzeczne”. Jeśli plakat ma zachować jedną kartę mm. międzypoprzecznych w kolejności Bochenka, to każdy z czterech rodzajów musi dostać znacznik „właściwy m. grzbietu / pochodzenia wentralnego” (patrz G4).

**Ten sam podział jako tabela (s. 659, 667, 669–671):**

| grupa opisowa | pasmo boczne | pasmo przyśrodkowe | poza pasmami – pochodzenia wentralnego |
|---|---|---|---|
| długie | mm. płatowate (przebieg kolcowo-poprzeczny); m. krzyżowo-grzbietowy = m. biodrowo-żebrowy + m. najdłuższy (układ międzypoprzeczny) | m. kolcowy (układ międzykolcowy); m. półkolcowy, m. wielodzielny, mm. skręcające (układ poprzeczno-kolcowy) | – |
| krótkie | mm. międzypoprzeczne tylne szyi i przyśrodkowe lędźwi (układ międzypoprzeczny) | mm. międzykolcowe, m. krzyżowo-guziczny tylny (układ międzykolcowy); wg s. 659 także mm. skręcające | mm. międzypoprzeczne przednie szyi i boczne lędźwi, m. krzyżowo-guziczny przedni, mm. dźwigacze żeber |
| podpotyliczne | m. skośny górny głowy | m. prosty tylny mniejszy głowy, m. prosty tylny większy głowy, m. skośny dolny głowy | m. prosty boczny głowy |

Uwaga do tabeli: Bochenek na s. 659 pisze ogólnie, że pasmo boczne tworzą „mm. międzypoprzeczne”; zawężenie do tylnych szyi i przyśrodkowych lędźwi wynika ze s. 670 („tylko [one] należą do właściwej mięśniówki grzbietu”). To połączenie dwóch miejsc tekstu, nie jedno zdanie Bochenka.

### 1.2 MIĘŚNIE KLATKI PIERSIOWEJ (s. 677–702)

```
MIĘŚNIE KLATKI PIERSIOWEJ – pochodne mięśniówki brzusznej tułowia, gałęzie przednie nn. rdzeniowych;
│                            „trzy odrębne zespoły” (s. 677)
│
├─ 1) POWIERZCHOWNE MIĘŚNIE KLATKI PIERSIOWEJ (s. 678–684) – przyczepiają się do kośćca okolicy barku i ramienia
│   ├─ m. piersiowy większy (m. pectoralis major)
│   │     • część obojczykowa (pars clavicularis) • część mostkowo-żebrowa (pars sternocostalis)
│   │     • część brzuszna (pars abdominalis) – czasami może jej brakować
│   ├─ m. piersiowy mniejszy (m. pectoralis minor)
│   ├─ m. podobojczykowy (m. subclavius)
│   └─ m. zębaty przedni (m. serratus anterior)
│         • część górna • część środkowa • część dolna   (bez łaciny u Bochenka)
│
├─ 2) GŁĘBOKIE ALBO WŁAŚCIWE MIĘŚNIE KLATKI PIERSIOWEJ (s. 684–689) – właściwe mięśnie ściany klatki piersiowej
│   │   „Mięśniówka ta składa się z mm. międzyżebrowych, mm. podżebrowych i m. poprzecznego klatki piersiowej” (s. 685)
│   ├─ mm. międzyżebrowe (mm. intercostales) – „w dwóch zasadniczych warstwach” (s. 685)
│   │   ├─ mm. międzyżebrowe zewnętrzne (mm. intercostales externi)   [ku przodowi: błony międzyżebrowe zewnętrzne]
│   │   └─ mm. międzyżebrowe wewnętrzne (mm. intercostales interni)   [ku tyłowi: błony międzyżebrowe wewnętrzne]
│   │         • warstwa zewnętrzna: mm. międzyżebrowe pośrednie (mm. intercostales intermedii*)
│   │         • warstwa wewnętrzna: mm. międzyżebrowe najgłębsze (mm. intercostales intimi)
│   ├─ mm. podżebrowe (mm. subcostales)
│   └─ m. poprzeczny klatki piersiowej (m. transversus thoracis)
│
└─ 3) PRZEPONA (diaphragma) (s. 689–696) – przegroda między jamą klatki piersiowej a jamą brzuszną
      • część lędźwiowa (pars lumbalis): odnoga prawa (crus dextrum), odnoga lewa (crus sinistrum);
        więzadła łukowate: pośrodkowe (lig. arcuatum medianum), przyśrodkowe (lig. arcuatum mediale), boczne (lig. arcuatum laterale)
      • część żebrowa (pars costalis)
      • część mostkowa (pars sternalis)
      • środek ścięgnisty (centrum tendineum) – wspólne ścięgno końcowe wszystkich trzech części
```

Drugi, równoległy podział Bochenka (s. 677–678, powtórzony na s. 703): właściwa mięśniówka przednio-bocznej ściany klatki piersiowej ma u ssaków **trzy warstwy** – mm. międzyżebrowe zewnętrzne, mm. międzyżebrowe wewnętrzne, m. poprzeczny klatki piersiowej. Ten podział nie wymienia mm. podżebrowych; streszczenie (s. 700) też je pomija.

### 1.3 MIĘŚNIE BRZUCHA (s. 702–733)

```
MIĘŚNIE BRZUCHA (s. 702)
│
├─ BOCZNE I PRZEDNIE MIĘŚNIE BRZUCHA (s. 704–712)
│   ├─ boczne mięśnie brzucha – 3 warstwy (s. 702–703); „trzy boczne mięśnie brzucha” (s. 707);
│   │   │                        inaczej: mięśnie szerokie brzucha (s. 716–717), mm. płaskie (s. 731–732)
│   │   ├─ m. skośny zewnętrzny brzucha (m. obliquus externus abdominis)
│   │   ├─ m. skośny wewnętrzny brzucha (m. obliquus internus abdominis)
│   │   ├─ m. poprzeczny brzucha (m. transversus abdominis)
│   │   └─ (pochodna dwóch ostatnich, nie czwarta warstwa) dźwigacz jądra (m. cremaster)
│   └─ przednie mięśnie brzucha – układ mięśni prostych; jedyne miejsce bez podziału na warstwy (s. 704)
│       ├─ m. prosty brzucha (m. rectus abdominis)
│       └─ m. piramidowy (m. pyramidalis)
│
└─ TYLNE MIĘŚNIE BRZUCHA (s. 712–715)
    ├─ grupa mm. międzypoprzecznych bocznych lędźwi (mm. intertransversarii laterales lumborum) – opis s. 670
    └─ m. czworoboczny lędźwi (m. quadratus lumborum)
          • warstwa przednia • warstwa tylna
```

---

## 2. Równoległe podziały mięśni głębokich grzbietu – który jest nadrzędny

Kluczowy akapit, s. 659 (po poprawieniu literówek OCR):

> „Pasma mięśniowe mogą przebiegać prawie poprzecznie lub skośnie od wyrostków poprzecznych do kolczystych i taki układ nazywamy układem poprzeczno-kolcowym (mm. transversospinales; rotatores, multifidi, semispinales). Inne pasma przybierają kierunek wybitnie podłużny i biegną albo od wyrostków kolczystych do kolczystych, albo od poprzecznych do poprzecznych […]; jest to układ międzykolcowy (mm. spinales et interspinales) oraz międzypoprzeczny (m. sacrospinalis et mm. intertransversarii). Układ poprzecznokolcowy i międzykolcowy stanowią razem pasmo przyśrodkowe, w przeciwieństwie do pasma bocznego. Pasmo boczne jest utworzone przez mm. międzypoprzeczne i wspólną masę m. krzyżowo-grzbietowego (m. sacrospinalis*), który dzieli się na m. biodrowo-żebrowy i m. najdłuższy. Do pasma bocznego zaliczamy również mm. płatowate, są to jedyne mięśnie o przebiegu kolcowo-poprzecznym (m. spinotransversalis). Pasmo boczne i przyśrodkowe stanowią razem wielką grupę: 1) mięśni długich grzbietu, z której wyłączamy 2) mięśnie krótkie grzbietu (mm. intertransversarii, rotatores et mm. interspinales) i 3) mięśnie podpotyliczne (mm. suboccipitales), należące czy to do pasma przyśrodkowego, czy też do bocznego.”

Z tego wynikają trzy piętra:

1. **Układy** – według tego, skąd dokąd biegną pasma mięśniowe: poprzeczno-kolcowy, międzykolcowy, międzypoprzeczny oraz przebieg kolcowo-poprzeczny (tylko mm. płatowate).
2. **Pasma** – układy łączą się w dwa pasma: przyśrodkowe (poprzeczno-kolcowy + międzykolcowy) i boczne (międzypoprzeczny + mm. płatowate). To jest podział morfologiczny całej właściwej mięśniówki grzbietu i w tym sensie jest nadrzędny: mięśnie krótkie i podpotyliczne też do niego należą.
3. **Grupy opisowe** – długie / krótkie / podpotyliczne. To według nich Bochenek układa nagłówki rozdziału i streszczenie (s. 659–673, 675–677). Każda z trzech grup zawiera mięśnie obu pasm (plus mięśnie pochodzenia wentralnego, które do pasm nie należą).

Wniosek dla plakatu: układ kolumn Długie / Krótkie / Podpotyliczne jest zgodny z nagłówkami Bochenka i może zostać. Błędem jest pokazanie pasm jako rozgałęzienia wyłącznie pod „Długimi”. Bochenek sam używa obu zakresów: „pasmo przyśrodkowe długich mięśni grzbietu” (m. kolcowy, s. 667 i 676) oraz „pasmo przyśrodkowe właściwych mięśni grzbietu” (mm. międzykolcowe, s. 669).

Odpowiedzi na pytania szczegółowe:

- **Czy mm. międzypoprzeczne należą do pasma bocznego?** Tak – s. 659: „Pasmo boczne jest utworzone przez mm. międzypoprzeczne i wspólną masę m. krzyżowo-grzbietowego”. Zastrzeżenie ze s. 670: do właściwej mięśniówki grzbietu należą tylko mm. międzypoprzeczne tylne szyi i przyśrodkowe lędźwi; przednie szyi i boczne lędźwi są pochodzenia wentralnego.
- **Czy mm. międzykolcowe i m. kolcowy należą do pasma przyśrodkowego?** Tak. M. kolcowy: „należy do pasma przyśrodkowego długich mięśni grzbietu […] stanowi część główną układu międzykolcowego” (s. 667). Mm. międzykolcowe: „należą do pasma przyśrodkowego właściwych mięśni grzbietu” (s. 669); streszczenie: „przyśrodkowe pasma właściwych mięśni grzbietu” (s. 676).
- **Mięśnie podpotyliczne:** m. skośny górny głowy „należy do pasma bocznego, natomiast trzy następne grzbietowe mięśnie podpotyliczne pochodzą z pasma przyśrodkowego” (s. 671); m. prosty boczny głowy „jest pochodnym błony mięśniowej brzusznej tułowia” (s. 673).
- **Co znaczy „pięć mięśni długich” (s. 669)?** Bochenek nigdzie tej piątki nie wylicza. Da się ją jednak wyprowadzić z jego własnego wyliczenia na s. 659: po odjęciu mięśni krótkich (mm. intertransversarii, rotatores, mm. interspinales) z listy układów zostają dokładnie: m. sacrospinalis, mm. splenii, mm. spinales, mm. semispinales, mm. multifidi. To zgadza się z pięcioma kolejnymi hasłami pod nagłówkiem „Długie mięśnie grzbietu”: mm. płatowate → m. krzyżowo-grzbietowy → m. kolcowy → m. półkolcowy → m. wielodzielny. Mm. skręcające są szóstym hasłem – krótkie, dołączone do tej grupy „ze względów klasyfikacyjnych”, bo są najgłębszą warstwą układu poprzeczno-kolcowego. Jest to wniosek z tekstu, nie cytat; drugie możliwe odczytanie (m. płatowaty, m. biodrowo-żebrowy, m. najdłuższy, m. kolcowy, „m. poprzeczno-kolcowy” jako całość) daje to samo drzewo, ale gorzej pasuje do zdania ze s. 669 i do streszczenia, gdzie m. krzyżowo-grzbietowy to „jeden mięsień” (s. 676).
- **Podział ze s. 669 (krótkie właściwe vs pochodzenia wentralnego)** jest podziałem wewnątrz grupy krótkich według pochodzenia i unerwienia; na plakacie go nie ma (G4).

---

## 3. Lista zmian do wprowadzenia

### 3.1 Grzbiet

**G1 – BŁĄD (hierarchia).** Pasma tylko pod mięśniami długimi.
- Na plakacie: `Głębokie → [Długie → (pasmo boczne | pasmo przyśrodkowe)] | Krótkie | Podpotyliczne` (`build.py` 348–369). Karty w „Krótkich” i „Podpotylicznych” nie mają żadnej informacji o paśmie.
- Powinno być: pasma dotyczą wszystkich trzech grup. Najmniejsza zmiana: zostawić trzy kolumny, a na kartach „Krótkich” i „Podpotylicznych” dodać znacznik pasma w tych samych kolorach co ramki pasm w „Długich” (teal = boczne, coral = przyśrodkowe), plus trzeci znacznik „pochodzenia wentralnego”. Przypisania – tabela w p. 1.1. Dodatkowo mała ramka „Podział wg s. 659” z tą tabelą.
- Bochenek: s. 659 „…mięśnie krótkie grzbietu […] i mięśnie podpotyliczne […], należące czy to do pasma przyśrodkowego, czy też do bocznego”; s. 669 „Mm. międzykolcowe […] należą do pasma przyśrodkowego właściwych mięśni grzbietu”; s. 671 (m. skośny górny głowy – pasmo boczne, trzy następne – pasmo przyśrodkowe).

**G2 – NIEJASNE.** Pytanie 4 i opisy pasm nie są sformułowaniem Bochenka.
- Na plakacie: pytanie „do których wyrostków biegną włókna?”; pasmo boczne – „włókna do wyr. poprzecznych i żeber”; pasmo przyśrodkowe – „włókna do wyr. kolczystych”.
- Ocena: to uproszczenie wyprowadzone z definicji układów – dla odcinków kręgosłupowych się zgadza, ale nie pasuje do części głowowych (m. płatowaty głowy i m. najdłuższy głowy kończą się na wyrostku sutkowatym, m. półkolcowy głowy na łusce kości potylicznej) i Bochenek tak pasm nie definiuje.
- Powinno być: pytanie „które pasmo? – jaki układ (skąd dokąd biegną pasma mięśniowe)?”. Opis pasma bocznego: „układ międzypoprzeczny (m. krzyżowo-grzbietowy; do niego należą też mm. międzypoprzeczne) + mm. płatowate – jedyne o przebiegu kolcowo-poprzecznym”. Opis pasma przyśrodkowego: „układ międzykolcowy (m. kolcowy; do niego należą też mm. międzykolcowe) + układ poprzeczno-kolcowy”.
- Bochenek: s. 659 (cytat w p. 2).

**G3 – BRAK.** Nazwy układów.
- Na plakacie: jest tylko grupa „Mięśnie poprzeczno-kolcowe”; nigdzie nie pada „układ międzykolcowy” ani „układ międzypoprzeczny”.
- Powinno być: w opisie grupy „Mięsień kolcowy”: „od wyrostków kolczystych do wyrostków kolczystych · część główna układu międzykolcowego”; w opisie grupy „Mięsień krzyżowo-grzbietowy”: „układ międzypoprzeczny – od wyrostków poprzecznych do poprzecznych lub ich odpowiedników (żeber)”; w opisie „Mięśnie poprzeczno-kolcowe”: „układ poprzeczno-kolcowy – od wyrostków poprzecznych do kolczystych”.
- Bochenek: s. 659; s. 663 („przebiega on między żebrami lub ich homologicznymi odpowiednikami”, „przebiega w zasadzie między wyrostkami poprzecznymi lub ich odpowiednikami”); s. 667 („stanowi część główną układu międzykolcowego”).

**G4 – BRAK.** Krótkie mięśnie grzbietu: podział na właściwe i pochodzenia wentralnego.
- Na plakacie: trzy karty obok siebie (mm. międzykolcowe, mm. międzypoprzeczne, mm. dźwigacze żeber), opis grupy „między dwoma sąsiednimi kręgami”. Cztery rodzaje mm. międzypoprzecznych są wymienione bez rozróżnienia. Tylko przy dźwigaczach żeber (★) jest zdanie, że nie należą do właściwych mięśni grzbietu.
- Powinno być: w nagłówku grupy dopisać „właściwe mięśnie grzbietu (gałęzie tylne) + mięśnie pochodzenia wentralnego (gałęzie przednie)”. Przy częściach mm. międzypoprzecznych: „tylne szyi” i „przyśrodkowe lędźwi” – „właściwe mm. grzbietu, pasmo boczne”; „przednie szyi” i „boczne lędźwi” – „pochodzenia wentralnego (odpowiadają mm. międzyżebrowym zewnętrznym)”. Przy „boczne lędźwi” dodać odsyłacz „→ także tylne mięśnie brzucha (s. 712)” – na stronie brzucha odsyłacz jest, w tę stronę go nie ma. Przy mm. międzykolcowych: „pasmo przyśrodkowe”.
- Bochenek: s. 669 „…zaliczamy nie tylko właściwe mięśnie grzbietu unerwione przez gałęzie tylne nerwów rdzeniowych (mm. międzykolcowe i międzypoprzeczne tylne oraz przyśrodkowe), ale również metameryczne mięśnie, które choć położone na grzbiecie, są pochodzenia wentralnego, unerwione przez gałęzie przednie nerwów rdzeniowych (mm. międzypoprzeczne przednie i boczne oraz dźwigacze żeber)”; s. 670 „Tylko mm. międzypoprzeczne tylne szyi i międzypoprzeczne przyśrodkowe lędźwi należą do właściwej mięśniówki grzbietu […]. Mięśnie międzypoprzeczne przednie szyi i boczne lędźwi są pochodzenia wentralnego”.

**G5 – BRAK.** Mięśnie podpotyliczne: pochodzenie i pasmo.
- Na plakacie: pięć kart z samymi nazwami; opis „potylica ↔ dwa górne kręgi · 5 mięśni”.
- Powinno być: znaczniki jak w drzewie 1.1 (skośny górny – pasmo boczne; prosty tylny mniejszy, prosty tylny większy, skośny dolny – pasmo przyśrodkowe; prosty boczny – pochodzenia wentralnego). W opisie grupy: „4 grzbietowe + m. prosty boczny głowy pochodzenia wentralnego”.
- Bochenek: s. 671 „…jako taki należy do pasma bocznego, natomiast trzy następne grzbietowe mięśnie podpotyliczne pochodzą z pasma przyśrodkowego”; s. 671–672 (prosty tylny mniejszy „jest najwyższym mięśniem międzykolcowym szyi”; większy „pochodzi z drugiego z kolei m. międzykolcowego szyi”; skośny dolny „pochodzi przypuszczalnie z m. międzykolcowego”); s. 673 (prosty boczny „odpowiada najwyższemu m. międzypoprzecznemu przedniemu szyi, tym samym jest pochodnym błony mięśniowej brzusznej tułowia”).

**G6 – BRAK.** Mm. skręcające i „pięć mięśni długich”.
- Na plakacie: notka „mm. skręcające są krótkie, ale Bochenek „ze względów klasyfikacyjnych” umieszcza je wśród mięśni długich (s. 669)”. Ostrzeżenie o s. 659 jest w `data.py` (pole `warn` przy mm. skręcających), ale karta „bare” go nie wyświetla. Cytat pomija słowa „w grupie pięciu mięśni długich”.
- Powinno być: notka z „!”: „S. 659: Bochenek wylicza mm. skręcające wśród mięśni krótkich (mm. intertransversarii, rotatores et mm. interspinales). S. 669: „są krótkie, ze względów klasyfikacyjnych umieściliśmy je jednak w grupie pięciu mięśni długich” – jako najgłębszą warstwę układu poprzeczno-kolcowego. Streszczenie (s. 676) też podaje je przed mięśniami krótkimi.” W nagłówku „Długie mięśnie grzbietu” dopisać: „5 mięśni długich: mm. płatowate, m. krzyżowo-grzbietowy, m. kolcowy, m. półkolcowy, m. wielodzielny + mm. skręcające” (z zaznaczeniem, że piątkę wyliczono z s. 659 – Bochenek jej nie wypisuje).
- Bochenek: s. 659, 669, 676.

**G7 – BRAK (poziom drzewa).** M. półkolcowy.
- Na plakacie: pod „Mięśnie poprzeczno-kolcowe” są cztery równorzędne karty: „m. półkolcowy klatki piersiowej i szyi”, „m. półkolcowy głowy”, „m. wielodzielny”, „mm. skręcające”. Nie ma karty „m. półkolcowy (m. semispinalis)”. Przy „3 warstwach” student widzi cztery mięśnie.
- Powinno być: jedna karta „m. półkolcowy (m. semispinalis) – warstwa powierzchowna” z częściami: m. półkolcowy klatki piersiowej i szyi; m. półkolcowy głowy (a w nim: część przyśrodkowa – m. dwubrzuścowy głowy, część boczna – m. spleciony większy). Tak samo, jak plakat robi to dla m. kolcowego, m. biodrowo-żebrowego i m. najdłuższego.
- Bochenek: s. 667 „Warstwę powierzchowną tworzy m. półkolcowy, warstwę środkową — wielodzielny i warstwę głęboką — mm. skręcające”; s. 667–668 „M. półkolcowy (m. semispinalis) […] ograniczając się do części piersiowej, szyjnej i głowowej”; s. 676 „12. M. półkolcowy (m. semispinalis) dzieli się na m. półkolcowy klatki piersiowej i szyi […] oraz m. półkolcowy głowy”.

**G8 – NIEJASNE.** Dwa znaczenia słowa „pasmo” przy m. krzyżowo-grzbietowym.
- Na plakacie: m. biodrowo-żebrowy – „pasmo boczne m. krzyżowo-grzbietowego”; m. najdłuższy – „pasmo przyśrodkowe m. krzyżowo-grzbietowego”; w karcie wspólnego początku: „dzieli się na m. biodrowo-żebrowy (pasmo boczne) i m. najdłuższy (pasmo przyśrodkowe)”. Obie karty leżą w ramce „pasmo boczne”, więc m. najdłuższy ma jednocześnie napis „pasmo przyśrodkowe”.
- Powinno być: m. biodrowo-żebrowy – „część boczna m. krzyżowo-grzbietowego” (dokładnie tak u Bochenka); m. najdłuższy – „pasmo przyśrodkowe m. krzyżowo-grzbietowego (nie mylić z pasmem przyśrodkowym mięśni grzbietu – cały m. krzyżowo-grzbietowy należy do pasma bocznego)”. W karcie wspólnego początku: „m. biodrowo-żebrowy (część boczna) i m. najdłuższy (pasmo przyśrodkowe tego mięśnia)”.
- Bochenek: s. 663 „M. biodrowo-żebrowy (m. iliocostalis) stanowi część boczną m. krzyżowo-grzbietowego”; „M. najdłuższy (m. longissimus) stanowi pasmo przyśrodkowe m. krzyżowo-grzbietowego”; s. 676 to samo.

**G9 – NIEJASNE.** Pytanie 3 „jak długie są włókna?”.
- Na plakacie: jedno pytanie prowadzi do trzech gałęzi: długie / krótkie / podpotyliczne. Trzecia gałąź nie jest odpowiedzią na pytanie o długość (mięśnie podpotyliczne też są „silne i krótkie”, s. 671).
- Powinno być: „ile kręgów mijają pasma mięśniowe?” → długie: „mijają coraz większą liczbę kręgów (warstwy bardziej powierzchowne)”; krótkie: „między dwoma sąsiednimi kręgami – zachowana budowa metameryczna (warstwy najgłębsze)”; podpotyliczne: „między kością potyliczną a dwoma górnymi kręgami – swoiste zróżnicowanie w związku z ruchami głowy”.
- Bochenek: s. 659 („…w warstwach natomiast bardziej powierzchownych pasma mięśniowe stają się stopniowo coraz dłuższe przeskakując coraz większą liczbę kręgów”); s. 669; s. 671.

**G10 – NIEJASNE.** „erector spinae” jako łacina grupy „Głębokie mięśnie grzbietu”.
- Na plakacie: pod nagłówkiem grupy sama łacina „erector spinae”; niżej ramka o niezgodności (dobrze).
- Powinno być: „prostownik grzbietu (erector spinae)” z polską nazwą, bo to nie jest łaciński odpowiednik „głębokich mięśni grzbietu”, tylko druga nazwa. Ramkę o niezgodności zostawić; można dopisać s. 673 („mięśnie głębokie grzbietu (erector spinae)”) i przypis ze s. 659: erector trunci.
- Bochenek: s. 659 „Cała ta mięśniówka nosi również nazwę prostownika grzbietu (erector spinae)”; s. 663 i 676 – nazwa dla m. krzyżowo-grzbietowego.

**G11 – BŁĄD.** Odmiana wpisana jako część m. równoległobocznego.
- Na plakacie: w wierszu CZĘŚCI trzecia pozycja: „rzadka odmiana – m. potyliczno-łopatkowy […] (m. occipitoscapularis)” (`data.py` 82).
- Powinno być: usunąć z CZĘŚCI (mięsień ma dwie części). To pozycja z akapitu „Odmiany”, a odmiany miały być z plakatu usunięte.
- Bochenek: s. 656 „…dzielące mięsień na dwie nierówne części: górną — m. równoległoboczny mniejszy […] i dolną — m. równoległoboczny większy”; s. 657, w „Odmianach”: „Rzadką odmianę stanowi tzw. m. potyliczno-łopatkowy”.

**G12 – BRAK.** Części m. najszerszego grzbietu.
- Na plakacie: karta nie ma wiersza CZĘŚCI; cztery części są tylko w drobnym druku poziomu 3 („PRZYCZEPY – UZUPEŁNIENIE”).
- Powinno być: wiersz CZĘŚCI na karcie: pars vertebralis, pars iliaca, pars costalis, pars scapularis – z dopiskiem, że Bochenek podaje je tylko po łacinie; najlepiej przypisać je do czterech punktów przyczepu początkowego.
- Bochenek: s. 652 (pars vertebralis m. latissimi dorsi*, pars iliaca*, pars costalis*, pars scapularis*).

**G13 – BŁĄD (drobny) + BRAK.** Opisy podgrup mięśni powierzchownych.
- Na plakacie: kolcowo-ramienne – „do łopatki i k. ramiennej”; kolcowo-żebrowe – „do żeber · mm. zębate tylne”; warstwy są tylko jako znaczniki na kartach (I, II, III). M. czworoboczny kończy się także na obojczyku, więc „do łopatki i k. ramiennej” jest nieścisłe.
- Powinno być: nagłówek „Powierzchowne”: dopisać „2 podgrupy, razem 3 warstwy”. Kolcowo-ramienne: „zdążają do kończyny górnej (obręcz kończyny górnej i k. ramienna) · 2 warstwy: I – m. czworoboczny, m. najszerszy grzbietu; II – m. równoległoboczny, dźwigacz łopatki”. Kolcowo-żebrowe: „do żeber · mm. zębate tylne · trzecia warstwa mięśni powierzchownych”.
- Bochenek: s. 650 (cały akapit o dwóch podgrupach); s. 650 „biegnących przeważnie, choć nie wyłącznie, do obręczy kończyny górnej i kości ramiennej”; s. 657 „M. równoległoboczny wraz z następnym — dźwigaczem łopatki stanowią drugą, głębszą warstwę”.

**G14 – NIEJASNE.** Pytanie 1 i nazwy gałęzi nerwów.
- Na plakacie: pytanie „skąd pochodzą – jaki mają nerw?”; powierzchowne – „gałęzie przednie nn. rdzeniowych”.
- Powinno być: pytanie zgodne z nazwami grup i z Bochenkiem: „jak głęboko leżą? (różnią się też budową i pochodzeniem)”. W opisie powierzchownych użyć słów ze s. 650: „mięśnie szerokie · gałęzie brzuszne nn. rdzeniowych”; w opisie głębokich: „mięśnie wysmukłe, podłużne · gałęzie grzbietowe (tylne) nn. rdzeniowych”. Bochenek używa zamiennie „brzuszne/przednie” i „grzbietowe/tylne”, ale na s. 649–650 i w streszczeniu (s. 675) są „brzuszne” i „grzbietowe”.
- Bochenek: s. 649–650, 658, 675.

**G15 – NIEJASNE.** Mm. krzyżowo-guziczne pokazane jako „części”.
- Na plakacie: m. krzyżowo-guziczny tylny jest czwartą „częścią” mm. międzykolcowych, a m. krzyżowo-guziczny przedni – piątą „częścią” mm. międzypoprzecznych.
- Powinno być: osobne małe pozycje bezpośrednio pod kartą macierzystą (nie w wyliczeniu odcinków): „m. krzyżowo-guziczny tylny – pozostałość mm. międzykolcowych między kością krzyżową a guziczną”; „m. krzyżowo-guziczny przedni – ta sama grupa co mm. międzypoprzeczne boczne (pochodzenia wentralnego); niestały”.
- Bochenek: s. 670 – oba mają własne hasła; streszczenie (s. 676–677) wspomina je przy pozycjach 15 i 16.

**G16 – NIEJASNE.** Polskie nazwy odcinków, których u Bochenka nie ma.
- Na plakacie: „mm. skręcające klatki piersiowej / szyi / lędźwi”, „mm. międzykolcowe szyi / lędźwi / klatki piersiowej”, „mm. dźwigacze żeber krótkie / długie”; łacina „mm. rotatores longi / breves”.
- U Bochenka: te odcinki mają tylko nazwy łacińskie w nawiasach – „(mm. rotatores thoracis)”, „(mm. rotatores cervicis)”, „(mm. rotatores lumborum)” (s. 669); „(mm. interspinales cervicis)”, „(mm. interspinales lumborum)”, „(mm. interspinales thoracis)” (s. 670); „(mm. levatores costarum breves)”, „(mm. levatores costarum longi)” (s. 671). Długie i krótkie skręcające: „(rotatores longi*)”, „(rotatores breves*)” – bez „mm.”; polskie „mm. skręcające krótkie” pada w tekście (s. 669), „długie” w streszczeniu (s. 676).
- Powinno być: albo zostawić samą łacinę z opisem („w odcinku szyjnym”, „do następnego żebra”), albo oznaczyć polskie nazwy jako utworzone przez analogię (znak jak „°”). Łacinę „rotatores longi / breves” podać bez „mm.”.

**G17 – NIEJASNE.** Opisy grup w paśmie bocznym i przyśrodkowym.
- „Mięsień krzyżowo-grzbietowy – wspólny pień – wyżej dwa mięśnie” oraz karta „m. krzyżowo-grzbietowy – wspólny początek”: Bochenek mówi „wspólna masa” („wspólną masę m. krzyżowo-grzbietowego”, s. 659; „wspólnej masy mięśniowej”, s. 663) i „daje się ku górze rozdzielić na dwa pasma” (s. 663). Zamienić „pień” na „wspólna masa mięśniowa”.
- „Mięsień kolcowy – po wyrostkach kolczystych”: zamienić na sformułowanie z G3.
- „Mięśnie poprzeczno-kolcowe – 3 warstwy – coraz krótsze w głąb”: lepiej „3 warstwy wg długości i kierunku włókien: m. półkolcowy mija więcej niż 4 kręgi, m. wielodzielny 2–4, mm. skręcające 1 lub 0” (s. 667–669).
- „Długie mięśnie grzbietu – włókna biegną przez wiele kręgów”: lepiej „pasma mięśniowe mijają coraz większą liczbę kręgów” (s. 659).

**G18 – NIEJASNE.** Kolejność nazw części m. czworobocznego.
- Na plakacie: „część zstępująca (górna)”, „część poprzeczna (środkowa)”, „część wstępująca (dolna)”.
- U Bochenka nazwą podstawową jest górna / środkowa / dolna: „Część górna (pars descendens)”, „Część środkowa (pars transversa)”, „Część dolna (pars ascendens)” (s. 651) i tak samo w streszczeniu (s. 675); „zstępująca / poprzeczna / wstępująca” pojawia się w topografii. Propozycja: „część górna – zstępująca (pars descendens)” itd.

**G19 – NIEJASNE.** Łacina „Mięśni kolcowo-poprzecznych”.
- Na plakacie: „m. spinotransversalis” – zgodnie ze s. 659. Streszczenie (s. 675) ma „(m. spinotransversarii)” i „m. splenius colli” zamiast „m. splenius cervicis” (s. 660). Warto dodać „!” z tą różnicą, bo student uczy się też ze streszczenia.

**G20 – BŁĄD (nazwa).** Tytuł ramki „Powięzi grzbietu”.
- Powinno być: „Powięzie grzbietu” – tak brzmi nagłówek u Bochenka (s. 673, 677), i tak plakat pisze na pozostałych stronach („Powięzie klatki piersiowej”, „Powięzie mięśni brzucha”). Źródło: `l3_grzbiet.json`, tytuł panelu.

### 3.2 Klatka piersiowa

**K1 – BRAK (poziom drzewa).** Mm. międzyżebrowe.
- Na plakacie: pod „Głębokie albo właściwe…” cztery równorzędne karty: mm. międzyżebrowe zewnętrzne, mm. międzyżebrowe wewnętrzne, mm. podżebrowe, m. poprzeczny klatki piersiowej.
- Powinno być: trzy składniki, a zewnętrzne i wewnętrzne jako dwie warstwy jednej pozycji „mm. międzyżebrowe (mm. intercostales)” – jak w drzewie 1.2. W opisie grupy dopisać: „skład: mm. międzyżebrowe, mm. podżebrowe, m. poprzeczny klatki piersiowej”.
- Bochenek: s. 685 „Mięśniówka ta składa się z mm. międzyżebrowych, mm. podżebrowych i m. poprzecznego klatki piersiowej”; „Mm. międzyżebrowe (mm. intercostales) […] występują w dwóch zasadniczych warstwach”; streszczenie s. 700: „5. Mm. międzyżebrowe”, „6. M. poprzeczny klatki piersiowej”.

**K2 – NIEJASNE.** Pytanie 1 „z czym się łączą?”.
- Na plakacie: jedno pytanie do trzech gałęzi; pasuje tylko do mięśni powierzchownych.
- Powinno być: „trzy odrębne zespoły – który?” z opisami: 1) powierzchowne – „przyczepiają się do kośćca okolicy barku i ramienia”; 2) głębokie – „właściwe mięśnie ściany klatki piersiowej”; 3) przepona – „przegroda między jamą klatki piersiowej a jamą brzuszną”. Opisy gałęzi na plakacie są już poprawne; brakuje słów „trzy odrębne zespoły” i lepszego pytania. W opisie rozdziału można dodać: „pochodne mięśniówki brzusznej tułowia · gałęzie przednie nn. rdzeniowych”.
- Bochenek: s. 677.

**K3 – NIEJASNE.** Dwa równoległe podziały mięśni głębokich.
- Na plakacie: w drobnym druku grupy jest zdanie o trzech warstwach (zewnętrzne, wewnętrzne, poprzeczny) – poprawne (s. 677–678). Nie widać, że to inny podział niż skład ze s. 685 i że mm. podżebrowe nie mają w nim miejsca.
- Powinno być: dopisać jedno zdanie: „W podziale na 3 warstwy (s. 677–678, 703) Bochenek nie wymienia mm. podżebrowych; streszczenie (s. 700) też je pomija”.

**K4 – BRAK (drobny).** Części przepony na krótkiej karcie.
- Na plakacie: „część lędźwiowa – odnoga prawa i lewa […] oraz więzadła łukowate”.
- Powinno być: nazwać trzy więzadła: pośrodkowe (lig. arcuatum medianum), przyśrodkowe (lig. arcuatum mediale), boczne (lig. arcuatum laterale). Jeśli pełna lista jest na stronie „Klatka i oddychanie”, wystarczy tu same nazwy.
- Bochenek: s. 691 „Rozpoczyna się ona po stronie prawej i lewej trzema ścięgnistymi więzadłami łukowatymi, pośrodkowym, przyśrodkowym i bocznym oraz odnogą przepony”.

**K5 – NIEJASNE.** Opis części „mm. międzyżebrowe pośrednie – warstwa zewnętrzna; od bruzdy żebra do mostka”.
- Miesza dwie różne informacje (miejsce początku na żebrze i zasięg ku przodowi). Powinno być: „warstwa zewnętrzna; zaczynają się na zewnątrz od bruzdy żebra; sięgają aż do mostka”.
- Bochenek: s. 686.

**K6 – BRAK (drobny, do rozważenia).** Powiązanie z grzbietem.
- Bochenek, s. 677: „Część obu pierwszych grup w rozwoju osobniczym przewędrowuje grzbietowo, zachowując swoje unerwienie i przykrywa właściwą mięśniówkę grzbietu. Z mięśniami tymi zapoznaliśmy się poprzednio.” Jedno zdanie przy nagłówku rozdziału wyjaśniłoby, skąd na grzbiecie mięśnie powierzchowne.

### 3.3 Brzuch

Grupy, przynależność mięśni i kolejność są zgodne z Bochenkiem (nagłówki s. 704 i 712, streszczenie s. 730–731). Uwagi:

**B1 – NIEJASNE.** Dźwigacz jądra jako czwarta karta pod „boczne – 3 warstwy”.
- Na plakacie: cztery równorzędne karty; trzy mają znacznik warstwy, dźwigacz jądra nie.
- Powinno być: karta wyraźnie podrzędna (mniejsza, wcięta, podpięta pod m. skośny wewnętrzny i m. poprzeczny) z napisem „nie jest czwartą warstwą – utworzony z włókien dwóch poprzednich mięśni”.
- Bochenek: s. 707 „ze wszystkich trzech bocznych mięśni brzucha jest on najmniejszy”; s. 710 (dźwigacz jądra opisany drobnym drukiem, „składa się z włókien, które wychodzą z dolnego brzegu m. skośnego wewnętrznego brzucha i m. poprzecznego brzucha”); streszczenie s. 731 – bez numeru, „utworzony z włókien dwóch poprzednich mięśni”.

**B2 – NIEJASNE.** Nazwy podgrup „boczne” i „przednie”.
- Powinno być pełnymi nazwami: „Boczne mięśnie brzucha” (z dopiskiem: „u Bochenka także: mięśnie szerokie brzucha, mm. płaskie”) i „Przednie mięśnie brzucha – układ mięśni prostych”. W opisie „przednich” dodać kryterium: „jedyne miejsce bez podziału na warstwy”. Strony przy „boczne”: 702–703, 707.
- Bochenek: s. 702 („w trzy warstwy”), 704 („przednie mięśnie brzucha — układ mięśni prostych”), 707, 716–717 („mięśni szerokich brzucha”), 731–732 („mm. płaskich”, „Mięśnie płaskie brzucha”).

**B3 – NIEJASNE.** M. prosty brzucha – wiersz „CZĘŚCI: smugi ścięgniste – najczęściej 3–4”.
- Smugi nie są częściami mięśnia; dzielą go „na poszczególne odcinki”. Powinno być: etykieta „BUDOWA” albo „smugi ścięgniste (najczęściej 3 lub 4) dzielą mięsień na odcinki”.
- Bochenek: s. 710.

**B4 – zgodne.** Tylne mięśnie brzucha: „grupa mm. międzypoprzecznych bocznych lędźwi (s. 670) oraz m. czworoboczny lędźwi” (s. 712) – na plakacie tak samo, z odsyłaczem. Dwie warstwy m. czworobocznego lędźwi (przednia, tylna) – zgodne.

---

## 4. Sprawdzone i zgodne z Bochenkiem

- Nazwy wszystkich nagłówków grup: Powierzchowne / Głębokie mięśnie grzbietu, Mięśnie kolcowo-ramienne, Mięśnie kolcowo-żebrowe, Długie mięśnie grzbietu, Mięśnie kolcowo-poprzeczne, Mięsień krzyżowo-grzbietowy, Mięsień kolcowy, Mięśnie poprzeczno-kolcowe, Krótkie mięśnie grzbietu, Mięśnie podpotyliczne; Powierzchowne mięśnie klatki piersiowej, Głębokie albo właściwe mięśnie klatki piersiowej, Przepona; Boczne i przednie mięśnie brzucha, Tylne mięśnie brzucha.
- Przynależność każdego mięśnia do grupy i kolejność mięśni w grupach – jak w tekście i streszczeniach (w tym kolejność pięciu mięśni podpotylicznych i kolejność części m. biodrowo-żebrowego, m. najdłuższego, m. kolcowego).
- Przypisanie mięśni długich do pasm: boczne – mm. płatowate i m. krzyżowo-grzbietowy; przyśrodkowe – m. kolcowy i mm. poprzeczno-kolcowe.
- Znaczniki warstw mięśni powierzchownych grzbietu (I: czworoboczny, najszerszy; II: równoległoboczny, dźwigacz łopatki; III: zębate tylne) i trzech warstw układu poprzeczno-kolcowego.
- Polskie i łacińskie nazwy mięśni oraz części: m. czworoboczny, m. równoległoboczny (mniejszy, większy), m. piersiowy większy (3 części), m. zębaty przedni (3 części bez łaciny), mm. międzyżebrowe pośrednie i najgłębsze, przepona (3 części, kolejność lędźwiowa → żebrowa → mostkowa), m. półkolcowy głowy (m. dwubrzuścowy głowy, m. spleciony większy), cztery rodzaje mm. międzypoprzecznych, oba mm. krzyżowo-guziczne.
- Trzy zespoły klatki piersiowej są trzema równorzędnymi gałęziami (łączniki rysowane do każdej z trzech grup).
- Notki „!” o niezgodnościach Bochenka dotyczące zakresu nazwy „prostownik grzbietu” – poprawne.

---

## 5. Zauważone przy okazji (poza klasyfikacją)

- `plakat_m3.txt`, karta ★ m. czworobocznego lędźwi: urwany fragment zdania po usunięciu unerwienia – „…można go porównać do mm. pochyłych szyi (s. 715). podżebrowy i gałązki splotu lędźwiowego (s. 712, 715).” Drugie zdanie trzeba usunąć.
- M. piramidowy: w „Odmianach” Bochenek raz nazywa go „m. stożkowaty” (s. 712) – nie przenosić tej nazwy.
