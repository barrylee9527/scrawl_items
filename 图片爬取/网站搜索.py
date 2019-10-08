"""
@author:barrylee
@time:2018/9/9
@qqnumber:1763272870

"""
import requests
pre_url = 'http://'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
for i in range(4, 9):
    for m in range(1, 9):
        for n in range(1, 9):
            url2 = pre_url + str(i) + str(m) + str(n)
            # url3.append(url2)
            for j in range(65, 90):
                for k in range(65, 90):
                    aci = chr(j).lower()
                    str1 = chr(k).lower()
                    # print(i)
                    url = url2 + str(aci) + str(str1)
                    real_url = url + '.com'
                    try:
                        if requests.get(real_url, headers=headers).status_code == 200:
                            print(real_url)
                            # uuu.append(real_url)
                            # with open(path, 'a') as f:
                            #     f.write(real_url + '\n')
                            # # print(real_url)
                        else:
                            print('无法访问')
                    except Exception as e:
                        print(repr(e))
                        pass
        # print(url3)

