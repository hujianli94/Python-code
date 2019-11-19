#键盘控制图片的移动 
import time  
from tkinter import *  
def moveImage(event):#图片的移动要绑定的函数  
    if event.keysym=='Up':  
        canvas.move(1,0,-3)#移动ID为1的事物，使得横坐标加0，纵坐标减3  
    elif event.keysym=='Down':  
        canvas.move(1,0,+3)  
    elif event.keysym=='Left':  
        canvas.move(1,-3,0)  
    elif event.keysym=='Right':  
        canvas.move(1,3,0)  
    tk.update()  #更新窗体
      
tk=Tk()#窗口  
canvas=Canvas(tk,width=400,height=400,bg='white')#画布  
canvas.pack()  
myImage=PhotoImage(file='cake.png')  
  
img=canvas.create_image(200,200,image=myImage)#加载图片  
tips=canvas.create_text(10, 50, anchor=NW,text="使用键盘控制移动方向")#创建提示文字
print (img);print (tips)  #显示图片和提示文字的ID  
canvas.bind_all('<KeyPress-Up>',moveImage)#绑定方向键 up  
canvas.bind_all('<KeyPress-Down>',moveImage)  
canvas.bind_all('<KeyPress-Left>',moveImage)  
canvas.bind_all('<KeyPress-Right>',moveImage) 
