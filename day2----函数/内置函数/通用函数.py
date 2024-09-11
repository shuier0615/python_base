# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     通用函数
   Description :
   Author :       水儿
   date：          2024/09/08
-------------------------------------------------
   Change Activity:
                   2024/09/08:
-------------------------------------------------
"""
__author__ = '水儿'

import asyncio

import asciimatics.effects
import mpmath
from aiohttp import request

#len(): 返回对象的长度。
len("hello")  # 输出: 5

#type(): 返回对象的类型。
type(42)  # 输出: <class 'int'>

#range(): 生成一个整数序列。
list(range(5))  # 输出: [0, 1, 2, 3, 4]

#sum(): 计算可迭代对象的总和。
sum([1, 2, 3])  # 输出: 6

#sorted(): 返回一个排序后的列表。
sorted([3, 1, 2])  # 输出: [1, 2, 3]

#map(): 应用函数到可迭代对象的每个元素。
list(map(str, [1, 2, 3]))  # 输出: ['1', '2', '3']

#filter(): 过滤可迭代对象中的元素。
list(filter(lambda x: x > 2, [1, 2, 3]))  # 输出: [3]

#zip(): 将多个可迭代对象打包成一个元组的迭代器。
list(zip([1, 2], ['a', 'b']))  # 输出: [(1, 'a'), (2, 'b')]

#all() 和 any(): 判断可迭代对象中的所有元素或任一元素是否为真。
all([True, True, False])  # 输出: False
any([True, False, False])  # 输出: True
