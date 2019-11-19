import xlrd
wb = xlrd.open_workbook('file.xls')
# 获取Sheets总数
ws_count = wb.nsheets
print('Sheets总数：', ws_count)
# 通过索引顺序获取Sheets
# ws = wb.sheets()[0]
# ws = wb.sheet_by_index(0)
# 通过Sheets名获取Sheets
ws = wb.sheet_by_name('Python')
# 获取整行的值（以列表返回内容）
row_value = ws.row_values(3)
print('第4行数据：', row_value)
# 获取整列的值（以列表返回内容）
row_col = ws.col_values(3)
print('D列数据：', row_col)

# 获得所有行列
nrows = ws.nrows
ncols = ws.ncols
print('总行数：', nrows, '，总列数：', ncols)

# 读取excel的数据，确保excel里面不能有图片
# 获取某个单元格内容cell(行, 列)
cell_F3 = ws.cell(2, 5).value
print('F3内容：', cell_F3)

# 使用行列索引获取某个单元格内容
row_F3 = ws.row(2)[5].value
col_F3 = ws.col(5)[2].value
print('F3内容：', row_F3, 'F3内容：', col_F3)
