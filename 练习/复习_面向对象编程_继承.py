class Animal:  # 父类
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name)
        pass

class Dog(Animal):  # 子类继承父类
    def speak(self):
        print(self.name)# 重写父类方法
        return "汪汪！"

class Cat(Animal):  # 另一个子类
    def speak(self):
        return "喵喵！"
    
dog = Dog("小白")
cat = Cat("小花")
        
print(dog.speak())  # 汪汪！
print(cat.speak())  # 喵喵！
