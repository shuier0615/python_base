# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     类的创建
   Description :
   Author :        水儿
   date：          2024/09/06
-------------------------------------------------
   Change Activity:
                   2024/09/06:
-------------------------------------------------
"""
__author__ = '水儿'


# 定义类
class Person:
    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #定义方法
    def greef(self):
        return f'你好啊，我的名字是{self.name}，今年{self.age}岁了'

if __name__ == '__main__':
    # 实例化对象
    person = Person("Alice", 30)
    # 访问属性
    print(person.name)  # 输出: Alice
    print(person.age)  # 输出: 30
    print(person.greef())