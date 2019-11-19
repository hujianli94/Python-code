#解码JSON数据
import json

# Python 字典类型转换为 JSON 对象
json_str='''
{"\u53d1\u9001\u8005": "\u4f60\u7684\u670b\u53cb\u5409\u68ee",
"\u63a5\u6536\u8005": "\u5c0f\u5c0f", "\u7f16\u53f7": 2, "\u540d\u79f0":
"\u56fd\u9645\u7535\u6e38\u5927\u4f1aVIP\u95e8\u7968", "\u7c7b\u578b":
"\u7535\u5b50\u51ed\u8bc1", "\u4f7f\u7528\u65f6\u95f4": 20180621,
"\u4f7f\u7528\u8005\u59d3\u540d": "\u5c0f\u5c0f", "\u4f7f\u7528\u5730\u70b9":
"\u706b\u661f\u53f7\u98de\u8239\u767b\u673a\u53e3"}
'''
# 将 JSON 对象转换为 Python 字典
python_dict = json.loads(json_str)
print ("收到的信息:\n", python_dict)
# 显示字典元素
print('================分隔线===================')
for key,value in python_dict.items():
    print (key,"：",value)
