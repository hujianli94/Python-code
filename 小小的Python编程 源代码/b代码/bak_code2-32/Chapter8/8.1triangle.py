#8.1triangle.py
a=int(input('输入三角形的边长a：'))
b=int(input('输入三角形的边长b：'))
c=int(input('输入三角形的边长c：'))
if a+b>c and b+c>a and a+c>b:
    print('可以组成三角形')
    if a==b or b==c or a==c:
        print('等腰三角形')
        if a==b and b==c:
            print('等边三角形')                
else:
    print('不能组成三角形')
