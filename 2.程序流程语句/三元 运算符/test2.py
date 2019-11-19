#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/5 18:28
# filename: test2.py
import sys
import os

if len(sys.argv) < 2:
    print("Error 【usage: python {} number】".format(os.path.basename(__file__)))
    sys.exit()
else:
    secore = int(sys.argv[1])
result = "及格" if secore >= 60 else "不及格"
print(result)
