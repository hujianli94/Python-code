#汉诺塔问题
global i    #全局变量，用于记录步骤数
hanoi="""
  [||]      ||       ||
 [ || ]     ||       ||
[  ||  ]    ||       ||
========================
    a       b        c
"""
print(hanoi)

#移动步骤
def move(n, a, b, c):
    global i
    if(n == 1):
        i+=1
        print(i,a,"->",c)
    else:
        move(n-1, a, b, c)
        i+=1
        print(i,a,"->",b)
        move(n-1,c,b,a)
        i+=1
        print(i,b,"->",c)
        move(n-1,a,b,c)        

#三阶汉诺塔
i=0
print("三阶汉诺塔移动步骤：")
move(3,"a","b","c")
input("按回车键结束")
