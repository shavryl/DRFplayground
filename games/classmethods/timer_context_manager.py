from timeit import default_timer


class Timer:

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.timer = default_timer

    def __enter__(self):
        self.start = default_timer()
        return self

    def __exit__(self, *args):
        end = default_timer()
        self.elapsed_secs = end - self.start
        self.elapsed = self.elapsed_secs * 1000
        if self.verbose:
            print('elapsed time: %f ms' % self.elapsed)
