if __name__ == '__main__':
    # 运行当前目录下所有的 用例
    pytest.main()

"""
__author__ = 'hogwarts_xixi'
"""
import pytest

@pytest.mark.parametrize("wd",["appium","selenium","pytest"])
@pytest.mark.parametrize("code",["utf-8","gbk","gb2312"])
def test_dkej(wd,code):
    print(f"wd: {wd}, code: {code}")