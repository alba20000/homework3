class Employee:
    salary = 0

    def get_paid(self):
        pass


class Manager(Employee):
    def get_paid(self):
        self.salary += 100000
        return self.salary


class Worker(Employee):
    def get_paid(self):
        self.salary += 10000
        return self.salary


manager = Manager()
worker = Worker()
manager.get_paid()
worker.get_paid()
print(manager.salary)
print(worker.salary)
