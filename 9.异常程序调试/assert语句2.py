#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
assert <条件测试>.<异常附件数据>
'''


# assert语句时简化的raise语句，它引发异常的前提是其后面的条件测试为假
def testAssert():
    for i in range(3):
        try:
            assert i < 2, "大于2了！！！"
        except AssertionError as e:
            print("Raise a AssertionError!", e)
        print(i)
    print('end......')


try:
    raise Exception('错误')
except Exception as e:
    print(e)

if __name__ == '__main__':
    testAssert()
