from selenium import webdriver
import time
my_driver = webdriver.Firefox()
url = "https://movie.douban.com/top250"
my_driver.get(url)
my_driver.maximize_window()
my_driver.implicitly_wait(10)
for count in range(0,10):
    all_score = my_driver.find_elements_by_class_name("item")
    time.sleep(5)
    for i in all_score:
        each_film_name = i.find_element_by_class_name("info").find_element_by_class_name("title").text
        each_score = str(i.find_element_by_class_name("info").find_element_by_class_name("star").find_element_by_class_name("rating_num").text)
        a = 9.5
        b = str(a)
        if each_score >= b:
            print(each_film_name, end="")
            print(each_score)
    my_driver.find_element_by_class_name("next").click()
    count += count
my_driver.quit()