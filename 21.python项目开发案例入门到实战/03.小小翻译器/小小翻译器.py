#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/24 14:04
# filename: 小小翻译器.py
"""
八度翻译开放平台提供的API接入文档链接如下：
http://api.fanyi.baidu.com/api/trans/product/apidoc

"""

from urllib import request

# req = request高级用法.Request("http://fanyi.baidu.com")
# response = request高级用法.urlopen(req)
# html = response.read()
# html = html.decode("utf-8")
# print(html)


if __name__ == '__main__':
    # res = request高级用法.urlopen("http://fanyi.baidu.com")
    # html = res.read()
    # html = html.decode("utf-8")
    # print(html)
    request.urlretrieve("https://www.zut.edu.cn/__local/9/22/C9/9A4213A2F267EA56E38F0CD50DE_1B72A6DA_B24C.jpg",
                        "aaa.jpg")
