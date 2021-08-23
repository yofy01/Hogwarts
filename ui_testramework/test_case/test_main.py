# -*- coding:utf-8 -*-
import pytest
import yaml

from ui_testramework.test_case.test_base import TestBase


class TestMain(TestBase):
	@pytest.mark.parametrize("value1, value2", yaml.safe_load(open('../page/test_main.yaml')))
	def test_main(self,value1, value2):
		print(value1, value2)
		self.app.start().main().goto_search()

	@pytest.mark.skip
	def test_window(self):
		self.app.start().main().goto_window()


if __name__ == '__main__':
    pytest.main()