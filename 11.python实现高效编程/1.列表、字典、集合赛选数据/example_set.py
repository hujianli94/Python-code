#!/usr/bin/env python
#-*- coding:utf8 -*-
#集合解析
import random

date = {random.randint(60,100) for x in range(30)}
set_jiexi = {x for x in date if x >90}
print(set_jiexi)