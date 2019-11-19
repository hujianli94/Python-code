#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/22 18:57
# filename: CSV数据交换格式-写.py

# writer()函数
# 先读取csv文件，再将读取的数据处理后写入新的csv中
import csv

headers = ['编号', '书名', '作者', '出版社', '出版时间', '级别']
rows = [
    "10,软件工程1,胡建力,机械工业出版社,199407226517,2",
    "11,汇编语言1,胡建力2,北京工业大学出版社,199407126517,2",
    "12,计算机语言1,胡建力3,经济科学出版社,199417126517,1",
    "13,FLASH精选1,胡建力4,中国纺织出版社,199417126511,3",
    "14,JAVA基础1,胡建力5,电子工业出版社,199117126511,3",
    "15,JAVA程序设计1,胡建力6,世界出版社,199117126512,2",
    "16,新东方英语1,胡建力7,外语出版社,192117126512,1"
]

with open("test.csv", "r", encoding="utf-8") as rf:
    reader = csv.reader(rf)
    print("开始读取test.csv文件内容......................")
    with open("test_bak.csv", "w", newline="", encoding="utf-8") as wf:
        writer = csv.writer(wf, delimiter=",")
        header = ["|".join(headers)]
        print("开始写入标题header 到test_bak.csv文件......................")
        writer.writerow(header)
        print("开始写入文件旧数据 到test_bak.csv文件......................")
        for row in reader:
            # print(row)
            writer.writerow(row)
        rows_list = [str(row).split(",") for row in rows]
        print("开始写入新的数据 到test_bak.csv文件......................")
        for row_new in rows_list:
            writer.writerow(row_new)
    print("读写完毕，查看写入后的内容................")

with open("test_bak.csv", "r", encoding="utf-8") as rf:
    reader = csv.reader(rf)
    for info in reader:
        print("|".join(info))




