import sys, asyncio
from playwright.async_api import async_playwright
src, dst, title = sys.argv[1], sys.argv[2], sys.argv[3]
FOOT = f'''<div style="width:100%;font-family:Inter,sans-serif;font-size:6.5pt;color:#8a9097;padding:0 9mm;display:flex;justify-content:space-between">
<span>{title}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>'''
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=__import__('os').environ.get('CHROMIUM', '/opt/pw-browsers/chromium'), args=['--no-sandbox'])
        pg = await b.new_page(viewport={'width': 1400, 'height': 1000})
        await pg.emulate_media(media='print')
        await pg.goto('file://' + src)
        await pg.wait_for_function('document.body.getAttribute("data-wired") === "1"', timeout=15000)
        # sprawdzenie przepełnień tekstu w węzłach
        over = await pg.evaluate('''() => {
          const r = [];
          document.querySelectorAll('.node, .tile, .rn, .hc, .q, .pcard, .page').forEach(e => {
            if (e.scrollWidth > e.clientWidth + 1 || e.scrollHeight > e.clientHeight + 1) {
              r.push((e.className + ' | ' + e.textContent.trim().slice(0, 60)) + ' | ' + e.scrollWidth + 'x' + e.scrollHeight + ' vs ' + e.clientWidth + 'x' + e.clientHeight);
            }
          });
          const pages = [...document.querySelectorAll('.page')].map(pg => {
            const pr = pg.getBoundingClientRect();
            let maxB = 0;
            pg.querySelectorAll('*').forEach(e => { const r = e.getBoundingClientRect(); if (r.height > 0) maxB = Math.max(maxB, r.bottom - pr.top); });
            return Math.round(maxB) + ' of ' + Math.round(pr.height);
          });
          return {over: r, pages};
        }''')
        print('PAGES', over['pages'])
        for o in over['over']:
            print('OVER', o)
        await pg.pdf(path=dst, print_background=True, display_header_footer=True,
                     header_template='<div></div>', footer_template=FOOT, prefer_css_page_size=True)
        await b.close()
asyncio.run(main())
