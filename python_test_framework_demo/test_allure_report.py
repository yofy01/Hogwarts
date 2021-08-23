# -*- coding:utf-8 -*-
import pytest
import allure

# @allure.feature('登录模块')
# class TestLogin:
#     @allure.story('登录成功')
#     def test_login_success(self):
#         print('这是登录： 测试用例， 登录成功')
#         pass
#
#     @allure.story('登录失败')
#     def test_login_success_a(self):
#         print('这是登录： 测试用例， 登录失败')
#         pass
#
#     @allure.story('用户名缺失')
#     def test_login_success_b(self):
#         print('用户名缺失')
#         pass
#
#     @allure.story('密码缺失')
#     def test_login_failure(self):
#         with allure.step('点击用户名'):
#             print('输入用户名')
#         with allure.step('点击密码'):
#             print('输入密码')
#         print('点击登录')
#         with allure.step('点击登录之后登录失败'):
#             assert '1' == 1
#             print('登录失败')
#
#     @allure.story('登录失败')
#     def test_login_failure_a(self):
#         print('这是登录： 测试用例， 登录失败')
#         pass
#
#     @allure.link('http://www.baidu.com', name='关联bug')
#     def test_error_link(self):
#         print('直接给关键测试用例的地址连接，关联bug等')
#         pass
#
#     TEST_CASE_LINK = 'http://www.baidu.com'
#     @allure.testcase(TEST_CASE_LINK)
#     def test_testcase(self):
#         print('加载测试用例连接')
#         pass
#
#     # --allure-link-pattern=issue:http://www.mytesttracker.com/issue()
#     @allure.issue('10086', '这是一个issue')
#     def test_issue(self):
#         pass

@allure.severity(allure.severity_level.TRIVIAL)
def test_allure_severity_trivial_level():
    print('TRIVIAL:轻微缺陷')
    pass

@allure.severity(allure.severity_level.MINOR)
def test_allure_severity_minor_level():
    print('MINOR:次要缺陷')
    pass

@allure.severity(allure.severity_level.NORMAL)
def test_allure_outside_severity_normal_level():
    print('NORMAL:普通缺陷')
    pass

@allure.severity(allure.severity_level.NORMAL)
class TestSeverity:

    @allure.severity(allure.severity_level.CRITICAL)
    def test_allure_severity_critical_level(self):
        print('CRITICAL:临界缺陷')
        pass

    def test_allure_severity_normal_class(self):
        print('没有加装饰器')
        pass


if __name__=="__main__":
    pytest.main()

