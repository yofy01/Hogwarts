# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
'''
复用已有浏览器页面（调试时很方便）
1、Chrome浏览器应用放入到环境变量，然后可以实现开启chrome调试模式
开启浏览器，随机指定端口，cmd输入：
chrome --remote-debugging-port=8888
'''

option = Options()
option.debugger_address = '127.0.0.1:8888'

driver = webdriver.Chrome(options=option)
driver.get('https://www.baidu.com')