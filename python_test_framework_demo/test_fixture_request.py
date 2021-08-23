# -*- coding:utf-8 -*-
import pytest
import sys
# 参数化：前两个是变量，后两个是对应的数据
# @pytest.mark.parametrize(参数-多个空格隔开，参数值-多个则列表形式)
# @pytest.mark.parametrize("test_input, expected", [("10-7", 3), ("4+19", 23), ("2+3", 5)])
# def test_eval(test_input, expected):
#     # eval 将字符串str当成有效的表达式来求值，并返回结果
#     assert eval(test_input) == expected

# 参数组合(针对不同输入参数，多种组合测试的场景）
# @pytest.mark.parametrize("x",[1,2])
# @pytest.mark.parametrize("y",[4,9,11,56])
# def test_add(x,y):
#     # print(type(x), type(y)) # <class 'int'> <class 'int'>
#     print("x:%d, y:%d" % (x, y))

# 方法名作为参数
test_user_data=['yofy', 'lily']
@pytest.fixture(scope='module') # 作用域是module，在整个运行期间都是可用的
def login(request):
    # 接收并传入参数
    user = request.param
    print(f'\n 打开首页准备登录，登录用户：{user}')
    return user

# @pytest.mark.skipif(sys.platform=='win32', reason="不在win上运行")
@pytest.mark.xfail
# indirect=True,可以把传过来的参数当做函数来执行
@pytest.mark.parametrize("login", test_user_data, indirect=True)
def test_login(login):
    a = login
    print(f"测试用例中login的返回时：{a}")
    assert a !=""
    raise NameError
