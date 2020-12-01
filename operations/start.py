#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/1 9:39
# @Author : gaoxuejian
# @Site : 
# @File : start.py
# @Software: PyCharm

from select_money import select
from send_money import send

if __name__ == '__main__':
    print("开始啦")
    send()
    select()
    print("结束啦")