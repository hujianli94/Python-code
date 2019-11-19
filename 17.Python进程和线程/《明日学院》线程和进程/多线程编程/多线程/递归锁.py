#!/usr/bin/env python
#-*- coding:utf8 -*-
import threading
def run1():
    print("grab the first part data")
    lock.acquire()
    global num
    num += 1
    lock.release()
    return num
def run2():
    print("grab the second part data")
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2
def run3():
    lock.acquire()
    res = run1()
    print('--------between run1 and run2-----')
    res2 = run2()
    lock.release()
    print(res, res2)

t_objs = []
if __name__ == '__main__':
    num, num2 = 0, 0
    lock = threading.RLock()  # RLock()类似创建了一个字典，每次退出的时候找到字典的值进行退出
    # lock = threading.Lock()  # Lock()会阻塞在这儿
    for i in range(10):
        t = threading.Thread(target=run3)
        t.start()
        t_objs.append(t)
for t in t_objs:
    t.join()
print(num, num2)
