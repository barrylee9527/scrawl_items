import requests
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        # "referer": "https://y.qq.com/n/yqq/playlist/5836559239.html",
        # 'cookie': 'RK=fxgc7YIgPq; ptcz=f1c0d38449a2a55c925bd295cb904864fe4d513df054507ad3925a635f3086ba; tvfe_boss_uuid=99a1332b9fea4779; pgv_pvid=2924616220; pgv_pvi=8648341504; mobileUV=1_166f892a917_7a092; ptui_loginuin=2218330583; pac_uid=1_1763272870; eas_sid=t1J5r4D5O3G9K5N5F8T6Y631U8; o_cookie=1763272870; ts_uid=1274878500; yqq_stat=0; pgv_info=ssid=s4264764056; ts_last=y.qq.com/n/yqq/playlist/5836559239.html'
    }
url = 'https://y.qq.com/portal/search.html#page=2&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%8A%E7%99%BD%E6%B0%94%E7%90%83'
req = requests.get(url, headers=headers)
req.encoding = 'utf-8'
print(req.text)