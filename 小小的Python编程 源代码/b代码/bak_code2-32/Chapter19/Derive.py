#类的继承
#父类Cake
class Cake:
    #定义类变量
    name="蛋糕"
    color=['黄']
    
    #定义方法
    def eat(self):
        return "吃自己"

    def preview(self):
        return "名字："+self.name+"；颜色："+str(self.color)

    def showClass(self):
        print(self,"的类名",self.__class__.__name__)

#子类Xcake
class Xcake(Cake):
    #定义类变量
    name="古怪蛋糕"
    color=['红','黄','蓝','绿','黑']
    shape="三角形"
    creamContent=0

    #定义方法
    def drink(self):
        return "喝自己"

#子类XcakePlus
class XcakePlus(Xcake):
    #定义类变量
    name="古怪蛋糕加强版"
    price=15

    #定义构造方法
    def __init__(self,size,qty):
        self.size=size
        self.qty=qty

    #定义方法
    def sumPrice(self):                                 #计算总价
        print("一共：",self.qty*self.price,"元")
        
    def preview(self):                                  #重写方法preview
        print("您要的蛋糕是：",self.name,"，尺寸：",self.size,"号",self.qty,"个。")
    
