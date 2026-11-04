import sys, asyncio
from playwright.async_api import async_playwright
src, dst = sys.argv[1], sys.argv[2]
FOOT = '''<div style="width:100%;font-family:Inter,sans-serif;font-size:7pt;color:#8a9097;padding:0 12mm;display:flex;justify-content:space-between">
<span>Mięśnie grzbietu – jak to jest poukładane · wg Bochenka, t. I</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>'''
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=__import__('os').environ.get('CHROMIUM', '/opt/pw-browsers/chromium'), args=['--no-sandbox'])
        pg = await b.new_page()
        await pg.goto('file://' + src)
        await pg.wait_for_timeout(500)
        await pg.pdf(path=dst, format='A4', print_background=True, display_header_footer=True,
                     header_template='<div></div>', footer_template=FOOT, prefer_css_page_size=True)
        await b.close()
asyncio.run(main())
