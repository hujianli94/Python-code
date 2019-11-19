#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/11/9 22:35
# filename: 文件属性浏览.py

def showFileProperties(path):
    """
    显示文件的属性，
    :param path: 文件夹路径
    :return:
    """
    import time, os
    for root, dirs, files in os.walk(path, True):
        print("位置：" + root)
        for filename in files:
            state = os.stat(os.path.join(root, filename))
            info = "文件名:" + filename + " "
            info = info + "\t大小:" + ("%d" % state[-4]) + " "
            t = time.strftime("%Y-%m-%d %X", time.localtime(state[-1]))
            info = info + "\t创建时间:" + t + " "
            t = time.strftime("%Y-%m-%d %X", time.localtime(state[-2]))
            info = info + "\t最后修改时间:" + t + " "
            t = time.strftime("%Y-%m-%d %X", time.localtime(state[-3]))
            info = info + "\t最后访问时间:" + t + " "
            print(info)


if __name__ == '__main__':
    path = "D:\\21-DAY-Python\\13.python文件操作/文件和流"
    showFileProperties(path)
