str = 'ABCDABC'
# 分割全部
print(str.split('B'))
# 输出内容：['A', 'CDA', 'C']
# 分割一次
print(str.split('B', 1))
# 输出内容：['A', 'CDABC']
