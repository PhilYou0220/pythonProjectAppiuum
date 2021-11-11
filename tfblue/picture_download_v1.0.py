"""根据索引关系下载图片"""

import xlrd
import os
import requests

my_excel = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\8.11博川物流临时堆场--嘉和世纪城(1)(1)(1).xlsx")
my_sheet = my_excel.sheet_by_index(2)
all_row = my_sheet.nrows
all_col = my_sheet.ncols
# print(all_col)

# xlrd 用的with open因此不用关闭
for i in range(0, all_col):
    if i == 0:
        # 读取第一列的所有数据，还有start_rowx end_rowx content1会作为一个列表存储数据
        content1 = my_sheet.col_values(colx=i)
    elif i == 2:
        content2 = my_sheet.col_values(colx=i)
# 集合去重车牌
unique_num = set(content1)
unique_num.discard("")
b_num = tuple(unique_num)
print(b_num)

# 获得 车牌与索引的对应关系
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
    aim_value = str(my_list2)
    my_dic[aim_key] = aim_value
    # print(my_dic)
    # 清空my_list2
    my_list2 = []
    count = count + 1

# 获得车牌与url的对应关系
my_list3 = []
my_dic2 = {}
count = 0
while count <= len(b_num) - 1:
    for x, y in enumerate(content2):
        # x = str(x)
        # print(my_dic[b_num[count]])
        # 字符串转列表 "[]" --> []
        z = eval(my_dic[b_num[count]])
        if x in z:
            my_list3.append(y)

    aim_key2 = str(b_num[count])
    aim_value2 = str(my_list3)
    my_list3 = []
    my_dic2[aim_key2] = aim_value2

    count += 1
    print(my_dic2)

# {'川AAR187': "['https://file.shomes.cn/minio/file/6/2021/0811/fa7f6275-f8d2-4c65-93e7-6a5937d754b7.jpg']"}
for i, j in my_dic2.items():
    file_path = r"C:\Users\Administrator\Desktop\新建文件夹2\{}".format(i)
    os.mkdir(file_path)
    url = eval(j)
    # print(url)
    # print(type(url))
    count = 0

    while count <= len(url) - 1:
        # print(url[count])
        if url[count] == "":
            count += 1
            continue
        # open 打开一个文件夹（目录），而不是文件
        else:
            r = requests.get(url[count])
            with open(file_path + "/" + "--" + str(count) + ".jpg", 'wb') as f:
                f.write(r.content)
            count += 1
