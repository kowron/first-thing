/* Wymienianka na czas: mówisz nazwy mięśni z listy, strona słucha (dyktowanie) albo czyta, co wpiszesz.
   Czas liczy się od chwili, gdy mikrofon słucha. Punkty: 100 za każdą nazwę, do tego premia za komplet
   tym większa, im szybciej (pełna przy czasie wzorcowym, zero przy dwukrotnie dłuższym). */
(function(){
'use strict';
var A=window.__so5,LISTS=window.WYM,M=window.WYMATCH;if(!A||!LISTS||!M)return;
var app=document.getElementById('app'),esc=A.esc;
var MODES={p:{t:'Polska',d:'Mówisz polskie nazwy.',sec:3},l:{t:'Łacińska',d:'Mówisz nazwy łacińskie (słowo „musculus” możesz pominąć).',sec:4},
  x:{t:'Mieszana',d:'Po każdej polskiej nazwie od razu łacińska.',sec:7}};
var ICO={
 mic:'<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0014 0M12 18v3"/></svg>',
 stop:'<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><rect x="6" y="6" width="12" height="12" rx="2.5" fill="currentColor"/></svg>',
 kb:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="3" y="6" width="18" height="12" rx="2.5"/><path d="M7 10h.01M11 10h.01M15 10h.01M7 14h10"/></svg>',
 timer:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2.5M9 2h6"/></svg>'};

/* ---------- pomocnicze ---------- */
function items(L){var a=[];L.g.forEach(function(g,gi){g.i.forEach(function(it){a.push({it:it,g:gi})})});return a}
function par(L,m){return items(L).length*MODES[m].sec*1000}
function fmt(ms,tenths){ms=Math.max(0,ms||0);var s=Math.floor(ms/1000),m=Math.floor(s/60);s%=60;
  return m+':'+(s<10?'0':'')+s+(tenths?'<small>,'+Math.floor(ms%1000/100)+'</small>':'')}
function fmtT(ms){ms=Math.max(0,ms||0);var s=Math.round(ms/1000),m=Math.floor(s/60);s%=60;return m+':'+(s<10?'0':'')+s}
function name(it,m){return m==='l'?it.l:(m==='x'?it.p+' · '+it.l:it.p)}
function S(){var s=A.S;if(!s.g)s.g={};return s}
function best(L,m){return S().g[L.id+'|'+m]||null}
function medal(r){return r&&r.md?r.md:''}
var MED={z:'złoto',s:'srebro',b:'brąz'};
function medalSvg(md,big){var c=md?'var(--m-'+md+')':'var(--line)',sz=big?64:22;
  return '<svg class="medal'+(md?'':' none')+'" width="'+sz+'" height="'+Math.round(sz*1.2)+'" viewBox="0 0 40 48" aria-hidden="true"><path d="M12 2h6l4 13h-6zM28 2h-6l-4 13h6z" fill="'+(md?'var(--accent)':'var(--line)')+'" opacity=".85"/><circle cx="20" cy="30" r="14" fill="'+c+'"/><circle cx="20" cy="30" r="10" fill="none" stroke="var(--surface)" stroke-opacity=".55" stroke-width="1.6"/></svg>'}
function score(L,m,found,tEnd){var n=items(L).length,f=0;Object.keys(found).forEach(function(k){if(found[k]!=null)f++});
  var pr=par(L,m),full=f===n,bonus=full?Math.round(1000*Math.max(0,Math.min(1,(2*pr-tEnd)/pr))):0;
  var md=full?(tEnd<=pr?'z':(tEnd<=1.5*pr?'s':'b')):'';
  return {p:f*100+bonus,f:f,n:n,bonus:bonus,md:md,t:tEnd}}

/* ---------- stan gry ---------- */
var G=null,tick=null,hooked=false,mode=(A.S.gm&&MODES[A.S.gm])?A.S.gm:'p';
function dict(){return A.cap&&A.cap.dict}
function hook(){var d=dict();if(!d||hooked)return;hooked=true;
  d.onPartial(function(e){if(G&&G.st==='run'){G.part=e.text||'';update()}});
  d.onFinal(function(e){if(G&&(G.st==='run'||G.st==='ending')){G.fin+=e.text;G.part='';update()}});
  d.onState(function(e){if(!G)return;G.ls=e.state;
    if(e.state==='listening'&&G.st==='run'&&!G.t0)begin();
    if(e.state==='idle'&&G.st==='run'){G.micOff=e.reason||'stopped';if(e.reason==='not_granted'||e.reason==='unavailable')G.noMic=true;if(!G.t0)begin()}
    if(e.state==='listening')G.micOff='';
    micUI()})}

/* ---------- ekran wyboru ---------- */
function home(){A.setView('game');A.nav('game');A.setTis('');G=null;stopTick();
  var h='<div class="g-lead"><div class="eb g-eb">'+ICO.timer+' Na czas</div><h1>Wymienianka</h1><p class="mut">Wybierz listę i mów nazwy mięśni na głos, w dowolnej kolejności. Liczę czas i punkty: 100 za każdą nazwę i premia za komplet, tym większa, im szybciej.</p></div>';
  h+='<div class="seg3" role="radiogroup" aria-label="Tryb">'+Object.keys(MODES).map(function(k){return '<button role="radio" aria-checked="'+(k===mode)+'" class="'+(k===mode?'on':'')+'" data-g="mode" data-m="'+k+'">'+MODES[k].t+'</button>'}).join('')+'</div>';
  h+='<p class="sm mut g-md">'+esc(MODES[mode].d)+'</p>';
  if(!dict())h+='<div class="g-note">Rozpoznawanie mowy działa w przeglądarce Chrome i w aplikacji Claude na komputerze. Tutaj możesz wpisywać nazwy, a czas i punkty liczą się tak samo.</div>';
  h+='<div class="g-lists">'+LISTS.map(function(L){var n=items(L).length,b=best(L,mode);
    return '<button class="g-card" data-g="ready" data-l="'+L.id+'"><span class="g-cm">'+medalSvg(medal(b))+'</span><span class="g-ct"><b>'+esc(L.t)+'</b><span class="g-cd">'+n+' '+A.pl(n,'nazwa','nazwy','nazw')+' · czas wzorcowy '+fmtT(par(L,mode))+'</span>'
      +'<span class="g-cb">'+(b?'Rekord: <b>'+b.p+' pkt</b>, '+fmtT(b.t)+(b.md?' · '+MED[b.md]:''):'Jeszcze nie grane')+'</span></span><span class="ch">'+A.ICO.ch+'</span></button>'}).join('')+'</div>';
  h+='<div class="g-rules"><div class="lbl">Medale</div><div class="g-rl"><span>'+medalSvg('z')+'komplet w czasie wzorcowym</span><span>'+medalSvg('s')+'komplet do 1,5× tego czasu</span><span>'+medalSvg('b')+'komplet</span></div></div>';
  A.page(h)}

function ready(L){A.setView('game');A.nav('game');A.setTis(L.tis||'muscle');G={L:L,m:mode,st:'ready'};stopTick();
  var n=items(L).length,b=best(L,mode);
  var h='<div><button class="back" data-g="home">'+A.ICO.back+' Wymienianka</button></div>';
  h+='<div><div class="eb">'+MODES[mode].t+' wymienianka</div><h1>'+esc(L.t)+'</h1><p class="mut" style="margin-top:8px">'+esc(L.d)+'</p></div>';
  h+=A.bkBox('Przed grą przeczytaj w Bochenku',L.s);
  h+='<div class="g-stats"><div><span>Nazw</span><b>'+n+'</b></div><div><span>Czas wzorcowy</span><b>'+fmtT(par(L,mode))+'</b></div><div><span>Rekord</span><b>'+(b?b.p+' pkt':'–')+'</b></div></div>';
  h+='<div class="g-how"><b>Jak grać</b>'+esc(MODES[mode].d)+' Kolejność jest dowolna. Czas rusza, gdy mikrofon zacznie słuchać. Gdy powiesz wszystko, gra kończy się sama; możesz też nacisnąć „Koniec”.</div>';
  h+=skeleton(L,mode,{},true);
  if(L.x)h+='<div class="xnote"><b>Uwaga</b>'+esc(L.x)+'</div>';
  A.page(h+A.dock('<button class="btn g-go" data-g="start">'+ICO.mic+' Start</button>','<span class="sm mut" style="padding:8px 0">Mów wyraźnie, jedną nazwę po drugiej.</span>'))}

/* puste miejsca na nazwy, pogrupowane jak u Bochenka */
function skeleton(L,m,found,still){var k=0;
  return '<div class="g-board'+(still?' still':'')+'">'+L.g.map(function(g){var f=0,cells=g.i.map(function(it){var i=k++,ok=found[i]!=null;if(ok)f++;
      return '<span class="slot'+(ok?' ok':'')+'" id="sl'+i+'">'+(ok?esc(name(it,m)):'')+'</span>'}).join('');
    return '<div class="g-grp"><div class="g-gh"><span>'+esc(g.t)+'</span><span class="g-gc" id="gc'+L.g.indexOf(g)+'">'+f+'/'+g.i.length+'</span></div><div class="slots">'+cells+'</div></div>'}).join('')+'</div>'}

/* ---------- gra ---------- */
function start(){if(!G)return;var d=dict();G.st='run';G.fin='';G.part='';G.typed='';G.found={};G.half={};G.t0=0;G.micOff='';G.noMic=!d;
  run();
  if(d){hook();d.start().catch(function(e){G.noMic=true;G.micOff=(e&&e.code)||'unavailable';if(!G.t0)begin();micUI();
      A.toast(e&&e.code==='not_granted'?'Mikrofon wyłączony. Wpisuj nazwy.':'Mikrofon niedostępny. Wpisuj nazwy.')})}
  else begin()}
function begin(){if(!G||G.t0)return;G.t0=Date.now();startTick();micUI();var i=document.getElementById('gin');if(i&&G.noMic)try{i.focus({preventScroll:true})}catch(e){}}
function startTick(){stopTick();tick=setInterval(function(){if(G&&G.st==='run'&&A.view!=='game-run'){var d0=dict();if(d0&&d0.active())d0.stop().catch(function(){});G=null}if(!G||G.st!=='run'){stopTick();return}var el=document.getElementById('gt');
  var t=G.t0?Date.now()-G.t0:0;if(el)el.innerHTML=fmt(t,true);var pr=par(G.L,G.m),pb=document.getElementById('gpar');if(pb)pb.style.width=Math.min(100,t/pr*100)+'%';
  if(pb)pb.classList.toggle('over',t>pr);if(G.t0&&t>3*pr)finish()},100)}
function stopTick(){if(tick){clearInterval(tick);tick=null}}
function run(){A.setView('game-run');var L=G.L,n=items(L).length;
  document.getElementById('top').innerHTML='<header class="bar sbar"><div class="wrap"><button class="x" data-g="quit" aria-label="Przerwij">'+A.ICO.x+'</button><div class="g-tl">'+esc(L.t)+' · '+MODES[G.m].t.toLowerCase()+'</div><span class="cnt" id="gcnt">0 z '+n+'</span></div></header>';
  var h='<div class="g-clock"><div class="g-time" id="gt">'+fmt(0,true)+'</div><div class="g-parbar"><b id="gpar"></b></div><div class="g-parl">czas wzorcowy '+fmtT(par(L,G.m))+'</div></div>';
  h+='<div class="g-mic" id="gmic"></div>';
  h+='<div class="g-heard" id="gh" aria-live="polite"><span class="mut">Tu pojawi się to, co słyszę.</span></div>';
  h+='<form id="gf" autocomplete="off"><input type="text" id="gin" autocapitalize="off" autocorrect="off" spellcheck="false" enterkeyhint="send" placeholder="albo wpisz nazwę i Enter" aria-label="Wpisz nazwę"></form>';
  h+=skeleton(L,G.m,{},false);
  A.page(h+A.dock('<button class="btn ghost" data-g="end">'+ICO.stop+' Koniec</button>'),true);micUI()}
function micUI(){var el=document.getElementById('gmic');if(!el||!G)return;
  if(G.st!=='run'){el.innerHTML='';return}
  if(G.noMic)el.innerHTML='<span class="g-dot kb">'+ICO.kb+'</span><span>Wpisujesz nazwy. Każda zatwierdzona Enterem trafia do gry.</span>';
  else if(G.ls==='listening')el.innerHTML='<span class="g-dot live"></span><span><b>Słucham.</b> Mów nazwy jedna po drugiej.</span>';
  else if(G.micOff&&G.t0)el.innerHTML='<span class="g-dot"></span><span>Mikrofon przestał słuchać.</span><button class="btn soft sml" data-g="mic">'+ICO.mic+' Wznów</button>';
  else el.innerHTML='<span class="g-dot wait"></span><span>Włączam mikrofon…</span>'}
function update(){if(!G||(G.st!=='run'&&G.st!=='ending'))return;var L=G.L,its=items(L),txt=G.fin+' '+G.typed+' '+(G.part||'');
  var R=M.scan(L,txt),now=G.t0?Date.now()-G.t0:0,fresh=[];
  R.forEach(function(r,i){var ok=G.m==='p'?r.p.length>0:(G.m==='l'?r.l.length>0:M.pair(r));
    if(G.m==='x'&&!ok&&(r.p.length||r.l.length))G.half[i]=1;
    if(ok&&G.found[i]==null){G.found[i]=now;fresh.push(i)}});
  fresh.forEach(function(i){var el=document.getElementById('sl'+i);if(el){el.className='slot ok pop';el.textContent=name(its[i].it,G.m)}});
  if(G.m==='x')Object.keys(G.half).forEach(function(i){if(G.found[i]==null){var el=document.getElementById('sl'+i);if(el)el.classList.add('half')}});
  var f=Object.keys(G.found).length;var c=document.getElementById('gcnt');if(c)c.textContent=f+' z '+its.length;
  L.g.forEach(function(g,gi){var n=0;its.forEach(function(x,i){if(x.g===gi&&G.found[i]!=null)n++});var e=document.getElementById('gc'+gi);if(e)e.textContent=n+'/'+g.i.length});
  var gh=document.getElementById('gh');if(gh){var words=(G.fin+' '+G.typed).trim().split(/\s+/).slice(-16).join(' ');
    gh.innerHTML=(words?'<span>'+esc(words)+'</span> ':'')+(G.part?'<i>'+esc(G.part)+'</i>':'')+(!words&&!G.part?'<span class="mut">Tu pojawi się to, co słyszę.</span>':'')}
  if(G.st==='run'&&f===its.length)finish()}
function finish(){if(!G||G.st!=='run')return;G.st='ending';G.tEnd=G.t0?Date.now()-G.t0:0;stopTick();
  var d=dict(),done=false,go=function(){if(done)return;done=true;update();G.st='end';result(true)};
  if(d&&!G.noMic&&d.active()){d.stop().then(go,go);setTimeout(go,3500)}else go()}
function quit(){var d=dict();stopTick();if(d&&G&&!G.noMic&&d.active())d.stop().catch(function(){});var L=G&&G.L;G=null;if(L)ready(L);else home()}

/* ---------- wynik ---------- */
function result(first){var L=G.L,m=G.m,its=items(L),sc=score(L,m,G.found,G.tEnd),key=L.id+'|'+m,b=S().g[key],rec=false;
  if(first){G.prev=b?b.p:null;if(!b||sc.p>b.p){S().g[key]={p:sc.p,t:sc.t,f:sc.f,n:sc.n,md:sc.md,at:Date.now()};A.save();rec=true}}
  else{if(!b||sc.p>b.p){S().g[key]={p:sc.p,t:sc.t,f:sc.f,n:sc.n,md:sc.md,at:Date.now()};A.save()}rec=G.prev==null||sc.p>G.prev}
  A.setView('game-end');A.nav('game');A.setTis(L.tis||'muscle');window.scrollTo(0,first?0:(G.sy||0));
  var pr=par(L,m),miss=sc.n-sc.f;
  var h='<div class="g-res"><div class="g-rm">'+medalSvg(sc.md,true)+'</div><div><div class="eb">'+(sc.md?{z:'Złoty medal',s:'Srebrny medal',b:'Brązowy medal'}[sc.md]:(miss?'Bez medalu':'Komplet'))+(rec&&G.prev!=null?' · nowy rekord':'')+'</div>'
   +'<div class="g-pts"><b>'+sc.p+'</b> pkt</div><p class="mut sm">'+sc.f+' z '+sc.n+' nazw · czas '+fmtT(sc.t)+' (wzorcowy '+fmtT(pr)+')'+(sc.bonus?' · premia '+sc.bonus:'')+'</p></div></div>';
  if(miss)h+='<p class="sm mut">Zabrakło '+miss+' '+A.pl(miss,'nazwy','nazw','nazw')+'. Jeśli coś powiedziałeś, a rozpoznawanie tego nie złapało, dotknij tej nazwy: zaliczę ją.</p>';
  var k=0;h+='<div class="g-sum">'+L.g.map(function(g){return '<div class="g-sg"><div class="g-gh"><span>'+esc(g.t)+'</span></div><ul>'+g.i.map(function(it){var i=k++,ok=G.found[i]!=null,man=G.man&&G.man[i];
      return '<li class="'+(ok?'ok':'no')+'"'+(ok&&!man?'':' data-g="tog" data-i="'+i+'" role="button" tabindex="0"')+'><span class="g-ck">'+(ok?'✓':'')+'</span><span class="g-nm"><b>'+esc(it.p)+'</b> <i>'+esc(it.l)+'</i>'
        +(ok?(man?' <span class="pg">zaliczone ręcznie</span>':' <span class="pg">'+fmtT(G.found[i])+'</span>'):' <span class="pg">'+esc(it.s)+'</span>')+'</span></li>'}).join('')+'</ul></div>'}).join('')+'</div>';
  if(L.x)h+='<div class="xnote"><b>Uwaga</b>'+esc(L.x)+'</div>';
  var heard=(G.fin+' '+G.typed).trim();
  if(heard)h+='<details class="g-tr"><summary>Co usłyszałem</summary><p>'+esc(heard)+'</p></details>';
  A.page(h+A.dock('<button class="btn ghost" data-g="home">Inna lista</button><button class="btn" data-g="again">Jeszcze raz</button>'),!first)}

/* ---------- zdarzenia ---------- */
document.addEventListener('click',function(e){var el=e.target.closest('[data-g]');if(!el)return;var a=el.getAttribute('data-g'),L;
  switch(a){
  case 'home':home();break;
  case 'mode':mode=el.getAttribute('data-m');A.S.gm=mode;A.save();home();break;
  case 'ready':L=LISTS.filter(function(x){return x.id===el.getAttribute('data-l')})[0];if(L)ready(L);break;
  case 'start':start();break;          /* d.start() musi paść od razu w kliknięciu */
  case 'mic':var d=dict();if(d&&G&&G.st==='run'){G.micOff='';micUI();d.start().catch(function(){G.noMic=true;micUI()})}break;
  case 'end':finish();break;
  case 'quit':quit();break;
  case 'again':L=G&&G.L;if(L){ready(L);start()}break;
  case 'tog':if(G&&G.st==='end'){var i=+el.getAttribute('data-i');G.man=G.man||{};if(G.found[i]==null){G.found[i]=G.tEnd;G.man[i]=1}else if(G.man[i]){delete G.found[i];delete G.man[i]}
      G.sy=window.scrollY;result(false)}break;
  }});
document.addEventListener('submit',function(e){if(e.target.id!=='gf')return;e.preventDefault();var i=document.getElementById('gin');if(!G||G.st!=='run'||!i||!i.value.trim())return;
  if(!G.t0)begin();G.typed+=' '+i.value.trim()+' ,';i.value='';update()});
document.addEventListener('keydown',function(e){if((e.key==='Enter'||e.key===' ')&&e.target.getAttribute&&e.target.getAttribute('data-g')==='tog'){e.preventDefault();e.target.click()}});
window.GAME={home:home,_G:function(){return G}};
})();
