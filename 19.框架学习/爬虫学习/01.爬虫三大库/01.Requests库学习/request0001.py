#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/27 12:11
# filename: request0001.py

import requests
r = requests.get("http://www.baidu.com")
print(r.text)
