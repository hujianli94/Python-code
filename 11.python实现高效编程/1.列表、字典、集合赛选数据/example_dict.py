#!/usr/bin/env python
#-*- coding:utf8 -*-
import random
#字典解析
date = { x: random.randint(60, 100) for x in range(1, 21) }
dict_jiexi = {k: v for k, v in date.items() if v > 90}
print(dict_jiexi)
