
#yield + 函数 = 生成器

# def provider():
#     for i in range (5):
#         print('before')
#         yield i #生成器：return i+暂停并且记住了上一次运行的位置。和fixture结合使用实现stup和teardown方法
#         print('after\n')
#
# p = provider()
# print(next(p),'------')
# print(next(p),'------')
# print(next(p),'------')
import pytest


def test_f11():
    # 本用例代码
    print('test_f11-')

def test_f12():
    # 本用例代码
    print('test_f12')


class TestSendMsg:

    def test_f1(self):
        # 本用例代码
        print('test_f1-')

    def test_f2(self):
        # 本用例代码
        print('test_f2-')

    def test_f3(self):
        # 本用例代码
        print('test_f3-')


if __name__ == '__main__':
    pytest.main(['-vs','test_yield.py::TestSendMsg'])