#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/12 16:14
# filename: 猜单词游戏.py
import random

# 创建单词序列
WORDS = ['python', 'junble', 'easy', 'difficult', 'answer', 'continue', 'phone', 'position', 'pose', 'game']

# 开始游戏
print("""
                (｡♥ᴗ♥｡) 欢迎参加猜单词游戏  (｡♥ᴗ♥｡)  
                            
                                      ,;,,;
                                     ,;;'(    马
                           __      ,;;' ' \   ┇
                        /'  '\'~~'~' \ /'\.)  到 
                     ,;(      )    /  |.      ┇
                    ,;' \    /-.,,(   ) \     成
                         ) /       ) / )|     ┇ 
                         ||        ||  \)     功
                         (_\       (_\
                         
                         
            (♥ω♥ ) ~♪ 把字母组合成一个正确的单词. (♥ω♥ ) ~♪ 
        
        

""")

iscontinue = "y"

while iscontinue == "y" or iscontinue == "Y":
    # 从序列中随机挑出一个单词
    word = random.choice(WORDS)

    # 用于判断玩家是否猜对的变量
    correct = word

    jumble = ""  # 创建乱序后的单词
    while word:
        # 根据word的长度产生word的随机位置
        position = random.randrange(len(word))

        # 将position位置的字母组合到乱序后单词
        jumble += word[position]

        # 通过切片将position位置的字母从原单词中删除
        word = word[:position] + word[(position + 1):]


    print("乱序后的单词: 【{}】  ❔❔❔❔".format(jumble))

    guess = input('\n😀😀😀请你猜 >: ')
    while guess != correct and guess != '':
        print("对不起不正确.😭")
        guess = input("请继续猜：")
    if guess == correct:
        print("真棒，你猜对了！👍")

    iscontinue = input("\n 是否继续(Y/N):")
