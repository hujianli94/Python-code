#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/23 8:45
# filename: 1.读取xml文件.py
import xml.etree.ElementTree as ET

tree = ET.parse("Notes.xml")  # 创建xml文档树
print(type(tree))

root = tree.getroot()  # root是根元素
print(type(root))
print(root.tag)

for index, child in enumerate(root):
    print("第{}个{}元素，属性{}".format(index, child.tag, child.attrib))
    for i, child_child in enumerate(child):
        print("     标签：{}，内容：{}".format(child_child.tag, child_child.text))
