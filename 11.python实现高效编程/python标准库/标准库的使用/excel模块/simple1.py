#!/usr/bin/env python
#-*- coding:utf8 -*-
import xlsxwriter
workbook = xlsxwriter.Workbook("hujianli.xlsx")
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A',20)          #设定第一列A宽度为20像素
bold = workbook.add_format({'bold': True})  # 定义一个加粗的格式对象
worksheet.write('A1','hello')
worksheet.write('A2','hello hujianli',bold) ##A2单元格写入'World'并引用加粗格式对象bold
worksheet.write('B2',u'胡建力',bold)
worksheet.write(2,0,32)
worksheet.write(3,0,35.5)
worksheet.write(4,0,'=SUM(A3: A4)')
worksheet.insert_image('B5','image/server.png')
workbook.close()
