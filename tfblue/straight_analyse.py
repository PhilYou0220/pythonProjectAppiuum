"""1.1 直传模式下单车定位数据量平均每天增加XX条
自2020年4月1日完成成都市渣土运输车辆定位数据直传成都市工地扬尘监控及建筑垃圾运输处置信息和监管平台（后文简称为“平台”）后，
通过与全平台处于转发接收定位数据模式状态下的数据量进行逐车对比取均值，得出结论为，单车定位数据平均每天增加XX条。"""

import pymysql

conn = pymysql.connect(host="221.237.182.170", port=3336, user='epuser', password='epuser@123-TFblue',
                       database='newgps')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 转发数据
all_car_base_sql = "SELECT plate_num FROM `vehicle_point_2021-02-01` WHERE plate_num is not null and car_status=1 GROUP BY plate_num"
print(all_car_base_sql)
cursor.execute(all_car_base_sql)
# base_car_result->所有车牌 格式->
base_car_result = cursor.fetchall()
print(base_car_result)
base_car_list = []
for i in base_car_result:
    base_car_list.append(i['plate_num'])
print(base_car_list)
# 每个车牌查询该车牌gps上传条数
all_count_plate_num = []
for j in base_car_list:
    # eval 去掉前后端引号 取出来自动去除引号
    # car_num = eval(j)
    each_car_base_sql = "SELECT count(id),plate_num FROM `vehicle_point_2021-02-01` WHERE plate_num ='%s' and car_status=1" % (
        j)
    # print(each_car_base_sql)
    cursor.execute(each_car_base_sql)
    each_car_base_result = cursor.fetchall()
    # print(each_car_base_result)
    # 转发数据总和：所有的上传数据条数和车牌 格式: [[{'count(id)': 14, 'plate_num': '川X68229'}]]
    all_count_plate_num.append(each_car_base_result)
print(all_count_plate_num)

# 直传数据
all_car_compare_sql = "SELECT plate_num FROM `vehicle_point_2021-05-01` WHERE plate_num is not null and car_status=1 GROUP BY plate_num"
print(all_car_compare_sql)
cursor.execute(all_car_compare_sql)
compare_car_result = cursor.fetchall()
# print(compare_car_result)
compare_car_list = []
for m in compare_car_result:
    compare_car_list.append(m['plate_num'])
# print(base_car_list)
# 每个车牌查询该车牌gps上传条数
all_count_plate_num1 = []
for n in compare_car_list:
    # eval 去掉前后端引号 取出来自动去除引号
    # car_num = eval(j)
    each_car_compare_sql = "SELECT count(id),plate_num FROM `vehicle_point_2021-05-01` WHERE plate_num ='%s' and car_status=1" % (
        n)
    # print(each_car_compare_sql)
    cursor.execute(each_car_compare_sql)
    each_car_compare_result = cursor.fetchall()
    # print(each_car_base_result)
    # 所有的上传数据条数和车牌 格式: [[{'count(id)': 14, 'plate_num': '川X68229'}]]
    all_count_plate_num1.append(each_car_compare_result)
print(all_count_plate_num1)
cursor.close()
conn.close()

old_car_num = []
for i in all_count_plate_num:
    # i->  [{'count(id)': 16, 'plate_num': '川X68950'}]
    for j in i:
        # j格式->{'count(id)': 14, 'plate_num': '川AZ9957'}
        old_car_num.append(j["plate_num"])
# old_car_num->['川AAA026', '川AAA061']
# print(old_car_num)


new_car_num = []
for m in all_count_plate_num1:
    for n in m:
        # n格式->{'count(id)': 14, 'plate_num': '川AZ9957'}
        new_car_num.append(n["plate_num"])
need_compare_car_num = []

sum = 0
new_count = 0
old_count = 0
data = 0
for k in old_car_num:
    # k -> 川X60312
    # print(k)

    if k in new_car_num:  # 之前的车牌需要包含在直传车牌中
        need_compare_car_num.append(k)
        for o in all_count_plate_num:
            for p in o:
                if p["plate_num"] == k:
                    old_count = p["count(id)"]
        for x in all_count_plate_num1:
            for y in x:
                if y["plate_num"] == k:
                    new_count = y["count(id)"]
        data = new_count - old_count
        print(data)
        print(sum)
        sum = sum + data  # 总和数据
    # else:
    #     print("此车牌{}不在直传的数据表中".format(k))

# print(need_compare_car_num)
all_need_compare_car = len(need_compare_car_num)  # 对比的车数做分母
print(all_need_compare_car)
result = sum / all_need_compare_car
print(result)
