import pytest


class TestDemo:
    #初始化大前提可以放在setup_class
    def setup_class(self):
        # 第一步，打开浏览器
        print("setup_class 第一步，打开浏览器")
        pass
    def teardown_class(self):
        # 第五步，关闭浏览器
        print("teardown_class 第五步，关闭浏览器")

        pass

    # 初始化小前提放在setup
    def setup(self):
        # 第二步，输入网址

        print('setup')

    def teardown(self):
        pass

    @pytest.fixture()
    def login(self, ):
        print('fixture-登录')
        username = ""
        yield username
        print('teardown')

    def test_a(self,login):
        # 第一步，打开浏览器
        # 第三步，定位
        # 第四步，各种操作
        print("test_a")

        pass
    def test_b(self):
        print("test_b")

        pass


    if __name__ == '__main__':
        pytest.main(['sv'])