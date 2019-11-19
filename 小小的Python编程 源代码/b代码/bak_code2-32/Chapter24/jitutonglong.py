#鸡兔同笼
def jitutonglong(tou,jiao):
    ji=0
    while 1:
        tu=tou-ji
        if 2*ji+4*tu==jiao:
            print("鸡有：",ji,"只")
            print("兔有",tu,"只")
            break
        ji+=1
    
