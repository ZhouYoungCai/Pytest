"""
@Author: 霍格沃兹测试开发学社-西西
@Desc: 更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860
"""
import pytest

"""
@Author: 霍格沃兹测试开发学社-西西
@Desc: 更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860
"""
import allure

# 未加【级别标签】的用例，在运行时候，是不会被收集上来的。
def test_with_no_severity_label():
    pass

@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass


@allure.severity(allure.severity_level.MINOR)
def test_with_minor():
    pass

@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity(object):

    def test_inside_the_normal(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_critical_severity(self):
        pass

    @allure.severity(allure.severity_level.BLOCKER)
    def test_blocker_severity(self):
        pass