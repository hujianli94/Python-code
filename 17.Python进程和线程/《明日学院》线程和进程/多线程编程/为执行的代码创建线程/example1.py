#!/usr/bin/env python
#-*- coding:utf8 -*-
import time
def countdown(n):
    while n >0:
        print("Start running child_Thread ",n)
        # print("T-minus",n)
        n -=1
        time.sleep(1)


from threading import Thread
t = Thread(target=countdown,args=(10,))
t.start()
t.join()        #join()方法等待线程结束后方可运行
print("Thread Completed!!")

# if t.is_alive():
#     print("Still running Thread......")
# else:
#     print("Thread Completed!!")

