#!/usr/bin/env python
#-*- coding:utf8 -*-
import configparser
config = configparser.ConfigParser()
config.read("file.conf",encoding="utf-8")

#添加节点"node1","node2",然后写入文件
# config.add_section("node1")
# config.add_section("node2")
# config.write(open("file.conf",'w'))

#检查节点是否存在
print(config.has_section("node1"))
print(config.has_section("node2"))
print(config.has_section("node3"))

#删除节点
config.remove_section("node2")
config.write(open('file.conf', 'w'))
print(config.has_section('node2'))

#设置节点内的键值对

# 添加完键值对之后别忘记了写入到文件中
config.set('node1', 'Name', "ansheng")
config.set('node1', 'Blog_URL', "https://blog.ansheng.me")
config.set('node1', 'Hostname', "localhost.localhost")
config.set('node1', 'IP', "127.0.0.1")
config.write(open('file.conf', 'w'))

#检查节点内的key是否存在
# 如果节点的Key存在就返回"True"，否则返回"False"
print(config.has_option('node1', 'Name'))
print(config.has_option('node1', 'IP'))
print(config.has_option('node1', 'VV'))


#删除节点内的key

# 如果删除的节点存在就返回"True"，否则就返回"False"
config.remove_option('node1', 'IP')

config.write(open('file.conf', 'w'))
print(config.has_option('node1', 'IP'))



#获取指定节点下指定key的值

# 默认返回的是字符串类型
print(config.get('node1', 'Name'))
print(config.get('node1', 'Blog_URL'))

# 返回的字符串我们可以设置成一下三种数据类型，分别是"int"，"float"，"bool"
# v = config.getint('node1', 'k1')
# v = config.getfloat('node1', 'k1')
# v = config.getboolean('node1', 'k1')

#获取指定节点下所有的key

# 返回节点下面所有的Key列表
print(config.options('node1'))

#获取指定节点下所有的键值对
# 返回一个列表，列表中每个元组就是一个键值对
print(config.items('node1'))

#获取所有节点
# 获取当前文件中有多少个节点
print(config.sections())

