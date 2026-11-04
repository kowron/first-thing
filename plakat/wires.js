(function () {
  var MM = 96 / 25.4; var K = window.POSTER_K || 1;
  var COLORS = { purple: '#8f88d9', teal: '#3aa889', coral: '#d97a56', blue: '#5d9bd8', pink: '#d46f95',
                 red: '#d46a6a', green: '#7fae45', amber: '#d39a3a', indigo: '#6f7dc4',
                 c1: '#1f6f78', c2: '#a23b3b', c3: '#a8741a', c4: '#2f7d4a', root: '#1d2126' };
  function widthFor(p) {
    var c = p.classList;
    if (c.contains('root')) return 6 * K;
    if (c.contains('chap')) return 4.4 * K;
    if (c.contains('world')) return 3.4 * K;
    if (c.contains('grp') || c.contains('band')) return 2.6 * K;
    if (c.contains('sg')) return 2.2 * K;
    return 1.8 * K;
  }
  function draw(box) {
    var svg = box.querySelector('svg.wires');
    var c = box.getBoundingClientRect();
    svg.setAttribute('width', c.width);
    svg.setAttribute('height', c.height);
    svg.setAttribute('viewBox', '0 0 ' + c.width + ' ' + c.height);
    function R(el) {
      var r = el.getBoundingClientRect();
      return { l: r.left - c.left, t: r.top - c.top, r: r.right - c.left, b: r.bottom - c.top,
               cx: (r.left + r.right) / 2 - c.left, cy: (r.top + r.bottom) / 2 - c.top };
    }
    var out = '';
    function L(x1, y1, x2, y2, col, w) {
      out += '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2 + '" y2="' + y2 + '" stroke="' + col +
             '" stroke-width="' + w + '" stroke-linecap="round"/>';
    }
    box.querySelectorAll('.sub').forEach(function (sub) {
      var p = sub.querySelector(':scope > .node');
      var q = sub.querySelector(':scope > .q');
      var kids = sub.querySelector(':scope > .kids');
      if (!p || !kids) return;
      var col = COLORS[sub.dataset.c] || '#9aa1a8';
      var w = widthFor(p);
      if (kids.classList.contains('grid2')) {
        // dwie kolumny kart: pień pośrodku przerwy, odgałęzienia w lewo i w prawo
        var gcols = kids.querySelectorAll(':scope > .gcol');
        if (gcols.length < 2) return;
        var P2 = R(p), G0 = R(gcols[0]), G1 = R(gcols[1]);
        var tx = (G0.r + G1.l) / 2, sx2 = P2.cx, sy2 = P2.b;
        if (q) { var Q2 = R(q); L(P2.cx, P2.b, Q2.cx, Q2.t, col, w); sx2 = Q2.cx; sy2 = Q2.b; }
        var items = [];
        [0, 1].forEach(function (ci) {
          Array.prototype.forEach.call(gcols[ci].children, function (k) {
            var nd = k.classList.contains('sub') ? k.querySelector(':scope > .node') : k;
            if (!nd) return;
            var hh = nd.querySelector(':scope > .ch'), rk = R(nd);
            items.push({ x: ci === 0 ? rk.r : rk.l, y: hh ? R(hh).cy : Math.min(rk.cy, rk.t + 6 * MM * K) });
          });
        });
        if (!items.length) return;
        var maxy = Math.max.apply(null, items.map(function (i) { return i.y; }));
        if (Math.abs(sx2 - tx) > 0.5) { L(sx2, sy2, sx2, sy2 + 2 * MM, col, w); L(sx2, sy2 + 2 * MM, tx, sy2 + 2 * MM, col, w); sy2 += 2 * MM; }
        L(tx, sy2, tx, maxy, col, w);
        items.forEach(function (i) { L(tx, i.y, i.x, i.y, col, w); });
        return;
      }
      var kn = [], side = [];
      Array.prototype.forEach.call(kids.children, function (k) {
        if (k.classList.contains('kstack')) {
          var st = Array.prototype.map.call(k.querySelectorAll(':scope > .sub, :scope > .node'), function (x) {
            return x.classList.contains('sub') ? x.querySelector(':scope > .node') : x; }).filter(Boolean);
          if (st.length) { kn.push(st[0]); for (var si = 1; si < st.length; si++) side.push({ n: st[si], col: k }); }
        } else if (k.classList.contains('kwrap')) {
          k.querySelectorAll(':scope > .krow > .sub').forEach(function (s2) { kn.push(s2.querySelector(':scope > .node')); });
        } else if (k.classList.contains('sub')) { kn.push(k.querySelector(':scope > .node')); }
        else if (k.classList.contains('node')) { kn.push(k); }
      });
      kn = kn.filter(Boolean);
      if (!kn.length) return;
      var P = R(p);
      if (kids.classList.contains('row')) {
        var sx = P.cx, sy = P.b;
        if (q) { var Q = R(q); L(P.cx, P.b, Q.cx, Q.t, col, w); sx = Q.cx; sy = Q.b; }
        var KR = kn.map(R);
        var top = Math.min.apply(null, KR.map(function (k) { return k.t; }));
        var by = sy + (top - sy) / 2;
        L(sx, sy, sx, by, col, w);
        var xs = KR.map(function (k) { return k.cx; });
        var sideX = side.map(function (s) { return R(s.col).l - 2.4 * MM * K; });
        L(Math.min.apply(null, xs.concat([sx], sideX)), by, Math.max.apply(null, xs.concat([sx], sideX)), by, col, w);
        KR.forEach(function (k) { L(k.cx, by, k.cx, k.t, col, w); });
        side.forEach(function (s, i) {
          var N = R(s.n), x = sideX[i], hy = N.t + Math.min(N.b - N.t, 9 * MM * K) / 2;
          L(x, by, x, hy, col, w); L(x, hy, N.l, hy, col, w);
        });
      } else {
        var qn = q ? q.querySelector('.qn') : null;
        var x0 = qn ? R(qn).cx : P.l + 2.6 * MM * K;
        var ys = kn.map(function (k) {
          var h = k.querySelector(':scope > .ch');
          var rk = R(k);
          return { l: rk.l, y: h ? R(h).cy : rk.cy };
        });
        L(x0, P.b, x0, ys[ys.length - 1].y, col, w);
        ys.forEach(function (k) { L(x0, k.y, k.l, k.y, col, w); });
      }
    });
    svg.innerHTML = out;
  }
  function subBottom(el) {
    var mb = el.getBoundingClientRect().bottom;
    el.querySelectorAll('*').forEach(function (e) { var r = e.getBoundingClientRect(); if (r.height > 0 && r.bottom > mb) mb = r.bottom; });
    return mb;
  }
  function placeDocks(box) {
    var c = box.getBoundingClientRect();
    box.querySelectorAll(':scope > .dock').forEach(function (d) {
      var l = Infinity, r = -Infinity, b = -Infinity;
      d.dataset.under.split(',').forEach(function (id) {
        var el = document.getElementById(id.trim()); if (!el) return;
        var rr = el.getBoundingClientRect();
        l = Math.min(l, rr.left); r = Math.max(r, rr.right); b = Math.max(b, subBottom(el));
      });
      var gap = (+d.dataset.gap || 6) * MM * K;
      d.style.left = (l - c.left) + 'px'; d.style.top = (b - c.top + gap) + 'px'; d.style.width = (r - l) + 'px';
    });
  }
  function run() {
    document.querySelectorAll('.treebox').forEach(placeDocks);
    document.querySelectorAll('.treebox').forEach(draw);
    document.body.setAttribute('data-wired', '1');
  }
  if (document.fonts && document.fonts.ready) { document.fonts.ready.then(run); } else { window.addEventListener('load', run); }
})();
