"""
@Author: 霍格沃兹测试开发学社-西西
@Desc: 更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860
"""

import pytest

# 当用例通过时标注为 xfail
@pytest.mark.xfail(reason='这是一个预期失败的用例')
def test_xfail_expected_failure():
    """this test is an xfail that will be marked as expected failure"""
    assert False

# 当用例通过时标注为 xpass
@pytest.mark.xfail
def test_xfail_unexpected_pass():
    """this test is an xfail that will be marked as unexpected success"""
    assert True

# 跳过用例
@pytest.mark.skipif('2 + 2 != 5', reason='当条件触发时这个用例被跳过 @pytest.mark.skipif')
def test_skip_by_triggered_condition():
    pass


"""
@Author: 霍格沃兹测试开发学社-西西
@Desc: 更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860
"""
import pytest

@pytest.fixture()
def func1():
    print("这是fixture func1 前置动作")
    yield
    print("这是fixture func1 后置动作")
@pytest.fixture()
def func(request):
    # 前置动作 -- 相当于setup
    print("这是一个fixture方法")
    # 后置动作 -- 相当于teardown
    # 定义一个终结器，teardown动作放在终结器中
    def over():
        print("session级别终结器")
    # 添加终结器，在执行完测试用例之后会执行终结器中的内容
    request.addfinalizer(over)


class TestClass(object):
    def test_with_scoped_finalizers(self,func,func1):
        print("测试用例")