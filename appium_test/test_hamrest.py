'''
appium的自动化
1、需要Capability来组装待测试app的基本信息（packageName/activityName/连接模拟器ip:端口/测试平台等信息）
2、进行元素定位、控件交互（点击、输入等操作）
3、断言，验证测试结果
'''

# -*- coding:utf-8 -*-
from time import sleep

import pytest
from appium import webdriver
from hamcrest import assert_that, equal_to, close_to, contains_string, less_than


class TestDw:
	def setup(self):
		desire_cap = {
			"app": "",  # app apk路径，待安装测试的apk
			"platformName": "android",
			"deviceName": "127.0.0.1:7555", # 网易mumu模拟器端口
			"appPackage": "com.xueqiu.android",
			"appActivity": ".view.WelcomeActivityAlias",
			"noReset": "True",  # 屏蔽弹窗
			# "dontStopAppOnReset": "True",  # 能提高用例执行的效率，不需要每次都重新启动app
			# "skipDeviceInitialization": "True"
		}

		self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_cap)
		self._driver.implicitly_wait(10)

	def teardown(self):
		# self._driver.back()  # 非首次执行，如果设置了 "donStopAppOnReset": "True"
		self._driver.quit()
	@pytest.mark.skip
	def test_search1(self):
		print('搜索测试用例')
		'''
		1、打开 雪球 app
		2、点击搜索输入框
		3、向搜索输入框输入“阿里巴巴”
		4、在搜索结果列点击“阿里巴巴”，然后点击
		5、获取这只 阿里巴巴的股价，并判断 这只股价的价格>200
		'''
		self._driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
		self._driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('alibaba')
		self._driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
		current_price = self._driver.find_element_by_xpath('//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
		print(current_price, type(current_price))
		# assert float(current_price)< 200
		assert_that(current_price,less_than(200), "当前股价小于200")
		sleep(3)

@pytest.mark.skip
def test_hamcrest():
    assert_that(2, equal_to(2), "期望等于2")
    assert_that(11, close_to(1, 10), "期望在1的基础上，上下10浮动")
    assert_that(-9, close_to(1, 10), "期望在1的基础上，上下10浮动")
    assert_that(5.555, close_to(1, 10), "期望在5.555的基础上，上下10浮动")
    assert_that("heihei", contains_string("h"), "字符串包含h")

if __name__ == '__main__':
    pytest.main()
