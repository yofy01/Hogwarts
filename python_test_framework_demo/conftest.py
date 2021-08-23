# -*- coding:utf-8 -*-
import pytest
# 1、pytest中的 @pytest.fixtues()
# 1.定义登录函数，在登录函数前加上 @pytest.fixture()
@pytest.fixture()
def login():
    print('这是conftest.py中的login：---用户登录---')

def pytest_configure(config):
    marker_list = ['search', 'list'] # 标签名集合
    for markers in marker_list:
        config.addinivalue_line(
            'markers', markers
        )