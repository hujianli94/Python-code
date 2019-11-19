#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/27 13:44
# filename: demo2.py
import requests

proxy = {"https": "124.205.155.146:9090",
         "http": "218.64.69.79:8080"}



respones = requests.get("http://www.mingrisoft.com/", proxies=proxy)
print(respones.content)
