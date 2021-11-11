"""在线车辆定身分析"""
import pymysql
from math import sin, cos, acos
import sys
import xlwt
import threading


# 深度递归设置为10000次，默认为1000次
# sys.setrecursionlimit(10000)


# 查询车牌方法
def query_1(sql):
    # 查询数据#
    con = pymysql.connect(host='221.237.182.170', port=3326, user='epuser', password='epuser@123-TFblue', database='ep')
    cur = con.cursor()  # 获取游标
    cur.execute(sql, ('2021-06-02 00:00:00', '2021-06-02 23:59:59', '2021-06-02'))  # 执行sql
    data = cur.fetchall()  # 获取查询结果
    cur.close()  # 关闭游标
    con.close()  # 关闭连接
    return data


# 根据车牌查询gps方法
def query_2(sql):
    # 查询数据#
    con = pymysql.connect(host='221.237.182.170', port=3336, user='epuser', password='epuser@123-TFblue',
                          charset='utf8', database='newgps')
    cur = con.cursor()  # 获取游标
    cur.execute(sql)  # 执行sql
    data = cur.fetchall()  # 获取查询结果
    cur.close()  # 关闭游标
    con.close()  # 关闭连接
    return data


# ”和“的计算 龟儿子再用递归计算和
def sum(x):
    head, *tail = x
    return head + sum(tail) if tail else head


def sum_1(y):
    count = 0
    sum = 0
    while count <= len(y) - 1:
        sum = sum + y[count]
        count += 1
    return sum


def my_main():
    sql_1 = "SELECT a.car_num FROM car_directory a WHERE car_num IN (SELECT DISTINCT car_num FROM car_inout_data WHERE deleted = 0 AND create_time >= %s AND create_time < %s AND car_num <> '' AND car_status IN (1, 2, 3, 4)) AND car_num IN (SELECT DISTINCT plate_num FROM vehicle_online_car WHERE summary_date = %s AND online_minute >= 1400) ORDER BY a.car_num"
    data_1 = query_1(sql_1)  # 6月2日有进出数据且在线时长大于等于1400的名录车
    # print(data_1)
    # print(type(data_1))
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet')

    p = []
    for i in data_1:
        p.append(i[0])
    m = 0
    while m <= len(p) - 1:
        sql_2 = "SELECT a.point_x,a.point_y FROM`vehicle_point_2021-06-02` AS a WHERE a.plate_num = '%s' GROUP BY a.point_x,a.point_y" % (
        p[m])
        print("查询车牌：", p[m])
        worksheet.write(m, 0, p[m])
        data = query_2(sql_2)
        a = []
        b = []
        e = []
        # 把经,纬度分别赋值给a,b
        for i in data:
            # print(i)
            a.append(i[0])
            b.append(i[1])

        for i in b:
            c = 90 - i
            e.append(c)  # e是90度-北纬
        # 经纬度长度相同 故用了经度的长度
        len1 = len(a)

        i = 0
        distance = []
        if len(a) == 1:  # 防止len(a)等于1 这种情况 如川AAA653在6月2日时的情况 所有坐标都相同 距离为0
            print(0)
            worksheet.write(m, 1, 0)
            workbook.save('车辆定身距离分析.xls')

        else:
            # 相邻两个经纬度计算距离
            while i <= len1 - 2:
                distance.append(sin(e[i]) * sin(e[i + 1]) * cos(a[i] - a[i + 1]) + cos(e[i]) * cos(e[i + 1]))
                i += 1

            n = 0
            final_distance = []  # 计算距离
            # print(len(distance))
            while n <= len(distance) - 1:
                final_distance.append(6371.004 * acos(distance[n]) / 180)
                n = n + 1
            sum_distance = sum_1(final_distance)
            print(sum_distance)
            # 写入第二列
            worksheet.write(m, 1, sum_distance)
            workbook.save('车辆定身距离分析.xls')
        m += 1
    print(m)


if __name__ == '__main__':
    my_main()
    # sys.setrecursionlimit(100000)
    # threading.stack_size(200000000)
    # thread = threading.Thread(target=my_main())
    # thread.start()
