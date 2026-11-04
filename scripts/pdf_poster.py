import sys, asyncio
from playwright.async_api import async_playwright
src, dst = sys.argv[1], sys.argv[2]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=__import__('os').environ.get('CHROMIUM', '/opt/pw-browsers/chromium'), args=['--no-sandbox'])
        pg = await b.new_page(viewport={'width': 4600, 'height': 3300})
        await pg.emulate_media(media='print')
        await pg.goto('file://' + src)
        await pg.wait_for_function('document.body.getAttribute("data-wired") === "1"', timeout=30000)
        info = await pg.evaluate('''() => {
          const poster = document.querySelector('.poster').getBoundingClientRect();
          const mm = 96/25.4;
          const cols = [...document.querySelectorAll('.treebox > .sub > .kids > .sub')].map(s => {
            let maxB = 0;
            s.querySelectorAll('*').forEach(e => { const r = e.getBoundingClientRect(); if (r.height > 0) maxB = Math.max(maxB, r.bottom); });
            const r = s.getBoundingClientRect();
            return (s.querySelector('.node .pl') || {}).textContent + ': bottom ' + ((maxB - poster.top)/mm).toFixed(0) + 'mm, width ' + (r.width/mm).toFixed(0) + 'mm';
          });
          const over = [];
          document.querySelectorAll('.card, .node.g, .q, .panel').forEach(e => {
            if (e.scrollWidth > e.clientWidth + 2) over.push('W ' + e.className + ' | ' + e.textContent.trim().slice(0, 50) + ' ' + e.scrollWidth + '>' + e.clientWidth);
          });
          const L = document.querySelector('.legend').getBoundingClientRect();
          const I = document.querySelector('.info').getBoundingClientRect();
          const root = document.querySelector('.node.root').getBoundingClientRect();
          return {cols, over, poster_h: (poster.height/mm).toFixed(0), legend_bottom: ((L.bottom-poster.top)/mm).toFixed(0),
                  legend_left: ((L.left-poster.left)/mm).toFixed(0), info_right: ((I.right-poster.left)/mm).toFixed(0),
                  root_l: ((root.left-poster.left)/mm).toFixed(0), root_r: ((root.right-poster.left)/mm).toFixed(0), root_b: ((root.bottom-poster.top)/mm).toFixed(0)};
        }''')
        for k, v in info.items():
            if isinstance(v, list):
                for x in v: print(k, '|', x)
            else:
                print(k, v)
        await pg.pdf(path=dst, print_background=True, prefer_css_page_size=True)
        await b.close()
asyncio.run(main())
