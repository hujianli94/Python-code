#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/26 11:22
# filename: datetime模块.py
"""

datetime模块定义了以下5个类。

datetime.date：表示日期的类。常用的属性有year、month、day。
datetime.time：表示时间的类。常用的属性有hour、minute、second、microsecond。
datetime.datetime：表示日期时间。
datetime.timedelta：表示时间间隔，即两个时间点之间的长度。
datetime.tzinfo：与时区有关的相关信息。
"""

import datetime

dt = datetime.datetime.now()

print("当前时间：", dt)
print('(%Y-%m-%d %H:%M:%S %f): ', dt.strftime('%Y-%m-%d %H:%M:%S %f'))
print('(%Y-%m-%d %H:%M:%S %p): ', dt.strftime('%y-%m-%d %I:%M:%S %p'))
print('%%a: %s ' % dt.strftime('%a'))
print('%%A: %s ' % dt.strftime('%A'))
print('%%b: %s ' % dt.strftime('%b'))
print('%%B: %s ' % dt.strftime('%B'))
print('日期时间%%c: %s ' % dt.strftime('%c'))
print('日期%%x：%s ' % dt.strftime('%x'))
print('时间%%X：%s ' % dt.strftime('%X'))
print('今天是这周的第 %s 天 ' % dt.strftime('%w'))
print('今天是今年的第 %s 天 ' % dt.strftime('%j'))
print('这周是今年的第 %s 周 ' % dt.strftime('%U'))

"""
当前时间： 2019-09-12 12:54:11.749537
(%Y-%m-%d %H:%M:%S %f):  2019-09-12 12:54:11 749537
(%Y-%m-%d %H:%M:%S %p):  19-09-12 12:54:11 PM
%a: Thu 
%A: Thursday 
%b: Sep 
%B: September 
日期时间%c: Thu Sep 12 12:54:11 2019 
日期%x：09/12/19 
时间%X：12:54:11 
今天是这周的第 4 天 
今天是今年的第 255 天 
这周是今年的第 36 周 
"""