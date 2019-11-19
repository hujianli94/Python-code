#!/usr/bin/env python
#-*- coding:utf8 -*-
from random import randint
data = [randint(0, 20) for _ in range(30)]
print(data)


from collections import Counter
#统计data中元素出现的次数
c2 = Counter(data)
print(c2.most_common(3))
print(c2)
print(c2[10])


