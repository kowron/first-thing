# Mierzy wysokości kart z measure_<PAGE>.html → measure_<PAGE>.json  {tytuł: {szer: wys}}
import asyncio, json, sys
from playwright.async_api import async_playwright
PAGE = sys.argv[1]
OUT = sys.argv[2] if len(sys.argv) > 2 else f'/home/user/first-thing/plakat/measure_{PAGE}.json'
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=__import__('os').environ.get('CHROMIUM', '/opt/pw-browsers/chromium'), args=['--no-sandbox'])
        pg = await b.new_page(viewport={'width': 9000, 'height': 3000})
        await pg.emulate_media(media='print')
        await pg.goto(f'file:///home/user/first-thing/plakat/measure_{PAGE}.html')
        await pg.wait_for_timeout(300)
        r = await pg.evaluate('''() => { const mm = 96/25.4; const out = {};
          document.querySelectorAll('.mbox').forEach(b => { const c = b.firstElementChild; const t = b.dataset.t, w = b.dataset.w;
            (out[t] = out[t] || {})[w] = +(c.getBoundingClientRect().height / mm).toFixed(1); }); return out; }''')
        json.dump(r, open(OUT, 'w'), ensure_ascii=False, indent=0)
        ws = sorted({int(w) for v in r.values() for w in v})
        print('karta'.ljust(40) + ''.join(str(w).rjust(6) for w in ws))
        for t, v in r.items():
            print(t[:39].ljust(40) + ''.join(str(round(v.get(str(w), 0))).rjust(6) for w in ws))
        await b.close()
asyncio.run(main())
