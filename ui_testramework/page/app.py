# -*- coding:utf-8 -*-
import yaml
from appium import webdriver
from ui_testramework.page.base_page import BasePage
from ui_testramework.page.main import Main


class App(BasePage):
	_package = 'com.xueqiu.android'
	_activity = '.view.WelcomeActivityAlias'

	def start(self):
		'''初始化deriver'''
		# desired_caps = {
		# 	"platformName": "Android",
		# 	"deviceName": "127.0.0.1:7555",
		# 	"appPackage": self._package,
		# 	"appActivity": self._activity,
		# 	"noReset": True,
		# 	"skipDeviceInitialization": True,
		# 	"skipServerInstallation": True,
		# 	"unicodeKeyBoard": "true",
		# 	"resetKeyBoard": "true"
		# }
		if self._driver == None:
			# desired_caps = {}  # 这样定义,会被认为跟赋值同一行，导致 desired_caps 为空，可以在后边加上一个pass
			# pass
			desired_caps = dict()
			desired_caps["platformName"] = "Android"
			desired_caps["deviceName"] = "127.0.0.1:7555"
			desired_caps["appPackage"] = self._package
			desired_caps["appActivity"] = self._activity
			desired_caps["noReset"] = True
			desired_caps["udid"] = yaml.safe_load(open('../page/configuration.yaml'))['desired_caps']['udid']
			desired_caps["skipDeviceInitialization"] = True
			desired_caps["skipServerInstallation"] = True
			desired_caps["unicodeKeyBoard"] = "true"
			desired_caps["resetKeyBoard"] = "true"

			self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
		else:
			self._driver.start_activity(self._package, self._activity)
		self._driver.implicitly_wait(10)
		return self

	def main(self) -> Main:
		return Main(self._driver)