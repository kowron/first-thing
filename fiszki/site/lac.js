/* Łacina: wszystkie nazwy łacińskie z rozdziałów Bochenka na to zaliczenie, w kolejności książki.
   Runda 1 – przegląd: oceniasz każdą fiszkę (umiem / nie jestem pewny / nie umiem); „umiem” idzie do banku.
   Runda 2 i dalej – pisanie: wpisujesz po łacinie tylko fiszki z przeglądu oznaczone jako niepewne lub nieznane;
   błędne wracają w następnej rundzie, aż wszystkie wyjdą. Między działami krótka plansza „Teraz: …”.
   Stan: S.lt = {ts, r (runda), q (kolejka rundy), i (pozycja), c: {klucz: {c:'k'|'u'|'n', ok:0|1, n: liczba prób}}} */
(function(){
'use strict';
var A=window.__so5,D=window.LAC;if(!A||!D)return;
var esc=A.esc,app=document.getElementById('app');
var CARDS=[],BYK={};
D.groups.forEach(function(g,gi){g.i.forEach(function(it){var k=it.id||('l:'+it.l.toLowerCase().replace(/[^a-z]+/g,'-'));if(BYK[k])return;
  var c={k:k,p:it.p,l:it.l,a:it.a||[],s:it.s,g:gi,t:g.t,kl:!!it.k};BYK[k]=c;CARDS.push(c)})});
var CH={1:'k',2:'u',3:'n'},CHL={k:'umiem',u:'nie jestem pewny',n:'nie umiem'};
function st(){var S=A.S;if(!S.lt||!S.lt.c)S.lt={ts:0,r:1,q:null,i:0,c:{}};var L=S.lt;
  if(L._inh!==2){L._inh=2;CARDS.forEach(function(c){if(c.k.slice(-2)!=='#2')return;var b=c.k.slice(0,-2);if(!L.c[c.k]&&L.c[b]){L.c[c.k]={c:L.c[b].c,ok:0,n:0};if(L.q&&L.q.indexOf(b)>=0&&L.q.indexOf(c.k)<0)L.q.push(c.k)}})}
  return L}
function save(){st().ts=Date.now();A.save()}
function cs(k){return st().c[k]||null}
function toTriage(){return CARDS.filter(function(c){return !cs(c.k)})}
function toLearn(){return CARDS.filter(function(c){var x=cs(c.k);return x&&x.c!=='k'&&!x.ok})}
function counts(){var r={all:CARDS.length,k:0,u:0,n:0,ok:0,left:0};CARDS.forEach(function(c){var x=cs(c.k);if(!x){r.left++;return}r[x.c]++;if(x.c!=='k'&&x.ok)r.ok++});return r}
/* bieżąca runda: 1 = przegląd, dopóki zostały nieocenione; potem pisanie w rundach */
function round(){var L=st();if(toTriage().length){L.r=1;return 1}if(L.r<2){L.r=2;L.q=null}return L.r}
function queue(){var L=st();if(round()===1)return toTriage().map(function(c){return c.k});
  if(!L.q){L.q=toLearn().map(function(c){return c.k});L.i=0;save()}return L.q}

/* ---------- ekran główny ---------- */
var mode=null,cur=null,last=null,undo=null,shown=false,rs=null;
function bkLine(){return '<div class="lt-seg">'+['k','ok','todo','left'].map(function(x){return '<b class="'+x+'" id="lb-'+x+'"></b>'}).join('')+'</div>'}
function segW(c){var n=c.all||1;return{k:c.k/n,ok:c.ok/n,todo:(c.u+c.n-c.ok)/n,left:c.left/n}}
function home(){A.setView('lac');A.nav('lac');A.setTis('');mode=null;
  var c=counts(),r=round(),q=r===1?toTriage():toLearn(),w=segW(c);
  var h='<div class="g-lead"><div class="eb lt-eb">Nazwy z Bochenka</div><h1>Łacina</h1><p class="mut">Wszystkie '+c.all+' '+A.pl(c.all,'nazwa łacińska','nazwy łacińskie','nazw łacińskich')+' z rozdziałów o kręgosłupie, klatce piersiowej i mięśniach grzbietu, klatki piersiowej i brzucha, w kolejności książki.</p></div>';
  h+='<div><div class="lt-seg">'+['k','ok','todo','left'].map(function(x){return '<b class="'+x+'" style="width:'+(w[x]*100).toFixed(2)+'%"></b>'}).join('')+'</div>'
   +'<div class="legend"><span class="lk">w banku „umiem” '+c.k+'</span><span class="lok">zaliczone pisaniem '+c.ok+'</span><span class="ltd">do napisania '+(c.u+c.n-c.ok)+'</span><span>nieprzejrzane '+c.left+'</span></div></div>';
  if(r===1){h+='<section class="hero lt-hero"><div><div class="eb">Runda 1 · przegląd</div><h2>'+(c.left===c.all?'Przejrzyj wszystkie fiszki':'Dokończ przegląd')+'</h2><p>Przy każdej nazwie zdecyduj: umiem, nie jestem pewny albo nie umiem. To, co umiesz, odkładam do banku i nie będziesz tego pisać. Zostało '+q.length+'.</p></div><button class="btn" data-l="go">'+(c.left===c.all?'Zacznij przegląd':'Dokończ przegląd')+'</button></section>'}
  else if(q.length){var L=st(),rem=L.q&&L.i<L.q.length?L.q.length-L.i:q.length;
    h+='<section class="hero lt-hero"><div><div class="eb">Runda '+L.r+' · pisanie</div><h2>Wpisz nazwy po łacinie</h2><p>'+rem+' '+A.pl(rem,'fiszka','fiszki','fiszek')+' w tej rundzie. Błędne wrócą w następnej, aż wszystkie wyjdą.</p></div><button class="btn" data-l="go">'+(L.i?'Dokończ rundę':'Zacznij rundę '+L.r)+'</button></section>'}
  else h+='<section class="hero lt-hero"><div><div class="eb">Koniec</div><h2>Wszystko zaliczone</h2><p>'+c.ok+' '+A.pl(c.ok,'nazwę','nazwy','nazw')+' napisałeś poprawnie, '+c.k+' '+A.pl(c.k,'jest','są','jest')+' w banku „umiem”. Możesz przejrzeć bank albo zacząć od nowa.</p></div></section>';
  h+='<details class="lt-det"><summary>Działy ('+D.groups.length+') i postęp w każdym</summary><div class="lt-topics">'+D.groups.map(function(g,gi){var n=0,d=0;CARDS.forEach(function(c){if(c.g!==gi)return;n++;var x=cs(c.k);if(x&&(x.c==='k'||x.ok))d++});
      return '<div class="lt-tp"><span>'+esc(g.t)+'</span><span class="lt-tn">'+d+'/'+n+'</span></div>'}).join('')+'</div></details>';
  h+='<div class="lt-links"><button class="btn ghost sml" data-l="bank">Bank „umiem” ('+c.k+')</button><button class="btn ghost sml" data-l="reset">'+(rs?'Na pewno od nowa?':'Zacznij od nowa')+'</button></div>';
  A.page(h,!!rs)}
function card(){var c=counts(),r=round(),n=r===1?c.left:(c.u+c.n-c.ok);
  if(!c.all)return '';
  return '<section class="hero lt-hero plain"><div><div class="eb">Łacina</div><h2>'+(r===1?'Przegląd nazw łacińskich':(n?'Runda '+st().r+': pisanie':'Łacina zaliczona'))+'</h2><p>'+(r===1?'Zostało '+n+' z '+c.all+' do przejrzenia. Co umiesz, odkładasz do banku.':(n?n+' '+A.pl(n,'nazwa','nazwy','nazw')+' do wpisania.':'Wszystkie nazwy zaliczone.'))+'</p></div><button class="btn ghost" data-a="lac">'+(n?'Ćwicz łacinę':'Zobacz')+'</button></section>'}

/* ---------- sesja ---------- */
function topBar(i,n){document.getElementById('top').innerHTML='<header class="bar sbar"><div class="wrap"><button class="x" data-l="exit" aria-label="Zakończ">'+A.ICO.x+'</button><div class="prog"><b style="width:'+(n?i/n*100:0)+'%"></b></div><span class="cnt">'+Math.min(i+1,n)+' z '+n+'</span></div></header>'}
function go(){mode=round()===1?'tri':'typ';last=null;next(true)}
function next(first){var r=round(),q;
  if(mode==='tri'){q=toTriage();if(!q.length){roundEnd(1);return}cur=q[0];var tot=CARDS.length,done=tot-q.length;topBar(done,tot)}
  else{var L=st();q=queue();if(!q.length){A.setTis('');home();return}if(L.i>=q.length){roundEnd(L.r);return}cur=BYK[q[L.i]];if(!cur){L.i++;next();return}topBar(L.i,q.length)}
  shown=false;
  if(!last||last.g!==cur.g)interlude(cur.t,first);
  last=cur;mode==='tri'?triView():typView()}
/* plansza działu: wjeżdża, po chwili znika (dotknięcie pomija) */
function interlude(t,first){var o=document.createElement('div');o.className='lt-intro';o.innerHTML='<div><span>'+(first?'Zaczynamy':'Teraz')+'</span><b>'+esc(t)+'</b></div>';
  o.addEventListener('click',function(){o.remove()});document.body.appendChild(o);setTimeout(function(){o.classList.add('out')},1150);setTimeout(function(){o.remove()},1500)}
function triView(){A.setView('lac-tri');A.setTis('');var c=cur;
  var h='<div class="crumb">Runda 1 · przegląd · '+esc(c.t)+'</div>'
   +'<div class="fc lt-fc" data-l="show" role="button" tabindex="0" aria-label="Pokaż łacinę"><div class="lb">Po łacinie to…'+(c.kl?' · pojęcie kliniczne':'')+'<span>'+esc(c.s?'s. '+c.s:'')+'</span></div><div class="lt-pl">'+esc(c.p)+'</div>'
   +'<div class="lt-la" id="lla">'+(shown?la(c):'<span class="lt-hide">Dotknij, żeby zobaczyć</span>')+'</div></div>'
   +'<p class="sm mut">Jeśli jesteś pewny odpowiedzi, nie musisz jej odsłaniać. Klawisze: spacja odsłania, 1 umiem, 2 nie jestem pewny, 3 nie umiem.</p>';
  A.page(h+A.dock('<button class="btn lt-n" data-l="t" data-c="n">Nie umiem</button><button class="btn lt-u" data-l="t" data-c="u">Nie jestem pewny</button><button class="btn" data-l="t" data-c="k">Umiem</button>',undo?'<button class="link" data-l="undo">Cofnij: '+esc(undo.p)+' → '+CHL[undo.c]+'</button>':''),true)}
function la(c){return '<i>'+esc(c.l)+'</i>'+(c.a&&c.a.length?'<div class="lt-alt">także: '+c.a.map(function(x){return '<i>'+esc(x)+'</i>'}).join(', ')+'</div>':'')}
function tri(ch){var c=cur;if(!c)return;st().c[c.k]={c:ch,ok:0,n:0};undo={k:c.k,p:c.p,c:ch};save();next()}
function typView(){A.setView('lac-typ');var c=cur,L=st();
  A.page('<div class="crumb">Runda '+L.r+' · pisanie · '+esc(c.t)+'</div><div><div class="lbl" style="margin-bottom:6px">Jak to się nazywa po łacinie?</div><div class="wq">'+esc(c.p)+'</div>'+(c.kl?'<div class="sm mut" style="margin-top:4px">pojęcie kliniczne</div>':'')+'</div>'
   +'<form id="lf" autocomplete="off"><input type="text" id="lin" autocapitalize="off" autocorrect="off" spellcheck="false" enterkeyhint="done" placeholder="nazwa łacińska" aria-label="Nazwa łacińska"></form><div id="lfb"></div>'
   +A.dock('<button class="btn" id="lb" data-l="check">Sprawdź</button>','<button class="link" id="ldk" data-l="dk">Nie wiem, pokaż</button>'));
  var el=document.getElementById('lin');try{el.focus({preventScroll:true})}catch(e){}}
function check(dk){var c=cur,el=document.getElementById('lin');if(!c||!el)return;var L=st(),x=L.c[c.k]||{c:'u',ok:0,n:0};
  if(el.readOnly){clearTimeout(autoT);L.i++;save();next();return}
  var v=A.nlat(el.value);if(!dk&&!v){el.focus();return}
  var ok=!dk&&[c.l].concat(c.a||[]).some(function(t){return A.nlat(t)===v});
  x.n=(x.n||0)+1;if(ok)x.ok=1;L.c[c.k]=x;save();el.readOnly=true;el.classList.add(ok?'ok':'bad');fb(ok);if(ok)auto()}
var autoT=null;function auto(){var c0=cur;clearTimeout(autoT);autoT=setTimeout(function(){if(cur!==c0||A.view!=='lac-typ')return;st().i++;save();next()},650)}
function fb(ok){var c=cur;document.getElementById('lfb').innerHTML='<div class="fb '+(ok?'ok':'no')+'">'+(ok?'Dobrze: ':'<b>Poprawnie:</b> ')+la(c)+' <span class="pg">'+esc(c.s?'s. '+c.s:'')+'</span>'
   +(ok||!(document.getElementById('lin')||{}).value?'':'<div><button class="link" type="button" data-l="okme" style="padding-left:0">Napisałem dobrze, zalicz</button></div>')+'</div>';
  var b=document.getElementById('lb'),d=document.getElementById('ldk');b.textContent=ok?'Dalej':'Dalej, wróci w następnej rundzie';if(d)d.hidden=true;try{b.focus({preventScroll:true})}catch(e){}}
function roundEnd(r){A.setView('lac-end');A.nav('lac');var c=counts(),L=st(),left=toLearn().length;
  var h='<div><div class="eb">Runda '+r+(r===1?' · przegląd':' · pisanie')+'</div><h1>Runda skończona</h1></div>';
  if(r===1)h+='<p class="mut">W banku „umiem”: <b>'+c.k+'</b>. Do napisania: <b>'+(c.u+c.n)+'</b> (nie jestem pewny '+c.u+', nie umiem '+c.n+'). Od teraz piszesz tylko te.</p>';
  else h+='<p class="mut">'+(left?'Wraca '+left+' '+A.pl(left,'fiszka','fiszki','fiszek')+'. Następna runda tylko z nimi.':'Wszystkie fiszki z tej rundy wyszły. Łacina zaliczona.')+'</p>';
  if(r>1&&L.i>=(L.q||[]).length){L.q=null;L.i=0;if(left)L.r=r+1;save()}
  if(r===1){L.r=2;L.q=null;L.i=0;save()}
  A.page(h+A.dock(left?'<button class="btn ghost" data-l="home">Na teraz koniec</button><button class="btn" data-l="go">Runda '+st().r+'</button>':'<button class="btn" data-l="home">Wróć</button>'))}
function bank(){A.setView('lac-bank');A.nav('lac');var ks=CARDS.filter(function(c){var x=cs(c.k);return x&&x.c==='k'});
  var h='<div><button class="back" data-l="home">'+A.ICO.back+' Łacina</button></div><div><h1>Bank „umiem”</h1><p class="mut" style="margin-top:8px">Te nazwy oznaczyłeś w przeglądzie jako pewne. Jeśli coś jednak warto poćwiczyć, przenieś to do pisania.</p></div>';
  if(!ks.length)h+='<p class="empty">Bank jest pusty. Trafią tu nazwy, które w przeglądzie oznaczysz jako „umiem”.</p>';
  else{var g=-1;h+='<div class="lt-bank">'+ks.map(function(c){var hd=c.g!==g?'<div class="lt-bh">'+esc(c.t)+'</div>':'';g=c.g;
    return hd+'<div class="lt-bi"><div><b>'+esc(c.p)+'</b> <i>'+esc(c.l)+'</i></div><button class="link" data-l="unbank" data-k="'+esc(c.k)+'">Do pisania</button></div>'}).join('')+'</div>'}
  A.page(h,true)}

/* ---------- zdarzenia ---------- */
document.addEventListener('click',function(e){var el=e.target.closest('[data-l]');if(!el)return;var a=el.getAttribute('data-l');
  switch(a){
  case 'home':rs=null;home();break;
  case 'go':go();break;
  case 'exit':cur=null;home();break;
  case 'show':if(!shown){shown=true;var x=document.getElementById('lla');if(x)x.innerHTML=la(cur)}break;
  case 't':tri(el.getAttribute('data-c'));break;
  case 'undo':if(undo){delete st().c[undo.k];save();undo=null;last=null;next()}break;
  case 'check':check(false);break;
  case 'dk':check(true);break;
  case 'okme':var L=st(),x=L.c[cur.k];if(x){x.ok=1;save()}var i=document.getElementById('lin');if(i){i.classList.remove('bad');i.classList.add('ok')}fb(true);auto();break;
  case 'bank':bank();break;
  case 'unbank':var k=el.getAttribute('data-k');st().c[k]={c:'u',ok:0,n:0};if(round()>1){var Q=st();if(Q.q&&Q.q.indexOf(k)<0)Q.q.push(k)}save();bank();break;
  case 'reset':if(!rs){rs=Date.now();home();setTimeout(function(){if(rs&&Date.now()-rs>=4800){rs=null;if(A.view==='lac')home()}},5000)}else{rs=null;A.S.lt=null;save();A.toast('Łacina od nowa');home()}break;
  }});
document.addEventListener('submit',function(e){if(e.target.id!=='lf')return;e.preventDefault();check(false)});
document.addEventListener('keydown',function(e){if(e.target&&e.target.tagName==='INPUT')return;
  if(A.view==='lac-tri'){if(e.key===' '){e.preventDefault();var s=document.querySelector('.lt-fc');if(s)s.click()}else if(CH[e.key]){e.preventDefault();tri(CH[e.key])}}});
window.LAC_UI={home:home,card:card,_cards:CARDS};
if(A.view==='home')A.home();   /* strona główna narysowała się przed wczytaniem łaciny */
})();
