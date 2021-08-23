# -*- coding:utf-8 -*-

def outter(value):
	def extends(func):	# 加包
		def hello(*args, **kwargs):	# 加包
			print('heelo')
			print(value)
			print(args)
			print(kwargs)
			func(*args, **kwargs)
			print('bye-bye')
		return hello	# 解包
	return extends  # 解包

@outter("这是一个参数")
def tmp(a,b,c,d):
	print('jojo')


def test_tmp():
	tmp(1,2,3, d=10) # 字典是在传值的时候才定义的