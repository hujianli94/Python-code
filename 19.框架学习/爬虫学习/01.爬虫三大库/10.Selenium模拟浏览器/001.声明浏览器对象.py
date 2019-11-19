#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/9 14:13
# filename: 001.声明浏览器对象.py
from selenium import webdriver

browser = webdriver.Chrome()  # 谷歌浏览器
browser = webdriver.Firefox()  # 火狐浏览器
browser = webdriver.Edge()  # IE浏览器
browser = webdriver.PhantomJS()  # 无头浏览器
browser = webdriver.Safari()  # 手机浏览器
