1、目录
	知识点梳理
	测试流程
	知识点练习
	业务分析
	用例设计
	编写用例
	练习题点评与解析
2、为什么要学习单测框架？
	测试发现：从多个文件中找到测试用例
	测试执行：按照一定的顺序和规则去执行用例，并生成结果
	测试判断：通过断言判断预期结果和实际结果的差异
	测试条件：给定一些前置和后置的条件
	测试报告：统计测试进度、耗时、通过率，生成测试报告
3、实战练习
	计算器场景
	设计测试用例
4、计算器场景需求分析
	被测方法需要传递的数据类型为：整型或者浮点型
	数据区间为【-99，99】
	浮点数允许小数点后两位
5、被测代码分析
	class Calculator:
		def add(self, a, b):

			if a > 99 or a < -99 or b > 99 or b < -99:
				print("请输入范围为【-99, 99】的整数或浮点数")
				return "参数大小超出范围"

			return a + b

		def div(self, a, b):
			if a > 99 or a < -99 or b > 99 or b < -99:
				print("请输入范围为【-99, 99】的整数或浮点数")
				return "参数大小超出范围"

			return a / b
6、测试用例设计
	等价类
	边界值
	错误推断
7、测试用例编写 1
	题目：
	根据需求编写计算机器（加法和除法）相应的测试用例
	在调用每个测试方法之前打印【开始计算】
	在调用测试方法之后打印【结束计算】
	调用完所有的测试用例最终输出【结束测试】
	为用例添加标签
	注意：
	a、使用等价类，边界值，错误猜测等方法进行用例设计
	b、用例中要添加断言，验证结果
	c、灵活使用测试装置
8、总结知识点
	setup, teardown
	参数化与 ids 用法
	浮点数处理
	异常处理
	断言
9、测试用例编写 2
	使用参数化实现测试数据的动态传递
	将测试数据保存到 datas/data.yml
	创建读取数据的方法（注意编码格式）
10、使用 yaml 实现数据驱动
	with open("./datas/datas.yml", encoding='utf-8') as f:
	  datas = yaml.safe_load(f)
		  print(datas)
11、测试数据
    测试数据：https://ceshiren.com/t/topic/14837
12、修改编码
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
13、添加标签
    @pytest.mark.标签名
14、总结
	文件只读一次：yaml 文件读取时只能读取一次，再次读取游标会指到最下面
	注意编码：windows 系统，读取 yaml 文件时，要指定 encoding=utf-8
	通过 pytest.ini 文件进行相关的配置（比如标签名，运行默认参数）
15、目录
	梳理 fixture 部分知识点
	实战一 - 使用 Fixture 实现计算器测试
	实战二 - 合理使用第三方插件实现特殊需求
	总结知识点
16、实战一 使用 Fixture
	使用fixture 提供 calc 对象
	使用 fixture实现：用例执行之前打印【开始计算】，之后【结束计算】
	当前模块所有用例执行完成之后，打印【测试结束】
	每条用例添加测试日志，并将日志打印输出到logs/ <日期_时间>.log 文件中
17、实战一 总结
	Fixture 用法
	Conftest.py 文件的用法
	conftest.py文件同目录，必须要有一个__Init__.py 文件
	固定写法，不需要导入
	所有同目录测试文件运行前都会执行conftest.py文件
	pytest.ini 用法
	配置 pytest相关配置
	比如日志文件 ，格式
	比如 markers 标签 ，
	也能指定执行哪个目录 ，或者过滤哪个目录
18、实战二
	使用fixture实现参数化
	定义执行顺序，顺序为
	先add方法 P1_1 和 P1_2级别的用例
	其次执行P0 级别
	然后执行 相除方法的用例
	最后执行add 方法P2）
	add 用例 （P1_1>P1_2>P0）> div 用例 >  add 用例（P2）
19、实战三
	加速执行，三个进程并发执行所有用例
	生成测试报告，添加用例分类
	添加测试步骤，添加图像（本地图片）