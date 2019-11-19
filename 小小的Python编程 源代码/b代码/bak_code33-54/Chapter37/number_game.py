#猜数游戏
#导入所需模块
import tkinter as tk
import sys
import random
import re
import pygame

#初始化猜数的范围
number = random.randint(0,1024)
isRunning = True
num = 0
maxNum = 1024
minNum = 0

#处理声音
pygame.mixer.init()
def playSound(flag):
    screen=pygame.display.set_mode([1,1])#临时措施
    if flag==1:#猜小了
        file="sound\\small.wav"
    elif flag==2:#猜大了
        file="sound\\big.wav"
    elif flag==3:#答对了
        file="sound\\right.wav"
    elif flag==4:#一次答对
        file="sound\\impossible.wav"
    elif flag==5:#十次以内
        file="sound\\wanderful.wav"
    elif flag==6:#50次以内
        file="sound\\good.wav"
    elif flag==7:#超50次
        file="sound\\goon.wav"
    elif flag==8:#quit
        file="sound\\quit.wav"
    sound=pygame.mixer.Sound(file)
    sound.play() 

def playMusic():
    file="sound\\bgm.mp3"
    pygame.mixer.music.load(file)   #载入音乐文件
    pygame.mixer.music.set_volume(0.2)  # 设置音量
    pygame.mixer.music.play(-1)    #循环播放

#处理事件
#关闭
def ebtnClose(event):
    playSound(8)
    pygame.mixer.music.stop()
    root.destroy()
    pygame.quit()
#猜数    
def ebtnGuess(event):
    global maxNum
    global minNum
    global num
    global isRunning
    #用户在答对后，提示标签不再变化
    if isRunning:
        val_a = int(entry_a.get())
        if val_a == number:
            labelqval("恭喜答对了！")
            playSound(3)    #播放猜对的音效
            num+=1  #记录猜测次数
            isRunning = False   #更新猜测状态
            guessComment()  #更新显示文字
        elif val_a < number:
            if val_a > minNum:
                minNum = val_a
                num+=1
                label_tip_min.config(label_tip_min,text=minNum)
            labelqval("小了哦")
            playSound(1)
        else:
            if val_a < maxNum:
                maxNum = val_a
                num+=1
                label_tip_max.config(label_tip_max,text=maxNum)
            labelqval("大了哦")
            playSound(2)
    else:
        labelqval('你已经答对啦...')
        playSound(3)

#交互信息
def guessComment():
    if num == 1:
        labelqval('一次答对！真厉害！')
    elif num < 10:
        labelqval('十次以内就答对了，真厉害！尝试次数：'+str(num))
    elif num < 50:
        labelqval('终于答对了，不错！尝试次数：'+str(num))
    else:
        labelqval('您已经试了超过50次了，坚持就是胜利！尝试次数：'+str(num))
#提示文字标签        
def labelqval(vText):
    label_val_q.config(label_val_q,text=vText)   

#创建窗体   
root = tk.Tk(className="猜数游戏")
root.geometry("400x90+200+200")

line_a_tip = tk.Frame(root)
label_tip_max = tk.Label(line_a_tip,text=maxNum)
label_tip_min = tk.Label(line_a_tip,text=minNum)
label_tip_max.pack(side = "top",fill = "x")
label_tip_min.pack(side = "bottom",fill = "x")
line_a_tip.pack(side = "left",fill = "y")

line_question = tk.Frame(root)
label_val_q = tk.Label(line_question,width="80")
label_val_q.pack(side = "left")
line_question.pack(side = "top",fill = "x")

line_input = tk.Frame(root)
entry_a = tk.Entry(line_input,width="40")
btnGuess = tk.Button(line_input,text="猜数")
entry_a.pack(side = "left")
#事件绑定
entry_a.bind('<Return>',ebtnGuess)
btnGuess.bind('<Button-1>',ebtnGuess)
btnGuess.pack(side = "left")
line_input.pack(side = "top",fill = "x")

line_btn = tk.Frame(root)
btnClose = tk.Button(line_btn,text="关闭")
btnClose.bind('<Button-1>',ebtnClose)
btnClose.pack(side="left")
line_btn.pack(side = "top")

labelqval("请输入0到1024之间的任意整数：")
entry_a.focus_set()

#启动窗体
print(number)
playMusic()
root.mainloop()
