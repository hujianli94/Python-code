#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/25 12:51
# filename: 主要的函数.py
import os
import tkinter


def mkdir(path):
    isexists = os.path.exists(path)
    if not isexists:
        os.mkdir(path)


def openfile(filename):
    f = open(filename)
    fllist = f.read()
    f.close()
    return fllist


def inputbox(showstr, showorder, lenght):
    """

    :param showstr: 请输入系列产品的数字起始号（3）
    :param showorder:
    1，数字格式，不限位数，大于零的整数
    2，要求字母格式且是指定字母
    3，要求数字格式且输入数字位数有要求
    :param lenght:
    :return:
    """
    instr = input(showstr)  # 使用input函数要求用户输入信息，showstr为输入提示文字
    if len(instr) != 0:
        # 分成三种验证方式验证，1：数字，不限位数；2：字母；3：数字且有位数要求
        if showorder == 1:  # 验证方式1，数字格式，不限位数，大于零的整数
            if str.isdigit(instr):  # 验证是否为数字
                if instr == 0:  # 验证数字是否为0
                    print("\033[1;31;40m 输入为零，请重新输入！！\033[0m")  # 要求重新输入
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m输入非法，请重新输入！！\033[0m")  # 要求重新输入
                return "0"

        if showorder == 2:  # 验证方式2，要求字母格式且是指定字母
            if str.isalpha(instr):  # 验证是否为字母
                if len(instr) != lenght:
                    print("\033[1;31;40m必须输入" + str(lenght) + " 个字母，请重新输入！！ \033[0m")  # 要求重新输入
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m输入非法，请重新输入！！\033[0m")  # 要求重新输入
                return "0"

        if showorder == 3:  # 验证方式3，要求数字格式且输入数字位数有要求
            if str.isdigit(instr):  # 验证是否为数字
                if len(instr) != lenght:
                    print("\033[1;31;40m必须输入" + str(lenght) + " 个字母，请重新输入！！ \033[0m")  # 要求重新输入
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m输入非法，请重新输入！！\033[0m")  # 要求重新输入
                return "0"
        else:
            print("\033[1;31;40m输入为空，请重新输入！！\033[0m")  # 输入为空，要求重新输入
            return "0"  # 函数返回值为“0”


# incount = inputbox("请输入您要生成验证码的数量：", 2, 6)


def wfile(sstr, sfile, typeis, smsg, datapath):
    """

    :param sstr: 生成的防伪码
    :param sfile: 保存防伪码的文件名
    :param typeis: 是否显示“输出完成”的信息提示框，为“”时显示，为no时不显示
    :param smsg: 提示框显示的提示内容
    :datapath:保存访问码的路径
    :return:
    """
    mkdir(datapath)  # 创建文件夹
    datafile = datapath + "\\" + sfile  # 设置保存防伪码的文件
    file = open(datafile, "w")  # 打开文件，如果不存在，则创建文件
    wrlist = sstr
    pdata = ""
    wdata = ""
    for i in range(len(wrlist)):  # 按条件循环读取防伪码数据
        wdata = str(str(wrlist[i]).replace('[', '')).replace(']', '')  # 去掉字符串中的中括号
        wdata = str(wdata.replace("'", "")).replace('\"', '')  # 去掉字符串中的引号
        file.write(str(wdata))
        pdata = pdata + wdata
    file.close()
    print("\033[1;31m" + pdata + "\033[0m")  # 屏幕输出防伪码信息
    if type != "no":
        tkinter.messagebox.showinfo("提示", smsg + str(len(sstr)) + "\n 防伪码文件存放位置：" + datafile)
        # TODO
        pass

