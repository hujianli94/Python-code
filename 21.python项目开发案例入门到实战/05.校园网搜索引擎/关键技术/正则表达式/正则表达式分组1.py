#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/12 17:01
# filename: 正则表达式分组1.py
import re

# 用()表示的就是要提取的分组^(\d{3})\-(\d{3,8})$ 分别定义了两个组。可以直接从匹配的字符串中提取出区号和本地号码

m = re.match(r'^(\d{3})\-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))
