import requests
import re
import json
import time

# 获取js源代码，获取英雄id
# 拼接url地址
# 获取下载图片地址


def get_lol_image():
    # 请求头
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    url_js = 'http://lol.qq.com/biz/hero/champion.js'
    res_js = requests.get(url_js, headers=headers).content
    # content是二进制格式
    # 转码 转换成字符串
    html_js = res_js.decode()
    # 正则表达式
    req = '"keys":(.*?),"data"'
    list_js = re.findall(req, html_js)
    #  str转dict
    dict_js = json.loads(list_js[0])
    # 定义图片列表
    # http://ossweb-img.qq.com/images/lol/web201310/skin/big22002.jpg
    pic_js = []
    for key in dict_js:
        # print(key)
        for i in range(20):
            num = str(i)
            if len(num) == 1:
                hero_num = '00' + num
            elif len(num) == 2:
                hero_num = '0' + num
            num_str = key + hero_num
            url = 'http://ossweb-img.qq.com/images/lol/web201310/skin/big' + num_str + '.jpg'
            pic_js.append(url)
    # 图片名称
    list_path = []
    path = 'F:\\lol_images\\'
    for name in dict_js.values():
        for i in range(20):
            file_path = path + name + str(i) + '.jpg'
            # print(file_path)
            list_path.append(file_path)
            # print(list_path)
    # 下载图片
    n = 0
    for i in pic_js:
        res = requests.get(i)
        # 获取状态码
        n += 1
        if res.status_code == 200:
            print("正在下载：%s" % list_path[n])
            time.sleep(1)
            with open(list_path[n], 'wb') as f:
                f.write(res.content)
        else:
            print('下载错误，状态码%d' % res.status_code)


get_lol_image()
