# 1、Python测试框架前言
# 	自动化测试前，需要提前准备好数据，测试完成后，需要自动清理脏数据，有没有更好用的框架呢？
# 	自动化测试中，需要使用多套测试数据实现用力的参数化，有没有更便捷的方式？
# 	自动化测试后，需要自动生成优雅、简洁的测试报告，有没有更好的测试方法
# 2、pytest是什么？
# 	pytest能够支持简单的单元测试和复杂的功能测试
# 	pytest可以结合request实现接口测试，结合selenium、appium实现自动化功能测试
# 	使用pytest结合allure集成到Jenkins中可以实现持续集成
# 	pytest支持315种以上的插件
# 3、为什么选择pytest
# 	丰富的第三方插件：报告、多线程、顺序控制
# 	功能非常强大，编写简单灵活
# 	兼容unittest、定制化插件开发
# 4、pytest环境安装
# 	前提：本地已配置完成Python环境，（大于3.6版本，才会自带pip）
# 	第一种方式：pip install pytest
# 	第二种方式：pycharm直接安装
# 5、运行第一个脚本
# 	代码：
# 	#content 0f test_sample.py
def inc(x):
	return x + 1
	print(inc(4))
# 	代码：
def test_answer():
	assert inc(4) == 5