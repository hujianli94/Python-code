#!/usr/bin/env python
#-*- coding:utf8 -*-、
'''
with expression as target:
    with-boby
'''
with open('message.txt','r',encoding='utf-8') as file:
    print(file.read())

print('\n 即将显示------\n')
print('文件是否关闭了？', file.closed)

