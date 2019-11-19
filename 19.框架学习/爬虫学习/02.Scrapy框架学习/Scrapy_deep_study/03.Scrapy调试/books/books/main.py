#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/1 19:35
# filename: main.py

from scrapy import cmdline
cmdline.execute("scrapy crawl booksspider -o books.csv".split())