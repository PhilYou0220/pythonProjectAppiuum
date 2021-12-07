import tkinter
from tkinter import messagebox

# 创建主窗口对象
top = tkinter.Tk()
# 给窗口命名
top.title("我的GUI")
# geometry窗口大小设置weight x height 窗口出现位置设置  +(左)-(右)100距离 +(上)-(下)100距离
top.geometry("500x300+200+100")
# btn01 = tkinter.Button(top,text="123")
# 放在主窗口
btn01 = tkinter.Button(top)
btn01["text"] = "请点击这里"
# 布局
btn01.pack()


def my_click1(e):  # e为事件对象
    # 弹窗信息展示，title 弹窗标题，message弹窗信息
    messagebox.showinfo(title="标题", message="昨夜星辰昨夜风")


# 绑定事件
btn01.bind("<Button-1>", my_click1)
# 调用mainloop()，进入事件循环
top.mainloop()
