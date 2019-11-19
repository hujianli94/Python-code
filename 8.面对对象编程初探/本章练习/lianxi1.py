#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/14 17:20
# filename: lianxi1.py

prompt_info = '''您可以通过name、email、address的方式查询相关信息: 
>>【name】\n>>【email】\n>>【address】\n'''

class Student_Class(object):
    #姓名列表
    list_name_info = []
    #邮箱列表
    list_email_info = []
    #地址列表
    list_address_info = []

    def __init__(self, name, age, gender, phone, address, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.address = address

        self.list_name_info.append(name)
        self.list_email_info.append(email)
        self.list_address_info.append(address)

    def eat(self):
        print("{} 吃/.....................".format(self.name))

    def Drink_water(self):
        print("{} 喝水........................".format(self.name))

    def play_game(self):
        print("{} 玩游戏....................".format(self.name))

    def Sleep(self):
        print("{} 睡觉.....................".format(self.name))

    def warr_info(self):
        print(prompt_info)
        input_info = input("请输入您要查询的信息：").strip().lower()
        if input_info == "name":
            input_name = input("请输入姓名").strip().lower()
            if input_name in self.list_name_info:
                print("查询到【{}】的相关信息".format(input_name))
        elif input_info == "email":
            input_email = input("请输入email").strip().lower()
            if input_email in self.list_email_info:
                print("查询到【{}】的相关信息".format(input_email))
        elif input_info == "address":
            input_address = input("请输入查询地址:").strip().lower()
            if input_address in self.list_address_info:
                print("查询到【{}】的相关信息".format(input_address))
        else:
            print("您输入的字符查询不到..........")

    def get_all_info(self):
        print(self.list_name_info)
        print(self.list_email_info)
        print(self.list_address_info)


if __name__ == '__main__':
    hu = Student_Class("胡建力1", 18, "man", "13262662212", "北京1", "1879324761@qq.com")
    hu2 = Student_Class("胡建力2", 18, "man", "13262662213", "北京2", "1879324762@qq.com")
    hu3 = Student_Class("胡建力3", 18, "man", "13262662214", "北京3", "1879324763@qq.com")
    hu.warr_info()

