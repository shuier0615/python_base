# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day01
   Description :
   Author :       水儿
   date：          2024/09/11
-------------------------------------------------
   Change Activity:
                   2024/09/11:
-------------------------------------------------
"""
__author__ = '水儿'

#变量
url = 'https://www.baidu.com/'
#控制流
if 'y' in url:
    print('在')
else:
    print('不在')
#数据类型
print(type(url))

xw = 'xinwen'
#运算符
new_url = url+xw
print(new_url)


def myfuction(a,b):
    return a+b

print(myfuction(5,6))
#转小写
print(url.lower())
#转大写
print(url.upper())
#首字母大写
print(url.capitalize())
#首每个单词首字母转大写
print(new_url.title)
#去除空白符号两端
print(url.strip())
#切片
print(url.split('.'))
#链接字符串
print(':'.join(['192.168.0.2','8080']))
#替换
print('hello word'.replace('word','python'))
#寻找
print(url.find('a'))
#格式化输出
print('我的名字叫{}，今年{}岁'.format('小明',15))