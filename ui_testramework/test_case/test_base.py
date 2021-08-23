# -*- coding:utf-8 -*-
from ui_testramework.page.app import App


class TestBase:
	app = None
	def setup(self):
		self.app = App()