#!/usr/bin/env python
# -*- coding:utf8 -*-
number = range(-5, 5)
print(list(number))
filter1 = filter(lambda x: x > 0, list(number))
print(list(filter1))

list2 = [x for x in number if x > 0]
print(list2)

string = filter(lambda x: x != "h", "hujianli")
print(list(string))
