#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/28 19:50
# filename: 11.通过某个关键字排序一个字典列表.py

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}

]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter("fname"))
rows_by_uid = sorted(rows, key=itemgetter("uid"))
for rows_by_f in rows_by_fname:
    print(rows_by_f)

print()
for rows_by_u in rows_by_uid:
    print(rows_by_u)
print()

rows_by_lfname = sorted(rows, key=itemgetter("lname", "fname"))
for rows_by_lfna in rows_by_lfname:
    print(rows_by_lfna)
