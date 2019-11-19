#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/8 9:08
# filename: urllib使用.py
from urllib import request
response = request.urlopen("http://www.baidu.com")
print(response.read().decode())