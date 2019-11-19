#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/11/9 22:23
# filename: 3.修改配置项.py
import configparser

ini_name = "Background.ini"
config = configparser.ConfigParser()
config.read(ini_name)
config.set("Mysqld", "port", "3307")  # 修改配置项
f = open(ini_name, "r+")
config.write(f)
f.close()
