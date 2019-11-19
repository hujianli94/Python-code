#!/usr/bin/env python
#-*- coding:utf8 -*-

#文件和目录操作
'''
# 循环读取old.txt文件内容并写入到new.txt文件当中
shutil.copyfileobj(open("old.txt",'r'),open('new.txt','w'))

shutil.copyfile(src, dst, *, follow_symlinks=True)
拷贝整个文件，没有第二个文件就创建，有就覆盖
shutil.copyfile('old.txt','new.txt')

shutil.copymode(src, dst, *, follow_symlinks=True)
仅拷贝文件权限，文件的内容、组、用户均不变
shutil.copymode('old.txt', 'new.txt')

shutil.copy(src, dst, *, follow_symlinks=True)
#拷贝文件和状态信息，同样不copy改动时间

shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False)
递归的去拷贝文件夹

shutil.rmtree(path, ignore_errors=False, onerror=None)
递归的去删除文件

shutil.move(src, dst, copy_function=copy2)
递归的去移动文件，它类似mv命令，其实就是重命名。

shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]])
Create an archive file (such as zip or tar) and return its name.

可选参数如下：
参数	说明
base_name	压缩包的文件名，也可以是压缩包的路径。
format	压缩包种类，“zip”, “tar”, “bztar”，“gztar”
root_dir	要压缩的文件夹路径（默认当前目录）
owner	用户，默认当前用户
group	组，默认当前组

shutil.make_archive("/home/ansheng/folder3", 'gztar', root_dir='/home/ansheng/folder3')
# 返回文件打包放在那儿了
'/home/ansheng/folder3.tar.gz'
'''