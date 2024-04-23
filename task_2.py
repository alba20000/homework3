class Person:
    def __init__(self, name, city, year):
        self.name = name
        self.city = city
        self.year = year

    def how_old(self):
        return 2024 - self.year


dude = Person("James", "London", 1984)
print(dude.how_old())
