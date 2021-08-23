# -*- coding:utf-8 -*-
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class TestDemo:
	def setup(self):
		desired_caps = dict()
		desired_caps["platformName"] = "Android"
		desired_caps["deviceName"] = "127.0.0.1:7555"
		desired_caps["appPackage"] ='com.xueqiu.android'
		desired_caps["appActivity"] = '.view.WelcomeActivityAlias'
		desired_caps["noReset"] = True
		desired_caps["skipDeviceInitialization"] = True
		desired_caps["skipServerInstallation"] = True
		desired_caps["unicodeKeyBoard"] = "true"
		desired_caps["resetKeyBoard"] = "true"

		self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
		self._driver.implicitly_wait(10)
		
	def test_search(self):
		sleep(1)
		self._driver.find_element(By.XPATH, '//*[@resource-id="android:id/tabs"]//*[@text="行情"]').click()
		sleep(1)
		self._driver.find_element(By.XPATH, '//*[contains(@resource-id, "action_search")]').click()
		sleep(1)
		self._driver.find_element(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]').send_keys('阿里巴巴')
		sleep(1)
		self._driver.find_element(By.XPATH, '//*[@text="BABA"]').click()
		sleep(1)
		self._driver.find_element(By.XPATH, '//*[contains(@resource-id, "stock_item_container")]//*[@text="阿里巴巴"]/../..//*[@text="加自选"]').click()
		eles = self._driver.find_elements(By.XPATH, '//*[contains(@resource-id, "stock_item_container")]//*[@text="阿里巴巴"]/../..//*[@text="已添加"]')
		assert len(eles) > 0
		sleep(5)