#!/usr/bin/python3
# coding=utf-8
import pytest

from pythoncode.calculator import Calculator


def pytest_collection_modifyitems(session, config, items):
    for item in items:
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)
        elif 'mult' in item.nodeid:
            item.add_marker(pytest.mark.mult)
        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)
    print(items)


# 用于避免执行指定自定义标记用例时其他未被执行的自定义标记用例报警告
def pytest_configure(config):
    marker_list = ['add', 'sub', 'mult', 'div']
    for markers in marker_list:
        config.addinivalue_line(
            'markers', markers
        )




@pytest.fixture(scope='module')
def calcAction():
    print('开始计算')
    yield
    print('结束计算')
