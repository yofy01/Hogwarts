# -*- coding:utf-8 -*-
from appium_xueqiu.page.app import App

class TestBase:
	app = None
	def setup_class(self):
		'''在类中，app只启动一次'''
		self.app = App()
		self.start = self.app.start()

	def teardown_class(self):
		self.app.stop()

	def setup(self):
		print('开始执行用例.....')

	def tear_down(self):
		pass

