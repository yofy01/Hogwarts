# -*- coding:utf-8 -*-
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class TestAppiumWeb:
	def setup(self):
		'''app端web的配置'''
		desired_caps = {
			"platformName": "Android",
			"deviceName": "127.0.0.1:7555",
			"platformNmae": "6.0",
			"browserName": "Browser",
			"noReset": True,
			# "chromeDriverExecutable":"D:\chromedriver.exe"
		}
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(10)

	def teardown(self):
		self.driver.quit()

	def test_search(self):
		'''访问百度网页并搜索'''
		self.driver.get('https://m.baidu.com')
		self.driver.find_element(By.ID, "index-kw").click()
		self.driver.find_element(By.ID, "index-kw").send_keys('python')
		self.driver.find_element(By.ID, 'index-bn').click()
		sleep(5)