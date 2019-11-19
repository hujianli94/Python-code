#!/usr/bin/env python
#-*- coding:utf8 -*-
def list_arg(lst=[]):
    """
    当lst第一次调用之后，会成为abc，lst在外部再次传入时，是带有参数的，默认lst=[]不生效
    :param lst:
    :return:
    """
    lst.append("abc")
    print(lst)

list_arg()
list_arg()
list_arg()


print("="*100)

def list_arg2(lst=None):
    lst = [] if lst is None else lst
    lst.append("abc")
    print(lst)

list_arg2()
list_arg2()
list_arg2()