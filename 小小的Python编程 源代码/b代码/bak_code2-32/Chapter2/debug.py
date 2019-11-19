cake=input('您买哪种蛋糕？[1]提拉米苏；[2]维也纳巧克力杏仁蛋糕');
cake1=12;cake2=15;price=0;
num=input("您需要买几个？");
if cake==1:
    price=cake1*num;
elif cake==2:
    price=cake2*num;
print("您总共需要付："+price+'元钱。');
