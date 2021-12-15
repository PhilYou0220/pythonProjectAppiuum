"""针对违规告警GPS离线和重车篷布密闭出场的导出"""
import pymysql
import time
import xlwt
import datetime
import os
import xlrd


# 获取当天开始时间和结束时间
def my_time():
    a = str(time.time())
    b = a.split(".")[0]
    # 时间元组 time.struct_time(tm_year=2021, tm_mon=2, tm_mday=4, tm_hour=10, tm_min=31, tm_sec=13, tm_wday=3, tm_yday=35, tm_isdst=0)
    # localtime 需整型
    c = time.localtime(int(b))
    # 格式化的时间 类型为str
    d = time.strftime("%Y-%m-%d %H:%M:%S", c)
    e = d.split(" ")[0]  # [0]取年月日 [1]是时分秒
    f = "00:00:00"
    g = "23:59:59"
    start_time = e + " " + f
    end_time = e + " " + g
    # striptime转化为时间元组 time.struct_time(tm_year=2021, tm_mon=2, tm_mday=4, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=35, tm_isdst=-1)
    m = time.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    n = time.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    # 时间元组转换为时间戳格式为float 我们需要转成str切割 然后取[0]即小数点前面的 再转强转int
    start_snap_time = int(str(time.mktime(m)).split(".")[0])
    end_snap_time = int(str(time.mktime(n)).split(".")[0])
    return start_snap_time, end_snap_time


def write_excel(car_out__result, number, count_list, instance_name_list):
    fields = ['实例名称', '告警总次数', '车牌号码', '车辆所属区县', '所属运企', '告警地址', '告警时间', '电子联单']
    # 新建一个excel文件，使用utf-8编码
    workbook = xlwt.Workbook(encoding='utf-8')

    # 设置格式居中对齐
    alignment = xlwt.Alignment()  # 创建对其格式的对象 Create Alignment
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style = xlwt.XFStyle()  # 创建样式对象 Create Style
    style.alignment = alignment

    # 添加一个工作表名为“sheet1”
    face_mask = workbook.add_sheet('sheet1', style)
    # face_mask = workbook.add_sheet('sheet1', cell_overwrite_ok=True)

    # face_mask = write（x,y,z）x:行号；y,列号，z:数据
    # 写入表头
    i = 0
    for title in fields:
        face_mask.write(0, i, title)
        i = i + 1
    filename = r'C:\Users\Administrator\Desktop'
    if car_out__result == 0:
        if number == 1:
            save_excel = (r'C:\Users\Administrator\Desktop\{}重车篷布密闭出场.xls'.format(time.strftime("%Y_%m_%d")))
        if os.path.exists(save_excel):
            print("正在删除重车篷布密闭出场今日老excel")
            os.remove(save_excel)
            time.sleep(1)
            workbook.save(save_excel)
        else:
            workbook.save(save_excel)
        if number == 2:
            save_excel1 = (r'C:\Users\Administrator\Desktop\{}GPS离线.xls'.format(time.strftime("%Y_%m_%d")))
        if os.path.exists(save_excel1):
            print("正在删除GPS离线今日老excel")
            os.remove(save_excel1)
            time.sleep(1)
            workbook.save(save_excel1)
        else:
            workbook.save(save_excel1)
    else:
        # 行所应
        count = 1
        # 列索引
        count2 = 0
        for i in car_out__result:
            # print(i) 字典 {'车牌号': '川ADD030','电子联单': '202111096525'}
            for j in i.values():  # 字典的值
                if count2 == 0:
                    face_mask.write(count, count2, j)
                    count2 += 1

                elif count2 == 1:
                    # face_mask.write(count, count2, )
                    # 写入第三行
                    face_mask.write(count, count2 + 1, j)
                    count2 += 1
                elif count2 == 5:  # 告警时间 时间格式转字符串
                    j = str(j)
                    face_mask.write(count, count2 + 1, j)
                    count2 += 1
                else:
                    face_mask.write(count, count2 + 1, j)
                    count2 += 1
            count2 = 0
            count += 1
        # 合并单元格
        x = 1
        for v in range(0, len(count_list)):
            if v == 0:
                row = count_list[v]
            else:
                row = x - 1 + count_list[v]
            # 合并单元格face_mask.write_merge(x,y,m,n,name,style) 从x行合并到y行，从m列到n列，合并单元格的名称
            face_mask.write_merge(x, row, 0, 0, f"{instance_name_list[v]}", style)
            face_mask.write_merge(x, row, 1, 1, f"{count_list[v]}", style)
            x = row + 1

        # 判断文件夹是否存在 不存在就创
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                os.makedirs(filename)
                print("目录{}创建成功,若在桌面上未找到新生成的EXCEL文件，请到{}下寻找".format(filename, filename))
                print("目录{}创建成功,若在桌面上未找到新生成的EXCEL文件，请到{}下寻找".format(filename, filename))
                print("目录{}创建成功,若在桌面上未找到新生成的EXCEL文件，请到{}下寻找".format(filename, filename))
        if number == 1:
            save_excel = (r'C:\Users\Administrator\Desktop\{}重车篷布密闭出场.xls'.format(time.strftime("%Y_%m_%d")))
            if os.path.exists(save_excel):
                print("正在删除重车篷布密闭出场今日老excel")
                os.remove(save_excel)
                time.sleep(1)
                workbook.save(save_excel)
            else:
                workbook.save(save_excel)
        if number == 2:
            save_excel1 = (r'C:\Users\Administrator\Desktop\{}GPS离线.xls'.format(time.strftime("%Y_%m_%d")))
            if os.path.exists(save_excel1):
                print("正在删除GPS离线今日老excel")
                os.remove(save_excel1)
                time.sleep(1)
                workbook.save(save_excel1)
            else:
                workbook.save(save_excel1)


def db(sql):
    conn = pymysql.connect(host="221.237.182.170", port=3326, user='epuser', password='epuser@123-TFblue',
                           database='ep')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql)
    result = cursor.fetchall()  # [{},{}]
    cursor.close()
    conn.close()
    return result


def sql1(start_time, end_time, instance_id, department_id):
    car_out_sql = """SELECT 
        a.instance_name as "实例名称",
        a.car_num AS "车牌号",
        c.name as  "车辆所属区县",
        a.transport_name AS "所属运企",
        a.address AS "告警地址",
        FROM_UNIXTIME(a.created_at) AS "告警时间",
        b.number AS "电子联单"
    FROM
        alarm_dog a
    LEFT JOIN ss_electric_ticket b
    ON b.id = a.ticket_id
    LEFT JOIN area c on c.id=a.car_area_id
    WHERE
        a.type = 13
    AND a.area_id=11
    AND a.status in (3,4)
    AND a.deleted_at = 0
    AND a.created_at BETWEEN %d
    AND %d
    AND  a.instance_id=%d
    AND  a.department_id=%d
    AND  a.car_num like "_______"
    ORDER BY a.created_at DESC""" % (start_time, end_time, instance_id, department_id)
    return car_out_sql


def sql2(start_time, end_time, instance_id, department_id):
    gps_offline = """SELECT 
        a.instance_name AS "实例名称",
        a.car_num AS "车牌号",
        c.name as  "车辆所属区县",
        a.transport_name AS "所属运企",
        a.address AS "告警地址",
        FROM_UNIXTIME(a.created_at) AS "告警时间",
        b.number AS "电子联单"
    FROM
        alarm_dog a
    LEFT JOIN ss_electric_ticket b
    ON b.id = a.ticket_id
    LEFT JOIN area c on c.id=a.car_area_id
    WHERE
        a.type = 5
    AND a.area_id=11
    AND a.status in (3,4)
    AND a.deleted_at = 0
    AND a.created_at BETWEEN %d
    AND %d
    AND  a.instance_id=%d
    AND  a.department_id=%d
    AND  a.car_num like "_______"
    ORDER BY a.created_at DESC""" % (start_time, end_time, instance_id, department_id)
    return gps_offline


def sql3(start_time, end_time, type):
    point = """
            SELECT
	a.instance_id,
	a.department_id,
	count(id),
	FROM_UNIXTIME(MAX(created_at)),
	a.instance_name 
FROM
	alarm_dog a
WHERE
a.area_id = 11
AND a.deleted_at = 0
AND a.car_num like "_______"
AND a.created_at BETWEEN %d
AND %d
AND type =%d
GROUP BY
	instance_id,
	department_id
ORDER BY
	MAX(a.created_at) DESC;
    """ % (start_time, end_time, type)
    return point


def vehicle_close(start_time, end_time):
    my_sql3 = sql3(start_time, end_time, 13)
    # 获得点位和部门
    instance_list = []
    department_list = []
    count_list = []
    ignore = []
    instance_name_list = []
    my_result3 = db(my_sql3)

    for i in my_result3:
        count = 0
        for j in i.values():
            if count == 0:
                instance_list.append(j)
            elif count == 1:
                department_list.append(j)
            elif count == 2:
                count_list.append(j)
            elif count == 3:
                ignore.append(j)
            elif count == 4:
                instance_name_list.append(j)
            else:
                print("gps_offline_data异常")
            count += 1

    vehicle_close_data = []
    if len(instance_list) == 0:
        return vehicle_close_data, count_list, instance_name_list
    else:
        for i in range(0, len(instance_list)):
            my_sql1 = sql1(start_time, end_time, instance_list[i], department_list[i])
            sql1_result = db(my_sql1)
            for j in sql1_result:
                vehicle_close_data.append(j)
            sql1_result = []
        return vehicle_close_data, count_list, instance_name_list


def gps_offline_data(start_time, end_time):
    my_sql3 = sql3(start_time, end_time, 5)
    # 获得点位和部门
    instance_list = []
    department_list = []
    count_list = []
    ignore = []
    instance_name_list = []
    my_result3 = db(my_sql3)

    for i in my_result3:
        count = 0
        for j in i.values():
            if count == 0:
                instance_list.append(j)
            elif count == 1:
                department_list.append(j)
            elif count == 2:
                count_list.append(j)
            elif count == 3:
                ignore.append(j)
            elif count == 4:
                instance_name_list.append(j)
            else:
                print("gps_offline_data异常")
            count += 1
    gps_offline_data_data = []
    if len(instance_list) == 0:
        return gps_offline_data_data, count_list, instance_name_list
    else:
        for i in range(0, len(instance_list)):
            my_sql2 = sql2(start_time, end_time, instance_list[i], department_list[i])
            sql1_result = db(my_sql2)
            for j in sql1_result:
                gps_offline_data_data.append(j)
            sql1_result = []
        return gps_offline_data_data, count_list, instance_name_list


if __name__ == '__main__':
    start_time, end_time = my_time()
    # start_time, end_time = 1636819200, 1636905599
    vehicle_close_data, count_list, instance_name_list = vehicle_close(start_time, end_time)
    write_excel(vehicle_close_data, 1, count_list, instance_name_list)
    gps_offline_data, count_list, instance_name_list = gps_offline_data(start_time, end_time)
    write_excel(gps_offline_data, 2, count_list, instance_name_list)

