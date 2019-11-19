#随机数应用示例1
import random
customNumber=[]                     #顾客小票号码
for i in range(1,31):               #假设号码从1到30
    customNumber.append(i)
lucky=random.choice(customNumber)
print("今天全部的小票号码是：",customNumber)
print("今天的幸运儿是：小票号码为",lucky,"的顾客！")
    

