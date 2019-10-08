import requests
import re
import os
from bs4 import BeautifulSoup

base_url = 'http://www.mmjpg.com/home/{page}'


def get_url(page):
    """
    :param page:
    :return:
    """
    PicSet = set()
    for i in range(1, page + 1, 1):
        print("正在收集第" + str(i) + "页数据.")
        url = base_url.format(page=i)
        resp = requests.get(url)
        resp.encoding = 'utf-8'
        href_pattern = re.compile(r'href="http://www.mmjpg.com/mm/(.*?)"')
        name_pattern = re.compile(r'alt="(.*?)"')
        bsObj = BeautifulSoup(resp.text, 'lxml')
        PicUrlList = bsObj.find_all('li', {})
        for Pic in PicUrlList:
            String = str(Pic)
            page_url = re.findall(href_pattern, String)[0]
            name = re.findall(name_pattern, String)[0]
            print("正在收集" + page_url + "数据")
            info = (page_url, name)
            PicSet.add(info)
    return PicSet


def download(pic_name, pic_url):
    b_url = 'http://www.mmjpg.com/mm/'
    url = b_url + pic_url
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    strFind = 'class="content"(.*?)/></a></div>'
    StrUrl = re.findall(strFind, resp.text)[0]
    url = re.findall('src="(.*?)1.jpg"', StrUrl)[0]

    strFind = 'class="page"(.*?)</a><em '
    StrNum = re.findall(strFind, resp.text)[0]
    num = StrNum[-2:]
    print(num)
    num = int(num)

    for n in range(1, num + 1, 1):
        img_src = url + str(n) + ".jpg"
        img = requests.get(img_src).content
        DirPath = os.getcwd() + "\\mm\\"
        path = DirPath + pic_name + str(n) + '.jpg'
        print('正在下载: ' + str(n) + '...')
        with open(path, 'wb') as f:
            f.write(img)


page = 5
PicPool = get_url(page)
print("收集数据完毕，准备下载-----------")
sum = 1
try:
    for Pic in PicPool:
        pic_url = Pic[0]
        pic_name = Pic[1]
        print("正在操作第" + str(sum) + "板块数据=========")
        download(pic_name, pic_url)
        sum = sum + 1
finally:
    print('下载停止')
