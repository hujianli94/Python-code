#队列演示
import queue                        #引入队列模块
line=queue.Queue()                  #创建队列
if line.empty():                 #测试队列是否为空
    print("队列line为空")
#向队列放入元素
for person in range(50):
    line.put("路人"+str(person))
line.put("小小")
line.put("爸爸")
#get()示例
x=line.get()
print(x)
x=line.get()
print(x)

#取出并依次打印队列里的元素
person=[]
for i in range(line.qsize()):
    person.append(line.get())
print(person)
