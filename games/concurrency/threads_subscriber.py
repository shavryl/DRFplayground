import threading, time
from games.concurrency.threads_producer import Publisher


class Subscriber(threading.Thread):

    def __init__(self, integers, condition):
        self.integers = integers
        self.condition = condition
        threading.Thread.__init__(self)

    def run(self):
        while True:
            self.condition.acquire()
            print('Condition acquired by Consumer: {}'.format(self.name))
            while True:
                if self.integers:
                    integer = self.integers.pop()
                    print('{} Popped from list by Consumer: {}'.format(integer, self.name))
                    break
                print('Condition Wait by {}'.format(self.name))
                self.condition.wait()
            print('Consumer {} Releasing Condition'.format(self.name))
            self.condition.release()


def main():
    integers = []
    condition = threading.Condition()

    pub1 = Publisher(integers, condition)
    pub1.start()

    sub1 = Subscriber(integers, condition)
    sub2 = Subscriber(integers, condition)
    sub1.start()
    sub2.start()

    pub1.join()
    sub1.join()
    sub2.join()

main()
