#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 10:18
# filename: 06.代理设置.py

import requests

proxies = {"https": "124.205.155.146:9090",
         "http": "218.64.69.79:8080"}



respones = requests.get("http://www.mingrisoft.com/", proxies=proxies)
print(respones.content)