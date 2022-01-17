"""     实例对象调用 类调用 访问实例属性  访问类属性
实例方法      1      0       /         1
类方 法      1      1       /         1
静态方法     1      1       /         0
普通方法     0      1       /         0
https://blog.csdn.net/weixin_44259638/article/details/121318407
"""


class A(object):
    nation = "china"  # 类属性

    def __init__(self):  # 魔法方法 对实例化对象封装属性
        self.province = "四川"  # 实例属性

    # 1.实例方法 实例调用
    def sky(self):
        name = "phil"
        # return print(self.province)
        # print(id(self))
        print("我是实例方法返回")

    # 2.静态方法 不需要参数 类和实例方法都可以调用
    @staticmethod
    def land():
        age = 18
        # return print(nation)
        # return print(self.province)
        print("我是静态方法返回")

    # 3.类方法  类和实例方法都可以调用
    @classmethod
    def person(cls):
        cls.sex = "male"
        return print(cls.nation)
        # return print(id(cls))
        # print("我是类方法返回")

    # 4.普通方法
    def normal():
        print("我是普通方法返回")
        # print()





# 实例化方法 普通方法不能调用
# a = A()
# a.sky()  # 结果: 我是实例方法返回
# a.land()  # 结果： 我是静态方法返回
# a.person()  # 结果： 我是类方法返回
# a.normal()   # 运行报错

# 类调用 实例方法不可调用
# A.sky()  # 运行实例方法出错
# A.land()  # 结果： 我是静态方法返回
# A.person()  # 结果： 我是类方法返回
# A.normal()  # 结果： 我是普通方法返回



# A() 普通方法不能调用
# A().person() # 1
# A().land() # 1
# A().sky() # 1
# A().normal() # 0

# a = A()
# print(id(a))
# a.sky()
# a.person()
# print(a.__dict__)
