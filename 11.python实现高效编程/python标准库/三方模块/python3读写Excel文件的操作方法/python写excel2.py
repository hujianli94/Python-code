#!/usr/bin/env python
#-*- coding:utf8 -*-
import xlwt
import copy

# 写Excel
def write_excel():
    style1=xlwt.XFStyle()
    style1.font=xlwt.Font()
    style1.font.name="Times New Roman"
    style1.font.bold=True
    style1.font.height=220
    style1.color_index=4

    style2=copy.deepcopy(style1)
    style2.font.bold=False

    f=xlwt.Workbook()
    sheet1=f.add_sheet('学生',cell_overwrite_ok=True)
    title=["姓名",'出生日期','爱好']
    content=[
        ['陈胜','吴广','项羽','刘邦'],
        ['1978/3/1','1983/4/7','1990/5/8','1976/9/11'],
        ['篮球','篮球','足球','麻将'],
    ]
    # 写第一行(标题)
    for i in range(0,len(title)):
        # 行,列,值,Style
        sheet1.write(0,i,title[i],style1)
    # 写第一列(内容)
    for i in range(0,len(content)):
        for j in range(0,len(content[i])):
            # 行,列,值,Style
            sheet1.write(j+1,i,content[i][j],style2)

    # 合并列单元格(1~2行，2~2列)
    sheet1.write_merge(1,2,2,2,'篮球')
    f.save('student.xls')

if __name__=='__main__':
    write_excel()