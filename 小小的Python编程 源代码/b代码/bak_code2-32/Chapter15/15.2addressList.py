#字典示例程序
addressList={'牛牛':'四眼桥五里屯6号','小花':'解放街凯旋路18号','石头':'美丽村杨树林胡同7号','小丁':'南湖大道文化街9号院'}
print("---------------小小的通讯录---------------")
print("addressList=",addressList)
while True:
    op=input("请选择要做的操作：【1】添加；【2】修改；【3】删除；【0】退出\n")
    if int(op)==0:
        break
    elif int(op)==1:                   #添加元素
        name=input("新增姓名：")
        addr=input("住址：")
        addressList[name]=addr
        print("已添加")
    elif int(op)==2:                   #修改元素
        name=input("姓名(请勿写错)：")
        print(name,"的原地址为：",addressList[name])
        addrNew=input("请输入新的地址：")
        addressList[name]=addrNew
        print("已修改")
    elif int(op)==3:                   #删除元素
        name=input("姓名(请勿写错)：")
        print("【警告】需要删除姓名为",name,"的记录吗？")
        comfirm=input("回答Yes确认")
        if comfirm.lower()=='yes':
            del addressList[name]
            print("记录已删除")
        else:
            print("未删除")
print("addressList=",addressList)
print("------------------已退出------------------")
        

