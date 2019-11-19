#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/17 13:54
# filename: 4.1对比nginx配置文件.py
import difflib
import sys,os

try:
    textfile1=sys.argv[1]       #获取参数1
    textfile2 = sys.argv[2]     #获取参数2
except Exception as e:
    print("Error: "+str(e))
    print("Usage: python 4.1对比nginx配置文件.py nginx1.cfg  nginx2.cfg")
    sys.exit()


def readfile(filename):
    try:
        fileHanle = open(filename, "rb")
        text = fileHanle.read().splitlines()        #读取后以行进行分隔
        fileHanle.close()
        return text
    except Exception as e:
        print("Read file Error :" + str(e))
        sys.exit()



if textfile1 == "" or textfile2 =="":
    print("Usage: python 4.1对比nginx配置文件.py nginx1.cfg  nginx2.cfg")
    sys.exit()

if __name__ == '__main__':
    text1_lines = readfile(textfile1)       #调用函数，获取分隔后的字符串
    text2_lines = readfile(textfile2)

    d = difflib.HtmlDiff()      #创建HtmlDiff对象
    html_file = "difflib_nginx.html"
    if not os.path.exists(html_file):
        with open(html_file, "w") as file:
            file.write(d.make_file(text1_lines, text2_lines))
    else:
        print(html_file + "is exists....")

