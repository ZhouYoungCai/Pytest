#coding:utf-8
#content of test_sample.py
def inc(x):
    return x + 1
def test_answer():
    assert inc(4) == 5  #assert代表断言
class TestDemo:
    def test_demo1(self):
        pass

    def test_demo2(self):
        pass