#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/28 19:45
# filename: 10.序列中出现次数最多的元素.py
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter

word_counts = Counter(words)

# 出现频率最高的3个单词
top_three = word_counts.most_common(3)
print(top_three)

print(word_counts["look"])
print(word_counts["eyes"])