#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/31 17:03
# filename: 03.设计函数对字符串进行获取.py


with open("test.html", "r", encoding="utf-8") as f:
    info = f.read()

# print(info)


def find_url(url):
    '''
    获取url信息
    :param url:
    :return:
    '''
    url = str(url).split()
    for i in url:
        if i.startswith("href"):
            i = i.split(">")[0]
            print(i)
find_url(info)
