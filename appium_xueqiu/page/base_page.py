# -*- coding:utf-8 -*-
import inspect
import json
import logging

import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver import Remote
from appium_xueqiu.page.wrapper import handle_alert


class BasePage:
	logging.basicConfig(level=logging.INFO)
	_driver:WebDriver
	_params = dict()
	
	def __init__(self, driver:WebDriver = None):
		self._driver = driver

	def set_implicitly(self, time):
		self._driver.implicitly_wait(time)

	def wait_element_visible(self, time, locator):
		'''等待元素出现'''
		return WebDriverWait(self._driver, time).until(expected_conditions.visibility_of_element_located(locator))

	def finds(self, locator, value:str = None):
		elements: list
		if isinstance(locator, tuple):
			elements = self._driver.find_elements(*locator)
		else:
			elements = self._driver.find_elements(locator, value)
		return elements

	# @handle_alert
	def find(self,locator, value: str = None):
		element: WebElement
		if isinstance(locator, tuple):
			element = self._driver.find_element(*locator)
		else:
			element = self._driver.find_element(locator, value)
		return element

	def steps(self, path):
		''' 解析 yaml 文件，yaml格式：
		方法：
			- 定位方式
			  定位元素
			  操作方式
		:param path: yaml 文件路径
		:param func: 待执行的函数名： func = inspect.stack()[1].function 通过过这个方式获取
		:return:
		'''
		with open(path, encoding='utf-8') as fr:
			logging.info(f'1、读取 {path} 文件')
			func = inspect.stack()[1].function # [0] -> steps, [1] -> 调用steps的方法名
			logging.info(f'正在获取方法 【{func}】 的yaml数据')
			steps = yaml.safe_load(fr)[func]
			logging.info('2、解析文件')

			# 将外部参数传入yaml文件，将 dict 转成 str, 用 str的replace方法，将 参数 替换成值，再转回dict
			# if self._params:
			steps_str = json.dumps(steps)
			for key, value in self._params.items():
				steps_str = steps_str.replace('${' + key + '}', value)
			steps = json.loads(steps_str)


			for step in steps:
				if "action" in step.keys():
					logging.info('3、多个动作解析')
					action = step['action']
					if action == 'click':
						logging.info('3.1、click 点击操作')
						self.find(step['by'], step['locator']).click()
					if action == 'send':
						logging.info('3.2、输入操作')
						if 'value' in step.keys():
							value = step['value']
							self.find(step['by'], step['locator']).send_keys(value)
						else:
							logging.info(f'文件[{path}]中定位元素[{step["locator"]}]缺少输入值 value')
					if action == 'len > 1':
						logging.info('3.3 验证操作')
						eles = self.finds(step['by'], step['locator'])
						logging.info('len(eles) > 0: ', len(eles) > 0)
						return len(eles) > 0


	'''---------------------------------------------'''
	''' 模拟键盘操作                                  '''
	'''---------------------------------------------'''
	def enter(self):
		'''回车，KEYCODE_ENTER -> 66'''
		self._driver.keyevent = 66