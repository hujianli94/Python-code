#绘制图像
from tkinter import *
root=Tk()
root.title("三国名人录")
#root.iconbitmap("souffle.images")
#窗体尺寸
root.geometry('500x700+600+20') #宽x高+左边距+上边距

def sango_show(event):
    #将图片文件声明为全局变量
    global img1,img2,img3,img4    
    #获取按钮文本
    ID=event.widget['text']
    print(ID)
    #加载图片
    if ID==sango[0]:
        myCanvas.create_image(0,0,anchor=NW,image=img0)
    elif ID==sango[1]:
        myCanvas.create_image(0,0,anchor=NW,image=img1)
    elif ID==sango[2]:
        myCanvas.create_image(0,0,anchor=NW,image=img2)
    elif ID==sango[3]:
        myCanvas.create_image(0,0,anchor=NW,image=img3)

#图片
img0=PhotoImage(file='pictures\\张飞.png')
img1=PhotoImage(file='pictures\\吕布.gif')
img2=PhotoImage(file='pictures\\貂蝉.png')
img3=PhotoImage(file='pictures\\孔明.gif')         

#Frame布局
fm1=Frame(root)
fm1.pack(side=TOP,padx=10,pady=10)
fm2=Frame(root)
fm2.pack()

#创建画布
myCanvas=Canvas(fm2,width=460,height=590,bg='black')
myCanvas.pack()

#文字
myCanvas.create_text(230,245,text='三国名人录',
        font=("隶书",48),fill='red')

#按钮
sango=['张飞','吕布','貂蝉','孔明']
b=[]
for i in range(4):
    b.append(Button(fm1,text=sango[i],font=('KaiTi',32,'bold'),
             width=5,height=1))
    b[i].pack(side=LEFT,anchor=NW)
    b[i].bind('<ButtonRelease-1>',sango_show)

root.mainloop()
