# -*- coding:utf-8 -*-
from time import sleep
import pytest
from appium import webdriver


class TestDw:
	def setup(self):
		desire_cap = {
			"app": "",  # app apk路径，待安装测试的apk
			"platformName": "android",
			"deviceName": "127.0.0.1:7555",
			"appPackage": "com.xueqiu.android",
			"appActivity": ".view.WelcomeActivityAlias",
			"noReset": "True",  # 屏蔽弹窗
			"dontStopAppOnReset": "True",  # 能提高用例执行的效率，不需要每次都重新启动app
			"skipDeviceInitialization": "True"
		}

		self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_cap)
		self._driver.implicitly_wait(10)

	def teardown(self):
		# self._driver.back()  # 非首次执行，如果设置了 "donStopAppOnReset": "True"
		self._driver.quit()

	def test_search(self):
		print('搜索测试用例')
		'''
		1、打开 雪球 app 首页
		2、定位首页的输入框
		3、判断搜索框是否可用，并查看搜索框text属性值
		4、打印搜索框这个元素的左上角坐标和它的宽高
		5、向搜索输入框输入“alibaba”
		6、判断“阿里巴巴”是否可见
		5、如果可见，打印“搜索成功”，否则输出“搜索失败”
		'''
		element = self._driver.find_element_by_id("com.xueqiu.android:id/home_search")
		search_enabled = element.is_enabled()
		print(element.text)
		print(element.location)
		print(element.size)
		print(element.parent)
		print(element.id)
		print(element.tag_name)
		if search_enabled:
			element.click()
			self._driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('alibaba')
			alibaba_result = self._driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
			if alibaba_result.get_attribute('displayed'):
				print("搜索成功")
			else:
				print('搜索失败')
		sleep(3)


if __name__ == '__main__':
    pytest.main()