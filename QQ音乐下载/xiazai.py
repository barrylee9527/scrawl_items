import requests
import urllib.request
import os
import re
path = 'D:/qqmusic/'
if not os.path.exists(path):
    os.mkdir(path)
print("******************************")
print('本软件可下载QQ音乐收费歌曲，原则')
print('上可以在QQ音乐听的歌曲都可下载')
print('制作日期：2019/01/20')
print('作者：barrylee')
print("******************************")
# print(songname)
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "referer": "https://y.qq.com/n/yqq/playlist/5836559239.html",
        # 'cookie': 'RK=fxgc7YIgPq; ptcz=f1c0d38449a2a55c925bd295cb904864fe4d513df054507ad3925a635f3086ba; tvfe_boss_uuid=99a1332b9fea4779; pgv_pvid=2924616220; pgv_pvi=8648341504; mobileUV=1_166f892a917_7a092; ptui_loginuin=2218330583; pac_uid=1_1763272870; eas_sid=t1J5r4D5O3G9K5N5F8T6Y631U8; o_cookie=1763272870; ts_uid=1274878500; yqq_stat=0; pgv_info=ssid=s4264764056; ts_last=y.qq.com/n/yqq/playlist/5836559239.html'
    }
def get_media(songname):
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.top&searchid=25594113905573506&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p='+str(1)+'&n=20&w={}&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'.format(songname)
    res = requests.get(url, headers=headers, timeout=3).json()
    # print(res['data']['song']['list'])
    songmedia = []
    songlist = []
    song_media_ = []
    for i, s in enumerate(res['data']['song']['list']):
        # print(s)
        print(i, '歌曲名字：', s['title'], '作者：', s['singer'][0]['name'])
        media_mid = s['mid']
        media_mid_second = s['file']['media_mid']
        # print(media_mid)
        # print(s['mid'])
        # print('第二个')
        # print(media_mid_second)
        song_media_.append(media_mid)
        if media_mid_second == '':
            songmedia.append(media_mid)
        else:
            songmedia.append(media_mid_second)
        songlist.append((s['title'], s['singer'][0]['name']))
    return songmedia, songlist, song_media_

def get_purl(media_mids, song_media_):
    # print(media_mids)
    purl = ''
    purls =''
    purrs = ''
    sf = 'https://u.y.qq.com/cgi-bin/musicu.fcg?data={"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"7208009084","songmid":["%s"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}}}' % media_mids
    sfs = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey854095660044653&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"2924616220","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"2924616220","songmid":["%s"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":24,"cv":0}}'% song_media_
    ree = requests.get(sf, headers=headers, timeout=3).json()
    rees = requests.get(sfs, headers=headers, timeout=3).json()
    try:
        purr = rees["req_0"]["data"]["midurlinfo"][0]["purl"]
        purrs = 'http://dl.stream.qqmusic.qq.com/' + purr
    # print(purr)
    except:
        try:
            purl = ree["req_0"]["data"]["midurlinfo"][0]["purl"]
            purl = 'http://isure.stream.qqmusic.qq.com/' + purl
            purls = 'http://dl.stream.qqmusic.qq.com/' + ree["req_0"]["data"]["midurlinfo"][0]["purl"]
        except:
            print('该歌曲查找错误')
    # print(purl)
    return purl, purls, purrs
# print(songmedia)


while True:
    songname_ = input('请输入你要下载的歌曲然后回车：')
    songname = urllib.request.quote(songname_)
    songmedia, songlist, song_media_ = get_media(songname)
    if len(songlist) == 0:
        print('未找到该歌曲信息')
    else:
        x = input('输入歌曲对应的数字然后回车：')
        # print(songmedia[int(x)])
        if int(x) <= 19:
            pur, purls, purrs = get_purl(songmedia[int(x)], song_media_[int(x)])
            # print(pur)
            # print(purls)
            # print(purrs)
            # print(songlist[int(x)])
            nnn = re.sub(r'/', '', songlist[int(x)][0])
            # print(nnn)
            path_loacl = path + nnn + '-' + songlist[int(x)][1] + '.m4a'
            paa = songlist[int(x)][0] + songlist[int(x)][1] + '.m4a'
            print("开始下载%s" % paa)
            # print(path_loacl)
            if os.path.exists(path_loacl):
                print('该歌曲已存在于%s' % path_loacl)
            else:
                try:
                    urllib.request.urlretrieve(pur, path_loacl)
                    print('下载完成')
                    print('请在路径:[%s]下查看' % path_loacl)
                    flag = input('如需继续下载可以按任意键进行搜歌，否则按数字键0结束程序:\n')
                    if flag == '0':
                        break
                except:
                    try:
                        urllib.request.urlretrieve(purls, path_loacl)
                        print('下载完成')
                        print('请在路径:[%s]下查看' % path_loacl)
                        flag = input('如需继续下载可以按任意键进行搜歌，否则按数字键0结束程序:\n')
                        if flag == '0':
                            break
                    except:
                        try:
                            # print('gf')
                            # print(purrs)
                            # print(path_loacl)
                            urllib.request.urlretrieve(purrs, path_loacl)
                            print('下载完成')
                            print('请在路径:[%s]下查看' % path_loacl)
                            flag = input('如需继续下载可以按任意键进行搜歌，否则按数字键0结束程序:\n')
                            if flag == '0':
                                break
                        except:
                            print('歌曲下载出错，可能是QQ音乐无该歌曲版权')
        else:
            print('数字输入错误，请输入正确的数字')
            pass
print('程序结束,非常感谢您的使用！！！')
