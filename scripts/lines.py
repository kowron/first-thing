import sys, asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=__import__('os').environ.get('CHROMIUM', '/opt/pw-browsers/chromium'), args=['--no-sandbox'])
        pg = await b.new_page(viewport={'width': 4600, 'height': 3300})
        await pg.emulate_media(media='print')
        await pg.goto('file:///home/user/first-thing/plakat/index.html')
        await pg.wait_for_function('document.body.getAttribute("data-wired") === "1"')
        r = await pg.evaluate('''() => {
          const mm = 96/25.4; const out = [];
          document.querySelectorAll('svg.wires line').forEach(l => {
            const x1=+l.getAttribute('x1'), x2=+l.getAttribute('x2'), y1=+l.getAttribute('y1'), y2=+l.getAttribute('y2');
            if (Math.abs(x2-x1) > 100*mm || Math.abs(y2-y1) > 400*mm) out.push([x1/mm, y1/mm, x2/mm, y2/mm, l.getAttribute('stroke')].map(v => typeof v === 'number' ? v.toFixed(0) : v).join(' '));
          });
          return out;
        }''')
        print('\n'.join(r))
        await b.close()
asyncio.run(main())
