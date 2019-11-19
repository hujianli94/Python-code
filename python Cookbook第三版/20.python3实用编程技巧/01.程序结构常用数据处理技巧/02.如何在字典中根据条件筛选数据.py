#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/17 22:49
# filename: 02.如何在字典中根据条件筛选数据.py

from random import randint

# 生成字典
d = {'student%d' % i: randint(100, 200) for i in range(1, 21)}
print(d)

# 方法1
d1 = {k: v for k, v in d.items() if v > 150}
print(d1)
#{'student15': 185, 'student1': 171, 'student7': 192, 'student19': 191, 'student2': 158, 'student16': 152, 'student13': 168, 'student9': 173}

# 方法2
d2 = dict(filter(lambda item: item[1] > 150, d.items()))
print(d2)
#{'student15': 185, 'student1': 171, 'student7': 192, 'student19': 191, 'student2': 158, 'student16': 152, 'student13': 168, 'student9': 173}