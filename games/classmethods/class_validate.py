

class CardHolder:

    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def get_name(self):
        return self.__name

    def set_name(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value

    name = property(get_name, set_name)

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value < 0 or value > 150:
            raise ValueError('Invalid age')
        else:
            self.__age = value

    age = property(get_age, set_age)

    def get_acct(self):
        return self.__acct[:-3] + '***'

    def set_acct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:
            raise TypeError('Invalid acct number')
        else:
            self.__acct = value

    acct = property(get_acct, set_acct)

    def remain_get(self):
        return self.retireage - self.age

    remain = property(remain_get)
