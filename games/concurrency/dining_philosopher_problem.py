import threading, time, random
from threading import RLock


class Philosopher(threading.Thread):

    def __init__(self, name, left_fork, right_fork):
        print('Philosopher has set down at the table')
        threading.Thread.__init__(self)
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        print('Philosopher: {} has started thinking'.format(threading.current_thread()))
        while True:
            time.sleep(random.randint(1, 100))
            print('Philosopher {} has finished thinking'.format(threading.current_thread()))
            self.left_fork.acquire()
            time.sleep(random.randint(1, 100))
            try:
                print('Philosopher {} has acquired left fork'.format(threading.current_thread()))
                self.right_fork.acquire()
                try:
                    print('Philosopher {} has acquired right fork,'\
                          ' currently eating'.format(threading.current_thread()))
                finally:
                    self.right_fork.release()
                    print('Philosopher {} has released right fork'.format(threading.current_thread()))
            finally:
                self.left_fork.release()
                print('Philosopher {} has released left fork'.format(threading.current_thread()))


left = RLock()
right = RLock()


def process():

    names = ['Kant', 'Aristotel', 'Fromm', 'Seneca', 'Socrates']

    philosophers = [Philosopher(names[i], left, right) for i in range(5)]
    for star in philosophers: star.start()

process()
