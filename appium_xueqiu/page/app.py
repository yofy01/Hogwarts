# -*- coding:utf-8 -*-
import yaml
from appium import webdriver
from appium_xueqiu.page.Main import Main
from appium_xueqiu.page.base_page import BasePage


class App(BasePage):
	_package = 'com.xueqiu.android'
	_activity = '.view.WelcomeActivityAlias'

	def start(self):
		'''初始化deriver'''
		if self._driver == None:
			# desired_caps = {}  # 这样定义,会被认为跟赋值同一行，导致 desired_caps 为空，可以在后边加上一个pass
			# pass
			desired_caps = dict()
			desired_caps["platformName"] = "Android"
			desired_caps["deviceName"] = "127.0.0.1:7555"
			desired_caps["appPackage"] = self._package
			desired_caps["appActivity"] = self._activity
			desired_caps["noReset"] = True
			desired_caps["skipDeviceInitialization"] = True
			desired_caps["skipServerInstallation"] = True
			desired_caps["unicodeKeyBoard"] = "true"
			desired_caps["resetKeyBoard"] = "true"
			desired_caps['newCommandTimeout'] = 300

			self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
		else:
			self._driver.launch_app()
			# self._driver.start_activity(self._package, self._activity)
		self._driver.implicitly_wait(10)
		return self

	def restart(self):
		'''重启app'''
		self._driver.quit()
		self._driver.launch_app()

	def stop(self):
		'''关闭app'''
		self._driver.quit()

	def get_driver(self):
		'''获取驱动'''
		return self._driver

	def main(self) -> Main:
		'''进入首页'''
		return Main(self._driver)