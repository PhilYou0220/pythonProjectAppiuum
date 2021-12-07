import tkinter
from tkinter import messagebox


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
        self.test01_label = tkinter.Label(self, text="用户名")
        self.test01_label.pack()
        # 设置变量获取值
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

        # lable显示图片
        self.photo = tkinter.PhotoImage(file=r"./a.ico")
        # self.test02_label = tkinter.Label(self, image=self.photo)
        # self.test02_label.pack()

    def login(self):
        self.username = self.username_input.get()
        print(self.username)
        self.password = self.password_input.get()
        print(self.password)
        if self.username == "" or self.password == "":
            tkinter.messagebox.showinfo(title="警告", message="账号或密码不能为空")

    def his_click(self):
        return messagebox.showinfo(title="弹窗一号", message="77最棒啦。")


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
