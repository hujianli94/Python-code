#正则表达式
import re
raw="燕子去了，有再来的时候；杨柳枯了，有再青的时候；桃花谢了，\
有再开的时候。但是，聪明的，你告诉我，我们的日子为什么一去不复返呢？——\
是有人偷了他们罢：那是谁？又藏在何处呢？是他们自己逃走了罢：现在又到了哪里呢？燕子"

patterns=["杨柳","燕子","桃花"]

print("===================原始字符串：")
print(raw)
print("===================正则表达式：")
for reg in patterns:
    print(reg)

#match
print("===================匹配字符串开头：")
for reg in patterns:
    matchObj=re.match(reg,raw)
    print("从头匹配原始字符串：)--->",matchObj)
    if matchObj:
        print("匹配结果：",matchObj.group())
        print("匹配位置：",matchObj.span())
    else:
        print("无匹配项")
      
#search
print("===================搜索整个字符串，进行匹配：")
for reg in patterns:
    matchObj=re.search(reg,raw)
    print("搜索原始字符串结果：)--->",matchObj)
    if matchObj:
        print("匹配结果：",matchObj.group())
        print("匹配位置：",matchObj.span())
    else:
        print("无匹配项。")

#更多模式
print("===================查找所有“了”字前面的动词：")
result=re.findall('([\S])了',raw)
for i in range(0,len(result)):
    print(result[i])
