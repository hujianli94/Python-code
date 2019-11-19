#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/9 14:49
# filename: 005.多个节点.py
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
lis = browser.find_element_by_css_selector('.service-bd li')
print(lis)
browser.close()
