01、fixture在自动化中的应用，自动应用
		场景：不想原测试方法有任何改动，或全部自动实现自动应用，美特利，也都不需要返回值时可以选择自动应用
		解决：使用fixture中参数autouse=Ture实现
		步骤：在方法上面加上@pytest.fixture(autouse=True)