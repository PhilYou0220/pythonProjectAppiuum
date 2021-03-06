import hashlib
import os
import tkinter
from tkinter import messagebox
import requests
from shutil import rmtree
from gui.DB import db1, db2  # 导入了两个实例化对象
from time import time


class Application(tkinter.Frame):
    # 给frame绑定到主窗口
    def __init__(self, master=None):
        # tkinter.Frame 的frame绑定主窗口
        super().__init__(master)
        self.master = master
        # 给实例化对象frame 一个布局
        self.pack()
        # 触发创建的组件
        self.create_widget()

    def create_widget(self):
        """创建组件"""
        # lable显示图片
        # self.photo = tkinter.PhotoImage(file=r"./a.ico")
        # 一个汉字占两个字符（weight）,width宽，height高，fg前景色，bg背景色，font字体
        self.test01_label = tkinter.Label(self, text="用户名", pady=25)
        # self.test01_label.pack()
        self.test01_label.grid(row=0, column=0)

        # 设置变量获取值
        self.get_username = tkinter.StringVar()
        self.username_input = tkinter.Entry(self, textvariable=self.get_username)
        # self.username_input.pack()
        self.username_input.grid(row=0, column=1)

        self.test02_label = tkinter.Label(self, text="密码",pady=10)
        # self.test02_label.pack()
        self.test02_label.grid(row=1, column=0)

        self.get_password = tkinter.StringVar()
        self.password_input = tkinter.Entry(self, textvariable=self.get_password, show="*")
        # self.password_input.pack()
        self.password_input.grid(row=1, column=1)

        self.login_btn = tkinter.Button(self, text="登录", command=self.login)
        # self.login_btn.pack()
        self.login_btn.grid(row=3, column=0, sticky="EW")
        self.login_btn = tkinter.Button(self, text="退出", command=root.destroy)  # 直接销毁主窗口
        # self.login_btn.pack()
        self.login_btn.grid(row=3, column=1)

    def his_click(self):
        return messagebox.showinfo(title="弹窗一号", message="77最棒啦。")

    def login(self):

        global user_id
        global real_name
        user_id = None  # 每次调用前先把user_id置空
        real_name = None  # 每次调用前先把user_id置空
        self.login_suc = "login_success"
        self.login_fai = "login_fail"
        self.username = self.username_input.get()
        self.pwd = self.password_input.get()

        print(self.username)
        print(self.password_input.get())
        self.password = hashlib.md5(self.password_input.get().encode(encoding='UTF-8')).hexdigest()
        print(self.password)
        if self.username == "" or self.password == "":
            tkinter.messagebox.showinfo(title="警告", message="账号或密码不能为空")
        sql = f"""SELECT	*
    FROM
    	`user` a
    WHERE
    a.username="{self.username}"
    and
    a.`password`="{self.password}"
    AND a.user_status=2
    AND a.deleted = 0"""

        self.sql_result = db1.select(sql)
        self.op_time = int(str(time()).split(".")[0])
        # print(self.sql_result)
        if self.sql_result:
            for i in self.sql_result:
                user_id = i["id"]
                real_name = i["name"]
                # print(i)
                if i["login_error"] == 5:
                    op_sql = f"INSERT INTO picture_download_log VALUES (NULL,{user_id},\"{real_name}\",\"{self.pwd}\",\"{self.login_fai}\",\"此账号密码输错五次，已被锁定\",{self.op_time})"
                    db2.insert(op_sql)
                    tkinter.messagebox.showinfo(title="警告", message="此账号密码输错五次，已被锁定")

                elif i["position_id"] != 737:
                    op_sql = f"INSERT INTO picture_download_log VALUES (NULL,{user_id},\"{real_name}\",\"{self.pwd}\",\"{self.login_fai}\",\"需使用总部坐席账号登录\",{self.op_time})"
                    db2.insert(op_sql)
                    tkinter.messagebox.showinfo(title="提醒", message="必须使用总部坐席账号登录！！！")

                else:
                    # tkinter.messagebox.showinfo(title="恭喜！！！", message="登录成功")
                    # 登录后销毁登录界面的frame
                    op_sql = f"INSERT INTO picture_download_log VALUES (NULL,{user_id},\"{real_name}\",\"{self.pwd}\",\"{self.login_suc}\",\"登录成功\",{self.op_time})"
                    db2.insert(op_sql)
                    self.destroy()
                    # 创建第二个frame并绑定到root主窗口 实例化第二个frame对象
                    second_app = WorkPage(second_master=root)
        else:
            op_sql = f"INSERT INTO picture_download_log VALUES (NULL,null,\"{self.username}\",\"{self.pwd}\",\"{self.login_fai}\",\"账号或密码错误\",{self.op_time})"
            db2.insert(op_sql)
            tkinter.messagebox.showinfo(title="警告", message="账号或密码错误！！！")


class WorkPage(tkinter.Frame):
    def __init__(self, second_master=None):
        # 创建另一个frame
        super().__init__(second_master)
        self.master = second_master
        self.pack()

        # 触发创建的组件
        self.second_create_widget()

    def second_create_widget(self):
        # self.second_get_string = tkinter.StringVar()
        # 不设置长度和高度
        self.path = r'C:\Users\Administrator\Desktop\picture1'
        self.second_notice_label = tkinter.Label(self,
                                                 text=f"此程序用于下载电子联单起点的出口照片，请在下面文本框内输入需要下载的电子联单号。",
                                                 anchor="w", justify='left')
        self.second_notice_label.pack()
        # 显示路径可以复制的text，label不可以复制
        self.second_notice2_text = tkinter.Text(self,
                                                width=50, height=2)

        self.second_notice2_text.insert("insert", f"温馨提示:下载的照片保存在{self.path}")
        # self.second_notice2_text.insert("end","!")
        self.second_notice2_text["relief"] = "solid"
        self.second_notice2_text["state"] = "disable"
        self.second_notice2_text.pack()

        self.text_input = tkinter.Text(self)
        self.text_input.pack()
        self.second01_button = tkinter.Button(self, text="提交并下载", command=self.second_commit)
        self.second01_button.pack()

    def second_commit(self):
        # 获取第一行第一列到最后的所有值
        self.content = self.text_input.get(1.0, "end")
        # 把字符串转换成了列表
        self.temp_content = self.content.strip().replace("\n", "\",\"")
        print(self.temp_content)
        # self.temp_content = self.content.strip().replace("\n", ",")
        # split字符串转列表，join列表转字符串
        # self.list_content = self.temp_content.split(",")
        # 列表里字符串转数字类型 但还不能转 存在字母
        # self.final_content = list(map(str, self.list_content))

        # tkinter.messagebox.showinfo(title="成功", message="提交成功")
        # self.second01_label = tkinter.Label(self,ti)
        self.my_picture()

    def car_inout_sql(self):
        self.sql1 = """
            SELECT url FROM ss_car_media WHERE ticket_id
                IN
                (SELECT id FROM ss_electric_ticket WHERE number IN ("%s")
    ) AND type=13
        """ % (self.temp_content)
        return self.sql1

    def my_picture(self):
        self.pic_success = "download_success"
        self.pic_fail = "download_fail"
        pwd = f"select password from picture_download_log where `user_id`={user_id} order by id desc limit 1"
        user_pwd_result = db2.select(pwd)
        for i in user_pwd_result:
            user_pwd = i["password"]

        # 下载时提交按钮置灰
        self.second01_button["state"] = "disable"
        # 下载时输入框不能输入
        self.text_input["state"] = "disable"
        self.process = tkinter.StringVar()
        self.second_process_label = tkinter.Label(self, textvariable=self.process, background="green", height=2,
                                                  width=500)
        self.second_process_label.pack()

        self.my_sql = self.car_inout_sql()
        self.my_result = db1.select(self.my_sql)  # [a,b,c]
        self.my_car_len = len(self.my_result)
        # 未找到照片时刷新页面
        if self.my_car_len == 0:
            messagebox.showinfo(title="警告！", message="输入的联单未发现任何出口照片，请重新输入联单！")
            self.second01_button["state"] = "normal"
            self.text_input["state"] = "normal"
            # 销毁进度条
            self.second_process_label.destroy()
        self.my_header = "https://file.shomes.cn/minio/"
        self.filename = r'C:\Users\Administrator\Desktop\picture1'
        # 存在先删除文件夹，再创建文件夹
        if os.path.exists(self.filename):
            # os.rmdir(self.filename) # 只能删除空文件夹
            rmtree(self.filename)  # 删除文件夹及下面的所有文件或文件夹
        if not os.path.exists(self.filename):
            os.makedirs(self.filename)
        self.count = 0
        for self.i in self.my_result:
            self.count += 1
            for self.j in self.i.values():
                if self.j is not None:
                    self.r = requests.get(self.my_header + self.j)
                    # 使用count计数，避免重复照片被覆盖掉
                    with open(self.filename + "/" + str(self.count) + self.j[-4:], 'wb') as self.f:
                        # with open(self.filename + "/" + self.j[-10:], 'wb') as self.f:
                        try:
                            self.f.write(self.r.content)
                            self.op_time = int(str(time()).split(".")[0])

                            op_sql = f"INSERT INTO picture_download_log VALUES (NULL,{user_id},\"{real_name}\",\"{user_pwd}\",\"{self.pic_success}\",\"{self.my_header + self.j}\",{self.op_time})"
                            db2.insert(op_sql)
                        except Exception as e:
                            self.op_time = int(str(time()).split(".")[0])
                            op_sql = f"INSERT INTO picture_download_log VALUES (NULL,{user_id},\"{real_name}\",\"{user_pwd}\",\"{self.pic_fail}\",\"self.my_header + self.j\",{self.op_time})"
                            db2.insert(op_sql)
                            messagebox.showinfo("异常", "下载时出现异常！")

                        self.process_values = "{}/{}".format(self.count, self.my_car_len)

                        # 更新textvarible 更新显示
                        self.process.set(self.process_values)
                        # self是frame 把它更新达到更新进度条的目的
                        self.update()

                        if self.count != self.my_car_len:
                            print("{}/{}".format(self.count, self.my_car_len))
                        elif self.count == self.my_car_len:
                            print("{}/{}".format(self.count, self.my_car_len))
                            # 下载完成提交按钮亮起
                            self.second01_button["state"] = "normal"
                            # 下载完成输入框可以输入
                            self.text_input["state"] = "normal"
                            messagebox.showinfo(title="下载完成", message=f"恭喜您下载完成！请到 {self.filename} 目录查看下载的照片。")


if __name__ == '__main__':
    # 设置一个主窗口
    root = tkinter.Tk()
    # 窗口大小
    root.geometry("500x500+500+500")
    # 主窗口名字
    root.title("test")
    # 实例化对象传入root
    app = Application(master=root)
    # second_app = WorkPage(second_master=root)
    # 事件循环
    root.mainloop()
