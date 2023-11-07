1、Allure 介绍
	Allure是⼀个轻量级，灵活的，⽀持多语⾔的测试报告⼯具
	多平台的,奢华的report框架
	可以为dev/qa提供详尽的的测试报告、测试步骤、log
	也可以为管理理层提供high level统计报告
	Java语⾔开发的，⽀持python，JaveScript, PHP, ruby 等
	可以集成到Jenkins
2、Allure 报告展示
	官方：http://allure.qatools.ru
3、Allure 报告展示 - 首页概览
	Allure 报告展示 - 用例详情页
4、Allure 安装
	1、安装 Java (推荐 1.8 版本)，需要配置环境变量
	2、安装 Allure ，需要配置环境变量
5、JDK 环境安装
	java 官方下载地址（windows 下载 exe 安装包即可）
	https://www.oracle.com/java/technologies/downloads/#java8
	社区提供下载地址：
	链接: https://pan.baidu.com/s/1R8KClEPKio5dE0PAYN1jlA
	提取码: xwd9
6、配置 JAVA 环境变量
	java（windows 系统）：https://ceshiren.com/t/topic/13450
	java（mac 系统）：https://ceshiren.com/t/topic/6967
7、Allure 安装
	下载地址：https://repo1.maven.org/maven2/io/qameta/allure/allure-commandline/
	mac/linux: 下载 tar
	windows: 下载 zip
	配置环境变量：解压后将 bin 目录加入PATH环境变量
	安装贴：https://ceshiren.com/t/topic/3386
8、环境验证
	allure --version
9、使用 Allure2 生成精美报告
	命令格式：allure  [option]   [command]   [command options]
	在测试执行期间收集结果
	pytest  [测试文件] -s –q --alluredir=./result/ (—alluredir这个选项 用于指定存储测试结果的路径)
	查看测试报告
	方式一：测试完成后查看实际报告， 在线看报告，会直接打开默认浏览器展示当前报告
	  allure serve ./result/   (注意这里的serve书写)
	方式二：从结果生成报告，这是一个启动tomcat的服务，需要两个步骤：生成报告，打开报告
	  生成报告 
		allure generate ./result/ -o ./report/ --clean  (注意：覆盖路径加--clean )
	  打开报告 
		allure open -h 127.0.0.1 -p 8883 ./report/ 
