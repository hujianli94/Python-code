#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/5 22:19
# filename: python写入excel表格.py
"""
http://pypi.python.org/pypi/xlwt

安装xlwt
安装方式一样是python setup.py install就可以了，或者直接解压到你的工程目录中。
"""
import xlwt as ExcelWrite


def writeXLS(file_name):
    value = [["name", "jim", "hmm", "lilei"], ["sex", "man", "woman", "man"], ["age", 19, 24, 24],
             ["country", "USA", "CHN", "CHN"]]
    xls = ExcelWrite.Workbook()
    sheet = xls.add_sheet("Sheet1")

    for i in range(4):
        for j in range(0, len(value)):
            sheet.write(j, i, value[i][j])
            xls.save(file_name)


if __name__ == '__main__':
    writeXLS("./test_write.xls")
