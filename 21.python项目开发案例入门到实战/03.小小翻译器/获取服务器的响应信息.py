#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/24 14:17
# filename: 获取服务器的响应信息.py
from urllib import request

f = request.urlopen("https://fanyi.baidu.com/")
data = f.read()
# 返回请求HTTP后的状态，reason返回未被响应的原因
print("Status:", f.status, f.reason)

# 返回HTTP响应的头信息
for k, v in f.getheaders():
    print("{}:{}".format(k, v))
