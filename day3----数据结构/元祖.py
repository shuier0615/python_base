"""
    创建元组：my_tuple = (1, 2, 3)
    访问元素：my_tuple[0]（访问第一个元素）
    切片：my_tuple[1:3]（获取子元组）
    不可变性：元组一旦创建，不能修改其内容
    解包：a, b, c = my_tuple（将元组元素赋值给多个变量）
    合并：new_tuple = my_tuple + (4, 5)
    重复：repeated_tuple = my_tuple * 3
    检查成员：2 in my_tuple
    遍历：for item in my_tuple: print(item)
    长度：len(my_tuple)
"""
# 创建元祖
my_tuple = (8, 9, 6, 1, 45)
# 访问元祖
a = my_tuple[0]
print(a)
# 切片
b = tuple[1:3]
print(b)
# 解包
c, d, e, f, g = my_tuple
print(c, d, e, f, g)
# 合并
new_tuple = my_tuple + (9, 6, 8)
print(new_tuple)
# 重复
repeated_tuple = my_tuple * 3
print(repeated_tuple)
#检查成员
j = 4 in my_tuple
print(j)
#遍历
for i in my_tuple:
    print(i)

length = len(my_tuple)
print(length)



