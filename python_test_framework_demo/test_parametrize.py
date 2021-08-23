# -*- coding:utf-8 -*-
import pytest
# 使用string
@pytest.mark.parametrize("a,b", [(10,20), (10,30)])
def test_param(a,b):
    print(a + b)

# 使用list
@pytest.mark.parametrize(["a","b"], [(10,20), (10,30)])
def test_param1(a,b):
    print(a * b)

# 使用tuple
@pytest.mark.parametrize(("a","b"), [(10,20), (10,30)])
def test_param2(a,b):
    print(a / b)

if __name__=='__main__':
    pytest.main()