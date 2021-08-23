# -*- coding:utf-8 -*-
import pytest
import allure
from selenium import webdriver
import time
"""
场景：使用pytest+allure+selenium完成百度搜素
步骤：
1、声明浏览器驱动
2、启动浏览器驱动，打开百度网址
3、获取输入框控件，输入搜索关键字，点击查询控件
4、关闭浏览器
说明：
1、查询关键字需要用到参数化：@pytest.mark.parametriz()
2、测试过程中需要截图，用到driver.save_screenshot()
3、将截图添加到测试报告对应的测试用例执行结果中：@allure.attach
4、使用@allure.step()记录执行过程
"""

@allure.feature("百度搜索")
@pytest.mark.parametrize("test_data", ["allure","python","java"])
def test_baidu_search(test_data):
    with allure.step("声明浏览器驱动，这里使用firefox浏览器"):
        # driver = webdriver.Firefox(executable_path='‪D:\Python39\geckodriver.exe')
        driver = webdriver.Firefox()
    with allure.step("打开百度"):
        driver.get('https://www.baidu.com/')
    with allure.step("浏览器最大化"):
        driver.maximize_window()
    with allure.step("暂停2秒"):
        time.sleep(2)
    with allure.step(f'输入查询数据 {test_data}'):
        driver.find_element_by_id('kw').send_keys(test_data)
    with allure.step('点击搜索按钮'):
        driver.find_element_by_id('su').click()
    with allure.step("暂停2秒"):
        time.sleep(2)
    with allure.step("屏幕截图并附到测试用例执行结果中"):
        driver.save_screenshot(f'./result/15/{test_data}.png')
        allure.attach.file(f'./result/15/{test_data}.png', name='测试截图', attachment_type=allure.attachment_type.PNG)
    with allure.step('关闭浏览器'):
        driver.quit()

if __name__=='__main__':
    pytest.main()

