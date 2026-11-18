#!/usr/bin/env node
/* Podręcznik „Biologia molekularna” – składanie PDF (natywny druk Chromium + pypdf; system z kolokwium 6).
 *
 *   node build.mjs                 całość (bez z00-demo) -> ./<book.output>.pdf
 *   node build.mjs --only 05       jeden rozdział (rozdzialy/z05-*.html) -> <buildDir>/rozdzial-05.pdf
 *   node build.mjs --demo          całość z rozdziałem z00-demo -> <buildDir>/demo.pdf
 *   node build.mjs --png ...       dodatkowo PNG stron (96 dpi) w <buildDir>/<nazwa>-png/
 *   --out-dir DIR                  inny katalog roboczy (albo zmienna PODR_BUILD_DIR)
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
if (opt.only !== null && !/^\d\d$/.test(opt.only)) { console.error('--only wymaga numeru rozdziału, np. --only 05 (Genomika: --only 01)'); process.exit(2); }
const mode = opt.only ? 'only' : opt.demo ? 'demo' : 'full';

const book = JSON.parse(fs.readFileSync(path.join(ROOT, 'book.json'), 'utf8'));
let buildDir = opt.outDir || process.env.PODR_BUILD_DIR || book.buildDir || path.join(ROOT, 'build');
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

const CH = 'rozdzialy';
let chapterFiles = listDir(CH, /^z\d\d-[\w.-]*\.html$/);
const strayChapters = listDir(CH, /\.html$/).filter((f) => !chapterFiles.includes(f));
for (const f of strayChapters) W.push({ level: 'warn', msg: `Pominięto ${CH}/${f}: nazwa musi mieć postać zNN-nazwa.html (np. z05-pcr.html)` });
if (mode === 'full') chapterFiles = chapterFiles.filter((f) => !f.startsWith('z00-'));
if (mode === 'only') {
  chapterFiles = chapterFiles.filter((f) => f.startsWith(`z${opt.only}-`));
  if (!chapterFiles.length) { console.error(`Brak pliku ${CH}/z${opt.only}-*.html`); process.exit(2); }
}
/* rycina z banku: <figure class="fig" data-bank="k5-ryc-04" …> -> build dokleja <img class="bank" src="bank-rycin/k5-ryc-04.svg"> */
const withBank = (html, rel) => html.replace(/<figure\b[^>]*\bdata-bank="([^"]*)"[^>]*>/g, (tag, id) => {
  const f = `bank-rycin/${id}.svg`;
  if (!fs.existsSync(path.join(ROOT, f))) { W.push({ level: 'error', msg: `${rel}: brak ryciny „${id}” w banku (${f}) – sprawdź id w bank-rycin/INDEX.md` }); return tag; }
  return `${tag}<img class="bank" src="${f}" alt="">`;
});
/* rycina rastrowa: <img src="ryciny/cNN-fig-….png"> – plik musi istnieć; szerokość w pikselach wg łamów
   (2 łamy ≈ 179 mm: 2400 px ≈ 340 dpi; 1 łam ≈ 86 mm: 1200 px); poniżej ok. 200 dpi druk będzie miękki */
const pngSize = (file) => {
  try {
    const b = fs.readFileSync(file);
    if (b.readUInt32BE(0) === 0x89504e47) return [b.readUInt32BE(16), b.readUInt32BE(20)];
    for (let i = 2; i < b.length - 9;) { // JPEG: znacznik SOF0–SOF3
      if (b[i] !== 0xff) { i++; continue; }
      const mk = b[i + 1];
      if (mk >= 0xc0 && mk <= 0xc3) return [b.readUInt16BE(i + 7), b.readUInt16BE(i + 5)];
      i += 2 + b.readUInt16BE(i + 2);
    }
  } catch { /* nieczytelny plik */ }
  return null;
};
const checkRaster = (html, rel) => {
  for (const m of html.matchAll(/<figure\b([^>]*)>([\s\S]*?)<\/figure>/g)) {
    const narrow = /class="[^"]*\bnarrow\b/.test(m[1]) || /data-wide="0"/.test(m[1]);
    for (const im of m[2].matchAll(/<img\b[^>]*\bsrc="([^"]+)"/g)) {
      const src = im[1];
      if (src.startsWith('bank-rycin/')) continue;
      if (!src.startsWith('ryciny/')) W.push({ level: 'warn', msg: `${rel}: obrazek „${src}” spoza katalogu ryciny/ – ryciny rastrowe trzymaj w ryciny/ (ścieżka względna: src="ryciny/plik.png")` });
      const file = path.join(ROOT, src);
      if (!fs.existsSync(file)) { W.push({ level: 'error', msg: `${rel}: brak pliku ryciny „${src}” (${file})` }); continue; }
      const sz = pngSize(file);
      const want = narrow ? 1200 : 2400;
      if (sz && sz[0] < want * 0.6) W.push({ level: 'warn', msg: `${rel}: „${src}” ma tylko ${sz[0]} px szerokości – na ${narrow ? '1 łam' : '2 łamy'} potrzeba ok. ${want} px (min. ${Math.round(want * 0.6)})` });
    }
  }
};
const chapters = chapterFiles.map((f) => {
  const rel = `${CH}/${f}`;
  let html = withBank(rd(rel), rel);
  checkRaster(html, rel);
  const n = (html.match(/<section\b[^>]*class="[^"]*\bchapter\b/g) || []).length;
  if (n !== 1) W.push({ level: 'error', msg: `${rel}: plik musi zawierać dokładnie jedną <section class="chapter"> (jest ${n})` });
  const m = /<section\b[^>]*data-num="(\d\d)"/.exec(html);
  if (m && m[1] !== f.slice(1, 3)) W.push({ level: 'error', msg: `${rel}: data-num="${m[1]}" nie zgadza się z numerem w nazwie pliku (${f.slice(1, 3)})` });
  if (/<(html|head|body)\b/i.test(html)) W.push({ level: 'error', msg: `${rel}: plik rozdziału to fragment – bez <html>, <head>, <body>` });
  return { file: rel, html: tagFile(html, rel) };
});

const backItems = [];
if (mode !== 'only') {
  for (const f of listDir('back', /^\d\d-[\w.-]*\.html$/)) {
    backItems.push({ order: parseInt(f.slice(0, 2), 10), html: tagFile(rd(`back/${f}`), `back/${f}`) });
  }
}
for (const [kind, a] of Object.entries(book.autoSections || {})) {
  if (mode === 'only') continue;
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
  // dzielenie wyrazów: wzorce Lianga (lib/hyph-pl.js) + ręczne wyjątki (lib/dzielenie-wyjatki.txt; # = komentarz)
  await page.addScriptTag({ path: path.join(ROOT, 'lib', 'hyph-pl.js') });
  const hyphExc = fs.readFileSync(path.join(ROOT, 'lib', 'dzielenie-wyjatki.txt'), 'utf8').split('\n')
    .map((l) => l.replace(/#.*/, '').trim()).filter(Boolean);
  await page.addScriptTag({ content: `window.K6_HYPH_EXC = ${JSON.stringify(hyphExc)};` });
  await page.addScriptTag({ path: path.join(ROOT, 'lib', 'browser.js') });
  // Wszystkie @font-face wczytujemy jawnie, zanim cokolwiek zmierzymy lub wydrukujemy.
  // Same document.fonts.ready nie wystarcza: podzbiory z unicode-range i kroje używane tylko w druku
  // (pagina w @page – Inter 600/700) ładują się leniwie, dopiero gdy układ ich zażąda; gdyby to nastąpiło
  // w trakcie page.pdf(), druk mógł wyjść z czcionką zastępczą albo z pustą stroną (niedeterministycznie).
  const loadFonts = () => page.evaluate(async () => {
    const faces = [...document.fonts];
    const res = await Promise.allSettled(faces.map((f) => f.load()));
    await document.fonts.ready;
    return res.map((r, i) => (r.status === 'rejected' || faces[i].status !== 'loaded') ? `${faces[i].family} ${faces[i].weight} ${faces[i].style}` : null).filter(Boolean);
  });
  const badFaces = await loadFonts();
  if (badFaces.length) W.push({ level: 'error', msg: `Nie wczytano czcionek: ${[...new Set(badFaces)].join(', ')} (sprawdź katalog fonts/)` });

  const prep = await page.evaluate((o) => window.K6.prepare(o), { mode, only: opt.only, book });
  W.push(...prep.warnings);
  await loadFonts();
  const fontsOk = await page.evaluate(() => document.fonts.check('10pt "Source Serif 4"', 'ąęłńśźżóć'));
  if (!fontsOk) W.push({ level: 'error', msg: 'Nie wczytano Source Serif 4 (sprawdź katalog fonts/)' });
  W.push(...(await page.evaluate(() => window.K6.measure())));
  await page.emulateMedia({ media: 'print' });
  await page.evaluate(() => document.fonts.ready);

  /* ---------- przebiegi: numery stron aż do stabilizacji ---------- */
  let applied = null, info = null, stable = false, passes = 0;
  for (let pass = 1; pass <= 5; pass++) {
    passes = pass;
    if (applied) {
      const missing = await page.evaluate((m) => window.K6.applyPages(m), applied);
      if (pass === 2 && missing.length) W.push({ level: 'warn', msg: `Brak strony dla: ${missing.join(', ')}` });
    }
    await page.pdf({ path: passPdf, preferCSSPageSize: true, printBackground: true, outline: false, tagged: false });
    // Zabezpieczenie przed sporadyczną pustą stroną (raz zaobserwowana pusta 1. strona w --only, nie do
    // odtworzenia): strona bez tekstu w polu zadruku -> drukujemy jeszcze raz, po ustabilizowaniu układu.
    for (let retry = 0; retry < 2; retry++) {
      const empty = emptyPages(passPdf, prep.hasCover);
      if (!empty.length) break;
      W.push({ level: 'info', msg: `Przebieg ${pass}: strona bez tekstu (s. ${empty.join(', ')}) – druk powtórzony` });
      await page.evaluate(() => new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(() => document.fonts.ready.then(r)))));
      await page.pdf({ path: passPdf, preferCSSPageSize: true, printBackground: true, outline: false, tagged: false });
    }
    info = JSON.parse(execFileSync('python3', [PDFTOOL, 'dests', passPdf], { encoding: 'utf8' }));
    const got = Object.fromEntries(Object.entries(info.dests).map(([k, [i]]) => [k, i + 1]));
    if (applied && JSON.stringify(got) === JSON.stringify(applied)) { stable = true; break; }
    applied = got;
    // ściąga: wyrównanie kolumn na ostatniej stronie (potrzebne strony punktów z 1. przebiegu)
    if (pass === 1) await page.evaluate((m) => window.K6.balanceColumns(m), got);
  }
  if (!stable) W.push({ level: 'error', msg: 'Numery stron nie ustabilizowały się po 5 przebiegach – sprawdź odsyłacze w pobliżu końca stron' });
  const pageOf = applied;

  /* ---------- miękkie łączniki -> prawdziwe dywizy tylko tam, gdzie wiersz się łamie ----------
     1. zamrożenie wg układu ekranowego (szerokość = druk, zob. style.css),
     2. druk i kontrola: te same strony i cele linków ORAZ te same wiersze na każdej stronie (pdftotext),
     3. jeśli jakiś akapit złamał się inaczej (remis „na styk” – różnice rzędu 1/64 px między ekranem
        a drukiem), zamrażamy go ponownie przy minimalnie węższym / szerszym wierszu; gdy i to nie pomoże,
        zostawiamy w nim U+00AD (tylko w tym akapicie). Gdyby nawet to nie dało zgodności – cały druk z U+00AD. */
  const pdfDests = (f) => JSON.parse(execFileSync('python3', [PDFTOOL, 'dests', f], { encoding: 'utf8' }));
  const lineDiff = (a, b) => JSON.parse(execFileSync('python3', [PDFTOOL, 'linediff', a, b], { encoding: 'utf8', maxBuffer: 64 << 20 }));
  const printPass = () => page.pdf({ path: passPdf, preferCSSPageSize: true, printBackground: true, outline: false, tagged: false });
  {
    const shyPdf = passPdf.replace(/\.pdf$/, '.shy.pdf');
    fs.copyFileSync(passPdf, shyPdf);
    await page.emulateMedia({ media: 'screen' });
    const fr = await page.evaluate(() => window.K6.freezeHyphens());
    await page.emulateMedia({ media: 'print' });
    let broken = fr.broken, ok = false, shyKept = [], repaired = new Set(), lastDiff = null;
    for (let attempt = 0; ; attempt++) {
      await printPass();
      const after = pdfDests(passPdf);
      const moved = Object.entries(info.dests).filter(([k, [p, top]]) => {
        const b = after.dests[k];
        return !(b && b[0] === p && (top === null || b[1] === null || Math.abs(b[1] - top) < 1));
      }).map(([k]) => k);
      const diff = lineDiff(shyPdf, passPdf);
      lastDiff = diff;
      if (process.env.K6_DEBUG) {
        for (const k of moved) console.log('DEST', k, info.dests[k], '->', after.dests[k]);
        for (const d of diff.diffs) console.log('LINES s.', d.page, JSON.stringify(d.a.slice(0, 4)), '->', JSON.stringify(d.b.slice(0, 4)));
      }
      if (after.pages === info.pages && !moved.length && !diff.diffs.length) { info = after; ok = true; break; }
      if (attempt >= 8) break;
      // różnica na pierwszej stronie zwykle przesuwa wszystko dalej – naprawiamy od pierwszej różniącej się strony
      const ds = diff.diffs.length > 6 ? diff.diffs.slice(0, 1) : diff.diffs;
      const segs = ds.flatMap((d) => d.a.concat(d.b));
      if (!segs.length) break;
      await page.emulateMedia({ media: 'screen' });
      const r = await page.evaluate((sg) => window.K6.refreezeHyphens(sg), segs);
      await page.emulateMedia({ media: 'print' });
      if (!r.refrozen.length && !r.shy.length) break;
      r.refrozen.forEach((e) => repaired.add(e));
      shyKept.push(...r.shy);
      broken += r.broken;
    }
    if (ok) {
      fs.rmSync(shyPdf, { force: true });
      if (shyKept.length) W.push({ level: 'info', msg: `Miękkie łączniki zostawiono w ${shyKept.length} akapitach (łamanie ekranu i druku różni się o ułamek piksela): ${shyKept.slice(0, 3).join('; ')}` });
    } else {
      fs.renameSync(shyPdf, passPdf);
      const d = lastDiff && lastDiff.diffs[0];
      W.push({ level: 'warn', msg: `Zamiana miękkich łączników zmieniłaby łamanie – zostawiono wersję z U+00AD (wyszukiwanie w PDF działa gorzej)${d ? `; pierwsza różnica s. ${d.page}: „${(d.a[0] || '').slice(0, 70)}”` : ''} – zgłoś to` });
    }
    // lista faktycznych przeniesień (do przeglądu jakości dzielenia): <buildDir>/<nazwa>-przeniesienia.txt
    fs.writeFileSync(path.join(buildDir, `${tag}-przeniesienia.txt`), (await page.evaluate(() => window.K6.frozenBreaks())).join('\n') + '\n');
    W.push({ level: 'info', msg: `Dzielenie wyrazów: ${ok ? broken : fr.broken} przeniesień${ok ? (repaired.size ? ` (${repaired.size} akapitów zamrożonych ponownie po kontroli)` : '') : ' (niezamrożone)'}` });
  }
  {
    // kontrola: w warstwie tekstowej nie zostają miękkie łączniki; dywiz U+2010 (wstawiany tylko przy
    // zamrażaniu przeniesień w tekście Inter) nie może stać w środku wiersza
    const all = execFileSync('pdftotext', [passPdf, '-'], { encoding: 'utf8', maxBuffer: 64 << 20 });
    const mids = all.split('\n').flatMap((l) => l.match(/[^\s\d]‐[^\s\d]/gu) || []);
    if (mids.length) W.push({ level: 'warn', msg: `Dywiz przeniesienia w środku wiersza (${mids.length}×, np. „${mids[0]}”) – łamanie ekranowe różni się od druku; zgłoś to` });
    const nShy = (all.match(/\u00AD/g) || []).length;
    if (nShy) W.push({ level: 'info', msg: `Warstwa tekstowa PDF zawiera ${nShy} miękkich łączników (U+00AD)` });
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
  const bodyText = bodyTexts(finalPdf);
  const holes = inkCheck(finalPdf, fin.pages, prep.hasCover, startPages, bodyText);

  /* ---------- czcionki ---------- */
  const fonts = execFileSync('pdffonts', [finalPdf], { encoding: 'utf8' });
  const fontNames = [...new Set(fonts.split('\n').slice(2).map((l) => l.split(/\s+/)[0]).filter(Boolean).map((n) => n.replace(/^[A-Z]{6}\+/, '')))];
  if (!fontNames.some((n) => /SourceSerif4|Source-Serif-4/i.test(n))) W.push({ level: 'error', msg: 'W PDF brak Source Serif 4!' });
  const odd = fontNames.filter((n) => !/^(Inter|SourceSerif4|Source-Serif-4|JetBrainsMono|JetBrains-Mono)/i.test(n));
  if (odd.length) {
    // które znaki i gdzie: strona -> sekcja -> plik źródłowy
    const secAt = (p) => prep.sections.filter((s) => pageOf[s.id] && pageOf[s.id] <= p).sort((a, b) => pageOf[b.id] - pageOf[a.id])[0];
    let detail = '';
    try {
      const chars = [...new Set(odd.map((n) => n.replace(/-.*$/, '')))].flatMap((pat) => JSON.parse(execFileSync('python3', [PDFTOOL, 'fontchars', finalPdf, pat], { encoding: 'utf8', maxBuffer: 16 << 20 })));
      detail = chars.map((c) => `„${c.char}” U+${c.char.codePointAt(0).toString(16).toUpperCase().padStart(4, '0')} (${c.font}) s. ${c.pages.map((p) => { const s = secAt(p); return `${p}${s && s.file ? ' [' + s.file + ']' : ''}`; }).join(', ')}`).join('; ');
    } catch { /* brak pdfminer – sama lista czcionek */ }
    W.push({ level: 'warn', msg: `Czcionki zastępcze w PDF (znaki spoza Source Serif/Inter/JetBrains Mono): ${odd.join(', ')}${detail ? ' – ' + detail + ' – dodaj glif do fonts/ (lib/fontpatch.py) albo zmień znak' : ''}` });
  }
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
  log(`Tryb: ${mode}${opt.only ? ' (rozdział ' + opt.only + ')' : ''} · rozdziałów: ${prep.stats.chapters} · rycin: ${prep.stats.figures} (z banku: ${prep.stats.bank}${prep.stats.raster ? `, PNG: ${prep.stats.raster}` : ''}${prep.stats.placeholders ? `, zaślepek: ${prep.stats.placeholders}` : ''}) · „Pojęcie”: ${prep.stats.notes} · ramek: ${prep.stats.boxes}`);
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
/* Tekst z samego pola zadruku każdej strony (bez żywej paginy i stopki): 22–272 mm w pionie,
   ok. 14–194,5 mm w poziomie (współrzędne pdftotext w pt). */
function bodyTexts(pdf) {
  return execFileSync('pdftotext', ['-x', '40', '-y', '62', '-W', '515', '-H', '709', pdf, '-'], { encoding: 'utf8', maxBuffer: 64 << 20 }).split('\f');
}
function emptyPages(pdf, hasCover) {
  const t = bodyTexts(pdf);
  const out = [];
  for (let i = 0; i < t.length; i++) {
    if (i === t.length - 1 && !t[i].trim()) break; // po ostatnim \f
    if (hasCover && i === 0) continue;
    if (!t[i].trim()) out.push(i + 1);
  }
  return out;
}

/* Kontrola „atramentu” na stronach: render 36 dpi w skali szarości (PGM). */
function inkCheck(pdf, nPages, hasCover, startPages, bodyText) {
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
    const noText = bodyText && !(bodyText[idx] || '').trim();
    if (lowest < 0 || (noText && fill < 0.35)) {
      // pusta strona (np. wymuszony podział strony przed pustym blokiem albo wyścig z ładowaniem czcionek)
      W.push({ level: 'warn', msg: `s. ${pno}: pusta strona – ${lowest < 0 ? 'nic poza paginą' : 'brak tekstu poza paginą'} (sprawdź break-before/after w okolicy; uruchom build ponownie, jeśli znika – zgłoś)` });
      holes.push(pno);
    } else if (fill < 0.35) {
      if (isEnd) W.push({ level: 'info', msg: `s. ${pno}: zapełniona w ${pct}% (ostatnia strona sekcji – zwykle w porządku)` });
      else {
        // < 20% w środku sekcji: zwykle nie rycina, tylko kilka osieroconych wierszy (np. podział kolumn w złym miejscu)
        const why = fill < 0.2 ? 'prawie pusta strona w środku rozdziału – zwykle 1–3 wiersze osierocone przez łamanie; zgłoś, jeśli nie stoi za tym rycina/tabela' : 'duża biała dziura (zwykle rycina/tabela nie zmieściła się i przeszła na następną stronę)';
        W.push({ level: 'warn', msg: `s. ${pno}: zapełniona tylko w ${pct}% – ${why}` }); holes.push(pno);
      }
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
