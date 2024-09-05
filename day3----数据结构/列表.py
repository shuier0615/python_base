"""
    创建列表：my_list = [1, 2, 3]
    访问元素：my_list[0]（访问第一个元素）
    修改元素：my_list[1] = 4
    添加元素：my_list.append(5)
    删除元素：my_list.remove(2) 或 del my_list[0]
    切片：my_list[1:3]（获取子列表）
    排序：my_list.sort() 或 sorted(my_list)
    遍历：for item in my_list: print(item)
    列表推导式：[x * 2 for x in my_list]
    检查成员：3 in my_list
"""
#创建列表
my_list = [4,41,6,8,12,89,2]
#列表推导式
new_list = [i * 2 for i in my_list]
#访问元素
a  = my_list[0]
#修改元素
my_list[2] = 999
print(my_list)
#添加元素
my_list.append(88888)
print(my_list)
#删除元素
my_list.remove(4)
#切片
b = my_list[1:4]
print(b)
#排序
new_list.sort()
print(new_list)
#遍历
for i in my_list:
    print(i)

#检查成员
c = 5 in my_list
print(c)
#长度
print(len(my_list))
