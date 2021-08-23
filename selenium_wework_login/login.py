# -*- coding:utf-8 -*-
from selenium_wework_login.register import Register
from selenium.webdriver.common.by import By
from selenium_wework_login.base import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Login(Base):
	def scanf(self):
		pass

	def goto_register(self):
		# click register
		locator = (By.CSS_SELECTOR, '.login_registerBar_link')
		WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator))
		self._driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
		return Register(self._driver)
