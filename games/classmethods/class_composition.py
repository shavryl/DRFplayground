from games.classmethods.class_reference import Person


class Manager(Person):

    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def give_raise(self, percent, bonus=.10):
        self.person.give_raise(percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)


class Department:

    def __init__(self, *args):
        self.members = list(args)

    def add_member(self, person):
        self.members.append(person)

    def give_raise(self, percent):
        for person in self.members:
            person.give_raise(percent)

    def show_all(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    tom = Manager('Tom Jones', 50000)

    development = Department(bob, sue)  # Embed objects in a composite
    development.add_member(tom)
    development.give_raise(.10)  # Runs embedded objects' giveRaise
    development.show_all()  # Runs embedded objects' __repr__
