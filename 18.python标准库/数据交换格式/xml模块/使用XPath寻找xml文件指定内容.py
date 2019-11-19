#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/23 8:54
# filename: 使用XPath寻找xml文件指定内容.py
import xml.etree.ElementTree as ET

tree = ET.parse("Notes.xml")
root = tree.getroot()

node = root.find("./Note")      # 查找当前接电线的第一个Note子节点
print(node.tag, node.attrib)
node = root.find("./Note/CDate")    # 查找Note子节点下的第一个CDdate节点
print(node.text)

node = root.find("./Note/CDate/..")     # Note节点
print(node.tag, node.attrib)

node = root.find(".//CDate")        # 当前节点查找所有后代节点中第一个CDate节点
print(node.text)

node = root.find("./Note[@id]")     # 具有id属性的Note节点
print(node.tag, node.attrib)

node = root.find("./Note[@id='2']")     # id属性等于'2'的Note节点
print(node.tag, node.attrib)

node = root.find("./Note[2]")     # 第二个Note节点
print(node.tag, node.attrib)

node = root.find("./Note[last()]")     # 最后一个Note节点
print(node.tag, node.attrib)

node = root.find("./Note[last()-2]")     # 倒数第三个Note节点
print(node.tag, node.attrib)