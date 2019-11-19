#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/28 14:09
# filename: 树演示.py
G = ['G', []]
H = ['H', []]
I = ['I', []]
J = ['J', []]
K = ['K', []]

E = ['E', [G, H, I, J, K]]
D = ['D', []]
F = ['F', []]
A = ['A', [D, E]]
B = ['B', []]
C = ['C', [F]]
Root = ['Root', [A, B, C]]
print(Root)
