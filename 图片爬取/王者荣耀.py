import requests
import os
import time
import sys
# 获取json数据，获取英雄id
# 拼接url地址
# 获取下载图片地址
path = "F:/王者荣耀ce/"
if not os.path.exists(path):
    os.mkdir(path)
def get_lol_image():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    url_js = 'http://pvp.qq.com/web201605/js/herolist.json'
    res_js = requests.get(url_js, headers=headers).json()
    # 转码 转换成字符串
    pic_js = get_url(res_js)
    list_path = get_file_path(res_js)
    download_image(list_path, pic_js)
def get_file_path(res_js):
    list_path = []
    for name in res_js:
        cname = name['cname']
        for i in range(1, 7):
            file_path = path + cname + str(i) + '.jpg'
            # print(file_path)
            list_path.append(file_path)
    return list_path
def get_url(res_js):
    pic_js = []
    for res_js_i in res_js:
        heros_id = res_js_i['ename']

        url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}'.format(heros_id)
        str_s = '/{}-bigskin-'.format(heros_id)
        for i in range(1, 7):
            num = str(i)
            real_url = url + str_s + num + '.jpg'
            pic_js.append(real_url)
    return pic_js
def download_image(list_path, pic_js):
    n = 0
    for i in pic_js:
        res = requests.get(i)
        n += 1
        if res.status_code == 200:
            print("正在下载：%s" % list_path[n])
            time.sleep(1)
            with open(list_path[n], 'wb') as f:
                f.write(res.content)
        else:
            print("下载失败")
            print("状态码%d没有对应皮肤" % res.status_code)


if __name__ == '__main__':
    if sys.version_info.major == 2:
        print('请使用python3运行')
    elif sys.version_info.major == 3:
        try:
            get_lol_image()
        except Exception as e:
            print(repr(e))
    else:
        print('运行结束')