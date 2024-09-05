#打开文件：

file1 = open('filename.txt', 'r')  # 只读模式
file2 = open('filename.txt', 'w')  # 只写模式（覆盖）
file3 = open('filename.txt', 'a')  # 追加模式
file4 = open('filename.txt', 'rb')  # 二进制读1取模式
#读取文件内容：


content1 = file1.read()       # 读取整个文件
content = file2.read(100)    # 读取指定字符数
lines = file3.readlines()    # 读取所有行并返回列表
#逐行读取文件：

for line in file1:
    print(line, end='')  # 打印每一行
#写入文件内容：

file1.write('Some text')  # 写入文本
#追加内容：

with open('filename.txt', 'a') as file:
    file.write('\nAppended text.')
#关闭文件：


file.close()  # 关闭文件
#使用 with 语句（推荐）：


with open('filename.txt', 'r') as file:
    content = file.read()
    print(content)
#检查文件是否存在：

import os
if os.path.exists('filename.txt'):
    print("File exists")
#获取文件信息：

import os
file_info = os.stat('filename.txt')
print(file_info.st_size)  # 文件大小