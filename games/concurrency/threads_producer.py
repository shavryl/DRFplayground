import threading, random, time


class Publisher(threading.Thread):

    def __init__(self, integers, condition):
        self.condition = condition
        self.integers = integers
        threading.Thread.__init__(self)

    def run(self):
        while True:
            integer = random.randint(0, 1000)
            self.condition.aquire()
            print('Condition aquired by Publisher: {}'.format(self.name))
            self.integers.append(integer)
            self.condition.notify()
            print('Condition Released by Publisher: {}'.format(self.name))
            self.condition.release()
            time.sleep(1)
