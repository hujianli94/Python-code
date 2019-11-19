#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/8 22:39
# filename: python实时打印时间显示.py

from datetime import datetime as dt
import sys
import time

while True:
    a = dt.now()
    sys.stdout.write('\r{0}'.format(a))
    sys.stdout.flush()
    sys.stdout.write('\033[4A')
    time.sleep(1)
