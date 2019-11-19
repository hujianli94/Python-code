#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/12 22:53
# filename: example01.py
import urllib.request
import re


def getHtmlCode(url):
    """
    获取url返回的源代码
    :param url:
    :return:
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}

    url1 = urllib.request.Request(url, headers=headers)  ## Request()函数将url添加到头部，模拟浏览器访问


    page = urllib.request.urlopen(url1).read()  # 将url页面的源代码保存成字符串
    page = page.decode('UTF-8')  # 字符串转码
    return page

print(getHtmlCode("https://movie.douban.com/"))
