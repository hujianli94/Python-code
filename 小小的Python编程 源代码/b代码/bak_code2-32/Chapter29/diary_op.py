#创建日记
def new_diary():
    import time
    str_diary="\n"
    end="end"
    now=time.asctime(time.localtime())
    str_diary+=now
    str_diary+="\n---------------------------------\n"
    title=input("请输入标题：")
    str_diary+="《"+title+"》"
    print(str_diary)
    print("(开始输入日记内容，输入end并回车结束）")
    line=""
    while line!="end":
        line=input()
        str_diary+="\n"+line
    return str_diary+"\n"

#读取全部日记
def read_diary(f):
    all_diary=f.read()
    print(all_diary)

#读取指定标题日记
def read_diary(f,title):
    start=0
    for line in f:
        if title in line:
            start=1
        if start==1:
            print(line,end='')
            if "end" in line:
                break
