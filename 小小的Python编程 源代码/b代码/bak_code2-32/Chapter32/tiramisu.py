#图形化界面菜单
#导入tkinter模块
from tkinter import *
#创建一个tk窗体
root = Tk()

#蛋糕数据
tiramisuTxt="""提拉米苏：是一种带咖啡和酒味的意大利甜点。
以马斯卡彭芝士作为主要材料，再以饼干碎片取代传统甜点
的海绵蛋糕，加入咖啡、可可粉等其他材料。吃到嘴里香、
滑、甜、腻、柔和中带有质感的变化，味道并不是一味的甜。"""
#创建一个Label
textLabel = Label(root, #将内容绑定在初始窗体root上
    text=tiramisuTxt,
    justify=LEFT,       #文本的对齐方式
    padx=20,pady=10)    #Label显示的外边距 
textLabel.pack(side=LEFT)        #将Label装入窗体，靠左显示

#创建一个图片Label
tiramisuPic=PhotoImage(file="tiramisu.png")   #创建图片对象
imgLabel = Label(
    root,               #父组件
    image=tiramisuPic) #image属性指明要显示的图片对象
imgLabel.pack(side=RIGHT)       #将Label装入窗体，靠右显示

#定制窗体
root.title("提拉米苏")          #设置标题
root.iconbitmap("tiramisu.images") #设置图标
root.mainloop()
