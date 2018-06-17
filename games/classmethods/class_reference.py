from games.classmethods.classtools import AttrDisplay


class Person(AttrDisplay):

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))


class Manager(Person):

    def __init__(self, name, pay):
        Person.__init__(self, name, 'mrg', pay)

    def give_raise(self, percent, bonus=.1):
        Person.give_raise(self, percent + bonus)




if __name__ == '__main__':

    sue = Person('Sue Bartender', 'Taxi driver', 500)
    bob = Person('Bob Smith')
    tom = Manager('Tom Woodovski', 800)
    tom.give_raise(.1)

    print('--All three--')

    for obj in (bob, sue, tom):
        obj.give_raise(.10)
        print(obj)
