from tkinter import *
from tkinter import messagebox
import requests
import os
import urllib.request
# 创建窗口
root = Tk()
# 标题
root.title('歌曲下载')
# 窗口大小
root.geometry('753x500')
# 窗口出现位置
root.geometry('+500+280')
path = 'D:/qqmusic/'
if not os.path.exists(path):
    os.mkdir(path)
# 标签控件
song_list = []
song_url = []


def get_song():
    name = entry1.get()
    if name == '':
        messagebox.askokcancel("提示", '请输入要查询的歌曲')
    song_name = str(name)
    name_quote = urllib.request.quote(str(name))
    headers = {
        # ':authority': 'music.mli.im',
        'origin': 'https://music.mli.im',
        'cookie': '4395559=true; 3779629=true; 2256615030=true; 3778678=true; 2339424866=true; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; A-donate-2.0=true',
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        'x-requested-with': 'XMLHttpRequest'
    }
    data = {

        'types': 'search',
        'source': 'netease',
        'pages': '2',
        'name': song_name,
        'cache':'9a94264bceaad353ef72684c2f01bb76'
    }

    song_url.clear()
    song_list.clear()
    url = 'https://music.mli.im/api/'
    req = requests.post(url, headers=headers, data=data).json()
    for i, s in enumerate(req):
        # print(s['url'])
        lis.delete(i, END)
        lis.insert(i, '%d 歌名：%s 歌手：%s' % (i, s['name'], s['artist'][0]))
        print(i, '歌曲名字：', s['name'], '作者：', s['artist'][0])

        song_url.append(s['id'])
        print(s['id'])

        song_list.append((s['name'], s['artist'][0]))
    print(song_list[0][1])

def down_load():
        # print('gd')
        # lis.insert(i+1, '歌名：%s' % s['title'])
    # # x = input('输入歌曲对应的数字然后回车：')
    x = entry2.get()
    if x == '':
        messagebox.askokcancel("提示", '请输入要歌曲对应的数字')
    pat = path + song_list[int(x)][0] + '-' + song_list[int(x)][1] + '.mp3'

    # print('开始下载于：%s' % pat)
    print(song_url[int(x)])
    data_json = {
        'types': 'url',
        'id': song_url[int(x)],
        'source': 'netease',
        'cache': '9a94264bceaad353ef72684c2f01bb76'
    }
    headers = {
        # ':authority': 'music.mli.im',
        'origin': 'https://music.mli.im',
        'cookie': '4395559=true; 3779629=true; 2256615030=true; 3778678=true; 2339424866=true; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; A-donate-2.0=true',
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        'x-requested-with': 'XMLHttpRequest'
    }
    url = 'https://music.mli.im/api/'
    mp3 = requests.post(url,headers=headers,data=data_json).json()
    print(mp3)
    urllib.request.urlretrieve(mp3['url'], pat)
    messagebox.showinfo(title='下载完成', message='歌曲保存在：%s' % pat)
    # print('下载完成')


label1 = Label(root, text='请输入要下载的歌曲名称：', font=('楷体', 14))
# 布局定位
label1.grid(row=0, column=0,)
# 输入控件
entry1 = Entry(root, font=('楷体', 19), width=31)
entry1.grid(row=0, column=1,)
label2 = Label(root, text='请输入要歌曲对应的数字：', font=('楷体', 14))
# 布局定位
label2.grid(row=2, column=0,)
label3 = Label(root, text='本软件可以下载QQ音乐收费歌曲，请先输入要', font=('楷体', 14))
label3.grid(row=7, column=1)
label4 = Label(root, text='下载的歌曲然后输入歌曲对应的数字进行下载', font=('楷体', 14))
label4.grid(row=8, column=1)
label5 = Label(root, text='感谢您的使用！！！', font=('楷体', 14))
label5.grid(row=9, column=1)
label6 = Label(root, text='', font=('楷体', 14))
label6.grid(row=6, column=1)
# 输入控件
entry2 = Entry(root, font=('楷体', 19), width=31)
entry2.grid(row=2, column=1,)
button_3 = Button(root, text='查询', width=12, command=get_song)
# sticky 对齐方式  E S W N
button_3.grid(row=0, column=2,)
# button_1.grid(row=0, column=2, )
# 列表控件
lis = Listbox(root, font=('宋体', 15), width=75, height=14)
# 跨列合并
lis.grid(row=1, columnspan=3)
# 按钮
button_1 = Button(root, text='下载', width=12, font=('楷体', 15), command=down_load)
# sticky 对齐方式  E S W N
button_1.grid(row=5, column=0,)
button_2 = Button(root, text='退出', width=12, font=('楷体', 15), command=root.quit)
# sticky 对齐方式  E S W N
button_2.grid(row=5, column=1,)

# 显示窗口 消息循环
root.mainloop()
