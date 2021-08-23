# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from ui_testramework.page.base_page import BasePage


class Main(BasePage):
	def goto_search(self):
		'''搜索功能'''
		# self.find(By.ID, 'tv_search').click()
		self.steps('../page/main.yaml')

	def goto_window(self):
		self.find(By.ID, 'post_status').click()
		'''此时出现一个跳转页面，当做弹窗点掉，然后点击搜索框'''
		self.find(By.ID, 'tv_search').click()