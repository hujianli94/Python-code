#!/usr/bin/env python
#-*- coding:utf8 -*-
hu = eval('3+4')         # 将字符串当表达式求值 得到7
print(hu)


exec('a=100')
print(a)

s = "for i in range(0,10):print(i)"
c = compile(s,',',"exec")
exec(c)

x=3
y=4
s2 = "3*x+4*y"
c2 = compile(s2, '', 'eval')
result = eval(c2)
print(result)