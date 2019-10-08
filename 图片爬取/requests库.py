import requests
import json
from requests.packages import urllib3
from requests.auth import HTTPBasicAuth
from  requests.exceptions import ReadTimeout


""" data = {
    'name': 'df',
    'age': '22'
}
"""
# response = requests.get('http://www.baidu.com', params=data)  # params可以拼接到链接后面，以字典形式
response = requests.get('http://httpbin.org/get', timeout=20)  # 可以添加超时
# from  requests.exceptions import ReadTimeout requests.get('http://httpbin.org/get',timeout=1)
print(response.json())
print(type(response.json()))
# 以字典的形式
# 提供了解析json的方法
# 或者如下 实现同样的效果
print(json.loads(response.text))
print(type(json.loads(response.text)))
# 下载图片 视频需要获取二进制内容
print(response.content)
# with open('./jpg', 'wb') as f:
#   f.write(response.content)
# get，post 方法里面直接可以传headers
# 响应
# response.headers ,response.status_code
# 高级操作
# 文件上传
files = {'file': open('./video.py', 'rb')}
response1 = requests.post('http://httpbin.org/post', files=files)
print(response1.text)
# 获取cookie 会话维持
s = requests.Session()
s.get('http://www.baidu.com')
# 证书验证 消除证书不安全提示 通过urllib3
urllib3.disable_warning()
res = requests.get('https://www.12306.cn', verify=False)  # 绕过认证
print(res.status_code)
# 也可以手动指定证书
# res1 = requests.get('https://www.12306.cn', cert=('.cert', '/'))
# 代理可以百度
# 认证设置
# from requests.auth import HTTPBasicAuth
r = requests.get('http://', auth=('user', '123'))

