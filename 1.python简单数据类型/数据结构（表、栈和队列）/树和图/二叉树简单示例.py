#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/10/1 14:42
# filename: 二叉树简单示例.py

class BeTree(object):
    def __init__(self, value):
        """
        构造方法，初始化value的值
        :param value:
        """
        self.left = None  # 左儿子
        self.date = value
        self.right = None  # 右儿子

    def insertLeft(self, value):
        """ 插入左儿子 """
        self.left = BeTree(value)
        return self.left

    def insertRight(self, value):
        """ 插入右儿子 """
        self.right = BeTree(value)
        return self.right

    def show(self):
        """ 打印value的数据 """
        print(self.date)


if __name__ == '__main__':
    Root = BeTree("root")  # 根节点
    A = Root.insertLeft("A")  # 向根节点中插入A节点
    C = A.insertLeft("C")  # 向A节点中插入C节点
    D = A.insertRight("D")  # 向A节点中插入D节点
    F = D.insertLeft("F")  # 向D节点中插入F节点
    G = D.insertRight("G")
    B = Root.insertRight("B")
    E = B.insertRight("E")
    Root.show()  # 输出节点数
    Root.left.show()
    Root.right.show()
    A = Root.left
    A.left.show()
    Root.left.right.show()

    # root
    # A
    # B
    # C
    # D
