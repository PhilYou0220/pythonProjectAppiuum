import requests

"""part 1"""
# case1 基本使用
url = "https://www.baidu.com/"
response = requests.get(url)
print(response)  # <Response [200]>
# case2 查看请求得url
print(response.url)
# case3 查看状态码
print(response.status_code)
# case4 查看响应内容，文本
print(response.text)

""""part 2"""
# case1 静态参数
url1 = "https://www.baidu.com/s?wd=CD"
response2 = requests.get(url1)
# case2 paramas