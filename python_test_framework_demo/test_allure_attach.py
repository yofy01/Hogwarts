# -*- coding:utf-8 -*-
import allure
import pytest

def test_attach_text():
    allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body><h2>这是一段html</h2></body>", "html测试块", attachment_type=allure.attachment_type.HTML)

# 传文件的时候用的是file方法
def test_attach_image():
    allure.attach.file(r"E:\TestDev\python_test_framework_demo\resource\多啦A.jpg", name="JPG图片", attachment_type=allure.attachment_type.JPG)

# 传文件的时候用的是file方法
def test_attach_vedio():
    allure.attach.file(r"E:\TestDev\python_test_framework_demo\resource\9 数据驱动.mp4", name="数据驱动.mp4", attachment_type=allure.attachment_type.MP4)


if __name__ == '__main__':
    pytest.main()
