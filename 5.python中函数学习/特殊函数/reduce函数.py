#!/usr/bin/env python
#-*- coding:utf8 -*-
from functools import reduce
'''
Docstring:
reduce(function, sequence[, initial]) -> value

Apply a function of two arguments cumulatively to the items of a sequence,
from left to right, so as to reduce the sequence to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
of the sequence in the calculation, and serves as a default when the
sequence is empty.
Type:      builtin_function_or_method
'''
lst = [1,2,3,4,5,6,7]
num = reduce(lambda x,y:x+y,lst)
print(num)
