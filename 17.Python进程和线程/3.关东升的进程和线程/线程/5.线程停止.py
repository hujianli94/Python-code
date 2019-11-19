#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/23 14:51
# filename: 5.线程停止.py
"""
模拟一个下载程序，设置一个停止子进程的停止变量
"""
import threading
import time

# 线程停止变量
isrunning = True
count = 0


# 线程体函数
def thread_body():
    while isrunning:
        # 线程开始工作
        # TODO
        global count
        count += 1
        print("下载中:【{}】.......".format(count), file=open("download.log", "a",encoding="utf-8"))
        # 程序休眠
        time.sleep(0.5)
    print("执行完成！！,执行结果查看：'download.log'")


# 主函数
def main():
    # 创建线程对象t1
    t1 = threading.Thread(target=thread_body)
    # 启动线程t1
    t1.start()

    # 从键盘停止指令
    command = input("请输入停止指令：")
    if command == "exit":
        global isrunning
        isrunning = False


if __name__ == '__main__':
    main()
