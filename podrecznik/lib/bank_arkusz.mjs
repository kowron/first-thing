#!/usr/bin/env node
/* Arkusz podglądu banku rycin: miniatury z id -> bank-rycin/podglad-<prefiks>.png
 *   node lib/bank_arkusz.mjs [prefiks ...]      (domyślnie: wszystkie prefiksy z bank-rycin/*.svg)
 *   --big   większe miniatury (2 kolumny) do kontroli krawędzi: <scratch>/bank/kontrola-<prefiks>.png */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const ROOT = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const BANK = path.join(ROOT, 'bank-rycin');
const args = process.argv.slice(2);
const big = args.includes('--big');
const outDir = big ? (process.env.BANK_CHECK_DIR || BANK) : BANK;
const files = fs.readdirSync(BANK).filter((f) => f.endsWith('.svg')).sort();
let prefixes = args.filter((a) => !a.startsWith('--'));
if (!prefixes.length) prefixes = [...new Set(files.map((f) => f.split('-ryc-')[0]))];

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });
for (const pre of prefixes) {
  const list = files.filter((f) => f.startsWith(pre + '-ryc-'));
  const cols = big ? 2 : 5;
  const cards = list.map((f) => `<div class="c"><div class="id">${f.replace('.svg', '')}</div><img src="${pathToFileURL(path.join(BANK, f)).href}"></div>`).join('');
  const html = `<!doctype html><meta charset="utf-8"><style>
    body{margin:0;padding:14px;background:#e9eeeb;font:600 13px Inter,sans-serif;color:#1d3a2a}
    h1{font-size:16px;margin:0 0 10px} .g{display:grid;grid-template-columns:repeat(${cols},1fr);gap:12px;align-items:start}
    .c{background:#fff;border:1px solid #b9c7bf;padding:6px} .id{margin:0 0 4px;color:#16613a}
    img{display:block;width:100%;height:auto;outline:1px dashed #e06666}
  </style><h1>Bank rycin – ${pre} (${list.length})</h1><div class="g">${cards}</div>`;
  const tmp = path.join(outDir, `.arkusz-${pre}.html`);
  fs.writeFileSync(tmp, html);
  await page.goto(pathToFileURL(tmp).href, { waitUntil: 'load' });
  const out = path.join(outDir, `${big ? 'kontrola' : 'podglad'}-${pre}.png`);
  await page.screenshot({ path: out, fullPage: true });
  fs.rmSync(tmp);
  console.log(out);
}
await browser.close();
