#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/25 12:51
# filename: 主要的函数.py
import os, time, string, random, tkinter, pyqrcode
import tkinter.filedialog
import tkinter.messagebox
from tkinter import *
from string import digits

root = tkinter.Tk()  # 建立根窗口

# 初始化数据
number = '1234567890'
letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
allis = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+'
i = 0
randstr = []
fourth = []
fifth = []
randfir = ""
randsec = ""
randthr = ""
str_one = ""
strtwo = ""
nextcard = ""
userput = ""
nres_leyyer = ""


def mainmenu():
    print("""\033[1;35m
    ***************************************************************************************
                                        企业编码生成系统
    ***************************************************************************************
        1.生成6位数字防伪编码（213563型）
        2.生成9位系列产品数字防伪编码（879-335439型）
        3.生成25位混合产品序列号（B2R12-N7TE8-9IET2-FE350-DW2K4型）
        4.生成含数据分析功能的防伪编码（5A61M0583D2）
        5.批量生成带数据分析功能的防伪码
        6.后续补加生成防伪码（5A61M0583D2）
        7.EAN-13条形码批量生成
        8.二维码批量输出
        9.企业粉丝防伪码抽奖
        0.退出系统
    =====================================================================================
    说明：通过数字键选择菜单
    ======================================================================================
    \033[0m""")


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


def input_validation(insel):
    if str.isdigit(insel):
        if insel == 0:
            print("\033[1;31;40m  输入非法，请重新输入！！！ \033[0m")
            return 0
        else:
            return insel
    else:
        print("\033[1;31;40m  输入非法，请重新输入！！！ \033[0m")
        return 0


def ffcode(scount, typestr, ismessage, schoice):
    """
    生成含数据分析功能的防伪编码函数
    :param scount: 生成防伪码的数量
    :param typestr: 数据分析字符
    :param ismessage: 输出完成时是否显示提示信息，"no"为不显示,其他为显示
    :param schoice: 设置输出文件的名称
    :return:
    """
    randstr.clear()  # 清空批量保存防伪码信息的变量randstr
    # 按数量生成含数据分析的防伪码
    for j in range(int(scount)):
        strpro = typestr[0].upper()  # 取得三个字母中的第一个，并转为大写，区域分析码
        strtype = typestr[1].upper()  # 取得三个字母中的第二个，并转为大写，颜色分析码
        strclass = typestr[2].upper()  # 取得三个字母中的第三个，并转为大写，版本分析码
        randfir = random.sample(number, 3)  # 随机抽取防伪码的3个位置，不分先后
        randsec = sorted(randfir)  # 对抽取的位置进行排序并赋值
        letterone = ""  # 清空单条防伪码的变量
        # 生成9位数字的防伪码
        for i in range(9):
            letterone = letterone + random.choice(number)

        # 将3个字母按randsec变量中存储的位置添加到数字防伪码中，保存到sim变量中
        sim = str(letterone[0:int(randsec[0])]) + strpro + str(letterone[int(randsec[0]):int(randsec[1])]) + strtype \
              + str(letterone[int(randsec[1]):int(randsec[2])]) + strclass + str(
            letterone[int(randsec[2]):9]) + "\n"
        randstr.append(sim)  # 将组合生成新的防伪码添加到randstr变量

    # 调用wfile()函数，实现生成的防伪码屏幕输出和文件输出
    wfile(randstr, typestr + "scode" + str(schoice) + ".txt" + ismessage, "", "生成含数据分析的防伪码共计：", "codepath")


def scode1(schoice):
    """
    生成6位数字防伪码
    :param schoice:
    :return:
    """
    # 调用inputbox函数对输入数据进行非空、输入合法性判断
    incount = inputbox("\033[1:32m 请输入您要生成防伪码的数量：\033[0m", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1:32m 请输入您要生成防伪码的数量：\033[0m", 1, 0)
    randstr.clear()  # 清空保存批量防伪码信息的变量randstr
    for j in range(int(incount)):  # 根据防伪码数量循环批量生成防伪码
        randfir = ""  # 设置存储单条防伪码的变量为空
        for i in range(6):
            randfir = randfir + random.choice(number)  # 产生数字随机因子
        randfir = randfir + "\n"  # 在单挑防伪码后面添加换行，使验证码单条列显示
        randstr.append(randfir)  # 单条防伪码保存批量验证码的变量randstr

    # 调用函数wfile(),实现生成的防伪码屏幕输出和文件输出
    wfile(randstr, "scode" + str(schoice) + ".txt", "", "已生成6位防伪码共计：", "codepath")


def scode2(schoice):
    """
    生成9位系列产品数字防伪编码
    :param schoice:
    :return:
    """
    ordstart = inputbox("\033[1;32m 请输入系列产品的数字起始号(3位):\033[0m", 3, 3)
    while int(ordstart) == 0:
        ordstart = inputbox("\033[1;32m 请输入系列产品的数字起始号(3位):\033[0m", 1, 0)
    ordcount = inputbox("\033[1;32m 请输入产品系列的数量：", 1, 0)
    # 如果输入的产品系列数量小于1或大于9999，则要求重新输入
    while int(ordcount) < 1 or int(ordcount) > 9999:
        ordcount = inputbox("\033[1;32m 请输入产品系列的数量：", 1, 0)
    intcount = inputbox("\033[1;32m 请输入要生成的每个系列产品的防伪码数量：\033[0m", 1, 0)
    while int(intcount) == 0:  # 如果输入为字母或者数字0，则要求重新输入
        ordcount = inputbox("\033[1;32m 请输入产品系列的数量：", 1, 0)
    randstr.clear()  # 清空保存批量防伪码信息的变量randstr
    for m in range(int(ordcount)):  # 分类产品编号
        for j in range(int(ordcount)):  # 产品防伪码编号
            randfir = ""
            for i in range(6):  # 生成一个不包含类别的产品防伪码
                randfir = randfir + random.choice(number)  # 每次生成一个随机因子
            # 将生成的单挑防伪码添加到防伪码列表
            randstr.append(str(int(ordstart) + m) + randfir + "\n")
    wfile(randstr, "scode" + str(schoice) + ".txt", "", "已生成9位系列产品防伪码共计：", "codepath")


def scode3(schoice):
    """
    生成25位混合产品序列号函数
    :param schoice: 参数schoice设置输出的文件名称
    :return:
    """
    incount = inputbox("\033[1;32m 请输入要生成的25位混合产品序列号数量：\033[0m", 1, 0)
    while int(incount) == 0:  # 如果输入非法（符合、字母或者数字0都任务是非法输入），重新输入
        incount = inputbox("\033[1;32m 请输入要生成的25位混合产品序列号数量：\033[0m", 1, 0)
    randstr.clear()  # 清空保存批量防伪码信息的变量randstr
    for j in range(int(incount)):  # 按输入数量生成防伪码
        strone = ""  # 保存生成的单条防伪码，不带横线“-”，循环时清空
        for i in range(25):
            # 每次产生一个随机因子，也就是每次产生单条防伪码的一位
            strone = strone + random.choice(letter)
        # 将生成的防伪码每隔5位添加横线"-"
        strtwo = strone[:5] + "-" + strone[5:10] + "-" + strone[10:15] + "-" + strone[15:20] + "-" + strone[
                                                                                                     20:25] + "\n"
        randstr.append(strtwo)
    # 调用函数wfile(),实现生成的防伪码在屏幕输出和文件输出
    wfile(randstr, "scode" + str(schoice) + ".txt", "", "已生成25混合访问序列码共计：", "codepath")


def scode4(schoice):
    """
    生成含数据分析功能防伪编码函数
    :param schoice:  设置输出的文件名称
    :return:
    """
    intype = inputbox("\033[1;32m 请输入数据分析编号（3位字母）: \033[0m", 2, 3)
    # 验证输入是否是三个字母，所以要判断输入是否是字母和输入长度是否为3
    while not str.isalpha(intype) or len(intype) != 3:
        intype = inputbox("\033[l;32m 请输入数据分析编号（3位字母）:\33[0m", 2, 3)
    incount = inputbox("\033[1;32m 输入要生成的带数据分析功能的防伪码数量： \33[0m", 1, 0)

    # 验证输入是否是大于零的整数，方法是判断输入转换为整数值时是否大于零
    while int(incount) == 0:  # 如果转换为整数时为零，则要求重新输入
        incount = inputbox("\033[1;32m 输入要生成的带数据分析功能的防伪码数量： \33[0m", 1, 0)
    ffcode(incount, intype, "", schoice)  # 调用ffcode()函数生成防伪码


def scode5(schoice):
    pass


def scode6(schoice):
    # 设置默认打开的文件名称
    default_dir = r'D:\21-DAY-Python\第二章：企业编码系统\主要函数功能\codepath'
    file_path = tkinter.filedialog.askopenfilename(title=u'请选择已经生产的防伪码文件', initialdir=(os.path.expanduser(default_dir)))
    codelist = openfile(file_path)  # 读取从文件选择对话框选中的文件
    codelist = codelist.split("\n")
    codelist.reverse("")  # 删除列表中的空行
    # 读取一行数据，以便获取原验证码的字母标志信息
    strset = codelist[0]
    # 使用maketrans()方法创建删除数字的字符映射转换表
    remove_digits = strset.maketrans("", "", digits)
    # 根据字符映射转换表删除该条防伪码中的数字，获取字母标识信息
    res_letter = strset.translate(remove_digits)
    nres_letter = list(res_letter)          #把信息用列表变量nres_letter存储
    strpro = nres_letter[0]                 #获取第一个字母，区域分析码
    strtype = nres_letter[1]                #获取第二个字母，色彩分析码
    strclass = nres_letter[2]               #获取第三个字母，版次分析码
    #去除信息中的括号和引号



while i < 9:
    mainmenu()

    choice = input("\033[1;32m 请输入您要操作的菜单选项：\33[0m")
    if len(choice) != 0:
        choice = input_validation(choice)  # 验证是否为数字
        choice = int(choice)

        if choice == 1:
            print("1.生成6位数字防伪编码（213563型）")
            scode1(str(choice))
        if choice == 2:
            print("2.生成9位系列产品数字防伪编码（879-335439型）")
            scode2(str(choice))
        if choice == 3:
            print("3.生成25位混合产品序列号（B2R12-N7TE8-9IET2-FE350-DW2K4型）")
            scode3(str(choice))
        if choice == 4:
            print("4.生成含数据分析功能的防伪编码（5A61M0583D2）")
            scode4(str(choice))
        if choice == 5:
            print("5.批量生成带数据分析功能的防伪码")
            pass
        if choice == 6:
            print("6.后续补加生成防伪码（5A61M0583D2）")
            pass
        if choice == 7:
            print("7.EAN-13条形码批量生成")
            pass
        if choice == 8:
            print("8.二维码批量输出")
            pass
        if choice == 9:
            print("9.企业粉丝防伪码抽奖")
            pass
        if choice == 0:
            i = 10
            print("正在退出系统")
    else:
        print("\033[1;31;40m 输入非法，请重新输入！！\033[0m")
