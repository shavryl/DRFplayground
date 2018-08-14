

class Person:

    def __init__(self, name, age, pay, job):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def last_name(self):
        return self.name.split()[-1]

    def give_rise(self, percent):
        self.pay *= (1.0 + percent)


if __name__ == '__main__':
    bob = Person('Bob Smith', 45, 35000, 'developer')
    sue = Person('Sue Jones', 18, 25000, 'hardware')
    print(bob.name, sue.pay)
