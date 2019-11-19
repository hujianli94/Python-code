#个性化异常处理
x=input("输入0-4会有异常：")
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
        if triger==4:
            b
            print("b=",b)
        if triger==5:
            print("欢迎来到没有异常的分支！")
    except IndexError:
        print("我的第六感告诉我：你的下标越界了！")
    except ZeroDivisionError as e:
        import sys
        print("你想干嘛？除零可不行！详情：",e,"->",sys.exc_info())
    except (ModuleNotFoundError,NameError):
        print("我的第六感告诉我：模块不存在或者名字错了！")
    except:
        print("直觉告诉我，此处有其他异常！")
    else:
        print("很顺利，什么异常也没有发生。")
    
        
