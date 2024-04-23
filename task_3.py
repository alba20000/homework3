class Calc:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b


print(Calc.add(2, 4))
print(Calc.subtract(8, 3))
print(Calc.multiply(5, 7))
print(Calc.divide(9, 6))
