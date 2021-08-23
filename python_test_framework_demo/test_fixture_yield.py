# -*- coding:utf-8 -*-
import pytest

# 作用域：module是在模块之前执行，模块之后执行
# @pytest.fixture(scope='module')
@pytest.fixture() # 默认 scope=function
def open():
    print('打开浏览器')
    yield
    print('执行 teadrdown')
    print('关闭浏览器')


def test_search1(open):
    print('test_search1')
    raise  NameError
    pass

def test_search2(open):
    print('test_search2')
    pass

def test_search3(open):
    print('test_search2')
    pass

if __name__=='__main__':
    pytest.main()