"""
@Author: 霍格沃兹测试开发学社-西西
@Desc: 更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860
"""
import allure


# 格式1：添加一个普通的link 链接
@allure.link('https://ceshiren.com/t/topic/15860')
def test_with_link():
    pass

# 格式1：添加一个普通的link 链接，添加name 起别名
@allure.link('https://ceshiren.com/t/topic/15860',name="测试人网 站")
def test_with_link1():
    pass



# 格式2：添加用例管理系统链接
TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'

@allure.testcase(TEST_CASE_LINK, '用例管理系统')
def test_with_testcase_link():
    pass


@allure.issue("15860", 'Bug管理系统')
def test_with_issue():
    pass