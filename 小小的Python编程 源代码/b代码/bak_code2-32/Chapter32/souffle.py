#图形化界面菜单
#导入tkinter模块
from tkinter import *
#准备数据
souffleTxt="""舒芙蕾，一种蛋奶酥。源自一种来自法国的烹饪方法。
这种特殊的厨艺方法，主要材料包括蛋黄及不同配料拌入经打匀后的蛋白，
经烘焙质轻而蓬松。"""

#创建一个tk窗体
root = Tk()

#创建一个Text
text=Text(root, #将内容绑定在初始窗体root上
    height=4,width=35)    #Label显示的外边距
text.insert(END,souffleTxt)
text.pack(side=LEFT)        #将Label装入窗体，靠左显示

#创建一个图片Label
soufflePic=PhotoImage(file="souffle.png")
imgLabel = Label(
    root,               #父组件
    image=soufflePic)   #image属性指明要显示的图片对象
imgLabel.pack(side=RIGHT)       #将Label装入窗体，靠右显示

#定制窗体
root.title("舒芙蕾")
root.iconbitmap("souffle.images")
root.mainloop() #窗体加入到主循环   
