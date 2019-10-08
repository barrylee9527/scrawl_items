import re
import requests
import os
import urllib.parse

header = {'content-type': 'application/json',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "http://soso.huitu.com/Search/GetAllPicInfo?perPageSize=102&kw={word}&page={num}"
word = input("请输入关键字：")
word = urllib.parse.quote(word)
urls = [str(url).format(word=word, num=x) for x in range(1, 2)]
i = 1
path = "./表情/"
if not os.path.exists(path):
    os.mkdir(path)
for url in urls:
    # print(url)
    html = requests.get(url).text

    # print(html)
    r = re.compile(r'"imgUrl":"(.*?)"')
    u = re.findall(r, html)

    for s in u:
        htmls = requests.get(s)
        print("正在下载第%s张图片" % i)
        with open(path + str(i) + ".jpg", 'wb')as f:
            f.write(htmls.content)
            i = i + 1