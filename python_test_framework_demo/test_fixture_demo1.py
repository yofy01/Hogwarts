# -*- coding:utf-8 -*-
import pytest

# 2、测试用例
def test_one(login):
    print('test_one 需要登录')

def test_two():
    print('test_two 不需要登录')

def test_three(login):
    print('test_three 需要登录')

if __name__=='__main__':
    pytest.main()