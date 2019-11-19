#!/usr/bin/env python
# -*- coding:utf8 -*-
def package_postion(*all_arguments):
    print(type(all_arguments))
    print(all_arguments)


package_postion(1, 4, 6, 8, 9)
print("第二次调用".center(100, "="))
package_postion(2, 6, 7, 8, 9)


def package_keyword(**all_arguments):
    print(type(all_arguments))
    print(all_arguments)


print("初次调用".center(100, '='))
package_keyword(a=1, b=9)
print("再次调用".center(100, '='))
package_keyword(m=2, n=1, c=11)
