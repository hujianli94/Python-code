#!/usr/bin/env python
#-*- coding:utf8 -*-
import json
date = {"name":"hujianli",
        "sex":"man",
        "age":18}

#字典转为json格式的字符串
js = json.dumps(date)
print(js)
print(type(js))

#json格式字符串转为字典
js_dic = json.loads(js)
print(js_dic)
print(type(js_dic))

print("json写文件".center(100, "*"))
#json写文件
with open("date.json", "w") as f:
    json.dump(date, f, indent=4)


#将列表序列化后写入文件
hu = [11, 22, 33, 44]
json.dump(hu, open("db", 'w'), indent=4)

