import threading, random, time
from games.concurrency.decorators import timeit
from threading import Thread, Lock


counter = 1
lock = Lock()


def worker_A():
    global counter
    lock.acquire()
    try:
        while counter < 1000:
            counter += 1
            print('Worker A is incrementing counter to {}'.format(counter))
            sleepTime = random.randint(0, 1)
            time.sleep(sleepTime)
    finally:
        lock.release()


def worker_B():
    global counter
    lock.acquire()
    try:
        while counter > -1000:
            counter -= 1
            print('Worker B is decrementing counter to {}'.format(counter))
            sleepTime = random.randint(0, 1)
            time.sleep(sleepTime)
    finally:
        lock.release()


@timeit
def main():
    thread1 = threading.Thread(target=worker_A)
    thread2 = threading.Thread(target=worker_B)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
