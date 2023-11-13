01、fixture在自动化中的应用，yield关键字
		场景：你已经可以将测试方法[前要执行或依赖的]解决了，测试方法后销毁清楚数据的要如何进行呢
		解决：通过在fixture函数中加入yield关键字，yield是调用第一次返回结果，第二次执行它下面的语句返回。
		步骤：在@pytest.fixture(scope=module)在登录的方法中加yield，之后加销毁清除的步骤