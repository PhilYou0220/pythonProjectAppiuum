# a = {"a":1,"b":2}
# print(a.get("c"))
# print(bool(a.get("c")))

my_str = """1.油漆渣转移1500吨至四川纳海环境有限公司（川环危第510603060号）
2.废活性炭转移100吨至川纳海环境有限公司（川环危第510603060号）
3.油漆桶转移150吨至四川西部聚鑫化工包装有限公司（川环危 510112047号）
4.含漆废物转移5吨至川纳海环境有限公司（川环危第510603060号）
5.污泥转移50吨至川纳海环境有限公司（川环危第510603060号）"""

my_str2 = my_str.replace(" ", "")
my_str3 = my_str2.replace("\n", "")
print(my_str3)
# import datetime
# import xlwt
# a =[{'车牌号': '川AY2301', '告警时间': datetime.datetime(2021, 11, 9, 18, 6, 46), '电子联单': '202111096562'},
#     {'车牌号': '川ADD030', '告警时间': datetime.datetime(2021, 11, 9, 18, 3, 19), '电子联单': '202111096525'}]
# count = 1
# # for i in a:
# #     print(i)
# #     for j in i.values():
# #         print(j)
# #         count+=1
# #         print(count)
#
# workbook = xlwt.Workbook(encoding='utf-8')
# face_mask = workbook.add_sheet('sheet1')
#
# print(datetime.datetime(2021, 11, 9, 16, 51, 13))
