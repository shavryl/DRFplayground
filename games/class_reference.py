

class Person:

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))



if __name__ == '__main__':

    sue = Person('Sue Bartender', 'Taxi driver', 500)
    bob = Person('Bob Smith')
    print(bob.last_name(), bob.pay)
    print(sue.name, sue.give_raise(.15), sue.pay)

