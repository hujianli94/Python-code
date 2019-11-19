#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/28 21:09
# filename: 01.搭建开发环境.py

"""
virtualenv优点

1.使不同应用开发环境独立
2.环境升级不影响其他应用，也不会影响全局的python环境
3.它可以防止系统中出现包管理混乱和版本的冲突

sudo pip install virtualenv
sudo pip install virtualenvwrapper



* 创建虚拟环境的命令如下：

mkvirtualenv 虚拟环境名称
例：
mkvirtualenv py_django




    此时使用的python版本与默认版本相同，给同学们的ubuntu中默认是使用python2
    指定python版本的命令如下：

mkvirtualenv -p python路径 虚拟环境名称
例：
mkvirtualenv -p /usr/bin/python3 py3_django



    退出虚拟环境的命令如下：

deactivate


查看与使用

    查看所有虚拟环境的命令如下：
    提示：workon后面有个空格，再按两次tab键

workon 两次tab键


    使用虚拟环境的命令如下：
    写出名称的前部分后，可以使用tab键补齐

workon 虚拟环境名称
例：
workon py_django


删除

    删除虚拟环境的命令如下：

rmvirtualenv 虚拟环境名称
例：
先退出：deactivate
再删除：rmvirtualenv py_django


包操作

    在虚拟环境中可以使用pip命令操作python包
    安装命令如下：

pip install 包名称

    查看命令如下：

pip freeze

安装django包

    后面要学习使用django，以1.8.2版本为例，这是一个稳定性高、使用广、文档多的版本
    如果前面删除过虚拟环境py_django，则需要先创建一下

mkvirtualenv py_django

    安装django1.8.2的包，命令如下：

pip install django==1.8.2


"""