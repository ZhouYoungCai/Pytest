01、pytest fixture的作用范围
		取值      范围       说明
		function  函数级     每一个函数或方法都会调用
		class     类级别     每个测试类只运行一次
		module    模块级     每个.py文件调用一次
		package   包级       每个Python包只调用一次（暂不支持）
		session   会话级     每次会话只需要运行一次，会话内所有方法及类，模块都共享这个方法