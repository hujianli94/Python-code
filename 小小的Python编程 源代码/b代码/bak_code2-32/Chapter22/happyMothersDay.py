#母亲节是哪一天
import calendar,time
print(calendar.month(2018,5))
mayCal=calendar.monthcalendar(2018,5)
#print(calendar.monthcalendar(2018,5))

mothersDay=mayCal[1][6]
print("2018年的母亲节是5月",mothersDay,"日\n")

#免费送蛋糕
presented=[]
visitRecord={}
while 1:
    #输入生日
    name=input("请输入顾客的姓名(输入q退出)：")
    if name=='q':
        break
    if name not in presented:
        print("未领取。请赠送'忘忧草蛋糕'一份！")
        presented.append(name)
        visitRecord[name]=[time.asctime(time.localtime())]
    else:
        print("已领取！")
    print(presented)
print("今日到访顾客及时间：",visitRecord)



