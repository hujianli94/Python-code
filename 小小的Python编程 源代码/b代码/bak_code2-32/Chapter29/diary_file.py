#创建文本文件
file_name="C:\Workspace\Chapter29\diary.book"
fo=open(file_name,'a+')
print("fo对象:",type(fo))
print("文件名: ", fo.name)
print("是否已关闭 : ",fo.closed)
print("访问模式 : ",fo.mode)
print("编码:",fo.encoding)
fo.close()
print("是否已关闭 : ",fo.closed)
