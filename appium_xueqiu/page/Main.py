# -*- coding:utf-8 -*-
from time import sleep

import yaml
from selenium.webdriver.common.by import By
from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.market import Market


class Main(BasePage):

	def goto_market(self):
		'''从首页切到行情页'''
		self.steps('../page/main.yaml')
		return Market(self._driver)
