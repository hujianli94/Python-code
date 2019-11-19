#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/10 11:47
# filename: traverse1.py
import os, os.path


def traverse(pathname):
    for item in os.listdir(pathname):
        fullitem = os.path.join(pathname, item)  # 将父目录和当前项拼接起来，获得文件全名
        print(fullitem)

        if os.path.isdir(fullitem):
            traverse(fullitem)


traverse("D:\GitHub")
