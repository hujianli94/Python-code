#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/22 12:27
# filename: python操作NOSQL数据类型.py
import dbm

with dbm.open('mydb', 'c') as db:
    db['name'] = 'hujianli'  # 更新数据
    print(db['name'].decode())  # 取出数据

    age = int(db.get('age', b'18').decode())  # 取出数据
    print(age)

    if 'age' in db:  # 判断是否存在age数据
        db['age'] = '20'  # 或者b'20'

    del db['name']  # 删除name数据

"""
1）写入数据。如果key不存在创建键，如果存在覆盖values
    db['name'] = 'hujianli'

2）读取数据
    age = int(db.get('age', b'18').decode())  # 取出数据
    print(age)

3）删除数据
    del db['name']  # 删除name数据
    
4）查找数据
    if 'age' in db:  # 判断是否存在age数据
    
"""