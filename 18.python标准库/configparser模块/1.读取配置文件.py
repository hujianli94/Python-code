#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/11/9 22:11
# filename: 1.读取配置文件.py
import configparser

config = configparser.ConfigParser()
config.read("Background.ini")
sections = config.sections()  # 返回所有的配置块
print("\033[31m配置块\033[0m：", sections)
o = config.options("Background2")  # 返回所有的配置项
print("\033[31m配置项:\033[0m", o)

v = config.items("Background2")  # 返回配置项的内容
print("\033[31m内容：\033[0m", v)
# 根据配置块和配置项返回内容
access = config.get("Background", "Outside-RightMargin")
print(access)

Image_info = config.get("Background", "Image")
print(Image_info)
