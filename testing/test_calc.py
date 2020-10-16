import pytest

from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        print('计算开始')
        self.calc = Calculator()

    def teardown_class(self):
        print('计算结束')

    @pytest.mark.parametrize('a,b,expect', [[1, 2, 3], [2, 3, 4], [3.0, 6, 9],[-1,-1,-2]],ids=['int_case1','int_case2','flat_case','minus_case'])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    def test_add2(self):
        result = self.calc.add(12, 1)
        assert result == 2

    @pytest.mark.parametrize('a,b,expect',[(2,2,0),(3,2,1),(-2,-4,2),(0,1,-1)])
    def test_sub(self,a,b,expect):
        result = self.calc.sub(a,b)

        assert result == expect
