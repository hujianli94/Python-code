#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/20 18:23
# filename: 02.链接爬虫1.py
import re
import urllib.request


class Link_get_Info(object):
    def __init__(self):
        self.__headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
        }
        self.count = 0
        self.__url = "https://blog.csdn.net"

    def getHtmlCode(self):
        """
        获取url返回的源代码
        :param url:
        :return:
        """

        url1 = urllib.request.Request(self.__url, headers=self.__headers)  ## Request()函数将url添加到头部，模拟浏览器访问

        page = urllib.request.urlopen(url1).read()  # 将url页面的源代码保存成字符串
        page = page.decode('UTF-8')  # 字符串转码
        return page

    def get_link_info(self):
        data = self.getHtmlCode()
        # 根据需求构建好链接表达式
        pat = '(https?://[^\s)";]+\.(\w|/)*)'
        link = re.compile(pat).findall(data)
        # 去除重复元素
        link = list(set(link))
        return link


if __name__ == '__main__':
    t1 = Link_get_Info()
    list_links = t1.get_link_info()
    for list_link in list_links:
        print(list_link)
