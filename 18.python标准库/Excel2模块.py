#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/18 10:38
# filename: Excel2模块.py
import xlsxwriter

workbook = xlsxwriter.Workbook("chart.xlsx")  # 创建一个Excel文件
worksheet = workbook.add_worksheet()  # 创建一个工作表对象
chart = workbook.add_chart({"type": "column"})  # 窗机一个图标对象

# 定义数据表头列表
title = ["业务名称", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日", "平均流量"]

# 定义5频道名称
buname = ["业务官网", "新闻中心", "购物频道", "体育频道", "亲子频道"]

# 定义5频道一周7天的流量数据
data = [
    [150, 152, 158, 149, 155, 145, 148],
    [89, 88, 95, 56, 48, 100, 99],
    [200, 201, 222, 234, 180, 179, 190],
    [77, 88, 99, 55, 66, 48, 90],
    [81, 82, 83, 84, 85, 86, 87],
]

format = workbook.add_format()
format.set_border(1)

format_title = workbook.add_format()
format_title.set_border(1)
format_title.set_bg_color('#cccccc')
format_title.set_align('center')
format_title.set_bold()

format_ave = workbook.add_format()
format_ave.set_border(1)
format_ave.set_num_format('0.00')

worksheet.write_row('A1', title, format_title)
worksheet.write_column('A2', buname, format)
worksheet.write_row('B2', data[0], format)
worksheet.write_row('B3', data[1], format)
worksheet.write_row('B4', data[2], format)
worksheet.write_row('B5', data[3], format)
worksheet.write_row('B6', data[4], format)


def chart_series(cur_row):
    worksheet.write_formula('I' + cur_row, \
                            '=AVERAGE(B' + cur_row + ':H' + cur_row + ')', format_ave)
    chart.add_series({
        'categories': '=Sheet1!$B$1:$H$1',
        'values': '=Sheet1!$B$' + cur_row + ':$H$' + cur_row,
        'line': {'color': 'black'},
        'name': '=Sheet1!$A$' + cur_row,
    })


for row in range(2, 7):
    chart_series(str(row))

# chart.set_table()
# chart.set_style(30)
chart.set_size({'width': 577, 'height': 287})
chart.set_title({'name': u'业务流量周报图表'})
chart.set_y_axis({'name': 'Mb/s'})

worksheet.insert_chart('A8', chart)
workbook.close()
