#!/usr/bin/env python
#-*- coding:utf8 -*-
from threading import Thread

#方法一
t = Thread(target=handle,args=(1,))
t.start()
print("main thread....")




#方法二
class MyThread(Thread):
    def __init__(self,sid):
        Thread.__init__(self)
        self.sid = sid
    def run(self):
        hanled(self.sid)

threads = []
for i in range(1,11):
    t = MyThread(i)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("main thread")
