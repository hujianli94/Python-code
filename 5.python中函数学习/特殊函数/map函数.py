#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
map(add，number)

Docstring:
map(func, *iterables) --> map object

Make an iterator that computes the function using arguments from
each of the iterables.  Stops when the shortest iterable is exhausted
'''

number = list(range(10))
map_num = list(map(lambda x:x+3,number))
print(map_num)

iterms = [1,2,3,4]
print(list(map(lambda x:x**2,iterms)))



#实现2个列表相加
lst1 = [1,2,3,4,5,6]
lst2 = [5,6,7,8,9,9]
print(list(map(lambda x,y:x+y,lst1,lst2)))


#实现3个列表相加
lst1 = [1,2,3,4,5]
lst2= [6,7,8,9,0]
lst3= [7,8,9,2,1]
print(list(map(lambda x,y,z:x+y+z,lst1,lst2,lst3)))

















