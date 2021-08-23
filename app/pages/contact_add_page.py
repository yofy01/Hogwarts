# -*- coding:utf-8 -*-
'''输入成员信息页面PO'''
from appium.webdriver.common.mobileby import MobileBy
from pages.base_page import BasePage


class ContactAdd(BasePage):

	def input_name(self):
		self.driver.find_element(MobileBy.XPATH, '姓名的父级下的姓名输入框').send_keys('姓名')
		return self

	def input_gender(self):
		self.driver.find_element(MobileBy.XPATH, '性别的父级下的姓别输入框').send_keys('性别')
		return self

	def input_phone(self):
		self.driver.find_element(MobileBy.XPATH, '手机号的父级下的手机号输入框').send_keys('手机号')
		return self

	def click_save(self):
		from pages.member_invite_page import MemberInvite
		return MemberInvite()
