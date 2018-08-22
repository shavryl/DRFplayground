

import sys, _signal, time


def now():
    return time.asctime()


def on_signal(signum, stackframe):
    print('Got alarm', signum, 'at', now())


while True:
    print('Setting at', now())
    _signal.signal(_signal.SIGALRM, on_signal)
    _signal.alarm(13)
    _signal.pause()
