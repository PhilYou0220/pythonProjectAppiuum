import xlrd

my_excel = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\1.xls")
my_sheet = my_excel.sheet_by_index(2)
all_row = my_sheet.nrows
all_col = my_sheet.ncols
# print(all_col)

# xlrd 用的with open因此不用关闭 获得两组车牌数据
for i in range(0, all_col):
    if i == 0:
        # 读取第一列的所有数据，还有start_rowx end_rowx content1会作为一个列表存储数据
        content1 = my_sheet.col_values(colx=i)
    elif i == 1:
        content2 = my_sheet.col_values(colx=i)
# 集合去重第一组车牌

unique_num = set(content1)
# unique_num.discard("")
b_num = tuple(unique_num)
print(b_num)

# 获得 第一组车牌与数量的字典
my_list2 = []
my_dic = {}
count = 0
while count <= len(b_num) - 1:
    for m, n in enumerate(content1):
        if n == b_num[count]:
            my_list2.append(m)
    # dict的键、值必须是不可变的
    # print(my_list2)
    aim_key = str(b_num[count])
    aim_value = str(len(my_list2))
    my_dic[aim_key] = aim_value
    # print(my_dic)
    # 清空my_list2
    my_list2 = []
    count = count + 1
print(my_dic)

# 集合去重第二组车牌

unique_num2 = set(content2)
# unique_num.discard("")
c_num = tuple(unique_num2)
print(c_num)

# 获得 第二组车牌与数量的字典
my_list3 = []
my_dic2 = {}
count2 = 0
while count2 <= len(c_num) - 1:
    for m, n in enumerate(content2):
        if n == c_num[count2]:
            my_list3.append(m)
    aim_key = str(c_num[count2])
    aim_value = str(len(my_list3))
    my_dic2[aim_key] = aim_value

    my_list3 = []
    count2 = count2 + 1
print(my_dic2)

# 只有一组数据拥有的车牌及哪组数据多出
extra_one_list = []
extra_two_list = []
diff = my_dic.keys() ^ my_dic2.keys()
if len(diff)>0:
    print("只有一组数据含有的的车牌号为:{}".format(diff))
else:
    print("数据名称均存在")
for i in diff:
    if i in my_dic.keys():
        if i:
            extra_one_list.append(i)
    elif i in my_dic2.keys():
        if i:
            extra_two_list.append(i)
    else:
        print("未知错误！！！")
if len(extra_one_list) > 0:
    print("第一组比第二组多出的数据为{}".format(extra_one_list))
if len(extra_two_list) > 0:
    print("第二组比第一组多出的数据为{}".format(extra_two_list))

# 两组数据都拥有的车牌出现次数之差
my_dic3 = {}
for i, j in my_dic.items():
    # python中数据为空的对象以及None对象在条件语句都作False看待：即 None，False，0，[]，""，{}，() 都相当于False
    # if bool(my_dic2.get(i)) != False:
    if bool(my_dic2.get(i)):
        a = int(j) - int(my_dic2[i])
        if a != 0:
            my_dic3[i] = str(a)
print("两组数据都拥有的车牌出现次数之差不等于0的其余车牌(第一组为基准)", my_dic3)
