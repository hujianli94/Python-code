#画直线
from tkinter import *
master = Tk()

#创建画布
canvas_width = 800
canvas_height = 400

myPaper = Canvas(master, 
    width=canvas_width,
    height=canvas_height,
    background='white')
myPaper.pack()

#绘制直线
x1,y1=50, int(canvas_height/2)
x2,y2=int(canvas_width/2),50
myPaper.create_line(x1,y1,x2,y2,fill="red",width=2)

x3,y3=canvas_width-50,int(canvas_height/2)
myPaper.create_line(x2,y2,x3,y3,fill="green",width=2)

x4,y4=int(canvas_width/2),canvas_height-50
myPaper.create_line(x3,y3,x4,y4,fill="blue",width=2)

myPaper.create_line(x4,y4,x1,y1,fill="black",width=2)

#绘制文字
text1="("+str(x1)+","+str(y1)+")"
myPaper.create_text(x1-10,y1+20,text=text1)
text2="("+str(x2)+","+str(y2)+")"
myPaper.create_text(x2,y2-20,text=text2)
text3="("+str(x3)+","+str(y3)+")"
myPaper.create_text(x3-10,y3+20,text=text3)
text4="("+str(x4)+","+str(y4)+")"
myPaper.create_text(x4,y4+20,text=text4)
myPaper.create_text(int(canvas_width/2),int(canvas_height/2),
        text="Canvas绘图示例",
        font=('Times',22))

#绘制方形和椭圆
import random
for i in range(3):
    x=random.randint(50, 800)
    y=random.randint(50, 800)
    m=random.randint(100, 400)
    n=random.randint(50, 200)
    myPaper.create_rectangle(x, y,m,n, fill="yellow")
    myPaper.create_oval(x,n,m,y,fill="blue")

#主循环
master.mainloop()
