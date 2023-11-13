"""
@Author: 霍格沃兹测试开发学社-西西
@Desc: 更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860
"""

import allure
from utils.log_util import logger
class TestWithAttach:
    def test_pic(self):
        logger.info("添加一个图片")

        allure.attach.file("./img/logo.png",
                           name="这是一个图片",
                           attachment_type=allure.attachment_type.PNG,
                           extension="png")

    def test_pic2(self):
        logger.info("这是通过allure.attach添加一个图片")
        with open("./img/logo.png", mode="rb") as f:
            # 文件的内容
            file = f.read()
            # 将文件内容添加到allure.attach()方法第一个参数中
            allure.attach(file, name="页面截图",attachment_type=allure.attachment_type.PNG)

