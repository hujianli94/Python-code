#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/22 12:52
# filename: studentsystem.py
'''
0  退出系统
1  调用insert()函数，录入学生信息
2  调用search()函数,查找学生信息
3  调用delete()函数，删除学生信息
4  调用modify()函数，修改学生信息
5  调用sort()函数，对学生成绩排序
6  调用total()函数，统计学生总人数
7  调用show()函数，显示学生的信息

'''

import os
import re

filename = "student.txt"


def save(student):
    try:
        students_txt = open(filename, "a")  # 文件存在就追加
    except Exception as e:
        students_txt = open(filename, "w")  # 文件不存在则创建文件并打开
    for info in student:
        students_txt.write(str(info) + "\n")  # 按行存储，添加换行符
    students_txt.close()


def insert():
    studentList = []  # 保存学生信息列表
    mark = True
    while mark:
        id = input("请输入ID（如：1001）：")
        if not id:  # 如果ID为空，跳出循环
            break
        name = input("请输入名字：")
        if not name:
            break  # 如果名字为空，跳出循环

        try:
            enlish = int(input("请输入英语成绩："))
            python = int(input("请输入Python成绩："))
            c = int(input("请输入C语言成绩："))
        except:
            print("输入无效，不是整型数值，.....重新录入信息")
            continue
        # 将输入的学生信息保存到字典
        student = {"id": id, "name": name, "english": enlish, "python": python, "c": c}
        studentList.append(student)  # 将学生字典添加到列表中
        inputMark = input("是否继续添加？（y/n）：")
        if inputMark == "y":
            mark = True
        else:
            mark = False  # 不继续添加
    save(studentList)  # 将学生信息保存到文件
    print("学生信息录入完毕!!!!!")


def delete():
    mark = True
    while mark:
        studentId = input("请输入要删除的学生ID：")
        if studentId is not "":
            if os.path.exists(filename):
                with open(filename, "r") as rfile:  # 打开文件
                    student_old = rfile.readlines()  # 读取全部内容
            else:
                student_old = []
            ifdel = False  # 标记是否删除
            if student_old:  # 如果存在学生信息
                with open(filename, "w") as wfile:  # 以写的方式打开文件
                    d = {}
                    for list in student_old:
                        d = dict(eval(list))  # 字符串转为字典
                        if d['id'] != studentId:
                            wfile.write(str(d) + "\n")
                        else:
                            ifdel = True  # 标记已经删除
                    if ifdel:
                        print("ID为{}的学生信息已经被删除.....".format(studentId))
                    else:
                        print("没有找到ID为{}的学生信息....".format(studentId))
            else:
                print("无学生信息....")
                break
            show()
            inputMark = input("是否继续删除？（y/n）：")
            if inputMark == "y":
                mark = True  # 继续删除
            else:
                mark = False  # 退出删除学生信息功能


def modify():
    show()  # 显示全部学生信息
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, "r") as rfile:  # 打开文件
            student_old = rfile.readlines()  # 读取全部内容
    else:
        return
    studentid = input("请输入要修改的学生ID：")
    with open(filename, "w") as wfile:
        for student in student_old:
            d = dict(eval(student))  # 字符串转为字典
            if d["id"] == studentid:
                print("找到了这名学生，可以修改他的信息！")
                with True:
                    try:
                        d["name"] = input("请输入姓名：")
                        d["enlish"] = int(input("请输入英语成绩："))
                        d["python"] = int(input("请输入Python成绩："))
                        d['c'] = int(input("请输入C语言成绩："))
                    except:
                        print("您的输入有误，请重新输入。")
                    else:
                        break
                student = str(d)  # 将字典转换为字符串
                wfile.write(student + "\n")
                print("修改成功！")
            else:
                wfile.write(student)  # 将未修改的信息写入到文件

    mark = input("是否继续修改其他学生信息？（y/n）：")

    if mark == "y":
        modify()  # 重新执行修改操作


def search():
    mark = True
    student_query = []  # 保存查询结果的学生列表
    while mark:
        id = ''
        name = ''
        if os.path.exists(filename):  # 判断文件是否存在
            mode = input("按ID查输入1；按姓名查输入2：")
            if mode == "1":  # 按学生编号查询
                id = input("请输入学生ID：")
            elif mode == "2":  # 按学生姓名查询
                name = input("请输入学生姓名：")
            else:
                print("您的输入有误，请重新输入！")
                search()  # 重新查询
            with open(filename, "r") as file:  # 打开文件
                student = file.readlines()  # 读取全部内容
                for list in student:
                    d = dict(eval(list))  # 字符串转换为字典
                    if id is not "":  # 判断是否按ID查询
                        if d['id'] == id:
                            student_query.append(d)  # 将找到的学生信息保存到列表中
                    elif name is not "":  # 判断是否按姓名查询
                        if d['name'] == name:
                            student_query.append(d)  # 将找到的学生信息保存到列表中

                show_student(student_query)  # 显示查询结果
                student_query.clear()  # 清空列表
                inputMark = input("是否继续查询？（y/n）：")
                if inputMark == 'y':
                    mark = True
                else:
                    mark = False
        else:
            print("暂未保存数据信息........")
            return


def show_student(studentList):
    if not studentList:  # 如果没有要显示的数据
        print("@@@@@ 无数据信息 @@@@\n")
        return

    # 定义标题显示格式
    format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(format_title.format("ID", "名字", "英语成绩", "Python成绩", "C语言成绩", "总成绩"))  # 按指定格式显示标题

    # 定义具体内容显示格式
    format_data = "{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    for info in studentList:  # 通过for循环将列表中的数据全部显示出来
        print(format_data.format(info.get("id"),
                                 info.get("name"),
                                 str(info.get("english")),
                                 str(info.get("python")),
                                 str(info.get("c")),
                                 str(info.get("english") + info.get("python") + info.get("c")).center(12)))


def total():
    if os.path.exists(filename):
        with open(filename, "r") as rfile:
            student_old = rfile.readlines()  # 读取全部内容

            if student_old:
                print("一共有{}名学生".format(len(student_old)))
            else:
                print("还未录入学生信息")
    else:
        print("暂未保存数据信息............")


def show():
    student_new = []
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, "r") as rfile:
            student_old = rfile.readlines()  # 打开文件并读取全部内容

        for list in student_old:
            student_new.append(eval(list))
        if student_new:
            show_student(student_new)
    else:
        print("暂未保存数据信息..............")


def sort():
    show()

    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, "r") as file:  # 以只读模式打开文件
            student_old = file.readlines()  # 读取全部内容
            student_new = []
        for list in student_old:
            d = dict(eval(list))  # 字符串转字典
            student_new.append(d)  # 将转换后的字典添加到列表中
    else:
        return
    ascORDESC = input("请选择（0升序；1降序）：")
    if ascORDESC == "0":
        ascORDESCBool = False
    elif ascORDESC == "1":
        ascORDESCBool = True
    else:
        print("您的输入有误，请重新输入！")
        sort()
    mode = input("请选择排序方式(1按英语成绩排序:"
                 "2按Python成绩排序: "
                 "3按C语言成绩排序: "
                 "0按总成绩排序: )")
    if mode == "1":
        student_new.sort(key=lambda x: x['english'], reverse=ascORDESCBool)
    elif mode == "2":
        student_new.sort(key=lambda x: x['python'], reverse=ascORDESCBool)
    elif mode == "3":
        student_new.sort(key=lambda x: x['c'], reverse=ascORDESCBool)
    elif mode == "0":
        student_new.sort(key=lambda x: x['english'] + x['python'] + x['c'], reverse=ascORDESCBool)
    else:
        print("您的输入有误，请重新输入！")
        sort()

    show_student(student_new)  # 显示排序结果


def menu():
    # 输出菜单
    print("******************************************************************************")
    print("--------👨‍👩‍👧👨‍👩‍👧👨‍👩‍👧👨‍👩‍👧👨‍👩‍👧👨‍👩‍👧👨‍👩‍👧👨‍👩‍👧👨‍👩‍👧---------------")
    print("""
        |==========================学生信息管理系统===================|
        |==========================  功能菜单  ===================    |
        |1.录入学生信息                                               |
        |2.查找学生信息                                               |
        |3.删除学生信息                                               |
        |4.修改学生信息                                               |
        |5.排序                                                       |
        |6.统计学生总人数                                             |
        |7.显示学生信息                                               |    
        |0.退出系统                                                   |   
        |============================================================ |
        | 说明：通过数字或↑↓方向键选择菜单                           |
        |-------------------------------------------------------------|
        """)


def main():
    ctrl = True  # 标记是否退出系统
    while (ctrl):
        menu()
        option = input("请选择：")
        option_str = re.sub("\D", "", option)  # 提取数字
        if option_str in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            option_int = int(option_str)
            if option_int == 0:  # 退出系统
                print("您已退出学生信息管理系统")
                ctrl = False
            elif option_int == 1:
                insert()  # 录入
                # print("1")
            elif option_int == 2:
                search()  # 查找
                # print("2")
            elif option_int == 3:
                delete()  # 删除
                # print("3")
            elif option_int == 4:
                modify()  # 修改
                # print("4")
            elif option_int == 5:
                sort()  # 排序
                # print("5")
            elif option_int == 6:
                total()  # 统计
                # print("6")
            elif option_int == 7:
                show()  # 显示所有学生信息
            else:
                ctrl = True


if __name__ == '__main__':
    main()
