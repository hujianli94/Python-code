#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/8 22:41
# filename: 01.python打印进度条.py

import time, sys

for i in range(0, 110, 10):
    percent = i / 100
    sys.stdout.write("\r{0}{1}".format("#" * i, '%.2f%%' % (percent * 100)))
    sys.stdout.flush()
    time.sleep(1)

