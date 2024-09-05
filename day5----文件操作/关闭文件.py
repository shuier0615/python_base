# 使用 with 语句自动关闭文件
with open('destination.txt', 'w') as file:
    file.write('Hello, world!')
# 文件在退出 with 语句块后自动关闭