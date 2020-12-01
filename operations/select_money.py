#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/1 9:36
# @Author : gaoxuejian
# @Site : 
# @File : select_money.py
# @Software: PyCharm

import money

def select():
    if money.money == 1000:
        print(f"还没有发工资，工资是：{money.money}")
    elif money.money == 2000:
        print("发工资了，好高兴，工资是{}".format(money.money))
    else:
        print("出错啦！")