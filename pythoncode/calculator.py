from decimal import Decimal

import pytest


class Calculator:



    def add(self, a, b):
        try:
            return a + b
        except TypeError as err:
            return 'TypeError'

    def sub(self, a, b):

        try:
            return round((a - b), 5)
        except TypeError as err:
            return 'TypeError'

    def mul(self, a, b):
        try:
            return round((a * b), 5)
        except TypeError as err:
            return 'TypeError'


    @pytest.mark.xfail
    def div(self, a, b):
        try:

            return round((a / b), 5)
        except ZeroDivisionError as err:
            return "division by zero"
        except TypeError as err:
            return 'TypeError'
