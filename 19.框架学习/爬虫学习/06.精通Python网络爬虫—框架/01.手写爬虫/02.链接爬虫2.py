#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/20 19:08
# filename: 02.链接爬虫2.py
import re
import urllib.request


class A:
    def __init__(self):
        self.headers = ("user-agent",
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36")
        self.url = "https://blog.csdn.net"

    def get_html(self, url):
        # 模拟成浏览器
        opener = urllib.request.build_opener()
        opener.addheaders = [self.headers]
        # 将opener安装为全局
        urllib.request.install_opener(opener)
        file = urllib.request.urlopen(url)
        data = str(file.read().decode("utf-8"))
        return data

    def get_link(self):
        data = self.get_html(self.url)
        pat1 = '(https?://[^\s)";]+\.(\w|/)*)'
        re_data = re.compile(pat1, re.S).findall(data)
        list_links = list(set(re_data))
        return list_links


if __name__ == '__main__':
    h1 = A()
    links = h1.get_link()
    for link in links:
        print(link)
