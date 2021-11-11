import requests
import json
import time
import datetime
import hashlib
# import config.Log

# logHttp = config.Log.logger


class RunMain():
    # 定义登录POST请求
    def login_send_post(self, telephone, password):
        # 参数必须按照url、data顺序传入
        t = int(time.time())
        password = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
        # url = "https://ticketapitest.shomes.cn/-/user/login"
        # 为何是8345
        url2 = "http://106.75.154.221:8345/-/user/login"
        # data = 'username=' + telephone + '&password=' + password + '&timestamp=' + str(t)
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        data = {
            "username": telephone,
            "password": password,
            "timestamp": int(t)
        }
        result = requests.post(url=url2, json=data, headers=headers).json()
        print("查看result", result)
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        print("查看res", res)
        value = json.loads(res)
        key = value['key']
        userID = value['id']
        return key, userID
    # 定义常规POST请求
    def send_post(self, url, data):
        # 参数必须按照url、data顺序传入
        result = requests.post(url=url, json=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res
    # 定义GET请求
    def send_get(self, url, data):
        result = requests.get(url=url, params=data).text
        print(result)
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res
    # 定义根据传参决定采用什么请求方式
    def run_main(self, method, url=None, data=None):  # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        if method == 'post':
            result = self.send_post(url, data)
        elif method == 'get':
            result = self.send_get(url, data)
        else:
            print("method值错误！！！")
        return result

    # 定义带鉴权的请求方式
    def send_test_post(self, url, data, telephone, password):
        # 打印日志
        # logHttp.info(url, data, telephone, password)
        print(url, data, telephone, password)
        #data = json.dumps(data)
        # 获取签证与用户ID
        telephone = str(telephone)
        password = str(password)
        key, userID = self.login_send_post(telephone, password)
        print(key, userID)
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
            # 这result的文件格式相当与F12的response
            result = requests.post(url=url, headers=headers, json=data).json()
            # sort_key = True 将数据根据keys的值进行排序。sort_keys是告诉编码器按照字典排序(a到z)输出。也可以1-9
            # 输出真正的中文需要指定ensure_ascii=False，输出中文
            # indent 缩进
            # 这res的文件格式相当与F12的preview 更适合实际情况
            res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
            print("返回参数：", res)
            return res

        except:
            res = json.dumps({"code":500,"msg":"接口并未返回期望参数，或发生服务器内部错误！请单独执行此模块确认是否问题！"}, ensure_ascii=False, sort_keys=True, indent=2)
            print("返回参数：", res)
            return res


if __name__ == '__main__':
    print("======start test======")
    # url = "http://106.75.154.221:8345/message/data"
    # data = {"page":1,"limit":100,"producerId":1}
    # ss = RunMain_waste().send_test_post(url, data, 'chanfei', '1')
    # print(ss)
