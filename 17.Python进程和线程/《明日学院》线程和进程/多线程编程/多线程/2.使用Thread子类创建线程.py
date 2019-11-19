#!/usr/bin/env python
#-*- coding:utf8 -*-
from threading import Thread
import time

class SubThread(Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = '子线程' + self.name + '执行，i=' + str(i)
            print(msg)


if __name__ == '__main__':
    print("------主线程开始--------")
    t1 = SubThread()
    t2 = SubThread()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("----------主线程结束--------")

