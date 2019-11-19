#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/27 14:08
# filename: demo3.py
import requests
from bs4 import BeautifulSoup

respones = requests.get("http://news.baidu.com")

soup = BeautifulSoup(respones.text, features="lxml")
print(soup.find("title").text)