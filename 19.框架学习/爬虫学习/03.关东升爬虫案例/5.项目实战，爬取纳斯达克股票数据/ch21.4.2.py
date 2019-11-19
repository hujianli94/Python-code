#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/8 16:02
# filename: ch21.4.2.py

"""
项目实战，爬取纳斯达克股票数据
"""
import urllib.request
import hashlib
from bs4 import BeautifulSoup

import os

url = "https://www.laohu8.com/hq/s/02128"


def validateUpdate(html):
    """
    验证数据是否更新，更新返回True，未更新返回False
    :param html:
    :return:
    """

    # 创建md5对象
    md5obj = hashlib.md5()
    md5obj.update(html.encode(encoding="utf-8"))
    md5code = md5obj.hexdigest()
    print(md5code)

    old_md5code = ''
    f_name = 'md5.txt'

    if os.path.exists(f_name):
        with open(f_name, "r", encoding="utf-8") as f:
            old_md5code = f.read()

    if md5code == old_md5code:
        print("数据没有更新....")
        return False
    else:
        # 把新的md5码写入到文件中
        with open(f_name, "w", encoding="utf-8") as f:
            f.write(md5code)
            print("数据更新..")
        return True


req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    data = response.read()
    html = data.decode()
    sp = BeautifulSoup(html, 'html.parser')
    #返回指定CSS选择器的div标签列表
    div = sp.select("#root > div > div.column-wrap.clear > div.main-side > div:nth-child(1) > div > div.quote-wrap > div.quote-main > div")
    divstring = div[0]
