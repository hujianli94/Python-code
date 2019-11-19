#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 10:35
# filename: 08.身份认证.py
import requests
from requests.auth import HTTPBasicAuth

# r = requests.get("http://localhost:5000",auth = HTTPBasicAuth('hujianli','admin#123'))
# print(r.status_code)

r = requests.get("http://localhost:5000",auth=('hujianli','admin#123'))
print(r.status_code)