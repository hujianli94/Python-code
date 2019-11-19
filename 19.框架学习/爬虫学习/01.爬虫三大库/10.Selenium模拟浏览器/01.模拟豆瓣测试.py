#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/23 17:25
# filename: 01.模拟豆瓣测试.py

from selenium import webdriver
import time
from lxml import etree

# 动态页面获取之二
driver = webdriver.PhantomJS()
driver.get("https://www.douban.com/")

# 获取源码
html = driver.page_source
root = etree.HTML(html)
iframes = root.xpath('//div[contains(@class,"login")]/iframe/@src')[0]

# 因为登录是iframe引入的  所以重新再开一个
driver.get("https:" + iframes)

# 模拟点击  切换到密码登录
driver.find_element_by_class_name("account-tab-account").click()
time.sleep(1)
# 输入账号和密码
driver.find_element_by_id("username").send_keys("13262662216")
driver.find_element_by_id("password").send_keys("cu0gu0ai@94")

# 点击登录
driver.find_element_by_class_name("btn-account").click()

time.sleep(4)
#打印网页源码
print(driver.page_source)

# 快照保存
driver.save_screenshot('douban_denglu.png')
# 退出
driver.quit()
