"""安顺火运智慧物流货运平台综合管理端 补单
需改变参数 number :运单的id
Cookie:下次重新赋值
Referer:注意文件夹重新赋值
"""
import requests
import json

number = 160589
url = "http://47.108.206.89:8010/api/repairManage/audit"
while number <= 160641:
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "42",
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": "JSESSIONID=CAFF230A378ED69F36AE3F8242432EA0",
        "Host": "47.108.206.89:8010",
        "Origin": "http://47.108.206.89:8010",
        "Referer": f"http://47.108.206.89:8010/detail/{number}/ludan/0/2201061044028911344",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

    headers1 = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "JSESSIONID=CAFF230A378ED69F36AE3F8242432EA0",
        "Host": "47.108.206.89:8010",
        "Referer": f"http://47.108.206.89:8010/detail/{number}/ludan/0/2201061044028911344",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    url1 = f"http://47.108.206.89:8010/api/repairManage/getInputDetail/{number}"
    data = {"id": number, "type": 1, "note": "", "track": 0}

    print(url1)
    r = requests.get(url=url1, headers=headers1)
    # print(number)
    # print(r.json())
    r1 = requests.post(url=url, headers=headers, json=data)
    with open("anshun_log.txt", "a") as f:
        f.write(url1)
        f.write("\n")
        f.write(str(number))
        f.write("\n")
        f.write(json.dumps(r1.json()))
        f.write("\n")
    print(number)
    print(r1.json())
    number += 1
