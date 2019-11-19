#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/17 23:46
# filename: map()函数.py
users = ["Tony", "Tom", "Ben", "Alex"]
user_map = map(lambda u: str(u).lower(), users)
print(list(user_map))

user_map2 = map(lambda u: str(u).lower(), filter(lambda u: str(u).startswith("T"), users))
print(list(user_map2))
