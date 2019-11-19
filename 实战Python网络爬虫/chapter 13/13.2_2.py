import re
# 匹配字符串中所有含有'oo'字符的单词
# 当正则表达式中没有圆括号时，列表中的字符串表示整个正则表达式匹配的内容
find_value = re.findall('\w*oo\w*', 'woo this foo is too')
print(find_value)

# 获取字符串中所有的数字字符串
# 当正则表达式中只带有一个圆括号时，列表中的元素为字符串，并且该字符串的内容与括号中的正则表达式相对应.
find_value = re.findall('.*?(\d+).*?', 'adsd12343.jl34d5645fd789')
print(find_value)

# 提取字符串中所有的有效的域名地址
# 正则表达式中有多个圆括号时，返回匹配成功的列表中的每一个元素都是由一次匹配成功后，
# 正则表达式中所有括号中匹配的内容组成的元组。
add = 'https://www.net.com.edu//action=?asdfsd and other https://www.baidu.com//a=b'
find_value = re.findall('((w{3}\.)(\w+\.)+(com|edu|cn|net))', add)
print(find_value)
