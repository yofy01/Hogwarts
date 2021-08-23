# -*- coding:utf-8 -*-
import pytest


@pytest.fixture(autouse=True)
def open():
    print('打开浏览器')

def test_1():
    print('test_1')

def test_2():
    print('test_2')

def test_3():
    print('test_3')

if __name__=='__main__':
    pytest.main()