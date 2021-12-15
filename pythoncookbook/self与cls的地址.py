class A(object):
    def sky(self):
        print(id(self))  # 2839707071368

    @classmethod
    def person(cls):
        return print(id(cls))  # 2839705905128


a = A()
print(id(a))  # 2839707071368
a.sky()
a.person()
print(id(A))  # 2839705905128

# 由此可见 sef 与实例化对象 a 内存地址相同
# cls与 类A 的地址相同l
