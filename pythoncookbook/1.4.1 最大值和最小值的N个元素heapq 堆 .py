"""堆是一个二叉树，其中每个父节点的值都小于或等于其所有子节点的值。整个堆的最小元素总是位于二叉树的根节点。python的heapq模块提供了对堆的支持。
堆数据结构最重要的特征是heap[0]永远是最小的元素"""
import heapq

# case 1 可对列表、元组、字符串，列表进行排序 不可对元组进行排序  包含英文 特殊字符等 规则未知
nums = [1, 8, 2, 23, 7, -4, 43, 37.2]  # 可
# nums = (1,34,431.3,-3) 可以
# nums = "123a12323@@" 可以
# nums = {21,33,m,4} set不可以
# nums = {'age': 18, 'name': '张三', 'sex': 'male'}  根据 key的先后顺序 排列
a = heapq.nlargest(3, nums)  # nlargest()方法 如其名N个元素中最大的值中最大的前3个值
b = heapq.nsmallest(3, nums)  # nsmallest()方法，如其名N个元素中最小的前3个值
print(a)  # [43, 37.2, 23]
print(b)  # [-4, 1, 2]

# case2 更加复杂的数据结构的排序
goods = [
    {'age': 18, 'name': '张三', 'sex': 'male'},
    {'age': 15, 'name': '李四', 'sex': 'male'},
    {'age': 20, 'name': '王小二', 'sex': 'female'},
    {'age': 23, 'name': '王老五', 'sex': 'male'}
]
# 这会根据age的顺序把整个字典进行排序
young = heapq.nsmallest(3, goods,
                        key=lambda s: s['age'])  # 参数：heapq.nsmallest(x,y,key) x：最大或者最小值中的前几个； y:某种数据集合 如列表； key：
print(young)

# case3
nums = [1, 8, 2, 23, 7, -4, 43, 37.2]
# heap = str(nums) 列表也可以转字符
heapq.heapify(nums)
print(nums)

