#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/27 14:39
# filename: 伪装成浏览器.py


import urllib.request


url = 'http://www.ctrip.com/'

req = urllib.request.Request(url)
req.add_header('User-Agent',
               'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1')

with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode()
    print(htmlstr)
    if htmlstr.find('mobile') != -1:
        print('移动版')


