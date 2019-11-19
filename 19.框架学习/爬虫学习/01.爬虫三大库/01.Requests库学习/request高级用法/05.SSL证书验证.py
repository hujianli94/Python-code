#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 10:15
# filename: 05.SSL证书验证.py

import requests
from requests.packages import urllib3

urllib3.disable_warnings()

response = requests.get('http://www.12306.cn', verify=False)
print(response.status_code)
