/* Kolokwium 6 – transformacje wykonywane w przeglądarce przed drukiem.
   Uruchamiane przez build.mjs (page.evaluate). Nie edytuj, jeśli piszesz rozdział. */
(function () {
  'use strict';
  const W = [];
  const warn = (m) => W.push({ level: 'warn', msg: m });
  const info = (m) => W.push({ level: 'info', msg: m });
  const error = (m) => W.push({ level: 'error', msg: m });

  const LABELS = {
    liceum: 'To było w liceum', pojecie: 'Pojęcie', warto: 'Warto wiedzieć', poza: 'Poza Drewą · uzupełnienie',
    zapamietaj: 'Zapamiętaj', przyklad: 'Przykład', obraz: 'Obraz w głowie', uwaga: 'Uwaga do źródła',
    w60: 'W 60 sekund', numbers: 'Liczby do zapamiętania', quiz: 'Sprawdź się',
  };
  const NOTE_KINDS = ['liceum', 'pojecie', 'warto', 'poza'];
  const BOX_KINDS = ['zapamietaj', 'przyklad', 'obraz', 'uwaga', 'poza'];
  const PH = '00'; // zaślepka numeru strony w 1. przebiegu

  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const cssStr = (s) => '"' + String(s).replace(/\\/g, '\\\\').replace(/"/g, '\\"').replace(/\n/g, ' ') + '"';
  const plural = (n, one, few, many) =>
    n === 1 ? one : (n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 10 || n % 100 >= 20)) ? few : many;
  const txt = (el) => (el ? el.textContent.replace(/[\u00AD]/g, '').replace(/\s+/g, ' ').trim() : '');
  const where = (el) => {
    const sec = el.closest('section');
    const f = sec && (sec.dataset.srcFile || sec.id);
    const s = txt(el).slice(0, 50);
    return `${f ? '[' + f + '] ' : ''}<${el.tagName.toLowerCase()}${el.id ? ' id="' + el.id + '"' : ''}${el.className && typeof el.className === 'string' ? ' class="' + el.className + '"' : ''}>${s ? ' „' + s + '…”' : ''}`;
  };
  const html = (s) => { const t = document.createElement('template'); t.innerHTML = s.trim(); return t.content; };
  const stripNum = (n) => String(parseInt(n, 10));

  /* ------------------------------------------------------------------ */
  function prepare(opts) {
    const book = opts.book || {};
    const mode = opts.mode || 'full';
    const chapters = $$('section.chapter');
    const backs = $$('section.back');
    const fronts = $$('section.front');
    const stats = { chapters: chapters.length, figures: 0, liceum: 0, questions: 0, notes: 0, boxes: 0 };
    const outline = [];
    const sections = [];
    const answers = [];
    const notePairs = [];

    /* ---------- Rozdziały: id, otwarcie ---------- */
    const chNums = new Set();
    for (const ch of chapters) {
      const num = ch.dataset.num || '';
      if (!/^\d\d$/.test(num)) { error(`${where(ch)}: data-num musi mieć dwie cyfry (np. "03"), jest "${num}"`); continue; }
      if (chNums.has(num)) error(`Dwa rozdziały mają ten sam numer ${num}`);
      chNums.add(num);
      if (ch.id && ch.id !== 'c' + num) warn(`${where(ch)}: id rozdziału nadaje build („c${num}”), usuń id="${ch.id}"`);
      ch.id = 'c' + num;
      if (!ch.dataset.title) error(`Rozdział ${num}: brak data-title`);
    }

    /* ---------- Id: prefiksy i duplikaty ---------- */
    const seen = new Map();
    for (const el of $$('[id]')) {
      if (el.closest('svg') && el.closest('.k6-defs')) continue;
      const id = el.id;
      if (seen.has(id)) error(`Zduplikowane id="${id}": ${where(seen.get(id))} oraz ${where(el)}`);
      else seen.set(id, el);
      if (!/^[A-Za-z][\w-]*$/.test(id)) warn(`Niepoprawne id="${id}" (tylko litery, cyfry, - i _): ${where(el)}`);
      const ch = el.closest('section.chapter');
      if (ch && el !== ch && ch.dataset.num && !id.startsWith('c' + ch.dataset.num + '-')) {
        error(`id="${id}" w rozdziale ${ch.dataset.num} musi zaczynać się od „c${ch.dataset.num}-”: ${where(el)}`);
      }
      const bk = el.closest('section.back');
      if (bk && !id.startsWith('b-')) warn(`id="${id}" w części końcowej powinno zaczynać się od „b-”: ${where(el)}`);
    }
    // id wewnątrz SVG muszą być unikalne globalnie – już sprawdzone powyżej.

    /* ---------- Nagłówki h2: autoid ---------- */
    for (const ch of chapters) {
      const num = ch.dataset.num;
      let i = 0;
      for (const h of $$('h2', ch)) {
        i++;
        if (h.closest('.box, .quiz, .w60, figure, aside')) { warn(`${where(h)}: h2 wewnątrz ramki/ryciny – użyj h3 albo h4`); continue; }
        if (!h.id) h.id = `c${num}-h2-${i}`;
      }
      for (const h of $$('h1', ch)) error(`${where(h)}: nie używaj h1 w rozdziale (tytuł bierze się z data-title)`);
    }

    /* ---------- Ryciny ---------- */
    const figMap = {};
    let fn = 0;
    for (const f of $$('figure.fig')) {
      fn++;
      const sec = f.closest('section');
      const prefix = sec && sec.classList.contains('chapter') ? `c${sec.dataset.num}-` : 'b-';
      if (!f.id) { f.id = `${prefix}fig-auto-${fn}`; warn(`${where(f)}: rycina bez id – nadano „${f.id}” (odsyłacze wymagają stałego id)`); }
      else if (!/-fig-/.test(f.id)) info(`${where(f)}: zalecane id ryciny w formie „${prefix}fig-…”`);
      let title = f.dataset.title || '';
      if (!title) warn(`${where(f)}: rycina bez tytułu (atrybut data-title)`);
      const cap = $(':scope > figcaption', f);
      if (!cap || !txt(cap)) warn(`Ryc. ${fn} („${title || f.id}”): brak podpisu <figcaption>`);
      if (!$('svg, img', f)) warn(`Ryc. ${fn}: brak SVG ani obrazka w rycinie`);
      if (!$('.fig-label', f)) {
        f.prepend(html(`<div class="fig-label"><span class="fig-num">Ryc. ${fn}</span>${esc(title)}</div>`));
      }
      figMap[f.id] = { n: fn, title, ch: sec && sec.dataset.num };
      for (const p of $$('.panel', f)) {
        if ((p.dataset.badge || p.dataset.title) && !$(':scope > .panel-head', p)) {
          p.prepend(html(`<div class="panel-head">${p.dataset.badge ? `<span class="badge">${esc(p.dataset.badge)}</span>` : ''}${p.dataset.title ? `<span class="ptitle">${esc(p.dataset.title)}</span>` : ''}</div>`));
        }
      }
      if (sec && sec.classList.contains('chapter')) stats.figures++;
    }

    /* ---------- Notatki marginesowe ---------- */
    for (const n of $$('aside.note')) {
      const kind = NOTE_KINDS.find((k) => n.classList.contains(k));
      if (!kind) warn(`${where(n)}: notatka bez typu (dodaj klasę liceum / pojecie / warto / poza)`);
      const inLegend = n.closest('.legend');
      if (!inLegend && !(n.parentElement && n.parentElement.matches('section.chapter'))) {
        warn(`${where(n)}: notatka marginesowa musi być bezpośrednim dzieckiem <section class="chapter"> (nie wewnątrz akapitu, listy ani ramki)`);
      }
      if (n.closest('section.chapter') && !inLegend) {
        const nx = n.nextElementSibling;
        if (nx && nx.matches('h2')) warn(`${where(n)}: notatka stoi tuż przed h2 – przenieś ją za nagłówek, przed akapit, którego dotyczy`);
        stats.notes++;
        if (kind === 'liceum') stats.liceum++;
      }
      if (n.closest('section.chapter') && !inLegend) {
        if (!n.id) n.id = `k6-note-${notePairs.length + 1}`;
        let anc = n.nextElementSibling;
        while (anc && anc.matches('aside.note')) anc = anc.nextElementSibling;
        if (anc) {
          if (!anc.id) anc.id = `k6-anc-${notePairs.length + 1}`;
          notePairs.push({ note: n.id, anchor: anc.id, text: txt(n).slice(0, 40), file: n.closest('section').dataset.srcFile || '' });
        }
      }
      if ($(':scope > .lbl', n)) continue;
      const lbl = n.dataset.label || LABELS[kind] || 'Notatka';
      let head = `<span class="lbl">${esc(lbl)}</span>`;
      if (n.dataset.term) head += `<span class="term">${esc(n.dataset.term)}</span>`;
      n.prepend(html(head));
    }

    /* ---------- Ramki ---------- */
    for (const b of $$('.box')) {
      const kind = BOX_KINDS.find((k) => b.classList.contains(k));
      if (!kind) warn(`${where(b)}: ramka bez typu (zapamietaj / przyklad / obraz / uwaga / poza)`);
      if (b.closest('section.chapter')) stats.boxes++;
      if ($(':scope > .lbl', b)) continue;
      const lbl = b.dataset.title || LABELS[kind] || '';
      b.prepend(html(`<div class="lbl">${esc(lbl)}</div>`));
    }
    for (const b of $$('.w60')) {
      if ($(':scope > .lbl', b)) continue;
      const items = $$(':scope > ul > li, :scope > ol > li', b).length;
      if (b.closest('section.chapter') && (items < 3 || items > 6)) warn(`${where(b)}: „W 60 sekund” powinno mieć 3–6 punktów (jest ${items})`);
      b.prepend(html(`<div class="lbl"><svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="11" r="7.2" fill="none" stroke="#6cc7c9" stroke-width="1.8"/><path d="M10 11 L10 6.5 M7.5 1.8 h5" stroke="#6cc7c9" stroke-width="1.8" stroke-linecap="round"/></svg>${esc(b.dataset.title || LABELS.w60)}</div>`));
    }
    for (const b of $$('.numbers')) {
      if (!$(':scope > .grid', b)) {
        const g = document.createElement('div'); g.className = 'grid';
        for (const n of $$(':scope > .n', b)) g.appendChild(n);
        b.appendChild(g);
      }
      if (!$(':scope > .lbl', b)) b.prepend(html(`<div class="lbl">${esc(b.dataset.title || LABELS.numbers)}</div>`));
    }

    /* ---------- Sprawdź się ---------- */
    const keySection = $('section[data-auto="answers"]');
    for (const ch of chapters) {
      const num = ch.dataset.num;
      const quizzes = $$('.quiz', ch);
      if (quizzes.length > 1) warn(`Rozdział ${num}: więcej niż jeden blok „Sprawdź się” – zalecany jeden, na końcu rozdziału`);
      quizzes.forEach((q, qi) => {
        if (!q.id) q.id = `c${num}-quiz${qi ? '-' + (qi + 1) : ''}`;
        const items = $$(':scope > ol > li', q);
        if (!items.length) warn(`${where(q)}: blok „Sprawdź się” bez pytań (<ol><li>…)`);
        items.forEach((li, i) => {
          if (!li.id) { li.id = `c${num}-q-auto-${i + 1}`; warn(`Rozdział ${num}, pytanie ${i + 1}: brak id (nadano ${li.id})`); }
          const ans = $(':scope > .answer', li) || $('.answer', li);
          const clone = li.cloneNode(true);
          $$('.answer', clone).forEach((a) => a.remove());
          const qhtml = clone.innerHTML.trim();
          if (!ans) warn(`Rozdział ${num}, pytanie ${i + 1} (${li.id}): brak odpowiedzi <div class="answer">`);
          answers.push({ num, title: ch.dataset.title, qid: li.id, n: i + 1, q: qhtml, a: ans ? ans.innerHTML.trim() : '<p><i>(brak odpowiedzi)</i></p>' });
          if (ans) ans.remove();
          stats.questions++;
        });
        if (!$(':scope > .quiz-head', q)) {
          const c = items.length;
          q.prepend(html(`<div class="quiz-head"><span class="lbl">${LABELS.quiz}</span><span class="quiz-title">${esc(q.dataset.title || 'Pytania kontrolne')}</span><span class="quiz-count">${c} ${plural(c, 'pytanie', 'pytania', 'pytań')}</span></div>`));
        }
        if (keySection && !$(':scope > .quiz-foot', q)) {
          q.append(html(`<div class="quiz-foot">Odpowiedzi z krótkim uzasadnieniem: klucz odpowiedzi, <a class="pageref" href="#b-key-c${num}"></a></div>`));
        }
      });
    }

    /* ---------- Otwarcie rozdziału (po autoid h2 i rycinach) ---------- */
    for (const ch of chapters) {
      if ($(':scope > .opener', ch)) continue;
      const num = ch.dataset.num;
      const title = ch.dataset.title || '';
      const lead = $(':scope > p.lead', ch);
      if (!lead) warn(`Rozdział ${num}: brak leadu <p class="lead">`);
      const h2s = $$(':scope > h2', ch);
      const nf = $$('figure.fig', ch).length;
      const list = h2s.map((h) => esc(h.dataset.toc || txt(h))).join(' · ');
      const head = html(`<header class="opener"><div class="opener-num">${num}</div><div class="opener-body">${ch.dataset.kicker ? `<p class="opener-kicker">${esc(ch.dataset.kicker)}</p>` : ''}<h1 class="ch-title">${esc(title)}</h1><div class="lead-slot"></div><p class="opener-meta"><b>W rozdziale:</b> ${list}${list ? ' · ' : ''}<b>Ryciny:</b> ${nf}</p></div></header>`);
      ch.prepend(head);
      if (lead) $('.lead-slot', ch).replaceWith(lead); else $('.lead-slot', ch).remove();
      sections.push({ id: ch.id, kind: 'chapter', title: `${num} ${title}`, file: ch.dataset.srcFile || '' });
      outline.push({ id: ch.id, title: `${num} ${title}`, children: h2s.map((h) => ({ id: h.id, title: txt(h) })) });
    }

    /* ---------- Część końcowa: nagłówki ---------- */
    const backOrder = [];
    for (const b of backs) {
      const title = b.dataset.title || '';
      if (!title) error(`${where(b)}: sekcja końcowa bez data-title`);
      if (!b.id) b.id = 'b-' + title.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/ł/g, 'l').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
      if (!$(':scope > .back-head', b) && !b.classList.contains('no-head')) {
        b.prepend(html(`<header class="back-head"><p class="kicker">${esc(b.dataset.kicker || 'Na koniec')}</p><h1>${esc(title)}</h1></header>`));
      }
      backOrder.push(b);
      sections.push({ id: b.id, kind: 'back', title, file: b.dataset.srcFile || '' });
    }
    for (const f of fronts) {
      if (!f.id) error(`${where(f)}: sekcja przednia bez id`);
      sections.push({ id: f.id, kind: 'front', title: f.dataset.title || txt($('h1', f)), file: f.dataset.srcFile || '' });
    }

    /* ---------- Klucz odpowiedzi ---------- */
    if (keySection) {
      const groups = {};
      for (const a of answers) (groups[a.num] = groups[a.num] || []).push(a);
      let out = `<p class="intro">Odpowiedzi do bloków „Sprawdź się” z końca każdego rozdziału. Najpierw spróbuj odpowiedzieć sam – numer strony obok rozdziału prowadzi z powrotem do pytań.</p>`;
      const nums = Object.keys(groups).sort();
      if (!nums.length) out += `<p class="intro"><i>Brak pytań kontrolnych w rozdziałach.</i></p>`;
      for (const num of nums) {
        const g = groups[num];
        out += `<div class="key-ch" id="b-key-c${num}"><h2><span class="n">${num}</span>${esc(g[0].title || '')}<span class="p">pytania: <a class="pageref" href="#c${num}-quiz"></a></span></h2><div class="key-list">`;
        for (const a of g) {
          out += `<div class="key-item"><span class="qn">${a.n}</span><div><div class="qtext">${a.q} <a class="pageref" href="#${a.qid}"></a></div>${a.a}</div></div>`;
        }
        out += `</div></div>`;
      }
      keySection.append(html(out));
    }

    /* ---------- Spis rycin ---------- */
    const figSec = $('section[data-auto="figures"]');
    if (figSec) {
      let out = '<div class="figlist">';
      for (const [id, f] of Object.entries(figMap)) {
        out += `<a href="#${id}"><span class="n">Ryc. ${f.n}</span><span class="t">${esc(f.title)}</span><span class="p" data-page-of="${id}">${PH}</span></a>`;
      }
      out += '</div>';
      if (!Object.keys(figMap).length) out = '<p class="intro"><i>Brak rycin.</i></p>';
      figSec.append(html(out));
    }

    /* ---------- Źródła ---------- */
    const srcSec = $('section[data-auto="sources"]');
    if (srcSec) {
      let out = '';
      if (book.sourcesIntro) out += `<p class="intro">${book.sourcesIntro}</p>`;
      out += '<ol class="sources">';
      (book.sources || []).forEach((s, i) => {
        out += `<li><span class="k">[${i + 1}]</span><span><b>${esc(s.key)}</b> – ${s.html}${s.note ? ` <span class="note">${s.note}</span>` : ''}</span></li>`;
      });
      out += '</ol>';
      // strony cytowane w rozdziałach (z linii .src)
      const rows = [];
      for (const ch of chapters) {
        const parts = [];
        for (const s of $$('.src', ch)) {
          for (const part of txt(s).replace(/^Źródł(o|a)\s*:\s*/i, '').split(/\s*·\s*/)) if (part) parts.push(part);
        }
        const items = mergeSources(parts);
        rows.push(`<tr><td>${ch.dataset.num} ${esc(ch.dataset.title || '')}</td><td>${items.map(esc).join(' · ') || '–'}</td></tr>`);
      }
      if (rows.length) out += `<h2>Strony źródeł cytowane w rozdziałach</h2><table class="tbl wide cited"><thead><tr><th style="width:38%">Rozdział</th><th>Źródła (zebrane z linii „Źródło” pod podrozdziałami)</th></tr></thead><tbody>${rows.join('')}</tbody></table>`;
      if (book.sourcesNote) out += `<p class="intro">${book.sourcesNote}</p>`;
      srcSec.append(html(out));
    }

    /* ---------- Spis treści ---------- */
    const toc = $('section[data-auto="toc"]');
    if (toc) {
      let out = '<div class="toc-cols">';
      for (const ch of chapters) {
        out += `<div class="toc-ch"><a href="#${ch.id}"><span class="n">${ch.dataset.num}</span><span class="t">${esc(ch.dataset.title || '')}</span><span class="p" data-page-of="${ch.id}">${PH}</span></a></div>`;
        for (const h of $$(':scope > h2', ch)) {
          out += `<div class="toc-sec"><a href="#${h.id}"><span class="t">${esc(h.dataset.toc || txt(h))}</span><span class="p" data-page-of="${h.id}">${PH}</span></a></div>`;
        }
      }
      if (backOrder.length) {
        out += '<div class="toc-end">NA KONIEC</div>';
        for (const b of backOrder) {
          out += `<div class="toc-ch toc-back"><a href="#${b.id}"><span class="n">·</span><span class="t">${esc(b.dataset.title)}</span><span class="p" data-page-of="${b.id}">${PH}</span></a></div>`;
        }
      }
      out += '</div>';
      toc.append(html(out));
    }

    /* ---------- Odsyłacze ---------- */
    const ids = new Set($$('[id]').map((e) => e.id));
    for (const a of $$('a.figref, a.pageref, a.chapref')) {
      const href = a.getAttribute('href') || '';
      const id = href.replace(/^#/, '');
      const cls = a.classList.contains('figref') ? 'figref' : a.classList.contains('chapref') ? 'chapref' : 'pageref';
      const ok = href.startsWith('#') && ids.has(id);
      if (!ok) {
        const other = /^c(\d\d)-?/.exec(id);
        if (mode === 'only' && other && other[1] !== opts.only) info(`Odsyłacz do innego rozdziału (#${id}) – w podglądzie pojedynczego rozdziału pokazany jako „?”: ${where(a)}`);
        else { warn(`Odsyłacz do nieistniejącego id „${href}”: ${where(a)}`); a.classList.add('broken'); }
        a.textContent = cls === 'figref' ? 'ryc.\u00A0?' : cls === 'chapref' ? 'rozdz.\u00A0?' : 's.\u00A0?';
        continue;
      }
      const cap = a.classList.contains('cap');
      if (cls === 'figref') {
        const f = figMap[id];
        if (!f) { warn(`figref wskazuje na element, który nie jest ryciną (#${id}): ${where(a)}`); a.textContent = 'ryc.\u00A0?'; continue; }
        a.textContent = `${cap ? 'Ryc.' : 'ryc.'}\u00A0${f.n}${a.dataset.panel ? '\u00A0' + a.dataset.panel : ''}`;
      } else if (cls === 'chapref') {
        const t = document.getElementById(id);
        if (!t.matches('section.chapter')) { warn(`chapref powinien wskazywać rozdział (#c03), a wskazuje #${id}: ${where(a)}`); }
        const n = t.dataset.num ? stripNum(t.dataset.num) : '?';
        a.innerHTML = `${cap ? 'Rozdz.' : 'rozdz.'}\u00A0${n} (s.\u00A0<span data-page-of="${id}">${PH}</span>)`;
      } else {
        a.innerHTML = `${cap ? 'S.' : 's.'}\u00A0<span data-page-of="${id}">${PH}</span>`;
      }
    }
    for (const a of $$('a[href^="#"]')) {
      if (a.closest('.ghost-links')) continue;
      const id = a.getAttribute('href').slice(1);
      if (id && !ids.has(id) && !a.classList.contains('broken') && !(mode === 'only' && /^c\d\d/.test(id))) {
        warn(`Link do nieistniejącego id „#${id}”: ${where(a)}`);
      }
    }

    /* ---------- Statystyki na okładce ---------- */
    for (const el of $$('[data-stat]')) {
      const v = stats[el.dataset.stat];
      if (v === undefined) { warn(`Nieznana statystyka data-stat="${el.dataset.stat}"`); continue; }
      el.textContent = String(v);
    }
    for (const el of $$('[data-stat-label]')) {
      const [key, forms] = el.dataset.statLabel.split(':');
      const [a, b, c] = (forms || '').split('|');
      const v = stats[key] || 0;
      el.textContent = plural(v, a, b || a, c || b || a);
    }

    /* ---------- Front: konspekt ---------- */
    const frontOutline = fronts.map((f) => ({ id: f.id, title: f.dataset.title || txt($('h1', f)) }));
    const backOutline = backOrder.map((b) => ({ id: b.id, title: b.dataset.title }));

    /* ---------- Ściąga: kotwice punktów (do wyrównania kolumn na ostatniej stronie) ---------- */
    let cu = 0;
    for (const u of $$('.cheat-cols > .cheat-block > :not(ul), .cheat-cols > .cheat-block > ul > li')) {
      if (!u.id) u.id = `b-k6cu-${++cu}`;
      u.dataset.k6cu = '1';
    }

    /* ---------- Ukryte linki (dla numerów stron) ---------- */
    const need = new Set();
    for (const u of $$('[data-k6cu]')) need.add(u.id);
    for (const el of $$('[data-page-of]')) need.add(el.dataset.pageOf);
    for (const s of sections) need.add(s.id);
    for (const o of outline) for (const c of o.children) need.add(c.id);
    for (const id of Object.keys(figMap)) need.add(id);
    for (const a of answers) need.add(a.qid);
    for (const np of notePairs) { need.add(np.note); need.add(np.anchor); }
    const gl = document.createElement('div'); gl.className = 'ghost-links'; gl.setAttribute('aria-hidden', 'true');
    for (const id of need) if (id && document.getElementById(id)) { const a = document.createElement('a'); a.href = '#' + id; a.textContent = '.'; gl.appendChild(a); }
    document.body.prepend(gl);

    /* ---------- Typografia: twarde spacje + dzielenie wyrazów ---------- */
    typography();

    /* ---------- Reguły @page ---------- */
    let css = `@page { @top-left { content: ${cssStr(book.header || '')}; } @bottom-left { content: ${cssStr(book.footer || '')}; } }\n`;
    for (const ch of chapters) {
      const num = ch.dataset.num;
      css += `#${ch.id} { page: ch${num}; }\n@page ch${num} { @top-right { content: ${cssStr(num + ' ' + (ch.dataset.short || ch.dataset.title || ''))}; } }\n`;
    }
    for (const b of backOrder) {
      const pn = 'bk-' + b.id.replace(/[^\w-]/g, '');
      css += `#${b.id} { page: ${pn}; }\n@page ${pn} { @top-right { content: ${cssStr(b.dataset.short || b.dataset.title || '')}; } }\n`;
    }
    const st = document.createElement('style'); st.id = 'k6-pages'; st.textContent = css;
    document.head.appendChild(st);

    return {
      warnings: W, stats, sections, notePairs,
      outline: { front: frontOutline, chapters: outline, back: backOutline },
      figures: Object.entries(figMap).map(([id, f]) => ({ id, ...f })),
      hasCover: !!$('section.cover'),
    };
  }

  /* „Drewa s. 712–713” + „Drewa s. 713–715” -> „Drewa s. 712–715” */
  function mergeSources(parts) {
    const groups = new Map();
    const other = [];
    for (const p of parts) {
      const m = /^(.*?)\s*s\.\s*([\d\s,–-]+)$/.exec(p);
      if (!m) { if (!other.includes(p)) other.push(p); continue; }
      const key = m[1].trim();
      const g = groups.get(key) || [];
      for (const r of m[2].split(/\s*,\s*/)) {
        const mm = /^(\d+)(?:\s*[–-]\s*(\d+))?$/.exec(r.trim());
        if (mm) g.push([+mm[1], +(mm[2] || mm[1])]);
      }
      groups.set(key, g);
    }
    const out = [];
    for (const [key, g] of groups) {
      g.sort((a, b) => a[0] - b[0]);
      const merged = [];
      for (const r of g) {
        const last = merged[merged.length - 1];
        if (last && r[0] <= last[1] + 1) last[1] = Math.max(last[1], r[1]);
        else merged.push([...r]);
      }
      out.push(`${key} s. ${merged.map(([a, b]) => (a === b ? `${a}` : `${a}–${b}`)).join(', ')}`);
    }
    return out.concat(other);
  }

  /* Ściąga: Chromium w druku wypełnia kolumny po kolei także na ostatniej stronie (column-fill: balance
     działa tylko dla bloku wielokolumnowego, który nie dzieli się między strony). Po pierwszym przebiegu
     znamy strony punktów ściągi: wszystko od pierwszego punktu ostatniej strony przenosimy do nowego
     kontenera .cheat-cols.cheat-cols-last (od nowej strony) – ten już się nie dzieli, więc Chromium
     wyrównuje jego kolumny. Blok przecięty stroną dzielimy na dwa (druga część bez nagłówka – tak jak
     wyglądała dotąd). pageOf: id -> numer strony. */
  function balanceColumns(pageOf) {
    let changed = 0;
    const moveFrom = (node, target) => { for (let n = node; n;) { const nx = n.nextSibling; target.appendChild(n); n = nx; } };
    for (const cols of $$('.cheat-cols:not(.cheat-cols-last)')) {
      const units = $$('[data-k6cu]', cols).filter((u) => pageOf[u.id]);
      if (!units.length) continue;
      const pages = units.map((u) => pageOf[u.id]);
      const last = Math.max(...pages);
      if (last === Math.min(...pages)) continue;
      const u = units.find((x) => pageOf[x.id] === last);
      const blk = u.closest('.cheat-block');
      let start = blk;
      if (u !== $('[data-k6cu]', blk)) {
        const b2 = blk.cloneNode(false);
        b2.removeAttribute('id');
        b2.classList.add('cheat-cont');
        const h = $(':scope > h3', blk);
        if (h) b2.dataset.cont = [...h.childNodes].map((n) => n.textContent.trim()).filter(Boolean).join(' ');
        if (u.matches('li')) {
          const ul = u.parentElement;
          const ul2 = ul.cloneNode(false);
          moveFrom(u, ul2);
          b2.appendChild(ul2);
          if (ul.nextSibling) moveFrom(ul.nextSibling, b2);
        } else {
          moveFrom(u, b2);
        }
        blk.after(b2);
        start = b2;
      }
      const c2 = cols.cloneNode(false);
      c2.removeAttribute('id');
      c2.classList.add('cheat-cols-last');
      moveFrom(start, c2);
      cols.after(c2);
      changed++;
    }
    return changed;
  }

  /* ------------------------------------------------------------------ */
  function applyPages(map) {
    const missing = new Set();
    for (const el of $$('[data-page-of]')) {
      const p = map[el.dataset.pageOf];
      if (p === undefined) missing.add(el.dataset.pageOf);
      el.textContent = p === undefined ? '?' : String(p);
    }
    return [...missing];
  }

  /* ---------- Typografia ------------------------------------------------ */
  const NO_TYPO = 'svg, code, pre, script, style, .mono, .seq, .ghost-links, .k6-defs';
  const NO_HYPH = NO_TYPO + ', h1, h2, h3, h4, .lbl, table, .toc-cols, .figlist, .fig-label, .src, .fig-src, a.figref, a.pageref, a.chapref, .numbers .v, .ptitle, section.cover, .opener-meta, .opener-kicker, dt, .nohyph, .quiz-head, .key-ch h2, .badge';
  const SINGLE = /(^|[\s\u00A0(„"'–—\/])([aiouwzAIOUWZ])[ \t\n\r]+/g;
  const UNITS = /(\d)[ \t\n\r]+(%|‰|°C|°|pz|kpz|Mpz|kb|Mb|bp|kDa|Da|nt|nm|µm|mm|cm|m|ml|µl|μl|l|mg|µg|μg|ng|pg|g|kg|V|mA|W|h|min|s|M|mM|µM|μM|pmol|rpm|×|x|cykli|cykle|cykl|razy|tys\.|mln|kopii|zasad|nukleotydów|aminokwasów|pz\.)(?=[\s\u00A0.,;:)\]–]|$)/g;
  const ABBR = /(^|[\s\u00A0(])(s\.|nr|rozdz\.|ryc\.|tab\.|pkt|ok\.|np\.|tzw\.|tj\.|ang\.|łac\.|wg|zob\.|por\.)[ \t\n\r]+/g;
  const DASH = /[ \t\n\r]+([–—])/g;

  function typography() {
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null);
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    for (const t of nodes) {
      const p = t.parentElement;
      if (!p || p.closest(NO_TYPO)) continue;
      let s = t.nodeValue;
      if (!s.trim()) continue;
      s = s.replace(SINGLE, '$1$2\u00A0').replace(SINGLE, '$1$2\u00A0');
      s = s.replace(UNITS, '$1\u00A0$2');
      s = s.replace(ABBR, '$1$2\u00A0');
      s = s.replace(DASH, '\u00A0$1');
      if (!p.closest(NO_HYPH) && p.closest('section.chapter, section.back, section.front')) {
        s = s.replace(/[\p{L}]+/gu, hyphenateWord);
      }
      if (s !== t.nodeValue) t.nodeValue = s;
    }
  }

  /* Dzielenie wyrazów po polsku – sylabizacja regułowa (bez słownika).
     Zasady: nie dzielimy dwuznaków (ch cz dz dź dż rz sz), „i” zmiękczające idzie
     ze spółgłoską, nie dzielimy między samogłoskami, grupę spółgłosek dzielimy
     przed ostatnią spółgłoską, ale „spółgłoska + r/l/ł/w/j” zostaje razem
     (elek-tro, se-kwen-cja). Min. 2 litery przed i 2 po dzieleniu, słowa ≥ 6 liter. */
  const VOWELS = 'aąeęioóuy';
  const DIGR = ['ch', 'cz', 'dz', 'dź', 'dż', 'rz', 'sz'];
  const OBSTR = /^(p|b|t|d|k|g|f|w|ch|c|s|z|ś|ź|sz|cz|dz|ż|rz|h)$/;
  function hyphenateWord(w) {
    if (w.length < 6) return w;
    if (/[A-ZĄĆĘŁŃÓŚŹŻ]/.test(w.slice(1))) return w; // skróty, CamelCase
    const lw = w.toLowerCase();
    const u = [];
    for (let i = 0; i < lw.length;) {
      const two = lw.substr(i, 2);
      if (DIGR.includes(two)) { u.push({ s: two, v: false, i }); i += 2; continue; }
      u.push({ s: lw[i], v: VOWELS.includes(lw[i]), i, soft: false }); i++;
    }
    for (let k = 1; k < u.length - 1; k++) {
      if (u[k].s === 'i' && u[k + 1].v && !u[k - 1].v) { u[k].v = false; u[k].soft = true; }
    }
    const nuc = []; u.forEach((x, k) => { if (x.v) nuc.push(k); });
    if (nuc.length < 2) return w;
    const breaks = [];
    for (let j = 0; j < nuc.length - 1; j++) {
      const a = nuc[j], b = nuc[j + 1];
      let end = b - 1;
      if (end > a && u[end].soft) end--;          // „ni”, „ci”, „si”… idą razem
      const cons = end - a;                        // liczba spółgłosek (bez „i” zmiękczającego)
      if (cons <= 0) continue;                     // samogłoska–samogłoska: nie dzielimy
      let at = end;
      if (cons >= 2) {
        const last = u[end].s, prev = u[end - 1].s;
        if (last === 'j' || (/^(r|l|ł|w)$/.test(last) && OBSTR.test(prev) && prev !== last)) at = end - 1;
      }
      const ci = u[at].i;
      if (ci >= 2 && w.length - ci >= 2) breaks.push(ci);
    }
    if (!breaks.length) return w;
    let out = '', last = 0;
    for (const c of breaks) { out += w.slice(last, c) + '\u00AD'; last = c; }
    return out + w.slice(last);
  }

  /* ---------- Kontrole układu (w widoku ekranowym o szerokości pola zadruku) ---------- */
  function measure() {
    const M = [];
    const wide = '.opener, figure.fig:not(.narrow), .wide, table.tbl.wide, .numbers.wide, .box.wide, .quiz, aside.note, .w60.wide, .ghost-links, .k6-defs';
    for (const sec of $$('section.chapter, section.back, section.front')) {
      const r0 = sec.getBoundingClientRect();
      const cs = getComputedStyle(sec);
      const fullRight = r0.left + sec.offsetWidth;
      const mainRight = r0.right - parseFloat(cs.paddingRight);
      const reported = new Set();
      for (const el of $$('*', sec)) {
        if (el.closest('svg') && el.tagName.toLowerCase() !== 'svg') continue;
        if (el.closest('.ghost-links, .answer')) continue;
        const r = el.getBoundingClientRect();
        if (!r.width) continue;
        const top = el.closest('section > *') || el;
        if (reported.has(top)) continue;
        if (r.right > fullRight + 1.5) {
          M.push({ level: 'warn', msg: `Element wystaje poza pole zadruku o ${((r.right - fullRight) * 0.75).toFixed(1)} pt: ${where(el)}` });
          reported.add(top); continue;
        }
        if (sec.classList.contains('chapter') && !el.closest(wide) && r.right > mainRight + 1.5) {
          M.push({ level: 'warn', msg: `Element wchodzi na kolumnę marginesową o ${((r.right - mainRight) * 0.75).toFixed(1)} pt (dodaj klasę wide albo zmniejsz): ${where(el)}` });
          reported.add(top);
        }
      }
    }
    // tekst w SVG: minimalny rozmiar po wydruku, wyjście poza viewBox
    let fi = 0;
    for (const f of $$('figure.fig')) {
      fi++;
      for (const svg of $$('svg', f)) {
        const vb = svg.viewBox && svg.viewBox.baseVal;
        if (!vb || !vb.width) { M.push({ level: 'warn', msg: `Ryc. ${fi}: <svg> bez viewBox – nie da się go skalować` }); continue; }
        const sr = svg.getBoundingClientRect();
        const scale = sr.width / vb.width;
        let min = Infinity, minTxt = '';
        let outside = '';
        for (const t of $$('text', svg)) {
          if (!t.textContent.trim()) continue;
          const fs = parseFloat(getComputedStyle(t).fontSize) * scale * 0.75;
          if (fs < min) { min = fs; minTxt = t.textContent.trim().slice(0, 30); }
          const tr = t.getBoundingClientRect();
          if (!outside && tr.width && (tr.left < sr.left - 2 || tr.top < sr.top - 2 || tr.right > sr.right + 2 || tr.bottom > sr.bottom + 2)) outside = t.textContent.trim().slice(0, 30);
        }
        if (min < 7.3) M.push({ level: 'warn', msg: `Ryc. ${fi}: tekst w SVG ma po wydruku tylko ${min.toFixed(1)} pt („${minTxt}”) – minimum 7,5 pt (font-size ≥ 10 przy viewBox 640)` });
        if (outside) M.push({ level: 'warn', msg: `Ryc. ${fi}: tekst „${outside}” wychodzi poza viewBox SVG (zostanie ucięty lub wejdzie na podpis)` });
      }
    }
    return M;
  }

  /* Po ustaleniu łamania: miękkie łączniki (U+00AD), na których wiersz faktycznie się łamie,
     zamieniamy na zwykły dywiz (U+2010 w Inter, „-” w Source Serif), a pozostałe usuwamy – w warstwie
     tekstowej PDF nie zostają niewidoczne znaki utrudniające wyszukiwanie i kopiowanie.
     Wywoływać w widoku ekranowym (te same szerokości co w druku – zob. @media screen w style.css).
     Oryginalne wartości węzłów zostają w FROZEN, żeby build mógł cofnąć/powtórzyć zamrożenie
     pojedynczych akapitów (refreezeHyphens), gdy kontrola wykaże różnicę z drukiem. */
  const SHY = '\u00AD';
  const FROZEN = new Map(); // węzeł tekstowy -> { orig: tekst z U+00AD sprzed zamrożenia, n: liczba przeniesień }
  const FREEZE_BLOCK = 'p, li, td, th, dd, dt, figcaption, blockquote, h1, h2, h3, h4, .lbl, aside, div';
  function freezeNodes(nodes) {
    const range = document.createRange();
    const plan = [];
    let broken = 0;
    for (const t of nodes) {
      const s = t.nodeValue;
      // Chromium rysuje przeniesienie znakiem U+2010, jeśli czcionka go ma (Inter), inaczej U+002D (Source Serif)
      const hy = /Source Serif/.test(getComputedStyle(t.parentElement).fontFamily.split(',')[0]) ? '-' : '\u2010';
      let out = '', n = 0;
      const segs = [];
      for (let i = 0; i < s.length; i++) {
        const c = s[i];
        if (c !== SHY) { out += c; continue; }
        let isBreak = false;
        if (i > 0 && i + 1 < s.length) {
          range.setStart(t, i - 1); range.setEnd(t, i);
          const a = range.getClientRects();
          range.setStart(t, i + 1); range.setEnd(t, i + 2);
          const b = range.getClientRects();
          if (a.length && b.length && Math.abs(b[b.length - 1].top - a[a.length - 1].top) > 2) isBreak = true;
        }
        if (isBreak) { segs.push(out); out = ''; broken++; n++; }
      }
      segs.push(out);
      plan.push([t, segs, hy]);
    }
    // Dywiz wstawiamy w osobnym <span class="k6-hy"> (font-kerning: none): miękki łącznik Chromium rysuje
    // bez kerningu z poprzednią literą, a zwykły dywiz w tym samym ciągu tekstu byłby kerningowany
    // (np. „e-” w Source Serif szersze o ok. 0,3 px) – wiersz „na styk” przestałby się mieścić.
    // Span nie dodaje znaków do warstwy tekstowej PDF.
    for (const [t, segs, hy] of plan) {
      const parts = [t];
      const orig = t.nodeValue;
      t.nodeValue = segs[0];
      let at = t;
      for (let k = 1; k < segs.length; k++) {
        const sp = document.createElement('span');
        sp.className = 'k6-hy';
        sp.textContent = hy;
        const tx = document.createTextNode(segs[k]);
        at.after(sp, tx);
        parts.push(sp, tx);
        at = tx;
      }
      FROZEN.set(t, { orig, n: segs.length - 1, parts });
    }
    return broken;
  }
  function shyNodes(root, skipSel) {
    const walker = document.createTreeWalker(root || document.body, NodeFilter.SHOW_TEXT, null);
    const nodes = [];
    while (walker.nextNode()) {
      const t = walker.currentNode;
      if (t.nodeValue.includes(SHY) && !(t.parentElement && t.parentElement.closest(skipSel || '#k6-none'))) nodes.push(t);
    }
    return nodes;
  }
  function freezeHyphens(skipSel) {
    const nodes = shyNodes(document.body, skipSel);
    return { nodes: nodes.length, broken: freezeNodes(nodes) };
  }

  /* Naprawa po kontroli: segments = fragmenty wierszy (z pdftotext) ze stron, na których zamrożony
     druk różni się od druku z U+00AD. Znajduje zamrożone akapity zawierające te fragmenty,
     przywraca w nich U+00AD i – przy kolejnych próbach dla tego samego akapitu:
       1. zamraża go ponownie przy wierszu węższym o 0,15 px, 2. szerszym o 0,05 px
          (remis „na styk” rozstrzyga się wtedy jak w druku),
       3. zostawia w nim U+00AD (wariant awaryjny: tylko ten akapit ma miękkie łączniki).
     Zwraca opisy akapitów zamrożonych ponownie (refrozen) i zostawionych z U+00AD (shy). */
  const TRIES = new WeakMap();
  function refreezeHyphens(segments) {
    const squash = (s) => s.replace(/[\s\u00A0\u00AD\u2010\u2011-]+/g, '');
    const segs = segments.map(squash).filter((s) => s.length >= 12);
    const blocks = new Map();
    for (const t of FROZEN.keys()) {
      if (!t.isConnected) continue;
      const el = t.parentElement && t.parentElement.closest(FREEZE_BLOCK);
      if (el && !blocks.has(el)) blocks.set(el, squash(el.textContent));
    }
    // najmniejsze pasujące elementy (akapit, a nie cały rozdział)
    let hit = [...blocks.entries()].filter(([, txt]) => segs.some((s) => txt.includes(s))).map(([el]) => el);
    hit = hit.filter((el) => !hit.some((o) => o !== el && el.contains(o)));
    let broken = 0;
    const refrozen = [], shy = [];
    for (const el of hit) {
      const tries = (TRIES.get(el) || 0) + 1;
      TRIES.set(el, tries);
      const D = [0.15, -0.05][tries - 1];
      const nodes = [];
      for (const [t, f] of FROZEN) {
        if (!t.isConnected || !el.contains(t)) continue;
        t.nodeValue = f.orig;
        for (const p of f.parts.slice(1)) p.remove();
        broken -= f.n;
        nodes.push(t);
      }
      for (const t of nodes) FROZEN.delete(t);
      if (D === undefined || el.matches('td, th')) { shy.push(where(el)); continue; }
      refrozen.push(where(el));
      const prev = el.style.marginRight;
      el.style.marginRight = `${(parseFloat(getComputedStyle(el).marginRight) || 0) + D}px`;
      broken += freezeNodes(nodes);
      el.style.marginRight = prev;
    }
    return { refrozen, shy, broken };
  }

  window.K6 = { prepare, applyPages, balanceColumns, measure, hyphenateWord, freezeHyphens, refreezeHyphens };
})();
