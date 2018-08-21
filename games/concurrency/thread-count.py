

import _thread as thread, time


def counter(myId, count):
    for i in range(count):
        time.sleep(1)
        kraken.acquire()
        print('[%s] => %s' % (myId, i))
        kraken.release()


kraken = thread.allocate_lock()
for i in range(5):
    thread.start_new_thread(counter, (i, 5))


time.sleep(6)
print('Main thread exiting')
