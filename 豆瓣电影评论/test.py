import requests
import urllib
def television_id(title1):
    title_real = urllib.request.quote(title1)
    # print(title_real)
    url_id = 'https://movie.douban.com/j/subject_suggest?q={}'.format(title_real)
    header = {
        'Accept': '*/*',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept - Language': 'zh - CN, zh;q = 0.9',
        'Connection': 'keep - alive',
        'Cookie': 'll="108309"; bid=LafEfE1BVe0; __yadk_uid=Ewje0GqgmobCJJVRWCiBvdZU11ujtwyC; _vwo_uuid_v2=DF0E8BADC8579F6F437C3F505D879367F|306e420a404650ab6f36e5bd536df117; ps=y; _ga=GA1.2.1419697443.1542716744; _gid=GA1.2.4734603.1544676071; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18862; douban-fav-remind=1; __utmz=30149280.1544678670.4.3.utmcsr=so.com|utmccn=(organic)|utmcmd=organic|utmctr=%E7%88%AC%E8%99%AB%E5%B0%86%E7%BD%91%E9%A1%B5%E6%98%BE%E7%A4%BA%E6%88%90%E4%B8%AD%E6%96%87; __utma=30149280.1419697443.1542716744.1544694879.1544699688.7; __utmc=30149280; __utmt=1; _gat_UA-7019765-1=1; dbcl2="188621559:Q4JJRTHtrZE"; ck=o-dD; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1544699894%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.968795927.1542716744.1544694879.1544699894.6; __utmb=223695111.0.10.1544699894; __utmc=223695111; __utmz=223695111.1544699894.6.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=30149280.9.10.1544699688; _pk_id.100001.4cf6=cfb516052a8bf35c.1542716744.7.1544699909.1544696419.',
        'DNT': '1',
        'Host': 'movie.douban.com',
        'Referer': 'https://movie.douban.com/subject_search?search_text={}&cat=1002'.format(title_real),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    proxies = {"http": "http://180.118.86.75:9000"}
    con_id = requests.get(url=url_id, headers=header)
    print(con_id.status_code)
    dictionary = []
    tit = []
    for m in con_id.json():
        # print(i['id'])
        dictionary.append(m['id'])
        tit.append(m['title'])
        # print(tit)
    return dictionary, tit
title = input("输入电影名字：")
dictionary, tit = television_id(title)
print(dictionary, tit)
