# 小小机器人
def cake_bot(in_msg):
    import random
    cake_dict = {
        '提拉米苏': '提拉米苏（Tiramisù），为一种有名的意大利式蛋糕，又可译成堤拉米苏。提拉米苏是由泡过咖啡或兰姆酒的手指饼干，加上一层马斯卡彭、蛋黄、干酪、糖的混合物，然后再在蛋糕表面洒上一层可可粉而成。',
        '瑞士卷': '瑞士卷是海绵蛋糕（sponge cake）的一种。在烤炉中将材料烤成薄薄的蛋糕，加上了果酱和奶油（混糖奶油，牛奶蛋糊奶油等），和切碎了的果肉，卷成卷状。另外可以加上混和的可可粉和咖啡粉，形成松软的海绵质感的卷蛋糕。',
        '黑森林': '黑森林蛋糕(Schwarzwaelder Kirschtorte)是德国著名甜点，制作原料主要有脆饼面团底托、鲜奶油、樱桃酒等。是受德国法律保护的甜点之一，在德文里全名"Schwarzwaelder" 即为黑森林。它融合了樱桃的酸、奶油的甜、樱桃酒的醇香。'}
    if in_msg in cake_dict.keys():
        return cake_dict[in_msg]
    else:
        reply = ['你说什么？',
                 '你说得对！',
                 '你想买哪种蛋糕？',
                 '提拉米苏？瑞士卷？还是黑森林？',
                 '我叫小i，你呢？']
        return random.choice(reply)


import socket

print('This is server_bot.')
local_addr = ('localhost', 20000)  # 本主机接收端口

# 创建socket对象，DGRAM方式
ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# socket对象绑定本主机地址及端口
ss.bind(local_addr)

while 1:
    # 通过socket接收消息和地址
    reciveData, rec_addr = ss.recvfrom(1024)
    if reciveData:
        print("from;", rec_addr)
        print("got message", reciveData.decode())
    # 通过socket向远端主机发消息
    echo = cake_bot(reciveData.decode())
    ss.sendto(echo.encode("utf-8"), rec_addr)
ss.close()
