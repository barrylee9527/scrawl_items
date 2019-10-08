# _*_ coding:utf-8 _*_
import requests
import urllib.request
from bs4 import BeautifulSoup
x = 0


def crawl():
    url = 'http://www.mmjpg.com'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    my_girls = soup.find_all('img')
    for girl in my_girls:
        link = girl.get('src')
        print(link)
        global x
        urllib.request.urlretrieve(link, 'F:\images\%s.jpg' % x)
        x += 1
        print("正在下载第%s张图片" % x)


if __name__ == '__main__':
    crawl()
