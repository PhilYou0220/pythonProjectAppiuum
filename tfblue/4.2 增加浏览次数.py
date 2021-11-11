"""
@Author:PhilYou
@Data:2020 07 07 23:10
"""
from selenium import webdriver
from time import sleep
import threading
import random
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('--headless')
my_browser1 = webdriver.Firefox(options=options)
my_browser2 = webdriver.Firefox(options=options)
my_browser3 = webdriver.Firefox(options=options)


def refresh1():
    url = 'https://www.tfblue.cn/duice.html?fromColId=115'
    my_browser1.get(url)
    my_browser1.maximize_window()
    my_browser1.implicitly_wait(10)
    # sleep(1)

    # all_handles = my_browser.window_handles
    # url = 'http://news.xhu.edu.cn/zhxw/list.htm'
    # my_browser.get(url)
    # my_browser.maximize_window()
    # my_browser.implicitly_wait(10)
    # sleep(1)
    # my_browser.find_element_by_link_text('我校师生赴巴塘县开展国家通用语言文字扶贫调研工作').click()
    # sleep(1)
    # all_handles = my_browser.window_handles

    # current_handle = my_browser.current_window_handle

    # all_handles = my_browser1.window_handles
    # my_browser1.switch_to.window(all_handles[1])

    # for handle in all_handles:
    #     if current_handle != handle:
    #         my_browser.switch_to.window(handle)
    # my_browser1 = webdriver.Firefox()
    count = 1
    # a = random.randint(3, 6)
    while count <= 1000:
        my_browser1.refresh()
        sleep(1.5)
        print('线程一', count)
        count = count + 1
    my_browser1.close()


def refresh2():
    url = 'https://www.tfblue.cn/'
    my_browser2.get(url)
    number = 0
    # a = random.randint(4, 8)
    while number <= 1000:
        my_browser2.refresh()
        sleep(1)
        print('线程二', number)
        number = number + 1
    my_browser2.quit()


def refresh3():
    url = 'https://www.tfblue.cn/jianzhulajichuzhi.html?fromColId=2'
    my_browser3.get(url)
    number = 0
    # a = random.randint(4, 8)
    while number <= 1000:
        my_browser3.refresh()
        sleep(1.2)
        print('线程三', number)
        number = number + 1
    my_browser3.quit()


threads = []
t1 = threading.Thread(target=refresh1)
threads.append(t1)
t2 = threading.Thread(target=refresh2)
threads.append(t2)
t3 = threading.Thread(target=refresh3)
threads.append(t3)

for t in threads:
    # 线程启动
    t.start()
for t in threads:
    # 线程加入
    t.join()













