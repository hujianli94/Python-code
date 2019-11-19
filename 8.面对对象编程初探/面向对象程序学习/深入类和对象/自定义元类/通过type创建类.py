#!/usr/bin/env python
#-*- coding:utf8 -*-

print("一个简单type创建类的例子".center(100,"*"))
#type(object_or_name, bases, dict)
#type里面有三个参数，第一个类名，第二个基类名，第三个是属性
User = type("User",(),{"name":"derek"})

my_obj = User()
print(my_obj.name)    #derek

print(" 使用type创建类和方法 ".center(100,"*"))

#不但可以定义属性，还可以定义方法
def say(self):     #必须加self
    return "i am derek"

User = type("User",(),{"name":"derek","say":say})

my_obj = User()
print(my_obj.name)     #derek
print(my_obj.say())    #i am derek

print(" 让type创建的类继承一个基类 ".center(100,"*"))
def say(self):     #必须加self
    return "i am derek"

class BaseClass:
    def answer(self):
        return "i am baseclass"

#type里面有三个参数，第一个类名，第二个基类名，第三个是属性
User = type("User",(BaseClass,),{"name":"derek","say":say})

if __name__ == '__main__':

    my_obj = User()
    print(my_obj.name)          #d erek
    print(my_obj.say())         # i am derek
    print(my_obj.answer())      # i am baseclass