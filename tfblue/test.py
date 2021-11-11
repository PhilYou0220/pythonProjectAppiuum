import os
import requests

a = {
    '川AAR187': "['https://file.shomes.cn/minio/file/6/2021/0811/fa7f6275-f8d2-4c65-93e7-6a5937d754b7.jpg','https://file.shomes.cn/minio/file/6/2021/0811/fa7f6275-f8d2-4c65-93e7-6a5937d754b78.jpg']",
    '川AAR188': "['https://file.shomes.cn/minio/file/6/2021/0811/fa7f6275-f8d2-4c65-93e7-6a5937d754b9.jpg','https://file.shomes.cn/minio/file/6/2021/0811/fa7f6275-f8d2-4c65-93e7-6a5937d75410.jpg']"}
# count = 0

for i, j in a.items():
    file_path = r"C:\Users\Administrator\Desktop\新建文件夹2\{}".format(i)
    os.mkdir(file_path)
    url = eval(j)
    print(url)
    print(type(url))
    count = 0

    while count <= len(url) - 1:
        print(url[count])
        r = requests.get(url[count])
        # open 打开一个文件夹（目录），而不是文件
        with open(file_path + "/" + "--" + str(count) + ".jpg", 'wb') as f:
            f.write(r.content)
        count += 1

