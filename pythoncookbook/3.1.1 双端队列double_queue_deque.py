"""两端都可以进 两端也可以出出 格式deque(['b', 'a'])  """
# case1 双端队列的创建和 增加
# 先导包 collectionscollections提供了几个额外的数据类型：Counter、deque、defaultdict、namedtuple和OrderedDict等

from collections import deque

# case1 单增 把a设置为一个双端队列 不属于任意一种基本类型 它属于一种叫collections.deque的数据类型
a = deque()
# 和列表的append一样添加到列表的右边 一次只允许传一个参数
a.append("a")
# 和列表有区别从头部开始添加
a.appendleft("b")
# print(type(a))
print(a)  # deque(['b', 'a'])

# case2 多增 批量添加extend与extendleft 但是现在只发现（）和[]才可以添加到deque
# 双端队列与列表的extend一致 在末尾添加
a.extend(["a", "b", "c"])
print(a)  # deque(['b', 'a', 'a', 'b', 'c'])
# 左侧要注意：一个一个如队列 入了32 再入4 就是 4,32的顺序
a.extendleft((32, 4))
print(a)  # deque([4, 32, 'b', 'a', 'a', 'b', 'c'])

# case3 指定位置插入
a.insert(0, "yf")
print(a)

# case4  pop右侧出队 popleft 左侧出队
print(a.popleft())

# case5 deque翻转 rotate（）后x个移到最前面x个来 整体前移  reverse直接倒序
a.rotate(3)  # 最后三个移到最前面三个来
print(a)

# case6 deque的拷贝 copy()方法
b = a.copy()
print(b)

# case7 双端队列的计数和索引
print(a.count('a'))
print(a.index('a'))

# case8 deque的删除 remove() pop() clear()
# remove方法如果没找到将要报错 只移除第一个 参数列表的remove(）方法
a.remove('a')
print(a)
# 清空
# a.clear()
print(a)

# case9 maxlen最大长度 超过最大长度前面的出队 直保留最后五位
a = deque(maxlen=5)
a.extend(['a', 'b', 'c', 'd', 'e'])
print(a)