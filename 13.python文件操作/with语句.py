#!/usr/bin/env python
#-*- coding:utf8 -*-

class Sample:
    def __enter__(self):
        print("in __enter__")
        return "Foo"
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("in __exit__")
def get_sample():
    return Sample()
with get_sample() as sample:
    print("Sample: ", sample)

'''
整个运行过程如下：
（１）__enter__()方法被执行；
（２）__enter__()方法返回的值，在这个例子中是”Foo”，赋值给变量sample；
（３）执行代码块，打印sample变量的值为”Foo”；
（４）__exit__()方法被调用；
'''

#总结
'''
实际上，在with后面的代码块抛出异常时，exit()方法被执行。开发库时，清理资源，关闭文件等操作，都可以放在exit()方法中。
总之，with-as表达式极大的简化了每次写finally的工作，这对代码的优雅性是有极大帮助的。
如果有多项，可以这样写：
'''
with open('1.txt') as f1, open('2.txt') as  f2:
    #do something
