str = 'ABCDABC'
# 查找全部
print(str.index('A'))
# 输出内容：0

# 从字符串第四个开始查找
print(str.index('A', 3))
# 输出内容：4

# 从字符串第二个到第六个开发查找
print(str.index('C', 1, 5))
# 输出内容：2

# 查找不存在的内容
print(str.index('E'))
# 输出内容：ValueError: substring not found
