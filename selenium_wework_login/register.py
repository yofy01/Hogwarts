# -*- coding:utf-8 -*-
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_wework_login.base import Base


class Register(Base):

	def register(self):
		# send content
		# click element
		locator = (By.ID,'corp_name')
		WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located(locator))
		self._driver.find_element(By.ID,'corp_name').send_keys('111111')
		self._driver.find_element(By.ID,'manager_name').send_keys('aaaa')
		self._driver.find_element(By.ID,'register_tel').send_keys('13268285931')
		self._driver.find_element(By.ID,'iagree').click()
		sleep(5)
		# self._driver.quit()
		# 老师偷懒，默认直接过了，return True
		return True