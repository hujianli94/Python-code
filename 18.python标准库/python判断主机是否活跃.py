#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/19 23:18
# filename: python判断主机是否活跃.py
import subprocess
import threading
from time import sleep


def is_reacheable(ip):
    result = subprocess.call(["ping", "-c", "1", ip])
    if result != 0:
        print("{0} is not alive".format(ip))
    else:
        print("{0} is alive".format(ip))


def main():
    # 读取ip地址信息文件，一行一行的读取
    with open("ips.txt") as f:
        lines = f.readlines()
        threads = []
        for line in lines:
            thr = threading.Thread(target=is_reacheable, args=(line,))
            thr.start()
            sleep(1)

            # 将读取的信息加入到列表中，多进程启动
            threads.append(thr)
        for thr in threads:
            thr.join()


if __name__ == '__main__':
    main()
