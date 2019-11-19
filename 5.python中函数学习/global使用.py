#!/usr/bin/env python
#-*- coding:utf8 -*-
Var_name = "hujianli_global"

def change_and_print_global():
    global Var_name
    Var_name = "hujianli local_Var"
    print("Inside change_and_print_global: ", Var_name)

print(Var_name)
change_and_print_global()
print(Var_name)