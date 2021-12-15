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
        # tkinter.Button(self)给按钮绑定到frame（实例化对象） text 文本名称 command绑定的触发事件只调用函数本身 不调用他的返回值 调用返回值会直接触发 即不加括号
        self.test_btn = tkinter.Button(self, text="请点击这里", command=self.his_click)
        # 在frame处显示此按钮
        self.test_btn.pack()
        # 销毁frame
        self.quit_btn1 = tkinter.Button(self, text="销毁frame", command=self.destroy)
        self.quit_btn1.pack()
        # 销毁主窗口 state="disable" 不生效
        self.quit_btn2 = tkinter.Button(self, text="销毁主窗口", command=root.destroy)
        self.quit_btn2.pack()

        # 一个汉字占两个字符（weight）,width宽，height高，fg前景色，bg背景色，font字体
        self.test01_label = tkinter.Label(self, text="测试标签", width=10, height=1, fg="blue", bg="white", font=("黑色", 30))
        self.test01_label.pack()

        # lable显示图片
        self.photo = tkinter.PhotoImage(file=r"./a.ico")
        self.test02_label = tkinter.Label(self, image=self.photo)
        self.test02_label.pack()

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
