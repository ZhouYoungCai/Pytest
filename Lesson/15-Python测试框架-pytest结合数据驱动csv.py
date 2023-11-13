1、csv 文件介绍
	csv：逗号分隔值
	是 Comma-Separated Values 的缩写
	以纯文本形式存储数字和文本
	文件由任意数目的记录组成
	每行记录由多个字段组成

	Linux从入门到高级,linux,¥5000
	web自动化测试进阶,python,¥3000
	app自动化测试进阶,python,¥6000
	Docker容器化技术,linux,¥5000
	测试平台开发与实战,python,¥8000
2、csv 文件使用
	读取数据

	内置函数：open()
	内置模块：csv
	方法：csv.reader(iterable)

	参数：iterable ,文件或列表对象
	返回：迭代器，每次迭代会返回一行数据。
	# 读取csv文件内容

	def get_csv():
		with open('demo.csv', 'r') as file:
			raw = csv.reader(file)

			for line in raw:
				print(line)
3、工程目录结构
	data 目录：存放 csv 数据文件

	func 目录：存放被测函数文件

	testcase 目录：存放测试用例文件

	# 工程目录结构
	.
	├── data
	│   └── params.csv
	├── func
	│   ├── __init__.py
	│   └── operation.py
	└── testcase
		├── __init__.py
		└── test_add.py
4、测试准备
	被测对象：operation.py

	测试用例：test_add.py

	测试数据：params.csv

	# operation.py 文件内容
	def my_add(x, y):
		result = x + y
		return result

	# test_add.py 文件内容
	class TestWithCSV:
		@pytest.mark.parametrize('x,y,expected', [[1, 1, 2]])
		def test_add(self, x, y, expected):
			assert my_add(int(x), int(y)) == int(expected)

	# params.csv 文件内容
	1,1,2
	3,6,9
	100,200,300
5、Pytest 数据驱动结合 csv 文件
	# 读取 data目录下的 params.csv 文件
	import csv

	def get_csv():
		"""
		获取csv数据
		:return: 返回数据的结构：[[1, 1, 2], [3, 6, 9], [100, 200, 300]]
		"""
		with open('../data/params.csv', 'r') as file:
			raw = csv.reader(file)
			data = []
			for line in raw:
				data.append(line)
		return data