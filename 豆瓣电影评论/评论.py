import re
import requests
import urllib.request
import urllib
import time


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


class Crawl_comments:
    def __init__(self, pos, uuid, title2):
        self.pos = 20*pos
        self.id = uuid
        self.tit = title2
        self.url = 'https://movie.douban.com/subject/'+str(self.id)+'/comments?start={}&limit=20&sort=new_score&status=P&comments_only=1'.format(self.pos)
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'll="108309"; bid=LafEfE1BVe0; __yadk_uid=Ewje0GqgmobCJJVRWCiBvdZU11ujtwyC; _vwo_uuid_v2=DF0E8BADC8579F6F437C3F505D879367F|306e420a404650ab6f36e5bd536df117; ps=y; _ga=GA1.2.1419697443.1542716744; _gid=GA1.2.4734603.1544676071; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18862; douban-fav-remind=1; __utmz=30149280.1544678670.4.3.utmcsr=so.com|utmccn=(organic)|utmcmd=organic|utmctr=%E7%88%AC%E8%99%AB%E5%B0%86%E7%BD%91%E9%A1%B5%E6%98%BE%E7%A4%BA%E6%88%90%E4%B8%AD%E6%96%87; __utma=30149280.1419697443.1542716744.1544694879.1544699688.7; __utmc=30149280; __utmt=1; _gat_UA-7019765-1=1; dbcl2="188621559:Q4JJRTHtrZE"; ck=o-dD; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1544699894%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.968795927.1542716744.1544694879.1544699894.6; __utmb=223695111.0.10.1544699894; __utmc=223695111; __utmz=223695111.1544699894.6.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=30149280.9.10.1544699688; _pk_id.100001.4cf6=cfb516052a8bf35c.1542716744.7.1544699909.1544696419.',
            'DNT': '1',
            'Host': 'movie.douban.com',
            'Referer': 'https://movie.douban.com/subject/'+str(self.id)+'/comments?start=0&limit=20&sort=new_score&status=P',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

    def comment(self):
        proxies = {"http": "http://180.118.86.75:9000"}
        req = requests.get(url=self.url, headers=self.headers, timeout=100)
        # print(req.status_code)
        # print(req.text)
        # print(req.status_code)
        # bianma = req.encoding
        # # print bianma
        # if bianma == 'utf-8' or bianma == 'UTF-8':
        #     html = req.text
        # elif bianma == 'gbk' or bianma == 'GBK':
        #     html = req.text.decode('gbk', 'ignore').encode('utf-8')
        # elif bianma == 'gb2312':
        #     html = req.text.decode('gb2312', 'ignore').encode('utf-8')
        # print(html)
        # req = req.text.encode().decode('unicode-escape')
        # print(req)
        # req = req.text.encode().decode('utf-8')
        # print(req)
        ree = re.compile(r'class=\\\"short\\\">(.*?)</span>', re.S).findall(req.text)
        # print(ree)
        if len(ree) >= 0:
            for rees in ree:
                r = rees.encode().decode('unicode-escape')
                text1 = re.compile(r'([\u4e00-\u9fa5]|[\u3002|\uff1f|\uff01|\uff0c|\u3001|\uff1b|\uff1a|\u201c|\u201d|\u2018|\u2019|\uff08|\uff09|\u300a|\u300b|\u3008|\u3009|\u3010|\u3011|\u300e|\u300f|\u300c|\u300d|\ufe43|\ufe44|\u3014|\u3015|\u2026|\u2014|\uff5e|\ufe4f|\uffe5])').findall(r)
                # print(text1)
                trr1 = ''
                for x in text1:
                    trr1 = trr1 + str(x)
                text2 = re.sub(r"'(.*)'", "", trr1)
                print(text2)
                path = self.tit + '.txt'
                with open(path, 'a') as f:
                    # rees = re.sub(r'\\\n', '', con)
                    # print(rees)
                    f.write(text2 + '\n')
                    # print(rees)
        else:
            print("评论无法显示")
            return


if __name__ == '__main__':
    # television_id()
    title = input("输入电影名字:")
    uid, tit = television_id(title)
    print(uid, tit)
    for i, j in zip(uid, tit):
        print('正在爬的是：%s' % j, end="")
        print("-->id是: %s" % i)
        for k in range(0, 50):
            crawl = Crawl_comments(k, i, j)
            crawl.comment()
            time.sleep(5)




