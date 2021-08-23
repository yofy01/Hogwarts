# -*- coding:utf-8 -*-
from appium_xueqiu.page.base_page import BasePage

class Search(BasePage):
	def search(self, stock_name, stock_code):
		'''搜索股票'''
		# send_keys:alibaba
		# click
		self.set_implicitly(15)
		self._params['stock_code'] = stock_code
		self._params['stock_name'] = stock_name

		self.steps('../page/search.yaml')

	def add_choose(self, stock_code):
		'''添加自选'''
		self._params['stock_code'] = stock_code
		self.steps('../page/search.yaml')

	def is_choose(self, stock_code):
		'''验证已添加自选'''
		self._params['stock_code'] = stock_code
		self.steps('../page/search.yaml')


	def reset_choose(self, stock_code):
		'''重置【已添加】恢复到【加自选】'''
		self._params['stock_code'] = stock_code
		self.steps('../page/search.yaml')


	def cancel(self):
		'''点击【取消】按钮'''
		self.steps('../page/search.yaml')






