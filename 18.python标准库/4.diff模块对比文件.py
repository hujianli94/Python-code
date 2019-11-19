#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/17 13:39
# filename: 4.diff模块对比文件.py
import difflib

text1 = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

"""

text2 = """
The Zen of Python, by Tim Peters

Beautiful is better than Ugly.
Explicit is better than iMplicit.
Simple is better than compsdslex.
Complex is better than complidscated.
Flat is better than nested////.
Sparse is better than dense.
Readability counts.
Special cases aren't special enougsadah to break the rules.
Although practicality beats pudasdrity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the tczccxzemptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!


"""

if __name__ == '__main__':
    # 以行进行分割，便于比较
    text1_lines = text1.splitlines()
    text2_lines = text2.splitlines()
    html_file = "difflib.html"
    # d = difflib.Differ()  # 创建differ()对象
    # diff = d.compare(text1_line, text2_line)
    # print("\n".join(list(diff)))

    ######################## 生成美观的html文件 查看比对情况 ######################################
    d = difflib.HtmlDiff()
    import os
    if not os.path.exists(html_file):
        with open(html_file, "w") as file:
            file.write(d.make_file(text1_lines, text2_lines))
    else:
        print(html_file + "is exists....")
