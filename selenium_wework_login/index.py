# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from selenium_wework_login.base import Base
from selenium_wework_login.login import Login
from selenium_wework_login.register import Register

class Index(Base):
	# 执行子类前，会先去执行父类的构造函数
	# 重写 _base_url
	_base_url = 'https://work.weixin.qq.com/'

	def goto_login(self):
		# click login
		# .index_top_operation_LoginBtn
		# 定位【企业登录】元素，然后点击
		self._driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
		return Login(self._driver)

	def goto_register(self):
		# click register
		self._driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
		return Register(self._driver)