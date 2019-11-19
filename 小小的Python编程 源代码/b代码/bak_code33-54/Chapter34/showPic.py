#绘制图像
from tkinter import *
root=Tk()

#创建画布
myCanvas=Canvas(root,width=460,height=590,bg='black')
myCanvas.pack()

img0=PhotoImage(file='pictures//孔明.gif')
myCanvas.create_image(1,1,anchor=NW,image=img0)
