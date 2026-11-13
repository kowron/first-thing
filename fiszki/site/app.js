/* Szkielet osiowy: pytania prowadzącego, odpowiedzi według Bochenka.
   Metoda: przeczytaj -> powiedz z pamięci -> porównaj -> braki do skutku -> jedna powtórka następnego dnia. */
(function(){
'use strict';
var B=window.BANK,app=document.getElementById('app'),topEl=document.getElementById('top');
var ICO={
 x:'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>',
 ck:'<svg class="ck" viewBox="0 0 24 24" fill="none" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M6 12.5l4 4 8-9"/></svg>',
 no:'<svg class="xx" viewBox="0 0 24 24" fill="none" stroke-width="3" stroke-linecap="round"><path d="M7 7l10 10M17 7L7 17"/></svg>',
 back:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg>',
 ch:'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5l7 7-7 7"/></svg>',
 book:'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 6.5C10 5 7 4.5 3.5 5v13c3.5-.5 6.5 0 8.5 1.5 2-1.5 5-2 8.5-1.5V5C17 4.5 14 5 12 6.5z"/><path d="M12 6.5v13"/></svg>',
 mic:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0014 0M12 18v3"/></svg>'};

/* ---------- tekst ---------- */
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;')}
function strip(h){return String(h).replace(/<[^>]+>/g,'').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&quot;/g,'"').replace(/&amp;/g,'&')}
function pl(n,a,b,c){var d=n%10,h=n%100;return n===1?a:(d>=2&&d<=4&&(h<12||h>14)?b:c)}
function fold(s){return String(s).toLowerCase().replace(/ł/g,'l').normalize('NFD').replace(/[̀-ͯ]/g,'')}
/* Łacina: literówek nie przepuszczam. Nie liczą się wielkość liter, kropki i przedrostki m., mm., lig. */
var DROPW={m:1,mm:1,musculus:1,musculi:1,lig:1,ligg:1,ligamentum:1,ligamenta:1};
function nlat(s){s=fold(s).replace(/[^a-z\s]/g,' ').replace(/\s+/g,' ').trim().replace(/\boe/g,'e').replace(/annul/g,'anul');
  return s.split(' ').filter(function(w){return w&&!DROPW[w]}).join(' ')}

/* ---------- dane ---------- */
var LESSONS=[],UNITS={},ALLU=[];
B.blocks.forEach(function(b,bi){b.lessons.forEach(function(l){l.bi=bi;LESSONS.push(l);
  l.units.forEach(function(u){u.L=l;u.key='u:'+u.id;UNITS[u.id]=u;ALLU.push(u);u.heads=u.pts.filter(function(p){return p.g}).map(function(p){return p.g});
    u.hay=fold(u.q+' '+u.pts.map(function(p){return strip(p.a)}).join(' ')+' '+u.fu.map(function(f){return f.q+' '+strip(f.a)}).join(' '))});
  l.words.forEach(function(w){w.L=l;w.key='w:'+w.la.toLowerCase().replace(/[^a-z]+/g,'-')})})});
var FIG={pochewka:'<figure class="sch"><svg viewBox="0 0 340 196" role="img" aria-label="Schemat pochewki mięśnia prostego brzucha powyżej i poniżej kresy łukowatej">'
 +'<style>.t{font:600 11.5px var(--sans);fill:#566076}.h{font:650 12.5px var(--sans);fill:#151a27}.m{fill:#ffd9d1;stroke:#e2503a;stroke-width:1.2}.ze{stroke:#c27c00}.we{stroke:#2b7be4}.po{stroke:#0a8767}.l{fill:none;stroke-width:3;stroke-linecap:round}.f{fill:none;stroke:#96a0b5;stroke-width:1.6;stroke-dasharray:3 3}</style>'
 +'<text class="h" x="6" y="14">Powyżej kresy łukowatej</text>'
 +'<ellipse class="m" cx="118" cy="52" rx="62" ry="15"/><text class="t" x="118" y="56" text-anchor="middle">m. prosty</text>'
 +'<path class="l ze" d="M330 26 H190 C176 26 176 28 150 28 H40"/>'
 +'<path class="l we" d="M330 52 H214 C200 52 196 33 180 33 H40"/><path class="l we" d="M214 52 C200 52 196 71 180 71 H40"/>'
 +'<path class="l po" d="M330 78 H196 C186 78 186 76 176 76 H40"/>'
 +'<path class="f" d="M330 86 H40"/>'
 +'<text class="h" x="6" y="114">Poniżej kresy łukowatej</text>'
 +'<ellipse class="m" cx="118" cy="158" rx="62" ry="15"/><text class="t" x="118" y="162" text-anchor="middle">m. prosty</text>'
 +'<path class="l ze" d="M330 128 H190 C176 128 176 130 150 130 H40"/>'
 +'<path class="l we" d="M330 152 H214 C200 152 196 135 180 135 H40"/>'
 +'<path class="l po" d="M330 176 H222 C204 176 200 140 182 140 H40"/>'
 +'<path class="f" d="M330 184 H200 C190 184 190 177 180 177 H40"/>'
 +'</svg><figcaption><span class="lg"><b style="background:#c27c00"></b>rozcięgno m. skośnego zewnętrznego</span><span class="lg"><b style="background:#2b7be4"></b>m. skośnego wewnętrznego</span><span class="lg"><b style="background:#0a8767"></b>m. poprzecznego</span><span class="lg"><b class="dash"></b>powięź poprzeczna</span><span class="cap">Przekrój poprzeczny, linia pośrodkowa po lewej. Schemat własny według opisu Bochenka.</span></figcaption></figure>'};
if(UNITS.pochewka)UNITS.pochewka.fig='pochewka';

/* ---------- stan ---------- */
/* Każde pytanie i każde słówko ma ten sam zapis: n = ile razy było robione „na czysto”, t = kiedy ostatnio,
   d = 1 gdy utrwalone, m = numery punktów, których zabrakło, f = numery dopytań, które nie wyszły. */
var LS='so5_v1',S={v:5,ts:0,rs:0,ai:1,u:{}};
try{localStorage.removeItem('so4d_v1')}catch(e){}
try{var raw=localStorage.getItem(LS);if(raw){var o0=JSON.parse(raw);if(o0&&o0.v===5&&o0.u)S=Object.assign(S,o0)}}catch(e){}
var dbRef=null,dbTimer=null,dbBusy=false,dbDirty=false,dbState='w tej przeglądarce';
function persist(){try{localStorage.setItem(LS,JSON.stringify(S))}catch(e){}}
function save(){S.ts=Date.now();persist();if(dbRef){dbDirty=true;clearTimeout(dbTimer);dbTimer=setTimeout(pushDb,4000)}}
function pushDb(){if(!dbRef||dbBusy||!dbDirty)return;dbBusy=true;dbDirty=false;
  dbRef.set({v:5,ts:S.ts,json:JSON.stringify(S)}).then(function(){dbBusy=false;if(dbDirty)dbTimer=setTimeout(pushDb,4000)},
    function(e){dbBusy=false;if(e&&(e.code==='invalid_argument'||e.code==='revoked'||e.code==='not_granted')){dbRef=null;dbState='w tej przeglądarce'}})}
function setU(k,v){v.t=Date.now();S.u[k]=v;save()}
function mergeRemote(R){if(!R||R.v!==5||!R.u)return;var ch=false;
  if((R.rs||0)>(S.rs||0)){S.rs=R.rs;Object.keys(S.u).forEach(function(k){if((S.u[k].t||0)<S.rs)delete S.u[k]});ch=true}
  Object.keys(R.u).forEach(function(k){var r=R.u[k];if((r.t||0)<(S.rs||0))return;if(!S.u[k]||(r.t||0)>(S.u[k].t||0)){S.u[k]=r;ch=true}});
  if(R.g){S.g=S.g||{};Object.keys(R.g).forEach(function(k){var r=R.g[k];if((r.at||0)<(S.rs||0))return;if(!S.g[k]||(r.p||0)>(S.g[k].p||0)){S.g[k]=r;ch=true}})}
  if(R.gm&&!S.gm){S.gm=R.gm;ch=true}
  if(ch)persist()}

/* ---------- postęp ---------- */
function dayKey(t){var d=new Date(t-4*3600e3);return d.getFullYear()*500+d.getMonth()*32+d.getDate()}
function learned(k){var u=S.u[k];return !!(u&&u.n)}
function done(k){var u=S.u[k];return !!(u&&u.d)}
function pending(k){var u=S.u[k];return !!(u&&u.n&&!u.d)}
function due(k){var u=S.u[k];return !!(u&&u.n&&!u.d&&dayKey(u.t)!==dayKey(Date.now()))}
function uo(u){return{k:'u',key:u.key,x:u,L:u.L}}
function objs(L){return L.units.map(uo).concat(L.words.map(function(w){return{k:'w',key:w.key,w:w,L:L}}))}
function learnQ(L){return objs(L).filter(function(o){return !learned(o.key)})}
function reviewQ(early,L){var a=[];(L?[L]:LESSONS).forEach(function(l){objs(l).forEach(function(o){if(early?pending(o.key):due(o.key))a.push(o)})});return a}
function missN(o){var u=S.u[o.key];return o.k==='u'&&u&&u.n>=2?(u.m||[]).length+(u.f||[]).length:0}
function cost(o,rev){if(o.k==='w')return rev?0.12:0.15;var om=rev?missN(o):0;if(om)return om*0.25;var n=o.x.pts.length;return rev?0.6+0.2*n:1.2+0.35*n+0.2*o.x.fu.length}
function mins(a,rev){return Math.max(1,Math.round(a.reduce(function(s,o){return s+cost(o,rev)},0)))}
function lstat(L){var a=objs(L),s={n:a.length,l:0,d:0,due:0,pend:0};a.forEach(function(o){if(learned(o.key))s.l++;if(done(o.key))s.d++;if(due(o.key))s.due++;if(pending(o.key))s.pend++});return s}
function nextLesson(){for(var i=0;i<LESSONS.length;i++)if(learnQ(LESSONS[i]).length)return LESSONS[i];return null}
function kinds(a){var u=0,w=0;a.forEach(function(o){if(o.k==='u')u++;else w++});var p=[];
  if(u)p.push(u+' '+pl(u,'pytanie','pytania','pytań'));if(w)p.push(w+' '+pl(w,'nazwa łacińska','nazwy łacińskie','nazw łacińskich'));return p.join(' i ')}

/* ---------- widok ---------- */
var view='',curL=null,T=null,cap={sample:null,dict:null},capTry=0,dictT=null,dictBase='',dictOn=false,noteFrom='lesson',resetArm=0;
var LOGO='<svg class="logo" width="20" height="22" viewBox="0 0 20 22" aria-hidden="true"><rect x="5.5" y="1" width="9" height="5" rx="2.2" fill="var(--accent)"/><rect x="4" y="8.5" width="12" height="5" rx="2.2" fill="var(--accent)" opacity=".72"/><rect x="2.5" y="16" width="15" height="5" rx="2.2" fill="var(--accent)" opacity=".45"/></svg>';
function setTis(t){document.body.className=t?'t-'+t:''}
function setView(v){view=v;window.scrollTo(0,0);if(cap.dict&&dictOn)cap.dict.stop().catch(function(){});dictT=null}
function nav(on){topEl.innerHTML='<header class="bar"><div class="wrap"><button class="brand" data-a="home">'+LOGO+'<span>Szkielet osiowy</span></button><nav><button data-a="game"'+(on==='game'?' class="on"':'')+'>Na czas</button><button data-a="notes"'+(on==='notes'?' class="on"':'')+'>Notatki</button><button data-a="set"'+(on==='set'?' class="on"':'')+'>Więcej</button></nav></div></header>'}
function bar(){var i=T.i,n=T.q.length;topEl.innerHTML='<header class="bar sbar"><div class="wrap"><button class="x" data-a="exit" aria-label="Zakończ">'+ICO.x+'</button><div class="prog"><b style="width:'+(n?i/n*100:0)+'%"></b></div><span class="cnt">'+Math.min(i+1,n)+' z '+n+'</span></div></header>'}
function page(h,still){app.innerHTML='<div class="wrap stack'+(still?' still':'')+'">'+h+'</div>'}
function dock(primary,links){return '<div class="dock"><div class="wrap">'+(links?'<div class="links">'+links+'</div>':'')+'<div class="row">'+primary+'</div></div></div>'}
function toast(t){[].forEach.call(document.querySelectorAll('.toast'),function(x){x.remove()});var e=document.createElement('div');e.className='toast';e.textContent=t;document.body.appendChild(e);setTimeout(function(){e.remove()},2000)}
function ring(l,d){var c=2*Math.PI*15,full=d>=1,pc=Math.round(d*100);
  return '<svg class="ring'+(full?' full':'')+'" viewBox="0 0 38 38" aria-hidden="true"><circle class="bg" cx="19" cy="19" r="15"/>'
   +(l>d?'<circle class="fg2" cx="19" cy="19" r="15" transform="rotate(-90 19 19)" stroke-dasharray="'+c.toFixed(1)+'" stroke-dashoffset="'+(c*(1-l)).toFixed(1)+'"/>':'')
   +(d>0?'<circle class="fg" cx="19" cy="19" r="15" transform="rotate(-90 19 19)" stroke-dasharray="'+c.toFixed(1)+'" stroke-dashoffset="'+(c*(1-d)).toFixed(1)+'"/>':'')
   +(full?'<text x="19" y="24" text-anchor="middle">✓</text>':(pc?'<text x="19" y="22.5" text-anchor="middle">'+pc+'</text>':''))+'</svg>'}
function bigRing(p){var c=2*Math.PI*52;return '<svg viewBox="0 0 120 120" class="bring" aria-hidden="true"><circle class="bg" cx="60" cy="60" r="52"/><circle class="fg" cx="60" cy="60" r="52" transform="rotate(-90 60 60)" stroke-dasharray="'+c.toFixed(1)+'" stroke-dashoffset="'+(c*(1-p/100)).toFixed(1)+'" style="--c:'+c.toFixed(1)+'"/><text x="60" y="69" text-anchor="middle">'+p+'%</text></svg>'}
function priChip(u){return u.pri===3?'<span class="pri p3">bardzo częste</span>':(u.pri===1?'<span class="pri p1">drugi termin</span>':'')}
function answerHtml(x){var h='<div class="answer">',open=false;
  x.pts.forEach(function(p,i){if(p.g||i===0){if(open)h+='</ul>';if(p.g)h+='<div class="g">'+esc(p.g)+'</div>';h+='<ul class="facts">';open=true}h+='<li>'+p.a+pgTag(p.s)+'</li>'});
  return h+(open?'</ul>':'')+'</div>'}
function xnote(x){return x.x?'<div class="xnote"><b>Uwaga do źródeł</b>'+x.x+'</div>':''}
function srcLine(x){return '<p class="src">Bochenek, Anatomia człowieka, t. I, '+esc(x.src)+'</p>'}
/* strony Bochenka: przy pytaniu (u.src), przy każdej fiszce i dopytaniu (p.s, f.s) i przy słówku (w.s) */
function pgs(s){var a=[];String(s||'').replace(/(\d{3})(?:\s*[–-]\s*(\d{3}))?/g,function(_,x,y){x=+x;y=y?+y:x;for(var i=x;i<=y;i++)if(a.indexOf(i)<0)a.push(i)});return a.sort(function(p,q){return p-q})}
function pgfmt(a){var r=[],i=0;while(i<a.length){var j=i;while(j+1<a.length&&a[j+1]===a[j]+1)j++;r.push(j>i?a[i]+'–'+a[j]:''+a[i]);i=j+1}return r.length?'s. '+r.join(', '):''}
function pgTag(s){return s?' <span class="pg">'+esc(s)+'</span>':''}
function bkBox(t,s){return '<div class="bk">'+ICO.book+'<div><b>'+t+'</b>Anatomia człowieka, t. I: <span class="pp">'+String(s).split(/,\s*/).map(function(x){return '<span class="nw">'+esc(x)+'</span>'}).join(', ')+'</span></div></div>'}
function ustatus(u){var s=S.u[u.key];if(!s||!s.n)return['','nowe'];if(s.d)return['d','utrwalone'];return['l',due(u.key)?'do powtórki dziś':'sprawdzian jutro']}

/* ---------- strona główna ---------- */
function home(){setView('home');nav('home');setTis('');curL=null;T=null;
  var n=ALLU.length,l=0,d=0;ALLU.forEach(function(u){if(learned(u.key))l++;if(done(u.key))d++});
  var dq=reviewQ(false),pq=reviewQ(true),nl=nextLesson();
  var h='<div class="lead"><h1>Zaliczenie nr 2</h1><p>'+n+' '+pl(n,'pytanie','pytania','pytań')+' prowadzącego. Odpowiedzi według Bochenka, od najczęściej zadawanych.</p></div>';
  h+='<div><div class="spine" role="img" aria-label="Postęp: utrwalone '+d+', po pierwszej nauce '+(l-d)+', nowe '+(n-l)+'">'+ALLU.map(function(u,i){var r=n>1?i/(n-1):0;
      return '<i class="'+(done(u.key)?'d':(learned(u.key)?'l':''))+'" style="height:'+(11+r*15).toFixed(1)+'px;flex-grow:'+(.7+r*.8).toFixed(2)+'" title="'+esc(u.q)+'"></i>'}).join('')+'</div><div class="legend"><span class="d">utrwalone '+d+'</span><span class="l">po pierwszej nauce '+(l-d)+'</span><span>nowe '+(n-l)+'</span></div><p class="spcap">Każdy krąg to jedno pytanie, od szyjnych po lędźwiowe.</p></div>';
  if(dq.length)h+='<section class="hero rev"><div><div class="eb">Powtórka</div><h2>Sprawdź to, czego uczyłeś się wcześniej</h2><p>'+kinds(dq)+', ok. '+mins(dq,true)+' min. Co powiesz dobrze, jest utrwalone i więcej nie wraca.</p></div><button class="btn" data-a="review">Zacznij powtórkę</button></section>';
  if(nl){var lq=learnQ(nl),st=lstat(nl);
    h+='<section class="hero t-'+nl.tis+(dq.length?' plain':'')+'"><div><div class="eb">'+(st.l?'Lekcja w toku':'Następna lekcja')+'</div><h2>'+esc(nl.t)+'</h2><p>'+esc(nl.d)+'</p></div><button class="btn'+(dq.length?' ghost':'')+'" data-a="learn" data-l="'+nl.id+'">'+(st.l?'Dokończ':'Zacznij')+', ok. '+mins(lq)+' min</button></section>'}
  else if(!dq.length)h+='<section class="hero rev"><div><div class="eb">Cały materiał przerobiony</div><h2>'+(pq.length?'Jutro ostatni sprawdzian':'Wszystko utrwalone')+'</h2><p>'+(pq.length?'Zostało '+kinds(pq)+' do sprawdzenia po przerwie.':'Możesz jeszcze zrobić próbny egzamin.')+'</p></div></section>';
  if(!dq.length&&pq.length)h+='<p class="sm mut">Na jutro czeka '+kinds(pq)+'. <button class="link" data-a="early" style="padding:0">Poćwicz już dziś</button></p>';
  var gm={z:0,s:0,b:0};Object.keys(S.g||{}).forEach(function(k){var md=S.g[k].md;if(md)gm[md]++});var gmt=gm.z+gm.s+gm.b;
  h+='<section class="hero game"><div><div class="eb">Na czas</div><h2>Wymienianka mięśni</h2><p>Mów nazwy na głos: po polsku, po łacinie albo na zmianę. 100 punktów za każdą nazwę i premia za szybki komplet.'+(gmt?' Twoje medale: '+[gm.z?gm.z+' '+pl(gm.z,'złoty','złote','złotych'):'',gm.s?gm.s+' '+pl(gm.s,'srebrny','srebrne','srebrnych'):'',gm.b?gm.b+' '+pl(gm.b,'brązowy','brązowe','brązowych'):''].filter(Boolean).join(', ')+'.':'')+'</p></div><button class="btn game-btn" data-a="game">Zagraj</button></section>';
  h+='<section class="hero plain"><div><h2>Próbny egzamin</h2><p>Sześć losowych pytań, częste trafiają się częściej. Do każdego jedno dopytanie.</p></div><button class="btn ghost" data-a="exam">Losuj pytania</button></section>';
  B.blocks.forEach(function(b){h+='<div><div class="bt">'+esc(b.t)+'</div><div class="list">'+b.lessons.map(function(L){var s=lstat(L),q=L.units.length;
    var sub=q+' '+pl(q,'pytanie','pytania','pytań')+(s.due?', '+s.due+' do powtórki':(s.l&&s.l<s.n?', w toku':(s.d===s.n?', utrwalona':(s.l===s.n?', sprawdzian jutro':''))));
    return '<button class="lrow t-'+L.tis+'" data-a="lesson" data-l="'+L.id+'"><span class="tab"></span><span><span class="t">'+esc(L.t)+'</span><div class="d">'+sub+'</div></span>'+ring(s.l/s.n,s.d/s.n)+'</button>'}).join('')+'</div></div>'});
  h+='<p class="sm mut">Postęp zapisuje się '+dbState+'.</p>';page(h)}

/* ---------- lekcja ---------- */
function urow(u,from){var s=ustatus(u);return '<button class="urow" data-a="unit" data-u="'+u.id+'" data-f="'+from+'"><span class="dot '+s[0]+'"></span><span><span class="t">'+esc(u.q)+'</span><div class="d">'+s[1]+(u.pri===3?', bardzo częste':(u.pri===1?', drugi termin':''))+(u.src?' · '+esc(u.src):'')+'</div></span><span class="ch">'+ICO.ch+'</span></button>'}
function lessonView(L){setView('lesson');nav('home');setTis(L.tis);curL=L;T=null;
  var s=lstat(L),lq=learnQ(L),dq=reviewQ(false,L),pq=reviewQ(true,L),wl=0,wd=0;L.words.forEach(function(w){if(learned(w.key))wl++;if(done(w.key))wd++});
  var h='<div><button class="back" data-a="home">'+ICO.back+' Wszystkie lekcje</button></div><div><h1>'+esc(L.t)+'</h1><p class="mut" style="margin-top:8px">'+esc(L.d)+'</p></div>';
  var lp=pgfmt(pgs(L.units.map(function(u){return u.src}).join(';')));if(lp)h+=bkBox('Przed lekcją przeczytaj w Bochenku',lp);
  h+='<div><div class="lbl">Pytania prowadzącego</div><div class="list">'+L.units.map(function(u){return urow(u,'lesson')}).join('')+'</div></div>';
  if(L.words.length)h+='<p class="sm mut">Na końcu lekcji wpisujesz '+L.words.length+' '+pl(L.words.length,'nazwę łacińską','nazwy łacińskie','nazw łacińskich')+' z tych odpowiedzi'+(wl?' (utrwalone '+wd+' z '+L.words.length+')':'')+'.</p>';
  var p,links='';
  if(lq.length)p='<button class="btn" data-a="learn" data-l="'+L.id+'">'+(s.l?'Dokończ lekcję':'Zacznij lekcję')+', ok. '+mins(lq)+' min</button>';
  else if(dq.length)p='<button class="btn" data-a="review" data-l="'+L.id+'">Powtórz, ok. '+mins(dq,true)+' min</button>';
  else if(pq.length){p='<button class="btn ghost" data-a="early" data-l="'+L.id+'">Poćwicz już dziś</button>';links='<span class="sm mut" style="padding:8px 0">Sprawdzian utrwalenia będzie jutro.</span>'}
  else p='<button class="btn ghost" data-a="again" data-l="'+L.id+'">Lekcja utrwalona. Przećwicz jeszcze raz</button>';
  page(h+dock(p,links))}
function unitView(u,from){setView('unit');nav(from==='notes'?'notes':'home');setTis(u.L.tis);T=null;noteFrom=from;curL=u.L;
  var h='<div><button class="back" data-a="'+(from==='notes'?'notes':'lesson')+'" data-l="'+u.L.id+'">'+ICO.back+' '+(from==='notes'?'Notatki':esc(u.L.t))+'</button></div>';
  var pc=priChip(u);if(pc)h+='<div class="chips">'+pc+'</div>';
  h+='<h2 class="ask">'+esc(u.q)+'</h2>'+bkBox('Przed nauką przeczytaj w Bochenku',u.src)+(u.fig?FIG[u.fig]:'')+answerHtml(u);
  if(u.fu.length)h+='<div><div class="lbl" style="margin-bottom:8px">O to prowadzący może dopytać</div><div class="fus">'+u.fu.map(function(f){return '<details><summary>'+esc(f.q)+'</summary><p>'+f.a+pgTag(f.s)+'</p></details>'}).join('')+'</div></div>';
  h+=xnote(u);
  page(h+dock('<button class="btn" data-a="one" data-u="'+u.id+'">Przećwicz to pytanie</button>'))}

/* ---------- sesja ---------- */
function startSession(q,o){if(!q.length){if(o.L)lessonView(o.L);else home();return}
  T={q:q.map(function(x){return{o:x,r:1}}),i:0,o:o,ok:0,n:0,back:0,wait:0,log:[]};step()}
function step(){if(!T)return;if(T.i>=T.q.length){finish();return}var t=T.q[T.i];T.t=t;setTis(t.o.L.tis);if(t.o.k==='w')wordView(t);else unitStart(t)}
function nextTask(){T.i++;step()}
function leave(o){var L=o&&o.L;if(o&&o.from==='notes')notes();else if(L)lessonView(L);else home()}
function exit(){var o=T&&T.o;T=null;leave(o)}
function crumb(extra){var t=T.t;return '<div class="crumb">'+esc(T.o.title)+(t.o.k==='u'&&T.o.mode!=='learn'?', '+esc(t.o.L.t):'')+(extra?', '+extra:'')+'</div>'}
/* Wynik „na czysto” zapisuje się raz na zadanie. Pierwszego dnia nic nie jest jeszcze utrwalone:
   utrwala dopiero dobra odpowiedź po przerwie (innego dnia). Błąd zawsze cofa do powtórki. */
function record(t,ok,ex){if(t.r!==1)return;T.n++;if(ok)T.ok++;var k=t.o.key,u=S.u[k]||{n:0},mode=T.o.mode,v;
  var same=!!u.n&&dayKey(u.t)===dayKey(Date.now());
  if(!u.n){if(mode==='exam')return;v={n:1,d:0}}
  else if(ok){if(mode==='exam')return;v={n:u.n+1,d:(same&&!u.d)?0:1};if(!v.d)T.wait++}
  else{v={n:u.n+1,d:0};T.back++}
  if(ex){v.m=ex.m;v.f=(mode==='exam'&&u.f)?u.f.concat(ex.f.filter(function(i){return u.f.indexOf(i)<0})):ex.f}
  setU(k,v)}

/* pytanie: przeczytaj -> powiedz z pamięci -> porównaj -> braki i dopytania fiszkami do skutku */
function unitStart(t){var x=t.o.x,u=S.u[x.key],mode=T.o.mode;
  T.u={x:x,miss:{},man:{},txt:'',drill:[],seen:{},fm:[],ff:[],plan:false,wr:false,only:false};
  if(mode==='review'&&u&&u.n>=2){var d=(u.m||[]).filter(function(i){return i<x.pts.length}).map(function(i){return{k:'p',i:i}})
      .concat((u.f||[]).filter(function(i){return i<x.fu.length}).map(function(i){return{k:'f',i:i}}));
    if(d.length){T.u.only=true;T.u.drill=d;drillView();return}}
  if((!u||!u.n)&&mode!=='exam')readView();else askView()}
function readView(){setView('read');bar();var x=T.u.x,pc=priChip(x);
  page(crumb()+'<div class="chips"><span class="pri new">nowe pytanie</span>'+pc+'</div><h2 class="ask">'+esc(x.q)+'</h2>'+bkBox('Najpierw przeczytaj w Bochenku',x.src)
   +'<div class="how"><b>Potem przeczytaj odpowiedź, najlepiej na głos</b>Za chwilę zakryję odpowiedź, a Ty powiesz ją z pamięci.</div>'+(x.fig?FIG[x.fig]:'')+answerHtml(x)+xnote(x)
   +dock('<button class="btn" data-a="u-ask">Zakryj i powiedz z pamięci</button>','<button class="link" data-a="skip">Pomiń to pytanie</button>'))}
function aiOn(){return !!(S.ai&&cap.sample)}
function micBtn(){return cap.dict?'<button class="btn ghost mic sml" type="button" data-a="mic">'+ICO.mic+' Mów</button>':''}
function askView(){setView('ask');bar();var u=T.u,x=u.x,exam=T.o.mode==='exam';
  var h=crumb()+'<h2 class="ask">'+esc(x.q)+'</h2><div class="how"><b>Powiedz odpowiedź z pamięci</b>Na głos albo w myślach, punkt po punkcie, z nazwami łacińskimi. Potem porównasz ją ze wzorcem.</div>';
  if(x.heads.length&&!exam)h+=u.plan?'<div><div class="lbl" style="margin-bottom:8px">Plan odpowiedzi</div><div class="cues">'+x.heads.map(function(g){return '<span>'+esc(g)+'</span>'}).join('')+'</div></div>'
    :'<div><button class="link" data-a="u-plan" style="padding-left:0">Nie wiem, od czego zacząć: pokaż plan</button></div>';
  if(aiOn())h+=u.wr?'<form id="af"><textarea id="ans" placeholder="Napisz albo podyktuj odpowiedź. AI wstępnie zaznaczy, czego zabrakło.">'+esc(u.txt)+'</textarea><div id="micslot" style="margin-top:8px">'+micBtn()+'</div></form>'
    :'<div><button class="link" data-a="u-write" style="padding-left:0">Wolę napisać lub podyktować, niech AI zaznaczy braki</button></div>';
  page(h+dock('<button class="btn" data-a="u-check">Pokaż wzorcową odpowiedź</button>','<button class="link" data-a="skip">Pomiń to pytanie</button>'),u.plan||u.wr);
  if(u.wr){dictT=document.getElementById('ans');dictBase=u.txt?u.txt+' ':''}}
function missCount(){var u=T.u,n=0;Object.keys(u.miss).forEach(function(i){if(u.miss[i])n++});return n}
function checkBtn(n){return n?'Dalej: przećwicz braki ('+n+')':'Dalej, wszystko powiedziałem'}
function checkView(still){setView('check');bar();var u=T.u,x=u.x,n=missCount();
  var note=u.aiBusy?'AI czyta Twoją odpowiedź…':(u.aiNote||'Dotknij punktów, których nie powiedziałeś. Niezaznaczone liczę jako dobre.');
  var h=crumb()+'<h2 class="ask sm2">'+esc(x.q)+'</h2><p class="mut" id="cnote">'+esc(note)+'</p>';
  if(u.aiErr&&u.aiErr.length)h+='<div class="fb no"><b>AI: to mogło być powiedziane błędnie</b><ul>'+u.aiErr.map(function(s){return '<li>'+esc(s)+'</li>'}).join('')+'</ul></div>';
  h+='<ul class="chk">'+x.pts.map(function(p,i){return (p.g?'<li class="hd">'+esc(p.g)+'</li>':'')+'<li class="it'+(u.miss[i]?' miss':'')+'" data-a="u-tog" data-i="'+i+'" role="checkbox" aria-checked="'+(u.miss[i]?'false':'true')+'" tabindex="0"><span class="c">'+ICO.ck+ICO.no+'</span><div>'+p.a+pgTag(p.s)+'</div></li>'}).join('')+'</ul>'+xnote(x)+srcLine(x);
  page(h+dock('<button class="btn" id="cb" data-a="u-save">'+checkBtn(n)+'</button>','<button class="link" id="cl" data-a="u-clear"'+(n?'':' hidden')+'>Umiem wszystko, odznacz</button>'),still);if(still)window.scrollTo(0,u.sy||0)}
function aiGrade(){var u=T.u,x=u.x;u.aiBusy=true;checkView();
  var facts=x.pts.map(function(p,k){return (k+1)+'. '+strip(p.a)}).join('\n'),N=x.pts.length;
  var prompt='Jesteś asystentem do nauki anatomii (podręcznik Bochenka). Student odpowiada z pamięci na pytanie z zaliczenia ustnego: „'+x.q+'”. Poniżej ponumerowane punkty wzorcowej odpowiedzi oraz odpowiedź studenta (pisana albo dyktowana; może być potoczna, bez interpunkcji, bez polskich znaków, z błędami rozpoznawania mowy).\n'
   +'Dla KAŻDEGO punktu oceń: 2 = student to przekazał (sens się zgadza, nie musi być dosłownie; synonimy i skróty są w porządku), 1 = wspomniał tylko część, 0 = pominął. Oceniaj życzliwie, po sensie, nie czepiaj się sformułowań. Zgadzać się muszą tylko liczby, poziomy kręgów, numery żeber i nazwy struktur.\n'
   +'Osobno wypisz stwierdzenia studenta SPRZECZNE z punktami (najwyżej 3, każde krótko). Nie dodawaj niczego spoza listy punktów.\n'
   +'Odpowiedz WYŁĄCZNIE jednym obiektem JSON w tej postaci: {"s":[2,0,1],"err":["powiedział C6, we wzorcu C7"]}. Tablica "s" ma mieć dokładnie '+N+' '+pl(N,'ocenę','oceny','ocen')+'.\n\nPUNKTY:\n'+facts+'\n\nODPOWIEDŹ STUDENTA:\n'+u.txt.slice(0,6000);
  var opt={modelTier:'quick',cache:false},ask;
  try{ask=typeof cap.sample.json==='function'?cap.sample.json(prompt,opt):cap.sample(prompt,opt).then(function(r){var s=r.text||'';return JSON.parse(s.slice(s.indexOf('{'),s.lastIndexOf('}')+1))})}catch(e){ask=Promise.reject(e)}
  ask.then(function(o){if(!T||T.u!==u||view!=='check')return;if(!o||!Array.isArray(o.s))throw {code:'invalid_json'};
    o.s.forEach(function(v,k){if(k<N&&!u.man[k])u.miss[k]=+v>=2?0:1});u.aiErr=(Array.isArray(o.err)?o.err:[]).filter(function(s){return typeof s==='string'&&s}).slice(0,3);
    u.aiBusy=false;u.aiNote='Braki wstępnie zaznaczyło AI. To tylko podpowiedź: dotknij punktu, żeby zmienić, albo wybierz „Umiem wszystko”.';u.sy=window.scrollY;checkView(true)})
  .catch(function(e){var c=e&&e.code,off=c==='not_granted'||c==='sampling_disabled'||c==='not_declared'||c==='capability_disabled';if(off)cap.sample=null;if(!T||T.u!==u)return;u.aiBusy=false;
    u.aiNote=off?'Sprawdzanie przez AI jest tu wyłączone. Zaznacz braki sam.':(c==='rate_limited'?'Limit zapytań do AI na teraz. Zaznacz braki sam.':'AI nie odpowiedziało. Zaznacz braki sam.');if(view==='check'){u.sy=window.scrollY;checkView(true)}})}
function afterCheck(){var u=T.u,x=u.x,us=S.u[x.key],mode=T.o.mode,fu=[];
  u.fm=Object.keys(u.miss).filter(function(i){return u.miss[i]}).map(Number).sort(function(a,b){return a-b});
  if(mode==='exam'){if(x.fu.length)fu=[Math.floor(Math.random()*x.fu.length)]}
  else if(!us||!us.n)fu=x.fu.map(function(_,i){return i});
  else fu=(us.f||[]).filter(function(i){return i<x.fu.length});
  u.drill=(mode==='exam'?[]:u.fm.map(function(i){return{k:'p',i:i}})).concat(fu.map(function(i){return{k:'f',i:i}}));
  if(u.drill.length)drillView();else unitSave()}
function drillView(shown){setView('drill');bar();var u=T.u,x=u.x,c=u.drill[0],isF=c.k==='f',q=isF?x.fu[c.i].q:x.pts[c.i].c,a=isF?x.fu[c.i].a:x.pts[c.i].a,ps=isF?x.fu[c.i].s:x.pts[c.i].s;
  var lab=isF?'Prowadzący dopytuje':(u.only?'Ostatnio tego zabrakło':'Tego zabrakło'),left=u.drill.length;
  var h=crumb()+(u.only||isF?'<p class="crumb" style="color:var(--ink2)">'+esc(x.q)+'</p>':'')
   +'<div class="fc'+(isF?' fu':'')+'"><div class="lb">'+lab+'<span>'+(left>1?'zostało '+left:'ostatnia')+'</span></div><div class="qq">'+esc(q)+'</div>'+(ps?'<div class="pgq">'+ICO.book+'<span>Przeczytaj w Bochenku: <b>'+esc(ps)+'</b></span></div>':'')+(shown?'<div class="aa">'+a+'</div>':'')+'</div>';
  page(h+dock(shown?'<button class="btn ghost" data-a="d-no">Jeszcze nie</button><button class="btn" data-a="d-yes">Wiem</button>':'<button class="btn" data-a="d-show">Pokaż odpowiedź</button>'),shown)}
function drillAns(yes){var u=T.u,c=u.drill.shift(),id=c.k+c.i;
  if(!u.seen[id]){u.seen[id]=1;if(!yes){if(c.k==='f')u.ff.push(c.i);else if(u.only)u.fm.push(c.i)}}
  if(!yes)u.drill.push(c);
  if(u.drill.length)drillView();else unitSave()}
function unitSave(){var u=T.u,ok=!u.fm.length&&!u.ff.length;T.log.push({x:u.x,m:u.fm.length+u.ff.length});record(T.t,ok,{m:u.fm,f:u.ff});nextTask()}

/* łacina: wpisujesz; błędne wracają w kolejnych rundach, aż każda wyjdzie */
function wordView(t){setView('word');bar();var w=t.o.w;t.done=false;
  page(crumb('łacina'+(t.r>1?', runda '+t.r:''))+'<div><div class="lbl" style="margin-bottom:6px">Jak to się nazywa po łacinie?</div><div class="wq">'+esc(w.pl)+'</div></div>'
   +'<form id="tf" autocomplete="off"><input type="text" id="in0" autocapitalize="off" autocorrect="off" spellcheck="false" enterkeyhint="done" placeholder="nazwa łacińska" aria-label="Nazwa łacińska"></form><div id="fb"></div>'
   +dock('<button class="btn" id="tb" data-a="w-check">Sprawdź</button>','<button class="link" id="dk" data-a="w-dk">Nie wiem, pokaż</button>'));
  var el=document.getElementById('in0');try{el.focus({preventScroll:true})}catch(e){}}
function wordCheck(dk){var t=T&&T.t;if(!t||t.o.k!=='w')return;
  if(t.done){record(t,t.ok);if(!t.ok)T.q.push({o:t.o,r:t.r+1});nextTask();return}
  var w=t.o.w,el=document.getElementById('in0'),v=nlat(el.value),ok=!dk&&!!v&&v===nlat(w.la);
  if(!dk&&!v){el.focus();return}
  el.classList.add(ok?'ok':'bad');el.readOnly=true;t.done=true;t.ok=ok;wordFb()}
function wordFb(){var t=T.t,w=t.o.w,ok=t.ok;
  document.getElementById('fb').innerHTML='<div class="fb '+(ok?'ok':'no')+'">'+(ok?'':'<b>Poprawnie:</b> ')+'<i>'+esc(w.la)+'</i>'+pgTag(w.s)+(ok?'':'<div><button class="link" type="button" data-a="w-ok" style="padding-left:0">Napisałem dobrze, zalicz</button></div>')+'</div>';
  var b=document.getElementById('tb'),d=document.getElementById('dk');b.textContent=ok?'Dalej':'Dalej, wróci na końcu';if(d)d.hidden=true;try{b.focus({preventScroll:true})}catch(e){}}

function finish(){var o=T.o,n=T.n,ok=T.ok,back=T.back,wait=T.wait,L=o.L,log=T.log;T=null;setView('end');nav('home');setTis(L?L.tis:'');
  if(!n){leave(o);return}
  var p=Math.round(ok/n*100),msg;
  if(o.mode==='learn')msg=(o.one?'Jutro to pytanie':'Jutro wszystko z tej lekcji')+' wróci raz, do sprawdzenia. Co powiesz dobrze, będzie utrwalone.';
  else if(o.mode==='exam'){var anyM=log.some(function(r){return r.m});msg=back?'Braki z pytań, które już przerabiałeś, zapisałem do powtórki.':(anyM?'Braki dotyczą pytań, których jeszcze nie przerabiałeś. Czekają w lekcjach.':'Bez braków.')}
  else msg=(ok-wait>0?(ok-wait)+' '+pl(ok-wait,'rzecz utrwalona','rzeczy utrwalone','rzeczy utrwalonych')+'. ':'')+(back?back+' '+pl(back,'wróci','wrócą','wróci')+' jutro, już tylko to, czego zabrakło. ':'')+(wait?'To był dodatkowy trening: sprawdzian utrwalenia będzie jutro.':'');
  var h='<div><h1>'+(o.mode==='exam'?'Koniec egzaminu':(o.one?'Pytanie zrobione':(o.mode==='learn'?'Lekcja zrobiona':(o.title==='Trening'?'Trening zrobiony':'Powtórka zrobiona'))))+'</h1></div><div class="res">'+bigRing(p)+'<div><div class="rl"><b>'+ok+' z '+n+'</b> od razu dobrze</div><p class="mut sm">'+msg+'</p></div></div>';
  if(log.length)h+='<ul class="rlist">'+log.map(function(r){return '<li>'+esc(r.x.q)+'<span class="'+(r.m?'no':'ok')+'">'+(r.m?'braki: '+r.m:'bez braków')+'</span></li>'}).join('')+'</ul>';
  var nl=nextLesson(),p1;
  if(o.one)p1='<button class="btn" data-a="'+(o.from==='notes'?'notes':'lesson')+'" data-l="'+L.id+'">Wróć</button>';
  else if(o.mode==='learn'&&nl&&nl!==L)p1='<button class="btn ghost" data-a="home">Na teraz koniec</button><button class="btn" data-a="lesson" data-l="'+nl.id+'">Następna lekcja</button>';
  else if(o.mode==='exam')p1='<button class="btn ghost" data-a="home">Wróć</button><button class="btn" data-a="exam">Losuj jeszcze raz</button>';
  else p1='<button class="btn" data-a="home">Wróć</button>';
  page(h+dock(p1))}
function startExam(){var pool=ALLU.filter(function(u){return learned(u.key)});if(pool.length<6)pool=ALLU.slice();var pick=[];
  while(pick.length<6&&pool.length){var tot=pool.reduce(function(s,u){return s+u.pri},0),r=Math.random()*tot,i=0;while(i<pool.length-1&&(r-=pool[i].pri)>0)i++;pick.push(pool.splice(i,1)[0])}
  curL=null;startSession(pick.map(uo),{mode:'exam',title:'Próbny egzamin'})}

/* ---------- notatki ---------- */
function notesList(q){var st=fold(q||'').split(/[^a-z0-9]+/).filter(Boolean).map(function(w){return w.length>4?w.slice(0,Math.max(4,w.length-2)):w}),h='',any=false;
  LESSONS.forEach(function(L){var us=L.units.filter(function(u){return st.every(function(s){return u.hay.indexOf(s)>=0})});if(!us.length)return;any=true;
    h+='<div class="t-'+L.tis+'"><div class="lh">'+esc(L.t)+'</div><div class="list">'+us.map(function(u){return urow(u,'notes')}).join('')+'</div></div>'});
  return any?h:'<p class="empty">Nic nie pasuje. Spróbuj krótszego słowa.</p>'}
var noteQ='';
function notes(){setView('notes');nav('notes');setTis('');T=null;curL=null;
  page('<div><h1>Notatki</h1><p class="mut" style="margin-top:8px">Wzorcowe odpowiedzi na wszystkie pytania. Do przejrzenia przed lekcją i tuż przed zaliczeniem.</p></div>'
   +'<form id="nf" role="search"><input type="search" id="nq" placeholder="Szukaj, np. kresa łukowata" aria-label="Szukaj w notatkach" value="'+esc(noteQ)+'"></form><div class="nl" id="nres">'+notesList(noteQ)+'</div>')}

/* ---------- więcej ---------- */
var REFS=[['McDaniel, Howard i Einstein 2009','przeczytaj, powiedz z pamięci, sprawdź: po takiej nauce studenci odtwarzali z pamięci więcej niż po ponownym czytaniu i po robieniu notatek','https://doi.org/10.1111/j.1467-9280.2009.02325.x'],
 ['Dunlosky i in. 2013','przegląd 10 technik nauki; najwyżej ocenione: sprawdzanie się z pamięci i rozłożenie nauki w czasie','https://doi.org/10.1177/1529100612453266'],
 ['Karpicke i Roediger 2008','ponowne przypominanie sobie tego, co już raz wyszło, dało po tygodniu ok. 80% zamiast ok. 35%','https://doi.org/10.1126/science.1152408'],
 ['Rawson i Dunlosky 2022','do skutku w pierwszej sesji, potem jeszcze raz do skutku po przerwie (successive relearning)','https://doi.org/10.1177/09637214221100484'],
 ['Cepeda i in. 2008','najlepsza przerwa przed powtórką to ok. 20–40% czasu do egzaminu; przy kilku dniach wychodzi 1 dzień','https://doi.org/10.1111/j.1467-9280.2008.02209.x'],
 ['MacLeod i Bodner 2017','mówienie na głos i pisanie pamięta się lepiej niż ciche czytanie','https://doi.org/10.1177/0963721417691356']];
function settings(){setView('set');nav('set');setTis('');T=null;curL=null;
  var nw=0;LESSONS.forEach(function(L){nw+=L.words.length});
  var h='<div><h1>Więcej</h1></div><div><h2 style="margin-bottom:12px">Jak to działa</h2><dl class="how2">'
   +'<div><dt>1. Czytasz wzorcową odpowiedź</dt><dd>Każde pytanie to pytanie prowadzącego. Odpowiedź jest w punktach, każda informacja występuje w niej raz.</dd></div>'
   +'<div><dt>2. Mówisz ją z pamięci</dt><dd>Na głos albo w myślach. Potem porównujesz ze wzorcem i zaznaczasz tylko to, czego zabrakło. O zaliczeniu punktu decydujesz Ty.</dd></div>'
   +'<div><dt>3. Braki i dopytania ćwiczysz do skutku</dt><dd>Każdy brakujący punkt dostaje własną fiszkę z konkretnym pytaniem. Do tego dopytania prowadzącego. Na koniec lekcji wpisujesz nazwy łacińskie; błędne wracają w kolejnych rundach.</dd></div>'
   +'<div><dt>4. Jedna powtórka po przerwie</dt><dd>Następnego dnia każde pytanie wraca raz. Dobra odpowiedź: utrwalone, więcej nie wraca. Braki: ćwiczysz je i kolejnego dnia wracają już tylko one.</dd></div></dl></div>'
   +'<div><h2 style="margin:10px 0 4px">Ustawienia</h2>'
   +'<div class="set"><div><b>Podpowiedź AI</b><p class="sm mut">Jeśli napiszesz albo podyktujesz odpowiedź, AI wstępnie zaznaczy braki. Decyzja zawsze jest Twoja. '+(cap.sample?'':'W tym widoku jest niedostępna.')+'</p></div><button class="sw'+(S.ai?' on':'')+'" data-a="s-ai" role="switch" aria-checked="'+(S.ai?'true':'false')+'" aria-label="Podpowiedź AI"></button></div>'
   +'<div class="set"><div><b>Zacznij od zera</b><p class="sm mut">Usuwa cały postęp. Zapisuje się on '+dbState+'.</p></div><button class="btn ghost sml" data-a="s-reset">'+(resetArm?'Na pewno usuń':'Usuń postęp')+'</button></div></div>'
   +'<div><h2 style="margin:10px 0 12px">Skąd pytania i odpowiedzi</h2><p class="mut">Pytania: lista realnych pytań prowadzącego i Twoja notatka z zajęć. Odpowiedzi: Bochenek, Anatomia człowieka, tom I; przy każdym pytaniu są numery stron. Tam, gdzie czegoś w Bochenku nie ma albo podaje to dwojako, jest o tym uwaga pod odpowiedzią. Razem '+ALLU.length+' pytań i '+nw+' nazw łacińskich.</p></div>'
   +'<div><h2 style="margin:10px 0 12px">Skąd ta metoda</h2><ul class="refs">'+REFS.map(function(r){return '<li><a href="'+r[2]+'" target="_blank" rel="noopener">'+r[0]+'</a>: '+r[1]+'.</li>'}).join('')+'</ul></div>';page(h,resetArm>0)}

/* ---------- zdarzenia ---------- */
function L_(el){var id=el.getAttribute('data-l');for(var i=0;i<LESSONS.length;i++)if(LESSONS[i].id===id)return LESSONS[i];return null}
function grabTxt(){var a=document.getElementById('ans');if(a&&T&&T.u)T.u.txt=a.value.trim()}
document.addEventListener('click',function(e){var el=e.target.closest('[data-a]');if(!el)return;var a=el.getAttribute('data-a'),u=T&&T.u,L,x;
  switch(a){
  case 'home':home();break;
  case 'notes':notes();break;
  case 'set':resetArm=0;settings();break;
  case 'lesson':L=L_(el);if(L)lessonView(L);break;
  case 'unit':x=UNITS[el.getAttribute('data-u')];if(x)unitView(x,el.getAttribute('data-f')||'lesson');break;
  case 'learn':L=L_(el);if(L){curL=L;startSession(learnQ(L),{mode:'learn',L:L,title:L.t})}break;
  case 'review':L=L_(el);curL=L;startSession(reviewQ(false,L),{mode:'review',L:L,title:'Powtórka'});break;
  case 'early':L=L_(el);curL=L;startSession(reviewQ(true,L),{mode:'review',L:L,title:'Trening'});break;
  case 'again':L=L_(el);if(L){curL=L;startSession(L.units.map(uo),{mode:'review',L:L,title:'Trening'})}break;
  case 'one':x=UNITS[el.getAttribute('data-u')];if(x){curL=x.L;startSession([uo(x)],{mode:learned(x.key)?'review':'learn',L:x.L,one:true,from:noteFrom,title:learned(x.key)?'Trening':x.L.t})}break;
  case 'exam':startExam();break;
  case 'game':if(window.GAME)window.GAME.home();break;
  case 'exit':exit();break;
  case 'skip':if(T)nextTask();break;
  case 'u-ask':askView();break;
  case 'u-plan':grabTxt();u.plan=true;askView();break;
  case 'u-write':u.wr=true;askView();var ta=document.getElementById('ans');if(ta)try{ta.focus({preventScroll:true})}catch(er){}break;
  case 'u-check':grabTxt();if(u.txt.length>=12&&aiOn())aiGrade();else checkView();break;
  case 'u-tog':var i=+el.getAttribute('data-i');u.miss[i]=u.miss[i]?0:1;u.man[i]=1;el.classList.toggle('miss',!!u.miss[i]);el.setAttribute('aria-checked',u.miss[i]?'false':'true');
    var n=missCount();document.getElementById('cb').textContent=checkBtn(n);document.getElementById('cl').hidden=!n;break;
  case 'u-clear':u.miss={};x=u.x;x.pts.forEach(function(_,k){u.man[k]=1});u.sy=window.scrollY;checkView(true);break;
  case 'u-save':if(u.aiBusy){u.aiBusy=false}afterCheck();break;
  case 'd-show':drillView(true);break;
  case 'd-yes':drillAns(true);break;
  case 'd-no':drillAns(false);break;
  case 'w-check':wordCheck(false);break;
  case 'w-dk':wordCheck(true);break;
  case 'w-ok':if(T&&T.t&&T.t.done){T.t.ok=true;var inp=document.getElementById('in0');inp.classList.remove('bad');inp.classList.add('ok');wordFb()}break;
  case 'mic':if(cap.dict){if(dictOn)cap.dict.stop().catch(function(){});else{dictT=document.getElementById('ans');dictBase=dictT&&dictT.value?dictT.value.replace(/\s*$/,' '):'';cap.dict.start().catch(function(){toast('Mikrofon niedostępny')})}}break;
  case 's-ai':S.ai=S.ai?0:1;save();settings();break;
  case 's-reset':if(!resetArm){resetArm=Date.now();settings();setTimeout(function(){if(resetArm&&Date.now()-resetArm>=5000){resetArm=0;if(view==='set')settings()}},5200)}
    else{resetArm=0;S.u={};S.g={};S.rs=Date.now();save();if(dbRef){clearTimeout(dbTimer);pushDb()}toast('Postęp usunięty');home()}break;
  }});
document.addEventListener('submit',function(e){e.preventDefault();if(e.target.id==='tf')wordCheck(false)});
document.addEventListener('input',function(e){if(e.target.id==='nq'){noteQ=e.target.value;document.getElementById('nres').innerHTML=notesList(noteQ)}});
document.addEventListener('keydown',function(e){if((e.key==='Enter'||e.key===' ')&&e.target.classList&&e.target.classList.contains('it')){e.preventDefault();e.target.click()}});
document.addEventListener('visibilitychange',function(){if(document.visibilityState==='hidden'&&dbRef&&dbDirty){clearTimeout(dbTimer);pushDb()}});

/* ---------- możliwości strony: AI, dyktowanie, zapis na koncie ---------- */
function initCaps(){var c=window.claude;if(!c||!c.use){if(capTry++<6)setTimeout(initCaps,700*capTry);return}
  c.use('sample').then(function(x){cap.sample=x||null},function(){});
  c.use('dictation').then(function(d){if(!d)return;cap.dict=d;
    d.onPartial(function(p){if(dictT)dictT.value=dictBase+p.text});
    d.onFinal(function(p){if(dictT){dictBase=dictBase+p.text+' ';dictT.value=dictBase}});
    d.onState(function(s){dictOn=s.state==='listening';var b=document.querySelector('.mic');if(b){b.classList.toggle('live',dictOn);b.innerHTML=dictOn?'Stop':ICO.mic+' Mów'}});
    var sl=document.getElementById('micslot');if(sl&&!sl.firstChild)sl.innerHTML=micBtn()},function(){});
  Promise.all([c.use('db'),c.use('user')]).then(function(r){var db=r[0],user=r[1];if(!db||!user)return;
    return user.id().then(function(uid){if(!uid)return;var ref=db.doc('data/users/'+uid+'/state');
      return ref.get().then(function(snap){var rts=0,fresh=true;dbRef=ref;dbState='na Twoim koncie';
        if(snap.exists){try{var d=snap.data();if(d&&d.v===5){fresh=false;rts=d.ts||0;mergeRemote(JSON.parse(d.json))}}catch(e){}}
        /* stary zapis (sprzed tej wersji) zostaje nadpisany: postęp z plakatu jest usunięty */
        if(fresh||(S.ts||0)>rts){if(!S.ts)S.ts=Date.now();dbDirty=true;pushDb()}
        if(view==='home'){var y=window.scrollY;home();window.scrollTo(0,y)}else if(view==='set')settings()})})}).catch(function(){})}

home();initCaps();
window.__so5={page:page,dock:dock,nav:nav,setView:setView,setTis:setTis,toast:toast,esc:esc,pl:pl,ICO:ICO,bkBox:bkBox,S:S,LESSONS:LESSONS,UNITS:UNITS,ALLU:ALLU,nlat:nlat,learnQ:learnQ,reviewQ:reviewQ,lstat:lstat,dayKey:dayKey,save:save,home:home,
  get T(){return T},get view(){return view},get cap(){return cap}};
})();
