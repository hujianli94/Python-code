#鸡兔同笼问题发生器
try:
    ji=int(input("请输入鸡的数量（必须是整数）："))
    tu=int(input("请输入兔的数量（必须是整数）："))
except TypeError:
    print("输入不是整数，请重来。")
print("头的数量：",ji+tu)
print("脚的数量：",4*tu+2*ji)

        
