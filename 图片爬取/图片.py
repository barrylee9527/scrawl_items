import requests as req
from bs4 import BeautifulSoup
import lxml
import re
import os
import aiohttp
import asyncio


u = "D:/test"
if not os.path.exists(u):
    os.mkdir(u)
base_url = "http://www.hkdsz.com/art-type-id-{page}-pg-{num}.html"
temp_url = "http://www.hkdsz.com"


async def job(p):
    urls = [base_url.format(page=p, num=x) for x in range(1, 3)]
    for url in urls:

        htmlone = req.get(url).text
        soup_one = BeautifulSoup(htmlone, features='lxml')
        pages = soup_one.find('div', {'class': 'box list channel'}).find('ul').find_all('a')
        for y in pages:

            title = y['title'].split()
            title = str(title).replace(':', '').replace('!', '').replace('?', '').replace(',', '').replace(' ', '')
            print(title)
            new_url = temp_url + y['href']
            htmltwo = req.get(new_url).text
            souptwo = BeautifulSoup(htmltwo, features='lxml')
            img_urls = souptwo.find('div', {'class': 'novelContent'}).find('img')
            img_base_url = s = str(img_urls['src']).split("-")[0]
            t = souptwo.find('div', {'class': 'pagination'}).find_all('a', {'class': 'pagelink_a'})[1]
            max = str(t).split("-")[-1].split(".")[0]
            n = 0
            try:
                os.mkdir(u + "/" + title)
            except Exception as e:
                continue
            for z in range(1, int(max) + 1):
                n = n + 1
                new_url = img_base_url + "-" + str(z) + ".jpg"
                html = req.get(new_url, timeout=7)
                with open(u + "/" + title + "/" + str(n) + ".jpg", 'wb') as f:
                    f.write(html.content)

        asyncio.sleep(1)


async def main(loop):
    tasks = [loop.create_task(job(x)) for x in range(0, 8)]
    await asyncio.wait(tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()