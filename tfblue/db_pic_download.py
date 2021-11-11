import pymysql
import requests


def db(sql):
    conn = pymysql.connect(host="221.237.182.170", port=3326, user='epuser', password='epuser@123-TFblue',
                           database='ep')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql)
    result = cursor.fetchall()  # [{},{}]
    cursor.close()
    conn.close()
    return result


def car_inout_sql():
    start_time = "2021-11-09 00:00:00"
    end_time = "2021-11-09 23:59:59"
    sql = "SELECT pic,pic_path FROM car_inout_data WHERE create_time BETWEEN  '%s'  AND '%s'  AND door_id=1946 AND deleted=0" % (
        start_time, end_time)
    return sql


if __name__ == '__main__':
    my_sql = car_inout_sql()
    my_result = db(my_sql)  # [{'pic': None, 'pic_path': 'file/6/2021/1109/92c407a7-75f1-42c9-9d31-676f807b6ae2.jpg'}]
    my_header = "https://file.shomes.cn/minio/"
    path = "./picture1/"
    for i in my_result:
        for j in i.values():
            if j is not None:
                r = requests.get(my_header + j)
                with open(path + j[-10:], 'wb') as f:
                    f.write(r.content)
