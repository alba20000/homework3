class Worker:
    def work(self):
        print("Работаю")


class Student:
    def study(self):
        print("Учусь")

    def work(self):
        print("Подрабатываю")


class Teenager(Worker, Student):
    def play(self):
        print("Играю в комп")


chel = Teenager()
chel.work()
chel.study()
chel.play()
print(Teenager.mro())
