import requests
import re
import time
import urllib.request
import sys
import os
# urllib.request.urlretrieve("https://www.559di.com/vod/17/12195-1.html",'D:\\code\\code2\\c++.mp4')
# print("done")
res = requests.get('https://www.559di.com/html/18/')
res.encoding = 'utf-8'
# print(res.text)
pattrn = re.compile('<a.*?video-pic loading.*?href="(.*?)"', re.S)
html = pattrn.findall(res.text)
path = "D:/code/"
if not os.path.exists(path):
    os.mkdir(path)
for item in html:
    # print(item)
    strr = "https://www.559di.com"+str(item)
    # print(strr)
    response = requests.get(strr)
    response.encoding = 'utf-8'
    # print(response.text)
    # time.sleep(1)
    pa = re.compile('var.*?httpurl = "(.*?)".*?', re.S)
    text = pa.findall(response.text)
    pb = re.compile('.*?<title>(.*?)</title>.*?', re.S)
    title = pb.findall(response.text)
    # print(title)
    # print(text[0])
    strrr = path + str(title[0])+".mp4"
    # # # print(type(strrr))
    print("开始下载...%s" % title[0])
    urllib.request.urlretrieve(text[0], strrr)
    print("done")
