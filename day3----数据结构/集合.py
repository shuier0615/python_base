"""
    创建集合：my_set = {1, 2, 3}
    添加元素：my_set.add(4)
    删除元素：my_set.remove(2) 或 my_set.discard(2)
    检查成员：3 in my_set
    集合运算：my_set1.union(my_set2)（并集），
            my_set1.intersection(my_set2)（交集），
            my_set1.difference(my_set2)（差集）
    获取集合长度：len(my_set)
    遍历集合：for item in my_set: print(item)
    清空集合：my_set.clear()
    复制集合：new_set = my_set.copy()
    集合推导式：{x**2 for x in range(5)}
"""
# 创建集合
my_set = {1, 2, 3}
my_set2 = {4, 5, 6}
# 添加元素
my_set.add(9)
print(my_set)
# 删除元素
my_set.remove(1)
print(my_set)
# 检查成员
a = 3 in my_set
print(a)
# 集合运算
# 并集
new_set = my_set.union(my_set2)
print(new_set)
# 交集
new_set2 = my_set.intersection(my_set2)
print(new_set2)
# 差集
new_set3 = my_set.difference(my_set2)
print(new_set3)
# 获取集合长度
long = len(my_set2)
print(long)
# 遍历集合
for i in my_set:
    print(i)
# 清空集合
my_set.clear()
print(my_set)
# 复制集合
jj = my_set.copy()
print(jj)
#集合推导式
ll = {i**2 for i in range(5)}
print(ll)