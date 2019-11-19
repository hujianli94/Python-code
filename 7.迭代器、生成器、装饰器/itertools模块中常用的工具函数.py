#!/usr/bin/env python
#-*- coding:utf8 -*-
import itertools
for i in itertools.count(1,3):
    #从1开始，步长为3
    print(i)
    if i >= 10:
        break

print("".center(100,"="))
print()

x = 0
for i in itertools.cycle(['a','b']):
    #无限循环seq
    print(i)
    x += 1
    if x >= 6:
        break
print()

print(list(itertools.repeat("hu",10)))
#循环迭代hu，循环10次


print(list(itertools.chain([1,3],[2,3])))
#链接迭代，将2个seq连接起来迭代

print(list(itertools.compress([1,2,3,4],[1,[],True,3])))

print(list(itertools.dropwhile(lambda x:x>6,[8,9,1,2,8,9])))
#当不满足lambda中情形，为假时，循环后面的seq

print(list(itertools.takewhile(lambda x:x>10,[18,19,1,21,8,9])))
#与dropwhile相反

for its in itertools.tee([0,1],4):
    for it in its:
        print(it)

print(list(itertools.permutations("abc",3)))
#迭代序列中3个元素的排列

print(list(itertools.combinations('abcd',3)))
#迭代序列中3个元素的组合


