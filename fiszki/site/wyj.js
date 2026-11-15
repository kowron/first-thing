/* Wyjaśnienie „po ludzku”: jak ruszają się żebra przy oddychaniu (stawy żebrowo-kręgowe i mostkowo-żebrowe).
   Tekst własny, bez cytatów; rysunki w wyj_figs.js (window.WYJ_FIG). Otwierane z lekcji „Połączenia żeber”
   i z pytań o ruchy żeber oraz o połączenia żeber z mostkiem. */
(function(){
'use strict';
var A=window.__so5;if(!A)return;
var S_ZEBRA=[
{h:'Po co żebra w ogóle się ruszają',p:[
 'Płuca same nie mają mięśni. Powietrze wchodzi do nich tylko dlatego, że klatka piersiowa robi się większa i „zasysa” je do środka. Klatkę można powiększyć na dwa sposoby: obniżyć jej dno (to robi przepona) albo rozsunąć jej ściany (to robią żebra).',
 'Żebro nie biegnie poziomo. Od kręgosłupa schodzi skośnie w dół i do przodu, jak opuszczona rączka. Wystarczy więc unieść jego przedni koniec, a żebro odsunie się od kręgosłupa i klatka zrobi się szersza i głębsza. <b>Cały wdech żebrowy to po prostu unoszenie żeber, a wydech to ich opadanie.</b>']},
{h:'Żebro wisi na dwóch stawach, więc działa jak zawias',f:'dwa-stawy',p:[
 'Z tyłu każde żebro (od I do X) trzyma się kręgosłupa w dwóch miejscach: głową przy trzonie kręgu i guzkiem przy końcu wyrostka poprzecznego. Dwa punkty zaczepienia to jak dwa zawiasy drzwi: wyznaczają jedną linię, wokół której można się obracać.',
 'Ta linia to <b>oś obrotu</b>. Biegnie wzdłuż szyjki żebra, przez oba stawy. Żebro nie może się wokół niej „kręcić jak śmigło”, bo z przodu jest przywiązane do mostka. Może tylko trochę się uchylić: przedni koniec idzie w górę przy wdechu i w dół przy wydechu.',
 'Żebra XI i XII nie mają stawu przy wyrostku poprzecznym i nie dochodzą do mostka. Dla oddychania prawie się nie liczą.']},
{h:'Dlaczego górne żebra idą do przodu, a dolne na boki',f:'kat-osi',p:[
 'Wszystko zależy od tego, jak ustawiona jest oś. Drzwi zawsze otwierają się prostopadle do linii zawiasów. Żebro tak samo: jego koniec zatacza łuk w płaszczyźnie prostopadłej do osi szyjki.',
 'U góry klatki wyrostki poprzeczne sterczą prawie dokładnie na boki, więc oś leży prawie poprzecznie (odchyla się od niej tylko o ok. 10° przy żebrze I). Im niżej, tym bardziej wyrostki odginają się do tyłu i oś robi się skośna, aż do ok. 45° przy żebrze X.',
 'Skutek: żebro z osią poprzeczną unosi się <b>do przodu</b>. Żebro z osią skośną unosi się bardziej <b>na bok</b>.']},
{h:'Dwa obrazki do zapamiętania: rączka pompy i rączka wiadra',f:'pompa-wiadro',p:[
 '<b>Rączka pompy</b> to ruch górnych żeber razem z mostkiem. Przedni koniec żebra i mostek idą w górę i do przodu, jak dźwignia starej pompy. Klatka robi się głębsza: rośnie wymiar przednio-tylny.',
 '<b>Rączka wiadra</b> to ruch dolnych żeber. Żebro jest zaczepione z tyłu (kręgosłup) i z przodu (mostek), a jego środek zwisa w dół jak pałąk wiadra. Przy wdechu pałąk unosi się na bok. Klatka robi się szersza: rośnie wymiar poprzeczny.',
 'W praktyce każde żebro robi trochę jednego i trochę drugiego. U góry przeważa pompa, u dołu wiadro.']},
{h:'Trzy typy ruchu żeber – to, o co pytają',f:'trzy-typy',p:[
 'Model „zawiasu” pasuje idealnie tylko do części żeber. Stawy przy wyrostkach poprzecznych nie są wszędzie zbudowane tak samo, dlatego wyróżnia się trzy typy ruchu. Dla każdego zapamiętaj: <b>jaki to ruch</b> i <b>w którą stronę idzie żebro najmocniej</b>.',
 '<b>Typ żeber II–V: czysty obrót.</b> Guzek żebra jest wypukły i siedzi w dołku wyrostka poprzecznego, więc staw pozwala tylko na obrót wokół osi szyjki. To jest książkowy zawias. Przy wdechu żebro idzie najmocniej w górę, słabiej w bok, najsłabiej do przodu.',
 '<b>Typ żeber VI–X: ślizg.</b> Tu powierzchnie stawowe są płaskie. Guzek nie obraca się w dołku, tylko <b>przesuwa się po wyrostku poprzecznym w górę i ku tyłowi</b>. Żebro nie kręci się więc wokół osi szyjki, tylko całe odchyla się jak pałąk wiadra. Przy wdechu idzie najmocniej w górę, słabiej w bok i odrobinę ku tyłowi (nie do przodu!).',
 '<b>Typ żebra I: obrót i ślizg naraz.</b> Żebro I ma oś prawie poprzeczną i trochę inaczej zbudowane stawy. Sam obrót dałby za mały ruch, więc dochodzi do niego ślizg: żebro przesuwa się względem wyrostka poprzecznego w górę przy wdechu i w dół przy wydechu. Przód żebra I idzie najmocniej w górę, słabiej do przodu, najsłabiej w bok.',
 'Jak to spiąć w jedno zdanie: <b>I – obrót ze ślizgiem (w górę i do przodu), II–V – obrót wokół szyjki (w górę i w bok), VI–X – ślizg guzka po wyrostku (w górę, w bok i trochę do tyłu).</b>']},
{h:'Ile to jest w milimetrach',f:'ile-mm',p:[
 'Liczby pomagają zobaczyć, że ruch jest mały, ale nie taki sam na każdym poziomie. Chodzi o drogę przedniego końca żebra kostnego.',
 '<b>W górę:</b> najwięcej żebro IV, ok. 35 mm; najmniej żebra I i X, ok. 25 mm. <b>W bok:</b> rośnie ku dołowi, od ok. 10 mm przy żebrze I do ok. 22 mm przy dolnych. <b>Do przodu:</b> maleje od ok. 15 mm przy żebrze I do ok. 1 mm przy V, a od żebra VI zamienia się w niewielki ruch <b>ku tyłowi</b> (od 2 do 8 mm przy X).',
 'Im bliżej kręgosłupa leży punkt na żebrze, tym mniejszą drogę pokonuje. Najwięcej porusza się przedni koniec.']},
{h:'Co się dzieje z przodu: chrząstka żebrowa i staw z mostkiem',f:'chrzastka-mostek',p:[
 'Prawe i lewe żebro są z przodu spięte mostkiem w jeden pierścień. Gdyby ten pierścień był w całości z kości, nie dałoby się go ruszyć, bo prawe i lewe żebro obracają się wokół dwóch różnie ustawionych osi. Ruch jest możliwy tylko dlatego, że między żebrem kostnym a mostkiem jest sprężysta wstawka: <b>chrząstka żebrowa</b>.',
 'Kiedy żebro się unosi, z przodu dzieją się naraz trzy rzeczy. <b>Po pierwsze</b> otwiera się kąt, pod którym chrząstka jest zgięta (u żeber I–V ten kąt leży na granicy kości i chrząstki, niżej w samej chrząstce). <b>Po drugie</b> chrząstka obraca się w <b>stawie mostkowo-żebrowym</b>, więc rośnie kąt między nią a mostkiem. <b>Po trzecie</b> chrząstka skręca się wzdłuż własnej długości, jak wyżymana szmatka, a jej górny brzeg obraca się lekko do wewnątrz.',
 'Staw mostkowo-żebrowy sam z siebie rusza się więc niewiele. Jego rola to pozwolić chrząstce zmienić kąt względem mostka. Żebro I nie ma tu stawu, tylko chrząstkozrost: jest z mostkiem połączone na sztywno i porusza się razem z rękojeścią jak jedna część.',
 'Skręcona i odgięta chrząstka zachowuje się jak napięta sprężyna. Dlatego po wdechu klatka sama wraca w stronę położenia spoczynkowego i spokojny wydech prawie nie wymaga pracy mięśni. Z tego samego powodu skostnienie chrząstek (u osób starszych) usztywnia klatkę i utrudnia oddychanie żebrami.']},
{h:'A mostek?',p:[
 'Mostek nie ma własnego napędu, jedzie na żebrach. Przy wdechu przesuwa się <b>w górę i do przodu</b>, prawie równolegle do siebie. „Prawie”, bo dolne żebra są dłuższe od górnych, więc dół mostka wysuwa się do przodu trochę bardziej niż góra.',
 'Rękojeść i trzon mostka nie leżą w jednej linii, tworzą <b>kąt mostka</b> (ok. 164°, na wysokości II żebra). Przy głębokim wdechu ten kąt trochę się prostuje. To jedyny własny ruch w obrębie mostka.']},
{h:'Całość w sześciu zdaniach',p:[
 '1. Wdech żebrowy to unoszenie żeber, wydech to ich opadanie.',
 '2. Żebro obraca się wokół osi, która biegnie przez szyjkę i oba stawy z kręgosłupem.',
 '3. U góry oś jest prawie poprzeczna, więc żebra idą do przodu (rączka pompy); u dołu skośna, więc idą na boki (rączka wiadra).',
 '4. Trzy typy: żebro I – obrót ze ślizgiem; żebra II–V – czysty obrót wokół szyjki; żebra VI–X – ślizg guzka po wyrostku poprzecznym w górę i ku tyłowi.',
 '5. Z przodu ruch umożliwia chrząstka żebrowa: otwiera kąt, obraca się w stawie mostkowo-żebrowym i skręca się jak sprężyna.',
 '6. Mostek idzie w górę i do przodu, dołem bardziej niż górą, a kąt mostka się prostuje.']}
];
var S_KANAL=[
{h:'Czym jest kanał pachwinowy',p:[
 'To nie jest rura z otworem w środku. To <b>skośna szczelina w przedniej ścianie brzucha</b>, tuż nad pachwiną, którą coś przechodzi z brzucha na zewnątrz: u mężczyzny powrózek nasienny (do jądra), u kobiety więzadło obłe macicy.',
 'U zdrowego dorosłego kanał jest „zamknięty”: jego ściany przylegają do tego, co przez niego biegnie, i nie ma wolnego światła. Dlatego mówi się, że istnieje tylko potencjalnie. Staje się prawdziwym kanałem dopiero wtedy, gdy coś go rozepchnie, na przykład pętla jelita przy przepuklinie.']},
{h:'Gdzie leży i jak biegnie',f:'kp-polozenie',p:[
 'Znajdź dwa punkty kostne: kolec biodrowy przedni górny (wystający kant miednicy z boku) i guzek łonowy (przy spojeniu łonowym). Między nimi rozpięte jest <b>więzadło pachwinowe</b>. Kanał leży tuż nad jego przyśrodkową połową.',
 'Kanał ma 4–5 cm i biegnie <b>skośnie</b>: z głębi na powierzchnię, z góry na dół i z boku ku środkowi ciała. Jest prawie równoległy do więzadła pachwinowego (odchyla się od niego o ok. 15°).',
 'Ma dwa końce. <b>Pierścień głęboki</b> to wejście od strony brzucha: leży mniej więcej w połowie długości więzadła pachwinowego, ok. 2 cm nad nim. <b>Pierścień powierzchowny</b> to wyjście pod skórę: leży tuż nad guzkiem łonowym, trochę bocznie od niego. Da się go wyczuć palcem.',
 'Po co ten skos? Wejście i wyjście nie leżą naprzeciw siebie. Gdy rośnie ciśnienie w brzuchu (kaszel, dźwiganie), tylna ściana kanału jest dociskana do przedniej i szczelina się zamyka, jak zawór.']},
{h:'Skąd się wziął: droga jądra',p:[
 'Jądro powstaje wysoko w jamie brzusznej, przy kręgosłupie lędźwiowym. Przed urodzeniem (w 7.–9. miesiącu) przechodzi przez ścianę brzucha do moszny. Kanał pachwinowy to ślad po tej wędrówce.',
 'Drogę wyznaczają dwie rzeczy. <b>Jądrowód</b> to pasmo, które łączy jądro z okolicą pachwiny i „prowadzi” je w dół; po wszystkim prawie zanika. <b>Wyrostek pochwowy otrzewnej</b> to uwypuklenie otrzewnej w kształcie palca rękawiczki, które wysuwa się przez ścianę brzucha aż do moszny; jądro schodzi wzdłuż jego tylnej strony.',
 'Po zstąpieniu jądra wyrostek pochwowy zarasta. Zostaje z niego tylko dno, które obejmuje jądro jako jego osłonka surowicza. Jeśli nie zarośnie, zostaje gotowa droga dla przepukliny wrodzonej.',
 'U kobiety jajnik nie wychodzi z brzucha, schodzi tylko do miednicy. Odpowiednik jądrowodu zostaje na stałe: jego dłuższa część to <b>więzadło obłe macicy</b>, które przechodzi przez kanał i kończy się na wzgórku łonowym i w wardze sromowej większej.']},
{h:'Cztery ściany',f:'kp-sciany',p:[
 'Skoro kanał jest szczeliną między warstwami ściany brzucha, jego ściany to po prostu te warstwy. Dwie są szerokie (przednia i tylna), dwie wąskie (górna i dolna).',
 '<b>Przednia</b> (od strony skóry): rozcięgno mięśnia skośnego zewnętrznego. <b>Tylna</b> (od strony brzucha): powięź poprzeczna, wzmocniona dwoma pasmami: więzadłem międzydołkowym i sierpem pachwinowym. <b>Górna</b>, czyli strop: dolne włókna mięśnia skośnego wewnętrznego i poprzecznego, które przechodzą łukiem nad powrózkiem. <b>Dolna</b>, czyli dno: więzadło pachwinowe, wygięte w rynienkę, w której leży powrózek.',
 'Jak to zapamiętać: z przodu najbardziej zewnętrzny mięsień płaski, z tyłu najgłębsza powięź, u góry dwa mięśnie środkowe, u dołu więzadło.']},
{h:'Dwa pierścienie z bliska',f:'kp-pierscienie',p:[
 '<b>Pierścień powierzchowny</b> to trójkątna szczelina w rozcięgnie mięśnia skośnego zewnętrznego. Włókna rozcięgna rozchodzą się tu na dwie strony i tworzą dwie <b>odnogi</b>: przyśrodkową (nad otworem) i boczną (pod otworem; przechodzi w więzadło pachwinowe). Żeby szczelina nie rozdzierała się dalej, od przodu spinają ją poprzeczne <b>włókna międzyodnogowe</b>. Od tyłu i dołu otwór zamyka <b>więzadło zagięte</b>: włókna, które odchodzą od więzadła pachwinowego i idą za nim w stronę kresy białej.',
 'Razem są więc cztery ograniczenia: odnoga przyśrodkowa, odnoga boczna, włókna międzyodnogowe (odnoga przednia) i więzadło zagięte (odnoga tylna).',
 '<b>Pierścień głęboki</b> to nie dziura z ostrymi brzegami, tylko miejsce, w którym powięź poprzeczna wpukla się do kanału jak rękaw. Najważniejsza rzecz do zapamiętania: leży <b>bocznie od naczyń nabrzusznych dolnych</b>. Te naczynia są granicą, według której odróżnia się dwa rodzaje przepuklin pachwinowych.']},
{h:'Co przechodzi przez kanał i skąd ma osłonki',f:'kp-oslonki',p:[
 'U mężczyzny przez kanał biegnie <b>powrózek nasienny</b>: nasieniowód razem z naczyniami i nerwami jądra. Nasieniowód jest twardy jak sznurek i da się go wyczuć przez skórę.',
 'Jądro, przechodząc przez ścianę brzucha, wypchnęło przed sobą każdą jej warstwę, jak palec wypycha kolejne warstwy materiału. Każda wypchnięta warstwa została jako osłonka powrózka i jądra. Od środka: <b>powięź poprzeczna</b> daje powięź nasienną wewnętrzną; <b>mięsień skośny wewnętrzny i poprzeczny</b> dają dźwigacz jądra; <b>rozcięgno mięśnia skośnego zewnętrznego z powięzią powierzchowną</b> dają powięź dźwigacza jądra.',
 'Powrózek „zbiera” więc osłonki po drodze i komplet ma dopiero przy pierścieniu powierzchownym.',
 'U kobiety przez kanał przechodzi tylko więzadło obłe macicy, dlatego kanał jest węższy.']},
{h:'Widok od środka: fałdy, doły i przepukliny',f:'kp-od-srodka',p:[
 'Gdy spojrzeć na przednią ścianę brzucha od strony jamy brzusznej, poniżej pępka widać pięć fałdów otrzewnej. <b>Pośrodkowy</b> (jeden) biegnie od pęcherza do pępka. <b>Przyśrodkowe</b> (dwa) leżą po bokach od niego. <b>Boczne</b> (dwa) zawierają naczynia nabrzuszne dolne.',
 'Między fałdami po każdej stronie są trzy doły: nadpęcherzowy, pachwinowy przyśrodkowy i pachwinowy boczny. Dwa ostatnie to słabe miejsca ściany.',
 '<b>Dół pachwinowy boczny</b> leży bocznie od naczyń nabrzusznych dolnych i odpowiada pierścieniowi głębokiemu. Przepuklina, która tędy wchodzi, przechodzi przez cały kanał, czyli skośnie. To <b>przepuklina boczna (skośna)</b>.',
 '<b>Dół pachwinowy przyśrodkowy</b> leży przyśrodkowo od tych naczyń, dokładnie naprzeciw pierścienia powierzchownego. Przepuklina przebija tu tylną ścianę kanału na wprost i wychodzi przez pierścień powierzchowny, omijając pierścień głęboki. To <b>przepuklina przyśrodkowa (prosta)</b>.',
 'Reguła: <b>bocznie od naczyń nabrzusznych dolnych – skośna, przyśrodkowo – prosta.</b>']},
{h:'Całość w sześciu zdaniach',p:[
 '1. Kanał pachwinowy to skośna szczelina długości 4–5 cm w ścianie brzucha, tuż nad przyśrodkową połową więzadła pachwinowego.',
 '2. Zaczyna się pierścieniem głębokim (w powięzi poprzecznej, bocznie od naczyń nabrzusznych dolnych), kończy pierścieniem powierzchownym (w rozcięgnie mięśnia skośnego zewnętrznego, nad guzkiem łonowym).',
 '3. Ściany: przednia – rozcięgno mięśnia skośnego zewnętrznego; tylna – powięź poprzeczna; górna – mięsień skośny wewnętrzny i poprzeczny; dolna – więzadło pachwinowe.',
 '4. Pierścień powierzchowny ograniczają: odnoga przyśrodkowa, odnoga boczna, włókna międzyodnogowe i więzadło zagięte.',
 '5. Zawartość: u mężczyzny powrózek nasienny (jego osłonki to wyciągnięte warstwy ściany brzucha), u kobiety więzadło obłe macicy.',
 '6. Przepuklina boczna idzie przez pierścień głęboki i cały kanał, przyśrodkowa przebija tylną ścianę naprzeciw pierścienia powierzchownego.']}
];
var T={
 zebra:{S:S_ZEBRA,tis:'joint',t:'Jak ruszają się żebra przy oddychaniu',d:'Stawy żebrowo-kręgowe i mostkowo-żebrowe wytłumaczone prosto, z rysunkami. Najważniejsze są trzy typy ruchu żeber.',
   lesson:'polaczenia-zeber',units:{'zebra-osie':1,'mostkowo-zebrowe':1,'mechanizm':1},bt:'Nie rozumiesz ruchów żeber?',bd:'Wyjaśnienie prostym językiem, z rysunkami: oś obrotu, rączka pompy i wiadra, trzy typy ruchu.'},
 kanal:{S:S_KANAL,tis:'muscle',t:'Kanał pachwinowy',d:'Gdzie leży, skąd się wziął, co go ogranicza i co przez niego przechodzi. Prosto, z rysunkami.',
   lesson:'brzuch',units:{'kanal-pachwinowy':1,'pod-powiezia':1},bt:'Kanał pachwinowy bez tajemnic',bd:'Wyjaśnienie prostym językiem, z rysunkami: przebieg, cztery ściany, dwa pierścienie, osłonki powrózka, przepukliny.'}
};
var ret=null,cur=null;
function open(id,back){var t=T[id];if(!t)return;cur=id;A.setView('wyj');A.nav('home');A.setTis(t.tis);var F=window.WYJ_FIG||{};
  var h='<div><button class="back" data-w="back">'+A.ICO.back+' Wróć</button></div>'
   +'<div><div class="eb">Wyjaśnienie własnymi słowami</div><h1>'+t.t+'</h1><p class="mut" style="margin-top:8px">'+t.d+'</p></div>';
  t.S.forEach(function(s){h+='<section class="wy"><h2>'+s.h+'</h2>'+(s.f&&F[s.f]?'<figure class="sch">'+F[s.f]+'</figure>':'')+s.p.map(function(x){return '<p>'+x+'</p>'}).join('')+'</section>'});
  A.page(h);ret=back}
function btn(id,b){var t=T[id];return '<button class="wybtn t-'+t.tis+'" data-w="open" data-t="'+id+'" data-b="'+b+'"><span><b>'+t.bt+'</b>'+t.bd+'</span>'+A.ICO.ch+'</button>'}
document.addEventListener('click',function(e){var el=e.target.closest('[data-w]');if(!el)return;var a=el.getAttribute('data-w');
  if(a==='open')open(el.getAttribute('data-t'),el.getAttribute('data-b')||'');
  else if(a==='back'){var m=(ret||'').split(':');
    if(m[0]==='u'&&A.UNITS[m[1]])A.unitView(A.UNITS[m[1]],'lesson');
    else{var id=T[cur]?T[cur].lesson:'';var L=A.LESSONS.filter(function(l){return l.id===id})[0];if(L)A.lessonView(L);else A.home()}}});
/* przyciski wstawiane w lekcji i przy pytaniach */
window.WYJ_UI={forLesson:function(id){return Object.keys(T).filter(function(k){return T[k].lesson===id}).map(function(k){return btn(k,'')}).join('')},
  forUnit:function(id){return Object.keys(T).filter(function(k){return T[k].units[id]}).map(function(k){return btn(k,'u:'+id)}).join('')}};
})();
