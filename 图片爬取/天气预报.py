# 导入库
from tkinter import *
from tkinter import messagebox
import urllib.request
import requests
# 创建窗口
root = Tk()
# 标题
root.title('天气查询')
# 窗口大小
root.geometry('500x400')
# 窗口出现位置
root.geometry('+400+180')


def weather():
    # 获取用户输入城市
    city = entry.get()
    if city == '':
        messagebox.askokcancel("提示", '请输入要查询的城市')
    else:
        # 加码
        if type(city) != str:
            print("请输入正确的城市名")
        else:
            city = urllib.request.quote(city)
            host = 'https://jisutqybmf.market.alicloudapi.com/weather/query'
            app_code = 'd75dfb3bac434086a2f1c2c62ffa9c4e'
            query_s = 'city=' + city
            header = {'Authorization': 'APPCODE ' + app_code}
            url = host + '?' + query_s
            request = requests.get(url, headers=header)
            print(request.status_code)
            info = request.json()['result']
            print(info)
            lis.delete(0, END)
            lis.insert(0, '风力：%s' % info['windpower'])
            lis.insert(0, '风向：%s' % info['winddirect'])
            lis.insert(0, '最低温度：%s℃' % info['templow'])
            lis.insert(0, '最高温度：%s℃' % info['temphigh'])
            lis.insert(0, '温度：%s℃' % info['temp'])
            lis.insert(0, '天气：%s' % info['weather'])
            lis.insert(0, '星期：%s' % info['week'])
            lis.insert(0, '更新时间：%s' % info['updatetime'])


# 标签控件
label = Label(root, text='请输入查询的城市：')
# 布局定位
label.grid()
# 输入控件
entry = Entry(root, font=('楷体', 19))
entry.grid(row=0, column=1)
# 列表控件
lis = Listbox(root, font=('宋体', 15), width=45, height=10)
# 跨列合并
lis.grid(row=1, columnspan=2)
# 按钮
button_1 = Button(root, text='查询', width=10, command=weather)
# sticky 对齐方式  E S W N
button_1.grid(row=2, column=0, sticky=W)
button_2 = Button(root, text='退出', width=10, command=root.quit)
# sticky 对齐方式  E S W N
button_2.grid(row=2, column=1, sticky=E)


# 显示窗口 消息循环
root.mainloop()
weather()
