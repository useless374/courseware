# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import pathlib, shutil
url = pathlib.Path("D:/mytemp/cw_site/wro-route-v5.html").as_uri()
png1 = r"D:/mytemp/cw_site/_shots/wro-route-v5-p1.png"
png2 = r"D:/mytemp/cw_site/_shots/wro-route-v5-p2.png"
pdf  = r"D:/mytemp/cw_site/_shots/古迹文明-路线v5-A4双面-1128.pdf"
final_pdf = r"D:/mytemp/cw_site/wro-route-v5-print.pdf"
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=r"C:/Users/Administrator/AppData/Local/ms-playwright/chromium-1228/chrome-win64/chrome.exe")
    pg = b.new_page(viewport={"width":1600,"height":900})
    pg.goto(url); pg.wait_for_timeout(600)
    pg.locator(".page").nth(0).screenshot(path=png1)
    pg.evaluate("""()=>{const e=document.querySelectorAll('.page')[1];
      e.style.position='static';e.style.left='auto';}""")
    pg.wait_for_timeout(300)
    pg.locator(".page").nth(1).screenshot(path=png2)
    pg.emulate_media(media="print")
    pg.wait_for_timeout(400)
    pg.pdf(path=pdf, format="A4", landscape=True, print_background=True,
           margin={"top":"6mm","bottom":"6mm","left":"6mm","right":"6mm"})
    b.close()
shutil.copyfile(pdf, final_pdf)
print("ok")
