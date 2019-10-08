import requests
import re
import urllib.request
import os
ur = 'http://411am.com'
pat = 'E:/unlock/'
if not os.path.exists(pat):
    os.mkdir(pat)
for i in range(1, 5):
    url = 'http://411am.com/list/?2_{}.html'.format(i)
    res = requests.get(url)
    res.encoding = 'gbk'
    # print(res.text)
    ree = re.compile(r'<a href="/content/.*?title="(.*?)"><i><img src="(.*?)"', re.S).findall(res.text)
    # print(ree)
    for i in ree:
        pic_url = ur + i[1]
        print(pic_url)
        path = pat + i[0] + '.jpg'
        urllib.request.urlretrieve(pic_url, path)

