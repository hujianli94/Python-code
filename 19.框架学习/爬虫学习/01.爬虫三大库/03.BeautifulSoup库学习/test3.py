#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/16 11:01
# filename: test3.py
from bs4 import BeautifulSoup
import requests
import urllib.request
import urllib

# 创建BeautifulSoup对象
# soup = BeautifulSoup(html)

# 用本地的html创建对象
soup = BeautifulSoup(open('index.html'), 'lxml')            #提供本地HTML文件
