#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/12 11:05
# filename: 03.数字的格式化输出.py
x = 1234.56789
print(format(x, '0.2f'))            #1234.57

print(format(x, '>10.1f'))          #    1234.6

print(format(x, '<10.1f'))          #1234.6

print(format(x, '^10.1f'))          #  1234.6

# Inclusion of thousands separator
print(format(x, ','))               #1,234.56789

print(format(x, '0,.1f'))           #1,234.6

print('The value is {:0,.2f}'.format(x))        #The value is 1,234.57