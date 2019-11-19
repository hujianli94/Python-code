#系统信息
import time,platform
#1.当前时间
print("------------------------1.当前时间----------------------------")
now=time.localtime(time.time())
now=time.strftime("%Y-%m-%d %H:%M:%S",now)
print("当前时间：",now)

#2.平台信息
print("\n------------------------2.平台信息----------------------------")
print("操作系统：",platform.system())
print("操作系统版本：",platform.version())
#获取操作系统的类型和位数
print("基于",platform.machine(),"机器的",platform.architecture(),"架构计算机") 
print("网络名：",platform.node())
print("处理器：",platform.processor())

#3.目录信息
import os
print("\n------------------------3.目录信息----------------------------")
print("当前文件系统名称：",os.name)
current=os.getcwd()
print("当前目录：",current)
print("当前目录文件：",os.listdir(current))
print("根目录绝对路径：",os.path.abspath('.'))
print("根目录文件：",os.listdir('.'))
mtime=time.localtime(os.path.getmtime(current))
mtime=time.strftime("%Y-%m-%d %H:%M:%S",mtime)
print("当前文件夹最后修改时间：",mtime)

#4.文件信息
import stat
print("\n------------------------4.文件信息----------------------------")
testfile=os.path.abspath('aROtestfile')
os.chmod(testfile,stat.S_IREAD)
mode_dict={0:'存在',4:'只读',2:'可写',1:'可执行'}
print("文件",testfile,"的权限为：")
for mode in (os.F_OK,os.R_OK,os.W_OK,os.X_OK):
    print(mode_dict[mode],':',end='')
    if os.access(testfile,mode):
        print("True")
    else:
        print("Flase")
thisfile=os.path.abspath('sys_info.py')
print(thisfile,"文件大小：",os.path.getsize(thisfile),"字节")


#5.调用系统命令
print("\n------------------------5.执行系统命令----------------------------")
while 1:
    cmd=input("============\n|1.网络信息|\n|2.画图板  |\n|3.计算器  |\n============\n")
    if cmd in ('1','2','3'):
        if cmd=='1':
            ipcon=os.popen('ipconfig').read()
            print(ipcon)
        if cmd=='2':
            os.popen('mspaint')         #启动画板
        if cmd=='3':
            os.popen('calc')            #启动计算器
    else:
        print("输入无效。")
        break
