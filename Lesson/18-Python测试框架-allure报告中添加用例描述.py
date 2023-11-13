10、Allure 用法
	查看官网：https://docs.qameta.io/allure/#_pytest
	源码example:  https://github.com/allure-examples/allure-examples/
11、Allure特性-feature/story
	场景:
	希望在报告中看到测试功能，子功能或场景
	解决:
	@Feature,  @story<br/> 步骤:
	import allure
	功能上加  @allure.feature(‘功能名称’)
	子功能上加  @allure.story(‘子功能名称’)
	运行：

	pytest 文件名 --allure-features=FEATURES_SET --allure-stories=STORIES_SET
12、Allure 特性-feature/story的关系
	feature 相当于一个功能，一个大的模块，相当于testsuite
	story 相当于对应这个功能或者模块下的不同场景，分支功能
	feature 与 story 类似于父子关系
13、Allure特性-step
	场景：
	测试过程中每个步骤，一般放在具体逻辑方法中，可以放在关键步骤中，在报告中显示
	在app, web⾃动测试当中，建议每切换到⼀个新的页⾯当做一个step
	解决 : 
	with allure.step():  可以放在测试用例方法里面，但测试步骤的代码需要被该语句包含
14、Allure特性 - testcase/issue/link
	场景：
	测试报告中，添加用例的链接，bug 链接地址，相关的链接地址

	解决 ：
	@allure.link()、@allure.issue()、@allure.testcase()
	主要是为了将allure报告和测试管理系统集成（用例管理/bug 管理 ），可以更快速的跳转到公司内部地址。
15、Allure特性 - 设置优先级
	五种级别 ：
		BLOCKER("blocker"),  阻塞缺陷（功能未实现，无法下一步）
		CRITICAL("critical"),    严重缺陷（功能点缺失）
		NORMAL("normal"),    一般缺陷（边界情况，格式错误）
		MINOR("minor"),     次要缺陷（界面错误与ui需求不符）
		TRIVIAL("trivial");    轻微缺陷（必须项无提示，或者提示不规范）
16、Allure特性 - 设置优先级
	场景：
	通常测试有P0、冒烟测试、验证上线测试。
	按重要性级别来分别执行的，比如上线要把主流程和重要模块都跑一遍
	解决 ：
	也可以通过 allure.severity来附加标记
	实例：
	在方法,函数和类上面加
	@allure.severity(allure.severity_level.TRIVIAL)

	运行：
	运⾏级别为：normal,critical  的测试⽤例
	pytest -s -v 文件名 –allure-severities normal,critical –alluredir=./result
17、Allure 特性 - 测试报告中添加附件
	场景：
	希望在报告中看到测试用例的详细内容展示
	比如在用例中添加附件信息，可以是数据，文本，图片，视频，网页

	解决:
	@allure.attach显示许多不同类型的提供的附件，可以补充测试，步骤或测试结果。
	用法：
	allure.attach(body(内容), name, attachment_type, extension):
18、Allure 总结
	支持多平台
	Java语⾔开发的，⽀持多语言 pytest，JaveScript, PHP, ruby 等
	可以为dev/qa提供详尽的的测试报告、测试步骤、log、标题、优先级、附件等等
	也可以为管理理层提供high level统计报告
	可以集成到Jenkins，展示项目的趋势图