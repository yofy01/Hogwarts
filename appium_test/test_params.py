from time import sleep
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that,close_to
from appium_test.base_appium import BaseAppium


class TestParams(BaseAppium):

	@pytest.mark.parametrize("stock_name, stock_code, stock_price",
							 [('alibaba', 'BABA', 180), ('xiaomi', '01810', 25)])
	# @pytest.mark.skip
	def test_params(self,stock_name, stock_code, stock_price):
		'''测试s搜索功能：参数胡实例
		1、打开雪球应用
		2、点击 搜索框
		3、输入搜索值 alibaba or xiaomi
		4、点击第一个搜索结果
		5、判断 股票价格
		:return:
		'''
		driver = self.get_driver()
		self.get_element(driver, MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/tv_banner"]').click()
		self.get_element(driver, MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]').send_keys(stock_name)
		self.get_element(driver, MobileBy.XPATH, f'//*[@text="{stock_code}"]').click()
		location = f'//*[@text="{stock_code}"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]'
		self.explicit_wait(driver, MobileBy.XPATH, location)
		current_price = float(self.get_element(driver, MobileBy.XPATH, location).text)
		expected_price = stock_price
		assert_that(current_price, close_to(expected_price, expected_price*0.1))
		sleep(2)
		driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/action_close').click()


if __name__ == '__main__':
	pytest.main()

