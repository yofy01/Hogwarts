# -*- coding:utf-8 -*-
import pytest
import yaml

from appium_xueqiu.testcases.test_base import TestBase


class TestSearch(TestBase):
	def setup(self):
		self.search_page = self.app.main().goto_market().goto_search()

	# @pytest.mark.parametrize("stock_name, stock_code", (("阿里巴巴", "BABA",), ("小米", "01810",)))
	@pytest.mark.parametrize("stock_name, stock_code", yaml.safe_load(open('../testcases/search_data.yaml', encoding='utf-8')))
	def test_search(self, stock_name, stock_code):
		self.search_page.search(stock_name, stock_code)

		# if self.search_page.is_choose(stock_code):
		# 	self.search_page.reset_choose(stock_name)

		self.search_page.add_choose(stock_code)
		assert self.search.is_choose(stock_code)
