#!/usr/bin/env python
#-*- coding:utf8 -*-
def filterchar(string):
    '''
    :param string:  要过滤的字符串
    :return: None
    '''
    import re       #导入re模块
    pattern = r"(黑客)|(抓包)|(监听)|(Trojan)"    #模式字符串
    sub = re.sub(pattern,"@_@",string)          #进行模式匹配
    print(sub)

string = " 我是一个黑客，我喜欢抓包，研究Trojan...."


def empty():
    pass

filterchar(string)      #调用函数，传入参数值
