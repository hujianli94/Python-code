#!/usr/bin/env python
#-*- coding:utf8 -*-
import os
import shutil
file_info = "hujianli.py"
write_info='''#!/usr/bin/env python
#-*- coding:utf8 -*-
print("test")
print()
'''

def create_file(file):
    if not os.path.exists(file):
        with open(file,"w") as f:
            f.write(write_info)
    else:
        number = 1
        Flag = True
        while Flag:
            file_info_name = file.split('.')
            file_name = file_info_name[0] + "_bak" + str(number) +"."+file_info_name[1]
            if not os.path.exists(file_name):
                with open(file) as f1,open(file_name,"w") as f2:
                    f2.write(f1.read())
                    Flag = False
            number +=1

class FileMgr:
    '自定义一个打开文件，后自动关闭文件的上下文管理器'
    def __init__(self,filename):
        self.filename = filename
        self.f = None

    def __enter__(self):
        self.f = open(self.filename,encoding='utf-8')
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.f:
            self.f.close()

if __name__ == "__main__":
    create_file(file_info)
    with FileMgr(file_info) as f:
        for line in f.readlines():
            print(line,end='')
