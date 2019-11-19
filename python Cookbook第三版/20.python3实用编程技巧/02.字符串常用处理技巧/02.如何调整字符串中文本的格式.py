#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/18 22:49
# filename: 02.如何调整字符串中文本的格式.py
import re

# 调整时间显示的格式
s = "2019-08-15 23:23:12"

s1 = re.sub(r'(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',s)
print(s1)       #08/15/2019 23:23:12
