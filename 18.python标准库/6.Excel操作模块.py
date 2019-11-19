#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/18 10:03
# filename: 6.Excel操作模块.py
import xlsxwriter

workbook = xlsxwriter.Workbook("测试表格.xlsx")  # 创建一个Excel文件
worksheet = workbook.add_worksheet()  # 创建一个工作表对象

worksheet.set_column("A:A", 20)  # 第一列A宽度为20像素
bold = workbook.add_format({"bold": True})  # 定义加粗格式对象
worksheet.write("A1", "Hello")  # A1单元格写入"Hello"
worksheet.write("A2", "World", bold)  # A2单元格写入"World"并引用加粗格式对象bold
worksheet.write("B2", "胡建力学python", bold)  # B2单元格写入中文并引用加粗格式对象bold

worksheet.write(2, 0, 32)  # 用行列表示法写入数字"32"和"35"
worksheet.write(3, 0, 35.5)
worksheet.write(4, 0, '=SUM(A3:A4)')
worksheet.insert_textbox("B5", "content.txt")  # 在B5单元格插入txt文件
workbook.close()
