#!/usr/bin/env python
#-*- coding:utf8 -*-
print("计算税后工资的一个deam".center(100,"*"))
Salary_Amount = input("请输入您的工资金额： ")
try:
    Salary_Amount = float(Salary_Amount)  #输入的工资
    New_Sa_Amout = float(Salary_Amount)   #运算后统计超过的工资
    if Salary_Amount <= 3500:
        print("您的工资为：{}".format(Salary_Amount))
    elif  Salary_Amount >3500 and Salary_Amount <= 9000:
        End_memoy = Salary_Amount - (New_Sa_Amout - 3500) * 0.2
        print("您扣税后的工资所得为：{}".format(End_memoy))
    elif Salary_Amount > 9000 and Salary_Amount <= 35000:
        End_memoy = Salary_Amount - (New_Sa_Amout - 9000) * 0.25
        print("您扣税后的工资所得为：{}".format(End_memoy))
    elif Salary_Amount > 35000 and Salary_Amount <= 55000:
        End_memoy = Salary_Amount - (New_Sa_Amout - 35000) * 0.3
        print("您扣税后的工资所得为：{}".format(End_memoy))
    elif Salary_Amount > 55000 and Salary_Amount <= 80000:
        End_memoy = Salary_Amount - (New_Sa_Amout - 55000) * 0.35
        print("您扣税后的工资所得为：{}".format(End_memoy))
    elif Salary_Amount > 80000 and Salary_Amount:
        End_memoy = Salary_Amount - (New_Sa_Amout - 80000) * 0.45
        print("您扣税后的工资所得为：{}".format(End_memoy))

except Exception as a:
    print("输入错误字符." + a)


