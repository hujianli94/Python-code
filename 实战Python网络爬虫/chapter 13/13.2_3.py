import re
# 将手机号的后4位替换成0
replace_value = re.sub('\d{4}$', '0000', '13435423143')
print(replace_value)
# 将代码后面的注释信息去掉
replace_value = re.sub('#.*$', '', 'num = 0 #a number')
print(replace_value)
