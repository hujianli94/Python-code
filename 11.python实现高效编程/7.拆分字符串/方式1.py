#!/usr/bin/env python
#-*- coding:utf8 -*-
def mySplixt(s,ds):
    res = [s]
    print(res)

    for d in ds:
        t = []
        map(lambda x: t.extend(x.split(d)), res)
        res = t

    return [x for x in res if x]

s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
print(mySplixt(s, ';,|\t'))
