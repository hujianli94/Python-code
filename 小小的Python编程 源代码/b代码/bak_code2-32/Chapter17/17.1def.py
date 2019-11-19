#定义printWall()函数
def printWall(width):
    print('|',' '*width,'|')

#定义Floor()函数
def Floor(width):
    return '-'*width

#调用函数，输出图案
print(Floor(15))                #Floor(15)有返回值
for x in range(1,5):
    printWall(11)
print(Floor(15))
for x in range(1,5):
    printWall(11)
print(Floor(15))
