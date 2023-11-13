"""
@Author: 霍格沃兹测试开发学社-西西
@Desc: 更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860
"""
import allure
import pytest

# 方式一：通过装饰器添加标题
@allure.title("自定义测试用例标题")
def test_with_title():
    assert True


# 第二种方式：通过占位符实现参数化的测试数据添加到标题中
@allure.title("参数化用例标题：参数一：{param1} ，参数二： {param2}")
@pytest.mark.parametrize("param1, param2, expected", [
    (1, 1, 2),
    (0.1, 0.3, 0.4)
])
def test_with_parametrize_title(param1, param2, expected):
    assert param1 + param2 == expected

# 第 三种方式：动态更新测试用例的标题

@allure.title("原始标题")
def test_with_dynamic_title():
    assert True
    allure.dynamic.title("更改后的新标题")