/* Wyjaśnienie „po ludzku”: jak ruszają się żebra przy oddychaniu (stawy żebrowo-kręgowe i mostkowo-żebrowe).
   Tekst własny, bez cytatów; rysunki w wyj_figs.js (window.WYJ_FIG). Otwierane z lekcji „Połączenia żeber”
   i z pytań o ruchy żeber oraz o połączenia żeber z mostkiem. */
(function(){
'use strict';
var A=window.__so5;if(!A)return;
var S=[
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
function open(back){A.setView('wyj');A.nav('home');A.setTis('joint');var F=window.WYJ_FIG||{};
  var h='<div><button class="back" data-w="back">'+A.ICO.back+' Wróć</button></div>'
   +'<div><div class="eb">Wyjaśnienie własnymi słowami</div><h1>Jak ruszają się żebra przy oddychaniu</h1><p class="mut" style="margin-top:8px">Stawy żebrowo-kręgowe i mostkowo-żebrowe wytłumaczone prosto, z rysunkami. Najważniejsze są trzy typy ruchu żeber.</p></div>';
  S.forEach(function(s){h+='<section class="wy"><h2>'+s.h+'</h2>'+(s.f&&F[s.f]?'<figure class="sch">'+F[s.f]+'</figure>':'')+s.p.map(function(x){return '<p>'+x+'</p>'}).join('')+'</section>'});
  A.page(h);ret=back}
var ret=null;
document.addEventListener('click',function(e){var el=e.target.closest('[data-w]');if(!el)return;var a=el.getAttribute('data-w');
  if(a==='open')open(el.getAttribute('data-b')||'');
  else if(a==='back'){var b=ret||'';var m=b.split(':');
    if(m[0]==='u'&&A.UNITS[m[1]])A.unitView(A.UNITS[m[1]],'lesson');
    else{var L=A.LESSONS.filter(function(l){return l.id==='polaczenia-zeber'})[0];if(L)A.lessonView(L);else A.home()}}});
/* przycisk wstawiany w lekcji i przy pytaniach o ruchy żeber */
window.WYJ_UI={units:{'zebra-osie':1,'mostkowo-zebrowe':1,'mechanizm':1},lesson:'polaczenia-zeber',
  btn:function(b){return '<button class="wybtn" data-w="open" data-b="'+b+'"><span><b>Nie rozumiesz ruchów żeber?</b>Wyjaśnienie prostym językiem, z rysunkami: oś obrotu, rączka pompy i wiadra, trzy typy ruchu.</span>'+A.ICO.ch+'</button>'}};
})();
