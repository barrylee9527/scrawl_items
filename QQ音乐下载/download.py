import json
import sys
import os
import requests
from retrying import retry
import urllib.request

path = 'E:/qqmusic/'
if not os.path.exists(path):
    os.mkdir(path)


class QQMusic(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "referer": "https://y.qq.com/n/yqq/playlist/5836559239.html",
            'cookie': 'RK=fxgc7YIgPq; ptcz=f1c0d38449a2a55c925bd295cb904864fe4d513df054507ad3925a635f3086ba; tvfe_boss_uuid=99a1332b9fea4779; pgv_pvid=2924616220; pgv_pvi=8648341504; mobileUV=1_166f892a917_7a092; ptui_loginuin=2218330583; pac_uid=1_1763272870; eas_sid=t1J5r4D5O3G9K5N5F8T6Y631U8; o_cookie=1763272870; ts_uid=1274878500; yqq_stat=0; pgv_info=ssid=s4264764056; ts_last=y.qq.com/n/yqq/playlist/5836559239.html'
        }
        # 获取songmid 的 url
        self.get_songmid_url = "https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg?singermid=003UjO1f3dJMRT&order=listen&begin=0&num=30&songstatus=1"
        # 获取purl 的 url
        self.purl_temp = 'https://u.y.qq.com/cgi-bin/musicu.fcg?data={"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"7208009084","songmid":["%s"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}}}'
        # 获取歌曲 的 url
        self.url_temp = "http://124.203.224.158/amobile.music.tc.qq.com/"
        # 代理
        self.proxies = {"https": "https://118.122.92.252:37901"}

    # 最多尝试6次
    @retry(stop_max_attempt_number=6)
    def _get_songmid(self):
        """获取songmid参数"""
        # 发送请求，获取响应 3s之内没有回应就强制结束
        resp = requests.get(self.get_songmid_url, headers=self.headers, timeout=3)  # proxies=self.proxies,
        print(resp.status_code)
        # 将获取结果进行解码
        url_str = resp.content.decode()
        # 转化为字典格式
        dict_str = json.loads(url_str)
        # 获取数据信息列表
        song_list = dict_str["data"]["list"]
        # 遍历列表获取songmid、songname
        name_mid_list = []
        for name_mid in song_list:
            name_mid_dict = {}
            name_mid_dict["song_name"] = name_mid["musicData"]["songname"]
            name_mid_dict["song_mid"] = name_mid["musicData"]["songmid"]
            name_mid_list.append(name_mid_dict)
        print(name_mid_list)
        return name_mid_list

    def get_songmid(self):
        try:
            name_mid_list = self._get_songmid()
        except Exception as e:
            print(e)
            name_mid_list = None
        return name_mid_list

    # 最多尝试6次
    @retry(stop_max_attempt_number=6)
    def _get_purl(self, songmid):
        """获取purl参数"""
        # 拼接purl
        purl = self.purl_temp % songmid
        # 发送请求，获取响应 3s之内没有回应就强制结束
        resp = requests.get(purl, headers=self.headers, timeout=3)  # proxies=self.proxies,
        # 对结果进行解码
        ret_json = resp.content.decode()
        # 转化为字典
        ret_dict = json.loads(ret_json)
        # 获取purl
        purl = ret_dict["req_0"]["data"]["midurlinfo"][0]["purl"]
        # 返回数据
        # print(purl)
        return purl

    def get_purl(self, songmid):
        try:
            purl = self._get_purl(songmid)
        except Exception as e:
            print(e)
            purl = None
        return purl

    # 最多尝试6次
    @retry(stop_max_attempt_number=6)
    def _parse_url(self, purl):
        """下载数据"""
        # 拼接url
        url = self.url_temp + purl
        # 发送请求，获取响应 30s之内没有回应就强制结束
        resp = requests.get(url, headers=self.headers, timeout=30)  # proxies=self.proxies,
        # 返回数据
        # print(resp.content)
        return resp.content

    def parse_url(self, purl):
        try:
            content = self._parse_url(purl)
        except Exception as e:
            print(e)
            content = None
        return content

    def save_music(self, songname, content):
        """保存歌曲"""
        cont = 'http://isure.stream.qqmusic.qq.com/' + content
        # print(cont)
        path = 'E:/qqmusic/' + songname + '.m4a'
        print(path)
        # with open(path, "wb") as f:
        #     f.write(cont)
        urllib.request.urlretrieve(cont, path)
        print(songname, "download over!")

    def run(self):  # 实现主要逻辑
        # 1.获取songmid、songname等参数
        name_mid_list = self.get_songmid()
        # 判断是否获取到songmid、songname等参数
        if not name_mid_list:
            print("获取songmid、songname等参数失败！")
            # 强制退出
            sys.exit()
        # 2.遍历获取purl
        for name_mid in name_mid_list:
            songname = name_mid["song_name"]
            songmid = name_mid["song_mid"]
            purl = self.get_purl(songmid)
            # 判断是否获取到purl 参数
            if not purl:
                print(songname, "下载失败！")
                continue
            # # 3.发送请求，获取响应
            # content = self.parse_url(purl)
            # print(content)
            # print('agjl')
            # # 判断是否返回数据
            # if not content:
            #     print(songname, "下载失败！")
            #     continue
            # 4.保存数据
            print('开始下载')
            self.save_music(songname, purl)


if __name__ == '__main__':
    music = QQMusic()
    music.run()
