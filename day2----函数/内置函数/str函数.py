# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     str函数
   Description :
   Author :        水儿
   date：          2024/09/06
-------------------------------------------------
   Change Activity:
                   2024/09/06:
-------------------------------------------------
"""

__author__ = '水儿'
# 字符串
a = str('aaa')
# str.upper()：将字符串转换为大写。
b = a.upper()
print(b)
# str.lower()：将字符串转换为小写。
c = b.lower()
print(c)
# str.capitalize()：将字符串的第一个字符转换为大写，其余字符转换为小写。
d = 'dLJLJjljlLJKLNLJ'
d1 = d.capitalize()
print(d1)
# str.title()：将每个单词的首字母转换为大写。
f = 'my is ball'
g = f.title()
print(g)
# str.strip()：去除字符串两端的空白字符。
j = '    sdada   ,adsasda    '
k = j.strip()
print(k)
# str.split(sep)：根据指定分隔符将字符串拆分成列表。
aa = 'da,sad,dad,sads,sad,w,w,dw'
aaa = aa.split(',')
print(aaa)

# str.join(iterable)：将可迭代对象中的字符串连接成一个字符串，使用指定的分隔符。
s = ":".join(["2024", "09", "06"])
print(s)  # 输出: "2024-09-06"

# str.replace(old, new)：将字符串中的指定子字符串替换为另一个子字符串。
s = "hello world"
print(s.replace("world", "Python"))  # 输出: "hello Python"


#str.find(sub)：查找子字符串 sub 在字符串中的位置。如果未找到，返回 -1。
s = "hello world"
print(s.find("world"))  # 输出: 6

#str.format()：格式化字符串，将大括号 {} 中的内容替换为指定的值。
s = "Hello, {}!"
print(s.format("Alice"))  # 输出: "Hello, Alice!"

