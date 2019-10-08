# _*_ coding:utf-8 _*_
# 解析库 BeautifulSoup(markup, 'html.parser') 'lxml'


from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.baidu.com')

soup = BeautifulSoup(html.text, 'html.parser')
print(soup.prettify())
print(soup.title)
print(soup.title.string)
print(soup.title.name)
print(soup.head)
print(soup.p['id'])
# 获取子节点
print(soup.p.contents)
# find_all(name,attrs,recursive,text,**kwargs)
# 可根据签名，属性，内容查找文档
print(soup.find_all('img'))
# soup.find('img)返回第一个值
for i in soup.find_all('img'):
    print(i.get('src'))
# CSS选择器 select()方法
print(soup.select('li'))

