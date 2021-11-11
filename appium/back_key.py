"""一个例子"""
# appium使用了selenium中的的东西如元素定位之类的
from appium import webdriver
import time
# 要使用
from appium.webdriver.common.mobileby import MobileBy
# 预期参数定义一个空字典

desired_caps = {}
# 1.平台类型
desired_caps["platformName"] = "Android"
# 2.平台版本号,获取手机系统版本：adb shell getprop ro.build.version.release
desired_caps["platformVersion"] = "9"

# 3.设备名
desired_caps["deviceName"] = "XWENW19325005377"
# 4.app包名
desired_caps["appPackage"] = "cn.shomes.tfblue"

# 5.app入口activity aapt命令获取
desired_caps["appActivity"] = "cn.shomes.tfblue.ui.aTrashOld.LaunchActivity"
# 使用uiautomator2框架
# desired_caps["automationName"] = "uiautomator2"
# 回到第一次安装时的状态
desired_caps["noReset"] = True
# driver 置为空
# driver = None

print(desired_caps)
# 启动Appium，连接Appium server 处于监听状态
# 参数1：Appium的服务器 参数二：发送给服务器的参数
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 运行成功前提，1.Appium处于监听状态；2.adb devices有设备
time.sleep(5)
driver.find_element_by_accessibility_id("我").click()
time.sleep(1)
driver.find_element_by_id("cn.shomes.tfblue:id/rightFTIcon").click()
time.sleep(1)
driver.find_element_by_accessibility_id("cn.shomes.tfblue:id/tvLogout").click()