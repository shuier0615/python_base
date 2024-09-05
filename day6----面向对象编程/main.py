"""
    定义类
    创建对象
    初始化方法
    访问属性
    定义方法
    调用方法
    继承
    重写方法
    多态
    私有属性和方法
    属性装饰器
"""
# 定义基类
class Animal:
    def __init__(self, name):
        self._name = name  # 私有属性
        self.__age = 0     # 另一种私有属性表示方式

    def speak(self):
        return f"{self._name} makes a sound."

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

# 创建对象
dog = Animal("Buddy")

# 访问属性
print(dog.name)  # 输出: Buddy

# 调用方法
print(dog.speak())  # 输出: Buddy makes a sound.

# 定义子类并继承
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 调用基类的初始化方法
        self.breed = breed

    # 重写基类方法
    def speak(self):
        return f"{self.name} barks."

# 创建子类对象
my_dog = Dog("Max", "Golden Retriever")

# 调用重写的方法
print(my_dog.speak())  # 输出: Max barks.

# 多态示例
def make_animal_speak(animal):
    print(animal.speak())

make_animal_speak(dog)  # 输出: Buddy makes a sound.
make_animal_speak(my_dog)  # 输出: Max barks.


