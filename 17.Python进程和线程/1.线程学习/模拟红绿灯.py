#!/usr/bin/env python
#-*- coding:utf8 -*-
import time
import threading

event = threading.Event()

def lighter():     #红绿灯
    count = 0
    event.set()     #set flag 初始绿灯
    while True:
        if count >5 and count < 10: #改成红灯
            event.clear() #把标志位清了
            print("现在是红灯")
        elif count >10:
            event.set() #变绿灯
            count = 0
        else:
            print("现在是绿灯")
        time.sleep(1)
        count +=1

def car(name):
    while True:
        if event.is_set():   #判断the flag 是否is set 代表绿灯
            print("[%s] running..."% name )
            time.sleep(1)
        else:
            print("[%s] waiting ...... " %name)
            event.wait()   #等flag被set
            print("绿灯亮了，%s可以走了" %name)
            time.sleep(1)



light = threading.Thread(target=lighter,)
light.start()

car1 = threading.Thread(target=car,args=("Tesla",))
car1.start()
