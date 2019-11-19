#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/15 18:38
# filename: 反序列化，磁盘读取到内存.py

try:
    import cPickle as pickle
except ImportError:
    import pickle
    import pprint

pklFile = open('file.pkl', 'rb')
data1 = pickle.load(pklFile)
pprint.pprint(data1)

data2 = pickle.load(pklFile)
pprint.pprint(data2)
pklFile.close()

'''
{'data1': [2, 8, 4, 3], 'data2': ('str1', 'str2'), 'data3': None}
[1, 2, 3]
'''