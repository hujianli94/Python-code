#17.3toolbox模块
#定义printWall()函数
def printWall(w,h):				#参数w表示墙的宽度,h表示高度
    for x in range(h):
        print('|',' '*w,'|')

#定义printFloor()函数
def printFloor(w):				#参数w表示地板的宽度
    print('-'*(w+4))

#定义printBuilding()函数
def printBuilding(w,h,r):                   #参数layer表示楼房的层数
    for x in range(r):
        printFloor(w)                         #调用printFloor()
        printWall(w,h)                          #调用printWall()
    printFloor(w)
