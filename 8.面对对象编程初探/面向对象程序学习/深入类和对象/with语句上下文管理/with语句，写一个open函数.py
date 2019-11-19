#!/usr/bin/env python
#-*- coding:utf8 -*-
#上下文管理器
class FileMgr:

    def __init__(self, filename):
        self.filename = filename
        self.f = None

    def __enter__(self):
        self.f = open(self.filename,encoding="utf-8")
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.f:
            self.f.close()

if __name__ == '__main__':
    with FileMgr("aa.py") as f:
        for line in f.readlines():
            print(line,end=" ")