"""类伪装成属性 实例化之后可直接访问"""


class Bmi(object):
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    # 伪装成属性 可直接修改
    @property
    def bmi(self):
        return self.weight // (self.height ** 2)

    # 修改属性值 需要传参
    @bmi.setter
    def bmi(self, values):
        self.weight = values
        return self.weight

    # 删除值
    @bmi.deleter
    def bmi(self):
        del self.weight


a = Bmi("张三", 1.73, 60)
print(a.bmi)
a.bmi = 200  # 修改参数weight
print(a.bmi)  # 重新获得结果
# del a.bmi
print(a.weight, a.bmi)
