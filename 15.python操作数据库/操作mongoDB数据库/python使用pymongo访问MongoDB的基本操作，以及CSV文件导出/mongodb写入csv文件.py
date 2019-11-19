#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/29 16:33
# filename: mongodb写入csv文件.py
# 导出数据库所有记录的标准模版
from pymongo import MongoClient
import csv

# 初始化数据库
stus = MongoClient().mydb.taobao_renaiping  # 一条语句实现连接到集合

# 将数据写入到CSV文件中
# 如果直接从mongod booster导出, 一旦有部分出现字段缺失，那么会出现结果错位的问题

# newline='' 的作用是防止结果数据中出现空行，专属于python3
with open("mongo-csv.csv", "w", newline='', encoding='gbk') as csvfileWriter:
    writer = csv.writer(csvfileWriter)
    # 先写列名
    # 写第一行，字段名
    fieldList = [
        "_id",
        "商店名称",
        "价格",
        "商品链接",
        "购买人数",
        "商品",
        "城市",
    ]
    writer.writerow(fieldList)

    allRecordRes = stus.find()
    # 写入多行数据
    for record in allRecordRes:
        # print("record = {record}")
        recordValueLst = []
        for field in fieldList:
            if field not in record:
                recordValueLst.append("None")
            else:
                recordValueLst.append(record[field])
        try:
            writer.writerow(recordValueLst)
        except Exception as e:
            print("write csv exception. e = {e}")
