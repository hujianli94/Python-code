#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/11/3 17:51
# filename: read_docx.py
import docx
def readDocx(docName):
    fullText = []
    doc = docx.Document(docName)
    # 读取全部内容
    paras = doc.paragraphs
    # 将每行数据存入列表
    for p in paras:
        fullText.append(p.text)
        # 将列表数据转换成字符串
    return '\n'.join(fullText)
# print(readDocx('test.docx'))
print(readDocx('AWS培训2019-10-23.docx'))


