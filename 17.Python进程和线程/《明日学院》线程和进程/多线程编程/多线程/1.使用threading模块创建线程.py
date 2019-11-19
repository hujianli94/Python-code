#!/usr/bin/env python
#-*- coding:utf8 -*-
import threading
import time

def thread():
    for i in range(3):
        time.sleep(1)
        print("thread name is {}".format(threading.current_thread().name))


if __name__ == '__main__':
    print("----主线程开始-------")
    threads = [threading.Thread(target=thread) for i in range(4) ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('-------------主线程结束-----------------')