# -*- coding:utf-8 -*-
from selenium_wework_login.index import Index

class TestRegister:
	def setup(self):
		self.index = Index()

	def test_register(self):
		# self.index.goto_register().register() # 从首页进入
		self.index.goto_login().goto_register().register()  # 从登录页面进入
