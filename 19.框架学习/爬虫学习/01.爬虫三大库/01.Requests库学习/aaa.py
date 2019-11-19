#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/18 15:11
# filename: aaa.py
a = """

                            导演: 弗兰克·德拉邦特 Frank Darabont&nbsp;&nbsp;&nbsp;主演: 蒂姆·罗宾斯 Tim Robbins /...<br>
                            1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;犯罪 剧情
                                                   1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;犯罪 剧情\n                                                1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;犯罪 剧情', 
"""
#导演
print(a.split("&nbsp;&nbsp;&nbsp;")[0].strip())

#主演
print(a.split("&nbsp;&nbsp;&nbsp;")[1].split('/')[0])

# 演员
print(a.split("&nbsp;&nbsp;&nbsp;")[1].split('/')[1].split('&')[0])

