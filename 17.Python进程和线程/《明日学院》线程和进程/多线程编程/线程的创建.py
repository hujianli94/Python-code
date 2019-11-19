#!/usr/bin/env python
#-*- coding:utf8 -*-
import time
import threading

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print("threading {} @{}".format(self.name, i))
            time.sleep(1)

def main():
    print("Start main threading")

    #创建三个线程
    threads = [ MyThread() for i in range(3) ]
    for t in threads:
        t.start()

    print("End main threading ")

if __name__ == '__main__':
    main()
