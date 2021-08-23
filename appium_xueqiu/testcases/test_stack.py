# -*- coding:utf-8 -*-
import inspect

def hello():
	lists = inspect.stack()
	for list in lists:
		print(list.function)

def world():
	hello()

def test_stack():
	world()