/* Wymienianka: dopasowanie tego, co padło (dyktowanie po polsku albo wpisany tekst), do nazw z listy.
   Klucz fonetyczny wyrównuje łacinę zapisaną „po polsku” (cerwicis, trapezjus, skapule) i odmianę (płatowate, głowy).
   Funkcja czysta: WYMATCH.scan(lista, tekst) -> dla każdej pozycji {p:[[od,do]...], l:[[od,do]...]}. */
(function(){
'use strict';
function fold(s){return String(s).toLowerCase().replace(/ł/g,'l').normalize('NFD').replace(/[̀-ͯ]/g,'')}
function ph(s){
  s=' '+fold(s).replace(/[^a-z]+/g,' ')+' ';
  s=s.replace(/ae|oe/g,'e').replace(/ph/g,'f').replace(/th/g,'t').replace(/rh/g,'r').replace(/ch/g,'h')
     .replace(/qu/g,'kw').replace(/x/g,'ks').replace(/y/g,'i').replace(/v/g,'w').replace(/j/g,'i')
     .replace(/c(?=[ei])/g,'C').replace(/c/g,'k').replace(/C/g,'c').replace(/z/g,'s').replace(/([a-z])\1+/g,'$1');
  return s.trim()}
var FILL={m:1,mm:1,miesien:1,miesnie:1,miesnia:1,muskulus:1,muskuli:1,i:1,et:1};
function stem(w){var L=w.length,n=Math.max(4,Math.min(L-1,8));return w.slice(0,Math.min(n,L))}
function tol(n){return n>=7?2:(n>=5?1:0)}
function lev(a,b){var m=a.length,n=b.length,d=[],i,j;for(i=0;i<=n;i++)d[i]=i;
  for(i=1;i<=m;i++){var p=d[0];d[0]=i;for(j=1;j<=n;j++){var t=d[j];d[j]=Math.min(d[j]+1,d[j-1]+1,p+(a[i-1]===b[j-1]?0:1));p=t}}return d[n]}
/* czy słowo zaczyna się (z tolerancją) od rdzenia */
function hit(st,w){if(!w)return false;var n=st.length,t=tol(n);if(w.length<n-t)return false;
  for(var L=Math.max(1,n-1);L<=n+1;L++){if(L>w.length)break;if(lev(st,w.slice(0,L))<=t)return true}return false}
/* dopasowanie rdzenia na pozycji i: zwraca liczbę zużytych słów (1 albo 2 – nazwa rozbita przez dyktowanie) */
function at(st,W,i){if(hit(st,W[i]))return 1;if(i+1<W.length&&W[i].length<st.length&&hit(st,W[i]+W[i+1]))return 2;return 0}
function keys(s){return ph(s).split(' ').filter(function(w){return w&&!FILL[w]}).map(stem)}
function prep(list){
  if(list._k)return list._k;
  var items=[];list.g.forEach(function(g,gi){g.i.forEach(function(it){items.push({it:it,g:gi,kp:keys(it.kp||it.p),kl:keys(it.kl||it.l)})})});
  var hp={},hl={};items.forEach(function(x){hp[x.kp[0]]=1;hl[x.kl[0]]=1});
  list._k={items:items,hp:Object.keys(hp),hl:Object.keys(hl)};return list._k}
/* wszystkie wystąpienia ciągu rdzeni: kolejne słowa w oknie, przerwa, gdy pojawi się początek innej nazwy */
function findAll(K,W,heads){var res=[];
  for(var i=0;i<W.length;i++){var c=at(K[0],W,i);if(!c)continue;
    var j=i+c,k=1,lim=i+K.length+8,ok=true;
    while(k<K.length){var f=false;
      while(j<W.length&&j<=lim){var c2=at(K[k],W,j);if(c2){j+=c2;k++;f=true;break}
        if(heads.some(function(h){return h!==K[0]&&hit(h,W[j])})){j=W.length;break}j++}
      if(!f){ok=false;break}}
    if(ok)res.push([i,j-1])}
  return res}
function scan(list,text){var P=prep(list),W=ph(text).split(' ').filter(Boolean);
  return P.items.map(function(x){return{p:findAll(x.kp,W,P.hp),l:findAll(x.kl,W,P.hl)}})}
/* czy w trybie mieszanym po polskiej nazwie od razu padła łacińska (najwyżej 5 słów dalej) */
function pair(r){return r.p.some(function(a){return r.l.some(function(b){return b[0]>a[1]&&b[0]-a[1]<=5})})}
window.WYMATCH={ph:ph,keys:keys,scan:scan,pair:pair,prep:prep};
})();
