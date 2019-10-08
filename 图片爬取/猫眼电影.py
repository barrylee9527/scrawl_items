import requests
from requests.exceptions import RequestException
import re
import operator as op


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


def get_page(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_page(html):
    pattern = re.compile('title=(.*?) data-act="boarditem-click" data-val="{movieId:', re.S)
    item = re.findall(pattern, html)
    # print(item)
    dic = []
    for i in item:
        content = re.sub(r' class="image-link"', '', i)
        print(content)




def main():
    url = 'http://maoyan.com/board/6'
    html = get_page(url)
    # print(html)
    parse_page(html)


if __name__ == '__main__':
    main()

