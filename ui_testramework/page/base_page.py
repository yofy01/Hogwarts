# -*- coding:utf-8 -*-
import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from ui_testramework.page.wrapper import handle_alert


class BasePage:

	_driver:WebDriver

	def __init__(self, driver:WebDriver = None):
		self._driver = driver

	@handle_alert
	def find(self, locator, value:str = None):
		if isinstance(locator, tuple):
			element = self._driver.find_element(*locator)
		else:
			element = self._driver.find_element(locator, value)
		return element


	def steps(self, path):
		'''解析yaml'''
		with open(path) as f:
			steps = yaml.safe_load(f)

			for step in steps:
				if "by" in step.keys():
					element = self.find(step['by'], step['locator'])
				if "action" in step.keys():
					action = step['action']
					'''1、点击操作'''
					if action == 'click':
						if element:
							element.click()
						else:
							print('定位元素失败')