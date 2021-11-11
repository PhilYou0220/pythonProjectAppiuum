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
# 账号定位先清除在发送id--(resource--id)
driver.find_element_by_id("cn.shomes.tfblue:id/phoneEt").clear().send_keys("13608031945")
# 密码定位先清除在发送
driver.find_element_by_id("cn.shomes.tfblue:id/pwdEt").clear().send_keys("1")
# 点击登录
driver.find_element_by_id("cn.shomes.tfblue:id/submitBtn").click()
time.sleep(2)
# 定位到全域管控，卧槽这个不是只能定位H5吗？范力升说是原生
driver.find_element_by_name("全域管控").click()
time.sleep(10)
# 点击所有项目按钮
# driver.find_element_by_class_name("android.widget.LinearLayout").click()
driver.find_element_by_android_uiautomator('new UiSelector().text("河道清淤项目(全部)")').click()
# driver.find_element_by_name("河道清淤项目(全部)").click()
time.sleep(3)
# 点击二标段
driver.find_element_by_name("都江堰白沙河二标项目").click()
# 点击确定进入二标
driver.find_element_by_name("确定").click()
time.sleep(5)
# 点击已完成进入已完成联单
driver.find_element_by_name("已完成").click()
time.sleep(10)
# 返回上一级页面全域管控页面
# driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.Button")').click()

driver.find_element_by_class_name("android.widget.Button").click()

# 由于定位返回按钮不到，所以获取了所有的和返回按钮属性一样的class_name取第一个行了（我估计只有一个）
# i = 0
# for first_back in all_back:
#     if i == 0:
#         first_back.find_element_by_android_uiautomator('new UiSelector().className("android.widget.Button")').click()
#         i = i+1
#     else:
#         break

time.sleep(5)
# 返回上一级页面到首页
driver.find_element_by_id("cn.shomes.tfblue:id/backIconFT").click()
# all_back1 = driver.find_elements_by_class_name("android.widget.Button")
# for first_back1 in all_back1:
#     first_back1.find_element_by_class_name("android.widget.Button").click()
time.sleep(5)
# 转到我的 图上的content-desc这个字段
driver.find_element_by_accessibility_id("我").click()
time.sleep(5)
driver.find_element_by_id("cn.shomes.tfblue:id/rightFTIcon").click()
time.sleep(1)
driver.find_element_by_id("cn.shomes.tfblue:id/tvLogout").click()
print("流程结束")
driver.quit()









