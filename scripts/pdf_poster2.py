import sys, asyncio
from playwright.async_api import async_playwright
# użycie: pdf_poster2.py index.html out.pdf   (out.pdf = "-" → tylko pomiar, bez PDF)
src, dst = sys.argv[1], sys.argv[2]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=__import__('os').environ.get('CHROMIUM', '/opt/pw-browsers/chromium'), args=['--no-sandbox'])
        pg = await b.new_page(viewport={'width': 7000, 'height': 5200})
        await pg.emulate_media(media='print')
        await pg.goto('file://' + src)
        await pg.wait_for_function('document.body.getAttribute("data-wired") === "1"', timeout=60000)
        info = await pg.evaluate('''() => {
          const P = document.querySelector('.poster').getBoundingClientRect(); const mm = 96/25.4;
          const f = v => +(v/mm).toFixed(0);
          const box = el => { const r = el.getBoundingClientRect(); return [f(r.left-P.left), f(r.top-P.top), f(r.right-P.left), f(r.bottom-P.top)]; };
          const deep = el => { let mb = el.getBoundingClientRect().bottom; el.querySelectorAll('*').forEach(e => { const r = e.getBoundingClientRect(); if (r.height>0) mb = Math.max(mb, r.bottom); }); return f(mb - P.top); };
          const out = {page: [f(P.width), f(P.height)]};
          out.cols = [...document.querySelectorAll('.sub[id]')].map(s => s.id + ' ' + JSON.stringify(box(s)) + ' dół ' + deep(s));
          out.docks = [...document.querySelectorAll('.dock')].map(d => d.dataset.under + ' ' + JSON.stringify(box(d)));
          const lg = document.querySelector('.legend'); out.legend = lg ? JSON.stringify(box(lg)) : '-';
          let maxB = 0, maxR = 0;
          document.querySelectorAll('.poster *').forEach(e => { if (e.closest('svg')) return; const r = e.getBoundingClientRect(); if (r.height>0) { maxB = Math.max(maxB, r.bottom); maxR = Math.max(maxR, r.right); } });
          out.max_bottom = f(maxB - P.top); out.max_right = f(maxR - P.left);
          out.over = [];
          document.querySelectorAll('.card, .node.g, .q, .panel').forEach(e => {
            if (e.scrollWidth > e.clientWidth + 2) out.over.push(e.className + ' | ' + e.textContent.trim().slice(0, 50));
          });
          // nakładanie się doków i legendy na karty
          const rects = [...document.querySelectorAll('.card, .node.g, .panel, .legend')].map(e => [e, e.getBoundingClientRect()]);
          out.overlap = [];
          for (let i = 0; i < rects.length; i++) for (let j = i+1; j < rects.length; j++) {
            const [a, ra] = rects[i], [c, rc] = rects[j];
            if (a.contains(c) || c.contains(a)) continue;
            const ix = Math.min(ra.right, rc.right) - Math.max(ra.left, rc.left), iy = Math.min(ra.bottom, rc.bottom) - Math.max(ra.top, rc.top);
            if (ix > 2 && iy > 2) out.overlap.push((a.querySelector('.nm,.pt,.pl')||a).textContent.slice(0,30) + ' × ' + (c.querySelector('.nm,.pt,.pl')||c).textContent.slice(0,30));
          }
          out.overlap = out.overlap.slice(0, 12);
          return out;
        }''')
        for k, v in info.items():
            if isinstance(v, list) and v and isinstance(v[0], str):
                for x in v: print(k, '|', x)
            else:
                print(k, v)
        if dst != '-':
            await pg.pdf(path=dst, print_background=True, prefer_css_page_size=True)
        await b.close()
asyncio.run(main())
