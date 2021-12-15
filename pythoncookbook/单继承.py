"""单继承"""


class Animal(object):  # 父类，基类，超类
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print("能吃")

    def sleep(self):
        print("能睡")


class Person(Animal):  # 子类，派生类
    def __init__(self, name, age, sex, favorite):
        Animal.__init__(self, name, age, sex)  # 方式一 既执行子类的初始化方法，又执行父类的初始化方法 注意需要传一个self
        self.favorite = favorite

    def work(self):
        print("工作")


class Cat(Animal):
    def __init__(self, name, age, sex, color):
        super().__init__(name, age, sex)  # 方式二（推荐） 采用super()继承 严格按照mro方式执行
        self.color = color

    def jump(self):
        print("能跳")


my_person = Person("张三", 18, "male", "read_book")

# __dict__查看对象空间里有哪些值
print(my_person.__dict__)
my_person.work()
