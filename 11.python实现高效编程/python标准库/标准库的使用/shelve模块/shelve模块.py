#!/usr/bin/env python
#-*- coding:utf8 -*-
import shelve
#写入数据
'''
f=shelve.open(r'sheve.txt')
f['stu1_info'] = {'name':'egon','age':18,'hobby':['piao','smoking','drinking']}
f['stu2_info'] = {'name':'gangdan','age':53}
f['school_info'] = {'website':'http://www.pypy.org','city':'beijing'}
f.close()
'''

#读取数据
'''
shelveFile_read2 = shelve.open("sheve.txt")
print(type(shelveFile_read2))
print(shelveFile_read2['stu1_info'])
print(shelveFile_read2['school_info'])

print(list(shelveFile_read2.keys()))
print(list(shelveFile_read2.values()))
'''
#写入数据
'''
shelveFile = shelve.open('mydata')
shelveFile['cats'] = ['hujianli', 'xiaojian2', 'huxiaojian3']
shelveFile.close()
'''

#读取数据
'''
shelveFile_read = shelve.open('mydata')
print(type(shelveFile_read))
print(shelveFile_read['cats'])
'''