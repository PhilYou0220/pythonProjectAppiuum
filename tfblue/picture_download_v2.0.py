import xlrd
import os
import requests
import datetime

# import time

my_excel = xlrd.open_workbook("./20210811.xlsx")
my_sheet = my_excel.sheet_by_index(2)
all_row = my_sheet.nrows
all_col = my_sheet.ncols
# print(all_col)

# xlrd 用的with open因此不用关闭 拿到数据
for i in range(0, all_col):
    if i == 0:
        # 读取第一列的所有数据，还有start_rowx end_rowx content1会作为一个列表存储数据
        car_num = my_sheet.col_values(colx=i)
    elif i == 2:
        url = my_sheet.col_values(colx=i)
    elif i == 3:
        time = my_sheet.col_values(colx=i)
base = "./picture/"
for j in range(1, len(car_num)):
    path = base + car_num[j]
    if not os.path.exists(path):
        os.mkdir(path)
    if url[j] != "":
        r = requests.get(url[j])
        # datemode 0: 1900-based, 1: 1904-based
        my_time = datetime.datetime(*xlrd.xldate_as_tuple(time[j], 0))
        # windows不允许：号
        my_time1 = my_time.strftime("%Y-%m-%d_%H_%M_%S")
        # print(type(b))
        # my_time = datetime.utcfromtimestamp(b).strftime('%Y-%m-%d-%H-%M-%S')
        with open(path + "/" + str(j) + "-" + my_time1 + '.jpg', 'wb') as f:
            f.write(r.content)
            print("{}/{}".format(j, len(car_num)))

    else:
        print("url地址错误")
        print("{}/{}".format(j, len(car_num)))
        continue
