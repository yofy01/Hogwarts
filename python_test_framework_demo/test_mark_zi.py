# -*- coding:utf-8 -*-
import pytest

@pytest.mark.search
def test_search1():
    print("test_search1")
    raise NameError
    pass

@pytest.mark.search
def test_search2():
    print("test_search2")
    pass

@pytest.mark.search
def test_search3():
    print("test_search3")
    pass

@pytest.mark.login
def test_login1():
    print("test_login1")
    pass

@pytest.mark.login
def test_login2():
    print("test_login2")
    pass

if __name__=='__main__':
    # pytest.main(('-s', '-m login', 'test_mark_zi.py'))  # 看网上是有用的，这会都没用了...
    # 运行登陆功能的用例
    pytest.main(['-m login'])