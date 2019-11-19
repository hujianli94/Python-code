#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 10:20
# filename: 07.超时设置.py
import requests

r = requests.get("https://www.taobao.com", timeout=1)
print(r.status_code)
