# -*- coding:utf-8 -*-

"""
1、pytest中的 @pytest.fixtues()
2、pytest中的 conftest.py
3、pytest中的 yield关键字
4、pytest中的 autouse的使用，@pytest.fixtues(autouse=True)
5、pytest中的 fixture固定参数request的应用
6、pytest中的 mark中的skip和 xfail
7、pytest中的 自定义mark
8、pytest中的 pytest-xdist库的应用 多线程并行和分布式执行
9、pytest中的 生成报告库：pytest-html
"""

"""
场景1：
* 用例1需要先登录
* 用例2不需要登录
* 用例3需要登录
----
这种场景无法使用setup和teardown实现，需要使用pytest的fixture
用法：@pytest.fixture()
步骤：
1、导入pytest
2、定义函数login,并在login函数前加上装饰器@pytest.fixtuer()，
    说明该函数名被别的函数当参数传入时，才会执行；不传入则不执行
3、定义三个测试函数test_one/test_two/test_three,其中test_one和test_three传入参数login
4、pytest.main()执行函数，查看结果可知，test_one和test_three在执行前先执行了登录login方法
"""

"""
场景2：
测试过程中，需要与其他测试工程师进行合作。公共模块需要用到 conftest.py
注意：
* conftest.py 文件名固定，不能换
* conftest.py 与运行的用例要在同一个package里，并且有__init__.py文件
* 不需要import导入coftest.py，pytest会自动取读取
* 全局的配置和前期工作都可以写在这里，放在某个包下，这个包就是数据共享的地方

* pytest执行用例时，会在当前文件中查找对应的变量
    没有找到的情况下会到conftest.py中查找
* 可以将场景1的带装饰器@pytest.fixture()的login方法写到conftest.py中
"""

"""
场景3：pytest中的 yield关键字
作用：类似teardownClass，收尾工作。测试方法执行结束后的销毁数据；范围是模块级别
用法：
* 通过在同一个模块中加入 yield 关键字，yield是调用第一次返回的结果，
第二次执行它下班的语句返回。

步骤：
在你的测试用例前面加上装饰器：@pytest.fixture(scope=module)

* 场景1的登录方法login中加yield，之后加销毁清除步骤
注意这种方法没有返回值，如果希望返回，只有addfinalizer
"""

"""
场景4：fixture 自动应用
* 不想原测试方法有任何改动
或全部都自动实现自动应用，没特例，也都不需要返回值时可以选择自动应用

解决：使用 fixture 中参数 autouse = True 实现
步骤：
* 在方法上面加 @pytest.fixture(autouse=True)
* 在测试方法上加 @pytest.mark.usefixture('start')  # 好像不加也没关系
"""

"""
场景5：fixture 带参数传递
测试离不开测试数据，为了数据灵活，一般是通过参数传递
解决：fixture通过固定参数 request 传递
步骤：
1、在fixture中添加 @pytest.fixure(params=[（’yofy‘，’123456‘），（’lily‘,'1234567'）]) 
    有几个测试用例传几组值,比如模拟用户登录，正确登录/错误登录
2、在方法参数写 request
"""