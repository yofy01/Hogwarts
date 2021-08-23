# -*- coding:utf-8 -*-
'''首页PO'''
from appium.webdriver.common.mobileby import MobileBy
from app.pages.addresslist_page import AddressList
from pages.base_page import BasePage


class Main(BasePage):
	'''本次实战用到的是通讯录'''
	def goto_message(self):
		pass

	def goto_addresslist(self):
		'''进入通讯录页面'''
		# 获取通讯录元素并点击
		self.driver.find_element(MobileBy.XPATH, '通讯录元素定位')
		return AddressList(self.driver)

	def goto_workbench(self):
		pass

	def goto_profile(self):
		pass