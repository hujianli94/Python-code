#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/19 15:03
# filename: urllib-urlopen函数.py

"""
import urllib.request高级用法

response = urllib.request高级用法.urlopen("http://www.python.org")
print(response.read().decode('utf-8'))
"""

# python3
import urllib.request

response = urllib.request.urlopen("http://www.python.org")
print(response.status)              #200
print(response.getheaders())
print(response.getheader('Server'))     #nginx.yaml



#python2
"""
import urllib2
response = urllib2.urlopen("http://www.python.org")
print(response.status)              #200
print(response.getheaders())
print(response.getheader('Server'))     #nginx.yaml

"""
