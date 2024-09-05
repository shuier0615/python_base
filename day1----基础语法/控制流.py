"""
控制流：控制流是指程序中执行语句的顺序控制方式，包括如何分支、循环和跳转。
控制流：
    条件语句：if、elif、else。
    循环语句：for、while。
    跳转语句：break（退出循环）、continue（跳过当前迭代）、return（退出函数）。
忌讳：
    过深的嵌套：使代码难以阅读和维护。
    无限循环：没有适当的终止条件。
    复杂的条件逻辑：应避免过于复杂的if-else嵌套，考虑简化逻辑或使用函数。

"""
a = 5
b = 6
if a == b:
    print(str(a) + '等于' + str(b))
elif a > b:
    print(str(a) + "大于" + str(b))
else:
    print(str(a) + '小于' + str(b))
