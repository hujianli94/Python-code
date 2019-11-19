#finally子句示例
try:
    x=input("输入0-3尝试捕获异常：")
    if x not in ['0','1','2','3']:
        print("本次没有发生异常。程序结束。")
        import sys
        sys.exit(0)
    else:
        triger=int(x)
        if triger==0:
            2/0
        if triger==1:
            int("a")
        if triger==2:
            '2'/'1'
        print("您输入了：",x)
except ZeroDivisionError as e:
    print("除零异常：",e)
else:
    print("没有发生异常。")
finally:
    print("异常处理完毕，未知异常将再次抛出。")

    
