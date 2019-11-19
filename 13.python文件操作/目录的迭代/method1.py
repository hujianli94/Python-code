#!/usr/bin/env python
#-*- coding:utf8 -*-
import os
import os.path

def traverse(pathname):
    for item in os.listdir(pathname):
        fullitem = os.path.join(pathname,item)
        print(fullitem)
        if os.path.isdir(fullitem):
            traverse(fullitem)
traverse("D:\GitHub")


