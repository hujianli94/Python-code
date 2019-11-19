#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/10 14:37
# filename: 字典格式化.py
temp = "书名是：%(name)s,价格是:%(price)010.2f,出版社是:%(publish)s"
book1 = {'name': "疯狂python讲义", 'price': 88.9, 'publish': '电子社1'}
print(temp % book1)
book2 = {'name': "疯狂java讲义", 'price': 78.9, 'publish': '电子社2'}
print(temp % book2)