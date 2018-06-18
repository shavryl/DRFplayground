

class NextClass:

    def printer(self, text):
        self.message = text
        print(self.message)


class Super:

    def method(self):
        print("I'm super method!")

    # Expected to be defined
    def delegate(self):
        self.action()


# Inherit method verbatim
class Inheritor(Super):
    pass


# Replace method completely
class Replacer(Super):

    def method(self):
        print('Replaced method')


# Extend method behavior
class Extender(Super):

    def method(self):
        print('Starting extending')
        Super.method(self)
        print('Ended extending')


# Fill in a required method
class Provider(Super):

    def action(self):
        print('In Provider.action!')




if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()
