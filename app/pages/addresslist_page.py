# -*- coding:utf-8 -*-
'''添加成员PO'''
from appium.webdriver.common.mobileby import MobileBy
from pages.base_page import BasePage

class AddressList(BasePage):
	def add_member(self):
		from app.pages.member_invite_page import MemberInvite
		# 获取邀请成员元素，并点击
		self.driver.find_element(MobileBy.XPATH, '获取邀请成员元素')
		return MemberInvite(self.driver)