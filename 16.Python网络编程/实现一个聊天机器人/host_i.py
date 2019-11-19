# 主机1
import socket

print('小i：你好，我是小i，有什么可以帮您？')
local_addr = ('localhost', 10000)  # 本地主机发送端口
# 目标主机接收端口，请根据实际情况设定ip地址
remote_addr = ('127.0.0.1', 20000)

# 创建socket对象，DGRAM方式。专门用于发送
ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# socket对象绑定地址及端口
ss.bind(local_addr)

while 1:
    sendData = input("发送:")
    if sendData == 'quit':
        break
    # 通过socket向远端主机发消息
    ss.sendto(sendData.encode("utf-8"), remote_addr)
    # 通过socket接收消息和地址
    reciveData, rec_addr = ss.recvfrom(1024)
    if reciveData:
        print("小i@", rec_addr)
        print("发来消息 :", reciveData.decode())
ss.close()
