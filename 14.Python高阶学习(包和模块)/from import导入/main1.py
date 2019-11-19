#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
from deam1 import fun_bmi

fun_bmi('李雷',1.81,65)
'''

from deam1 import *
#查看导入了那些定义名
print(dir())
fun_bmi('hujianli', 1.81,65)
list1 = [['hujianli', 1.81, 70], ['xiaojian', 1.79, 62]]
fun_bmi_very_much(list1)