# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By


def handle_alert(func):
	def wrapper(*args, **kwargs):  # 装饰func的
		from ui_testramework.page.base_page import BasePage
		_black_list = [
			(By.ID, 'iv_close'),
			(By.XPATH, '//*[@text="确认"]'),
			(By.XPATH, '//*[@text="确定"]'),
		]  # 弹窗黑名单

		_error_num = 0
		_max_num = 3

		instance: BasePage = args[0]  # 将 self 参数传给 instance

		try:
			element = func(*args, **kwargs)
			# _error_num = 0   # 这个值会造成死循环
			instance._driver.implicitly_wait(10)
			return element

		except Exception as e:
			instance._driver.implicitly_wait(1)
			for i in range(_max_num):
				if _error_num > _max_num:
					raise e
				_error_num += 1

				for black in _black_list:
					'''判断弹窗是否在黑名单中，是的话，就点掉'''
					elements = instance._driver.find_elements(*black)
					if len(elements) > 0:
						'''默认当前只弹出一个弹窗'''
						elements[0].click()
						# break
						'''处理弹窗后，继续找原来的元素。递归'''
						return wrapper(*args, **kwargs)
			raise e

	return wrapper