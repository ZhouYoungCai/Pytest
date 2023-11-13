1、json 文件介绍
	json 是 JS 对象
	全称是 JavaScript Object Notation
	是一种轻量级的数据交换格式
	json 结构
	对象 {"key": value}
	数组 [value1, value2 ...]
	{
	  "name:": "hogwarts ",
	  "detail": {
		"course": "python",
		"city": "北京"
	  },
	  "remark": [1000, 666, 888]
	}
2、json 文件使用
	查看 json 文件
	pycharm
	txt 记事本
	读取 json 文件
	内置函数 open()
	内置库 json
	方法：json.loads()
	方法：json.dumps()
	# 读取json文件内容
	def get_json():
		with open('demo.json', 'r') as f:
			data = json.loads(f.read())
			print(data)
3、工程目录结构
	data 目录：存放 json 数据文件

	func 目录：存放被测函数文件

	testcase 目录：存放测试用例文件

	# 工程目录结构
	.
	├── data
	│   └── params.json
	├── func
	│   ├── __init__.py
	│   └── operation.py
	└── testcase
		├── __init__.py
		└── test_add.py
4、测试准备
	被测对象：operation.py

	测试用例：test_add.py

	测试数据：params.json

	# operation.py 文件内容
	def my_add(x, y):
		result = x + y
		return result

	# test_add.py 文件内容
	class TestWithJSON:
		@pytest.mark.parametrize('x,y,expected', [[1, 1, 2]])
		def test_add(self, x, y, expected):
			assert my_add(int(x), int(y)) == int(expected)

	# params.json 文件内容
	{
	  "case1": [1, 1, 2],
	  "case2": [3, 6, 9],
	  "case3": [100, 200, 300]
	}
5、Pytest 数据驱动结合 json 文件
	# 读取json文件
	def get_json():
		"""
		获取json数据
		:return: 返回数据的结构：[[1, 1, 2], [3, 6, 9], [100, 200, 300]]
		"""
		with open('../data/params.json', 'r') as f:
			data = json.loads(f.read())
			return list(data.values())