import requests
import urllib
import re
import json
import os 
def get_name_list():
    url = 'https://user.qzone.qq.com/proxy/domain/photo.qzone.qq.com/fcgi-bin/fcg_list_album_v3?g_tk=1800864531&callback=shine0_Callback&t=529878759&hostUin=2257368378&uin=1369562185&appid=4&inCharset=utf-8&outCharset=utf-8&source=qzone&plat=qzone&format=jsonp&notice=0&filter=1&handset=4&pageNumModeSort=40&pageNumModeClass=15&needUserInfo=1&idcNum=4&callbackFun=shine0&_=1582531813771'
    headers = {
        'cookie':'pgv_pvi=2875039744; pgv_si=s6474109952; eas_sid=M1w5f8b188u6Z2v2H4T5Z3d3a9; pgv_info=ssid=s3905474713; pgv_pvid=1906625006; tokenParams=%3Ftype%3D2%26docid%3D14748495972753578133; lolqqcomrouteLine=news_news; RK=hwhU7aIjdI; ptcz=93ba32b3d10f952e099d03bbb3c14acdf5c5da2a6525663d9294f104c96e7fac; _qpsvr_localtk=0.18154505804908316; ptui_loginuin=1763272870; uin=o1369562185; skey=@m019PDWZE; p_uin=o1369562185; welcomeflash=1350560644_79198; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; pt4_token=7L8xv0qUulehZvjVtoM8UglIbfkTyh18wpEH94zpz1w_; p_skey=OGxbll1B1VJqUbRcRWyPb0jbbj1AXxAKjQjggCrs944_; rv2=80683A01CBDA3D7C28608678B029CC43C33CB538EB699993F4; property20=43616B574F83CB119DE09543514361550DB79E3D20AA1EC22BF79E5DEA97275C060562D4E9350741',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
    }
    
    res = requests.get(url,headers=headers).text  
    ree = re.compile(r'"id" : "(.*?)",',re.S).findall(res)
    print(ree)
    name = re.compile(r'"name" : "(.*?)",',re.S).findall(res)
    print(name)
    return ree,name
def get_img(id,path):
    headers = {
        'cookie':'pgv_pvi=2875039744; pgv_si=s6474109952; eas_sid=M1w5f8b188u6Z2v2H4T5Z3d3a9; pgv_info=ssid=s3905474713; pgv_pvid=1906625006; tokenParams=%3Ftype%3D2%26docid%3D14748495972753578133; lolqqcomrouteLine=news_news; RK=hwhU7aIjdI; ptcz=93ba32b3d10f952e099d03bbb3c14acdf5c5da2a6525663d9294f104c96e7fac; _qpsvr_localtk=0.18154505804908316; ptui_loginuin=1763272870; uin=o1369562185; skey=@m019PDWZE; p_uin=o1369562185; welcomeflash=1350560644_79198; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; pt4_token=7L8xv0qUulehZvjVtoM8UglIbfkTyh18wpEH94zpz1w_; p_skey=OGxbll1B1VJqUbRcRWyPb0jbbj1AXxAKjQjggCrs944_; rv2=80683A01CBDA3D7C28608678B029CC43C33CB538EB699993F4; property20=43616B574F83CB119DE09543514361550DB79E3D20AA1EC22BF79E5DEA97275C060562D4E9350741',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
    }
    x = 1
    for page_num in range(30):
        print(page_num)
        page_num = 28*page_num
        page_id = 28
        if (page_num+1)/2 == 0:
            page_id = 14
        print(page_id,page_num)
        url = 'https://h5.qzone.qq.com/proxy/domain/photo.qzone.qq.com/fcgi-bin/cgi_list_photo?g_tk=1800864531&callback=shine0_Callback&t=641480396&mode=0&idcNum=4&hostUin=2257368378&topicId={}&noTopic=0&uin=1369562185&pageStart='.format(id)+str(page_num)+'&pageNum='+str(page_id)+'&skipCmtCount=0&singleurl=1&batchId=&notice=0&appid=4&inCharset=utf-8&outCharset=utf-8&source=qzone&plat=qzone&outstyle=json&format=jsonp&json_esc=1&question=&answer=&callbackFun=shine0&_=1582531946633'
        res = requests.get(url,headers=headers)
        if res.status_code == 200:
            rext = res.text
            ree = re.compile(r'"url" : "(.*?)",',re.S).findall(rext)  
            print(len(ree))   
            for i,link in enumerate(ree):
                print("正在下载第%s张" % x)
                files = urllib.request.urlretrieve(link, path + '/%s.jpg' % x)
                x = x+1
        else:
            print('无当前页面')
            
list_album,name = get_name_list()
for s,i in enumerate(list_album):
    path = 'D:/桌面/mg' + '/' + name[s]
    if not os.path.exists(path):
        os.mkdir(path)
    print('正在下载相册:%s'% name[s])
    get_img(i,path)