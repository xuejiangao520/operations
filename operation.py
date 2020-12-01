#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/1 9:26
# @Author : gaoxuejian
# @Site : 
# @File : operation.py
# @Software: PyCharm

"""
课后作业
原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额
"""

money = 1000

def sendmoney():
    global money
    # print("发工资了好高兴")
    money = 2000

def showmoney():
    if money == 1000:
        print(f"还没有发工资，工资是：{money}")
    elif money == 2000:
        print("发工资了，好高兴，工资是{}".format(money))
    else:
        print("出错啦！")

if __name__ == '__main__':
    sendmoney()
    showmoney()