#json编码示例
import json

# Python类型转换为 JSON 对象
funcs=['飞行','潜水','爬坡','公路狂奔']   
ops=('功能启动','功能关闭','功能切换')

data = {
    'no' : 1,
    'name' : '云霄飞车',
    'type' : '玩具',
    'function' :funcs,
    'operation' :ops
}

#转换成json字符串
json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)
