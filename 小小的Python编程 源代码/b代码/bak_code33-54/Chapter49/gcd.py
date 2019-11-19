#辗转相除法的实现
def gcd(a,b):
    if a<b:
        a,b =b,a    #交换两数值，大数作被除数，小数作除数
    while b!=0:
        temp=a%b    #a/b的余数
        a=b         #除数作为新一轮的被除数
        b=temp      #余数作为新一轮的除数
    return a

def lcm(a,b):
    return a*b/gcd(a,b)      #最小公倍数即两数积除以最大公约数

#求两数最大公约数和最小公倍数
a=int(input("输入第一个整数："))
b=int(input("输入第二个整数："))
print('%d 和 %d 的最大公约数为：' %(a,b),gcd(a,b))
print('%d 和 %d 的最小公倍数为：' %(a,b),lcm(a,b))
