# 模块级别，python是一个文件一个模块
def setup_module():
    print('资源准备：setup_module')


# 模块级别，python是一个文件一个模块
def teardown_module():
    print('资源销毁：teardown_module')


def test_case1():
    print('case1')


# 不在类中，函数级别
def setup_function():
    print('资源准备：setup_function')


def teardown_function():
    print('资源销毁：teardown_fuction')


# 类级别和方法级别
class TestDemo:
    # 类级别
    def setup_class(self):
        print('TestDemo setup_class')

    # 类级别
    def teardown_class(self):
        print('TestDemo teardown_class')

    def setup_method(self):
        print('TestDemo setup_method')

    def teardown_method(self):
        print('TestDemo teardown_method')

    # 方法级别
    def setup(self):
        print('TestDemo setup')

    # 方法级别
    def teardown(self):
        print('TestDemo teardown')

    def test_demo1(self):
        print('demo1')


class TestDemo1:
    # 类级别
    def setup_class(self):
        print('1 TestDemo setup_class')

    # 类级别
    def teardown_class(self):
        print('1 TestDemo teardown_class')

    # 方法级别
    def setup(self):
        print('1 TestDemo setup')

    # 方法级别
    def teardown(self):
        print('1 TestDemo teardown')

    def test_demo1(self):
        print('1 demo1')
