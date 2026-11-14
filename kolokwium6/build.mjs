#!/usr/bin/env node
/* Kolokwium 6 – składanie PDF (natywny druk Chromium + pypdf).
 *
 *   node build.mjs                 całość  -> ./<book.output>.pdf
 *   node build.mjs --only 03       jeden rozdział (+ klucz odpowiedzi) -> <buildDir>/rozdzial-03.pdf
 *   node build.mjs --demo          całość z rozdziałem 00-demo -> <buildDir>/demo.pdf
 *   node build.mjs --png ...       dodatkowo PNG stron (96 dpi) w <buildDir>/<nazwa>-png/
 *   --out-dir DIR                  inny katalog roboczy (albo zmienna K6_BUILD_DIR)
 *   --keep                         zostaw złożony HTML i PDF-y pośrednie
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { execFileSync } from 'node:child_process';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const ROOT = path.dirname(fileURLToPath(import.meta.url));
const T0 = Date.now();

/* ---------- argumenty ---------- */
const argv = process.argv.slice(2);
const opt = { only: null, png: false, demo: false, outDir: null, keep: false };
for (let i = 0; i < argv.length; i++) {
  const a = argv[i];
  if (a === '--only') opt.only = String(argv[++i] || '').padStart(2, '0');
  else if (a.startsWith('--only=')) opt.only = a.slice(7).padStart(2, '0');
  else if (a === '--png') opt.png = true;
  else if (a === '--demo') opt.demo = true;
  else if (a === '--out-dir') opt.outDir = argv[++i];
  else if (a === '--keep') opt.keep = true;
  else if (a === '--help' || a === '-h') { console.log(fs.readFileSync(fileURLToPath(import.meta.url), 'utf8').split('\n').slice(1, 11).join('\n')); process.exit(0); }
  else { console.error(`Nieznana opcja: ${a}`); process.exit(2); }
}
if (opt.only !== null && !/^\d\d$/.test(opt.only)) { console.error('--only wymaga numeru rozdziału, np. --only 03'); process.exit(2); }
const mode = opt.only ? 'only' : opt.demo ? 'demo' : 'full';

const book = JSON.parse(fs.readFileSync(path.join(ROOT, 'book.json'), 'utf8'));
let buildDir = opt.outDir || process.env.K6_BUILD_DIR || book.buildDir || path.join(ROOT, 'build');
try { fs.mkdirSync(buildDir, { recursive: true }); fs.accessSync(buildDir, fs.constants.W_OK); }
catch { buildDir = path.join(ROOT, 'build'); fs.mkdirSync(buildDir, { recursive: true }); }

const tag = mode === 'only' ? `rozdzial-${opt.only}` : mode === 'demo' ? 'demo' : 'pelny';
const finalPdf = mode === 'full' ? path.join(ROOT, book.output) : path.join(buildDir, `${tag}.pdf`);
const tmpHtml = path.join(buildDir, `${tag}.tmp.html`);
const passPdf = path.join(buildDir, `${tag}.pass.pdf`);
const metaJson = path.join(buildDir, `${tag}.meta.json`);
const checkDir = path.join(buildDir, `${tag}-check`);
const pngDir = path.join(buildDir, `${tag}-png`);
const PDFTOOL = path.join(ROOT, 'lib', 'pdftool.py');

const W = []; // {level, msg}
const log = (s) => console.log(s);

/* ---------- pliki źródłowe ---------- */
const rd = (p) => fs.readFileSync(path.join(ROOT, p), 'utf8');
const listDir = (d, re) => (fs.existsSync(path.join(ROOT, d)) ? fs.readdirSync(path.join(ROOT, d)).filter((f) => re.test(f)).sort() : []);
const tagFile = (html, rel) => html.replace(/<section\b/, `<section data-src-file="${rel}"`);

let chapterFiles = listDir('chapters', /^\d\d-[\w.-]*\.html$/);
const strayChapters = listDir('chapters', /\.html$/).filter((f) => !chapterFiles.includes(f));
for (const f of strayChapters) W.push({ level: 'warn', msg: `Pominięto chapters/${f}: nazwa musi mieć postać NN-nazwa.html (np. 03-elektroforeza-bialek.html)` });
if (mode === 'full') chapterFiles = chapterFiles.filter((f) => !f.startsWith('00-'));
if (mode === 'only') {
  chapterFiles = chapterFiles.filter((f) => f.startsWith(opt.only + '-'));
  if (!chapterFiles.length) { console.error(`Brak pliku chapters/${opt.only}-*.html`); process.exit(2); }
}
const chapters = chapterFiles.map((f) => {
  const rel = `chapters/${f}`;
  let html = rd(rel);
  const n = (html.match(/<section\b[^>]*class="[^"]*\bchapter\b/g) || []).length;
  if (n !== 1) W.push({ level: 'error', msg: `${rel}: plik musi zawierać dokładnie jedną <section class="chapter"> (jest ${n})` });
  const m = /<section\b[^>]*data-num="(\d\d)"/.exec(html);
  if (m && m[1] !== f.slice(0, 2)) W.push({ level: 'error', msg: `${rel}: data-num="${m[1]}" nie zgadza się z numerem w nazwie pliku (${f.slice(0, 2)})` });
  if (/<(html|head|body)\b/i.test(html)) W.push({ level: 'error', msg: `${rel}: plik rozdziału to fragment – bez <html>, <head>, <body>` });
  return { file: rel, html: tagFile(html, rel), quiz: /class="[^"]*\bquiz\b/.test(html) };
});

const backItems = [];
if (mode !== 'only') {
  for (const f of listDir('back', /^\d\d-[\w.-]*\.html$/)) {
    backItems.push({ order: parseInt(f.slice(0, 2), 10), html: tagFile(rd(`back/${f}`), `back/${f}`) });
  }
}
for (const [kind, a] of Object.entries(book.autoSections || {})) {
  if (mode === 'only' && (kind !== 'answers' || !chapters.some((c) => c.quiz))) continue;
  backItems.push({ order: a.order, html: `<section class="back auto" id="${a.id}" data-auto="${kind}" data-title="${a.title}"></section>` });
}
backItems.sort((a, b) => a.order - b.order);

const front = [];
if (mode !== 'only') {
  front.push(tagFile(rd('front/cover.html'), 'front/cover.html'));
  front.push(tagFile(rd('front/howto.html'), 'front/howto.html'));
  front.push(`<section class="front toc" id="toc" data-auto="toc" data-title="Spis treści"><div class="front-head"><h1>Spis treści</h1></div><p class="intro">${book.tocIntro || ''}</p></section>`);
}

const docTitle = mode === 'only' ? `Podgląd rozdziału ${opt.only} – ${book.title}` : book.title;
const assembled = `<!doctype html>
<html lang="pl"><head><meta charset="utf-8">
<base href="${pathToFileURL(ROOT).href}/">
<title>${docTitle.replace(/</g, '&lt;')}</title>
<link rel="stylesheet" href="css/style.css">
</head><body class="mode-${mode}">
${rd('lib/svg-defs.html')}
${front.join('\n')}
${chapters.map((c) => c.html).join('\n')}
${backItems.map((b) => b.html).join('\n')}
</body></html>`;
fs.writeFileSync(tmpHtml, assembled);

/* ---------- przeglądarka ---------- */
// --font-render-hinting=none: szerokości tekstu w widoku ekranowym = jak w druku (potrzebne do freezeHyphens i kontroli)
const browser = await chromium.launch({ args: ['--font-render-hinting=none'] });
let exitCode = 0;
try {
  // deviceScaleFactor 2 włącza subpikselowe pozycjonowanie glifów – szerokości tekstu na ekranie = w druku
  const page = await browser.newPage({ viewport: { width: 1000, height: 1400 }, deviceScaleFactor: 2 });
  page.on('pageerror', (e) => W.push({ level: 'error', msg: `Błąd JS na stronie: ${e.message}` }));
  page.on('console', (m) => { if (m.type() === 'error') W.push({ level: 'warn', msg: `Konsola: ${m.text()}` }); });
  page.on('requestfailed', (r) => W.push({ level: 'warn', msg: `Nie wczytano zasobu: ${r.url()}` }));
  await page.goto(pathToFileURL(tmpHtml).href, { waitUntil: 'load' });
  await page.addScriptTag({ path: path.join(ROOT, 'lib', 'browser.js') });
  await page.evaluate(() => document.fonts.ready);

  const prep = await page.evaluate((o) => window.K6.prepare(o), { mode, only: opt.only, book });
  W.push(...prep.warnings);
  await page.evaluate(() => document.fonts.ready);
  const fontsOk = await page.evaluate(async () => {
    await document.fonts.load('10pt "Source Serif 4"', 'ąęłńśźżóć');
    return document.fonts.check('10pt "Source Serif 4"', 'ąęłńśźżóć');
  });
  if (!fontsOk) W.push({ level: 'error', msg: 'Nie wczytano Source Serif 4 (sprawdź katalog fonts/)' });
  W.push(...(await page.evaluate(() => window.K6.measure())));
  await page.emulateMedia({ media: 'print' });

  /* ---------- przebiegi: numery stron aż do stabilizacji ---------- */
  let applied = null, info = null, stable = false, passes = 0;
  for (let pass = 1; pass <= 5; pass++) {
    passes = pass;
    if (applied) {
      const missing = await page.evaluate((m) => window.K6.applyPages(m), applied);
      if (pass === 2 && missing.length) W.push({ level: 'warn', msg: `Brak strony dla: ${missing.join(', ')}` });
    }
    await page.pdf({ path: passPdf, preferCSSPageSize: true, printBackground: true, outline: false, tagged: false });
    info = JSON.parse(execFileSync('python3', [PDFTOOL, 'dests', passPdf], { encoding: 'utf8' }));
    const got = Object.fromEntries(Object.entries(info.dests).map(([k, [i]]) => [k, i + 1]));
    if (applied && JSON.stringify(got) === JSON.stringify(applied)) { stable = true; break; }
    applied = got;
  }
  if (!stable) W.push({ level: 'error', msg: 'Numery stron nie ustabilizowały się po 5 przebiegach – sprawdź odsyłacze w pobliżu końca stron' });
  const pageOf = applied;

  /* ---------- miękkie łączniki -> prawdziwe dywizy tylko tam, gdzie wiersz się łamie ---------- */
  {
    await page.emulateMedia({ media: 'screen' });
    const snap = () => page.evaluate(() => Array.from(document.querySelectorAll('p, li, td, figcaption, dd, .box, aside')).map((e) => Math.round(e.getBoundingClientRect().height)));
    const h0 = process.env.K6_DEBUG ? await snap() : null;
    const fr = await page.evaluate(() => window.K6.freezeHyphens());
    if (h0) {
      const h1 = await snap();
      const els = await page.evaluate(() => Array.from(document.querySelectorAll('p, li, td, figcaption, dd, .box, aside')).map((e) => e.textContent.slice(0, 60)));
      h0.forEach((v, i) => { if (v !== h1[i]) console.log('HEIGHT', v, '->', h1[i], els[i]); });
    }
    await page.emulateMedia({ media: 'print' });
    const shyPdf = passPdf.replace(/\.pdf$/, '.shy.pdf');
    fs.copyFileSync(passPdf, shyPdf);
    await page.pdf({ path: passPdf, preferCSSPageSize: true, printBackground: true, outline: false, tagged: false });
    const after = JSON.parse(execFileSync('python3', [PDFTOOL, 'dests', passPdf], { encoding: 'utf8' }));
    const same = after.pages === info.pages && Object.entries(info.dests).every(([k, [p, top]]) => {
      const b = after.dests[k];
      return b && b[0] === p && (top === null || b[1] === null || Math.abs(b[1] - top) < 1);
    });
    if (process.env.K6_DEBUG) {
      for (const [k, [p, top]] of Object.entries(info.dests)) { const b = after.dests[k]; if (!b || b[0] !== p || Math.abs(b[1] - top) >= 1) console.log('DEST', k, p, top, '->', b); }
    }
    if (same) { info = after; fs.rmSync(shyPdf, { force: true }); }
    else {
      fs.renameSync(shyPdf, passPdf);
      W.push({ level: 'info', msg: `Zamiana miękkich łączników zmieniłaby łamanie – zostawiono wersję z U+00AD (wyszukiwanie w PDF może gorzej działać)` });
    }
    W.push({ level: 'info', msg: `Dzielenie wyrazów: ${fr.broken} przeniesień${same ? '' : ' (niezamrożone)'}` });
  }
  {
    // kontrola: dywiz U+2010 (wstawiany tylko przy zamrażaniu przeniesień w tekście Inter) nie może stać w środku wiersza
    const all = execFileSync('pdftotext', [passPdf, '-'], { encoding: 'utf8' });
    const mids = all.split('\n').flatMap((l) => l.match(/[^\s\d]‐[^\s\d]/gu) || []);
    if (mids.length) W.push({ level: 'warn', msg: `Dywiz przeniesienia w środku wiersza (${mids.length}×, np. „${mids[0]}”) – łamanie ekranowe różni się od druku; zgłoś to` });
  }
  if (pageOf.howto && pageOf.toc && pageOf.toc - pageOf.howto > 1) W.push({ level: 'warn', msg: `Strona „Jak korzystać” zajmuje ${pageOf.toc - pageOf.howto} strony – skróć front/howto.html do jednej` });

  /* ---------- notatki marginesowe: czy stoją obok swojego akapitu ---------- */
  for (const np of prep.notePairs || []) {
    const n = info.dests[np.note], a = info.dests[np.anchor];
    if (!n || !a) continue;
    const where = `${np.file ? '[' + np.file + '] ' : ''}notatka „${np.text}…”`;
    if (n[0] !== a[0]) {
      W.push({ level: 'warn', msg: `s. ${a[0] + 1}: ${where} nie zmieściła się obok swojego akapitu i przeszła na s. ${n[0] + 1} – skróć ją albo przenieś przed wcześniejszy akapit` });
    } else if (n[1] !== null && a[1] !== null && a[1] - n[1] > 120) {
      W.push({ level: 'info', msg: `s. ${n[0] + 1}: ${where} stoi ${Math.round(a[1] - n[1])} pt poniżej swojego akapitu (za dużo notatek obok siebie)` });
    }
  }

  /* ---------- kontrola: tytuły sekcji leżą na stronach z mapy ---------- */
  const pageText = (p) => execFileSync('pdftotext', ['-f', String(p), '-l', String(p), '-layout', passPdf, '-'], { encoding: 'utf8' }).replace(/\u00AD/g, '').replace(/\s+/g, ' ');
  const squash = (s) => s.replace(/[\s\u00AD\u00A0-]+/g, '').toLowerCase();
  let checked = 0, bad = 0;
  for (const s of prep.sections) {
    const p = pageOf[s.id];
    if (!p) { W.push({ level: 'warn', msg: `Nie znaleziono strony sekcji ${s.id}` }); continue; }
    const want = squash((s.kind === 'chapter' ? s.title.slice(3) : s.title).slice(0, 18));
    checked++;
    if (!squash(pageText(p)).includes(want)) { bad++; W.push({ level: 'error', msg: `Kontrola numeracji: „${s.title}” nie występuje na s. ${p}` }); }
  }

  /* ---------- finalizacja: metadane, zakładki, linki ---------- */
  const outline = [
    ...prep.outline.front.map((f) => ({ id: f.id, title: f.title })),
    ...prep.outline.chapters,
    ...prep.outline.back,
  ];
  fs.writeFileSync(metaJson, JSON.stringify({ title: docTitle, author: book.author, subject: book.subject, keywords: book.keywords, outline }));
  const fin = JSON.parse(execFileSync('python3', [PDFTOOL, 'finalize', passPdf, finalPdf, metaJson], { encoding: 'utf8' }));
  for (const b of fin.broken) W.push({ level: 'error', msg: `Martwy link na s. ${b.page} → #${b.dest}` });
  for (const m of fin.outline_missing) W.push({ level: 'warn', msg: `Zakładka bez celu: #${m}` });

  /* ---------- kontrola wydruku: białe dziury, wystające elementy ---------- */
  const startPages = new Set(prep.sections.map((s) => pageOf[s.id]).filter(Boolean));
  const holes = inkCheck(finalPdf, fin.pages, prep.hasCover, startPages);

  /* ---------- czcionki ---------- */
  const fonts = execFileSync('pdffonts', [finalPdf], { encoding: 'utf8' });
  const fontNames = [...new Set(fonts.split('\n').slice(2).map((l) => l.split(/\s+/)[0]).filter(Boolean).map((n) => n.replace(/^[A-Z]{6}\+/, '')))];
  if (!fontNames.some((n) => /SourceSerif4|Source-Serif-4/i.test(n))) W.push({ level: 'error', msg: 'W PDF brak Source Serif 4!' });
  const odd = fontNames.filter((n) => !/^(Inter|SourceSerif4|Source-Serif-4|JetBrainsMono|JetBrains-Mono)/i.test(n));
  if (odd.length) W.push({ level: 'info', msg: `Czcionki zastępcze w PDF (znaki spoza Source Serif/Inter): ${odd.join(', ')}` });
  if (/\bno\b\s+\S+\s+\S+\s*\d+\s+\d+\s*$/m.test(fonts)) W.push({ level: 'warn', msg: 'Niektóre czcionki nie są osadzone' });

  /* ---------- PNG ---------- */
  if (opt.png) {
    fs.rmSync(pngDir, { recursive: true, force: true });
    fs.mkdirSync(pngDir, { recursive: true });
    execFileSync('pdftoppm', ['-r', '96', '-png', finalPdf, path.join(pngDir, 'p')], { stdio: 'ignore' });
  }

  if (!opt.keep) { for (const f of [passPdf, metaJson, tmpHtml]) fs.rmSync(f, { force: true }); }

  /* ---------- raport ---------- */
  const order = { error: 0, warn: 1, info: 2 };
  const uniq = [];
  const seenMsg = new Set();
  for (const w of W) { if (!seenMsg.has(w.msg)) { seenMsg.add(w.msg); uniq.push(w); } }
  uniq.sort((a, b) => order[a.level] - order[b.level]);
  const sym = { error: 'BŁĄD   ', warn: 'UWAGA  ', info: 'info   ' };
  log('');
  for (const w of uniq) log(`${sym[w.level]} ${w.msg}`);
  const ne = uniq.filter((w) => w.level === 'error').length, nw = uniq.filter((w) => w.level === 'warn').length;
  log('');
  log(`Tryb: ${mode}${opt.only ? ' (rozdział ' + opt.only + ')' : ''} · rozdziałów: ${prep.stats.chapters} · rycin: ${prep.stats.figures} · notatek „liceum”: ${prep.stats.liceum} · pytań: ${prep.stats.questions}`);
  log(`Stron: ${fin.pages} · przebiegów: ${passes}${stable ? ' (numeracja stabilna)' : ' (NIESTABILNA)'} · kontrola stron sekcji: ${checked - bad}/${checked} OK · linków: ${fin.links} (martwych: ${fin.broken.length}) · zakładek: ${outline.reduce((s, o) => s + 1 + (o.children ? o.children.length : 0), 0)}`);
  if (holes.length) log(`Strony z dużą białą przestrzenią: ${holes.join(', ')}`);
  log(`Czcionki: ${fontNames.join(', ')}`);
  log(`PDF: ${finalPdf} (${(fs.statSync(finalPdf).size / 1024).toFixed(0)} KB)`);
  if (opt.png) log(`PNG: ${pngDir}/p-*.png`);
  log(`Błędy: ${ne} · uwagi: ${nw} · czas: ${((Date.now() - T0) / 1000).toFixed(1)} s`);
  if (ne) exitCode = 1;
} finally {
  await browser.close();
}
process.exit(exitCode);

/* ====================================================================== */
/* Kontrola „atramentu” na stronach: render 36 dpi w skali szarości (PGM). */
function inkCheck(pdf, nPages, hasCover, startPages) {
  fs.rmSync(checkDir, { recursive: true, force: true });
  fs.mkdirSync(checkDir, { recursive: true });
  const DPI = 36;
  execFileSync('pdftoppm', ['-r', String(DPI), '-gray', pdf, path.join(checkDir, 'p')], { stdio: 'ignore' });
  const files = fs.readdirSync(checkDir).filter((f) => f.endsWith('.pgm')).sort();
  const mm = DPI / 25.4;
  const X0 = Math.round(15.5 * mm), X1 = Math.round(194.5 * mm), Y0 = Math.round(22 * mm), Y1 = Math.round(272 * mm);
  const FOOT = Math.round(279 * mm);
  const holes = [];
  files.forEach((f, idx) => {
    const pno = idx + 1;
    if (hasCover && pno === 1) return;
    const { w, h, data } = readPgm(path.join(checkDir, f));
    const px = (x, y) => data[y * w + x];
    let lowest = -1;
    for (let y = Y1; y >= Y0 && lowest < 0; y--) for (let x = X0; x < X1; x++) if (px(x, y) < 246) { lowest = y; break; }
    const fill = lowest < 0 ? 0 : (lowest - Y0) / (Y1 - Y0);
    const isEnd = startPages.has(pno + 1) || pno === nPages;
    const pct = Math.round(fill * 100);
    if (fill < 0.35) {
      if (isEnd) W.push({ level: 'info', msg: `s. ${pno}: zapełniona w ${pct}% (ostatnia strona sekcji – zwykle w porządku)` });
      else { W.push({ level: 'warn', msg: `s. ${pno}: zapełniona tylko w ${pct}% – duża biała dziura (zwykle rycina/tabela nie zmieściła się i przeszła na następną stronę)` }); holes.push(pno); }
    } else if (fill < 0.6 && !isEnd) {
      W.push({ level: 'info', msg: `s. ${pno}: zapełniona w ${pct}% (biała przestrzeń na dole strony)` });
    }
    // wystające poza pole zadruku
    let side = 0, below = 0;
    for (let y = Y0; y < Y1; y++) {
      for (let x = 0; x < X0 - 3; x++) if (px(x, y) < 236) side++;
      for (let x = X1 + 3; x < w; x++) if (px(x, y) < 236) side++;
    }
    for (let y = Y1 + 3; y < FOOT && y < h; y++) for (let x = X0; x < X1; x++) if (px(x, y) < 236) below++;
    if (side > 3) W.push({ level: 'warn', msg: `s. ${pno}: coś wystaje poza boczny margines (pole zadruku 179 mm)` });
    if (below > 3) W.push({ level: 'warn', msg: `s. ${pno}: coś wystaje poza dolny margines (element wyższy niż strona?)` });
  });
  fs.rmSync(checkDir, { recursive: true, force: true });
  return holes;
}

function readPgm(file) {
  const buf = fs.readFileSync(file);
  let pos = 0;
  const tok = () => {
    while (/\s/.test(String.fromCharCode(buf[pos]))) pos++;
    if (buf[pos] === 35) { while (buf[pos] !== 10) pos++; return tok(); }
    let s = '';
    while (!/\s/.test(String.fromCharCode(buf[pos]))) s += String.fromCharCode(buf[pos++]);
    return s;
  };
  const magic = tok(); const w = +tok(); const h = +tok(); tok(); pos++;
  if (magic !== 'P5') throw new Error('PGM P5 expected');
  return { w, h, data: buf.subarray(pos, pos + w * h) };
}
