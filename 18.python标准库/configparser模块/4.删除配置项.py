#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/11/9 22:27
# filename: 4.删除配置项.py
import configparser

ini_name = "Background.ini"
config = configparser.ConfigParser()
config.read(ini_name)
config.remove_option("Mysqld", "port")  # 删除配置项
config.remove_section("Mysqld")  # 删除配置块
f = open(ini_name, "w+")
config.write(f)
f.close()