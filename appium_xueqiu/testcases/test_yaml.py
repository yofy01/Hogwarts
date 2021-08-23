# -*- coding:utf-8 -*-
import json

import pytest
import yaml

_params =  dict()
_params['stock_name'] = '阿里巴巴'
_params['stock_code'] = 'BABA'

def test_params():
	with open('../page/search.yaml', encoding='utf-8') as f:
		steps = yaml.safe_load(f)['search']
		steps_str = json.dumps(steps)
		for key, value in _params.items():
			old = '${' + key + '}'
			print(steps_str.find(old))
			print(old)
			steps_str = steps_str.replace('${' + key + '}', value)
		print(steps_str)
		# steps = json.loads(steps_str)
		# print(steps)

def test_yaml():
	with open('../testcases/search_data.yaml', encoding='utf-8') as f:
		data = yaml.safe_load(f)
		print(data,type(data))
