class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return round((a - b),10)

    def mul(self, a, b):
        return round((a * b),5)

    def div(self, a, b):
        try:
            round((a / b), 5)
            return round((a / b), 5)
        except ZeroDivisionError as err:
            print (f'err:{err}')
            return "divisor can't 0"


