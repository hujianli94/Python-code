#条件语句示例2
con=input('作业做完了吗?(Y或N)')
if con=='Y':
    print("欢迎您，王者。请进入游戏！")
    age=int(input("请问王者，您几岁？（0-150）"))
    if age<12 and age>0:
        print("您只能玩1个小时哦！")
    elif age>=12 and age<18:
        print("您只能玩2个小时哦！")
    elif age>=18 and age<=150:
        print("您已经是成年人了，请自己控制游戏时间！")
    else:
        print("别闹，您输入的不是人的年龄！")
elif con=='N':
    print("想什么呢？快滚回去做作业！")
else:
    print("答非所问！")
