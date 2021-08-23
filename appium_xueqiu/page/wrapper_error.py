# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By


def handle_black(func):
	def wrapper(*args, **kwargs):
		from appium_xueqiu.page.base_page import BasePage
		_black_list = [
			# 弹窗黑名单,有别的可以继续补充
			(By.XPATH, "//*[@text=’确认‘]"),
			(By.XPATH, "//*[@text=’下次再说‘]"),
			(By.XPATH, "//*[@text=’确定‘]")
		]
		_max_num = 3
		_error_num = 0

		instance:BasePage = args[0] # 把第一参数传给instance，第一个参数是 self

		try:
			element = func(*args, **kwargs)
			# 隐式等待回复原来的等待，
			instance._driver.implicitly_wait(10)
			return element

		except Exception as e:
			'''处理弹窗,判断弹窗是否属于黑名单里的元素，是的话，
			把弹窗点掉，继续查找想要的元素;如果一直找不到元素，迭代三次后结束'''
			# 灵活的设置隐式等待时间，在本次异常查找时，隐式等待时长为1秒
			instance._driver.implicitly_wait(1)
			for i in range(_max_num):
				'''判断异常处理次数'''
				if _error_num > _max_num:
					raise e
				_error_num = + 1
				'''处理黑名单里面的弹框'''
				for black in _black_list:
					'''判断弹窗是否在黑名单中，是的话，就点掉'''
					# elelist = instance.finds(*black)
					elelist = instance._driver.find_elements(*black)
					print(elelist)
					if len(elelist) > 0:
						'''默认当前只弹出一个弹窗'''
						elelist[0].click()
						'''关闭弹窗后，继续找原来的元素。递归'''
						return wrapper(*args, **kwargs)
			raise e

	return wrapper