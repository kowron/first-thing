import sys, asyncio
from playwright.async_api import async_playwright
src = sys.argv[1]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=__import__('os').environ.get('CHROMIUM', '/opt/pw-browsers/chromium'), args=['--no-sandbox'])
        pg = await b.new_page(viewport={'width': 4600, 'height': 3300})
        await pg.emulate_media(media='print')
        await pg.goto('file://' + src)
        await pg.wait_for_function('document.body.getAttribute("data-wired") === "1"', timeout=30000)
        rows = await pg.evaluate('''() => {
          const P = document.querySelector('.poster').getBoundingClientRect(); const mm = 96/25.4;
          const out = [];
          document.querySelectorAll('.sub').forEach(s => {
            const n = s.querySelector(':scope > .node'); if (!n) return;
            let maxB = 0; s.querySelectorAll('*').forEach(e => { const r = e.getBoundingClientRect(); if (r.height>0) maxB = Math.max(maxB, r.bottom); });
            const r = s.getBoundingClientRect();
            let d = 0, x = s; while (x.parentElement && !x.parentElement.classList.contains('treebox')) { x = x.parentElement; if (x.classList.contains('sub')) d++; }
            out.push('  '.repeat(d) + (n.querySelector('.pl')||n.querySelector('.nm')||n).textContent.trim().slice(0,40) + ' | x ' + ((r.left-P.left)/mm).toFixed(0) + ' w ' + (r.width/mm).toFixed(0) + ' top ' + ((r.top-P.top)/mm).toFixed(0) + ' bottom ' + ((maxB-P.top)/mm).toFixed(0));
          });
          return out;
        }''')
        print('\n'.join(rows))
        await b.close()
asyncio.run(main())
