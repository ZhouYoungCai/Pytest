"""
@Author: 霍格沃兹测试开发学社-西西
@Desc: 更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860
"""
import allure

from utils.log_util import logger


@allure.epic("需求1")
@allure.feature("功能模块一")
class TestEpic:
    @allure.story("子功能一")
    @allure.title("用例1")
    def test_case1(self):
        logger.info("这是 TestEpic 第一条用例")
        print("用例1")

    @allure.story("子功能二")
    @allure.title("用例2")
    def test_case2(self):
        logger.debug("这是 TestEpic 第二条用例")
        print("用例2")

    @allure.story("子功能二")
    @allure.title("用例3")
    def test_case3(self):
        logger.warning("这是 TestEpic 第三条用例")
        print("用例3")

    @allure.story("子功能一")
    @allure.title("用例4")
    def test_case4(self):
        logger.error("这是 TestEpic 第四条用例")
        print("用例4")

    @allure.story("子功能三")
    @allure.title("用例5")
    def test_case5(self):
        print("用例5")

@allure.epic("需求1")
@allure.feature("功能模块二")
class TestEpic1:
    @allure.story("子功能四")
    def test_case1(self):
        print("用例1")

    @allure.story("子功能五")
    def test_case2(self):
        print("用例2")

    def test_case3(self):
        print("用例3")


@allure.epic("需求2")
class TestEpic2:
    def test_case1(self):
        print("用例1")

    def test_case2(self):
        print("用例2")

    def test_case3(self):
        print("用例3")