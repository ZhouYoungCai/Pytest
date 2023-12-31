1、跳过(skip)及预期失败(xfail)
    这是pytest的内置标签，可以处理一些特殊的测试用例，不能成功的测试用例
	skip-始终跳过该测试用例
	skipif-遇到特定情况跳过该测试用例
	xfail -遇到特定情况，产生一个“期望失败“输出
    skip使用场景：
	    调试时不想运行这个用例
		标记无法在某些平台上运行的测试功能
		在某些版本中执行，其他版本中跳过
		比如：当前的外部资源不可用时跳过
		    如果测试数据是从数据库中取到的，连接数据库的功能如果返回结果未成功就跳过，因为执行也都报错
		解决1：添加装饰器
		    @pytest.mark.skip
			@pytest.mark.skipif
	    解决2：代码中添加跳过代码
		    pytest.skip(renson)
	xfail使用场景
	    与skip类似，预期结果为fail，标记用例为fail
		用法：添加装饰器@pytest.mark.xfail