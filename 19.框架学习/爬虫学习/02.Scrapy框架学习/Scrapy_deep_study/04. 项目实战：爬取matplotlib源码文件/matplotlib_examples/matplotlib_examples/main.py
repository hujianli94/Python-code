#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/8 16:46
# filename: main.py

from scrapy import cmdline
cmdline.execute("scrapy crawl matplot -o examples.json".split())