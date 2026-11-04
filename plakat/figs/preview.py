# Podgląd rysunków: python3 preview.py nazwa1 [nazwa2 ...]  → figs/png/<nazwa>.png (8 px/mm, czcionki jak na plakacie)
import sys, os, asyncio
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(HERE, 'png'), exist_ok=True)
PX = float(os.environ.get('PXMM', 8))
async def main(names):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=__import__('os').environ.get('CHROMIUM', '/opt/pw-browsers/chromium'), args=['--no-sandbox'])
        pg = await b.new_page(device_scale_factor=PX / (96 / 25.4))
        for n in names:
            svg = open(os.path.join(HERE, 'out', n + '.svg'), encoding='utf-8').read()
            await pg.set_content(f'<html><body style="margin:0;background:#fff">{svg}</body></html>')
            await pg.evaluate('document.fonts.ready')
            el = await pg.query_selector('svg')
            await el.screenshot(path=os.path.join(HERE, 'png', n + '.png'))
            print('png/' + n + '.png')
        await b.close()
asyncio.run(main(sys.argv[1:]))
