import requests
import json
import time
import datetime
import hashlib
import sys
import socket# 客户端 发送一个数据，再接收一个数据
import urllib.request
from urllib.parse import quote
import string
# import config.Log

# logHttp = config.Log.logger
class RunMain():
    #定义登录POST请求
    def login_send_post(self, telephone, password):
        # 参数必须按照url、data顺序传入
        t = int(time.time())
        password = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
        url = "https://ticketapitest.shomes.cn/-/user/login"
        #url2 = "http://106.75.154.221:8345/-/user/login"
        data = 'username=' + telephone + '&password=' + password + '&timestamp=' + str(t)
        # data = {
        #     "username": telephone,
        #     "password": password,
        #     "timestamp": str(t)
        # }
        result = requests.post(url=url, data=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        # print(res)
        value = json.loads(res)
        key = value['key']
        userID = value['id']
        # print(key, userID)
        return key, userID
    #定义根据传参决定采用什么请求方式
    def run_main(self, method, url=None, data=None):  # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        if method == 'post':
            result = self.send_post(url, data)
        elif method == 'get':
            result = self.send_get(url, data)
        else:
            print("method值错误！！！")
        return result
    #定义带鉴权的请求方式
    def send_test_post(self, url, data, telephone, password):
        # 打印日志
        # logHttp.info(url, data, telephone, password)
        #print(url, data, telephone, password)
        #data = json.dumps(data)
        # 获取签证与用户ID
        telephone = str(telephone)
        password = str(password)
        key, userID = self.login_send_post(telephone, password)
        #print(key, userID)
        # 参数必须按照url、data顺序传入
        times = int(time.time())
        text = str(key) + str(times) + "city_web" + str(userID)
        headers = {
            "Shomes-Time" : str(times),
            "Shomes-Type" : "city_web",
            "Shomes-User" : str(userID),
            "Shomes-Sign" : hashlib.md5(text.encode(encoding='UTF-8')).hexdigest()
        }
        try:
            result = requests.post(url=url, headers=headers, json=data).json()
            res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
            #print("返回参数：", res)
            return res
        except:
            res = json.dumps({"code":500,"msg":"接口并未返回期望参数，或发生服务器内部错误！请单独执行此模块确认是否问题！"}, ensure_ascii=False, sort_keys=True, indent=2)
            #print("返回参数：", res)
            return res
def dict_dis(dictA, dictB):
    print("ok")

if __name__ == '__main__':
    print("======start test======")
    url = "https://ticketapi.shomes.cn/tao/alarm-dog/data"
    data = {"order":[],"limit":100000,"page":1,"keyType":"carNum","timess":["2021-04-12T16:00:00.000Z","2021-04-13T15:59:59.999Z"],"status":1,"alarmType":1,"keyword":""}
    ss = RunMain().send_test_post(url, data, '18328035519', '1')
    ss = json.loads(ss)
    #print(type(ss))
    id_list= []
    for i in ss["data"]:
        # print(i["id"])
        id_list.append(i["id"])
    #print(id_list)
    url_Cardetail = "https://ticketapi.shomes.cn/tao/alarm-dog/detail"
    url_deal = "https://ticketapi.shomes.cn/tao/alarm-dog/deal"
    file_url = "https://file.shomes.cn/minio/"
    data = id_list
    with open('overCar.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
        differ = set(data) ^ set(json_data)  
        over_id = list(differ)    
    for i in over_id:
        alarm_data = {"id":i}
        alarm_detail = RunMain().send_test_post(url_Cardetail, alarm_data, '18328035519', '1')
        alarm_detail = json.loads(alarm_detail)
        inoutPhoto = alarm_detail["inoutPhoto"].split(",")
        pic_url = file_url + inoutPhoto[0]
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #声明socket类型，同时生成链接对象
        #client.connect(('192.168.103.88',8890)) #建立一个链接，连接到本地的6969端口
        msg = pic_url #strip默认取出字符串的头尾空格
        # try:
        client.connect(('223.85.203.92',8890))
        client.send(msg.encode('utf-8'))  #发送一条信息 python3 只接收btye流
        data = client.recv(1024).decode('utf-8') #接收一个信息，并指定接收的大小 为1024字节
        client.close()
        if data == "":
            continue
        else:
            data = json.loads(data)
            print(data["class"])
            if data["class"] != "渣土车":
                deal_data = {"id":i,"status":2}
                # alarm_deal = RunMain().send_test_post(url_deal, deal_data, '18328035519', '1')
                # alarm_deal = json.loads(alarm_deal)
                print("非渣土车，已经忽略告警！")
            else:
                print("识别到渣土车，不进行操作！")
                json_data.append(i)
                with open('overCar.json', 'w', encoding='utf8')as fp:
                    json.dump(json_data, fp)



