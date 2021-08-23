# -*- coding:utf-8 -*-
import logging

from selenium.webdriver.common.by import By

def handle_alert(func):
	logging.basicConfig(level=logging.INFO)

	def wrapper(*args, **kwargs):  # 装饰func的
		from appium_xueqiu.page.base_page import BasePage
		_black_list = [
            (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']"),
            (By.XPATH, "//*[@text='确认']"),
            (By.XPATH, "//*[@text='下次再说']"),
            (By.XPATH, "//*[@text='确定']"),
        ]  # 弹窗黑名单

		_max_num = 0
		_error_num = 0
		instance: BasePage = args[0]  # 将 self 参数传给 instance

		try:

			logging.info("run " + func.__name__ + "\n args: \n" + repr(args[1:]) + "\n" + repr(kwargs))
			element = func(*args, **kwargs)
			# _error_num = 0   # 这个值会造成死循环
			_error_num = 0
			instance._driver.implicitly_wait(10)
			return element

		except Exception as e:

			instance._driver.implicitly_wait(1)
			# 判断异常处理次数
			if _error_num > _max_num:
				raise e
			_error_num += 1
			for ele in _black_list:
				logging.info(ele)
				'''判断弹窗是否在黑名单中，是的话，就点掉'''
				elelist = instance.finds(*ele)
				if len(elelist) > 0:
					'''默认当前只弹出一个弹窗'''
					elelist[0].click()
					'''处理弹窗后，继续找原来的元素。递归'''
					return wrapper(*args, **kwargs)
			raise e

	return wrapper