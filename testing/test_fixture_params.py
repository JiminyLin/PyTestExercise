#!/usr/bin/python3
# coding=utf-8
import pytest


class TestFixtureParams:

    # @pytest.mark.parametrize('a,b',)
    def test_one(self,preMethod):
        print(f'\n test_one preMethod:{preMethod}')

    def test_two(self):
        print('执行test_two')

    def test_three(self,preMethod):
        print(f'\n test_three preMethod:{preMethod}')
