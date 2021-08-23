# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By

from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.search import Search


class Market(BasePage):
	def goto_search(self):
		'''进入搜索页'''
		# click
		self.steps('../page/search.yaml')
		return Search(self._driver)