# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

class Base:
	_driver = None
	_base_url = ''

	def __init__(self, driver: WebDriver = None):
		# 实现 driver的复用
		# 冒号 : ,给driver 贴个标签，说明这个driver是一个WebDriver
		# 可以调用WebDriver的方法，调用时点号.后有下拉提示
		# 如果去掉这个:标签，调用时不会有下拉提示，它不是必须的，但能提高工作效率
		if driver is None:
			options = Options()
			options.debugger_address = '127.0.0.1:8888'  # 实现浏览器的复用
			self._driver = webdriver.Chrome(options=options)
			self._driver.maximize_window() # 放大浏览器
			self._driver.implicitly_wait(5) # 隐式等待5秒
		else:
			self._driver = driver

		if self._base_url != '':
			self._driver.get(self._base_url)



