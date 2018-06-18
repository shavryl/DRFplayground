from games.classmethods.class_reference import Person, Manager
import shelve

bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)


db = shelve.open('pesondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()
