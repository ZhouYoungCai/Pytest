01、allure常用命令--报告生成
		生成测试报告流程：
		1、运行pytest用例----生成中间结果，包括json、text格式，执行allure server命令，生成在线版本测试报告。
		2、运行pytest用例----生成中间结果，包括json、text格式，执行allure generate命令，生成最终版本测试报告。
		命令：pytest --alluredir