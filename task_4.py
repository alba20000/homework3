class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"What a beautiful {self.color} {self.name}!"


bober = Animal("beaver", "brown")
print(str(bober))
