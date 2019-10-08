# _*_ coding:utf-8 _*_
import urllib
import re
import urllib.request
from bs4 import BeautifulSoup
x = 0
url = 'http://www.budejie.com/pic'
html = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
req = urllib.request.urlopen(html, timeout=20)
contents = req.read()
soup = BeautifulSoup(contents, 'html.parser')
con = soup.find_all('img')
for i in con:
    link = i.get('src')
    print(link)
    urllib.request.urlretrieve(link, 'E:\images\%s.jpg' % x)
    x += 1
