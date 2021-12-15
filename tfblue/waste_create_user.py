import pymysql


def db(sql):
    conn = pymysql.connect(host="221.237.108.38", port=3356, user='epuser', password='epuser@123-New',
                           database='waste')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql)
    conn.commit()
    result = cursor.fetchall()  # [{},{}]
    # conn.commit()
    cursor.close()
    conn.close()
    return result


if __name__ == '__main__':
    for i in range(0, 201):
        name = "flmtest0" + str(i)
        sql1 = f"""
        INSERT INTO `user` (`id`, `username`, `password`, `group_id`, `name`, `card_number`, `sex`, `birthday`, `address`, `phone`, `avatar`, `deleted_at`, `disabled`, `remark`, `created_at`, `branch_account`, `app_uuid`, `password_at`, `login_error_count`, `login_error_at`) VALUES (null, "{name}", '5b89073ac4d157f8bfcc2f57f95e7248', '2', '市级管理员', '', '0', '0', '', '', '', '0', '0', '', '0', '0', '', '1637206580', '0', '1639389206');
        """
        a = db(sql1)
        sql2 = f"""select id from user where username="{name}" """
        b = db(sql2)
        for j in b:
            c = int(j["id"])
            sql3 = f"""INSERT INTO `area_user` (`id`, `user_id`, `area_code`, `deleted_at`) VALUES (null, {c}, '510100', '0');
        """
            d = db(sql3)
