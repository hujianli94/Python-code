#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/15 18:34
# filename: 序列化，把对象写入文件.py
try:
    import cPickle as pickle
except ImportError:
    import pickle

dicData = {
    'data1': [2, 8, 4, 3],
    'data2': ('str1', 'str2'),
    'data3': None
}

listData = [1, 2, 3]
output = open('file.pkl', 'wb')
pickle.dump(dicData, output)
pickle.dump(listData, output, -1)
output.close()




