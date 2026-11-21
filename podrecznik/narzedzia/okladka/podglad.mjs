#!/usr/bin/env node
/* Szybki podgląd okładki bez składania całej książki.
 *
 *   node narzedzia/okladka/podglad.mjs [wynik.png] [--pdf wynik.pdf] [--skala 2] [--rozdzialy 10] [--ryciny 85]
 *
 * Bierze front/cover.html i css/style.css (te same czcionki i style co build.mjs), wstawia liczniki
 * (data-stat – w prawdziwym składzie robi to lib/browser.js) i zapisuje zrzut całej okładki (domyślnie
 * Okladka_podglad.png w katalogu podręcznika, skala 2 = 1588 × 2246 px). Z --pdf drukuje też jednostronicowy PDF A4.
 */
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');

const argv = process.argv.slice(2);
const opt = { png: path.join(ROOT, 'Okladka_podglad.png'), pdf: null, scale: 2, chapters: 10, figures: 85 };
for (let i = 0; i < argv.length; i++) {
  const a = argv[i];
  if (a === '--pdf') opt.pdf = argv[++i];
  else if (a === '--skala') opt.scale = Number(argv[++i]);
  else if (a === '--rozdzialy') opt.chapters = Number(argv[++i]);
  else if (a === '--ryciny') opt.figures = Number(argv[++i]);
  else if (a.startsWith('--')) { console.error(`Nieznana opcja: ${a}`); process.exit(2); }
  else opt.png = a;
}

const cover = fs.readFileSync(path.join(ROOT, 'front', 'cover.html'), 'utf8');
const html = `<!doctype html>
<html lang="pl"><head><meta charset="utf-8">
<base href="${pathToFileURL(ROOT).href}/">
<link rel="stylesheet" href="css/style.css">
<style>@media screen { body { width: auto; margin: 0; } }</style>
</head><body>
${cover}
</body></html>`;
const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'okladka-'));
const tmp = path.join(dir, 'okladka.html');
fs.writeFileSync(tmp, html);

const browser = await chromium.launch({ args: ['--font-render-hinting=none'] });
try {
  const page = await browser.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: opt.scale });
  page.on('requestfailed', (r) => console.error(`Nie wczytano zasobu: ${r.url()}`));
  await page.goto(pathToFileURL(tmp).href, { waitUntil: 'load' });
  await page.evaluate(async () => { await Promise.allSettled([...document.fonts].map((f) => f.load())); await document.fonts.ready; });
  // liczniki i formy liczby mnogiej – tak jak w lib/browser.js
  await page.evaluate((stats) => {
    const plural = (n, one, few, many) => (n === 1 ? one : (n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 10 || n % 100 >= 20)) ? few : many);
    for (const el of document.querySelectorAll('[data-stat]')) el.textContent = String(stats[el.dataset.stat] ?? el.textContent);
    for (const el of document.querySelectorAll('[data-stat-label]')) {
      const [key, forms] = el.dataset.statLabel.split(':');
      const [a, b, c] = (forms || '').split('|');
      el.textContent = plural(stats[key] || 0, a, b || a, c || b || a);
    }
  }, { chapters: opt.chapters, figures: opt.figures });
  const el = await page.$('section.cover');
  await el.screenshot({ path: opt.png });
  console.log(`PNG: ${opt.png}`);
  if (opt.pdf) {
    await page.emulateMedia({ media: 'print' });
    await page.pdf({ path: opt.pdf, preferCSSPageSize: true, printBackground: true });
    console.log(`PDF: ${opt.pdf} (${(fs.statSync(opt.pdf).size / 1024).toFixed(0)} KB)`);
  }
} finally {
  await browser.close();
  fs.rmSync(dir, { recursive: true, force: true });
}
