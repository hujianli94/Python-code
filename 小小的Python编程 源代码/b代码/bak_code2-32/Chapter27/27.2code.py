#五个数互不相等
def condition1(a,b,c,d,e):
    x=[a,b,c,d,e]           #五个数放进列表
    y=x.copy()              #复制一份
    y.sort()                #排序
    z=list(set(y))          #转换成集合去重
    if y==z:                #去重后会自动排序，再与未去重前比较
        return True         #如果相等，说明原列表中没有重复元素

#满足等式条件
def condition2(a,b,c,d,e):
    if (a*10000+b*1000+c*100+d*10+e)*a==e*111111:
        return True

#暴力破解通关密码
for A in range(1,10):
    for B in range(0,10):
        for C in range(0,10):
            for D in range(0,10):
                for E in range(0,10):
                    if condition1(A,B,C,D,E) and condition2(A,B,C,D,E):
                        temp=A*10000+B*1000+C*100+D*10+E
                        print(temp,"*",A,"=",E*111111)
                        print("密码就是：",A,B,C,D,E)       
