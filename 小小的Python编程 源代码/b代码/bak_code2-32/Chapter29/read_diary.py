#读取日记
import diary_op
file_name="C:\Workspace\Chapter29\diary.book"
try:
    fo=open(file_name,'r')
    diary_op.read_diary(fo)
except:
    raise
finally:
    fo.close()
