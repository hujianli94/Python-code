#!/usr/bin/env python
# -*- coding:utf8 -*-
def cube(name, **nature):
    # 定义一个字典
    all_nature = {"x": 1,
                  "y": 1,
                  "z": 1,
                  "color": "white",
                  "weight": 1}

    all_nature.update(nature)  # 将第二个参数收集到的数据用来更新字典
    print(name, "立方体的属性：")
    print("体积", all_nature["x"] * all_nature["y"] * all_nature["z"])
    print("颜色", all_nature["color"])
    print("重量", all_nature["weight"])


cube("first")
cube("second", y=3, color="red")
cube("third", y=2, color="grenn", weight=10)




from functools import reduce

alst = [1, 2, 3, 4, 5]
a = reduce(lambda x, y: x + y, alst)
print(a)
