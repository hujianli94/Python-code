#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 9:59
# filename: 01.request文件上传.py

import requests

files = {'file': open('book01.jpg', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)
