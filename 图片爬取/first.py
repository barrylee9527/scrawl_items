# _*_ coding:utf-8 _*_
import urllib.request
import urllib
from bs4 import BeautifulSoup
# 爬取网页数据
# soup = BeautifulSoup(html, 'html.parser')
# print soup.prettify()#打印本地文件内容
# print (soup.title)
# 字符串格式化 %s %d format  //'https://www.dbmeinv.com/?pager_offset={}'.format(2)
# 如何获取网页源码
x = 0
num = 50


def crawl(pages):
    url = 'https://www.dbmeinv.com/?pager_offset={}'.format(pages)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    # 模拟浏览器登录
    req = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(req, timeout=20)  # 设置超时 page.status 为状态码 它没法添加请求头
    contents = page.read()  # page.read().decode('utf-8')  可以转换编码格式
    soup = BeautifulSoup(contents, 'html.parser')
    my_girls = soup.find_all('img')      # 找到img标签
    for girl in my_girls:
        link = girl.get('src')   # 找到链接
        print(link)
        # 全局变量
        global x
        files = urllib.request.urlretrieve(link, 'F:\images\%s.jpg' % x)  # 下载图片
        x += 1
        if files:
            print("已下载")
        else:
            print("正在下载第%s张" % x)


for i in range(1, num+1):
    print("正在下载第{}页".format(i))
    crawl(i)




