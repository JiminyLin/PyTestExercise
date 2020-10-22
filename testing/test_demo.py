import pytest

test_user_data = ['Tom', 'Jerry']


@pytest.fixture(scope='module')
def login_r(request):
    user = request.param
    print(f'\n 打开首页准备登录，登录用户：{user}')
    return user


@pytest.mark.parametrize('login_r', test_user_data, indirect=True)
def test_login(login_r):
    a = login_r
    print(f'测试用例中login返回值,{a}')
    assert a != ''

class TestDemo:
    def func(self, x):
        return x + 1

    def test_answer(self):
        result = self.func(2) == 30
        pytest.assume(result == 21)
        pytest.assume(self.func(20) == 21)
        pytest.assume(self.func(2) == 2)

    def test_answer2(self):
        result = self.func(2)
        assert result == 3

    @pytest.mark.xfail
    def test_xfail(self):
        result = self.func(1)
        assert result== 2


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_demo.py::TestDemo::test_answer'])# 不知道为什么指定执行的方法无效
    pass