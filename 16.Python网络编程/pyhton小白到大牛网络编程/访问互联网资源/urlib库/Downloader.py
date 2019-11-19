#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/24 11:12
# filename: Downloader.py
import urllib.parse
import urllib.request

url = 'http://www.51work6.com/template/veikei_dz_com_20130920_color/images/logo.png'

with urllib.request.urlopen(url) as reponse:
    data = reponse.read()
    f_name = 'download.png'
    with open(f_name, 'wb') as f:
        f.write(data)
        print("下载文件成功")
