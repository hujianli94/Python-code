#!/usr/bin/env python
#-*- coding:utf8 -*-
import xml.etree.ElementTree as ET
tree = ET.parse("hujianli.xml")
root = tree.getroot()
print(root.tag)

#子节点也是迭代器，我们可以迭代它
for child in root:
    print(child.tag,child.attrib)

#子项是嵌套的，我们可以通过索引访问特定的子节点
print(root[0][1].text)

#Finding interesting elements 寻找有趣的元素
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

print()
#Element.findall()仅查找具有标记的元素，这些元素是当前元素的直接子元素。 Element.find()查找具有特定标记的第一个子项
for country in root.findall("country"):
    rank = country.find("rank").text
    name = country.get('name')
    print(name,rank)

#update Xml文件输出到另一个文件
for rank in root.iter("rank"):
    new_rank = int(rank.text) +1
    rank.text = str(new_rank)
    rank.set('update','yes')
tree.write('output.xml')

#删除元素Element.remove()
for coun in root.findall('country'):
    rank = int(coun.find('rank').text)
    if rank > 50:
        root.remove(coun)
tree.write("output1.xml")