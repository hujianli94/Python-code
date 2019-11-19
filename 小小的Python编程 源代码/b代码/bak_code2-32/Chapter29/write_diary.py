#本件操作示例
import diary_op
file_name="C:\Workspace\Chapter29\diary.book"

#写入新日记
try:
    fo=open(file_name,'a')
    new_diary=diary_op.new_diary()
    fo.write(new_diary)
    print("=======写入成功！=======")
except:
    print("发生错误，写入失败")
    raise
finally:
    fo.close()

