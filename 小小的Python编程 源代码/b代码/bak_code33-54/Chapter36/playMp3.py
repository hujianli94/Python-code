#播放mp3
import pygame
file="music\\bgm.mp3"
#初始化
pygame.mixer.init()
print("播放音乐")
#加载
track = pygame.mixer.music.load(file)
#播放
while 1:
    #检查音乐流播放，如果没有音乐流则选择播放
    q=input("按【Enter】键播放，再次按【Enter】键停止")
    if pygame.mixer.music.get_busy()==False:
        pygame.mixer.music.play(5)
    elif q=='':
        pygame.mixer.music.stop()
        break


