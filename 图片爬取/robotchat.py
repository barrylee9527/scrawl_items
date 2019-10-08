# _*_ coding:utf-8 _*_
from tkinter import *
from tkinter import messagebox
from time import sleep
import requests
root = Tk()
# 标题
root.title('机器人聊天')
# 窗口大小
root.geometry('500x400')
# 窗口出现位置
root.geometry('+400+180')

s = input("请输入任意话题开始聊天：")
while True:
    resp = requests.post('http://www.tuling123.com/openapi/api',
                         data={'key': '675af59b127d43f4884cd637a0409a57', 'info': s, })
    resp = resp.json()
    sleep(2)
    print('小千：', resp['text'])
    s = resp['text']
    resp = requests.get('http://api.qingyunke.com/api.php', {'key': 'free', 'appid': 0, 'msg': s})
    resp.encoding = 'utf8'
    resp = resp.json()
    sleep(2)
    print('傻妞:', resp['content'])
    s = resp['content']

