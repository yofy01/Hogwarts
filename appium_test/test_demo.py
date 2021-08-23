from time import sleep
import pytest
from appium import webdriver


class TestDemo:
	def setup(self):
		desired_caps = {
			"platformName": "Android",
			"deviceName": "127.0.0.1:7555",
			"appPackage": "com.xueqiu.android",
			"appActivity": ".view.WelcomeActivityAlias",
			"noReset": True,
			"skipDeviceInitialization": True,
			"unicodeKeyBoard": "true",
			"resetKeyBoard": "true"
		}
		self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
		self._driver.implicitly_wait(10)

	def teardown(self):
		# self._driver.back()  
		# self._driver.quit()
		pass



if __name__ == '__main__':
    pytest.main()

