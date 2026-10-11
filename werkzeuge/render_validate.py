from pathlib import Path
import json, asyncio
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
async def main():
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
  page=await browser.new_page(viewport={'width':1440,'height':1000})
  errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  await page.goto('http://127.0.0.1:8765/seattle_uebersicht.html',wait_until='networkidle')
  await page.evaluate('document.querySelectorAll("img").forEach(i=>i.loading="eager")')
  await page.wait_for_function('Array.from(document.querySelectorAll("img[src]")).every(i=>i.complete && i.naturalWidth>0)')
  assert await page.locator('.asset').count()==33
  await page.get_by_role('button',name='Set: Raum & Stadt',exact=True).click()
  assert await page.locator('input:checked').count()==14
  await page.get_by_role('button',name='Set: Konstruktion',exact=True).click()
  assert await page.locator('input:checked').count()==11
  await page.get_by_role('button',name='Set: Kurzvortrag',exact=True).click()
  assert await page.locator('input:checked').count()==17
  await page.reload(wait_until='networkidle')
  assert await page.locator('input:checked').count()==17
  await page.get_by_role('button',name='Originalpläne',exact=True).click()
  assert await page.locator('.asset:visible').count()==10
  await page.get_by_role('button',name='Alles',exact=True).click()
  await page.locator('[data-level="3"]').click()
  assert await page.locator('#level-no').inner_text()=='5'
  await page.locator('[data-open="P03"]').click()
  assert await page.locator('#viewer').is_visible()
  await page.keyboard.press('Escape')
  await page.get_by_role('button',name='Leeren',exact=True).click()
  await page.locator('[data-level="5"]').click()
  await page.evaluate('window.scrollTo(0,0)')
  await page.screenshot(path='/tmp/seattle_overview_desktop.png')
  await page.pdf(path=str(ROOT/'Seattle_Central_Library_Recherche_Johannes_Fink.pdf'),print_background=True,prefer_css_page_size=True,display_header_footer=True,header_template='<span></span>',footer_template='<div style="width:100%;font:8px Arial;color:#777;text-align:center">Johannes Fink · Seattle Central Library · <span class="pageNumber"></span> / <span class="totalPages"></span></div>')
  await page.set_viewport_size({'width':390,'height':844})
  await page.emulate_media(media='screen')
  await page.evaluate('window.scrollTo(0,0)')
  assert await page.evaluate('document.documentElement.scrollWidth<=innerWidth')
  await page.screenshot(path='/tmp/seattle_overview_mobile.png')
  await page.set_viewport_size({'width':1280,'height':900})
  await page.goto('http://127.0.0.1:8765/05_praesentation/praesentation.html',wait_until='networkidle')
  await page.wait_for_function('Array.from(document.querySelectorAll("img[src]")).every(i=>i.complete && i.naturalWidth>0)')
  checks=await page.evaluate('''()=>Array.from(document.querySelectorAll('.slide')).map(s=>{let f=s.querySelector('.foot').getBoundingClientRect();let els=[...s.querySelectorAll('.image-grid,.cover,.source-list,.credit-list')];return {slide:s.id,bottom:Math.max(...els.map(e=>e.getBoundingClientRect().bottom))-s.getBoundingClientRect().top,footer:f.top-s.getBoundingClientRect().top,overflow:s.scrollWidth>s.clientWidth||s.scrollHeight>s.clientHeight}})''')
  print(json.dumps(checks,indent=2))
  bad=[c for c in checks if c['bottom']>c['footer']-8 or c['overflow']]
  assert not bad, f'Layout overflow: {bad}'
  await page.emulate_media(media='print')
  await page.add_style_tag(content='@page {size:1280px 720px;margin:0} @media print {.slide {zoom:1!important}}')
  await page.pdf(path=str(ROOT/'05_praesentation/OMA_Seattle_Central_Library_Praesentation_Fink.pdf'),width='13.333333in',height='7.5in',print_background=True,prefer_css_page_size=True)
  # Raster copies of our SVGs for editable PowerPoint (not replacements for the originals).
  for a in sorted((ROOT/'02_analysen').glob('*.svg')):
   await page.goto('http://127.0.0.1:8765/02_analysen/'+a.name)
   await page.set_viewport_size({'width':900,'height':650})
   await page.locator('svg').screenshot(path=str(a.with_suffix('.png')))
  await browser.close()
  assert not errors,errors
  print('PASS: 33 images, selection persistence, filters, levels, dialog, mobile width; 16 slide layouts; PDF exports.')
if __name__=='__main__':asyncio.run(main())
