#创建类
class Xcake:
    name="古怪蛋糕"
    colorNumber=5
    color=['红','黄','蓝','绿','黑']
    shape='三角形'
    creamContent=0

    def eat(self):
        return '吃我啊！吃我啊！'

    def drink(self):
        return '喝我啊！喝我啊！'

    def sell(self):
        return '买我啊！买我啊！'

#创建类
class XcakePlus:    
#定义类变量，也称属性
    name="古怪蛋糕加强版"
    size=None                                       #蛋糕的尺寸
    price=15                                        #单价
        
#定义构造方法
    def __init__(self,size,qty):
        self.size=size
        self.qty=qty
        
#定义其他方法
    def eat(self):
        print('吃我啊！吃我啊！')
    def sumPrice(self):                                 #计算总价
        print("一共：",self.qty*self.price,"元")       
    def preview(self):
        print("您要的蛋糕是:",self.name,"，尺寸：",self.size,"号",self.qty,"个。")
