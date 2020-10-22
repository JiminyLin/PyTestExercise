#!/usr/bin/python3
# coding=utf-8
import pytest
import yaml

from pythoncode.calculator import Calculator


def get_Add_Datas():
    with open("./datas/calcData.yml",encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    print(f'get_Add_Datas-datas{datas}')


    return [add_datas,add_ids]

def get_Sub_Datas():
    with open("./datas/calcData.yml",encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        print(f'datas:{datas}')
    sub_datas = datas['sub']['datas']
    sub_ids = datas['sub']['ids']

    return [sub_datas,sub_ids]

def get_Mult_Datas():
    with open("./datas/calcData.yml",encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    mul_datas = datas['mult']['datas']
    mul_ids = datas['mult']['ids']

    return [mul_datas,mul_ids]

def get_Div_Datas():
    with open("./datas/calcData.yml",encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    div_datas = datas['div']['datas']
    div_ids = datas['div']['ids']

    return [div_datas,div_ids]


class TestCalcTaskOne:

    def setup_class(self):
        self.calc = Calculator()


    def teardown_class(self):
        pass

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect',get_Add_Datas()[0],ids=get_Add_Datas()[1])
    def test_add(self, a, b, expect):
        result = self.calc.add(a,b)
        assert  result == expect

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,expect',get_Sub_Datas()[0],ids=get_Sub_Datas()[1])
    def test_sub(self,a, b, expect):
        result = self.calc.sub(a,b)
        assert  result == expect

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,expect', get_Mult_Datas()[0], ids=get_Mult_Datas()[1])
    def test_mult(self, a, b, expect):
        result = self.calc.mul(a,b)
        assert result == expect

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,expect',get_Div_Datas()[0],ids=get_Div_Datas()[1])
    def test_div(self,a,b,expect):
        result = self.calc.div(a,b)
        assert result == expect


if __name__ == '__main__':
    pytest.main(['-vs','test_calc2.py'])