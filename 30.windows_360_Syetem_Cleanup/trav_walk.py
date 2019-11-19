#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/10 11:51
# filename: trav_walk.py
import os, os.path


def trav_walk(pathname):
    for root, dir, files in os.walk(pathname):
        for fil in files:
            fname = os.path.abspath(os.path.join(root, fil))  # 拼接路径和文件名
            print(fname)


trav_walk("D:\GitHub")
