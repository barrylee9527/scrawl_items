import requests
from pyquery import PyQuery as pq
html = requests.get('http://www.baidu.com').text
# 字符串初始化
doc = pq(html)
print(doc('p'))
# URL初始化
doc = pq(url='http://www.baidu.com')
print(doc('head'))
# 查找子元素
print(doc('head').find('meta'))
# 文件初始化
doc = pq(filename='demo.html')
print(doc('head'))
# 基于CSS选择器
print(doc('p'))
# 遍历 li=doc.items()
# for i in li:
# print(i)
# 获取信息 a.attr('herf')
# 获取html a.html()
# DOM操作
# 移除active标签 li.removeClass('active') 增加为addClass

