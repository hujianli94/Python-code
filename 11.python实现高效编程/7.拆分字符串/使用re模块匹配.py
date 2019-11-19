#!/usr/bin/env python
#-*- coding:utf8 -*-
import re
s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
print(re.split(r'[,;\t|]+',s))  # +号，对于前面的形式，至少有一个或者多个
