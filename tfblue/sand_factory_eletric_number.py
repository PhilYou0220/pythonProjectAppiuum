from tools.DB import db1
from tools.current_timestamp import current_timestamp

JM_sql = f"""SELECT number FROM ss_electric_ticket WHERE deleted=0 AND start_time BETWEEN \"2022-01-12 00:00:00\" AND "2022-01-12 23:59:59" AND acquirer_id<>0 AND end_id =182 AND number like "JM%" ORDER BY number ASC"""
FS_SQL = """SELECT number FROM ss_electric_ticket WHERE deleted=0 AND start_time BETWEEN "2022-01-12 00:00:00" AND "2022-01-12 23:59:59" AND acquirer_id<>0 AND end_id =17 AND number like "FS%" ORDER BY number ASC"""


def compare(sql):
    abnormal = []
    result = db1.select(sql)
    # print(result)
    real_number = []

    for i in result:
        # print(i["number"])
        real_number.append(i["number"][-4:])
    count = len(real_number)
    # print(real_number)
    real_number1 = list(map(int, real_number))  # str转int [1,2,3]
    for j in range(1, count + 1):
        if j not in real_number1:
            abnormal.append(j)
    return abnormal


if __name__ == '__main__':
    print(compare(JM_sql))
    print(compare(FS_SQL))
