#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
功能	说明
datetime.date.today()	打印输出当前的系统日期
datetime.date.fromtimestamp(time.time())	将时间戳转成日期格式
datetime.datetime.now()	打印当前的系统时间
current_time.replace(2016,5,12)	返回当前时间,但指定的值将被替换
datetime.datetime.strptime(“21/11/06 16:30”, “%d/%m/%y %H:%M”)	将字符串转换成日期格式
'''
import datetime,time
#输出当前系统时间
print(datetime.date.today())

#将时间戳格式转换为日期格式
print(time.time())
print(datetime.date.fromtimestamp(time.time()))

#将日期格式转换为struct_time格式
current_time = datetime.datetime.now()
print(current_time)
print(current_time.timetuple())

#替换当前系统时间
print(current_time.replace(2016,5,12))

#将字符串转化成日期格式
str_to_date = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(str_to_date)

######时间相加减

#比现在加10天

new_date = datetime.datetime.now() + datetime.timedelta(days=10)
print(new_date)

#比现在减10天

new_date = datetime.datetime.now() + datetime.timedelta(days=-10)
print(new_date)

#比现在减10小时
new_date = datetime.datetime.now() + datetime.timedelta(hours=-10)
print(new_date)

#比现在+120s
new_date = datetime.datetime.now() + datetime.timedelta(seconds=120)
print(new_date)

