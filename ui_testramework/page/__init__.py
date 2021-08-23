# -*- coding:utf-8 -*-
import yaml

caps = yaml.safe_load(open('../page/configuration.yaml'))

print(caps)
print(caps['desired_caps'])
print(caps['desired_caps']['udid'])