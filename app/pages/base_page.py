# -*- coding:utf-8 -*-
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
import logging


class BasePage:
	logging.basicConfig(level=logging.INFO)
	_black_list= [
		'''弹窗黑名单,有别的可以继续补充'''
		(By.XPATH, "//*[@text=’确认‘]"),
		(By.XPATH, "//*[@text=’下次再说‘]"),
		(By.XPATH, "//*[@text=’确定‘]")
	]
	_max_num = 3
	_error_num = 0

	def __init__(self, driver:WebDriver = None):
		self.driver = driver

	def find(self, locator, value:str=None):
		logging.info(locator)
		logging.info(value)
		element:WebElement
		try:
			if isinstance(locator, tuple):
				'''判断如果传的是元组'''
				element = self.driver.find_element(*locator)
			else:
				element = self.driver.find_element(locator, value)
				# 找到元素之前，+eeor_num归0
				self._error_num = 0
				# 恢复隐式等待原来的等待
				self.driver.implicitly_wait(10)
			return element
		except Exception as e:
			'''处理弹窗,判断弹窗是否属于黑名单里的元素，是的话，
			把弹窗点掉，继续查找想要的元素;如果一直找不到元素，迭代三次后结束'''
			# 灵活的设置隐式等待时间，在本次异常查找时，隐式等待时长为1秒
			self.driver.implicitly_wait(1)
			if self._error_num > self._max_num:
				raise e
			self._error_num =+ 1

			for ele in self._black_list:
				# find_elements 找不到元素也不会报错
				elelist = self.driver.find_elements(*ele)
				if len(elelist) > 0:
					elelist[0].click()
					return self.find(locator, value)
			raise e


	def find_and_get_text(self, locator, value:str=None):
		'''这么写不优雅，应该做成装饰器'''
		element:WebElement
		try:
			if isinstance(locator, tuple):
				'''判断如果传的是元组'''
				element_text = self.driver.find_element(*locator).text
			else:
				element_text = self.driver.find_element(locator, value).text
				# 找到元素之前，+eeor_num归0
				self._error_num = 0
				# 恢复隐式等待原来的等待
				self.driver.implicitly_wait(10)
			return element
		except Exception as e:
			'''处理弹窗,判断弹窗是否属于黑名单里的元素，是的话，
			把弹窗点掉，继续查找想要的元素;如果一直找不到元素，迭代三次后结束'''
			self.driver.implicitly_wait(1)   # 灵活的设置隐式等待时间，在本次异常查找时，隐式等待时长为1秒
			if self._error_num > self._max_num:
				raise e
			self._error_num =+ 1

			for ele in self._black_list:
				elelist = self.driver.find_elements(*ele) # find_elements 找不到元素也不会保存
				if len(elelist) > 0:
					elelist[0].click()
					return self.find_and_get_test(locator, value)
			raise e