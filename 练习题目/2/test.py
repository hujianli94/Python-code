#!/usr/bin/env python
#-*- coding:utf8 -*-
L = [2, 5, 3, 8, 10, 1]
print(sorted(L))

ss = "123456"
print(ss[::-1])

d = {"a":1,"b":2,"c":3}
for key, value in d.items():
    print(key, "====>", value)
d["d"] = 4
print(d)

for a in range(2,100):
    if 100%a == 0:
        print(a, end=",")

