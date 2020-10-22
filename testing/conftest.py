#!/usr/bin/python3
# coding=utf-8
import pytest


@pytest.fixture(scope='module',autouse=False)
def login():
    a = 'conftest-login方法中login';
    print(a)
    yield
    a = 'conftest-login方法中logout'
    print(a)

@pytest.fixture(scope='module')
def outCalcStarEnd():
    print('开始计算')
    yield
    print('计算结束')

@pytest.fixture(params=[[11,22],[33,44]])
def preMethod(request):
    print(f'执行conftest preMethod的前置函数，params：{request.param}')
    return request.param

#用于避免执行指定自定义标记用例时其他未被执行的自定义标记用例报警告
def pytest_configure(config):
    marker_list = ['add','sub','mult','div']
    for markers in marker_list:
        config.addinivalue_line(
            'markers',markers
        )