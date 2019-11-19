import xlwt
# 新建一个Excel文件
wb = xlwt.Workbook()
# 新建一个Sheet
ws = wb.add_sheet('Python', cell_overwrite_ok=True)
# 定义字体对齐方式对象
alignment = xlwt.Alignment()
# 设置水平方向
# HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED
# HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
alignment.horz = xlwt.Alignment.HORZ_CENTER
# 设置垂直方向
# VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
alignment.vert = xlwt.Alignment.VERT_CENTER
# 定义格式对象
style = xlwt.XFStyle()
style.alignment = alignment
# 合并单元格write_merge(开始行, 结束行, 开始列, 结束列, 内容, 格式)
ws.write_merge(0, 0, 0, 5, 'Python网络爬虫', style)

# 写入数据wb.write(行,列,内容)
for i in range(2, 7):
    for k in range(5):
        ws.write(i, k, i+k)
    # Excel公式xlwt.Formula
    ws.write(i, 5, xlwt.Formula('SUM(A'+str(i+1)+':E'+str(i+1)+')'))

# 插入图片，insert_bitmap(img, x, y, x1, y1, scale_x=0.8, scale_y=1)
# 图片格式必须为bmp
# x表示行数，y表示列数
# x1表示相对原来位置向下偏移的像素
# y1表示相对原来位置向右偏移的像素
# scale_x，scale_y缩放比例
# ws.insert_bitmap('E:\\test.bmp', 9, 1, 2, 2, scale_x=0.3, scale_y=0.3)

# 保存文件
wb.save('file.xls')
