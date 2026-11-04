# -*- coding: utf-8 -*-
# Dane: Bochenek, Anatomia człowieka t. I (skan użytkownika), s. 649–755.
# [[...]] = łacińska nazwa miejsca przyczepu (mała czcionka, w nawiasie)
# ° po łacinie = brak tej łaciny w tomie I Bochenka

def M(pl, lat, pg, **kw):
    d = dict(kind='m', pl=pl, lat=lat, pg=pg)
    d.update(kw)
    return d

def S(pl, lat, **kw):
    d = dict(kind='s', pl=pl, lat=lat)
    d.update(kw)
    return d

def G(title, lat, pg, items, **kw):
    d = dict(kind='g', title=title, lat=lat, pg=pg, items=items)
    d.update(kw)
    return d

def REF(pl, lat, pg, txt):
    return dict(kind='ref', pl=pl, lat=lat, pg=pg, txt=txt)

# =====================================================================
# I. MIĘŚNIE GRZBIETU
# =====================================================================
GRZBIET = G('Mięśnie grzbietu', 'musculi dorsi°', '649–677', [

  G('Powierzchowne mięśnie grzbietu', '', '650–658', [

    G('Mięśnie kolcowo-ramienne', 'mm. spinohumerales', '650–658', [

      M('m. czworoboczny', 'm. trapezius', '650–651',
        layer='warstwa I',
        parts=[
          'część zstępująca (górna) [[pars descendens]]',
          'część poprzeczna (środkowa) [[pars transversa]]',
          'część wstępująca (dolna) [[pars ascendens]]',
        ],
        o=[
          'przyśrodkowa część kresy karkowej górnej [[linea nuchae superior]] i guzowatość potyliczna zewnętrzna [[protuberantia occipitalis externa]] kości potylicznej',
          'więzadło karkowe [[ligamentum nuchae]]',
          'wyrostki kolczyste C7 i wszystkich kręgów piersiowych (Th1–Th12) [[processus spinosus]]',
          'odpowiednie odcinki więzadła nadkolcowego [[ligamentum supraspinale]]',
        ],
        i=[
          'koniec barkowy obojczyka [[clavicula – extremitas acromialis]] – część zstępująca',
          'wyrostek barkowy [[acromion]] – część poprzeczna',
          'grzebień łopatki [[spina scapulae]] – część poprzeczna; część wstępująca kończy się na przyśrodkowej części górnego brzegu grzebienia',
        ],
        f=[
          '<b>część zstępująca:</b> dźwiga staw ramienny ku górze („wzruszanie ramionami”) i dźwiga ciężary na stawie ramiennym; przy ustalonym stawie ramiennym zgina głowę ku tyłowi',
          '<b>część poprzeczna:</b> zbliża łopatkę do kręgosłupa',
          '<b>część wstępująca:</b> opuszcza staw ramienny; przy ustalonej obręczy kończyny górnej unosi tułów ku górze',
          '<b>część zstępująca + wstępująca:</b> obracają łopatkę – kąt górny zbliża się do kręgosłupa, kąt dolny idzie do przodu i bocznie, panewka kieruje się ku górze; dzięki temu ramię może być uniesione ponad poziom',
          '<b>cały mięsień:</b> cofa staw ramienny, zbliża łopatkę do kręgosłupa i przyciska ją do klatki piersiowej',
        ]),

      M('m. najszerszy grzbietu', 'm. latissimus dorsi', '652–655',
        layer='warstwa I',
        o=[
          'wyrostki kolczyste Th7–Th12 i L1–L5 oraz grzebień krzyżowy pośrodkowy [[crista sacralis mediana]] – szerokim ścięgnem, które tworzy blaszkę powierzchowną powięzi piersiowo-lędźwiowej [[fascia thoracolumbalis]]',
          'tylna ⅓ wargi zewnętrznej grzebienia biodrowego [[crista iliaca – labium externum]]',
          'powierzchnia zewnętrzna żeber IX lub X, XI i XII – 3–4 pasma [[costa]]',
          'kąt dolny łopatki – często, niewielka część mięśnia [[angulus inferior scapulae]]',
        ],
        i=[
          'grzebień guzka mniejszego kości ramiennej [[crista tuberculi minoris]] – do przodu od m. obłego większego',
        ],
        f=[
          'przy ustalonym kręgosłupie opuszcza podniesione ramię, przywodzi je do tyłu i obraca do wewnątrz (ręka zbliża się do pośladków)',
          'razem z m. piersiowym większym opuszcza wysoko podniesione ramię, np. przy podciąganiu się na drążku',
          'przy ustalonych ramionach mięśnie obu stron dźwigają dolne żebra – pomocnicze mięśnie wdechowe',
          'przy ustalonym stawie ramiennym naciska bocznie na żebra – jego brzeg boczny twardnieje podczas kaszlu, czyli wydechu – „mięsień kaszlu”',
        ]),

      M('m. równoległoboczny', 'm. rhomboideus', '655–657',
        layer='warstwa II',
        parts=[
          'część górna, szyjna – m. równoległoboczny mniejszy [[m. rhomboideus minor]]',
          'część dolna, grzbietowa – m. równoległoboczny większy [[m. rhomboideus major]]',
        ],
        o=[
          'dolny odcinek więzadła karkowego [[ligamentum nuchae]]',
          'wyrostki kolczyste C6–C7 [[processus spinosus]]',
          'więzadło nadkolcowe [[ligamentum supraspinale]]',
          'wyrostki kolczyste Th1–Th4',
        ],
        i=[
          'brzeg przyśrodkowy łopatki – od grzebienia (trójkąta grzebienia) do kąta dolnego [[margo medialis scapulae]]',
        ],
        f=[
          'pociąga łopatkę przyśrodkowo i ku górze; zwłaszcza kąt dolny przesuwa przyśrodkowo i ku górze',
          'przyciska łopatkę, zwłaszcza jej brzeg przyśrodkowy, do klatki piersiowej',
          'kieruje panewkę stawową ku dołowi (s. 675)',
        ],
        warn=['W streszczeniu (s. 675) Bochenek podaje początek na wyrostkach kolczystych C7–Th4. Notatka podaje opis ze s. 655 (dwa ostatnie kręgi szyjne + Th1–Th4).']),

      M('dźwigacz łopatki', 'm. levator scapulae', '657',
        layer='warstwa II',
        o=[
          'guzki tylne wyrostków poprzecznych C1–C4 – 4 wiązki [[processus transversus – tuberculum posterius]]',
        ],
        i=[
          'górny odcinek brzegu przyśrodkowego łopatki – od kąta górnego do trójkąta grzebienia [[angulus superior; margo medialis; trigonum spinae]]',
        ],
        f=[
          'razem z częścią zstępującą m. czworobocznego pociąga łopatkę ku górze i przyśrodkowo',
          'obraca łopatkę: kąt dolny przyśrodkowo, wyrostek barkowy bocznie',
          'przy ustalonej obręczy kończyny górnej: jednostronnie zgina kręgosłup w odcinku szyjnym ku bokowi, obustronnie – ku tyłowi',
        ]),
    ]),

    G('Mięśnie kolcowo-żebrowe', 'mm. spinocostales', '658', [
      M('m. zębaty tylny górny', 'm. serratus posterior superior', '658',
        layer='warstwa III',
        o=[
          'dolna część więzadła karkowego [[ligamentum nuchae]]',
          'wyrostki kolczyste C6–C7 i Th1–Th2 [[processus spinosus]]',
        ],
        i=[
          'brzeg górny i powierzchnia zewnętrzna żeber II–V – 4 pasma [[costa]]',
        ],
        f=['dźwiga żebra – mięsień wdechowy'],
        warn=['W streszczeniu (s. 675) jest „do zewnętrznej powierzchni II i V żebra”. Notatka podaje opis ze s. 658 (żebra II–V, 4 pasma).']),

      M('m. zębaty tylny dolny', 'm. serratus posterior inferior', '658',
        layer='warstwa III',
        o=[
          'blaszka tylna powięzi piersiowo-lędźwiowej na wysokości Th10–L2 [[fascia thoracolumbalis]]',
        ],
        i=[
          'brzeg dolny żeber IX–XII – 4 pasma [[costa]]',
        ],
        f=['opuszcza żebra i kieruje je ku bokom; kurczy się podczas wydechu'],
        warn=['W streszczeniu (s. 675) Bochenek pisze: „dolny opuszcza je (również m. wdechowy)”. Notatka podaje opis ze s. 658.']),
    ]),
  ]),

  G('Głębokie mięśnie grzbietu', 'erector spinae', '658–673',
    intro='Właściwe mięśnie grzbietu. Bochenek: cała ta mięśniówka nosi też nazwę prostownika grzbietu (s. 659).',
    items=[

    G('Długie mięśnie grzbietu', '', '659–669', [

      G('Mięśnie kolcowo-poprzeczne', 'm. spinotransversalis', '659–660', [
        M('m. płatowaty głowy', 'm. splenius capitis', '659–660',
          o=[
            'więzadło karkowe na wysokości C3–C7 [[ligamentum nuchae]]',
            'wyrostki kolczyste Th1–Th2 [[processus spinosus]]',
            'więzadło nadkolcowe Th1–Th2 [[ligamentum supraspinale]]',
          ],
          i=[
            'wyrostek sutkowaty kości skroniowej [[processus mastoideus]]',
            'tuż poniżej bocznej ⅓ kresy karkowej górnej kości potylicznej [[linea nuchae superior]]',
          ],
          f=[
            'obustronnie: zgina głowę ku tyłowi (razem z m. czworobocznym i m. półkolcowym głowy)',
            'jednostronnie: obraca twarz w tę samą stronę i nieco ku górze',
          ]),
        M('m. płatowaty szyi', 'm. splenius cervicis', '660',
          o=[
            'wyrostki kolczyste i więzadło nadkolcowe Th3–Th5 [[processus spinosus; ligamentum supraspinale]]',
          ],
          i=[
            'guzki tylne wyrostków poprzecznych 2–3 górnych kręgów szyjnych – 2–3 wiązki [[processus transversus – tuberculum posterius]]',
          ],
          f=[
            'zgina szyję do tyłu',
            'obraca górną część szyi w tę samą stronę (tak jak m. płatowaty głowy obraca głowę)',
          ]),
      ]),

      G('Mięsień krzyżowo-grzbietowy', 'm. sacrospinalis', '660–665',
        intro='Bochenek: m. biodrowo-żebrowy i m. najdłuższy tworzą razem prostownik grzbietu [[erector spinae]] (s. 676).',
        items=[
        M('m. krzyżowo-grzbietowy – wspólny początek', 'm. sacrospinalis', '663, 665',
          o=[
            'grzebień biodrowy [[crista iliaca]]',
            'więzadła krzyżowo-biodrowe tylne [[ligamenta sacroiliaca dorsalia]]',
            'powierzchnia grzbietowa kości krzyżowej [[os sacrum – facies dorsalis]]',
            'wyrostki kolczyste kręgów lędźwiowych i 2–3 dolnych kręgów piersiowych [[processus spinosus]]',
          ],
          i=['wyżej dzieli się na m. biodrowo-żebrowy (pasmo boczne) i m. najdłuższy (pasmo przyśrodkowe) – ich przyczepy końcowe niżej'],
          f=[
            'utrzymuje równowagę tułowia; napina się przy każdym kroku',
            'bierze udział w oddychaniu – przy głębokim wdechu prostuje kręgosłup',
          ]),

        M('m. biodrowo-żebrowy', 'm. iliocostalis', '663, 665',
          note='pasmo boczne m. krzyżowo-grzbietowego',
          sub=[
            S('m. biodrowo-żebrowy lędźwi', 'm. iliocostalis lumborum',
              o=['wspólna masa m. krzyżowo-grzbietowego'],
              i=['kąty 6–9 dolnych żeber [[angulus costae]]']),
            S('m. biodrowo-żebrowy klatki piersiowej', 'm. iliocostalis thoracis',
              o=['kąty żeber VII–XII – przyśrodkowo od przyczepów części lędźwiowej [[angulus costae]]'],
              i=['kąty 6 lub 5 górnych żeber']),
            S('m. biodrowo-żebrowy szyi', 'm. iliocostalis cervicis',
              o=['kąty żeber III–VI, często II–VII – 4–6 wiązek'],
              i=['guzki tylne wyrostków poprzecznych C4–C6 (także C3) [[processus transversus – tuberculum posterius]]']),
          ],
          f=[
            'dzięki przyczepom do żeber silnie zgina kręgosłup w kierunku bocznym',
            'obustronnie, razem z m. najdłuższym: prostuje tułów (zgina go do tyłu)',
          ]),

        M('m. najdłuższy', 'm. longissimus', '663, 665',
          note='pasmo przyśrodkowe m. krzyżowo-grzbietowego',
          sub=[
            S('m. najdłuższy klatki piersiowej', 'm. longissimus thoracis',
              o=['wspólna masa i powierzchowna masa ścięgnista m. krzyżowo-grzbietowego',
                 'wyrostki poprzeczne 6–7 dolnych kręgów piersiowych [[processus transversus]]'],
              i=['wiązki boczne: wyrostki poprzeczne kręgów lędźwiowych',
                 'wiązki boczne: kąty żeber II–XII [[angulus costae]]',
                 'wiązki przyśrodkowe: wyrostki dodatkowe kręgów lędźwiowych [[processus accessorius]]',
                 'wiązki przyśrodkowe: wyrostki poprzeczne wszystkich kręgów piersiowych']),
            S('m. najdłuższy szyi', 'm. longissimus cervicis',
              o=['wyrostki poprzeczne 4–6 górnych kręgów piersiowych'],
              i=['guzki tylne wyrostków poprzecznych C2–C5 [[processus transversus – tuberculum posterius]]']),
            S('m. najdłuższy głowy', 'm. longissimus capitis',
              o=['wyrostki poprzeczne Th1–Th3 i C3–C7 [[processus transversus]]'],
              i=['wyrostek sutkowaty kości skroniowej [[processus mastoideus]]']),
          ],
          f=[
            'obustronnie, razem z m. biodrowo-żebrowym: prostuje tułów (zgina go do tyłu)',
            '<b>m. najdłuższy głowy:</b> pociąga głowę ku tyłowi, zgina ją i pochyla w tę samą stronę',
          ]),
      ]),

      G('Mięsień kolcowy', 'm. spinalis', '665–667', [
        M('m. kolcowy', 'm. spinalis', '667',
          note='pasmo przyśrodkowe; leży tuż przy wyrostkach kolczystych',
          sub=[
            S('m. kolcowy klatki piersiowej', 'm. spinalis thoracis',
              o=['wyrostki kolczyste L1–L3 i Th10–Th12 [[processus spinosus]]'],
              i=['wyrostki kolczyste Th2–Th8 (Th9 przeważnie ominięty)']),
            S('m. kolcowy szyi', 'm. spinalis cervicis',
              o=['wyrostki kolczyste Th1–Th2 i C6–C7'],
              i=['wyrostki kolczyste C2–C4 (C5 zwykle bez przyczepu)']),
            S('m. kolcowy głowy', 'm. spinalis capitis', tag='odmiana',
              o=['wyrostki kolczyste górnych kręgów piersiowych i dolnych szyjnych'],
              i=['kość potyliczna w pobliżu guzowatości potylicznej zewnętrznej [[protuberantia occipitalis externa]]']),
          ],
          f=[
            'jednostronnie: zgina kręgosłup w kierunku bocznym',
            'obustronnie: wzmaga zgięcie kręgosłupa ku tyłowi',
          ]),
      ]),

      G('Mięśnie poprzeczno-kolcowe', 'mm. transversospinales', '667–669',
        intro='Trzy warstwy: powierzchowna – m. półkolcowy, środkowa – m. wielodzielny, głęboka – mm. skręcające (s. 667).',
        items=[
        M('m. półkolcowy klatki piersiowej i szyi', 'm. semispinalis thoracis et cervicis', '668',
          layer='warstwa powierzchowna',
          o=['wyrostki poprzeczne wszystkich kręgów piersiowych [[processus transversus]]'],
          i=['wyrostki kolczyste 5–6 górnych kręgów piersiowych i C2–C7; kręg szczytowy nie ma przyczepu [[processus spinosus]]'],
          f=[
            'jednostronnie: zgina kręgosłup w odcinku piersiowym i szyjnym w bok i obraca go w stronę przeciwną',
            'obustronnie: prostuje kręgosłup w odcinku szyjnym i ustala go',
          ],
          warn=['W streszczeniu (s. 676) Bochenek podaje koniec na wyrostkach kolczystych C2–Th1. Notatka podaje opis ze s. 668.']),
        M('m. półkolcowy głowy', 'm. semispinalis capitis', '668',
          layer='warstwa powierzchowna',
          parts=[
            'część przyśrodkowa – m. dwubrzuścowy głowy [[m. biventer capitis]]',
            'część boczna – m. spleciony większy [[m. complexus major]]',
          ],
          o=[
            'wyrostki poprzeczne Th1–Th6 [[processus transversus]]',
            'wyrostki poprzeczne i stawowe C4–C7 [[processus transversus; processus articularis]]',
          ],
          i=['łuska kości potylicznej między kresą karkową górną i dolną [[squama occipitalis; linea nuchae superior; linea nuchae inferior]]'],
          f=[
            'jednostronnie: zgina głowę ku bokowi i obraca ją twarzą w stronę przeciwną',
            'obustronnie: zgina głowę ku tyłowi, zwiększając lordozę szyjną',
          ]),
        M('m. wielodzielny', 'm. multifidus', '668–669',
          layer='warstwa środkowa',
          omax='Bochenek podaje 7 przyczepów początkowych – tu wybrane 4',
          o=[
            'powierzchnia grzbietowa kości krzyżowej [[os sacrum – facies dorsalis]]',
            'wyrostki suteczkowate kręgów lędźwiowych [[processus mamillaris]]',
            'wyrostki poprzeczne wszystkich kręgów piersiowych [[processus transversus]]',
            'wyrostki stawowe dolne C5–C7 [[processus articularis inferior]]',
          ],
          i=['wyrostki kolczyste kręgów lędźwiowych, piersiowych i C2–C7 [[processus spinosus]]'],
          f=[
            'obustronnie: prostuje kręgosłup i ustala go',
            'jednostronnie: zgina kręgosłup ku bokowi i obraca go w stronę przeciwną',
          ],
          warn=['W streszczeniu (s. 676) Bochenek zamiast wyrostków suteczkowatych podaje wyrostki poprzeczne kręgów lędźwiowych. Notatka podaje opis ze s. 669.']),
        M('mm. skręcające', 'mm. rotatores', '669',
          layer='warstwa głęboka',
          parts=[
            'krótkie – dochodzą do sąsiedniego, wyżej leżącego kręgu [[mm. rotatores breves]]',
            'długie – mijają jeden kręg [[mm. rotatores longi]]',
            'wg odcinków: lędźwi, klatki piersiowej, szyi [[mm. rotatores lumborum, thoracis, cervicis]]',
          ],
          o=['tylne i górne brzegi wyrostków poprzecznych (od kości krzyżowej do C2) [[processus transversus]]',
             'w odcinku szyjnym: wyrostki stawowe dolne [[processus articularis inferior]]',
             'w odcinku lędźwiowym: wyrostki suteczkowate [[processus mamillaris]]'],
          i=['nasada wyrostków kolczystych wyżej leżących kręgów [[processus spinosus]]',
             'w odcinku szyjnym: podstawa wyrostków kolczystych',
             'w odcinku lędźwiowym: dolne brzegi łuków kręgów [[arcus vertebrae]]'],
          f=['jak m. wielodzielny'],
          warn=['Na s. 659 Bochenek zalicza mm. skręcające do krótkich mięśni grzbietu, a na s. 669 umieszcza je w grupie mięśni długich. Notatka idzie za s. 669.']),
      ]),
    ]),

    G('Krótkie mięśnie grzbietu', '', '669–671',
      intro='Łączą dwa sąsiednie kręgi (s. 669).',
      items=[
      M('mm. międzykolcowe', 'mm. interspinales', '669–670',
        parts=[
          'szyi – parzyste [[mm. interspinales cervicis]]',
          'lędźwi – nieparzyste [[mm. interspinales lumborum]]',
          'klatki piersiowej – przeważnie zanikłe [[mm. interspinales thoracis]]',
        ],
        att=['wierzchołki wyrostków kolczystych dwóch sąsiednich kręgów – w odcinku szyjnym i lędźwiowym [[processus spinosus]]'],
        f=['prostują kręgosłup w odcinku szyjnym i lędźwiowym'],
        extra=[('m. krzyżowo-guziczny tylny', 'm. sacrococcygeus dorsalis',
                'szczątkowa pozostałość mm. międzykolcowych między kością krzyżową a guziczną (s. 670)')],
        warn=['W streszczeniu (s. 676) Bochenek pisze: „Służą głównie ruchom obrotowym”. Notatka podaje opis ze s. 670.']),

      M('mm. międzypoprzeczne', 'mm. intertransversarii', '670',
        sub=[
          S('mm. międzypoprzeczne przednie szyi', 'mm. intertransversarii anteriores cervicis',
            att=['łączą guzki przednie wyrostków poprzecznych sąsiednich kręgów szyjnych [[processus transversus – tuberculum anterius]]']),
          S('mm. międzypoprzeczne tylne szyi', 'mm. intertransversarii posteriores cervicis',
            att=['łączą guzki tylne wyrostków poprzecznych sąsiednich kręgów szyjnych [[processus transversus – tuberculum posterius]]']),
          S('mm. międzypoprzeczne boczne lędźwi', 'mm. intertransversarii laterales lumborum',
            att=['łączą wyrostki żebrowe sąsiednich kręgów lędźwiowych [[processus costalis]]']),
          S('mm. międzypoprzeczne przyśrodkowe lędźwi', 'mm. intertransversarii mediales lumborum',
            att=['łączą wyrostki dodatkowe z wyrostkami suteczkowatymi [[processus accessorius; processus mamillaris]]']),
        ],
        f=['zginają kręgosłup bocznie'],
        extra=[('m. krzyżowo-guziczny przedni', 'm. sacrococcygeus ventralis',
                'niestały, szczątkowy; od przedniej powierzchni części bocznych ostatnich kręgów krzyżowych do przedniej powierzchni ostatniego kręgu guzicznego (s. 670–671)')]),

      M('mm. dźwigacze żeber', 'mm. levatores costarum', '671',
        note='12 z każdej strony',
        parts=[
          'krótkie – do następnego żebra [[mm. levatores costarum breves]]',
          'długie – w 3–4 dolnych przestrzeniach, mijają jedną przestrzeń międzyżebrową [[mm. levatores costarum longi]]',
        ],
        o=['wyrostki poprzeczne C7 i Th1–Th11 [[processus transversus]]'],
        i=['następne żebro; mięśnie długie – drugie z kolei żebro [[costa]]'],
        f=[
          'przypuszczalnie współdziałają przy prostowaniu kręgosłupa, pochylaniu go w bok i obracaniu w stronę przeciwległą',
          'Bochenek: nie unoszą żeber; ich praca jako mięśni wdechowych jest sporna',
        ]),
    ]),

    G('Mięśnie podpotyliczne', 'mm. suboccipitales', '671–673',
      intro='Pięć mięśni między kością potyliczną a dwoma górnymi kręgami (s. 671).',
      items=[
      M('m. skośny górny głowy', 'm. obliquus capitis superior', '671',
        o=['wyrostek poprzeczny kręgu szczytowego [[atlas – processus transversus]]'],
        i=['poniżej bocznego odcinka kresy karkowej dolnej [[linea nuchae inferior]]'],
        f=['jednostronnie: obraca głowę twarzą w stronę przeciwległą',
           'razem z mm. prostymi tylnymi i skośnym dolnym: pociąga głowę ku tyłowi'],
        warn=['W streszczeniu (s. 677) Bochenek pisze: „do bocznego odcinka kresy karkowej górnej”. Notatka podaje opis ze s. 671.']),
      M('m. prosty tylny mniejszy głowy', 'm. rectus capitis posterior minor', '671–672',
        o=['guzek tylny kręgu szczytowego [[atlas – tuberculum posterius]]'],
        i=['poniżej przyśrodkowego odcinka kresy karkowej dolnej [[linea nuchae inferior]]'],
        f=['pociąga głowę ku tyłowi',
           'oba mm. proste tylne jednej strony, razem ze skośnym dolnym: obracają głowę twarzą w tę samą stronę']),
      M('m. prosty tylny większy głowy', 'm. rectus capitis posterior major', '672',
        o=['wyrostek kolczysty kręgu obrotowego [[axis – processus spinosus]]'],
        i=['poniżej środkowej części kresy karkowej dolnej [[linea nuchae inferior]]'],
        f=['pociąga głowę ku tyłowi',
           'razem z prostym tylnym mniejszym i skośnym dolnym tej samej strony: obraca głowę twarzą w tę samą stronę']),
      M('m. skośny dolny głowy', 'm. obliquus capitis inferior', '672',
        o=['wyrostek kolczysty kręgu obrotowego [[axis – processus spinosus]]'],
        i=['wyrostek poprzeczny kręgu szczytowego [[atlas – processus transversus]]'],
        f=['obraca głowę razem z kręgiem szczytowym twarzą w tę samą stronę – jako jedyny bez równoczesnego unoszenia lub opuszczania głowy',
           'razem z mm. prostymi tylnymi: pociąga głowę ku tyłowi']),
      M('m. prosty boczny głowy', 'm. rectus capitis lateralis', '672–673',
        o=['wyrostek poprzeczny kręgu szczytowego [[atlas – processus transversus]]'],
        i=['powierzchnia dolna wyrostka szyjnego kości potylicznej [[processus jugularis]]'],
        f=['zgina głowę ku bokowi']),
    ]),
  ]),
])

# =====================================================================
# II. MIĘŚNIE KLATKI PIERSIOWEJ
# =====================================================================
KLATKA = G('Mięśnie klatki piersiowej', 'musculi thoracis°', '677–702', [

  G('Powierzchowne mięśnie klatki piersiowej', '', '678–684', [
    M('m. piersiowy większy', 'm. pectoralis major', '678–680',
      parts=[
        'część obojczykowa [[pars clavicularis]]',
        'część mostkowo-żebrowa [[pars sternocostalis]]',
        'część brzuszna – czasem jej brak [[pars abdominalis]]',
      ],
      o=[
        'przyśrodkowa połowa obojczyka [[clavicula]] – część obojczykowa',
        'powierzchnia przednia mostka (błona przednia mostka) [[sternum; membrana sterni]] – część mostkowo-żebrowa',
        'chrząstki żeber prawdziwych, często z wyjątkiem I i VII [[cartilago costalis]] – część mostkowo-żebrowa',
        'blaszka przednia pochewki m. prostego brzucha [[vagina m. recti abdominis]] – część brzuszna',
      ],
      i=['grzebień guzka większego kości ramiennej [[crista tuberculi majoris]]'],
      f=[
        'pociąga łopatkę do przodu',
        'przyciąga ramię przyśrodkowo i do przodu, opuszcza podniesione ramię i obraca je do wewnątrz (jak przy obejmowaniu)',
        'przy ustalonym podniesionym ramieniu podźwiga całe ciało ku górze (np. wspinanie się na linie)',
        'przy ustalonych ramionach – ważny pomocniczy mięsień wdechowy',
      ]),
    M('m. piersiowy mniejszy', 'm. pectoralis minor', '681–682',
      o=['powierzchnia zewnętrzna przednich końców żeber kostnych II lub III do V – 3–4 wiązki [[costa]]'],
      i=['wyrostek kruczy łopatki [[processus coracoideus]]'],
      f=[
        'obniża obręcz kończyny górnej (z dolnymi częściami m. czworobocznego i m. zębatego przedniego) i pociąga ją przyśrodkowo',
        'z m. piersiowym większym przesuwa obręcz kończyny górnej do przodu (np. przy podnoszeniu przedmiotu z podłogi)',
        'z dźwigaczem łopatki i m. równoległobocznym obraca łopatkę, obniżając nieco panewkę stawową',
        'przy ustalonym stawie ramiennym – mięsień wdechowy',
      ],
      warn=['W streszczeniu (s. 700) Bochenek podaje żebra III–V. Notatka podaje opis ze s. 681.']),
    M('m. podobojczykowy', 'm. subclavius', '682–683',
      o=['powierzchnia górna I żebra na granicy kostno-chrzęstnej, bocznie od więzadła żebrowo-obojczykowego [[costa I]]'],
      i=['powierzchnia dolna obojczyka przy końcu barkowym [[clavicula – extremitas acromialis]]'],
      f=[
        'pociąga obojczyk ku dołowi i do przodu',
        'hamuje ruchy w stawie mostkowo-obojczykowym',
        'przy podnoszeniu ramienia powiększa światło żyły podobojczykowej (jego powięź jest zrośnięta ze ścianą żyły)',
      ]),
    M('m. zębaty przedni', 'm. serratus anterior', '683–684',
      note='10 zębów na 9 górnych żebrach',
      parts=['część górna', 'część środkowa', 'część dolna'],
      o=[
        'część górna: I żebro (obok przyczepu m. pochyłego środkowego), guzowatość m. zębatego przedniego na II żebrze [[tuberositas m. serrati anterioris]] i łuk ścięgnisty między nimi',
        'część środkowa: żebra II i III [[costa]]',
        'część dolna: żebra IV–IX',
      ],
      i=[
        'część górna: strona żebrowa kąta górnego łopatki [[angulus superior; facies costalis]]',
        'część środkowa: brzeg przyśrodkowy łopatki [[margo medialis]]',
        'część dolna: strona żebrowa kąta dolnego łopatki [[angulus inferior]]',
      ],
      f=[
        '<b>część górna:</b> pociąga staw ramienny do przodu',
        '<b>część dolna:</b> z dolną częścią m. czworobocznego pociąga bark ku dołowi; obraca łopatkę – kąt dolny do przodu i bocznie, panewka ku górze – dzięki temu ramię może być odwiedzione ponad poziom',
        '<b>cały mięsień:</b> przyciska łopatkę do klatki piersiowej (z m. równoległobocznym)',
        'przy ustalonym barku i ramieniu – pomocniczy mięsień wdechowy',
      ]),
  ]),

  G('Głębokie albo właściwe mięśnie klatki piersiowej', '', '684–689', [
    M('mm. międzyżebrowe zewnętrzne', 'mm. intercostales externi', '685',
      note='od guzków żeber do bocznych końców chrząstek żebrowych; dalej do przodu – błony międzyżebrowe zewnętrzne [[membranae intercostales externae]]',
      o=['dolny brzeg wyżej leżącego żebra, na zewnątrz od bruzdy żebra [[sulcus costae]]'],
      i=['górny brzeg niżej leżącego żebra [[costa]]'],
      f=['unoszą żebra – mięśnie wdechowe',
         'razem z mm. międzyżebrowymi wewnętrznymi napinają ścianę międzyżebrzy, dzięki czemu w każdej fazie oddechu pozostaje ona równa (s. 687–688)']),
    M('mm. międzyżebrowe wewnętrzne', 'mm. intercostales interni', '686–687',
      note='od kątów żeber do mostka; dalej do tyłu – błony międzyżebrowe wewnętrzne [[membranae intercostales internae]]',
      parts=[
        'warstwa zewnętrzna – mm. międzyżebrowe pośrednie: zaczynają się, jak mm. zewnętrzne, na zewnątrz od bruzdy żebra i sięgają do mostka [[mm. intercostales intermedii]]',
        'warstwa wewnętrzna – mm. międzyżebrowe najgłębsze, kończą się na granicy chrzęstno-kostnej [[mm. intercostales intimi]]',
      ],
      o=['dolny brzeg wyżej leżącego żebra, do wewnątrz od bruzdy żebra [[sulcus costae]]'],
      i=['górny brzeg niżej leżącego żebra [[costa]]'],
      f=['opuszczają żebra – mięśnie wydechowe (Bochenek: tak należy przyjąć; sporne jest, czy same wystarczą do wydechu)']),
    M('mm. podżebrowe', 'mm. subcostales', '687',
      o=['powierzchnia wewnętrzna dolnych żeber w okolicy kątów żeber [[angulus costae]]'],
      i=['brzeg górny żebra po minięciu 1–2 żeber [[costa]]'],
      f=['mięśnie szczątkowe o niewielkim znaczeniu czynnościowym; włókna biegną jak w mm. międzyżebrowych wewnętrznych']),
    M('m. poprzeczny klatki piersiowej', 'm. transversus thoracis', '688–689',
      o=['powierzchnia tylna wyrostka mieczykowatego [[processus xiphoideus]] i dolnej części trzonu mostka [[corpus sterni]]'],
      i=['granica chrzęstno-kostna żeber II–VI – 5 zębów [[costa; cartilago costalis]]'],
      f=['część dolna, poprzeczna: zmniejsza kąt przyczepu chrząstek żebrowych do mostka – działa wydechowo',
         'górne wiązki: działanie bardzo nieznaczne']),
  ]),

  G('Przepona', 'diaphragma', '689–696', [
    M('przepona', 'diaphragma', '689–695',
      parts=[
        'część lędźwiowa [[pars lumbalis]]',
        'część żebrowa [[pars costalis]]',
        'część mostkowa [[pars sternalis]]',
      ],
      o=[
        'część lędźwiowa – odnogi: prawa [[crus dextrum]] od przedniej powierzchni trzonów L1–L3 (od więzadła podłużnego przedniego [[ligamentum longitudinale anterius]]), lewa [[crus sinistrum]] od L1–L2; przed rozworem aortowym łączą się w więzadło łukowate pośrodkowe [[ligamentum arcuatum medianum]]',
        'część lędźwiowa – więzadło łukowate przyśrodkowe [[ligamentum arcuatum mediale]] (trzon L1 lub L2 → wyrostek żebrowy L1) i boczne [[ligamentum arcuatum laterale]] (wyrostek żebrowy L1 → XII żebro)',
        'część żebrowa: powierzchnia wewnętrzna chrząstek żeber VII–XII – 6 wiązek [[cartilagines costales]]',
        'część mostkowa: powierzchnia wewnętrzna wyrostka mieczykowatego [[processus xiphoideus]]',
      ],
      i=['środek ścięgnisty – wspólne ścięgno końcowe wszystkich trzech części [[centrum tendineum]]'],
      f=[
        'ważny mięsień wdechowy: podczas skurczu spłaszcza się, kopuły obniżają się (przy spokojnym wdechu ok. 2 cm), jama klatki piersiowej powiększa się – tzw. oddychanie brzuszne',
        'podczas wydechu rozluźnioną przeponę podnosi napięcie mięśni brzucha',
        'czynna przy wydawaniu głosu – reguluje siłę wydechowego prądu powietrza',
        'przy ustalonej miednicy i klatce piersiowej kurczy się razem z mięśniami dna miednicy i mięśniami powłok brzucha – tłocznia brzuszna [[prelum abdominis]] (s. 716)',
      ]),
  ]),
])

# =====================================================================
# III. MIĘŚNIE BRZUCHA
# =====================================================================
BRZUCH = G('Mięśnie brzucha', 'musculi abdominis°', '702–733', [

  G('Boczne i przednie mięśnie brzucha', '', '704–712',
    intro='Boczne: trzy warstwy – m. skośny zewnętrzny, skośny wewnętrzny i poprzeczny brzucha. Przednie: układ mięśni prostych – m. prosty brzucha i m. piramidowy (s. 702, 704).',
    items=[
    M('m. skośny zewnętrzny brzucha', 'm. obliquus externus abdominis', '704–706',
      layer='boczny · warstwa I',
      o=['powierzchnia zewnętrzna żeber V–XII – najczęściej 8 wiązek [[costa]]'],
      i=[
        'rozcięgno – wchodzi w skład blaszki przedniej pochewki m. prostego brzucha [[vagina m. recti abdominis – lamina anterior]]',
        'kresa biała – krzyżuje się tu z włóknami strony przeciwnej [[linea alba]]',
        'więzadło pachwinowe – dolne pęczki rozcięgna [[ligamentum inguinale]]',
        'warga zewnętrzna grzebienia biodrowego – najbardziej tylne i dolne włókna [[crista iliaca – labium externum]]',
      ],
      f=[
        'jednostronnie: zgina kręgosłup i klatkę piersiową w bok i obraca tułów w stronę przeciwległą (współpracuje tu z m. skośnym wewnętrznym strony przeciwnej)',
        'obustronnie: zgina kręgosłup do przodu i pociąga klatkę piersiową ku dołowi – mięsień wydechowy',
        'przy ustalonej klatce piersiowej dźwiga miednicę',
        'prawy m. skośny zewnętrzny razem z lewym wewnętrznym kierują prawy staw ramienny do przodu',
      ]),
    M('m. skośny wewnętrzny brzucha', 'm. obliquus internus abdominis', '707–708',
      layer='boczny · warstwa II',
      o=[
        'powierzchnia tylna złączonych blaszek powięzi piersiowo-lędźwiowej [[fascia thoracolumbalis]]',
        'kresa pośrednia grzebienia biodrowego [[crista iliaca – linea intermedia]]',
        'boczne ⅔ więzadła pachwinowego [[ligamentum inguinale]]',
      ],
      i=[
        'brzegi dolne żeber X–XII – włókna tylne [[costa]]',
        'rozcięgno → pochewka m. prostego brzucha: w górnych ⅔ dzieli się na blaszkę przednią i tylną, w dolnej ⅓ biegnie tylko do przodu od mięśnia [[vagina m. recti abdominis]]',
        'kresa biała [[linea alba]]',
      ],
      f=[
        'obustronnie: zgina tułów do przodu i pociąga klatkę piersiową ku dołowi – wydech',
        'jednostronnie: obraca tułów w tę samą stronę i cofa staw ramienny tej strony (współpracuje z m. skośnym zewnętrznym strony przeciwnej)',
        'z m. skośnym zewnętrznym tej samej strony: zgina tułów w bok',
      ],
      ),
    M('m. poprzeczny brzucha', 'm. transversus abdominis', '708–710',
      layer='boczny · warstwa III',
      o=[
        'powierzchnia wewnętrzna chrząstek żebrowych VII–XII – 6 zębów, wchodzą między zęby przepony [[cartilago costalis]]',
        'linia połączenia obu blaszek powięzi piersiowo-lędźwiowej [[fascia thoracolumbalis]]',
        'warga wewnętrzna grzebienia biodrowego [[crista iliaca – labium internum]]',
        'boczna połowa więzadła pachwinowego [[ligamentum inguinale]]',
      ],
      i=[
        'wzdłuż kresy półksiężycowatej przechodzi w rozcięgno [[linea semilunaris]]',
        'rozcięgno → pochewka m. prostego brzucha: w górnych ⅔ blaszka tylna, w dolnej ⅓ blaszka przednia [[vagina m. recti abdominis]]',
        'kresa biała [[linea alba]]',
      ],
      f=[
        'zbliża żebra do płaszczyzny pośrodkowej, zwęża klatkę piersiową – wydech',
        'poprzecznie „sznuruje” ściany brzucha – główny mięsień tłoczni brzusznej',
      ]),
    M('dźwigacz jądra', 'm. cremaster', '710',
      note='utworzony z włókien m. skośnego wewnętrznego i m. poprzecznego brzucha',
      o=['dolny brzeg m. skośnego wewnętrznego i m. poprzecznego brzucha – pasmo boczne i przyśrodkowe przy powrózku nasiennym'],
      i=['powięź nasienna wewnętrzna, którą otacza łukowato (po przejściu przez pierścień powierzchowny kanału pachwinowego) [[fascia spermatica interna]]'],
      f=['unosi jądro w worku mosznowym',
         'u kobiety pojedyncze włókna dochodzą do więzadła obłego macicy']),
    M('m. prosty brzucha', 'm. rectus abdominis', '710–711',
      layer='przedni',
      parts=['smugi ścięgniste – najczęściej 3–4 [[intersectiones tendineae]]'],
      o=[
        'powierzchnia przednia chrząstek żebrowych V–VII [[cartilago costalis]]',
        'wyrostek mieczykowaty [[processus xiphoideus]]',
        'więzadła żebrowo-mieczykowe [[ligamenta costoxiphoidea]]',
      ],
      i=[
        'górna gałąź kości łonowej [[ramus superior ossis pubis]]',
        'powierzchnia przednia spojenia łonowego – krzyżuje się z włóknami strony przeciwnej [[symphysis pubica]]',
      ],
      f=[
        'zgina tułów do przodu – z leżenia na plecach podnosi górną połowę ciała albo unosi miednicę',
        'zginając tułów, opuszcza żebra – mięsień wydechowy',
        'wzmacnia tłocznię brzuszną',
        'antagonista prostownika grzbietu',
      ]),
    M('m. piramidowy', 'm. pyramidalis', '712',
      layer='przedni',
      note='mięsień szczątkowy, leży w pochewce m. prostego brzucha',
      o=['górne ramię kości łonowej i spojenie łonowe – do przodu od przyczepu m. prostego brzucha [[ramus superior ossis pubis; symphysis pubica]]'],
      i=['kresa biała [[linea alba]]'],
      f=['napina kresę białą; przy rozluźnionych mięśniach brzucha tworzy poniżej pępka bruzdę pośrodkową']),
  ]),

  G('Tylne mięśnie brzucha', '', '712–715', [
    REF('mm. międzypoprzeczne boczne lędźwi', 'mm. intertransversarii laterales lumborum', '670',
        'opisane przy krótkich mięśniach grzbietu; Bochenek zalicza je też do tylnych mięśni brzucha (s. 712)'),
    M('m. czworoboczny lędźwi', 'm. quadratus lumborum', '712–714',
      note='dwie warstwy włókien',
      sub=[
        S('warstwa przednia', '',
          o=['wyrostki żebrowe L2–L5 [[processus costalis]]'],
          i=['dolny brzeg XII żebra [[costa XII]]', 'trzon Th12 [[corpus vertebrae]]']),
        S('warstwa tylna', '',
          o=['warga wewnętrzna grzebienia biodrowego [[crista iliaca – labium internum]]', 'więzadło biodrowo-lędźwiowe [[ligamentum iliolumbale]]'],
          i=['wyrostki żebrowe L1–L4 [[processus costalis]]', 'dolny brzeg XII żebra']),
      ],
      f=[
        'jednostronnie: zgina tułów do boku (z m. lędźwiowym większym, m. krzyżowo-grzbietowym i mięśniami brzucha)',
        'mięśnie obu stron w napięciu spoczynkowym ustalają część lędźwiową kręgosłupa',
        'obustronnie: obniża XII żebra',
      ]),
  ]),
])

# =====================================================================
# IV. MIĘŚNIE SZYI
# =====================================================================
SZYJA = G('Mięśnie szyi', 'musculi colli°', '733–755',
  intro='Mięśnie położone do tyłu od kręgosłupa (mięśnie karku) Bochenek omawia przy grzbiecie (s. 733).',
  items=[

  G('Grupa powierzchowna mięśni szyi', '', '734–738', [
    M('m. szeroki szyi', 'platysma', '734–735',
      o=['tkanka podskórna okolicy podobojczykowej na wysokości II lub III żebra'],
      i=[
        'powięź przyusznicza i żwaczowa – część boczna włókien',
        'kąt ust – łączy się z obniżaczem wargi dolnej i obniżaczem kąta ust',
        'żuchwa powyżej podstawy, od guzka bródkowego do poziomu pierwszego zęba trzonowego [[basis mandibulae; tuberculum mentale]]',
      ],
      f=[
        'unosi skórę szyi z tkanką podskórną – zmniejsza ciśnienie na żyłę szyjną zewnętrzną i ułatwia krwiobieg',
        'pociąga kąty ust ku dołowi i bocznie – wyraz strachu, wściekłości, przerażenia',
      ]),
    M('m. mostkowo-obojczykowo-sutkowy', 'm. sternocleidomastoideus', '736–738',
      parts=['głowa przyśrodkowa (mostkowa)', 'głowa boczna (obojczykowa)'],
      o=[
        'głowa przyśrodkowa: powierzchnia przednia rękojeści mostka [[manubrium sterni]]',
        'głowa boczna: powierzchnia górna końca mostkowego obojczyka [[clavicula – extremitas sternalis]]',
      ],
      i=[
        'powierzchnia boczna wyrostka sutkowatego [[processus mastoideus]]',
        'boczny odcinek kresy karkowej górnej [[linea nuchae superior]]',
      ],
      f=[
        'jednostronnie (przy ustalonej klatce piersiowej): zgina głowę ku bokowi i obraca ją w stronę przeciwległą, unosząc twarz ku górze',
        'obustronnie: zgina głowę do tyłu, unosząc twarz, i wzmaga lordozę szyjną',
        'obustronnie, przy ustalonym i wyprostowanym odcinku szyjnym: może pociągać głowę do przodu (np. podnoszenie głowy u leżącego)',
        'przy ustalonej głowie unosi mostek – pomocniczy mięsień wdechowy',
      ]),
  ]),

  G('Grupa środkowa mięśni szyi', '', '738–744',
    intro='Wszystkie mięśnie tej grupy są związane z kością gnykową (s. 734).',
    items=[
    G('Mięśnie podgnykowe', 'mm. infrahyoidei', '738–741',
      intro='Powierzchownie: m. mostkowo-gnykowy i łopatkowo-gnykowy; głębiej: m. mostkowo-tarczowy i tarczowo-gnykowy (s. 738).',
      groupf=['wspólnie ustalają kość gnykową – staje się ona punktem podpory dla mięśni języka i przy obniżaniu żuchwy',
              'przy wielkim braku powietrza mogą brać pewien udział we wdechu'],
      groupf_pg='740',
      items=[
      M('m. mostkowo-gnykowy', 'm. sternohyoideus', '738–739',
        layer='warstwa powierzchowna',
        o=['powierzchnia tylna rękojeści mostka [[manubrium sterni]], stawu mostkowo-obojczykowego i końca mostkowego obojczyka [[clavicula – extremitas sternalis]]'],
        i=['trzon kości gnykowej – przyśrodkowo od m. łopatkowo-gnykowego [[corpus ossis hyoidei]]'],
        f=['z m. łopatkowo-gnykowym obniża kość gnykową']),
      M('m. łopatkowo-gnykowy', 'm. omohyoideus', '739',
        layer='warstwa powierzchowna',
        parts=['brzusiec dolny [[venter inferior]]', 'ścięgno pośrednie [[tendo intermedius]]', 'brzusiec górny [[venter superior]]'],
        o=['boczna część górnego brzegu łopatki [[margo superior scapulae]] i więzadło poprzeczne łopatki, aż do podstawy wyrostka kruczego [[ligamentum transversum scapulae]]'],
        i=['trzon kości gnykowej – bocznie od m. mostkowo-gnykowego [[corpus ossis hyoidei]]'],
        f=['napina blaszkę przedtchawiczą powięzi szyi i przez to zwiększa światło żyły szyjnej wewnętrznej',
           'z m. mostkowo-gnykowym obniża kość gnykową']),
      M('m. mostkowo-tarczowy', 'm. sternothyroideus', '739–740',
        layer='warstwa głębsza',
        o=['powierzchnia tylna rękojeści mostka [[manubrium sterni]] i chrząstki I żebra – poniżej m. mostkowo-gnykowego [[cartilago costalis]]'],
        i=['kresa skośna chrząstki tarczowatej [[linea obliqua cartilaginis thyroideae°]]',
           'poszczególne włókna przechodzą bezpośrednio w m. tarczowo-gnykowy i część tarczowo-gardłową dolnego zwieracza gardła'],
        f=['obniża chrząstkę tarczowatą']),
      M('m. tarczowo-gnykowy', 'm. thyrohyoideus', '740',
        layer='warstwa głębsza',
        o=['kresa skośna chrząstki tarczowatej [[linea obliqua cartilaginis thyroideae°]]'],
        i=['trzon i rogi większe kości gnykowej – do tyłu od mm. mostkowo-gnykowego i łopatkowo-gnykowego [[corpus ossis hyoidei; cornua majora]]'],
        f=['unosi chrząstkę tarczowatą z całą krtanią podczas łykania']),
    ]),

    G('Mięśnie nadgnykowe', 'mm. suprahyoidei', '741–744', [
      M('m. dwubrzuścowy', 'm. digastricus', '741',
        parts=['brzusiec tylny [[venter posterior]]', 'ścięgno pośrednie [[tendo intermedius]]', 'brzusiec przedni [[venter anterior]]'],
        o=['brzusiec tylny: wcięcie sutkowe kości skroniowej [[incisura mastoidea]]'],
        i=[
          'brzusiec przedni: dół dwubrzuścowy żuchwy [[fossa digastrica]]',
          'ścięgno pośrednie: przebija m. rylcowo-gnykowy; włóknista pętla blaszki powierzchownej powięzi szyi przytwierdza je do trzonu i nasady rogów większych kości gnykowej [[corpus ossis hyoidei; cornua majora]]',
        ],
        f=['przy ustalonej kości gnykowej opuszcza żuchwę',
           'przy ustalonej żuchwie podnosi kość gnykową – oba brzuśce razem albo jeden (wtedy kość gnykowa idzie do przodu lub do tyłu)']),
      M('m. rylcowo-gnykowy', 'm. stylohyoideus', '743',
        o=['wyrostek rylcowaty kości skroniowej [[processus styloideus]]'],
        i=['trzon lub rogi większe kości gnykowej; przy przyczepie obejmuje dwiema odnogami ścięgno pośrednie m. dwubrzuścowego [[corpus ossis hyoidei; cornua majora]]'],
        f=['pociąga kość gnykową ku górze i ku tyłowi']),
      M('m. żuchwowo-gnykowy', 'm. mylohyoideus', '743–744',
        note='z mięśniem strony przeciwnej tworzy dno jamy ustnej',
        o=['kresa żuchwowo-gnykowa żuchwy [[linea mylohyoidea]]'],
        i=['szew pośrodkowy rozpięty między kością gnykową a spojeniem żuchwy',
           'włókna tylne: powierzchnia przednia trzonu kości gnykowej [[corpus ossis hyoidei]]'],
        f=['przy ustalonej kości gnykowej obniża żuchwę',
           'przy ustalonej żuchwie unosi kość gnykową ku górze i do przodu, napina dno jamy ustnej, podpiera i unosi język; ważny przy łykaniu']),
      M('m. bródkowo-gnykowy', 'm. geniohyoideus', '744',
        o=['kolec bródkowy żuchwy [[spina mentalis]]'],
        i=['powierzchnia przednia trzonu kości gnykowej [[corpus ossis hyoidei]]'],
        f=['pociąga kość gnykową do przodu i ku górze',
           'przy ustalonej kości gnykowej opuszcza żuchwę',
           'unosi język w pierwszym okresie łykania (z m. żuchwowo-gnykowym i dwubrzuścowym)']),
    ]),
  ]),

  G('Grupa głęboka mięśni szyi', '', '744–748',
    intro='Wszystkie zaczynają się na kręgosłupie. Podgrupa boczna – mięśnie pochyłe (dochodzą do żeber); podgrupa przyśrodkowa – mięśnie przedkręgowe (łączą się tylko z kręgami) (s. 744).',
    items=[
    G('Mięśnie pochyłe', 'mm. scaleni', '744–747',
      intro='podgrupa boczna',
      groupf=['jednostronnie: pochylają kręgosłup w odcinku szyjnym do boku',
              'obustronnie: zginają go do przodu',
              'przy ustalonym kręgosłupie dźwigają żebra ku górze – pomocnicze mięśnie wdechowe, szczególnie przy przegiętej do tyłu szyi i głowie'],
      groupf_pg='745',
      items=[
      M('m. pochyły przedni', 'm. scalenus anterior', '744–745',
        o=['guzki przednie wyrostków poprzecznych C3–C6 – 4 pasma [[processus transversus – tuberculum anterius]]'],
        i=['guzek m. pochyłego przedniego na I żebrze [[tuberculum m. scaleni anterioris]]']),
      M('m. pochyły środkowy', 'm. scalenus medius', '745',
        o=['brzeg boczny bruzdy nerwu rdzeniowego wyrostków poprzecznych C1–C6 (C7) – 6–7 pasm [[sulcus nervi spinalis]]'],
        i=['I żebro – do tyłu od bruzdy tętnicy podobojczykowej [[sulcus arteriae subclaviae]]',
           'często też powięź I przestrzeni międzyżebrowej i górny brzeg II żebra [[costa II]]']),
      M('m. pochyły tylny', 'm. scalenus posterior', '745',
        o=['guzki tylne wyrostków poprzecznych C5 lub C6 i C7 – 2–3 pasma [[processus transversus – tuberculum posterius]]'],
        i=['powierzchnia boczna II żebra [[costa II]]']),
      M('m. pochyły najmniejszy', 'm. scalenus minimus', '745', tag='niestały',
        o=['wyrostki poprzeczne C6 albo C6 i C7 – 1–2 pasma [[processus transversus]]'],
        i=['powierzchnia boczna I żebra [[costa I]] i osklepek opłucnej']),
    ]),

    G('Mięśnie przedkręgowe', 'musculi prevertebrales°', '747–748',
      intro='podgrupa przyśrodkowa',
      items=[
      M('m. prosty przedni głowy', 'm. rectus capitis anterior', '747',
        o=['łuk przedni i nasada wyrostka poprzecznego kręgu szczytowego [[atlas – arcus anterior; processus transversus]]'],
        i=['część podstawna kości potylicznej [[pars basilaris ossis occipitalis]]'],
        f=['zgina głowę do przodu i w stronę boczną']),
      M('m. długi głowy', 'm. longus capitis', '747',
        o=['guzki przednie wyrostków poprzecznych C3–C6 [[processus transversus – tuberculum anterius]]'],
        i=['część podstawna kości potylicznej – nieco do przodu od m. prostego przedniego głowy [[pars basilaris ossis occipitalis]]'],
        f=['zgina głowę do przodu i w stronę boczną']),
      M('m. długi szyi', 'm. longus colli', '747–748',
        note='od kręgu szczytowego do Th3; trzy pasma',
        sub=[
          S('pasmo przyśrodkowe (podłużne)', '',
            o=['trzony C2–C4 [[corpus vertebrae]]'],
            i=['trzony C6–C7 i Th1–Th3']),
          S('pasmo boczne skośne górne', '',
            o=['guzki przednie wyrostków poprzecznych C3–C6 [[processus transversus – tuberculum anterius]]'],
            i=['guzek przedni kręgu szczytowego [[atlas – tuberculum anterius]] i trzon kręgu obrotowego [[axis]]']),
          S('pasmo boczne skośne dolne', '',
            o=['trzony Th1–Th3 [[corpus vertebrae]]'],
            i=['guzki przednie wyrostków poprzecznych C6 i C7 albo C5 i C6']),
        ],
        f=['zgina kręgosłup w odcinku szyjnym do przodu i w stronę boczną oraz obraca go w swoją stronę']),
    ]),
  ]),
])

CHAPTERS = [
  dict(id='grzbiet', num='I', color='#1f6f78', g=GRZBIET),
  dict(id='klatka', num='II', color='#a23b3b', g=KLATKA),
  dict(id='brzuch', num='III', color='#a8741a', g=BRZUCH),
  dict(id='szyja', num='IV', color='#3e4f9c', g=SZYJA),
]
