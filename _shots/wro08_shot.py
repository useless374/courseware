# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import pathlib
url = pathlib.Path("D:/mytemp/cw_site/wro08.html").as_uri()
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=r"C:/Users/Administrator/AppData/Local/ms-playwright/chromium-1228/chrome-win64/chrome.exe")
    pg = b.new_page(viewport={"width":1600,"height":900}, device_scale_factor=1)
    pg.goto(url); pg.wait_for_timeout(500)
    n = pg.evaluate("document.querySelectorAll('.slide').length")
    for k in range(n):
        pg.evaluate(f"i={k};paint();")
        pg.wait_for_timeout(150)
        pg.locator("#stage").screenshot(path=f"D:/mytemp/cw_site/_shots/wro08-s{k+1}.png")
    b.close()
print("ok", n)
