#应用模块示例
import alliance
#使用模块中的变量
#print("我们的宣言是：===",alliance.declaration,"===\n")
for i in range(3):
    x=int(input("请问您需要什么服务？【1.跑步；2.跳舞；3.计算作业速度】："))
    if x==1:
        alliance.running(5000)
    elif x==2:
        alliance.dancing()
    else:
        alliance.tell_speed(5)
