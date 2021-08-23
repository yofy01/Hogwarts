# -*- coding:utf-8 -*-
from appium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseAppium:
	_deviceName = "127.0.0.1:7555"
	_driver = None

	def set_up(self):
		'''启动appium、待测app的基础配置'''
		print('----测试开始-----')

	def tear_down(self):
		if self._driver:
			self._driver.quit()

	def get_driver(self):
		desired_caps = {
			"platformName": "Android",
			"deviceName": "127.0.0.1:7555",
			"appPackage": "com.xueqiu.android",
			"appActivity": ".view.WelcomeActivityAlias",
			"noReset": True,
			"skipDeviceInitialization": True,
			"skipServerInstallation":True,
			"unicodeKeyBoard": "true",
			"resetKeyBoard": "true"
		}
		self._driver:webdriver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
		self._driver.implicitly_wait(10)
		return self._driver


	def get_element(self,driver, locate_type, location):
		'''查找单个元素
		:param locate_type: 定位类型 by、xpath、name等
		:param location: 定位元素
		:return:
		'''
		return driver.find_element(locate_type, location)

	def get_elements(self,driver, locate_type, location):
		'''查找元素,返回多个，列表形式存储
		:param locate_type: 定位类型 by、xpath、name等
		:param location: 定位元素
		:return:
		'''
		return driver.find_elements(locate_type, location)

	def implicit_wait(self, driver, s_time):
		'''隐式等待
		:param s_time: 等待时间，单位毫秒
		:return:
		'''
		return driver.implicitly_wait(s_time)

	def explicit_wait(self, driver, locate_type, location):
		'''显式等待,可以找同个页面内单个比较复杂的元素取等待
		:param location: 定位元素，locator = (locate_type, location)
		:return:
		'''
		return WebDriverWait(driver, 30).until(
			expected_conditions.visibility_of_element_located((locate_type, location)))

	def activity_wait(self, driver, activity, s_time):
		'''等待控件出现
		:param activity: 控件名称
		:param s_time: 等待时间
		:return:
		'''
		return driver.wait_activity(activity=activity, timeout=s_time)

	def click(self):
		'''点击'''
		pass

	def send_keys(self):
		'''输入值'''
		pass