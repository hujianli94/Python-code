#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/21 10:32
# filename: 分页的类.py

class Pagination(object):
    """
    分页相关的代码
    """

    def __init__(self, data_list, page, per_page=30):
        """

        :param data_list: 数据的列表
        :param page: 当前查看的页面
        :param per_page: 每页默认要显示的行数
        """
        self.data_list = data_list
        self.page = page
        self.per_page = per_page

    @property
    def start(self):
        """
        计算索引的起始位置
        :return:
        """
        return (self.page - 1) * self.per_page

    @property
    def end(self):
        """
        计算分页的结束位置
        :return:
        """
        return self.page * self.per_page

    @property
    def check_show(self):
        res = None
        if self.page * self.per_page > len(self.data_list):
            print("--------已为您打开最后一页-------------")
            last_index = int(len(self.data_list)/self.per_page)
            self.page = last_index
            res = self.data_list[self.start:self.end]
        else:
            res = self.data_list[self.start:self.end]

        for index in res:
            print(index)



if __name__ == '__main__':

    # 模拟所有数据写入到一个list里面
    data_list = []
    for i in range(1, 901):
        data_list.append("hujianli-blog-{}".format(i))

    # 循环查看页面页数
    while True:
        page = int(input("请输入要查看的页数:"))
        obj = Pagination(data_list, page)
        obj.check_show
