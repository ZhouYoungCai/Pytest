"""
@Author: 霍格沃兹测试开发学社-西西
@Desc: 更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860
"""

import allure

from utils.log_util import logger


class TestWithAttach:
    def test_video(self):
        logger.info("测试用例执行过程视频")
        allure.attach.file("/Users/juanxu/Movies/Allure2安装.mp4",
                           name="这是一个mp4视频文件",
                           attachment_type=allure.attachment_type.MP4,
                           extension="mp4")

    def test_video1(self):
        allure.attach.file("/Users/juanxu/Movies/Allure2报告生成.mp4",
                           name="这是一个mp4视频文件",
                           attachment_type=allure.attachment_type.MP4,
                           extension="mp4")