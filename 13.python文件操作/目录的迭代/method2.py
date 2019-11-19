#!/usr/bin/env python
#-*- coding:utf8 -*-
import os
import os.path

def trav_walk(pathname):
    '''
    root:当前目录
    dirs：当前目录下的子目录
    files：目录下的所有文件
    '''
    for root,dirs,files in os.walk(pathname):
        for file in files:
            fname = os.path.abspath(os.path.join(root,file))
            print(fname)

trav_walk("D:\GitHub")