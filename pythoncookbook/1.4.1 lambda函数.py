"""我们常常看到一个这样的表达式
A=lambda x:x+1
可能会一头雾水不知道怎么计算 最基本的理解就是
def A(x):
return x+1
但是理解程序不会将一个表达式在转为函数的，因为lambda函数设计出来就是
简化def的。
其实很简单 我们可以这样分析通过冒号就能知道这句话什么意思
冒号左边→想要传递的参数
冒号右边→想要得到的数（可能带表达式）
这样在遇到lambda函数就可以一目了然的明白这个式子是干嘛的了"""

# lambda 函数很简洁
g = lambda x: x + 1
print(g(3))
