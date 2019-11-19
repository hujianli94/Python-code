#!/usr/bin/env python
#-*- coding:utf8 -*-
def fun_checkout(money):
    '''
    计算商品合计金额，并进行折扣处理
    :param money: 保存商品金额的列表
    :return:商品的合计金额和折扣后的金额
    '''
    money_old = sum(money)      #计算合计金额
    money_new = money_old       #计算折扣后的金额
    if 500 <= money_old < 1000:  #享受9折优惠
        money_new = '{:.2f}'.format(money_new*0.9)
    elif 1000 <= money_old <= 2000:  #享受8折优惠
        money_new = '{:.2f}'.format(money_new*0.8)
    elif 2000 <= money_old <= 3000:  #享受7折优惠
        money_new = '{:.2f}'.format(money_new*0.7)
    elif money_old >= 3000:             #享受6折优惠
        money_new = '{:.2f}'.format(money_new*0.6)
    return money_old, money_new

#调用函数
print('开始结算......\n')
list_money = []
while True:
    In_money = float(input("请输入您购买的商品金额(输入0表示输入完毕)："))
    if int(In_money) == 0:
        break       #退出循环
    else:
        list_money.append(In_money)
        money = fun_checkout(list_money)        #调用函数
print("合计金额：{},应付金额:{}".format(money[0], money[1]))