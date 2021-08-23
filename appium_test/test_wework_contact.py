# -*- coding:utf-8 -*-
'''企业微信app自动化测试'''
from appium import webdriver


class TestWeWorkContant:
	def setup(self):
		desired_caps = {
			"platformName": "Android",
			"deviceName": '127.0.0.1:7555',
			"appPackage": "com.xueqiu.android",
			"appActivity": ".view.WelcomeActivityAlias",
			"noReset": True,
			"skipDeviceInitialization": True,
			"skipServerInstallation": True,
			"unicodeKeyBoard": "true",
			"resetKeyBoard": "true"
		}
		self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
		self._driver.implicitly_wait(10)

	def teardown(self):
		self._driver.quit()

	def test_contact(self):
		'''添加联系人
		1、找到【通讯录】元素，并点击
		2、在通讯录页面找到【添加成员】元素，并点击
		3、点击【手动输入成员】元素，并点击
		4、添加成员页面，找到【姓名、性别、手机、邮箱、地址】对应的输入框元素，并输入对应的内容
			注意元素是否带前后空格
		:return:
		'''
		pass