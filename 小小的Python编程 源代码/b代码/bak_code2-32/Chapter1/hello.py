#在屏幕上打印姓名和成绩
score = [80,70,90]   #定义变量grades
min_grade = None     #定义变量min_grade最低分
max_grade = None     #定义变量grade _grade最高分
sum_grade = 0.0      #定义变量sum_grade总分
print ("我的名字是：小小。")	#输出相关信息
print ("本次考试我的语文成绩：%d"%score[0])
print ("            数学成绩：%d"%score[1])
print ("            英语成绩：%d"%score[2])
sum_grade = score[0]+ score[1]+score[2]    #求总分
ave_grade = sum_grade / 3		   #求平均分
min_grade=score.index(min(score))          #最低分
max_grade=score.index(max(score))          #最高分
print ("总  分:", sum_grade)               #打印出总分
print ("最高分:", score[max_grade])        #打印出最高分
print ("最低分:", score[min_grade])        #打印出最低分
print ("平均分:", ave_grade)               #打印出平均分
