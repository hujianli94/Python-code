#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/6 13:26
# filename: 09.尽量使用enumerate取代range.py
flavor_list = ['vanilla','chocolate','pecan','strawberry']
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print("%d : %s " % (i, flavor))

print()
for i,flavor in enumerate(flavor_list,1):
    print("{}:{}".format(i,flavor))


"""
1.enumerate函数提供了一种精简的写法，可以在遍历迭代器时获知每个元素的索引
2.尽量用enumerate来改写那种将range与下标访问相结合的序列遍历代码
3.可以给enumerate提供第二个参数，以指定开始计数时所用的值，（默认为0）
"""