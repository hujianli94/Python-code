#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/28 12:41
# filename: 02.解压可迭代对象赋值给多个变量.py
"""
record = ("hujianli", "hujianli@163.com", "13262662216", "877323-3232")
name, email, *photo_numbers = record
print(email)
print(photo_numbers)



"""

""" 
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *foelds, homedir, sh = line.split(":")
print(uname)
print(foelds)
print(homedir)
print(sh)

"""

record = ("ACME", 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)