#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/15 10:59
# filename: 为jieba添加自定义词典.py
import jieba

jieba.load_userdict('dict.txt')  # 导入自定义词典
text = "故宫的著名景点包括乾清宫、太和殿和黄琉璃瓦等"

seg_list = jieba.cut(text, cut_all=False)  # 精确模式
print("【精确模式】:", "/".join(seg_list))

