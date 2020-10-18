import allure
import pytest
import yaml

from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()

    def teardown_class(self):
        pass

    @allure.story('计算器的加法')
    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('./data/add.yml')))
    def test_Add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @allure.story('计算器的减法')
    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('./data/sub.yml')))
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @allure.story('计算器的乘法')
    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('./data/mult.yml')))
    def test_mult(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    @allure.story('计算器的除法')
    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('./data/div.yml')))
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect
