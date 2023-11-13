if __name__ == '__main__':
    # 运行当前目录下所有的 用例
    pytest.main()
"""
__author__ = 'hogwarts_xixi'
"""
import pytest

search_list = ['appium','selenium','pytest']

@pytest.mark.parametrize('name',search_list)
def test_search(name):
    assert name in search_list