#异常处理
x=input("输入0-3会有异常：")
if x not in ['0','1','2','3','4','5']:
    print("本次没有发生异常。程序结束。")
    import sys
    sys.exit(0)
else:
    try:
        triger=int(x)
        if triger==0:
            e=1/0
        if triger==1:
            a=[1,2,3,4,5,6]
            print(a[6])
        if triger==2:
            a='2'+3    
        if triger==3:
            import notExistModule
    except:
        print("我的第六感告诉我：发生异常了！")
print("程序运行结束。")
        
