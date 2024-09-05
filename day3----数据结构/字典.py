"""
    创建字典：my_dict = {'name': 'Alice', 'age': 25}
    访问值：my_dict['name']（访问 'Alice'）
    修改值：my_dict['age'] = 26
    添加键值对：my_dict['city'] = 'New York'
    删除键值对：del my_dict['age']
    检查键是否存在：'name' in my_dict
    获取所有键：my_dict.keys()
    获取所有值：my_dict.values()
    获取所有键值对：my_dict.items()
    使用默认值获取值：my_dict.get('age', 'Unknown')
    清空字典：my_dict.clear()
    复制字典：new_dict = my_dict.copy()
    合并字典：dict1.update(dict2)
    遍历字典：for key, value in my_dict.items(): print(f'{key}: {value}')
    字典推导式：{x: x**2 for x in range(5)}
"""
#创建字典
mydict = {'name':"小明",'age':18}
#访问值
name = mydict['name']
print(name)
#添加元素（键值对）
mydict['city'] = '广东'
print(mydict)
#删除键值对
del mydict['age']
print(mydict)
#检查键值对
b = 'name' in mydict
print(b)
#获取所有的键
keys = mydict.keys()
#获取所有的值
values = mydict.values()
#获取所有的键值对
c = mydict.items()
print(c)
#使用默认获取值
d = mydict.get('age','none')
#清空字典
mydict.clear()
print(mydict)
#复制字典
#字典推导式
new_dict = {x:x**2 for x in range(5)}
mydict = new_dict.copy()
print(mydict)
#合并字典
mydict.update(new_dict)
print(mydict)
#遍历字典
for i,j in mydict.items():
    print({i,j})