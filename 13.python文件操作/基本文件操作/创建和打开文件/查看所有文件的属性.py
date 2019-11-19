#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/20 14:56
# filename: 查看所有文件的属性.py


def ShowFileProperties(path):
    """
    显示文件属性，包括路径、大小、创建日期、最后修改时间、最后访问时间
    :param path:
    :return:
    """
    import os, time
    for root, dirs, files in os.walk(path, True):
        print("位置：" + root)
        for filename in files:
            state = os.stat(os.path.join(root, filename))
            info = "文件名：" + filename + " "
            info = info + "大小：" + ("%d" % state[-4]) + " "
            t = time.strftime("%Y-%m-%d %X", time.localtime(state[-1]))
            info = info + "创建时间：" + t + " "
            t = time.strftime("%Y-%m-%d %X", time.localtime(state[-2]))
            info = info + "修改时间：" + t + " "
            t = time.strftime("%Y-%m-%d %X", time.localtime(state[-3]))
            info = info + "最后访问时间：" + t + " "
            print(info)


if __name__ == '__main__':
    path = r"D:\GitHub\21_staduy_python\13.python文件操作\基本文件操作"
    ShowFileProperties(path)
