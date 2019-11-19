#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/20 11:53
# filename: 模拟Java的输入输出流.py

def FileinputStrem(filename):
    """
    文件输入流
    :return:
    """
    try:
        f = open(filename)
        for line in f:
            for byte in line:
                yield byte
    except StopIteration as e:
        f.close()
        return


def FileoutputStrem(inputStream, filename):
    """
    文件输出流
    :return:
    """
    try:
        f = open(filename, "w")
        while True:
            byte = inputStream.__next__()
            f.write(byte)
    except StopIteration as e:
        f.close()
        return


if __name__ == '__main__':
    FileoutputStrem(FileinputStrem("hello.txt"), "hello2.txt")
