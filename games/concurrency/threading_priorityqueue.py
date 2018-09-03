import threading, time, random
from queue import PriorityQueue


def my_subscriber(queue):
    while not queue.empty():
        item = queue.get()
        if item is None:
            break
        print('{} removed {} from the queue'.format(threading.current_thread(), item))
        queue.task_done()
        time.sleep(1)


my_queue = PriorityQueue()


def process():

    for i in range(5):
        my_queue.put(i, i)

    for i in range(5):
        my_queue.put(i, i)

    print('Queue populated')
    threads = []

    for i in range(2):
        thread = threading.Thread(target=my_subscriber, args=(my_queue,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

        print('Queue is empty')


process()
