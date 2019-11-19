#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/9 14:22
# filename: 003.访问页面.py

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
print(browser.page_source)
browser.close()
