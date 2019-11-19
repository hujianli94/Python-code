#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 10:11
# filename: 04.会话保持.py
import requests

s = requests.Session()

s.get("http://httpbin.org/cookies/set/number/123456789")
r = s.get('http://httpbin.org/cookies')
print(r.text)
