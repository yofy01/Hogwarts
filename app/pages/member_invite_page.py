# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from pages.base_page import BasePage
from pages.contact_add_page import ContactAdd


class MemberInvite(BasePage):

	def addmember_by_manul(self):
		'''手动添加'''
		self.driver.find_element(MobileBy.XPATH, '获取手动添加元素')
		return ContactAdd(self.driver)

	def get_toast(self):
		'''添加成员成功后，弹出【添加成功】toast
			也可以通过别的方式验证是否添加成功....
		'''
		self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成功"]')
		return "toast"