"""       实例调用  类调用  访问实例属性   访问类属性
实例方法      1      0       1          1
类方 法      1      1       0          1
静态方法     1      1       0          0
https://blog.csdn.net/weixin_44259638/article/details/121318407
"""


class A(object):
    nation = "china"

    # 1.实例方法 实例调用
    def sky(self):
        name = "phil"
        # return print(name)
        print(id(self))

    # 2.静态方法 不需要参数 类和实例方法都可以调用
    @staticmethod
    def land():
        age = 18
        # return print(nation)

    # 3.类方法  类和实例方法都可以调用
    @classmethod
    def person(cls):
        cls.sex = "male"
        # return print(cls.nation)
        return print(id(cls))


# 实例化方法 所有方法都可以下载
# a = A()
# a.sky()  # 1
# a.land()  # 1
# a.person()  # 1

# 直接用调用静态方法、类方法
# A.sky()  # 0 报错
# A.land() # 1
# A.person() # 1

# # A()所有方法
# A().person() # 1
# A().land() # 1
# A().sky() # 1

a = A()
print(id(a))
a.sky()
a.person()
# print(a.__dict__)
