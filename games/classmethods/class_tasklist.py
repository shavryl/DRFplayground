

class Adder(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.data = dict()

    def __add__(self, other):
        return self.add()

    def add(self):
        return 'not implemented'


class ListAdder(Adder):

    def add(self):
        return self.x + self.y


class DictAdder(Adder):

    def add(self):

        self.data['x'] = self.x
        self.data['y'] = self.y

        return self.data
