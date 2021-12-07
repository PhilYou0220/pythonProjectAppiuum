import hashlib
import tkinter
from tkinter import messagebox
import pymysql


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
        # self.photo = tkinter.PhotoImage(file=r"./a.g")
        # 一个汉字占两个字符（weight）,width宽，height高，fg前景色，bg背景色，font字体
        self.test01_label = tkinter.Label(self, text="用户名")
        self.test01_label.pack()
        # 设置变量获取值 entry单行文本
        self.get_username = tkinter.StringVar()
        self.username_input = tkinter.Entry(self, textvariable=self.get_username)
        self.username_input.pack()

        self.test02_label = tkinter.Label(self, text="密码")
        self.test02_label.pack()

        self.get_password = tkinter.StringVar()
        self.password_input = tkinter.Entry(self, textvariable=self.get_password, show="*")
        self.password_input.pack()

        self.login_btn = tkinter.Button(self, text="登录", command=self.login)
        self.login_btn.pack()

    def db(self, sql):
        self.conn = pymysql.connect(host="221.237.182.170", port=3326, user='epuser', password='epuser@123-TFblue',
                                    database='ep')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        self.cursor.close()
        self.conn.close()
        return self.result

    def his_click(self):
        return messagebox.showinfo(title="弹窗一号", message="77最棒啦。")

    def login(self):
        self.username = self.username_input.get()
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

        self.sql_result = self.db(sql)
        # print(self.sql_result)
        if self.sql_result:
            for i in self.sql_result:
                # print(i)
                if i["login_error"] == 5:
                    tkinter.messagebox.showinfo(title="警告", message="此账号密码输错五次，已被锁定")
                elif i["position_id"] != 737:
                    tkinter.messagebox.showinfo(title="提醒", message="此角色禁止登录，必须使用总部坐席角色账号登录！！！")
                else:
                    tkinter.messagebox.showinfo(title="恭喜！！！", message="登录成功")
        else:
            tkinter.messagebox.showinfo(title="警告", message="账号或密码错误！！！")


if __name__ == '__main__':
    # 设置一个主窗口
    root = tkinter.Tk()
    # 窗口大小
    root.geometry("500x500+500+500")
    # 主窗口名字
    root.title("test")
    # 实例化对象传入root
    app = Application(master=root)
    # 事件循环
    root.mainloop()
