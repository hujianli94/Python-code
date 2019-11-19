#移动示例
import time      
from tkinter import*

window=Tk()       #建立主窗体
canvas=Canvas(window,width=500,height=500)     #建立一个画布对象canvas
canvas.pack()
#建立多边形，顶点坐标（x1,y1,x2,y2,x3,y3）
canvas.create_polygon(10,10,10,60,50,35,fill='red')   #图形编号为1，以后的图形编号顺序类推

def draw_one_frame():
    canvas.move(1,5,0)  #移动1号对象，x方向移动5像素，y方向移动0像素

def animate():
    draw_one_frame()
    window.after(100,animate)

window.after(100,animate)
window.mainloop()



