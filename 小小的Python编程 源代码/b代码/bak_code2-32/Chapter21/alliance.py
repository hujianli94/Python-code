#特工联盟条约（模块示例）
#模块内的变量
declaration="既然不得不做出选择,那就请面带微笑态度严肃没有所谓的沿袭正道或逐步偏离。\
就让执念一路冲锋陷阵,因为我们的去向,从来都掌握在自己手中。"
#模块内的程序段
if __name__ == '__main__':
    #仅在模块运行时执行的程序段
    import time
    print("模块最后一次执行日期为：",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
else:
    #模块被引入时自动执行的程序段
    print("====================================================")
    print(declaration)
    print("====================================================\n")
#模块内的函数
def running(distance):
    "心有多远，就能跑多远！"
    if distance<=10000:
        print("OK！我跑",distance,"米没问题！")
    elif distance>10000:
        print("什么？这个距离我可跑不了！")
    else:
        print("你在开玩笑吗？")

def tell_speed(subject):
    "做完作业不厉害，快速做完才厉害！"
    hours=int(input("请输入你估计要用几个小时完成作业（1-24）："))
    if hours>0:
        if hours<=4:
            print("想要",hours,"小时完成",subject,"门作业","你必须",hours/subject*60,"分钟就完成一门！")
        elif hours<=6:
            print("老师说一门作业超过",hours/subject*60,"分钟完成的都太慢了。")
        else:
            print("一门功课要做",hours/subject*60,"分钟这么久？早点洗洗睡吧！")
    else:
        print("输入无效")

def dancing():
    "起舞吧！少年！"
    import random
    dance=["<(￣ˇ￣)/~~~","*╰(￣▽￣)╭*","ヾ(≧O≦)〃嗷~"]
    print(random.choice(dance))
