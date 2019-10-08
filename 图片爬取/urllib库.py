import urllib.request
from urllib import error
# 保存cookie ,维持登陆状态
# 异常处理模块error   URL解析  urllib.parser urlparse可以拆分url urlunparse 可以拼接url
import http.cookiejar
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
try:
    response = opener.open('https://google.com')
    for i in cookie:
        print(i.name + '=' + i.value)
except error.URLError as e:
    print(e.reason)
# request = urllib.request.urlopen('http://www.baidu.com', timeout=20)
# print(request)