#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/17 12:27
# filename: testmylog.py

from loggingClass4 import MyLog

if __name__ == '__main__':
    t1 = MyLog()
    t1.info("This is info")
    t1.debug("This is debug")
    t1.warn("This is warnning")
    t1.error("This is error")
    t1.critical("This is critcal")
