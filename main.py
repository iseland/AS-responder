import tkinter as tk
import requests
import time
from threading import Thread

def Bullet_screen():

    headers ={
    "accept": 'application/json,text/javascript, */*; q=0.01',
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-length": "178",
    "Content-Type": 'application/x-www-form-urlencoded;charset=UTF - 8',
    "cookie": "*****填入你的cookie******",
    "dnt": "1",
    "Origin": "https://live.bilibili.com",
    "Referer": "https://live.bilibili.com/"+str(live_id),
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3765.400 QQBrowser/10.6.4153.400",
            }

    form_data = {
    'color': '16777215',
    'fontsize': '25',
    'mode': '1',
    'msg':str(e1.get()),
    'rnd': str(rnd),
    'roomid': str(live_id),
    'bubble': '0',
    'csrf_token': '******填入你的csrf_token******',
    'csrf': '******填入你的csrf******',
                    }

    def func():
        global stop_mainfunction
        for k in range(1,31):
            j= requests.post(url=start_url, data=form_data, headers=headers)
            print(j.status_code)
            time.sleep(0.3)
            print(k)

            if stop_mainfunction:
                print('打call函数停止运行')
                stop_mainfunction = False
                break



    global t
    t = Thread(target=func)
    t.setDaemon(True)
    t.start()

def Bullet_stop():
    global stop_mainfunction
    stop_mainfunction = True


def print_selection():
   global key
   global live_id
   global rnd
   key = v.get()
   live_id = Live_list[key]["live_id"]
   print(live_id)
   rnd = Live_list[key]["rnd"]
   print(rnd)

if __name__ == '__main__':
#在字典中存入直播间参数
    Live_list ={
        1: {
            "live_id": 22632424,
            "rnd": 1613138724,
             },
        2: {
            "live_id": 22637261,
            "rnd": 11612773151,
             },
        3: {
            "live_id": 22634198,
            "rnd": 1613268949,
        },
        4: {
            "live_id": 22625025,
            "rnd": 1613268645,
        },
        5: {
            "live_id": 22625027,
            "rnd": 1613268797,
        },
        6: {
            "live_id": 22632157,
            "rnd": 1613221708,
            },
                }
    start_url = 'https://api.live.bilibili.com/msg/send'
    # 实例化object，建立窗口window
    window = tk.Tk()
    # 给窗口的可视化起名字
    window.title('AS打call器')

    # 设定窗口的大小(长 * 宽)
    window.geometry('400x300')  # 这里的乘是小x

    # 在图形界面上创建 500 * 200 大小的画布并放置各种元素

    l = tk.Label(window, text='请选择要打call直播间', font=('Arial', 12), width=30, height=2)
    l.pack()
    GIRLS = [
        ("贝拉直播间", 1),
        ("嘉然直播间", 2),
        ("伽乐直播间", 3),
        ("向晚直播间", 4),
        ("乃琳直播间", 5),
        ("AS直播间", 6),
    ]
    v = tk.IntVar()

    for girl, num in GIRLS:
        r = tk.Radiobutton(window, text=girl, variable=v, value=num,command=print_selection)
        r.pack()
    print(v.get())
    e1 = tk.Entry(window, show=None, font=('Arial', 14))  # 显示成明文形式

    e1.pack()
    b = tk.Button(window, text='打call', font=('Arial', 12), width=10, height=1, command=Bullet_screen)
    b.pack()
    stop_mainfunction = False
    b2 = tk.Button(window, text='停止', font=('Arial', 12), width=10, height=1, command=Bullet_stop)
    b2.pack()
    # 第7步，主窗口循环显示
    window.mainloop()



