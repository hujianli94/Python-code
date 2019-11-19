#百钱百鸡
#设公鸡为x只，母鸡为y只，小鸡为z只
for x in range(1,101):
    for y in range(1,101):
        for z in range(1,101):
            #print("---------------调试信息：公鸡、母鸡、小鸡各",x,y,z,"只")
            if x+y+z==100 and 5*x+3*x+1/3*z==100:
                print("公鸡、母鸡、小鸡各",x,y,z,"只")

