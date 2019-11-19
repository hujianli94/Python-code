#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/11/9 22:20
# filename: 2.写配置项.py
import configparser

config = configparser.ConfigParser()
config.add_section("Mysqld")            #添加新的配置块
config.set("Mysqld", "port", "3306")    #添加新的配置项
f = open("Background.ini","a+")
config.write(f)
f.close()

