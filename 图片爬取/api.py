import urllib.request
import json
host = 'https://jisutqybmf.market.alicloudapi.com/weather/query'
# 请求方式
method = 'GET'
app_code = '5229472d8d684a87af2f4ff9ed2967c3'
query_s = 'city=%E5%AE%89%E9%A1%BA'
url = host + '?' + query_s
print(url)
# 解码 转换为中文
con = urllib.request.unquote('%E5%AE%89%E9%A1%BA')
print(con)

request = urllib.request.Request(url)
# 模拟浏览器请求
request.add_header('Authorization', 'APPCODE ' + app_code)
response = urllib.request.urlopen(request)
content = response.read()
# 解码
info = content.decode()
info = json.loads(info)
if info:
    print(info)
