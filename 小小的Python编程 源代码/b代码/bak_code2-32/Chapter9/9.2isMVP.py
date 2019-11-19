#身份运算符示例
team=['乔丹','邓肯','科比','马小小','詹姆斯','韦德','奥拉朱旺','哈登']
print('梦之队:',team)
#我是小小
me='马小小'
if me in team:
    print(me,'是这只球队的成员！')
else:
    print(me,'不是这只球队的成员！')
    
#我是MVP
mvp=me
if me is mvp:
    print(me,'是MVP！')
else:
    print(me,'不是MVP！')

#隔壁班的“小小”，自称MVP
he='刘小小'
if he is mvp:
    print(he,'是MVP！')
else:
    print(he,'不是MVP！') 
