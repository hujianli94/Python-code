#!/usr/bin/env python
#-*- coding:utf8 -*-
import xlrd
from datetime import date,datetime
import logging

'''
filename="student.xls"

logging.basicConfig(level=logging.ERROR)

def read_excel():
    # 打开文件
    wb=xlrd.open_workbook(filename=filename)
    # 获取所有表格名字
    logging.info(wb.sheet_names())
    # INFO:root:['学生']
    # 通过名字获取表格
    sheet1=wb.sheet_by_name('学生')
    logging.info(sheet1)
    # INFO:root:<xlrd.sheet.Sheet object at 0x0000024A26111F60>
    logging.info(sheet1.name)
    # INFO:root:学生
    logging.info(sheet1.nrows)
    # INFO:root:5
    logging.info(sheet1.ncols)
    # INFO:root:3
    # 获取行内容
    print(sheet1.row_values(2))
    # ['吴广', '1983/4/7', '']
    # 获取列内容
    print(sheet1.col_values(2))
    # ['爱好', '篮球', '', '足球', '麻将']
    # 获取表格里的内容
    print(sheet1.cell(2,1).value)
    # 1983/4/7
    # ctype :  0 empty，1 string，2 number， 3 date，4 boolean，5 error
    print(sheet1.cell(2,1).ctype)
    # 1
    # 日期格式处理(未验证)
    # date_value = xlrd.xldate_as_tuple(sheet1.cell_value(1,2),wb.datemode)
    # date(*date_value[:3]).strftime('%Y/%m/%d')

    # 获取合并单元格的内容
    print(sheet1.merged_cells)
    # merged_cells返回的这四个参数的含义是：(row,row_range,col,col_range)
    # 即(1, 3, 4, 5)的含义是：第1到2行（不包括3）合并，(7, 8, 2, 5)的含义是：第2到4列合并。

if __name__=='__main__':
    read_excel()
'''


import xlrd
book = xlrd.open_workbook("student.xls")

#sheets可以获取所有的表，返回一个sheet对象
book.sheets()
#另一种方式
sheet = book.sheet_by_index(0)

#访问行数
print(sheet.nrows)

#访问列数
print(sheet.ncols)

#获取单元格内容
cell = sheet.cell(0, 0)
print(cell.ctype)
print(cell.value)
# sheet.row(1,1)