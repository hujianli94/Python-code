#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/18 10:30
# filename: simple01.py

from wxpy import *

# 初始化机器人，扫码登录
# cache_path保持登录，Bot初始化中可以加入参数：console_qr是否在控制台显示二维码
bot = Bot(cache_path=True)

print("登录成功")

bot.logout()
print("退出登录成功")