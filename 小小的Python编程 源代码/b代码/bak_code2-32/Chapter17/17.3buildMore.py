#模块示例
import module.toolbox                  #引入模块

width=int(input("请输入墙的宽度："))
height=int(input("请输入层高："))
layer=int(input("请输入层数："))
#模块函数的调用
module.toolbox.printBuilding(width,height,layer)
