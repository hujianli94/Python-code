#用字典表示蛋糕档案
cakeFile={}
#提拉米苏和舒芙蕾对应的文件，其余蛋糕省略
cakeFile['提拉米苏']='tiramisu.py'
cakeFile['舒芙蕾']='souffle.py'
def openCakeCard(cakeName):
    import os
    try:
        print(cakeFile[cakeName])
        os.popen(cakeFile[cakeName])
    except KeyError as e:
        print(e,"身份牌未就绪。")
    
#导入tkinter模块
from tkinter import *
#创建一个tk窗体
root = Tk()
#定制窗体
root.title("蛋糕档案")
root.iconbitmap("cakeFile.images")

#事件处理程序
def selectCake(event):
    item=cakeListbox.get(cakeListbox.curselection())
    print(item)
    openCakeCard(item)
    
#创建listBox
cakeListbox = Listbox(root,justify=LEFT,width=30,selectmode=SINGLE)

#事件绑定
cakeListbox.bind('<ButtonRelease-1>',selectCake)

#蛋糕列表框
cakeList=['提拉米苏','舒芙蕾','黑森林蛋糕','瑞士卷']
for cake in cakeList:
    cakeListbox.insert(END,cake)

#绘制列表框
cakeListbox.pack()

#加入主循环
root.mainloop()
