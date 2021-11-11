import time
import hashlib
import json
import requests


url = "https://ticketapi.shomes.cn/tao/alarm-dog/data"
# 请求非法外运待处理的数据
data = {"order":[], "limit":10, "page":1, "keyType":"carNum", "timess":["2021-04-14T16:00:00.000Z","2021-04-15T15:59:59.999Z"],"alarmType":4, "status":1}
header= {"shomes-user":"35419"}
# .json()方法可以转化为字典
response = requests.post(url=url, headers=header, json=data).json()
print(type(response))
print(response)
my_data = response['data']
print(my_data)
id_list = []
for i in my_data:
    # 得到非法外运待处理的数据id
    id_list.append(i['id'])


for j in id_list:
    url2 = "https://ticketapi.shomes.cn/tao/alarm-dog/deal"
    data2 ={"id": j, "status": 2}
    response2 = requests.post(url=url2, headers=header, json=data2)
