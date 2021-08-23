# -*- coding:utf-8 -*-
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDw:
	def setup(self):
		desire_cap = {
			# "app": "",  # app apk路径，待安装测试的apk
			"platformName": "android",
			"deviceName": "127.0.0.1:7555",
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
	def test_move_by_element(self):
		action = TouchAction(self._driver)
		# 切换到热门tab
		self._driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/title_text" and @text="热门"]').click()
		ele_from = self._driver.find_element_by_id("com.xueqiu.android:id/home_search")
		ele_to = self._driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/hot_topic_tv" and @text="热门话题"]')
		print(ele_from.location)
		print(ele_to.location)
		# action.press(ele_from).wait(2000).move_to(ele_to).release().perform()
		action.press(ele_to).wait(2000).move_to(ele_from).release().perform()  # 这个才是上滑...
		sleep(3)

	def test_move(self):
		action = TouchAction(self._driver)
		print(self._driver.get_window_rect())
		window_rect = self._driver.get_window_rect()
		width = window_rect['width']
		height = window_rect['height']
		x1 = int(width * (1 / 2))
		y1 = int(height * (4 / 5))
		y2 = int(height * (1 / 5))
		action.press(x=x1, y=y2).wait(2000).move_to(x=x1, y=y1).release().perform()
		sleep(3)


if __name__ == '__main__':
    pytest.main()