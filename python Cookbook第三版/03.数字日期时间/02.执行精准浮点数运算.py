#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/9 16:36
# filename: 02.执行精准浮点数运算.py

# a = 4.2
# b = 2.1
# print(a + b)  # 6.300000000000001
#
# print((a + b) == 6.3)  # False

from decimal import Decimal

a1 = Decimal(4.2)
b1 = Decimal(2.1)

print(a1 + b1)
print((a1 + b1) == Decimal('6.3'))

import math
example1 = [1.000001, 2.0001, 3.001, 4.2]
print(sum(example1))
print(math.fsum(example1))
