#!/usr/bin/env python
#-*- coding:utf8 -*-
import os
src_txt = "a.txt"
dst_txt = "a_bak.txt"
with open(src_txt,"w") as f:
    f.write("花儿呀。\n"
            "花儿呀")

with open(src_txt) as fr,open(dst_txt,"w") as fw:
    for line in fr:
        lines = line.replace("花","flower")
        fw.write(lines)

os.remove(src_txt)
os.rename(dst_txt,src_txt)
