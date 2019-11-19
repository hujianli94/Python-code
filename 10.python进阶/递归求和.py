#!/usr/bin/env python
# -*- coding:utf8 -*-

def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])


print(mysum([1, 2, 3, 4, 5]))

print()
print("循环语句while ".center(100, "="))
print()
L = [1, 2, 3, 4, 5]
sum = 0
while L:
    sum += L[0]
    L = L[1:]

print(sum)

print()
print("循环语句for ".center(100, "="))
print()

L = [1, 2, 3, 4, 5]
falg = 0
for i in L:
    falg += i
print(falg)
