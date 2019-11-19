#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/11/10 10:26
# filename: 用户注册登录.py

class UserInfo:
    def __init__(self):
        self.__username = None
        self.__password = None

    def __str__(self):
        return self.__username

    def login(self):
        """
        用户登录
        :return:
        """
        print("--------------------欢迎来到登录界面---------------------")
        self.__username = input("请输入登录的用户名：")
        self.__password = input("请输入登录的密码：")
        with open("user.txt", encoding="utf-8") as rs:
            info = rs.readlines()
            for i in info:
                user = i.replace("\n", "")
                u_p = user.split()
                if self.__username == u_p[0] and self.__password == u_p[1]:
                    print("用户登录成功")
                    return False
                else:
                    print("用户登录失败")
                    return True

    def regiested(self):
        """
        用户注册
        :return:
        """
        print("---------------------欢迎来到用户注册------------------------")
        self.__username = input("请输入注册的用户名：")
        self.__password = input("请输入注册的密码：")
        if self.__username and self.__password:
            with open("user.txt", "a", encoding="utf-8") as ws:
                ws.write(self.__username + "\t" + self.__password + "\n")
                print("注册用户成功！")
        else:
            print("用户密码不能为空")


def main():
    Flag = True
    hu = UserInfo()
    hu.regiested()
    while Flag:
        Flag = hu.login()


if __name__ == '__main__':
    main()
