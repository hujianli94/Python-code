#播放wav文件
import winsound

def play(event):
    global wav
    wav=winsound.PlaySound("music\\sample.wav",winsound.SND_ASYNC)
    print(event)
def stop(event):
    winsound.PlaySound(wav,winsound.SND_PURGE)

from tkinter import *
root=Tk()

btn1=Button(root,
            width=20,
            height=1,
           text='播放')
btn2=Button(root,
            width=20,
            height=1,
            text='停止')
btn1.pack(side=LEFT)
btn2.pack(side=RIGHT)
btn1.bind('<ButtonRelease-1>',play)
btn2.bind('<ButtonRelease-1>',stop)
root.mainloop()
