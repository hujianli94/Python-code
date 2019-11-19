import csv
# 若存在文件，打开csv文件，若不存在即新建文件
# 如不设置newline=''，每行数据会隔一行空白行
csvfile = open('csv_test.csv', 'w', newline='')
# 将文件加载到csv对象中
writer = csv.writer(csvfile)
# 写入一行数据
writer.writerow(['姓名', '年龄', '电话'])
# 多行数据写入
data = [
    ('小P', '18', '138001380000'),
    ('小Y', '22', '138001380000')
]
writer.writerows(data)
# 关闭csv对象
csvfile.close()
