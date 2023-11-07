 1、标记测试用例
     场景：只执行符合要求的某一部分的用例，可以吧一个web项目划分为多个模块，然后指定模块名称执行
	 解决：在测试用例方法上加@pytest.mark.标签名
	 执行：-m 执行自定义标记的相关用例
	     pytest -s test_mark_zi_09.py -m=webtest
		 pytest -s test_mark_zi_09.py -m apptest
		 pytest -s test_mark_zi_09.py -m "not ios"