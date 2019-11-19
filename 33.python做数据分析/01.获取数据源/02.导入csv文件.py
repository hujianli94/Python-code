#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/31 13:00
# filename: 02.导入csv文件.py
import pandas as pd

df = pd.read_csv(r'test002.csv',encoding="utf8")
print(df)