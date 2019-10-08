import requests
import json
import os
import urllib.request
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "referer": "https://y.qq.com/n/yqq/playlist/5836559239.html",
            'cookie': 'RK=fxgc7YIgPq; ptcz=f1c0d38449a2a55c925bd295cb904864fe4d513df054507ad3925a635f3086ba; tvfe_boss_uuid=99a1332b9fea4779; pgv_pvid=2924616220; pgv_pvi=8648341504; mobileUV=1_166f892a917_7a092; ptui_loginuin=2218330583; pac_uid=1_1763272870; eas_sid=t1J5r4D5O3G9K5N5F8T6Y631U8; o_cookie=1763272870; ts_uid=1274878500; yqq_stat=0; pgv_info=ssid=s4264764056; ts_last=y.qq.com/n/yqq/playlist/5836559239.html'
        }
albumMID = []
zhuanji_list = []


def get_purl(media_mids):
    sf = 'https://u.y.qq.com/cgi-bin/musicu.fcg?data={"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"7208009084","songmid":["%s"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}}}' % media_mids
    ree = requests.get(sf, headers=headers).json()
    purl = ree["req_0"]["data"]["midurlinfo"][0]["purl"]
    purl = 'http://isure.stream.qqmusic.qq.com/' + purl
    # print(purl)
    return purl


def get_album(songname):
    urll = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&remoteplace=txt.yqq.album&searchid=88061514132671527&aggr=0&catZhida=1&lossless=0&sem=10&t=8&p=1&n=30&w={}&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'.format(songname)
    album = requests.get(urll, headers=headers, timeout=3).json()
    for j, i in enumerate(album['data']['album']['list']):
        # print(i)
        albumMID.append(i['albumMID'])
        zhuanji_list.append(i['albumName'])
        print(j, '专辑名字：', i['albumName'])


print("************************************")
print('本软件可下载QQ音乐歌手专辑音乐，原则')
print('上这些专辑可以在QQ音乐听的歌曲都可下载')
print('制作日期：2019/01/20')
print('作者：barrylee')
print("************************************")
songname = input('输入下载的歌手名字然后回车：')
get_album(songname)
# print(zhuanji_list)
# print(albumMID)
x = input('请输入要下载的专辑编号然后回车：')
a = albumMID[int(x)]
get_songmid_url = "https://c.y.qq.com/v8/fcg-bin/fcg_v8_album_info_cp.fcg?ct=24&albummid={}&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0".format(a)

# 发送请求，获取响应 3s之内没有回应就强制结束
resp = requests.get(get_songmid_url, headers=headers, timeout=3)  # proxies=self.proxies,
# print(resp.status_code)
# 将获取结果进行解码
url_str = resp.content.decode()
# 转化为字典格式
dict_str = json.loads(url_str)
# 获取数据信息列表
# print(dict_str)
song_list = dict_str["data"]["list"]
songmid = []
song_name_list = []
for s, k in enumerate(song_list):
    # print(i)
    print(s, '歌曲名字：', k['songname'])
    # print(i['songmid'])
    songmid.append(k['songmid'])
    song_name_list.append(k['songname'])
# print(len(songmid))
for m in range(len(songmid)):
    purl = get_purl(songmid[m])
    # print(purl)
    path = 'D:/qqmusic_专辑/' + songname + '/'
    print(path)
    # print(os.path.exists(path))
    if not os.path.exists(path):
        # print('fg')
        os.mkdir(path)
    pat = path + song_name_list[m] + '.m4a'
    print('开始下载：%s' % song_name_list[m])
    if os.path.exists(pat):
        print('歌曲已存在于%s' % pat)
    else:
        urllib.request.urlretrieve(purl, pat)
        print('%s下载完成' % song_name_list[m])
print("恭喜，该专辑下载完成")
