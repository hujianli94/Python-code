#!/usr/bin/env python
#-*- coding:utf8 -*-
import threading
import time
# def thread_job():
#     print("This is an added Thread,number is {}".format(threading.current_thread()))
#
#
# def main():
#     added_thread = threading.Thread(target=thread_job)
#     # print(threading.active_count())  #几个线程？
#     # print(threading.enumerate())
#     # print(threading.current_thread())   #是什么线程？
#     added_thread.start()
#
# if __name__ == '__main__':
#     main()

def thread_job():
    print("T1 start...")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish....")

def T2_job():
    print("T2 start.....")
    print("T2 finish.....")

added_thread = threading.Thread(target=thread_job,name="T1")
thread2 = threading.Thread(target=T2_job,name="T2")
added_thread.start()
thread2.start()
added_thread.join()     #等待子进程运行完毕，进行阻塞
thread2.join()
print("all done\n")



