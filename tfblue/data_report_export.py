import time

from gui.DB import db1
import json
import xlwt

sql = """SELECT fr.structure as "内容" FROM`form_reply` `fr`
LEFT JOIN `form` `f` ON `f`.`id` = `fr`.`form_id`
LEFT JOIN `form_task` `ft` ON `ft`.`id` = `fr`.`task_id`
WHERE
	`fr`.`position_id` = '3'
AND `fr`.`instance_id` = '0'
AND `fr`.`status` = '2'
AND fr.start_time BETWEEN "2021-01-01 00:00:00" AND "2022-01-01 23:59:59"
AND ft.task_name LIKE "%重污染天气应急预案%"
ORDER BY
	fr.start_time """
result = db1.select(sql)
real_result = []
# print(result)
workbook = xlwt.Workbook(encoding='utf-8')
alignment = xlwt.Alignment()  # 创建对其格式的对象 Create Alignment
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER
style = xlwt.XFStyle()  # 创建样式对象 Create Style
style.alignment = alignment
face_mask = workbook.add_sheet('sheet1', style)
fields = ['出动执法人数 （人次）', '出动执法车辆 （台次）', '检查工地（个次）', '查处违规工地 （个次）', '取缔露天烧烤摊 （个次）', '出动清扫保洁 （人次）', '出动水车及其他除尘作业车辆 （台次）',
          '主街干道冲洗次数', '中小街道冲洗次数', '冲洗面积 （万平方米）', '设置运渣车检查卡点 （个）', '检查运渣车辆 （台次）', '查处违规运渣车辆（台次）', '查处露天焚烧垃圾落叶 （处次）',
          '工地处罚金额 （万元）', '运渣车共处罚金额（万元）']
n = 0
for title in fields:
    face_mask.write(0, n, title)
    n = n + 1
row_count = 1
for i in result:
    a = json.loads(i["内容"])  # 转python对象 ascii码会自动转义
    # b = json.dumps(a,ensure_ascii=False) #转json字符串
    col_count = 0
    print(a)
    for j in a:
        print(j)
        for m in j:
            print(m)
            face_mask.write(row_count, col_count, m['value'])
            col_count += 1
        col_count = 0  # 列指针重置
    row_count += 1
save_excel = (r'C:\Users\Administrator\Desktop\{}测试.xls'.format(time.strftime("%Y_%m_%d %H_%M_%S")))
workbook.save(save_excel)
