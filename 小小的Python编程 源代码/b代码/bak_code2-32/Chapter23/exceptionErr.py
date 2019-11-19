#异常的示例
x=input("输入0-5会有异常：")
if x not in ['0','1','2','3','4','5']:
    print("本次没有发生异常。程序结束。")
    import sys
    sys.exit(0)
else:
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
    if triger==4:
        print("b=",b)
    if triger==5:
        dict={1:"张三",2:"李四",3:"王武"}
        print(dict[4])
