class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


rect = Rectangle(4, 6)
print(rect.area())
print(rect.perimeter())
