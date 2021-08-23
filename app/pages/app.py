# -*- coding:utf-8 -*-
'''针对app的操作'''
from appium import webdriver
from app.pages.main import Main
from pages.base_page import BasePage


class App(BasePage):
	def start(self):
		'''capability'''
		'''继承父类的driver，并重写,self.driver 实例变量，同类中别的方法可用'''
		if self.driver == None:
			desired_caps ={
				"platformName": "Android",
				"deviceName": "127.0.0.1:7555",
				"appPackage": "企业微信appPackage",
				"appActivity": ".企业微信appActivity",
				"noReset": True,
				"skipDeviceInitialization": True,
				"skipServerInstallation": True,
				"unicodeKeyBoard": "true",
				"resetKeyBoard": "true"
			}
			self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
			self.driver.implicitly_wait(10)
		else:
			self.driver.launch_app() # appium提供的起到App的方法
			# self.driver.start_activity(app_package='企业微信appPackage', app_activity='企业微信appActivity') # 起到对应的activity


	def restart(self):
		pass

	def stop(self):
		pass

	def main(self) -> Main:
		'''跳转到首页：self.driver 实例变量，同类中别的方法可用'''
		return Main(self.driver)